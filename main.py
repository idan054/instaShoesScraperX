from color_printer import printGreen

from Examples.Gsheet import update_nxt_row
from Examples.instaFilter import insta_filter

if __name__ == '__main__':
    # for post in instaloader.Hashtag.from_name(L.context, 'cat').get_posts():
    users_min_followers = input("Insert the minimum followers size") or 2.5*1000  # K
    users_max_followers = input("Insert the maximum followers size") or 1000*1000  # K
    limit_per_session = input("limit per session?") or 3
    selected_user = input("""
Make sure you can get_similar_accounts from
Please select user with ABOVE followers then minimum""") or "stabilo"

    matched_users_dict = insta_filter(users_min_followers, users_max_followers,
                                      limit_per_session, selected_user)

    # matched_users_dict = {'topspeed.alain': {'followers': 2828, 'external_link': 'https://maps.app.goo.gl/jwDgwadqw5vp7kvj6', 'insta_link': 'https://instagram.com/topspeed.alain'}, 'brand_shoes_express': {'followers': 6135, 'external_link': 'http://www.patrickschoice.com/', 'insta_link': 'https://instagram.com/brand_shoes_express'}, 'top_shoes.il': {'followers': 10918, 'external_link': 'https://www.topshoesil.co.il/', 'insta_link': 'https://instagram.com/top_shoes.il'}, 'calebjonnson': {'followers': 6401, 'external_link': 'http://calebjohnsonphotography.com/', 'insta_link': 'https://instagram.com/calebjonnson'}, 'blauwblokkers.nl': {'followers': 4851, 'external_link': 'http://www.blauwblokkers.nl/', 'insta_link': 'https://instagram.com/blauwblokkers.nl'}, 'brity.nl': {'followers': 3231, 'external_link': 'https://brity.nl/', 'insta_link': 'https://instagram.com/brity.nl'}, 'buketparis': {'followers': 3625, 'external_link': 'https://buketparis.ru/', 'insta_link': 'https://instagram.com/buketparis'}}

    #     matched_users_dict \
    #         = {
    #   'carolinewolf_homedecor': {
    #     'followers': 84865,
    #     'external_link': 'https: //linkpad.bio/caroline.wolf',
    #     'insta_link': 'https: //instagram.com/carolinewolf_homedecor'
    #   },
    #   'sher_fitness': {
    #     'followers': 404619,
    #     'external_link': 'https: //m.youtube.com/watch?v=gXhMvmh20W4',
    #     'insta_link': 'https: //instagram.com/sher_fitness'
    #   },
    #   'oriaazran_': {
    #     'followers': 166658,
    #     'external_link': 'https: //oriaazran.com/',
    #     'insta_link': 'https: //instagram.com/oriaazran_'
    #   },
    #   'gaya_boutique_official': {
    #     'followers': 57269,
    #     'external_link': 'https: //gaya-boutique.co.il/',
    #     'insta_link': 'https: //instagram.com/gaya_boutique_official'
    #   },
    #   'nunii_fashion': {
    #     'followers': 53491,
    #     'external_link': 'https: //nuniifashion.com/',
    #     'insta_link': 'https: //instagram.com/nunii_fashion'
    #   },
    #   'oran_nave': {
    #     'followers': 41253,
    #     'external_link': 'https: //api.whatsapp.com/send?phone=972528877995',
    #     'insta_link': 'https: //instagram.com/oran_nave'
    #   },
    #   'melach_haaretz_shani': {
    #     'followers': 84135,
    #     'external_link': 'http: //www.melach-haaretz.co.il/',
    #     'insta_link': 'https: //instagram.com/melach_haaretz_shani'
    #   },
    #   'odelboutique': {
    #     'followers': 26492,
    #     'external_link': 'http: //www.odelboutique.co.il/',
    #     'insta_link': 'https: //instagram.com/odelboutique'
    #   },
    #   'natalydadon': {
    #     'followers': 752205,
    #     'external_link': 'https: //www.queensclub.co.il/',
    #     'insta_link': 'https: //instagram.com/natalydadon'
    #   },
    #   'galita_fashion': {
    #     'followers': 262075,
    #     'external_link': 'https: //www.galita-fashion.co.il/',
    #     'insta_link': 'https: //instagram.com/galita_fashion'
    #   },
    #   'galita_fashion': {
    #     'followers': 262075,
    #     'external_link': 'https: //www.galita-fashion.co.il/',
    #     'insta_link': 'https: //instagram.com/galita_fashion'
    #   }
    # }

    printGreen("Start part B - GSheet update")

    usernames_list = list(matched_users_dict.keys())
    for username in usernames_list:
      ref = matched_users_dict[username] # dict reference
      # print(ref["followers"]//1000)
      # print(ref["external_link"])
      # print(ref["insta_link"])

      update_nxt_row(
        username,
        [
        [username, ref["followers"]//1000, ref["external_link"], ref["insta_link"]] # One Row
      ])
      # break

    print("GSheet Updated!")

    # update_nxt_row([
    #     ["Row 1", "Row 1"],
    #     ["Row 2", "Row 2"]
    # ])