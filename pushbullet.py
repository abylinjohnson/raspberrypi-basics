from pushbullet import Pushbullet

pb = Pushbullet('Auth token')
push = pb.push_note("Good Morning","Have a nice day")

