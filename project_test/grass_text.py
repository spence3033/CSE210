import pyray
from files.actor import Actor
from files.color import Color
from files.video_service import VideoService

grass = Actor()
grass._color = Color(0, 255, 0)

video = VideoService()

video.open_window()
video.draw_actor(grass)
