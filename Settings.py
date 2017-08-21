import  SoundsAndNotifications
import Miscellaneous

header = {'id': 'com.talkatone.android:id/toolbar_title',
          'xpath': '//android.widgetTextView[@resource-id="com.talkatone.android:id/toolbar_title"]'}

account_data = {'id': 'com.talkatone.android:id/settingsAccountView',
               'xpath': '//android.widget.RelativeLayout[@resource-id="com.talkatone.android:id/settingsAccountView"]'}

account_name = {'id': 'com.talkatone.android:id/itemAccountNameTextView',
               'xpath': '//android.widget.TextView[@resource-id="com.talkatone.android:id/itemAccountNameTextView"]'}

account_phone = {'id': 'com.talkatone.android:id/itemAccountPhoneTextView',
                'xpath': '//android.widget.TextView[@resource-id="com.talkatone.android:id/itemAccountPhoneTextView"]'}

account_email = {'id': 'com.talkatone.android:id/itemAccountEmailTextView',
                'xpath': '//android.widget.TextView[@resource-id="com.talkatone.android:id/itemAccountEmailTextView"]'}

burn_number_button = {'id': 'com.talkatone.android:id/burn_number',
                    'xpath': '//android.widget.ImageView[@resource-id="com.talkatone.android:id/burn_number"]'}

share_number_button = {'id': 'com.talkatone.android:id/share_number',
                     'xpath': '//android.widget.ImageView[@resource-id="com.talkatone.android:id/share_number"]'}

settings_scroll_view_container = {'id': 'com.talkatone.android:id/settingsScrollContainer',
                               'xpath': '//android.widget.TextView[@resource-id="com.talkatone.android:id/settingsScrollContainer"]'}

menu_items = ['Get a New Number', 'Credits', 'Remove Ads', 'International Calls', 'Notifications & Sounds',
             'Voicemail Greeting', 'Texting', 'Passcode', 'Blocked numbers', 'Miscellaneous', 'Quit Talkatone']

small_menu_items_active_no_ads = ['For international calls', 'Active', 'Unlimited calls to select countries']

small_menu_items = ['For international calls', 'Hide all ads for $1.99/month', 'Unlimited calls to select countries']

paid_credits = {'id': 'com.talkatone.android:id/paid_credits_text',
               'xpath': '//android.widget.TextView[@resource-id="com.talkatone.android:id/paid_credits_text"]'}
# Only if Paid Credits text = 0.00
buy_credits = {'id': 'com.talkatone.android:id/buy_credits_text',
              'xpath': '//android.widget.TextView[@resource-id="com.talkatone.android:id/buy_credits_text"]'}

remove_ads_switch = {'id': 'com.talkatone.android:id/switchWidget',
                   'xpath': '//android.widget.TextView[@resource-id="com.talkatone.android:id/switchWidget"]'}

iternational_calls_sub_state = {'id': 'com.talkatone.android:id/subs_state',
                             'xpath': '//android.widget.TextView[@resource-id="com.talkatone.android:id/subs_state"]'}

iternational_calls_sub_state_more = {'id': 'com.talkatone.android:id/more',
                                 'xpath': '//android.widget.TextView[@resource-id="com.talkatone.android:id/more"]'}

contact_us = {'id': '', 'xpath': '//android.widget.TextView[@text="Need help with Talkatone? \n Contact us"]'}



