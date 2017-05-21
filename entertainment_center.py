# -*- coding: UTF-8 -*-

import media
import fresh_tomatoes

#创建一个电影实例
kill_zone = media.Movie('Kill Zone',
						'Chinese Kong Fu',
						'http://p9.qhmsg.com/t01dbac23bf78cce62a.jpg',
						'https://www.youtube.com/watch?v=ZWOmy3s4a5Y')

#创建一个电影实例
kill_zone_2 = media.Movie('Kill Zone 2',
						'Chinese Kong Fu',
						'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1495367381454&di=c5a185d34d888661f58a36e38a9bda09&imgtype=0&src=http%3A%2F%2Fch.bonafilm.cn%2Fupload%2FPicture%2F2013%2F20150922035140.jpg',
						'https://www.youtube.com/watch?v=GXh0zf2Qbbc')

movies = [kill_zone,kill_zone_2]#fresh_tomatoes中的输入是一个又多个电影实例组成的列表

fresh_tomatoes.open_movies_page(movies)#调用fresh_tomatoes中的open_movies_page方法，生成电影网页