from model_utils import Choices
from django.utils.translation import gettext_lazy as _

USER_TYPE_CHOICES = Choices(
    (0, _('GUEST')),
    (1, _('BRONZE')),
    (2, _('SILVER')),
    (3, _('GOLD')),
    (4, _('PLATINUM')),
    (5, _('DIAMOND')),
    (6, _('LEGEND')),
    (7, _('STAFF')),
    (8, _('PRO_STAFF')),
    (9, _('SUPER_STAFF')),
    (10, _('MASTER')),
)

MEMBER_TYPE_CHOICES = Choices(
    (1, _('BRONZE')),
    (2, _('SILVER')),
    (3, _('GOLD')),
    (4, _('PLATINUM')),
    (5, _('DIAMOND')),
    (6, _('LEGEND')),
)

STAFF_TYPE_CHOICES = Choices(
    (7, _('STAFF')),
    (8, _('PRO_STAFF')),
    (9, _('SUPER_STAFF')),
    (10, _('MASTER')),
)

VIEW_MODE_CHOICES = Choices(
    ('LIST_TYPE', _('LIST_TYPE')),
    ('ALBUM_TYPE', _('ALBUM_TYPE')),
    ('CARD_TYPE', _('CARD_TYPE')),
)

LINK_SHARE_CHOICES = Choices(
    ('LINK', _('LINK')),
    ('FACEBOOK', _('FACEBOOK')),
    ('TWITTER', _('TWITTER')),
    ('TELEGRAM', _('TELEGRAM')),
)

BOARD_GROUP_TYPE_CHOICES = Choices(
    ('NORMAL', _('NORMAL')),
    ('DEFAULT', _('DEFAULT')),
)

BOARD_TYPE_CHOICES = Choices(
    ('NORMAL', _('NORMAL')),
    ('ALL', _('ALL')),
    ('NOTICE', _('NOTICE')),
    ('EVENT', _('EVENT')),
    ('GALLERY', _('GALLERY')),
    ('VIDEO', _('VIDEO')),
)

REPORT_TYPE_CHOICES = Choices(
    ('SPAM', _('스팸 홍보/도배글 입니다.')),
    ('PORNOGRAPHY', _('음란물 입니다.')),
    ('ILLEGAL', _('불법정보를 포함하고 있습니다.')),
    ('HARMFUL', _('청소년에게 유해한 내용입니다.')),
    ('ABUSE', _('욕설, 비방, 차별, 혐오 표현입니다.')),
    ('PRIVACY', _('개인정보 노출 게시물입니다.')),
    ('ETX', _('기타')),
)
