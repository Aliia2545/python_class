# class MyProfile:
#     def __init__(self, user_name, profile_photo, nikname, description, phone_number, email, photo = None):
#         self.__user_name = user_name
#         self.__profile_photo = profile_photo
#         self.__nikname = nikname
#         self.__description = description
#         self.__phone_number = phone_number
#         self.__email = email
#         self.__photo = photo
#
#     def __str__(self):
#         return f"name: {self.__user_name}\t{self.__profile_photo}\n \nnik name: {self.__nikname}\n \nAbout me: \n{self.__description}\n \n#{self.__phone_number} | {self.__email}\n \nPublications: {self.__photo}"
#
#
# user1 = MyProfile(user_name="alex23", profile_photo="img1.jpg", nikname="alxx", description="Football player\nTraveler",
#                   phone_number="0770223365", email="alex.ua@email.com", photo ="img2.jpg")
#
# print(user1)


class SocialNetworks:
    def __init__(self, name, founder, was_founded, amount_of_users, agreement):
        self.__name = name
        self.__founder = founder
        self.__was_founded = was_founded
        self.__amount_of_users = amount_of_users
        self.__agreement = agreement

    def __str__(self):
        return f"Name of the Social Media: {self.__name}\nFounder is {self.__founder}\nWas created: {self.__was_founded}\nHow many people use this social network: {self.__amount_of_users}\n \n{self.__agreement}"
social1 = SocialNetworks(name='Instagram', founder='Кевин Систром и Майк Кригер', was_founded='6 октября 2010 года', amount_of_users='1,1 млрд', agreement='''Basic Terms
1.You must be 13 years or older to use this site.
2.You may not post nude, partially nude, or sexually suggestive photos.
3.You are responsible for any activity that occurs under your screen name.
4.You are responsible for keeping your password secure.
5.You must not abuse, harass, threaten, impersonate or intimidate other Instagram users.
6.You may not use the Instagram service for any illegal or unauthorized purpose. International users agree to comply with all local laws regarding online conduct and acceptable content.
7.You are solely responsible for your conduct and any data, text, information, screen names, graphics, photos, profiles, audio and video clips, links ("Content") that you submit, post, and display on the Instagram service.
8.You must not modify, adapt or hack Instagram or modify another website so as to falsely imply that it is associated with Instagram.
9.You must not access Instagram's private API by any other means other than the Instagram application itself.
10.You must not crawl, scrape, or otherwise cache any content from Instagram including but not limited to user profiles and photos.''')

print(social1)
