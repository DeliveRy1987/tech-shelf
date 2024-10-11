from django.db import models
from .consts import MAX_RATE

RATE_CHOICES = [(x, str(x)) for x in range(0, MAX_RATE + 1)]   #レビューの数を決めるよう
# class SampleModel(models.Model):
#     title = models.CharField(max_length=100)
#     number = models.IntegerField()

CATEGORY = (
    ('business', 'ビジネス'),('life','生活'),('Python','Python'),('Django','Django'),('Ruby','Ruby'),('Rails','Rails'),('Java','Java'),('Spring','Spring'),('HTML/CSS','HTML/CSS'),('JavaScript','JavaScript'),('Vue.js','Vue.js'),('React','React'),('Angular','Angular'),('PHP','PHP'),('Laravel','Laravel'),('C++','C++'),('C#','C#'),('Unity','Unity'),('Swift','Swift'),('Kotlin','Kotlin'),('Go','Go'),('Rust','Rust'),('SQL','SQL'),('NoSQL','NoSQL'),
    ('other','その他')
    )
class Book(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    thumbnail = models.ImageField(null=True, blank=True)
    category = models.CharField(max_length=100, choices=CATEGORY)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    price = models.IntegerField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    
    def __str__(self):
        return self.title                                             #self.xxxを返すと、そのxxxがデータのタイトルとして表示される
    
    
    
class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)     #on deleteはそのモデルが削除されたときの挙動を＝で指定する。cascadeは親が削除されたら子も削除する
    title = models.CharField(max_length=100)
    text = models.TextField()
    rate = models.IntegerField(choices=RATE_CHOICES)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    

class Question(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=700)
    email = models.EmailField(default='example@example.com')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    

#お気に入り機能
class FavoriteBook(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'book']  # 1つの投稿に対して1ユーザー1お気に入り制約

    def __str__(self):
        return f"{self.user} - {self.book.title}"