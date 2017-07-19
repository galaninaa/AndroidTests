Header = {'id':'com.talkatone.android:id/toolbar_title', 'xpath':'//android.widgetTextView[@resource-id="com.talkatone.android:id/toolbar_title"]'}

AccountData = {'id':'com.talkatone.android:id/settingsAccountView', 'xpath':'//android.widget.RelativeLayout[@resource-id="com.talkatone.android:id/settingsAccountView"]'}

AccountName = {'id':'com.talkatone.android:id/itemAccountNameTextView', 'xpath':'//android.widget.TextView[@resource-id="com.talkatone.android:id/itemAccountNameTextView"]'}

AccountPhone = {'id':'com.talkatone.android:id/itemAccountPhoneTextView', 'xpath':'//android.widget.TextView[@resource-id="com.talkatone.android:id/itemAccountPhoneTextView"]'}

AccountEmail = {'id':'com.talkatone.android:id/itemAccountEmailTextView', 'xpath':'//android.widget.TextView[@resource-id="com.talkatone.android:id/itemAccountEmailTextView"]'}

BurnNumberButton = {'id':'com.talkatone.android:id/burn_number', 'xpath':'//android.widget.ImageView[@resource-id="com.talkatone.android:id/burn_number"]'}

ShareNumberButton = {'id':'com.talkatone.android:id/share_number', 'xpath':'//android.widget.ImageView[@resource-id="com.talkatone.android:id/share_number"]'}

SettingsScrollViewContainer = {'id': 'com.talkatone.android:id/settingsScrollContainer', 'xpath':'//android.widget.TextView[@resource-id="com.talkatone.android:id/settingsScrollContainer"]'}

MenuItems = ['Get a New Number','Credits','Remove Ads', 'International Calls', 'Notifications & Sounds', 'Voicemail Greeting', 'Texting', 'Passcode',	'Blocked numbers', 'Miscellaneous', 'Quit Talkatone']

SmallMenuItems = ['For international calls', 'Active','Unlimited calls to select countries']

PaidCredits = {'id':'com.talkatone.android:id/paid_credits_text', 'xpath':'//android.widget.TextView[@resource-id="com.talkatone.android:id/paid_credits_text"]'}
#Only if Paid Credits text = 0.00
BuyCredits = {'id':'com.talkatone.android:id/buy_credits_text', 'xpath':'//android.widget.TextView[@resource-id="com.talkatone.android:id/buy_credits_text"]'}

RemoveAdsSwitch = {'id':'com.talkatone.android:id/switchWidget', 'xpath':'//android.widget.TextView[@resource-id="com.talkatone.android:id/switchWidget"]'}

IternationalCallsSubState = {'id':'com.talkatone.android:id/subs_state', 'xpath':'//android.widget.TextView[@resource-id="com.talkatone.android:id/subs_state"]'}

IternationalCallsSubStateMore = {'id':'com.talkatone.android:id/more', 'xpath':'//android.widget.TextView[@resource-id="com.talkatone.android:id/more"]'}

ContactUs = {'id':'', 'xpath':'//android.widget.TextView[@text="Need help with Talkatone? \n Contact us"]'}

def giveAllSettingsPath(MenuItems):
    all={}
    for allElement in MenuItems:
        all[allElement]='//android.widget.TextView[@text="'+allElement+'"]'
    return all

