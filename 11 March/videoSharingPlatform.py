class IdGenerator:
    def __init__(self):
        self._limit = 1000
        self._id_stack = []
        self._last_stack_position = -1
    
    def refill_stack(self):
        self._id_stack.extend(range(self._last_stack_position + self._limit, self._last_stack_position, -1))
        self._last_stack_position += self._limit

    def get_id(self) -> int:
        if len(self._id_stack) == 0:
            self.refill_stack()
        return self._id_stack.pop()

    def free_id(self, removed_id: int):
        self._id_stack.append(removed_id)

class VideoObj:
    def __init__(self, video: str):
        self.video = video
        self.like = 0
        self.dislike = 0
        self.views = 0


class VideoSharingPlatform:
    def __init__(self):
        self.video_map = {}
        self.IdGenerator = IdGenerator()

    def _get_video(self, video_id: int):
        if video_id not in self.video_map: 
            raise Exception(f'Video with this videoId: {video_id} not found.')
        return self.video_map[video_id]

    def _remove_video(self, video_id: int):
        if video_id not in self.video_map: 
            raise Exception(f'Video with this videoId: {video_id} not found.')
        self.video_map.pop(video_id)
        self.IdGenerator.free_id(video_id)
         
    
    def _add_video(self, video_id: int, video: str):
        self.video_map[video_id] = VideoObj(video)

    def upload(self, video: str) -> int:
        new_video_id = self.IdGenerator.get_id()
        self._add_video(new_video_id, video)
        return new_video_id
    
    def remove(self, video_id: int):
        self._remove_video(video_id)
    
    def watch(self, video_id: int, start_min: int, end_min: int)-> str:
        try:
            video = self._get_video(video_id)
            video.views += 1
            l, r = max(0, start_min - 1), min(end_min, len(video.video))
            return video.video[l:r]
        except:
            return -1


    def like(self, video_id: int):
        try:
            self._get_video(video_id).like += 1
        except: 
            pass

    def dislike(self, video_id: int):
        try:
            self._get_video(video_id).dislike += 1
        except:
            pass
    
    def getLikesAndDislikes(self, video_id: int) -> list[int, int]:
        try:
            video = self._get_video(video_id)
            return [video.like, video.dislike]
        except:
            return [-1]
    
    def getViews(self, video_id: int) -> int:
        try:
            video = self._get_video(video_id)
            return video.views
        except:
            return -1


    
platform = VideoSharingPlatform()

assert platform.upload('abc') == 0

video1 = platform.upload('abcd')

assert platform.watch(video1, 1, 2) == 'ab'

assert platform.getViews(video1) == 1

assert platform.getViews(-1) == -1

platform.remove(video1)

video2 = platform.upload('1234')
print(video1, video2)

assert video1 == video2

print(platform.remove(0), platform.watch(0, 0, 1), platform.like(0), platform.dislike(0), platform.getLikesAndDislikes(0), platform.getViews(0))

