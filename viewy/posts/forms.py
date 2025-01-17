from django import forms
from .models import Posts, Videos
from accounts.models import FreezeNotification
from django.core.exceptions import ValidationError
from moviepy.editor import VideoFileClip
from django.core.files.uploadedfile import InMemoryUploadedFile, TemporaryUploadedFile
import tempfile
from multiupload.fields import MultiFileField

from moviepy.editor import VideoFileClip
from django.core.files.uploadedfile import InMemoryUploadedFile, TemporaryUploadedFile
import tempfile



class PostForm(forms.ModelForm):
    title = forms.CharField(label='タイトル', widget=forms.TextInput(attrs={'placeholder': 'タイトル（最大30字）'}))
    hashtag1 = forms.CharField(required=False, label='ハッシュタグ１', widget=forms.TextInput(attrs={'placeholder': '（最大20字）'}), error_messages={'max_length': "ハッシュタグは最大20字までです。",})
    hashtag2 = forms.CharField(required=False, label='ハッシュタグ２', widget=forms.TextInput(attrs={'placeholder': ''}), error_messages={'max_length': "ハッシュタグは最大20字までです。",})
    hashtag3 = forms.CharField(required=False, label='ハッシュタグ３', widget=forms.TextInput(attrs={'placeholder': ''}), error_messages={'max_length': "ハッシュタグは最大20字までです。",})
    caption = forms.CharField(required=False, label='説明欄', widget=forms.Textarea(attrs={'placeholder': 'キャプション（最大100字）'}))
    url = forms.URLField(required=False, widget=forms.TextInput(attrs={'placeholder': 'URL'}), error_messages={'invalid': '有効なURLを入力してください。',})
    scheduled_post_time = forms.DateTimeField(
        required=False,
        widget=forms.DateTimeInput(
            format='%Y-%m-%dT%H:%M',  # HTML5 datetime-local input format
            attrs={
                'type': 'datetime-local',  # specifying the input type to be datetime-local
                'placeholder': '公開日時'
            }),
        input_formats=['%Y-%m-%dT%H:%M'],  # Expected input format
        error_messages={
            'invalid': '有効な日付と時刻を入力してください。'
        }
    )

    class Meta:
        model = Posts
        fields = ['title', 'hashtag1', 'hashtag2', 'hashtag3', 'caption', 'url']
        
    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        caption = cleaned_data.get('caption')
        
        # タイトルとキャプションの内容が重複する場合はエラー
        if title == caption:
            raise ValidationError("タイトルとキャプションの内容は重複できません。")
        
        # タイトルが2文字以下の場合はエラー
        if len(title) < 2:
            raise ValidationError("タイトルは2文字以上で入力してください。")
        
        return cleaned_data

ALLOWED_EXTENSIONS = ['jpg', 'jpeg', 'png', 'gif']
    

class VisualForm(forms.Form):
    visuals = MultiFileField(
        min_num=1, 
        max_num=31, 
        max_file_size=1024*1024*5,  # 5MBを超えるサイズはエラー
        label="画像",
    )
    
    def clean_visuals(self):
        visuals = self.cleaned_data.get('visuals')

        if visuals:
            for visual in visuals:
                # 5MBを超えるサイズはエラー
                if visual.size > 5 * 1024 * 1024:
                    print("File too large!")
                    raise ValidationError("5MBを超える画像は投稿できません")
                
                # ファイルのMIMEタイプをチェック
                main_type = visual.content_type.split('/')[0]
                if not main_type == 'image':
                    print("Not an image!")
                    raise ValidationError("画像ファイルを選択してください。")

        return visuals


    
    
class VideoForm(forms.Form):
    video = forms.FileField(
        label="動画",
        widget=forms.ClearableFileInput(attrs={'accept': 'video/*'}),
    )

    def clean_video(self):
        video = self.cleaned_data.get('video')

        # ファイルサイズのチェック
        if video.size > 200 * 1024 * 1024:  # 200MBを超えるサイズはエラー
            raise ValidationError("200MB以上の動画は投稿できません。")

        # ファイルのMIMEタイプをチェック
        main_type = video.content_type.split('/')[0]
        if not main_type == 'video':
            raise ValidationError("動画ファイルを選択してください。")

        # 動画の長さをチェック
        if isinstance(video, InMemoryUploadedFile):
            tmp_file = tempfile.NamedTemporaryFile(delete=False)
            for chunk in video.chunks():
                tmp_file.write(chunk)
            tmp_file.close()
            clip_path = tmp_file.name
        elif isinstance(video, TemporaryUploadedFile):
            clip_path = video.temporary_file_path()

        with VideoFileClip(clip_path) as clip:
            if clip.duration > 120:  # 動画が120秒より長い場合
                raise ValidationError('２分以上の動画は投稿できません。')
                
        if isinstance(video, InMemoryUploadedFile):
            tmp_file.close()  # テンポラリファイルをクローズ

        return video
    
    
class SearchForm(forms.Form):
    query = forms.CharField(
        max_length=100, 
        widget=forms.TextInput(attrs={'placeholder': '検索する', 'id': 'search'}),
        label=False,  # ラベルを非表示にする
        )
    
# 凍結通知申請フォーム
class FreezeNotificationForm(forms.ModelForm):
    class Meta:
        model = FreezeNotification
        fields = ['new_url']
        widgets = {
            'new_url': forms.URLInput(attrs={'placeholder': 'URLを入力'}),
        }