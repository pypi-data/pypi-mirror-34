import re

from pynga.default_config import HOST
from pynga.forum import Forum, SubForum
from pynga.post import Post
from pynga.session import Session
from pynga.thread import Thread
from pynga.user import User
from .__version__ import __version__  # noqa: F401


class NGA(object):
    """NGA 基础类.

    Parameters
    --------
    authentication: dict
        登陆信息, 支持的 key 包括 uid, username, cid.
        其中 cid 为必须的 key, uid 和 username 至少需要指定一个.
    max_retries: int
        请求最多重试的次数. 默认: 5.
    """

    def __init__(self, authentication=None, max_retries=5):
        self.session = Session(authentication, max_retries)
        self._set_current_user()

    def _set_current_user(self):
        authentication = self._get_current_user_info()
        self.current_user = self.User(
            uid=authentication['uid'],
            username=authentication['username']
        )

    def _get_current_user_info(self):
        text = self.session.get_text(f'{HOST}')

        # extract uid
        uid = re.findall('__CURRENT_UID = parseInt\(\'([0-9]*)\',10\)', text)
        assert len(uid) == 1
        uid = int(uid[0]) if uid[0] else None

        # extract username
        username = re.findall('__CURRENT_UNAME = \'([\s\S]*?)\'', text)
        assert len(username) == 1
        username = username[0] if username[0] else None

        return {'uid': uid, 'username': username}

    def User(self, uid=None, username=None):
        """定义一个 NGA 用户.

        用户的 uid 和 username 至少需要指定一个, 否则是匿名用户.

        Parameters
        --------
        uid: int
            用户的 UID.
        username: str
            用户的用户名. 默认: None.

        Returns
        --------
        :class:`User <pynga.user.User>`
            定义的用户对象.
        """
        return User(uid=uid, username=username, session=self.session)

    def Post(self, pid):
        """定义一个回复.

        Parameters
        --------
        pid: int
            回复的 PID.

        Returns
        --------
        :class:`Post <pynga.post.Post>`
            定义的回复对象.
        """
        return Post(pid, session=self.session)

    def Thread(self, tid, *args, **kwargs):
        """定义一个帖子.

        Parameters
        --------
        tid: int
            帖子的 TID.

        Returns
        --------
        :class:`Thread <pynga.thread.Thread>`
            定义的帖子对象.
        """
        return Thread(tid, session=self.session, *args, **kwargs)

    def Forum(self, fid, page_limit=20):
        """定义一个版面.

        Parameters
        --------
        fid: int
            版面的 FID.
        page_limit: int
            最大页面数量. 默认: 20.

        Returns
        --------
        :class:`Forum <pynga.forum.Forum>`
            定义的版面对象.
        """
        return Forum(fid, session=self.session, page_limit=page_limit)

    def SubForum(self, stid):
        """定义一个合集.

        Parameters
        --------
        stid: int
            合集的 STID.

        Returns
        --------
        :class:`SubForum <pynga.forum.SubForum>`
            定义的合集对象.
        """
        return SubForum(stid, session=self.session)
