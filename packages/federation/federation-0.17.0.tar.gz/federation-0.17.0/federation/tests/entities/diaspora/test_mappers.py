from datetime import datetime
from lxml import etree
from unittest.mock import patch, Mock

import pytest

from federation.entities.base import (
    Comment, Post, Reaction, Relationship, Profile, Retraction, Image,
    Follow, Share)
from federation.entities.diaspora.entities import (
    DiasporaPost, DiasporaComment, DiasporaLike, DiasporaRequest,
    DiasporaProfile, DiasporaRetraction, DiasporaContact, DiasporaReshare)
from federation.entities.diaspora.mappers import (
    message_to_objects, get_outbound_entity, check_sender_and_entity_handle_match)
from federation.tests.fixtures.payloads import (
    DIASPORA_POST_SIMPLE, DIASPORA_POST_COMMENT, DIASPORA_POST_LIKE,
    DIASPORA_REQUEST, DIASPORA_PROFILE, DIASPORA_POST_INVALID, DIASPORA_RETRACTION,
    DIASPORA_POST_WITH_PHOTOS, DIASPORA_POST_LEGACY_TIMESTAMP, DIASPORA_POST_LEGACY, DIASPORA_CONTACT,
    DIASPORA_LEGACY_REQUEST_RETRACTION, DIASPORA_POST_WITH_PHOTOS_2, DIASPORA_PROFILE_EMPTY_TAGS, DIASPORA_RESHARE,
    DIASPORA_RESHARE_WITH_EXTRA_PROPERTIES, DIASPORA_RESHARE_LEGACY, DIASPORA_POST_SIMPLE_WITH_MENTION,
    DIASPORA_PROFILE_FIRST_NAME_ONLY)


def mock_fill(attributes):
    attributes["guid"] = "guidguidguidguidguid"
    return attributes


