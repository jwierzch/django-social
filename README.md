implementation of the walkthrough from: https://realpython.com/django-social-network-1/
Customized for my own curiosity as well as I had a big issue with the password reset done template not working, resovled via: #https://stackoverflow.com/questions/66406530/keep-getting-this-error-of-reverse-for-password-reset-confirm-not-found-pass
added ability to upload images for sharing

TODO
pin pics to profiles, ability to manage own gallery

#instructions
git clone
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver


also useful
python manage.py changepassword username


other useful things
https://www.devhandbook.com/django/user-profile/
https://stackoverflow.com/questions/23922289/django-pil-save-thumbnail-version-right-when-image-is-uploaded

had to switch from create to get or crate in the signal
Profile.objects.get_or_create(user=instance)