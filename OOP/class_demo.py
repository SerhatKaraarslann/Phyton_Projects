# Create a class with name Comment
# Comment class has the attribute username, text,likes, dislikes.
# Create a 5 different comments and print them with a loop.

class Comment:
    def __init__(self,username, text, likes, dislikes):
        self.username = username
        self.text = text
        self.likes = likes
        self.dislikes = dislikes
    

c1 = Comment("Serhat","I like Python",15,1)
c2 = Comment("Julia","That was an impressive course!",55,7)
c3 = Comment("Uras","I would like to learn more and more :)",121,3)
c4 = Comment("Nora","I hate computer science",3,43)
c5 = Comment("Isa","I wish i learned it when i was younger",76,9)

comments = [c1,c2,c3,c4,c5]

for comment in comments:
    print(f"{comment.username}  =>  {comment.text} " )
    print (f"Likes : {comment.likes} - Dislikes : {comment.dislikes}")