class TestDiasporaEntityMappersReceive:
    def test_message_to_objects_mentions_are_extracted(self):
        entities = message_to_objects(DIASPORA_POST_SIMPLE_WITH_MENTION, "alice@alice.diaspora.example.org")
        assert len(entities) == 1
        post = entities[0]
        assert post._mentions == {'diaspora://jaywink@jasonrobinson.me/profile/'}

    def test_message_to_objects_simple_post(self):
        entities = message_to_objects(DIASPORA_POST_SIMPLE, "alice@alice.diaspora.example.org")
        assert len(entities) == 1
        post = entities[0]
        assert isinstance(post, DiasporaPost)
        assert isinstance(post, Post)
        assert post.raw_content == "((status message))"
        assert post.guid == "((guidguidguidguidguidguidguid))"
        assert post.handle == "alice@alice.diaspora.example.org"
        assert post.public == False
        assert post.created_at == datetime(2011, 7, 20, 1, 36, 7)
        assert post.provider_display_name == "Socialhome"

    def test_message_to_objects_post_legacy(self):
        # This is the previous XML schema used before renewal of protocol
        entities = message_to_objects(DIASPORA_POST_LEGACY, "alice@alice.diaspora.example.org")
        assert len(entities) == 1
        post = entities[0]
        assert isinstance(post, DiasporaPost)
        assert isinstance(post, Post)
        assert post.raw_content == "((status message))"
        assert post.guid == "((guidguidguidguidguidguidguid))"
        assert post.handle == "alice@alice.diaspora.example.org"
        assert post.public is False
        assert post.created_at == datetime(2011, 7, 20, 1, 36, 7)
        assert post.provider_display_name == "Socialhome"

    def test_message_to_objects_legact_timestamp(self):
        entities = message_to_objects(DIASPORA_POST_LEGACY_TIMESTAMP, "alice@alice.diaspora.example.org")
        post = entities[0]
        assert post.created_at == datetime(2011, 7, 20, 1, 36, 7)

    def test_message_to_objects_post_with_photos(self):
        entities = message_to_objects(DIASPORA_POST_WITH_PHOTOS, "alice@alice.diaspora.example.org")
        assert len(entities) == 1
        post = entities[0]
        assert isinstance(post, DiasporaPost)
        photo = post._children[0]
        assert isinstance(photo, Image)
        assert photo.remote_path == "https://alice.diaspora.example.org/uploads/images/"
        assert photo.remote_name == "1234.jpg"
        assert photo.raw_content == ""
        assert photo.linked_type == "Post"
        assert photo.linked_guid == "((guidguidguidguidguidguidguid))"
        assert photo.height == 120
        assert photo.width == 120
        assert photo.guid == "((guidguidguidguidguidguidguif))"
        assert photo.handle == "alice@alice.diaspora.example.org"
        assert photo.public == False
        assert photo.created_at == datetime(2011, 7, 20, 1, 36, 7)

        entities = message_to_objects(DIASPORA_POST_WITH_PHOTOS_2, "xxxxxxxxxxxxxxx@diasp.org")
        assert len(entities) == 1
        post = entities[0]
        assert isinstance(post, DiasporaPost)
        photo = post._children[0]
        assert isinstance(photo, Image)

    @patch("federation.entities.diaspora.mappers.DiasporaComment._validate_signatures")
    def test_message_to_objects_comment(self, mock_validate):
        entities = message_to_objects(DIASPORA_POST_COMMENT, "alice@alice.diaspora.example.org",
                                      sender_key_fetcher=Mock())
        assert len(entities) == 1
        comment = entities[0]
        assert isinstance(comment, DiasporaComment)
        assert isinstance(comment, Comment)
        assert comment.target_guid == "((parent_guidparent_guidparent_guidparent_guid))"
        assert comment.guid == "((guidguidguidguidguidguid))"
        assert comment.handle == "alice@alice.diaspora.example.org"
        assert comment.participation == "comment"
        assert comment.raw_content == "((text))"
        assert comment.signature == "((signature))"
        assert comment._xml_tags == [
            "guid", "parent_guid", "text", "author",
        ]
        mock_validate.assert_called_once_with()

    @patch("federation.entities.diaspora.mappers.DiasporaLike._validate_signatures")
    def test_message_to_objects_like(self, mock_validate):
        entities = message_to_objects(DIASPORA_POST_LIKE, "alice@alice.diaspora.example.org", sender_key_fetcher=Mock())
        assert len(entities) == 1
        like = entities[0]
        assert isinstance(like, DiasporaLike)
        assert isinstance(like, Reaction)
        assert like.target_guid == "((parent_guidparent_guidparent_guidparent_guid))"
        assert like.guid == "((guidguidguidguidguidguid))"
        assert like.handle == "alice@alice.diaspora.example.org"
        assert like.participation == "reaction"
        assert like.reaction == "like"
        assert like.signature == "((signature))"
        assert like._xml_tags == [
            "parent_type", "guid", "parent_guid", "positive", "author",
        ]
        mock_validate.assert_called_once_with()

    def test_message_to_objects_request(self):
        entities = message_to_objects(DIASPORA_REQUEST, "bob@example.com")
        assert len(entities) == 2
        sharing = entities[0]
        assert isinstance(sharing, DiasporaRequest)
        assert isinstance(sharing, Relationship)
        following = entities[1]
        assert not isinstance(following, DiasporaRequest)
        assert isinstance(following, Relationship)
        assert sharing.handle == "bob@example.com"
        assert following.handle == "bob@example.com"
        assert sharing.target_handle == "alice@alice.diaspora.example.org"
        assert following.target_handle == "alice@alice.diaspora.example.org"
        assert sharing.relationship == "sharing"
        assert following.relationship == "following"

    @patch("federation.entities.diaspora.entities.DiasporaProfile.fill_extra_attributes", new=mock_fill)
    def test_message_to_objects_profile(self):
        entities = message_to_objects(DIASPORA_PROFILE, "bob@example.com")
        assert len(entities) == 1
        profile = entities[0]
        assert profile.handle == "bob@example.com"
        assert profile.name == "Bob Bobertson"
        assert profile.image_urls == {
            "large": "https://example.com/uploads/images/thumb_large_c833747578b5.jpg",
            "medium": "https://example.com/uploads/images/thumb_medium_c8b1aab04f3.jpg",
            "small": "https://example.com/uploads/images/thumb_small_c8b147578b5.jpg",
        }
        assert profile.gender == ""
        assert profile.raw_content == "A cool bio"
        assert profile.location == "Helsinki"
        assert profile.public == True
        assert profile.nsfw == False
        assert profile.tag_list == ["socialfederation", "federation"]

    @patch("federation.entities.diaspora.entities.DiasporaProfile.fill_extra_attributes", new=mock_fill)
    def test_message_to_objects_profile__first_name_only(self):
        entities = message_to_objects(DIASPORA_PROFILE_FIRST_NAME_ONLY, "bob@example.com")
        assert len(entities) == 1
        profile = entities[0]
        assert profile.name == "Bob"

    @patch("federation.entities.diaspora.entities.DiasporaProfile.fill_extra_attributes", new=mock_fill)
    def test_message_to_objects_profile_survives_empty_tag_string(self):
        entities = message_to_objects(DIASPORA_PROFILE_EMPTY_TAGS, "bob@example.com")
        assert len(entities) == 1

    def test_message_to_objects_retraction(self):
        entities = message_to_objects(DIASPORA_RETRACTION, "bob@example.com")
        assert len(entities) == 1
        entity = entities[0]
        assert isinstance(entity, Retraction)
        assert entity.handle == "bob@example.com"
        assert entity.target_guid == "x" * 16
        assert entity.entity_type == "Post"

    def test_message_to_objects_retraction_legacy_request(self):
        entities = message_to_objects(DIASPORA_LEGACY_REQUEST_RETRACTION, "jaywink@iliketoast.net",
                                      user=Mock(guid="swfeuihiwehuifhiwheiuf"))
        assert len(entities) == 1
        entity = entities[0]
        assert isinstance(entity, Retraction)
        assert entity.handle == "jaywink@iliketoast.net"
        assert entity.target_guid == "7ed1555bc6ae03db"
        assert entity.entity_type == "Profile"
        assert entity._receiving_guid == "swfeuihiwehuifhiwheiuf"

    def test_message_to_objects_contact(self):
        entities = message_to_objects(DIASPORA_CONTACT, "alice@example.com")
        assert len(entities) == 1
        entity = entities[0]
        assert isinstance(entity, DiasporaContact)
        assert entity.handle == "alice@example.com"
        assert entity.target_handle == "bob@example.org"
        assert entity.following is True

    def test_message_to_objects_reshare(self):
        entities = message_to_objects(DIASPORA_RESHARE, "alice@example.org")
        assert len(entities) == 1
        entity = entities[0]
        assert isinstance(entity, DiasporaReshare)
        assert entity.handle == "alice@example.org"
        assert entity.guid == "a0b53e5029f6013487753131731751e9"
        assert entity.provider_display_name == ""
        assert entity.target_handle == "bob@example.com"
        assert entity.target_guid == "a0b53bc029f6013487753131731751e9"
        assert entity.public is True
        assert entity.entity_type == "Post"
        assert entity.raw_content == ""

    def test_message_to_objects_reshare_legacy(self):
        entities = message_to_objects(DIASPORA_RESHARE_LEGACY, "alice@example.org")
        assert len(entities) == 1
        entity = entities[0]
        assert isinstance(entity, DiasporaReshare)
        assert entity.handle == "alice@example.org"
        assert entity.guid == "a0b53e5029f6013487753131731751e9"
        assert entity.provider_display_name == ""
        assert entity.target_handle == "bob@example.com"
        assert entity.target_guid == "a0b53bc029f6013487753131731751e9"
        assert entity.public is False
        assert entity.entity_type == "Post"

    def test_message_to_objects_reshare_extra_properties(self):
        entities = message_to_objects(DIASPORA_RESHARE_WITH_EXTRA_PROPERTIES, "alice@example.org")
        assert len(entities) == 1
        entity = entities[0]
        assert isinstance(entity, DiasporaReshare)
        assert entity.raw_content == "Important note here"
        assert entity.entity_type == "Comment"

    @patch("federation.entities.diaspora.mappers.logger.error")
    def test_invalid_entity_logs_an_error(self, mock_logger):
        entities = message_to_objects(DIASPORA_POST_INVALID, "alice@alice.diaspora.example.org")
        assert len(entities) == 0
        assert mock_logger.called

    def test_adds_source_protocol_to_entity(self):
        entities = message_to_objects(DIASPORA_POST_SIMPLE, "alice@alice.diaspora.example.org")
        assert entities[0]._source_protocol == "diaspora"

    @patch("federation.entities.diaspora.mappers.DiasporaComment._validate_signatures")
    def test_source_object(self, mock_validate):
        entities = message_to_objects(DIASPORA_POST_COMMENT, "alice@alice.diaspora.example.org",
                                      sender_key_fetcher=Mock())
        entity = entities[0]
        assert entity._source_object == etree.tostring(etree.fromstring(DIASPORA_POST_COMMENT))

    @patch("federation.entities.diaspora.mappers.DiasporaComment._validate_signatures")
    def test_element_to_objects_calls_sender_key_fetcher(self, mock_validate):
        mock_fetcher = Mock()
        message_to_objects(DIASPORA_POST_COMMENT, "alice@alice.diaspora.example.org", mock_fetcher)
        mock_fetcher.assert_called_once_with("alice@alice.diaspora.example.org")

    @patch("federation.entities.diaspora.mappers.DiasporaComment._validate_signatures")
    @patch("federation.entities.diaspora.mappers.retrieve_and_parse_profile")
    def test_element_to_objects_calls_retrieve_remote_profile(self, mock_retrieve, mock_validate):
        message_to_objects(DIASPORA_POST_COMMENT, "alice@alice.diaspora.example.org")
        mock_retrieve.assert_called_once_with("alice@alice.diaspora.example.org")

    @patch("federation.entities.diaspora.mappers.check_sender_and_entity_handle_match")
    def test_element_to_objects_verifies_handles_are_the_same(self, mock_check):
        message_to_objects(DIASPORA_POST_SIMPLE, "bob@example.org")
        mock_check.assert_called_once_with("bob@example.org", "alice@alice.diaspora.example.org")

    def test_element_to_objects_returns_no_entity_if_handles_are_different(self):
        entities = message_to_objects(DIASPORA_POST_SIMPLE, "bob@example.org")
        assert not entities


