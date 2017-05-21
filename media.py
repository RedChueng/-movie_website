# _*_ coding:UTF-8 _*_

import webbrowser

class Movie():
	""" 我最喜欢的电影"""

	# VALID_RATINGS = ['G','PG','PG-13','R']

	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):#定义实例变量
		self.title = movie_title #电影标题
		self.storyline = movie_storyline #电影情节
		self.poster_image_url = poster_image #电影宣传图
		self.trailer_youtube_url = trailer_youtube #电影预告片YouTube地址

	def show_trailer(self):#实例方法，播放预告片
		webbrowser.open(self.trailer_youtube_url)