class TestGetOutboundEntity:
    def test_already_fine_entities_are_returned_as_is(self, private_key):
        entity = DiasporaPost()
        assert get_outbound_entity(entity, private_key) == entity
        entity = DiasporaLike()
        assert get_outbound_entity(entity, private_key) == entity
        entity = DiasporaComment()
        assert get_outbound_entity(entity, private_key) == entity
        entity = DiasporaRequest()
        assert get_outbound_entity(entity, private_key) == entity
        entity = DiasporaProfile()
        assert get_outbound_entity(entity, private_key) == entity
        entity = DiasporaContact()
        assert get_outbound_entity(entity, private_key) == entity
        entity = DiasporaReshare()
        assert get_outbound_entity(entity, private_key) == entity

    def test_post_is_converted_to_diasporapost(self, private_key):
        entity = Post()
        assert isinstance(get_outbound_entity(entity, private_key), DiasporaPost)

    def test_comment_is_converted_to_diasporacomment(self, private_key):
        entity = Comment()
        assert isinstance(get_outbound_entity(entity, private_key), DiasporaComment)

    def test_reaction_of_like_is_converted_to_diasporalike(self, private_key):
        entity = Reaction(reaction="like")
        assert isinstance(get_outbound_entity(entity, private_key), DiasporaLike)

    def test_relationship_of_sharing_or_following_is_converted_to_diasporarequest(self, private_key):
        entity = Relationship(relationship="sharing")
        assert isinstance(get_outbound_entity(entity, private_key), DiasporaRequest)
        entity = Relationship(relationship="following")
        assert isinstance(get_outbound_entity(entity, private_key), DiasporaRequest)

    def test_profile_is_converted_to_diasporaprofile(self, private_key):
        entity = Profile()
        assert isinstance(get_outbound_entity(entity, private_key), DiasporaProfile)

    def test_other_reaction_raises(self, private_key):
        entity = Reaction(reaction="foo")
        with pytest.raises(ValueError):
            get_outbound_entity(entity, private_key)

    def test_other_relation_raises(self, private_key):
        entity = Relationship(relationship="foo")
        with pytest.raises(ValueError):
            get_outbound_entity(entity, private_key)

    def test_retraction_is_converted_to_diasporaretraction(self, private_key):
        entity = Retraction()
        assert isinstance(get_outbound_entity(entity, private_key), DiasporaRetraction)

    def test_follow_is_converted_to_diasporacontact(self, private_key):
        entity = Follow()
        assert isinstance(get_outbound_entity(entity, private_key), DiasporaContact)

    def test_share_is_converted_to_diasporareshare(self, private_key):
        entity = Share()
        assert isinstance(get_outbound_entity(entity, private_key), DiasporaReshare)

    def test_signs_relayable_if_no_signature(self, private_key):
        entity = DiasporaComment()
        outbound = get_outbound_entity(entity, private_key)
        assert outbound.signature != ""

    def test_returns_entity_if_outbound_doc_on_entity(self, private_key):
        entity = Comment()
        entity.outbound_doc = "foobar"
        assert get_outbound_entity(entity, private_key) == entity


def test_check_sender_and_entity_handle_match():
    assert not check_sender_and_entity_handle_match("foo", "bar")
    assert check_sender_and_entity_handle_match("foo", "foo")
