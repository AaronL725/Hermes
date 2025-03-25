

  * 

[The Official "Ok, now I'm pissed" Thread](/thread/73546-the-official-ok-now-im-pissed-thread "Hello Everyone, 
 
Seeing the apparent lack of threads of this nature \(just kidding, but read on\) I have decided to set up a respectable...") 51 replies

[Historic Charts: NZ Official Cash Rate](/thread/20380-historic-charts-nz-official-cash-rate "Sep 14, 2005") 15 replies

[Is there an official exchange rate?!](/thread/11571-is-there-an-official-exchange-rate "Different brokers have different bid and ask prices for every cross or pair.  However, the bid and ask price is based on something...I am...") 14 replies

[Official forex time zone](/thread/9940-official-forex-time-zone "is there a standard forex time zone? do i follow gmt or NY time? i use 4 hour charts and sometimes the time is way off because of time zone...") 3 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/533099-udineea-official-thread/reply#reply)
  * Subscribe
  * [100](javascript:void\(0\);)

Attachments: UdineEA Official Thread

Tags: UdineEA Official Thread

#  [](/thread/533099-udineea-official-thread)UdineEA Official Thread 

  * 

  * [#1](/thread/533099-udineea-official-thread "Post Permalink")

  * First Post: Edited Sep 17, 2015 4:12pm  Mar 30, 2015 1:08am | Edited Sep 17, 2015 4:12pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

[update 17 Sep 2015]   
_**UdineEA forward test in demo account is discontinued since it doesn't have any kind of edge over the market, related Trade Explorer is removed.**_  
  
A new Trade Explorer is attached related to [this](http://www.forexfactory.com/showthread.php?p=8450202#post8450202) 'idea' on how to trade UdineEA in a different way.  
  
Hi All,  
I'd like to share with you a simple EA coded for 00 Levels thread opened by Udine, I prefer to open a separate thread so to not clutter original thread with post related to this EA, so please direct your questions related to this EA here instead of Udine's thread.  
  
**[Thread Rules]**  
_* No troll, no calling names, no flame are allowed in any form here. We are professional here and act as professional if we want to succeed in our quest._  
_* Inappropriate behaviours will be punished with permanent ban from the thread and reported to the site administrators._  
_* **EA is provided as is, there maybe several bugs that could damage seriously your account , so it's completely your decision and your risk to use it with real money**._  
_* I'll not share the source code (.mq4) for multiple reasons : mostly because there was a lot of work done to code it, I don't want to find it sold on some scammer site and lastly I'd like to have full control on its development and subsequent versions._  
_* There's no free lunch here, go and do your homework , STUDYING what's about Udine's strategy. This EA is meant as an helping hand but cannot substitute in any way trader's knowledge._  
_* Do not never ask me here (or by pm) for 'custom' changes to this EA. If you do so then I'll charge a fee per hour since I'm a professional coder and if you really need a modify or whatever then you have to pay for my time (which is limited due to my daily job)._  
_* There's no commercial interest on my side and everything here is shared for free in the spirit of helping others, if someone is trying to sell my EA please report back._  
  
**[Note]**  
I think that **_using _**w**_ hatever EA without knowledge about its logic coded, it's limit, what can or cannot do, is a recipe for disaster._**  
This is why in this first testing stage , I'm locking the EA to run only on demo account and for limited time ( usually end of each month so to be sure everyone is using latest version), then in due time I will share new version to be traded on real account.  
In this way we can test it more deeply to find hidden bugs and most important to understand what's logic behind Udine's strategy (which by the way is very simple if you took the time to study it).  
To be noted that this EA cannot be properly backtested due to news filter presence, so I do not trust it completely because I cannot figure out its statistical behaviour so I cannot evaluate its weakness and limit (max drawdown, max consecutive losses,...)  
Lastly, since this EA works with TP 5 and SL 10 is very very important that you choose a regulated ECN broker with [spreads](/brokers/spreads "View Live Spreads on the Broker Guide") below 2 pips for official pairs allowed (EJ,EU,GJ,GU)  
  
**[Technical Details]**  
**Latest Version : 1.1.8 [30 May 2015]**  
Expire on : _unlimited_  
Account type : _all (demo+live)_  
TimeFrame : _M30 (locked)_  
Risk Per Trade : _< 4% (locked)_  
Pair : _EURUSD,EURJPY,GBPJPY,GBPUSD (locked)_  
Entry type coded : _Level 1 (Refer to Udine's thread)_  
  
**[Users's Parameters]**  
~~LotSize (default = 0.01) // only used if MoneyManagement is false~~ (deprecated)  
StopLoss (default = 10) // Stoploss in pips  
TakeProfit (default = 5) // Takeprofit in pips  
~~MoneyManagement (default = true) // if true then orders are opened based on Risk % of account~~ (deprecated)  
Risk (default = 2) // only used if MoneyManagement is true - do not use Risk too much high (< 4% is maximum value suggested)  
MaxLossesPerDay (default = 4) // Max losses per day allowed, if reached EA stops opening trade for the whole day  
TradeOnlyLondon (default = true) // If true EA places trades only trade during London session (7 GMT - 16 GMT), if false EA places trades always (not suggested)  
TrailingStop (default = 3.5) // Trailingstop in pips  
DailyTargetPercentage (default = 2) // Daily target as percentage of account balance , when EA reaches this value stops trading for the whole day.  
PairSuffix (default = "") // Suffix of pair in case your broker support it (ie GBPJPYi, or EURUSDmicro and so on...)  
GUI_X = x-axis in pixel for UI  
GUI_Y = y-axis in pixel for UI  
  
**[Mandatory Indicators]**  
Wukar_News  
FFCal-Wukar  
AbsoluteStrenghtHisto  
  
**[Template Indicators]**  

Attached Image

![](/attachment/image/1642709?d=1427645126)

  
  
**[Screenshot]**  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot1.png
Size: 49 KB](/attachment/image/1658964/thumbnail?d=1429688981)](/attachment/image/1658964?d=1429688981)   

  
  
**[EA Rules]**  
This EA is designed to place and manage trades according to Level 1 rule from Udine's 00-level strategy, in particular all important informations is collected and shown on chart screen.  
EA will scan the chart and place trade based on simple rules, it will check for daily open price and place only long if price above, short if price below.  
Only one trade will be opened per hour and all orders will be done through placing pending orders. Pending orders, if not triggered, will be deleted 5 minutes before an M30 candle is closed.  
At the start of each M30 candle , EA will place a pending order @ .00 level only if ASH (AbsoluteStrenghtHisto) is changing colour from red to green (long - above daily open) or from green to red (short - below daily open).  
EA is designed to open only at .00 level (not .50 level) and work only on EJ,EU,GU,GJ (**_please don't ask for other currencies,index,metals,cfd and so on...!_**)  
EA will show on chart an yellow line that is to be intended as a *potential* entry. If all conditions are met then EA will automatically place a pending order.  
No trades will be placed 1 hour before big red News for EUR,JPY,GBP,USD and after half an hour.  
No trades will be placed if ADR has not space left in pips (up or down depending on daily open side)  
No trades will be placed if it's long @ .900 level or short @ .100 level  
No trades will be placed if max losses per days are reached.  
No trades will be places if daily target level is hit for the day.  
No trades will be placed before London Open and after London Close (if TradeOnlyLondon is set to true), in particular EA detects automatically London open and close time.  
  
**[EA Installation]**  
Extract UdineEA_package.rar directly into MT4 root (C:\\...\\{Your MT4 folder}\\) , you'll find UdineEA, indicators and template I'm currently using with Udine EA.  
After extracting all files , simply open platform and select Udine EA template.tpl from template list and you should are ready to go (just in case check in Expert and Journal tab if some indicators are missing).  
Finally be sure to see a smiling face in the top-right corner of your screen which indicates UdineEA is running correctly.  
  
**[Thanks]**  
This thread and UdineEA may exists only through the great thread started by Udine and his very sound trading approach which is helping a lot of traders to become successful, a big thank to Udine !  
  
Cheers,  
Skyline 

Attached File(s)

![File Type: rar](https://assets.faireconomy.media/images/attach/rar.gif) [UdineEA_v118.rar](/attachment/file/1684794?d=1432975773) 223 KB | 1,354 downloads | Uploaded May 30, 2015 5:49pm 

  * [#2](/thread/post/8171873#post8171873 "Post Permalink")

  * Mar 30, 2015 1:31am  Mar 30, 2015 1:31am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar34773_1.gif) GoForPip](goforpip)

  * | Commercial User  | Joined Mar 2007 | [120 Posts](/search?do=process&provider=Member&searchuser=34773)

Once again ![](https://resources.faireconomy.media/images/emojis/64/1f647-200d-2642-fe0f.png?v=15.1).  
I really appreciate your contribution. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#3](/thread/post/8171876#post8171876 "Post Permalink")

  * Mar 30, 2015 1:33am  Mar 30, 2015 1:33am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar338950_1.gif) cescof](cescof)

  * Joined Jun 2013 | Status: Trader | [1,006 Posts](/search?do=process&provider=Member&searchuser=338950)

> [Quoting skyline](/thread/post/8171858#post8171858 "View Quoted Post")
> 
> Disliked
> 
> Hi All, I'd like to share with you a simple EA coded for 00 Levels thread opened by Udine, I prefer to open a separate thread so to not clutter original thread with post related to this EA, so please direct your questions related to this EA here instead of Udine's thread. [Thread Rules] * No troll, no calling names, no flame are allowed in any form here. We are professional here and act as professional if we want to succeed in our quest. * Inappropriate behaviours will be punished with permanent ban from the thread and reported to the site administrators....
> 
> Ignored

Thanks really aprreciate....![](https://resources.faireconomy.media/images/emojis/64/1f44f.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#4](/thread/post/8171893#post8171893 "Post Permalink")

  * Mar 30, 2015 2:06am  Mar 30, 2015 2:06am 

  * [ stoolo123](stoolo123)

  * | Joined Nov 2014  | Status: Trader | [17 Posts](/search?do=process&provider=Member&searchuser=388474)

nicely ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#5](/thread/post/8171896#post8171896 "Post Permalink")

  * Mar 30, 2015 2:08am  Mar 30, 2015 2:08am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar402612_1.gif) mokuro89](mokuro89)

  * Joined Mar 2015 | Status: Trader | [449 Posts](/search?do=process&provider=Member&searchuser=402612)

Thanks for the EA, going test it 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#6](/thread/post/8171901#post8171901 "Post Permalink")

  * Mar 30, 2015 2:16am  Mar 30, 2015 2:16am 

  * [ stoolo123](stoolo123)

  * | Joined Nov 2014  | Status: Trader | [17 Posts](/search?do=process&provider=Member&searchuser=388474)

it is work on ea tester? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#7](/thread/post/8171907#post8171907 "Post Permalink")

  * Mar 30, 2015 2:25am  Mar 30, 2015 2:25am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting stoolo123](/thread/post/8171901#post8171901 "View Quoted Post")
> 
> Disliked
> 
> it is work on ea tester?
> 
> Ignored

Yes it works but it's useless due to the news filter which cannot be used in backtest. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#8](/thread/post/8171908#post8171908 "Post Permalink")

  * Mar 30, 2015 2:27am  Mar 30, 2015 2:27am 

  * [ Mianlien](mianlien)

  * | Joined Oct 2014  | Status: Trader | [142 Posts](/search?do=process&provider=Member&searchuser=387855)

thank for EA going to test demo  
Nice system 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#9](/thread/post/8171916#post8171916 "Post Permalink")

  * Edited 2:54am  Mar 30, 2015 2:35am | Edited 2:54am 

  * [ stoolo123](stoolo123)

  * | Joined Nov 2014  | Status: Trader | [17 Posts](/search?do=process&provider=Member&searchuser=388474)

i want do backtest on gbp/usd and its show me ea allowed pair G/U e/u .... pleas check, it dosent open any orders what is going on?  
  
"2015.03.29 19:53:32.355 2015.01.30 06:13 Udine EA_v112 EURUSD,M30: Alert: Udine EA allowed only on EURUSD,EURJPY,GBPUSD,GBPJPY, please check!!  
" 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#10](/thread/post/8171935#post8171935 "Post Permalink")

  * Mar 30, 2015 3:01am  Mar 30, 2015 3:01am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting stoolo123](/thread/post/8171916#post8171916 "View Quoted Post")
> 
> Disliked
> 
> i want do backtest on gbp/usd and its show me ea allowed pair G/U e/u .... pleas check, it dosent open any orders what is going on? "2015.03.29 19:53:32.355 2015.01.30 06:13 Udine EA_v112 EURUSD,M30: Alert: Udine EA allowed only on EURUSD,EURJPY,GBPUSD,GBPJPY, please check!! "
> 
> Ignored

It's not working on strategy tester 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#11](/thread/post/8171938#post8171938 "Post Permalink")

  * Edited 3:17am  Mar 30, 2015 3:03am | Edited 3:17am 

  * [ stoolo123](stoolo123)

  * | Joined Nov 2014  | Status: Trader | [17 Posts](/search?do=process&provider=Member&searchuser=388474)

in the future Y allowed another pair?  
one more question i need to open ea on every single chart e/u g/u e/j ,, or only in one? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#12](/thread/post/8171953#post8171953 "Post Permalink")

  * Edited 3:52am  Mar 30, 2015 3:39am | Edited 3:52am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar383001_1.gif) bypasssbo](bypasssbo)

  * | Joined Sep 2014  | Status: Trader | [53 Posts](/search?do=process&provider=Member&searchuser=383001)

Account type : demo (locked)  
  
**It means that we cant use it on a live account?**  
  
Sorry the answer was at the first post  
  
I think that **_using _**w**_ hatever EA without knowledge about its logic coded, it's limit, what can or cannot do, is a recipe for disaster._**  
This is why in this first testing stage , I'm locking the EA to run only on demo account and for limited time ( usually end of each month so to be sure everyone is using latest version), then in due time I will share new version to be traded on real account.  
  
Thanks 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#13](/thread/post/8171999#post8171999 "Post Permalink")

  * Mar 30, 2015 4:58am  Mar 30, 2015 4:58am 

  * [ PartySheeper](partysheeper)

  * | Joined Mar 2015  | Status: Trader | [34 Posts](/search?do=process&provider=Member&searchuser=404900)

Very well done, Skyline!  
I'm curious how this EA will work, taking each and every trade regarding Udine's Level 1 rules, without measuring the risk of the trade (DP, WP, candle formations, possible support/resistance areas etc.)  
I hope it will work well! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#14](/thread/post/8172008#post8172008 "Post Permalink")

  * Mar 30, 2015 5:10am  Mar 30, 2015 5:10am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting stoolo123](/thread/post/8171938#post8171938 "View Quoted Post")
> 
> Disliked
> 
> in the future Y allowed another pair? one more question i need to open ea on every single chart e/u g/u e/j ,, or only in one?
> 
> Ignored

Of course you have to put it on every single pair allowed 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#15](/thread/post/8172010#post8172010 "Post Permalink")

  * Mar 30, 2015 5:11am  Mar 30, 2015 5:11am 

  * [ Adam84](adam84)

  * | Joined Feb 2014  | Status: Trader | [117 Posts](/search?do=process&provider=Member&searchuser=364444)

Thank you Skyline! Look forward to the demo results..  
  
Just one question with regard to the installation: you indicate that the ASH indicator is mandatory, but it is not included in the file you provided. Is it already included in the EA or do I have load it myself? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#16](/thread/post/8172016#post8172016 "Post Permalink")

  * Mar 30, 2015 5:16am  Mar 30, 2015 5:16am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting PartySheeper](/thread/post/8171999#post8171999 "View Quoted Post")
> 
> Disliked
> 
> Very well done, Skyline! I'm curious how this EA will work, taking each and every trade regarding Udine's Level 1 rules, without measuring the risk of the trade (DP, WP, candle formations, possible support/resistance areas etc.) I hope it will work well!
> 
> Ignored

Ty PartySheeper ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)  
You can always turn off EA if you see general market conditions are too risky to place trades. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#17](/thread/post/8172023#post8172023 "Post Permalink")

  * Mar 30, 2015 5:22am  Mar 30, 2015 5:22am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting Adam84](/thread/post/8172010#post8172010 "View Quoted Post")
> 
> Disliked
> 
> Thank you Skyline! Look forward to the demo results.. Just one question with regard to the installation: you indicate that the ASH indicator is mandatory, but it is not included in the file you provided. Is it already included in the EA or do I have load it myself?
> 
> Ignored

You're are right Adam, sorry it was my fault I've forgot to add mandatory indicators to rar file, please download it again from first post (Udine_package_v1.rar) otherwise EA won't work.  
  
Thanks,  
Skyline 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#18](/thread/post/8172027#post8172027 "Post Permalink")

  * Mar 30, 2015 5:23am  Mar 30, 2015 5:23am 

  * [ Adam84](adam84)

  * | Joined Feb 2014  | Status: Trader | [117 Posts](/search?do=process&provider=Member&searchuser=364444)

> [Quoting skyline](/thread/post/8172023#post8172023 "View Quoted Post")
> 
> Disliked
> 
> {quote} You're are right Adam, sorry it was my fault I've forgot to add mandatory indicators to rar file, please download it again from first post (Udine_package_v1.rar) otherwise EA won't work. Thanks, Skyline
> 
> Ignored

Will do, thanks! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#19](/thread/post/8172041#post8172041 "Post Permalink")

  * Mar 30, 2015 5:41am  Mar 30, 2015 5:41am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

I've found another bug which prevent EA running correctly (now it should starts in Strategy Tester but it's still useless due to news filter).  
  
**Please download again UdineEA_package_v2.rar from first post**  
  
Ty,  
Skyline 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#20](/thread/post/8172066#post8172066 "Post Permalink")

  * Mar 30, 2015 6:09am  Mar 30, 2015 6:09am 

  * [ leancuisine](leancuisine)

  * | Joined Jul 2014  | Status: Trader | [38 Posts](/search?do=process&provider=Member&searchuser=376648)

I keep getting an error that it can only trade EUR/USD, GBP/USD, etc. There isn't any prefixes at my broker either... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * UdineEA Official Thread
  *   * [ **Reply to Thread** ](/thread/533099-udineea-official-thread/reply#reply)

  * More

[](https://www.forexfactory.com "Homepage")

  * [Forums](forums)
  * [Trades](trades)
  * [Calendar](calendar)
  * [News](news)
  * [Market](market)
  * [Brokers](brokers)

****

[](https://www.faireconomy.com/)

  * 

[The Official "Ok, now I'm pissed" Thread](/thread/73546-the-official-ok-now-im-pissed-thread "Hello Everyone, 
 
Seeing the apparent lack of threads of this nature \(just kidding, but read on\) I have decided to set up a respectable...") 51 replies

[Historic Charts: NZ Official Cash Rate](/thread/20380-historic-charts-nz-official-cash-rate "Sep 14, 2005") 15 replies

[Is there an official exchange rate?!](/thread/11571-is-there-an-official-exchange-rate "Different brokers have different bid and ask prices for every cross or pair.  However, the bid and ask price is based on something...I am...") 14 replies

[Official forex time zone](/thread/9940-official-forex-time-zone "is there a standard forex time zone? do i follow gmt or NY time? i use 4 hour charts and sometimes the time is way off because of time zone...") 3 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/533099-udineea-official-thread/reply#reply)
  * Subscribe
  * [100](javascript:void\(0\);)

Attachments: UdineEA Official Thread

Tags: UdineEA Official Thread

#  [](/thread/533099-udineea-official-thread)UdineEA Official Thread 

  * 

  * [#21](/thread/post/8172068#post8172068 "Post Permalink")

  * Mar 30, 2015 6:13am  Mar 30, 2015 6:13am 

  * [ rmndschmidt](rmndschmidt)

  * | Joined Mar 2014  | Status: Trader | [42 Posts](/search?do=process&provider=Member&searchuser=365689)

> [Quoting skyline](/thread/post/8171935#post8171935 "View Quoted Post")
> 
> Disliked
> 
> {quote} It's not working on strategy tester
> 
> Ignored

Hello skyline,  
thank you very much for sharing your EA. But there is a problem I don´t understand. Look at the picture! 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Udine EA.png
Size: 612 KB](/attachment/image/1642761/thumbnail?d=1427663578)](/attachment/image/1642761?d=1427663578)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#22](/thread/post/8172071#post8172071 "Post Permalink")

  * Mar 30, 2015 6:15am  Mar 30, 2015 6:15am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting rmndschmidt](/thread/post/8172068#post8172068 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hello skyline, thank you very much for sharing your EA. But there is a problem I dont understand. Look at the picture! {image}
> 
> Ignored

**Please download again UdineEA_package_v2.rar from first post**

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#23](/thread/post/8172075#post8172075 "Post Permalink")

  * Mar 30, 2015 6:18am  Mar 30, 2015 6:18am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar338950_1.gif) cescof](cescof)

  * Joined Jun 2013 | Status: Trader | [1,006 Posts](/search?do=process&provider=Member&searchuser=338950)

> [Quoting rmndschmidt](/thread/post/8172068#post8172068 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hello skyline, thank you very much for sharing your EA. But there is a problem I dont understand. Look at the picture! {image}
> 
> Ignored

same here v113  
Regards 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#24](/thread/post/8172078#post8172078 "Post Permalink")

  * Mar 30, 2015 6:21am  Mar 30, 2015 6:21am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting cescof](/thread/post/8172075#post8172075 "View Quoted Post")
> 
> Disliked
> 
> {quote} same here v113 Regards
> 
> Ignored

Please remove v1.1.2 and put v1.1.3 on chart from 1st post , it's working on my platform.  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot1.png
Size: 44 KB](/attachment/image/1642763/thumbnail?d=1427664163)](/attachment/image/1642763?d=1427664163)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#25](/thread/post/8172081#post8172081 "Post Permalink")

  * Mar 30, 2015 6:23am  Mar 30, 2015 6:23am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar338950_1.gif) cescof](cescof)

  * Joined Jun 2013 | Status: Trader | [1,006 Posts](/search?do=process&provider=Member&searchuser=338950)

> [Quoting skyline](/thread/post/8172078#post8172078 "View Quoted Post")
> 
> Disliked
> 
> {quote} Please remove v1.1.2 and put v1.1.3 on chart from 1st post , it's working on my platform.
> 
> Ignored

its ok now i forgot to remove from one chart  
Regards 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#26](/thread/post/8172085#post8172085 "Post Permalink")

  * Mar 30, 2015 6:26am  Mar 30, 2015 6:26am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting cescof](/thread/post/8172081#post8172081 "View Quoted Post")
> 
> Disliked
> 
> {quote} its ok now i forgot to remove from one chart Regards
> 
> Ignored

![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#27](/thread/post/8172086#post8172086 "Post Permalink")

  * Mar 30, 2015 6:26am  Mar 30, 2015 6:26am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar54390_11.gif) Chake](chake)

  * | Joined Nov 2007  | Status: Long time member | [765 Posts](/search?do=process&provider=Member&searchuser=54390)

Congrats on this EA and the thread skyline! ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)

Persistence will get it. Consistency will keep it.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#28](/thread/post/8172121#post8172121 "Post Permalink")

  * Mar 30, 2015 7:10am  Mar 30, 2015 7:10am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar357421_1.gif) bazze](bazze)

  * | Joined Dec 2013  | Status: Trader | [1,135 Posts](/search?do=process&provider=Member&searchuser=357421)

??? 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: LiteForex MT4.png
Size: 130 KB](/attachment/image/1642770/thumbnail?d=1427667008)](/attachment/image/1642770?d=1427667008)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#29](/thread/post/8172124#post8172124 "Post Permalink")

  * Mar 30, 2015 7:13am  Mar 30, 2015 7:13am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar34773_1.gif) GoForPip](goforpip)

  * | Commercial User  | Joined Mar 2007 | [120 Posts](/search?do=process&provider=Member&searchuser=34773)

Hi Skyline  
I just got " i-Profittracker_" zero divide error   
I don't know does it matters but nevertheless... 

Attached Image

![](/attachment/image/1642773?d=1427667161)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#30](/thread/post/8172138#post8172138 "Post Permalink")

  * Mar 30, 2015 7:24am  Mar 30, 2015 7:24am 

  * [ DerBerliner](derberliner)

  * | Joined Feb 2011  | Status: Trader | [822 Posts](/search?do=process&provider=Member&searchuser=168827)

Hi bazze ! The same here ! It seems that's a bug ... kind of ? ![](https://resources.faireconomy.media/images/emojis/64/1f937-200d-2642-fe0f.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#31](/thread/post/8172139#post8172139 "Post Permalink")

  * Mar 30, 2015 7:24am  Mar 30, 2015 7:24am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting GoForPip](/thread/post/8172124#post8172124 "View Quoted Post")
> 
> Disliked
> 
> Hi Skyline I just got " i-Profittracker_" zero divide error I don't know does it matters but nevertheless... {image}
> 
> Ignored

I don't have this error , maybe you don't have all history shown in your history tab.  
Btw don't worry it's not used by EA , you can delete it if that error keeps annoying you ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#32](/thread/post/8172140#post8172140 "Post Permalink")

  * Mar 30, 2015 7:29am  Mar 30, 2015 7:29am 

  * [ DerBerliner](derberliner)

  * | Joined Feb 2011  | Status: Trader | [822 Posts](/search?do=process&provider=Member&searchuser=168827)

Yep the zero divide thingy doesnt worry me ... but what about that "Cannot open file ... " remark in the "Expert" tab ?  
  
Bazze reported that bug as well ... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#33](/thread/post/8172141#post8172141 "Post Permalink")

  * Mar 30, 2015 7:30am  Mar 30, 2015 7:30am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar158271_2.gif) dann0000](dann0000)

  * | Joined Oct 2010  | Status: Trader | [10 Posts](/search?do=process&provider=Member&searchuser=158271)

great work skyline and thank you...btw, we have to download in history all the quotes for those 4 pairs..? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#34](/thread/post/8172154#post8172154 "Post Permalink")

  * Mar 30, 2015 7:49am  Mar 30, 2015 7:49am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar357421_1.gif) bazze](bazze)

  * | Joined Dec 2013  | Status: Trader | [1,135 Posts](/search?do=process&provider=Member&searchuser=357421)

Can't see why the spread is to high??? Can you please explain, skyline... 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Global Prime - MetaTrader 4.png
Size: 115 KB](/attachment/image/1642781/thumbnail?d=1427669316)](/attachment/image/1642781?d=1427669316)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#35](/thread/post/8172161#post8172161 "Post Permalink")

  * Mar 30, 2015 7:59am  Mar 30, 2015 7:59am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar357421_1.gif) bazze](bazze)

  * | Joined Dec 2013  | Status: Trader | [1,135 Posts](/search?do=process&provider=Member&searchuser=357421)

Sorry,but have another one that I don't understand also.... 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Global Prime2.png
Size: 121 KB](/attachment/image/1642782/thumbnail?d=1427669924)](/attachment/image/1642782?d=1427669924)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#36](/thread/post/8172166#post8172166 "Post Permalink")

  * Mar 30, 2015 8:04am  Mar 30, 2015 8:04am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar135523_1.gif) blamshakk](blamshakk)

  * Joined Mar 2010 | Status: Trader | [2,240 Posts](/search?do=process&provider=Member&searchuser=135523)

im running v 113 and all the pairs are saying spread too high even though some of them are like 0.4  
  

> [Quoting bazze](/thread/post/8172154#post8172154 "View Quoted Post")
> 
> Disliked
> 
> Can't see why the spread is to high??? Can you please explain, skyline... {image}
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#37](/thread/post/8172256#post8172256 "Post Permalink")

  * Edited 10:51am  Mar 30, 2015 10:06am | Edited 10:51am 

  * [ mebarrac](mebarrac)

  * | Joined Feb 2015  | Status: Trader | [38 Posts](/search?do=process&provider=Member&searchuser=402218)

Hi Im running [fxcm](/brokers/fxcm "View FXCM Broker Profile") us demo server , I can load EUR/USD pair fine ,all be it with the spread error , but as soon as I put the template on any of the other pairs it crashes my MT4 and hangs up. Anyone else seeing this?  
  
Edit: got it working now, I needed to put the ea on first then load the indicators and it wouldn't crash...weird  
still get the spread to high error even though my pairs are all below 1.0, I guess it won't enter with this rule not satisfied  
  
Great job btw Skyline , appreciate you putting the work in to code this and sharing it with the group...thank you! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#38](/thread/post/8172373#post8172373 "Post Permalink")

  * Mar 30, 2015 12:51pm  Mar 30, 2015 12:51pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar388093_1.gif) firewight](firewight)

  * | Joined Oct 2014  | Status: Trader | [817 Posts](/search?do=process&provider=Member&searchuser=388093)

> [Quoting skyline](/thread/post/8171858#post8171858 "View Quoted Post")
> 
> Disliked
> 
> Hi All, I'd like to share with you a simple EA coded for 00 Levels thread opened by Udine, I prefer to open a separate thread so to not clutter original thread with post related to this EA, so please direct your questions related to this EA here instead of Udine's thread.
> 
> Ignored

Cheers mate, I appreciate all your hard efforts in compiling this EA!  
  
Further to the "Spread too high" error, I have watched the charts for some time & can advise that a spread of 0.1 is OK and ready to trade, but as soon as the spread exceeds 0.2 the spread too high error occurs.  
  
I hope this helps with bug fixes and testing.  
  
Great work mate!  
  
Cheers! 

Life is like a snickers, its full of nuts!

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#39](/thread/post/8172378#post8172378 "Post Permalink")

  * Mar 30, 2015 1:04pm  Mar 30, 2015 1:04pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar82721_6.gif) jurn_e](jurn_e)

  * | Joined Oct 2008  | Status: Trader | [984 Posts](/search?do=process&provider=Member&searchuser=82721)

subscribed! 

Pivot Boss in the making~

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#40](/thread/post/8172431#post8172431 "Post Permalink")

  * Mar 30, 2015 1:54pm  Mar 30, 2015 1:54pm 

  * [ cardm3n](cardm3n)

  * | Joined Mar 2015  | Status: Trader | [126 Posts](/search?do=process&provider=Member&searchuser=406276)

I am looking forward to the development of this EA. Currently trying to make my way through Udine's 00 level trading thread. Quite a ways to go still. Good luck gusy. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * UdineEA Official Thread
  *   * [ **Reply to Thread** ](/thread/533099-udineea-official-thread/reply#reply)

  * More

[](https://www.forexfactory.com "Homepage")

  * [Forums](forums)
  * [Trades](trades)
  * [Calendar](calendar)
  * [News](news)
  * [Market](market)
  * [Brokers](brokers)

****

[](https://www.faireconomy.com/)

  * 

[The Official "Ok, now I'm pissed" Thread](/thread/73546-the-official-ok-now-im-pissed-thread "Hello Everyone, 
 
Seeing the apparent lack of threads of this nature \(just kidding, but read on\) I have decided to set up a respectable...") 51 replies

[Historic Charts: NZ Official Cash Rate](/thread/20380-historic-charts-nz-official-cash-rate "Sep 14, 2005") 15 replies

[Is there an official exchange rate?!](/thread/11571-is-there-an-official-exchange-rate "Different brokers have different bid and ask prices for every cross or pair.  However, the bid and ask price is based on something...I am...") 14 replies

[Official forex time zone](/thread/9940-official-forex-time-zone "is there a standard forex time zone? do i follow gmt or NY time? i use 4 hour charts and sometimes the time is way off because of time zone...") 3 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/533099-udineea-official-thread/reply#reply)
  * Subscribe
  * [100](javascript:void\(0\);)

Attachments: UdineEA Official Thread

Tags: UdineEA Official Thread

#  [](/thread/533099-udineea-official-thread)UdineEA Official Thread 

  * 

  * [#41](/thread/post/8172438#post8172438 "Post Permalink")

  * Mar 30, 2015 2:02pm  Mar 30, 2015 2:02pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar299111_1.gif) dimdel](dimdel)

  * Joined Oct 2012 | Status: Trader | [2,555 Posts](/search?do=process&provider=Member&searchuser=299111)

subscribed 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#42](/thread/post/8172451#post8172451 "Post Permalink")

  * Mar 30, 2015 2:20pm  Mar 30, 2015 2:20pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar370579_1.gif) shg](shg)

  * | Joined Apr 2014  | Status: Trader | [436 Posts](/search?do=process&provider=Member&searchuser=370579)

> [Quoting skyline](/thread/post/8171858#post8171858 "View Quoted Post")
> 
> Disliked
> 
> Hi All, I'd like to share with you a simple EA coded for 00 Levels thread opened by Udine, I prefer to open a separate thread so to not clutter original thread with post related to this EA, so please direct your questions related to this EA here instead of Udine's thread.
> 
> Ignored

Thanks skyline for your effort and EA. My demo have only EU below 2 spread but rest of them have higher. On the other hand my live account have many pairs with lower [spreads](/brokers/spreads "View Live Spreads on the Broker Guide") so will be very interesting to see how things work outs. I have subscribe the thread and will keep the eyes and actively read all post so i keep learning. I will demo EU and will try to contribute if i have something....  
  
thanks once again... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#43](/thread/post/8172510#post8172510 "Post Permalink")

  * Mar 30, 2015 3:29pm  Mar 30, 2015 3:29pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

Hi Guys,  
I'll check into the 'spread too high' issue , by the way it's only a simple alarm (even if it's wrong) and doesn't affect the normal EA operations , so you can just ignore it until I fix ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)  
  
Cheers,  
Skyline 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#44](/thread/post/8172522#post8172522 "Post Permalink")

  * Mar 30, 2015 3:45pm  Mar 30, 2015 3:45pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

I've fixed a bug that prevent open orders at correct London open due to DST changes and also spread now is correctly indicated on chart.  
  
**MANDATORY UPDATE : Please download again UdineEA_v114.rar from first post**  
  
Cheers,  
Skyline 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#45](/thread/post/8172538#post8172538 "Post Permalink")

  * Mar 30, 2015 4:02pm  Mar 30, 2015 4:02pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377617_1.gif) merrygold](merrygold)

  * Joined Jul 2014 | Status: Trader | [736 Posts](/search?do=process&provider=Member&searchuser=377617)

Good luck on your thread skyline.  
  
Subscribe![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)

MY SITTING, NEVER MY THINKING!

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#46](/thread/post/8172580#post8172580 "Post Permalink")

  * Mar 30, 2015 4:20pm  Mar 30, 2015 4:20pm 

  * [ Udine](udine)

  * Joined Jul 2008 | Status: Trader | [5,763 Posts](/search?do=process&provider=Member&searchuser=75976)

Skyline,  
  
job well done..  
  
good luck with the thread, I will be following with interest ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)  
  
Udine 

Sleep less, live fast, as it aint gonna last ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#47](/thread/post/8172594#post8172594 "Post Permalink")

  * Mar 30, 2015 4:28pm  Mar 30, 2015 4:28pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar309469_3.gif) gigicualex](gigicualex)

  * | Joined Nov 2012  | Status: Trader | [1,187 Posts](/search?do=process&provider=Member&searchuser=309469)

Thank you Skyline. Much appreciated!  
I've installed it on a Demo account, looking forward for the 1st setup today to see how 'smart' your code is ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
Cheers,  
G. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#48](/thread/post/8172602#post8172602 "Post Permalink")

  * Mar 30, 2015 4:35pm  Mar 30, 2015 4:35pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting Udine](/thread/post/8172580#post8172580 "View Quoted Post")
> 
> Disliked
> 
> Skyline, job well done.. good luck with the thread, I will be following with interest ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1) Udine
> 
> Ignored

Thank you Master Udine !! ![](https://resources.faireconomy.media/images/emojis/64/1f647-200d-2642-fe0f.png?v=15.1)  
Your input is really appreciated , if you have the time to set up this tiny EA in your chart ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)  
  
P.S.: Ops sorry I've realized just now that I used your nickname without asking you first in thread subject ('UdineEA Official Thread'), hope you don't mind, just in case let me know and I change it.  
  
Cheers,  
Skyline 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#49](/thread/post/8172609#post8172609 "Post Permalink")

  * Mar 30, 2015 4:36pm  Mar 30, 2015 4:36pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

First level 1 for the day for me on EU @ 1.08300 ([IC Markets](/brokers/ic-markets "View IC Markets Broker Profile")), still waiting to be activated  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot1.png
Size: 36 KB](/attachment/image/1642971/thumbnail?d=1427700970)](/attachment/image/1642971?d=1427700970)   

  
  
Edit : it was fast , EU to TP ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot2.png
Size: 2 KB](/attachment/image/1642975/thumbnail?d=1427701122)](/attachment/image/1642975?d=1427701122)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#50](/thread/post/8172610#post8172610 "Post Permalink")

  * Mar 30, 2015 4:37pm  Mar 30, 2015 4:37pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar34773_1.gif) GoForPip](goforpip)

  * | Commercial User  | Joined Mar 2007 | [120 Posts](/search?do=process&provider=Member&searchuser=34773)

EURUSD  
Skyline  
Shouldn't Entry be either 00 or 50 lvl?  
EA has placed first order on 00 lvl 1.08300 and previous close was on 1.08379. More than enough room to place it on 1.08350 including the spread.  
  
Edit: Forgot to mention that it didn't placed any order EA just drew the line. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot_39.png
Size: 51 KB](/attachment/image/1642973/thumbnail?d=1427701033)](/attachment/image/1642973?d=1427701033)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#51](/thread/post/8172618#post8172618 "Post Permalink")

  * Mar 30, 2015 4:41pm  Mar 30, 2015 4:41pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar360590_1.gif) ronwalt](ronwalt)

  * | Joined Jan 2014  | Status: Trader | [88 Posts](/search?do=process&provider=Member&searchuser=360590)

> [Quoting skyline](/thread/post/8172609#post8172609 "View Quoted Post")
> 
> Disliked
> 
> First level 1 for the day for me on EU @ 1.08300 (IC Markets), still waiting to be activated {image} Edit : it was fast , EU to TP ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1) {image}
> 
> Ignored

Yes, that was nice. Looked away and the next thing I knew it triggered and exited. Thanks skyline....looking good. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#52](/thread/post/8172619#post8172619 "Post Permalink")

  * Mar 30, 2015 4:42pm  Mar 30, 2015 4:42pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar370579_1.gif) shg](shg)

  * | Joined Apr 2014  | Status: Trader | [436 Posts](/search?do=process&provider=Member&searchuser=370579)

> [Quoting skyline](/thread/post/8172522#post8172522 "View Quoted Post")
> 
> Disliked
> 
> I've fixed a bug that prevent open orders at correct London open due to DST changes and also spread now is correctly indicated on chart. MANDATORY UPDATE : Please download again UdineEA_v114.rar from first post Cheers, Skyline
> 
> Ignored

Hi skyline,  
  
i just downloaded and loaded again. in EU i have 1.2 spread in demo but it still says that spread too high...  
  
thanks 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#53](/thread/post/8172627#post8172627 "Post Permalink")

  * Mar 30, 2015 4:47pm  Mar 30, 2015 4:47pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting GoForPip](/thread/post/8172610#post8172610 "View Quoted Post")
> 
> Disliked
> 
> EURUSD Skyline Shouldn't Entry be either 00 or 50 lvl? EA has placed first order on 00 lvl 1.08300 and previous close was on 1.08379. More than enough room to place it on 1.08350 including the spread. Edit: Forgot to mention that it didn't placed any order EA just drew the line. {image}
> 
> Ignored

Hi GoForPip,  
EA is designed to open only at .00 level  
  
Cheers,  
Skyline 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#54](/thread/post/8172630#post8172630 "Post Permalink")

  * Mar 30, 2015 4:48pm  Mar 30, 2015 4:48pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar309469_3.gif) gigicualex](gigicualex)

  * | Joined Nov 2012  | Status: Trader | [1,187 Posts](/search?do=process&provider=Member&searchuser=309469)

> [Quoting skyline](/thread/post/8172609#post8172609 "View Quoted Post")
> 
> Disliked
> 
> First level 1 for the day for me on EU @ 1.08300 (IC Markets), still waiting to be activated {image} Edit : it was fast , EU to TP ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1) {image}
> 
> Ignored

Same here, working good so far(at least from the technical point of view)  
I didn't take this trade on live as I considered to be a risky one(setup candle too big) 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot1.png
Size: 119 KB](/attachment/image/1642980/thumbnail?d=1427701668)](/attachment/image/1642980?d=1427701668)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#55](/thread/post/8172639#post8172639 "Post Permalink")

  * Mar 30, 2015 4:53pm  Mar 30, 2015 4:53pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar121788_9.gif) maadz](maadz)

  * Joined Nov 2009 | Status: It must come from a need! | [121 Posts](/search?do=process&provider=Member&searchuser=121788)

> [Quoting skyline](/thread/post/8172609#post8172609 "View Quoted Post")
> 
> Disliked
> 
> First level 1 for the day for me on EU @ 1.08300 (IC Markets), still waiting to be activated {image} Edit : it was fast , EU to TP ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1) {image}
> 
> Ignored

The same here .. Thanks for great work ..  
  
  
  
But I think this trade is risky due to prev. candle is too big (The gray dot would prevent me to enter this trade) .. Can you put this rule in next versions?  
  
  
  
Thanks again 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: Screenshot1.png
Size: 54 KB](/attachment/image/1642984/thumbnail?d=1427701867)](/attachment/image/1642984?d=1427701867)   
[![Click to Enlarge

Name: Screenshot2.png
Size: 11 KB](/attachment/image/1642986/thumbnail?d=1427701983)](/attachment/image/1642986?d=1427701983)   

It must come from a need!

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#56](/thread/post/8172640#post8172640 "Post Permalink")

  * Mar 30, 2015 4:53pm  Mar 30, 2015 4:53pm 

  * [ Udine](udine)

  * Joined Jul 2008 | Status: Trader | [5,763 Posts](/search?do=process&provider=Member&searchuser=75976)

> [Quoting skyline](/thread/post/8172602#post8172602 "View Quoted Post")
> 
> Disliked
> 
> {quote} Thank you Master Udine !! ![](https://resources.faireconomy.media/images/emojis/64/1f647-200d-2642-fe0f.png?v=15.1) Your input is really appreciated , if you have the time to set up this tiny EA in your chart ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1) P.S.: Ops sorry I've realized just now that I used your nickname without asking you first in thread subject ('UdineEA Official Thread'), hope you don't mind, just in case let me know and I change it. Cheers, Skyline
> 
> Ignored

  
no problem at all ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)  
  
trading live, so no reason to put in on my chart, as it only works on demo ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)  
  
Udine 

Sleep less, live fast, as it aint gonna last ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#57](/thread/post/8172679#post8172679 "Post Permalink")

  * Mar 30, 2015 5:11pm  Mar 30, 2015 5:11pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting maadz](/thread/post/8172639#post8172639 "View Quoted Post")
> 
> Disliked
> 
> Can you put this rule in next versions?
> 
> Ignored

Hi Maadz, please could you read thread rules in 1st post ? ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
  
_* Do not never ask me here (or by pm) for 'custom' changes to this EA. If you do so then I'll charge a fee per hour since I'm a professional coder and if you really need a modify or whatever then you have to pay for my time (which is limited due to my daily job)._  
  
Cheers,  
Skyline 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#58](/thread/post/8172734#post8172734 "Post Permalink")

  * Mar 30, 2015 5:33pm  Mar 30, 2015 5:33pm 

  * [ jackok](jackok)

  * | Joined Jun 2009  | Status: Trader | [9 Posts](/search?do=process&provider=Member&searchuser=106372)

Hi Skyline,  
  
First of all, thank you for your great work. I got a quick question here. Earlier on GBPJPY, the EA gave a hint for a long trade at 177.600. When price crossed up the line, it seems the EA didn't trigger the trade. Do we need to place the order manually instead of EA doing it? Correct me if I was wrong, thanks.  
  
Regards,  
  
\--  
Jack 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 63 KB](/attachment/image/1643017/thumbnail?d=1427704363)](/attachment/image/1643017?d=1427704363)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#59](/thread/post/8172745#post8172745 "Post Permalink")

  * Mar 30, 2015 5:38pm  Mar 30, 2015 5:38pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting jackok](/thread/post/8172734#post8172734 "View Quoted Post")
> 
> Disliked
> 
> Hi Skyline, First of all, thank you for your great work. I got a quick question here. Earlier on GBPJPY, the EA gave a hint for a long trade at 177.600. When price crossed up the line, it seems the EA didn't trigger the trade. Do we need to place the order manually instead of EA doing it? Correct me if I was wrong, thanks. Regards, -- Jack {image}
> 
> Ignored

Hi Jackok,  
the yellow line is only a *potential* entry, show as reference , if all conditions are met then a pending order is placed automatically by EA, maybe I have to change a little bit that line description because it's misleading ![](https://resources.faireconomy.media/images/emojis/64/1f61f.png?v=15.1)  
In that particular order on GJ , ASH didn't change color (changed one candle earlier) so no entry.  
  
Cheers,  
Skyline 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#60](/thread/post/8172764#post8172764 "Post Permalink")

  * Mar 30, 2015 5:46pm  Mar 30, 2015 5:46pm 

  * [ jackok](jackok)

  * | Joined Jun 2009  | Status: Trader | [9 Posts](/search?do=process&provider=Member&searchuser=106372)

> [Quoting skyline](/thread/post/8172745#post8172745 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi Jackok, the yellow line is only a *potential* entry, show as reference , if all conditions are met then a pending order is placed automatically by EA, maybe I have to change a little bit that line description because it's misleading ![](https://resources.faireconomy.media/images/emojis/64/1f61f.png?v=15.1) In that particular order on GJ , ASH didn't change color (changed one candle earlier) so no entry. Cheers, Skyline
> 
> Ignored

Got it. Thank you for your kind reply. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * UdineEA Official Thread
  *   * [ **Reply to Thread** ](/thread/533099-udineea-official-thread/reply#reply)

  * More

[](https://www.forexfactory.com "Homepage")

  * [Forums](forums)
  * [Trades](trades)
  * [Calendar](calendar)
  * [News](news)
  * [Market](market)
  * [Brokers](brokers)

****

[](https://www.faireconomy.com/)

  * 

[The Official "Ok, now I'm pissed" Thread](/thread/73546-the-official-ok-now-im-pissed-thread "Hello Everyone, 
 
Seeing the apparent lack of threads of this nature \(just kidding, but read on\) I have decided to set up a respectable...") 51 replies

[Historic Charts: NZ Official Cash Rate](/thread/20380-historic-charts-nz-official-cash-rate "Sep 14, 2005") 15 replies

[Is there an official exchange rate?!](/thread/11571-is-there-an-official-exchange-rate "Different brokers have different bid and ask prices for every cross or pair.  However, the bid and ask price is based on something...I am...") 14 replies

[Official forex time zone](/thread/9940-official-forex-time-zone "is there a standard forex time zone? do i follow gmt or NY time? i use 4 hour charts and sometimes the time is way off because of time zone...") 3 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/533099-udineea-official-thread/reply#reply)
  * Subscribe
  * [100](javascript:void\(0\);)

Attachments: UdineEA Official Thread

Tags: UdineEA Official Thread

#  [](/thread/533099-udineea-official-thread)UdineEA Official Thread 

  * 

  * [#61](/thread/post/8172808#post8172808 "Post Permalink")

  * Mar 30, 2015 6:08pm  Mar 30, 2015 6:08pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting Udine](/thread/post/8172640#post8172640 "View Quoted Post")
> 
> Disliked
> 
> {quote} no problem at all ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1) trading live, so no reason to put in on my chart, as it only works on demo ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1) Udine
> 
> Ignored

Ty Udine ! ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)  
I guess at the end of April after 1 month of intensive testing on demo with the help of this amazing community I can share live version ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)  
  
Cheers,  
Skyline 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#62](/thread/post/8172927#post8172927 "Post Permalink")

  * Mar 30, 2015 7:12pm  Mar 30, 2015 7:12pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar121788_9.gif) maadz](maadz)

  * Joined Nov 2009 | Status: It must come from a need! | [121 Posts](/search?do=process&provider=Member&searchuser=121788)

> [Quoting skyline](/thread/post/8172679#post8172679 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi Maadz, please could you read thread rules in 1st post ? ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) * Do not never ask me here (or by pm) for 'custom' changes to this EA. If you do so then I'll charge a fee per hour since I'm a professional coder and if you really need a modify or whatever then you have to pay for my time (which is limited due to my daily job). Cheers, Skyline
> 
> Ignored

  

> Quote
> 
> Disliked
> 
> This EA is designed to place and manage trades according to Level 1 rule from Udine's 00-level strategy, in particular all important informations is collected and shown on chart screen

  
It's depends on the definition of "custom" .. since it was a level 1 rule.  
  
anyway thanks for your efforts and time ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) .

It must come from a need!

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#63](/thread/post/8172940#post8172940 "Post Permalink")

  * Mar 30, 2015 7:16pm  Mar 30, 2015 7:16pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar121788_9.gif) maadz](maadz)

  * Joined Nov 2009 | Status: It must come from a need! | [121 Posts](/search?do=process&provider=Member&searchuser=121788)

2nd entry >> Ts @ open price 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot1.png
Size: 64 KB](/attachment/image/1643086/thumbnail?d=1427710538)](/attachment/image/1643086?d=1427710538)   

It must come from a need!

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#64](/thread/post/8172945#post8172945 "Post Permalink")

  * Mar 30, 2015 7:17pm  Mar 30, 2015 7:17pm 

  * [ dman7800](dman7800)

  * | Joined Sep 2014  | Status: Trader | [31 Posts](/search?do=process&provider=Member&searchuser=382482)

Hi Skyline,  
Thanks for your efforts on this, I am testing your EA eagerly.  
  
GBPUSD traded through the yellow line & no trade opened..  
Is the "SPREAD TOO HIGH" stopping the trade? I know you mentioned that its only an alert, but should a trade have opened short @1.48300 ?  
  
Cheers!  
  
See below: 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: udineEA_GBPUSD.JPG
Size: 239 KB](/attachment/image/1643089/thumbnail?d=1427710608)](/attachment/image/1643089?d=1427710608)   

Enter Signature

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#65](/thread/post/8172972#post8172972 "Post Permalink")

  * Mar 30, 2015 7:28pm  Mar 30, 2015 7:28pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting maadz](/thread/post/8172927#post8172927 "View Quoted Post")
> 
> Disliked
> 
> {quote} {quote} It's depends on the definition of "custom" .. since it was a level 1 rule. anyway thanks for your efforts and time ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) .
> 
> Ignored

eheheh well maybe i have to change 'custom' to 'any' ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
  
I preferred to not overcomplicate EA in this first stage this is why only coded .00 entry level, maybe in future could consider to add .50 level entry but from test it seems doing good also with basic .00 level ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)  
  
Ty for testing ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
Cheers,  
Skyline 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#66](/thread/post/8172979#post8172979 "Post Permalink")

  * Mar 30, 2015 7:31pm  Mar 30, 2015 7:31pm 

  * [ Traffex](traffex)

  * | Joined Nov 2013  | Status: Trader | [366 Posts](/search?do=process&provider=Member&searchuser=356934)

> [Quoting dman7800](/thread/post/8172945#post8172945 "View Quoted Post")
> 
> Disliked
> 
> Hi Skyline, Thanks for your efforts on this, I am testing your EA eagerly. GBPUSD traded through the yellow line & no trade opened.. Is the "SPREAD TOO HIGH" stopping the trade? I know you mentioned that its only an alert, but should a trade have opened short @1.48300 ? Cheers! See below: {image}
> 
> Ignored

The trade was opened, but closed within 1 - 2 minutes by Ts on BE. Perhaps you look to yor account history. I lost commision, skyline could you make an input to avoid this ? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#67](/thread/post/8172986#post8172986 "Post Permalink")

  * Mar 30, 2015 7:33pm  Mar 30, 2015 7:33pm 

  * [ dman7800](dman7800)

  * | Joined Sep 2014  | Status: Trader | [31 Posts](/search?do=process&provider=Member&searchuser=382482)

> [Quoting Traffex](/thread/post/8172979#post8172979 "View Quoted Post")
> 
> Disliked
> 
> {quote} The trade was opened, but closed within 1 - 2 minutes by Ts on BE. Perhaps you look to yor account history. I lost commision, skyline could you make an input to avoid this ?
> 
> Ignored

Hi Traffex,  
Trade definitely did not open..I am sitting in front of it, looking at it..  
Last trade in my history was 26th March  
  
Cheers  
  
Dman 

Enter Signature

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#68](/thread/post/8172989#post8172989 "Post Permalink")

  * Mar 30, 2015 7:34pm  Mar 30, 2015 7:34pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting dman7800](/thread/post/8172945#post8172945 "View Quoted Post")
> 
> Disliked
> 
> Hi Skyline, Thanks for your efforts on this, I am testing your EA eagerly. GBPUSD traded through the yellow line & no trade opened.. Is the "SPREAD TOO HIGH" stopping the trade? I know you mentioned that its only an alert, but should a trade have opened short @1.48300 ? Cheers! See below: {image}
> 
> Ignored

Hi dman,  
yes I confirm that label about spread is not preventing EA opening trade, it's just an advise.  
Maybe your broker doesn't allow for placing pending orders too much near to actual price in my broker this value is 0 pips.  
You can check this by opening the trade window (F9) and select a pending order, you should see something this 'Open price you set must differ from open price by at least X pips' and in my case X = 0 :  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot1.png
Size: 33 KB](/attachment/image/1643096/thumbnail?d=1427711594)](/attachment/image/1643096?d=1427711594)   

  
  
Btw 2.1 pips spread for GU is too much high for Udine system even if you trade in manual without any EA.  
  
Cheers,  
Skyline 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#69](/thread/post/8172996#post8172996 "Post Permalink")

  * Mar 30, 2015 7:36pm  Mar 30, 2015 7:36pm 

  * [ DerBerliner](derberliner)

  * | Joined Feb 2011  | Status: Trader | [822 Posts](/search?do=process&provider=Member&searchuser=168827)

@Traffex: I confirm your result ! Broker is Global Prime.  
  
Ah .. and I see skyline has the same trade in his Trade explorer ! ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#70](/thread/post/8172998#post8172998 "Post Permalink")

  * Mar 30, 2015 7:37pm  Mar 30, 2015 7:37pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting maadz](/thread/post/8172940#post8172940 "View Quoted Post")
> 
> Disliked
> 
> 2nd entry >> Ts @ open price {image}
> 
> Ignored

Same result for me too ! ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#71](/thread/post/8173012#post8173012 "Post Permalink")

  * Mar 30, 2015 7:40pm  Mar 30, 2015 7:40pm 

  * [ dman7800](dman7800)

  * | Joined Sep 2014  | Status: Trader | [31 Posts](/search?do=process&provider=Member&searchuser=382482)

> [Quoting skyline](/thread/post/8172989#post8172989 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi dman, yes I confirm that label about spread is not preventing EA opening trade, it's just an advise. Maybe your broker doesn't allow for placing pending orders too much near to actual price in my broker this value is 0 pips. You can check this by opening the trade window (F9) and select a pending order, you should see something this 'Open price you set must differ from open price by at least X pips' and in my case X = 0 : {image} Btw 2.1 pips spread for GU is too much high for Udine system even if you trade in manual without any EA. Cheers,...
> 
> Ignored

Hi Skyline,  
Yes you are right.. it must differ by 2 pips for my broker..  
  
So I guess you send an order right on the 00 level? Which means I cannot use this with my broker, as you suggested.  
  
Cheers! 

Enter Signature

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#72](/thread/post/8173027#post8173027 "Post Permalink")

  * Mar 30, 2015 7:46pm  Mar 30, 2015 7:46pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar388093_1.gif) firewight](firewight)

  * | Joined Oct 2014  | Status: Trader | [817 Posts](/search?do=process&provider=Member&searchuser=388093)

I also got the GU to TS.  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: EA 1.jpg
Size: 635 KB](/attachment/image/1643110/thumbnail?d=1427712396)](/attachment/image/1643110?d=1427712396)   

Life is like a snickers, its full of nuts!

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#73](/thread/post/8173035#post8173035 "Post Permalink")

  * Mar 30, 2015 7:49pm  Mar 30, 2015 7:49pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar388093_1.gif) firewight](firewight)

  * | Joined Oct 2014  | Status: Trader | [817 Posts](/search?do=process&provider=Member&searchuser=388093)

> [Quoting dman7800](/thread/post/8173012#post8173012 "View Quoted Post")
> 
> Disliked
> 
> So I guess you send an order right on the 00 level? Which means I cannot use this with my broker, as you suggested. Cheers!
> 
> Ignored

It just depends how far away that 00 level is from your market price at any given time... 

Life is like a snickers, its full of nuts!

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#74](/thread/post/8173065#post8173065 "Post Permalink")

  * Mar 30, 2015 8:04pm  Mar 30, 2015 8:04pm 

  * [ mebarrac](mebarrac)

  * | Joined Feb 2015  | Status: Trader | [38 Posts](/search?do=process&provider=Member&searchuser=402218)

Anyone in the U,S using this with a decent ECN broker with low [spreads](/brokers/spreads "View Live Spreads on the Broker Guide"), I can see I'm going to get burned on the GBP/JPY with [FXCM](/brokers/fxcm "View FXCM Broker Profile") spreads  
  
Thanks Tom 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#75](/thread/post/8173072#post8173072 "Post Permalink")

  * Mar 30, 2015 8:08pm  Mar 30, 2015 8:08pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar121788_9.gif) maadz](maadz)

  * Joined Nov 2009 | Status: It must come from a need! | [121 Posts](/search?do=process&provider=Member&searchuser=121788)

It's Daily Pivot 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot1.png
Size: 61 KB](/attachment/image/1643121/thumbnail?d=1427713697)](/attachment/image/1643121?d=1427713697)   

It must come from a need!

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#76](/thread/post/8173086#post8173086 "Post Permalink")

  * Mar 30, 2015 8:14pm  Mar 30, 2015 8:14pm 

  * [ DerBerliner](derberliner)

  * | Joined Feb 2011  | Status: Trader | [822 Posts](/search?do=process&provider=Member&searchuser=168827)

Have to confirm the actual 10 pips loss on GBPJPY with GP ! ![](https://resources.faireconomy.media/images/emojis/64/1f630.png?v=15.1)  
  
[http://www.myfxbook.com/members/TGT_...rading/1201341](http://www.myfxbook.com/members/TGT_FX/udine-ea-v114-00level-trading/1201341)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#77](/thread/post/8173091#post8173091 "Post Permalink")

  * Mar 30, 2015 8:15pm  Mar 30, 2015 8:15pm 

  * [ Traffex](traffex)

  * | Joined Nov 2013  | Status: Trader | [366 Posts](/search?do=process&provider=Member&searchuser=356934)

> [Quoting DerBerliner](/thread/post/8173086#post8173086 "View Quoted Post")
> 
> Disliked
> 
> Have to confirm the actual 10 pips loss on GBPJPY with GP !
> 
> Ignored

Same loss. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#78](/thread/post/8173104#post8173104 "Post Permalink")

  * Mar 30, 2015 8:19pm  Mar 30, 2015 8:19pm 

  * [ DerBerliner](derberliner)

  * | Joined Feb 2011  | Status: Trader | [822 Posts](/search?do=process&provider=Member&searchuser=168827)

Good to see this strong conformity using different brokers by different traders ! ![](https://resources.faireconomy.media/images/emojis/64/1f44f.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#79](/thread/post/8173129#post8173129 "Post Permalink")

  * Mar 30, 2015 8:34pm  Mar 30, 2015 8:34pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar375828_2.gif) JibalaPasan](jibalapasan)

  * Joined Jun 2014 | Status: Trader | [2,498 Posts](/search?do=process&provider=Member&searchuser=375828)

> [Quoting skyline](/thread/post/8172989#post8172989 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi dman, yes I confirm that label about spread is not preventing EA opening trade, it's just an advise. Maybe your broker doesn't allow for placing pending orders too much near to actual price in my broker this value is 0 pips. You can check this by opening the trade window (F9) and select a pending order, you should see something this 'Open price you set must differ from open price by at least X pips' and in my case X = 0 : {image} Btw 2.1 pips spread for GU is too much high for Udine system even if you trade in manual without any EA. Cheers,...
> 
> Ignored

Hello @Skyline,  
  
first of all, great work! I just sit back and compare signals but I have to confirm @dman7800's statement, no more trade since the EU (I got the same signal!). But after that there should have been signal on GU & GJ.  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Ashampoo_Snap_2015.03.30_19h08m03s_003_.png
Size: 98 KB](/attachment/image/1643143/thumbnail?d=1427715118)](/attachment/image/1643143?d=1427715118)   

  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Ashampoo_Snap_2015.03.30_18h53m06s_002_Order.png
Size: 34 KB](/attachment/image/1643142/thumbnail?d=1427715112)](/attachment/image/1643142?d=1427715112)   

  
Jibala 

PDF & BCC (Patience Discipline Focus & Belief Confidence Consistency)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#80](/thread/post/8173145#post8173145 "Post Permalink")

  * Mar 30, 2015 8:43pm  Mar 30, 2015 8:43pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting DerBerliner](/thread/post/8173086#post8173086 "View Quoted Post")
> 
> Disliked
> 
> Have to confirm the actual 10 pips loss on GBPJPY with GP ! ![](https://resources.faireconomy.media/images/emojis/64/1f630.png?v=15.1) [http://www.myfxbook.com/members/TGT_...rading/1201341](http://www.myfxbook.com/members/TGT_FX/udine-ea-v114-00level-trading/1201341)
> 
> Ignored

Loss also for me on GJ 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * UdineEA Official Thread
  *   * [ **Reply to Thread** ](/thread/533099-udineea-official-thread/reply#reply)

  * More

[](https://www.forexfactory.com "Homepage")

  * [Forums](forums)
  * [Trades](trades)
  * [Calendar](calendar)
  * [News](news)
  * [Market](market)
  * [Brokers](brokers)

****

[](https://www.faireconomy.com/)

  * 

[The Official "Ok, now I'm pissed" Thread](/thread/73546-the-official-ok-now-im-pissed-thread "Hello Everyone, 
 
Seeing the apparent lack of threads of this nature \(just kidding, but read on\) I have decided to set up a respectable...") 51 replies

[Historic Charts: NZ Official Cash Rate](/thread/20380-historic-charts-nz-official-cash-rate "Sep 14, 2005") 15 replies

[Is there an official exchange rate?!](/thread/11571-is-there-an-official-exchange-rate "Different brokers have different bid and ask prices for every cross or pair.  However, the bid and ask price is based on something...I am...") 14 replies

[Official forex time zone](/thread/9940-official-forex-time-zone "is there a standard forex time zone? do i follow gmt or NY time? i use 4 hour charts and sometimes the time is way off because of time zone...") 3 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/533099-udineea-official-thread/reply#reply)
  * Subscribe
  * [100](javascript:void\(0\);)

Attachments: UdineEA Official Thread

Tags: UdineEA Official Thread

#  [](/thread/533099-udineea-official-thread)UdineEA Official Thread 

  * 

  * [#81](/thread/post/8173155#post8173155 "Post Permalink")

  * Mar 30, 2015 8:46pm  Mar 30, 2015 8:46pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting JibalaPasan](/thread/post/8173129#post8173129 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hello @Skyline, first of all, great work! I just sit back and compare signals but I have to confirm @dman7800's statement, no more trade since the EU (I got the same signal!). But after that there should have been signal on GU & GJ. {image} {image} Jibala
> 
> Ignored

Hi Jibala,  
looking at your chart there's no signal on GU (ASH color changed earlier from green to red) but there should be a valid entry on GJ , check if you have any error in Expert/Journal tab or maybe there was some conditions that I cannot see that invalidate trade in your platform. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#82](/thread/post/8173160#post8173160 "Post Permalink")

  * Mar 30, 2015 8:48pm  Mar 30, 2015 8:48pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar378281_1.gif) ChrisGC](chrisgc)

  * | Joined Jul 2014  | Status: Trader | [192 Posts](/search?do=process&provider=Member&searchuser=378281)

Looks like its working for me?  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Capture.JPG
Size: 189 KB](/attachment/image/1643156/thumbnail?d=1427716099)](/attachment/image/1643156?d=1427716099)   

The problem is not giving offence but taking offence!

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#83](/thread/post/8173166#post8173166 "Post Permalink")

  * Mar 30, 2015 8:50pm  Mar 30, 2015 8:50pm 

  * [ mebarrac](mebarrac)

  * | Joined Feb 2015  | Status: Trader | [38 Posts](/search?do=process&provider=Member&searchuser=402218)

Any idea what happened here on the GBP JPY trade withe sell stop instead of sell order?  
<http://i.imgur.com/1fp9t1I.jpg>

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#84](/thread/post/8173176#post8173176 "Post Permalink")

  * Mar 30, 2015 8:54pm  Mar 30, 2015 8:54pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar375828_2.gif) JibalaPasan](jibalapasan)

  * Joined Jun 2014 | Status: Trader | [2,498 Posts](/search?do=process&provider=Member&searchuser=375828)

> [Quoting skyline](/thread/post/8173155#post8173155 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi Jibala, looking at your chart there's no signal on GU (ASH color changed earlier from green to red) but there should be a valid entry on GJ , check if you have any error in Expert/Journal tab or maybe there was some conditions that I cannot see that invalidate trade in your platform.
> 
> Ignored

Sorry, in the journal there is nothing! The only trade(s) (some from basket I finished already) and the only one with the higher lot size is EU! No errors in journal or something like this. That was the first I was looking for, prior to my post.  
  
Jibala  
  
Edit: I just saw this:  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Ashampoo_Snap_2015.03.30_19h56m34s_005_.png
Size: 33 KB](/attachment/image/1643163/thumbnail?d=1427716643)](/attachment/image/1643163?d=1427716643)   

  
It's because of the M-Candles? 

PDF & BCC (Patience Discipline Focus & Belief Confidence Consistency)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#85](/thread/post/8173201#post8173201 "Post Permalink")

  * Mar 30, 2015 9:09pm  Mar 30, 2015 9:09pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting mebarrac](/thread/post/8173166#post8173166 "View Quoted Post")
> 
> Disliked
> 
> Any idea what happened here on the GBP JPY trade withe sell stop instead of sell order? {image}
> 
> Ignored

All trades are sellstop or buystop then if triggered become sell order or buy order. It seems your sell stop wasn't triggered , maybe not enough margin left ? Check in platform Journal/Expert tab. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#86](/thread/post/8173210#post8173210 "Post Permalink")

  * Mar 30, 2015 9:13pm  Mar 30, 2015 9:13pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting JibalaPasan](/thread/post/8173176#post8173176 "View Quoted Post")
> 
> Disliked
> 
> {quote} Sorry, in the journal there is nothing! The only trade(s) (some from basket I finished already) and the only one with the higher lot size is EU! No errors in journal or something like this. That was the first I was looking for, prior to my post. Jibala Edit: I just saw this: {image} It's because of the M-Candles?
> 
> Ignored

  
No it's not M-Candles, maybe didn't you have enough margin left to open position ? It's hard for me to say what's your problem just looking at a screenshot , sorry ![](https://resources.faireconomy.media/images/emojis/64/1f641.png?v=15.1)  
Btw, my advice is to test in a fresh demo account running only UdineEA (no other trades opened manually or by other EAs).  
  
Cheers,  
Skyline 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#87](/thread/post/8173504#post8173504 "Post Permalink")

  * Mar 30, 2015 11:01pm  Mar 30, 2015 11:01pm 

  * [ mebarrac](mebarrac)

  * | Joined Feb 2015  | Status: Trader | [38 Posts](/search?do=process&provider=Member&searchuser=402218)

> [Quoting skyline](/thread/post/8173201#post8173201 "View Quoted Post")
> 
> Disliked
> 
> {quote} All trades are sellstop or buystop then if triggered become sell order or buy order. It seems your sell stop wasn't triggered , maybe not enough margin left ? Check in platform Journal/Expert tab.
> 
> Ignored

Thanks Skyline ; I think that was it, the demo I opened defaulted to 50k zero margin!, I opened another demo on [FXCM](/brokers/fxcm "View FXCM Broker Profile") with the smallest account size possible to account for the zero margin. Hopefully it will enter correctly now.  
  
thanks again for the support  
  
Tom 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#88](/thread/post/8173569#post8173569 "Post Permalink")

  * Mar 30, 2015 11:26pm  Mar 30, 2015 11:26pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting mebarrac](/thread/post/8173504#post8173504 "View Quoted Post")
> 
> Disliked
> 
> {quote} Thanks Skyline ; I think that was it, the demo I opened defaulted to 50k zero margin!, I opened another demo on FXCM with the smallest account size possible to account for the zero margin. Hopefully it will enter correctly now. thanks again for the support Tom
> 
> Ignored

![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#89](/thread/post/8173610#post8173610 "Post Permalink")

  * Mar 30, 2015 11:41pm  Mar 30, 2015 11:41pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar375828_2.gif) JibalaPasan](jibalapasan)

  * Joined Jun 2014 | Status: Trader | [2,498 Posts](/search?do=process&provider=Member&searchuser=375828)

> [Quoting skyline](/thread/post/8173210#post8173210 "View Quoted Post")
> 
> Disliked
> 
> {quote} No it's not M-Candles, maybe didn't you have enough margin left to open position ? It's hard for me to say what's your problem just looking at a screenshot , sorry ![](https://resources.faireconomy.media/images/emojis/64/1f641.png?v=15.1) Btw, my advice is to test in a fresh demo account running only UdineEA (no other trades opened manually or by other EAs). Cheers, Skyline
> 
> Ignored

I dont know how old you are, me pretty young but it seems we both need an eye glasses! :nerd:  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Ashampoo_Snap_2015.03.30_21h00m16s_006_.png
Size: 97 KB](/attachment/image/1643302/thumbnail?d=1427726440)](/attachment/image/1643302?d=1427726440)   

  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Ashampoo_Snap_2015.03.30_21h03m01s_007_Expert - Udine EA-v114.png
Size: 29 KB](/attachment/image/1643303/thumbnail?d=1427726447)](/attachment/image/1643303?d=1427726447)   

  
Next trade on GJ => TP  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Ashampoo_Snap_2015.03.30_22h37m54s_010_.png
Size: 93 KB](/attachment/image/1643300/thumbnail?d=1427726366)](/attachment/image/1643300?d=1427726366)   

  
Jibala 

PDF & BCC (Patience Discipline Focus & Belief Confidence Consistency)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#90](/thread/post/8173626#post8173626 "Post Permalink")

  * Mar 30, 2015 11:47pm  Mar 30, 2015 11:47pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

Good catch Jibala (btw I'm 42 not so young ![](https://resources.faireconomy.media/images/emojis/64/1f61e.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)) 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#91](/thread/post/8173627#post8173627 "Post Permalink")

  * Mar 30, 2015 11:47pm  Mar 30, 2015 11:47pm 

  * [ mebarrac](mebarrac)

  * | Joined Feb 2015  | Status: Trader | [38 Posts](/search?do=process&provider=Member&searchuser=402218)

spoke to soon im getting an invalid sl tp message now on my new demo...any ideas?  
  
<http://i.imgur.com/HPsY1xS.jpg>  
  
<http://i.imgur.com/PvhdXoW.jpg>

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#92](/thread/post/8173642#post8173642 "Post Permalink")

  * Edited Mar 31, 2015 12:03am  Mar 30, 2015 11:53pm | Edited Mar 31, 2015 12:03am 

  * [ DerBerliner](derberliner)

  * | Joined Feb 2011  | Status: Trader | [822 Posts](/search?do=process&provider=Member&searchuser=168827)

Recently I got another trade with GBPJPY (btw: entry 117.60 !), hit the TP: + 5 pips ! ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#93](/thread/post/8173647#post8173647 "Post Permalink")

  * Mar 30, 2015 11:55pm  Mar 30, 2015 11:55pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting mebarrac](/thread/post/8173627#post8173627 "View Quoted Post")
> 
> Disliked
> 
> spoke to soon im getting an invalid sl tp message now on my new demo...any ideas? {image} {image}
> 
> Ignored

Check this post : [http://www.forexfactory.com/showthre...89#post8172989](http://www.forexfactory.com/showthread.php?p=8172989#post8172989)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#94](/thread/post/8173667#post8173667 "Post Permalink")

  * Mar 31, 2015 12:00am  Mar 31, 2015 12:00am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting DerBerliner](/thread/post/8173642#post8173642 "View Quoted Post")
> 
> Disliked
> 
> Recently I got another trade with GBPJPY (btw: entry 117.60 !), hit the TP - 5 pips ! ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)
> 
> Ignored

Yes !  
This is my current situation up to now (0 pips) :  
  

Attached Image

![](/attachment/image/1643321?d=1427727543)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#95](/thread/post/8173695#post8173695 "Post Permalink")

  * Mar 31, 2015 12:11am  Mar 31, 2015 12:11am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar357421_1.gif) bazze](bazze)

  * | Joined Dec 2013  | Status: Trader | [1,135 Posts](/search?do=process&provider=Member&searchuser=357421)

So far today.....ootb 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Global Prime3.png
Size: 146 KB](/attachment/image/1643328/thumbnail?d=1427728269)](/attachment/image/1643328?d=1427728269)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#96](/thread/post/8173701#post8173701 "Post Permalink")

  * Mar 31, 2015 12:13am  Mar 31, 2015 12:13am 

  * [ mebarrac](mebarrac)

  * | Joined Feb 2015  | Status: Trader | [38 Posts](/search?do=process&provider=Member&searchuser=402218)

> [Quoting skyline](/thread/post/8173647#post8173647 "View Quoted Post")
> 
> Disliked
> 
> {quote} Check this post : [http://www.forexfactory.com/showthre...89#post8172989](http://www.forexfactory.com/showthread.php?p=8172989#post8172989)
> 
> Ignored

Yes , I have the same screen as you there, set to zero, so that doesn't appear to be the issue with this one. will try and shut everything down and restart and see if I can get a trade to enter right.  
  
Thanks again 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#97](/thread/post/8173703#post8173703 "Post Permalink")

  * Mar 31, 2015 12:15am  Mar 31, 2015 12:15am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar379623_3.gif) RoneyFX](roneyfx)

  * | Joined Aug 2014  | Status: Trader | [129 Posts](/search?do=process&provider=Member&searchuser=379623)

Compliments for the EA  
I think you must add command stop when reached daily target a choice like 2% or 2wins 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#98](/thread/post/8173752#post8173752 "Post Permalink")

  * Mar 31, 2015 12:36am  Mar 31, 2015 12:36am 

  * [ mary4x](mary4x)

  * | Joined May 2009  | Status: Trader | [616 Posts](/search?do=process&provider=Member&searchuser=103730)

Traffex, you have a pm. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#99](/thread/post/8173754#post8173754 "Post Permalink")

  * Edited 1:01am  Mar 31, 2015 12:36am | Edited 1:01am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar338950_1.gif) cescof](cescof)

  * Joined Jun 2013 | Status: Trader | [1,006 Posts](/search?do=process&provider=Member&searchuser=338950)

Hy and sorry for question but why i don't have this pending order at 177.8 for GBP/JPY  
  
<http://gyazo.com/557b3807aac5666c7c13b03806505e10>  
  
What's wrong? Seems all conditions are ok..  
Regards  
  
edit... but i din't have any pending order so mybe it's not spread related... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#100](/thread/post/8173780#post8173780 "Post Permalink")

  * Mar 31, 2015 12:47am  Mar 31, 2015 12:47am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar379623_3.gif) RoneyFX](roneyfx)

  * | Joined Aug 2014  | Status: Trader | [129 Posts](/search?do=process&provider=Member&searchuser=379623)

I saw that there is already present 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * UdineEA Official Thread
  *   * [ **Reply to Thread** ](/thread/533099-udineea-official-thread/reply#reply)

  * More

[](https://www.forexfactory.com "Homepage")

  * [Forums](forums)
  * [Trades](trades)
  * [Calendar](calendar)
  * [News](news)
  * [Market](market)
  * [Brokers](brokers)

****

[](https://www.faireconomy.com/)

  * 

[The Official "Ok, now I'm pissed" Thread](/thread/73546-the-official-ok-now-im-pissed-thread "Hello Everyone, 
 
Seeing the apparent lack of threads of this nature \(just kidding, but read on\) I have decided to set up a respectable...") 51 replies

[Historic Charts: NZ Official Cash Rate](/thread/20380-historic-charts-nz-official-cash-rate "Sep 14, 2005") 15 replies

[Is there an official exchange rate?!](/thread/11571-is-there-an-official-exchange-rate "Different brokers have different bid and ask prices for every cross or pair.  However, the bid and ask price is based on something...I am...") 14 replies

[Official forex time zone](/thread/9940-official-forex-time-zone "is there a standard forex time zone? do i follow gmt or NY time? i use 4 hour charts and sometimes the time is way off because of time zone...") 3 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/533099-udineea-official-thread/reply#reply)
  * Subscribe
  * [100](javascript:void\(0\);)

Attachments: UdineEA Official Thread

Tags: UdineEA Official Thread

#  [](/thread/533099-udineea-official-thread)UdineEA Official Thread 

  * 

  * [#101](/thread/post/8173792#post8173792 "Post Permalink")

  * Mar 31, 2015 12:51am  Mar 31, 2015 12:51am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar375828_2.gif) JibalaPasan](jibalapasan)

  * Joined Jun 2014 | Status: Trader | [2,498 Posts](/search?do=process&provider=Member&searchuser=375828)

> [Quoting cescof](/thread/post/8173754#post8173754 "View Quoted Post")
> 
> Disliked
> 
> Hy and sorry for question but why i don't have this pending order at 177.8 for GBP/JPY <http://gyazo.com/557b3807aac5666c7c13b03806505e10> What's wrong? Seems all conditions are ok.. Regards
> 
> Ignored

Imho the spread was at that moment a little bit to high!  
  
Jibala  
  
Edit: Limit of 1.5 for some pairs to small! 

PDF & BCC (Patience Discipline Focus & Belief Confidence Consistency)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#102](/thread/post/8173804#post8173804 "Post Permalink")

  * Mar 31, 2015 12:57am  Mar 31, 2015 12:57am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar338950_1.gif) cescof](cescof)

  * Joined Jun 2013 | Status: Trader | [1,006 Posts](/search?do=process&provider=Member&searchuser=338950)

> [Quoting JibalaPasan](/thread/post/8173792#post8173792 "View Quoted Post")
> 
> Disliked
> 
> {quote} Imho the spread was at that moment a little bit to high! Jibala Edit: Limit of 1.5 for some pairs to small!
> 
> Ignored

Yes maybe you're right.... but i think could be really better if spread doesn't hard coded..  
Regards 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#103](/thread/post/8173832#post8173832 "Post Permalink")

  * Mar 31, 2015 1:05am  Mar 31, 2015 1:05am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar375828_2.gif) JibalaPasan](jibalapasan)

  * Joined Jun 2014 | Status: Trader | [2,498 Posts](/search?do=process&provider=Member&searchuser=375828)

I have canceled GU short. Imho GBP still too much strong for short!  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Ashampoo_Snap_2015.03.31_00h03m23s_011_.png
Size: 97 KB](/attachment/image/1643397/thumbnail?d=1427731492)](/attachment/image/1643397?d=1427731492)   

  
Jibala 

PDF & BCC (Patience Discipline Focus & Belief Confidence Consistency)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#104](/thread/post/8173901#post8173901 "Post Permalink")

  * Mar 31, 2015 1:26am  Mar 31, 2015 1:26am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar379623_3.gif) RoneyFX](roneyfx)

  * | Joined Aug 2014  | Status: Trader | [129 Posts](/search?do=process&provider=Member&searchuser=379623)

the backtest it takes a really long time but I'm going to find the best settings for each currency, someone has already done something like this??  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: oback.PNG
Size: 13 KB](/attachment/image/1643416/thumbnail?d=1427732792)](/attachment/image/1643416?d=1427732792)   

  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: modx.PNG
Size: 11 KB](/attachment/image/1643417/thumbnail?d=1427732802)](/attachment/image/1643417?d=1427732802)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#105](/thread/post/8173906#post8173906 "Post Permalink")

  * Mar 31, 2015 1:27am  Mar 31, 2015 1:27am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar350360_20.gif) AKCodingEye](akcodingeye)

  * Joined Sep 2013 | Status: Such a Silly Game It is | [181 Posts](/search?do=process&provider=Member&searchuser=350360)

Thanks for sharing EA ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)  
Testing out on [FXCM](/brokers/fxcm "View FXCM Broker Profile") Demo on my VPS atm for all four pairs. 

Whats get measured get improved

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#106](/thread/post/8173910#post8173910 "Post Permalink")

  * Mar 31, 2015 1:30am  Mar 31, 2015 1:30am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar389954_3.gif) honestknave](honestknave)

  * Joined Nov 2014 | Status: Trader | [1,300 Posts](/search?do=process&provider=Member&searchuser=389954)

> [Quoting RoneyFX](/thread/post/8173901#post8173901 "View Quoted Post")
> 
> Disliked
> 
> the backtest it takes a really long time but I'm going to find the best settings for each currency, someone has already done something like this?? {image} {image}
> 
> Ignored

Hello RoneyFX,  
How are you dealing with the historical news issue for backtesting? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#107](/thread/post/8173915#post8173915 "Post Permalink")

  * Mar 31, 2015 1:33am  Mar 31, 2015 1:33am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar258750_3.gif) rochild](rochild)

  * | Joined May 2012  | Status: Trader | [77 Posts](/search?do=process&provider=Member&searchuser=258750)

Not working for me on fxcm demo,pending order doesn't appear on the chart.probably because high spread (2.5 pips) 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#108](/thread/post/8173916#post8173916 "Post Permalink")

  * Mar 31, 2015 1:34am  Mar 31, 2015 1:34am 

  * [ mebarrac](mebarrac)

  * | Joined Feb 2015  | Status: Trader | [38 Posts](/search?do=process&provider=Member&searchuser=402218)

my GBP USD trade is still running never hit stop loss , seems like the ea has issues with the TP and SL on fxcm broker  
sl and tp are always listed as 0.00000 in the order entry part  
  
Is there anything anyone can think of , I really don't want to switch brokers because fxcm is the only one for us clients that will come close to the [spreads](/brokers/spreads "View Live Spreads on the Broker Guide") required.  
  
Thanks Tom 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#109](/thread/post/8173920#post8173920 "Post Permalink")

  * Mar 31, 2015 1:35am  Mar 31, 2015 1:35am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar379623_3.gif) RoneyFX](roneyfx)

  * | Joined Aug 2014  | Status: Trader | [129 Posts](/search?do=process&provider=Member&searchuser=379623)

> [Quoting honestknave](/thread/post/8173910#post8173910 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hello RoneyFX, How are you dealing with the historical news issue for backtesting?
> 
> Ignored

no matter, I take 50 trade and watch the results with the original settings and begin to edit SL / TP / TS until I find the best results, when i get it i do a test of 1 year to see if i actually improved it 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#110](/thread/post/8173922#post8173922 "Post Permalink")

  * Mar 31, 2015 1:38am  Mar 31, 2015 1:38am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar389954_3.gif) honestknave](honestknave)

  * Joined Nov 2014 | Status: Trader | [1,300 Posts](/search?do=process&provider=Member&searchuser=389954)

> [Quoting mebarrac](/thread/post/8173916#post8173916 "View Quoted Post")
> 
> Disliked
> 
> my GBP USD trade is still running never hit stop loss , seems like the ea has issues with the TP and SL on fxcm broker sl and tp are always listed as 0.00000 in the order entry part Is there anything anyone can think of , I really don't want to switch brokers because fxcm is the only one for us clients that will come close to the spreads required. Thanks Tom
> 
> Ignored

Some brokers require you to place the order THEN set the stops (through OrderModify).  
Not sure how the EA is coded... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#111](/thread/post/8173924#post8173924 "Post Permalink")

  * Mar 31, 2015 1:38am  Mar 31, 2015 1:38am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar389954_3.gif) honestknave](honestknave)

  * Joined Nov 2014 | Status: Trader | [1,300 Posts](/search?do=process&provider=Member&searchuser=389954)

> [Quoting RoneyFX](/thread/post/8173920#post8173920 "View Quoted Post")
> 
> Disliked
> 
> {quote} no matter, I take 50 trade and watch the results with the original settings and begin to edit SL / TP / TS until I find the best results, when i get it i do a test of 1 year to see if i actually improved it
> 
> Ignored

So you're essentially testing it without any news filter? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#112](/thread/post/8173932#post8173932 "Post Permalink")

  * Mar 31, 2015 1:41am  Mar 31, 2015 1:41am 

  * [ mebarrac](mebarrac)

  * | Joined Feb 2015  | Status: Trader | [38 Posts](/search?do=process&provider=Member&searchuser=402218)

> [Quoting honestknave](/thread/post/8173922#post8173922 "View Quoted Post")
> 
> Disliked
> 
> {quote} Some brokers require you to place the order THEN set the stops (through OrderModify). Not sure how the EA is coded...
> 
> Ignored

yeah its looking more and more like that .....bugger the U.S and its restrictions...anyone know of a good U.S broker other than FXCM with low spreads? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#113](/thread/post/8173940#post8173940 "Post Permalink")

  * Mar 31, 2015 1:44am  Mar 31, 2015 1:44am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar379623_3.gif) RoneyFX](roneyfx)

  * | Joined Aug 2014  | Status: Trader | [129 Posts](/search?do=process&provider=Member&searchuser=379623)

> [Quoting honestknave](/thread/post/8173924#post8173924 "View Quoted Post")
> 
> Disliked
> 
> {quote} So you're essentially testing it without any news filter?
> 
> Ignored

I should do the calculations manually subtracting the trade made during the news and this will be a suicide, in both cases the tests are made on the same orders so no matter 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#114](/thread/post/8173962#post8173962 "Post Permalink")

  * Mar 31, 2015 1:57am  Mar 31, 2015 1:57am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting mebarrac](/thread/post/8173701#post8173701 "View Quoted Post")
> 
> Disliked
> 
> {quote} Yes , I have the same screen as you there, set to zero, so that doesn't appear to be the issue with this one. will try and shut everything down and restart and see if I can get a trade to enter right. Thanks again
> 
> Ignored

That's strange, maybe daily target 2% reached ? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#115](/thread/post/8173963#post8173963 "Post Permalink")

  * Mar 31, 2015 1:59am  Mar 31, 2015 1:59am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting cescof](/thread/post/8173754#post8173754 "View Quoted Post")
> 
> Disliked
> 
> Hy and sorry for question but why i don't have this pending order at 177.8 for GBP/JPY <http://gyazo.com/557b3807aac5666c7c13b03806505e10> What's wrong? Seems all conditions are ok.. Regards edit... but i din't have any pending order so mybe it's not spread related...
> 
> Ignored

Check Udine level 1 rules again Cescof, from your screenshot ASH is always green (did not turn from red to green) , so no entry 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#116](/thread/post/8173974#post8173974 "Post Permalink")

  * Mar 31, 2015 2:03am  Mar 31, 2015 2:03am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting JibalaPasan](/thread/post/8173792#post8173792 "View Quoted Post")
> 
> Disliked
> 
> {quote} Imho the spread was at that moment a little bit to high! Jibala Edit: Limit of 1.5 for some pairs to small!
> 
> Ignored

I already wrote some post ago, spread is not taken into account to place pending orders, it's only a visual information to the trader but EA ignores it !! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#117](/thread/post/8173996#post8173996 "Post Permalink")

  * Mar 31, 2015 2:12am  Mar 31, 2015 2:12am 

  * [ mebarrac](mebarrac)

  * | Joined Feb 2015  | Status: Trader | [38 Posts](/search?do=process&provider=Member&searchuser=402218)

> [Quoting skyline](/thread/post/8173962#post8173962 "View Quoted Post")
> 
> Disliked
> 
> {quote} That's strange, maybe daily target 2% reached ?
> 
> Ignored

skyline : I haven't been able to get in or out of a trade properly since open so i don't think this is it , still trying to figure this all out  
I have made some progress today in that it gets into a trade o.k. without error but the sl and tp are zero and I can't get out without manually adjusting them , someone said I may have to go in manually and edit the sl and tp with some brokers , everything is zero by default when I go into the order. I hope I don't have to do this.  
  
Thanks Tom 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#118](/thread/post/8174000#post8174000 "Post Permalink")

  * Mar 31, 2015 2:13am  Mar 31, 2015 2:13am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting honestknave](/thread/post/8173922#post8173922 "View Quoted Post")
> 
> Disliked
> 
> {quote} Some brokers require you to place the order THEN set the stops (through OrderModify). Not sure how the EA is coded...
> 
> Ignored

that's exactly how this EA works, pending orders are placed without any sl,tp then when activated are modified , so it's weird is not working on fxcm, will try to test on it... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#119](/thread/post/8174003#post8174003 "Post Permalink")

  * Mar 31, 2015 2:14am  Mar 31, 2015 2:14am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting mebarrac](/thread/post/8173996#post8173996 "View Quoted Post")
> 
> Disliked
> 
> {quote} skyline : I haven't been able to get in or out of a trade properly since open so i don't think this is it , still trying to figure this all out I have made some progress today in that it gets into a trade o.k. without error but the sl and tp are zero and I can't get out without manually adjusting them , someone said I may have to go in manually and edit the sl and tp with some brokers , everything is zero by default when I go into the order. I hope I don't have to do this. Thanks Tom
> 
> Ignored

yes that's very strange, will look into this issue 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#120](/thread/post/8174062#post8174062 "Post Permalink")

  * Mar 31, 2015 2:42am  Mar 31, 2015 2:42am 

  * [ mebarrac](mebarrac)

  * | Joined Feb 2015  | Status: Trader | [38 Posts](/search?do=process&provider=Member&searchuser=402218)

> [Quoting skyline](/thread/post/8174003#post8174003 "View Quoted Post")
> 
> Disliked
> 
> {quote} yes that's very strange, will look into this issue
> 
> Ignored

thanks , will keep an eye on it , it seems pretty repeatable now though , at least for me . looking at the locations of people running FXCM , they all seem to be from europe , like yourself . but I doubt the server location will make a difference.  
  
let me know if you want me to help and test anything this end 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * UdineEA Official Thread
  *   * [ **Reply to Thread** ](/thread/533099-udineea-official-thread/reply#reply)

  * More

[](https://www.forexfactory.com "Homepage")

  * [Forums](forums)
  * [Trades](trades)
  * [Calendar](calendar)
  * [News](news)
  * [Market](market)
  * [Brokers](brokers)

****

[](https://www.faireconomy.com/)

  * 

[The Official "Ok, now I'm pissed" Thread](/thread/73546-the-official-ok-now-im-pissed-thread "Hello Everyone, 
 
Seeing the apparent lack of threads of this nature \(just kidding, but read on\) I have decided to set up a respectable...") 51 replies

[Historic Charts: NZ Official Cash Rate](/thread/20380-historic-charts-nz-official-cash-rate "Sep 14, 2005") 15 replies

[Is there an official exchange rate?!](/thread/11571-is-there-an-official-exchange-rate "Different brokers have different bid and ask prices for every cross or pair.  However, the bid and ask price is based on something...I am...") 14 replies

[Official forex time zone](/thread/9940-official-forex-time-zone "is there a standard forex time zone? do i follow gmt or NY time? i use 4 hour charts and sometimes the time is way off because of time zone...") 3 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/533099-udineea-official-thread/reply#reply)
  * Subscribe
  * [100](javascript:void\(0\);)

Attachments: UdineEA Official Thread

Tags: UdineEA Official Thread

#  [](/thread/533099-udineea-official-thread)UdineEA Official Thread 

  * 

  * [#121](/thread/post/8174401#post8174401 "Post Permalink")

  * Mar 31, 2015 6:46am  Mar 31, 2015 6:46am 

  * [ TwoUp](twoup)

  * | Joined Oct 2014  | Status: Trader | [37 Posts](/search?do=process&provider=Member&searchuser=384929)

Thanks for your generosity Skyline. looks like you have put a lot of effort in developing this EA. H/T!  
I have set time to trade to false since my day job prevents me from trading the preset hours. I will test and share the results of the hours I am able to trade.  
Regards,  
TwoUp 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#122](/thread/post/8175070#post8175070 "Post Permalink")

  * Mar 31, 2015 4:14pm  Mar 31, 2015 4:14pm 

  * [ Bhutugly](bhutugly)

  * | Joined Oct 2011  | Status: Trader | [12 Posts](/search?do=process&provider=Member&searchuser=200586)

Skyline,  
  
congratulations and thanks for this.  
  
Just one quick question, will these EA work correctly if i'm running Wheelbarrow and WUKAR?  
  
Cheers  
  
Ian 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#123](/thread/post/8175136#post8175136 "Post Permalink")

  * Mar 31, 2015 4:38pm  Mar 31, 2015 4:38pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting Bhutugly](/thread/post/8175070#post8175070 "View Quoted Post")
> 
> Disliked
> 
> Skyline, congratulations and thanks for this. Just one quick question, will these EA work correctly if i'm running Wheelbarrow and WUKAR? Cheers Ian
> 
> Ignored

UdineEA will handle trailingstop (even if not hiding because it's very risk to not use SL,TP if connection is lost) so there's no need to use other EA like Wheelbarrow or WUKAR, which could create problems, so it's better to use only UdineEA on your chart (and account).  
  
Cheers,  
Skyline 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#124](/thread/post/8175194#post8175194 "Post Permalink")

  * Mar 31, 2015 5:01pm  Mar 31, 2015 5:01pm 

  * [ Bhutugly](bhutugly)

  * | Joined Oct 2011  | Status: Trader | [12 Posts](/search?do=process&provider=Member&searchuser=200586)

Thanks  
  
Will sort it out when I get back.  
  
Cheers  
  
Ian 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#125](/thread/post/8175293#post8175293 "Post Permalink")

  * Mar 31, 2015 5:27pm  Mar 31, 2015 5:27pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar389954_3.gif) honestknave](honestknave)

  * Joined Nov 2014 | Status: Trader | [1,300 Posts](/search?do=process&provider=Member&searchuser=389954)

> [Quoting skyline](/thread/post/8174000#post8174000 "View Quoted Post")
> 
> Disliked
> 
> {quote} that's exactly how this EA works, pending orders are placed without any sl,tp then when activated are modified , so it's weird is not working on fxcm, will try to test on it...
> 
> Ignored

![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#126](/thread/post/8175566#post8175566 "Post Permalink")

  * Mar 31, 2015 7:01pm  Mar 31, 2015 7:01pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar350360_20.gif) AKCodingEye](akcodingeye)

  * Joined Sep 2013 | Status: Such a Silly Game It is | [181 Posts](/search?do=process&provider=Member&searchuser=350360)

No trade so far by EA. There are lots of news today so might be in Afternoon 

Whats get measured get improved

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#127](/thread/post/8175587#post8175587 "Post Permalink")

  * Mar 31, 2015 7:10pm  Mar 31, 2015 7:10pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting AKCodingEye](/thread/post/8175566#post8175566 "View Quoted Post")
> 
> Disliked
> 
> No trade so far by EA. There are lots of news today so might be in Afternoon
> 
> Ignored

Yes AKCodingEye, we have to wait , as told by UDINE PDF & BCC ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#128](/thread/post/8175638#post8175638 "Post Permalink")

  * Edited 8:26pm  Mar 31, 2015 7:37pm | Edited 8:26pm 

  * [ Mariodrugs](mariodrugs)

  * | Membership Revoked  | Joined Dec 2014 | [379 Posts](/search?do=process&provider=Member&searchuser=394832)

1). Why it says 'Spread to HIGH!!!!' 1.9 so high ?  
  
2) Skyline Which broker do you prefer with lowest [spreads](/brokers/spreads "View Live Spreads on the Broker Guide") for this strategy ??  
  
3) trades open automatically or i have to do it handly buy stop sell stop ?  
  
  
My trade on GbpJpy not oppened, why?  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: why no open.png
Size: 166 KB](/attachment/image/1643949/thumbnail?d=1427800813)](/attachment/image/1643949?d=1427800813)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#129](/thread/post/8175707#post8175707 "Post Permalink")

  * Mar 31, 2015 8:10pm  Mar 31, 2015 8:10pm 

  * [ Lopuch](lopuch)

  * | Joined Aug 2006  | Status: Trader | [161 Posts](/search?do=process&provider=Member&searchuser=16379)

In any case, good job, but the fundamental error is that EA affects other orders.  
Respectfully. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#130](/thread/post/8175712#post8175712 "Post Permalink")

  * Mar 31, 2015 8:12pm  Mar 31, 2015 8:12pm 

  * [ mebarrac](mebarrac)

  * | Joined Feb 2015  | Status: Trader | [38 Posts](/search?do=process&provider=Member&searchuser=402218)

Hi Skyline , im noticing these two errors pop up after a while , each time after I reload the mt4 platform. Is this a problem? , could it be related to [fxcm](/brokers/fxcm "View FXCM Broker Profile") issue I was seeing yesterday...no trades yet so haven't see any entry error  
Thanks Tom  
  
<http://i.imgur.com/Vd48YAO.jpg>

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#131](/thread/post/8175727#post8175727 "Post Permalink")

  * Mar 31, 2015 8:19pm  Mar 31, 2015 8:19pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar375828_2.gif) JibalaPasan](jibalapasan)

  * Joined Jun 2014 | Status: Trader | [2,498 Posts](/search?do=process&provider=Member&searchuser=375828)

> [Quoting mebarrac](/thread/post/8175712#post8175712 "View Quoted Post")
> 
> Disliked
> 
> Hi Skyline , im noticing these two errors pop up after a while , each time after I reload the mt4 platform. Is this a problem? , could it be related to fxcm issue I was seeing yesterday...no trades yet so haven't see any entry error Thanks Tom {image}
> 
> Ignored

Did you allow DLL - import?  

Attached Image (click to enlarge)

[![Click to Enlarge

Size: 31 KB](/attachment/image/1643947/thumbnail?d=1427800767)](/attachment/image/1643947?d=1427800767)   

  
Jibala 

PDF & BCC (Patience Discipline Focus & Belief Confidence Consistency)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#132](/thread/post/8175769#post8175769 "Post Permalink")

  * Mar 31, 2015 8:36pm  Mar 31, 2015 8:36pm 

  * [ Mariodrugs](mariodrugs)

  * | Membership Revoked  | Joined Dec 2014 | [379 Posts](/search?do=process&provider=Member&searchuser=394832)

Do I Have to open manually trades or its something wrong with setups ?  
  
GbpJpy trade not oppened...  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: why no open.png
Size: 166 KB](/attachment/image/1643962/thumbnail?d=1427801787)](/attachment/image/1643962?d=1427801787)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#133](/thread/post/8175771#post8175771 "Post Permalink")

  * Mar 31, 2015 8:39pm  Mar 31, 2015 8:39pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting Mariodrugs](/thread/post/8175638#post8175638 "View Quoted Post")
> 
> Disliked
> 
> 1). Why it says 'Spread to HIGH!!!!' 1.9 so high ? 2) Skyline Which broker do you prefer with lowest spreads for this strategy ?? 3) trades open automatically or i have to do it handly buy stop sell stop ? My trade on GbpJpy not oppened, why? {image}
> 
> Ignored

Hi Mariodrugs,  
you have to take your time and read 1st post very carefull, then study Udine's level 1 strategy. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#134](/thread/post/8175775#post8175775 "Post Permalink")

  * Mar 31, 2015 8:44pm  Mar 31, 2015 8:44pm 

  * [ Mariodrugs](mariodrugs)

  * | Membership Revoked  | Joined Dec 2014 | [379 Posts](/search?do=process&provider=Member&searchuser=394832)

> [Quoting skyline](/thread/post/8175771#post8175771 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi Mariodrugs, you have to take your time and read 1st post very carefull, then study Udine's level 1 strategy.
> 
> Ignored

I was studyiong it long time ago. So my question is. This EA robot open trades automatically or have to open manually? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#135](/thread/post/8175780#post8175780 "Post Permalink")

  * Mar 31, 2015 8:47pm  Mar 31, 2015 8:47pm 

  * [ mebarrac](mebarrac)

  * | Joined Feb 2015  | Status: Trader | [38 Posts](/search?do=process&provider=Member&searchuser=402218)

> [Quoting Mariodrugs](/thread/post/8175775#post8175775 "View Quoted Post")
> 
> Disliked
> 
> {quote} I was studyiong it long time ago. So my question is. This EA robot open trades automatically or have to open manually?
> 
> Ignored

Mariodrugs, this is not a valid trade setup yet , study first post and Udines thread, ea should be automatic but you have no trade setup in place yet. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#136](/thread/post/8175785#post8175785 "Post Permalink")

  * Mar 31, 2015 8:48pm  Mar 31, 2015 8:48pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting Mariodrugs](/thread/post/8175775#post8175775 "View Quoted Post")
> 
> Disliked
> 
> {quote} I was studyiong it long time ago. So my question is. This EA robot open trades automatically or have to open manually?
> 
> Ignored

And my question is, why don't you read 1st post of this thread where everything is explained in detail ? ![](https://resources.faireconomy.media/images/emojis/64/1f44e.png?v=15.1)  
  
<http://www.forexfactory.com/showthread.php?t=533099>

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#137](/thread/post/8175786#post8175786 "Post Permalink")

  * Mar 31, 2015 8:49pm  Mar 31, 2015 8:49pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting mebarrac](/thread/post/8175780#post8175780 "View Quoted Post")
> 
> Disliked
> 
> {quote} Mariodrugs, this is not a valid trade setup yet , study first post and Udines thread, ea should be automatic but you have no trade setup in place yet.
> 
> Ignored

![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#138](/thread/post/8175788#post8175788 "Post Permalink")

  * Mar 31, 2015 8:50pm  Mar 31, 2015 8:50pm 

  * [ mebarrac](mebarrac)

  * | Joined Feb 2015  | Status: Trader | [38 Posts](/search?do=process&provider=Member&searchuser=402218)

> [Quoting JibalaPasan](/thread/post/8175727#post8175727 "View Quoted Post")
> 
> Disliked
> 
> {quote} Did you allow DLL - import? {image} Jibala
> 
> Ignored

Jibala : no I did not , thank you for pointing that out, maybe that was my problem - we will see!  
  
thank you again  
  
Tom 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#139](/thread/post/8175860#post8175860 "Post Permalink")

  * Edited 9:48pm  Mar 31, 2015 9:23pm | Edited 9:48pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

Possible short EU @1.07300  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot1.png
Size: 16 KB](/attachment/image/1643993/thumbnail?d=1427804579)](/attachment/image/1643993?d=1427804579)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#140](/thread/post/8175878#post8175878 "Post Permalink")

  * Mar 31, 2015 9:30pm  Mar 31, 2015 9:30pm 

  * [ Mariodrugs](mariodrugs)

  * | Membership Revoked  | Joined Dec 2014 | [379 Posts](/search?do=process&provider=Member&searchuser=394832)

> [Quoting skyline](/thread/post/8175860#post8175860 "View Quoted Post")
> 
> Disliked
> 
> Possible short EU @1.07300 (and EJ possible short maybe on next candle) {image}
> 
> Ignored

I have the same now ;- )  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: eu possible short.png
Size: 93 KB](/attachment/image/1644001/thumbnail?d=1427805046)](/attachment/image/1644001?d=1427805046)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * UdineEA Official Thread
  *   * [ **Reply to Thread** ](/thread/533099-udineea-official-thread/reply#reply)

  * More

[](https://www.forexfactory.com "Homepage")

  * [Forums](forums)
  * [Trades](trades)
  * [Calendar](calendar)
  * [News](news)
  * [Market](market)
  * [Brokers](brokers)

****

[](https://www.faireconomy.com/)

  * 

[The Official "Ok, now I'm pissed" Thread](/thread/73546-the-official-ok-now-im-pissed-thread "Hello Everyone, 
 
Seeing the apparent lack of threads of this nature \(just kidding, but read on\) I have decided to set up a respectable...") 51 replies

[Historic Charts: NZ Official Cash Rate](/thread/20380-historic-charts-nz-official-cash-rate "Sep 14, 2005") 15 replies

[Is there an official exchange rate?!](/thread/11571-is-there-an-official-exchange-rate "Different brokers have different bid and ask prices for every cross or pair.  However, the bid and ask price is based on something...I am...") 14 replies

[Official forex time zone](/thread/9940-official-forex-time-zone "is there a standard forex time zone? do i follow gmt or NY time? i use 4 hour charts and sometimes the time is way off because of time zone...") 3 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/533099-udineea-official-thread/reply#reply)
  * Subscribe
  * [100](javascript:void\(0\);)

Attachments: UdineEA Official Thread

Tags: UdineEA Official Thread

#  [](/thread/533099-udineea-official-thread)UdineEA Official Thread 

  * 

  * [#141](/thread/post/8175910#post8175910 "Post Permalink")

  * Mar 31, 2015 9:41pm  Mar 31, 2015 9:41pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar375828_2.gif) JibalaPasan](jibalapasan)

  * Joined Jun 2014 | Status: Trader | [2,498 Posts](/search?do=process&provider=Member&searchuser=375828)

> [Quoting skyline](/thread/post/8175860#post8175860 "View Quoted Post")
> 
> Disliked
> 
> Possible short EU @1.07300 (and EJ possible short maybe on next candle) {image}
> 
> Ignored

If you use confirmation what @nasap has described in Udines 00-level post #28236 then "no false signal"! ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Ashampoo_Snap_2015.03.31_20h33m48s_020_.png
Size: 61 KB](/attachment/image/1644024/thumbnail?d=1427805604)](/attachment/image/1644024?d=1427805604)   

  
Jibala 

PDF & BCC (Patience Discipline Focus & Belief Confidence Consistency)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#142](/thread/post/8175933#post8175933 "Post Permalink")

  * Mar 31, 2015 9:48pm  Mar 31, 2015 9:48pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting Mariodrugs](/thread/post/8175878#post8175878 "View Quoted Post")
> 
> Disliked
> 
> {quote} I have the same now ;- ) {image}
> 
> Ignored

![](https://resources.faireconomy.media/images/emojis/64/1f44f.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#143](/thread/post/8175954#post8175954 "Post Permalink")

  * Mar 31, 2015 9:55pm  Mar 31, 2015 9:55pm 

  * [ brucech](brucech)

  * | Joined Sep 2006  | Status: Trader | [594 Posts](/search?do=process&provider=Member&searchuser=18716)

Skyline,  
  
Just back from traveling past few weeks. Thank you for your willingness to share this EA. You have done a great job in outlining not only the use of the EA, but also how we can participate in it's development on demo until such time as most of the bugs are solved. It is greatly appreciated by all for the time that you have put in to creating and developing this EA and the thread to control it development and use.  
  
Many thanks.  
  
Bruce  
  
  

> [Quoting skyline](/thread/post/8171907#post8171907 "View Quoted Post")
> 
> Disliked
> 
> {quote} Yes it works but it's useless due to the news filter which cannot be used in backtest.
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#144](/thread/post/8175994#post8175994 "Post Permalink")

  * Mar 31, 2015 10:11pm  Mar 31, 2015 10:11pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting brucech](/thread/post/8175954#post8175954 "View Quoted Post")
> 
> Disliked
> 
> Skyline, Just back from traveling past few weeks. Thank you for your willingness to share this EA. You have done a great job in outlining not only the use of the EA, but also how we can participate in it's development on demo until such time as most of the bugs are solved. It is greatly appreciated by all for the time that you have put in to creating and developing this EA and the thread to control it development and use. Many thanks. Bruce {quote}
> 
> Ignored

You're welcome Brucech ! ![](https://resources.faireconomy.media/images/emojis/64/1f917.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#145](/thread/post/8176008#post8176008 "Post Permalink")

  * Mar 31, 2015 10:16pm  Mar 31, 2015 10:16pm 

  * [ Mariodrugs](mariodrugs)

  * | Membership Revoked  | Joined Dec 2014 | [379 Posts](/search?do=process&provider=Member&searchuser=394832)

Is this system watch out for support / ressistances ? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#146](/thread/post/8176148#post8176148 "Post Permalink")

  * Mar 31, 2015 11:22pm  Mar 31, 2015 11:22pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar393445_1.gif) Vlad13685](vlad13685)

  * Joined Dec 2014 | Status: Professional Demo Trader | [536 Posts](/search?do=process&provider=Member&searchuser=393445)

Hi Skyline, thanks for the thread!  
  
I had another EU short come up, however it was during USD Red news, and trade still triggered.  
  
Do you have the same your side?  
  
Vlad 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Capture.PNG
Size: 63 KB](/attachment/image/1644106/thumbnail?d=1427811769)](/attachment/image/1644106?d=1427811769)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#147](/thread/post/8176182#post8176182 "Post Permalink")

  * Mar 31, 2015 11:34pm  Mar 31, 2015 11:34pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting Vlad13685](/thread/post/8176148#post8176148 "View Quoted Post")
> 
> Disliked
> 
> Hi Skyline, thanks for the thread! I had another EU short come up, however it was during USD Red news, and trade still triggered. Do you have the same your side? Vlad {image}
> 
> Ignored

Hi Vlad,  
thank you for testing this EA ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)  
No sorry I don't have that pending order placed, maybe some error from Wukar_News ? ![](https://resources.faireconomy.media/images/emojis/64/1f615.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/2753.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#148](/thread/post/8176194#post8176194 "Post Permalink")

  * Mar 31, 2015 11:39pm  Mar 31, 2015 11:39pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar393445_1.gif) Vlad13685](vlad13685)

  * Joined Dec 2014 | Status: Professional Demo Trader | [536 Posts](/search?do=process&provider=Member&searchuser=393445)

> [Quoting skyline](/thread/post/8176182#post8176182 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi Vlad, thank you for testing this EA ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1) No sorry I don't have that pending order placed, maybe some error from Wukar_News ? ![](https://resources.faireconomy.media/images/emojis/64/1f615.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/2753.png?v=15.1)
> 
> Ignored

Hey Skyline,  
  
Well WUKAR and FCAL on my chart did indicate that there was news at the correct time (see screen shot) but for some reason the EA still placed the pending order?  
  
The WUKAR indicator and your "News = OK TO TRADE" indicator on the left don't seem to be in Sync on my side.  
  
Not sure why...  
  
Vlad 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Capture.PNG
Size: 72 KB](/attachment/image/1644123/thumbnail?d=1427813038)](/attachment/image/1644123?d=1427813038)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#149](/thread/post/8176369#post8176369 "Post Permalink")

  * Apr 1, 2015 12:37am  Apr 1, 2015 12:37am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar375828_2.gif) JibalaPasan](jibalapasan)

  * Joined Jun 2014 | Status: Trader | [2,498 Posts](/search?do=process&provider=Member&searchuser=375828)

> [Quoting Vlad13685](/thread/post/8176194#post8176194 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hey Skyline, Well WUKAR and FCAL on my chart did indicate that there was news at the correct time (see screen shot) but for some reason the EA still placed the pending order? The WUKAR indicator and your "News = OK TO TRADE" indicator on the left don't seem to be in Sync on my side. Not sure why... Vlad {image}
> 
> Ignored

Have a look in Experts tab if there are any error messages.  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Ashampoo_Snap_2015.03.31_23h35m33s_024_.png
Size: 42 KB](/attachment/image/1644173/thumbnail?d=1427816212)](/attachment/image/1644173?d=1427816212)   

  
Jibala 

PDF & BCC (Patience Discipline Focus & Belief Confidence Consistency)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#150](/thread/post/8176492#post8176492 "Post Permalink")

  * Apr 1, 2015 1:42am  Apr 1, 2015 1:42am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar393445_1.gif) Vlad13685](vlad13685)

  * Joined Dec 2014 | Status: Professional Demo Trader | [536 Posts](/search?do=process&provider=Member&searchuser=393445)

> [Quoting JibalaPasan](/thread/post/8176369#post8176369 "View Quoted Post")
> 
> Disliked
> 
> {quote} Have a look in Experts tab if there are any error messages. {image} Jibala
> 
> Ignored

Hi I think you are correct! It could have been that DLL imports were disabled earlier.  
  
Will see if this fixes it tomorrow.  
  
Thanks!  
  
Vlad 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#151](/thread/post/8176565#post8176565 "Post Permalink")

  * Apr 1, 2015 2:29am  Apr 1, 2015 2:29am 

  * [ rmndschmidt](rmndschmidt)

  * | Joined Mar 2014  | Status: Trader | [42 Posts](/search?do=process&provider=Member&searchuser=365689)

> [Quoting skyline](/thread/post/8172071#post8172071 "View Quoted Post")
> 
> Disliked
> 
> {quote} Please download again UdineEA_package_v2.rar from first post
> 
> Ignored

Hello and thank you! In this moment I installed the newest Version (all indicators,template and EA) and it looks like the picture shows. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Unbenannt2.png
Size: 586 KB](/attachment/image/1644239/thumbnail?d=1427822953)](/attachment/image/1644239?d=1427822953)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#152](/thread/post/8176685#post8176685 "Post Permalink")

  * Apr 1, 2015 3:30am  Apr 1, 2015 3:30am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting rmndschmidt](/thread/post/8176565#post8176565 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hello and thank you! In this moment I installed the newest Version (all indicators,template and EA) and it looks like the picture shows. {image}
> 
> Ignored

Hi rmndschimdt,  
what do you think is related that message ? ![](https://resources.faireconomy.media/images/emojis/64/263a-fe0f.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f4ad.png?v=15.1)  
Do you have at least read that message? ![](https://resources.faireconomy.media/images/emojis/64/1f612.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/231b.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#153](/thread/post/8176710#post8176710 "Post Permalink")

  * Apr 1, 2015 3:41am  Apr 1, 2015 3:41am 

  * [ rmndschmidt](rmndschmidt)

  * | Joined Mar 2014  | Status: Trader | [42 Posts](/search?do=process&provider=Member&searchuser=365689)

> [Quoting skyline](/thread/post/8176685#post8176685 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi rmndschimdt, what do you think is related that message ? ![](https://resources.faireconomy.media/images/emojis/64/263a-fe0f.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f4ad.png?v=15.1) Do you have at least read that message? ![](https://resources.faireconomy.media/images/emojis/64/1f612.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/231b.png?v=15.1)
> 
> Ignored

Hi skyline, I read it and I downloades and installes the newest version. 5 minutes before I found the cause. The EA has problems sometimes to recognize an account as a demo account. I have opened a new demo account and now it works.![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#154](/thread/post/8176825#post8176825 "Post Permalink")

  * Apr 1, 2015 4:53am  Apr 1, 2015 4:53am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting rmndschmidt](/thread/post/8176710#post8176710 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi skyline, I read it and I downloades and installes the newest version. 5 minutes before I found the cause. The EA has problems sometimes to recognize an account as a demo account. I have opened a new demo account and now it works.![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)
> 
> Ignored

![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#155](/thread/post/8177053#post8177053 "Post Permalink")

  * Apr 1, 2015 8:04am  Apr 1, 2015 8:04am 

  * [ mebarrac](mebarrac)

  * | Joined Feb 2015  | Status: Trader | [38 Posts](/search?do=process&provider=Member&searchuser=402218)

> [Quoting Vlad13685](/thread/post/8176194#post8176194 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hey Skyline, Well WUKAR and FCAL on my chart did indicate that there was news at the correct time (see screen shot) but for some reason the EA still placed the pending order? The WUKAR indicator and your "News = OK TO TRADE" indicator on the left don't seem to be in Sync on my side. Not sure why... Vlad {image}
> 
> Ignored

I seem to have the same problem as you Vlad..news must be out of synch or something  
  
<http://i.imgur.com/wPy3vVo.jpg>

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#156](/thread/post/8177065#post8177065 "Post Permalink")

  * Apr 1, 2015 8:15am  Apr 1, 2015 8:15am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar185229_8.gif) Erebus](erebus)

  * Joined Jul 2011 | Status: Trader | [8,576 Posts](/search?do=process&provider=Member&searchuser=185229)

Hey everybody,  
  
I've been following along for a few days now, even though I think a PT of 5 pips is...???  
  
So, big congratulation to skyline for developing the EA  
  
I have the same trade as mentioned in last few posts  
  
I notice on my chart that the News indicator seem to be missing bars  
  
I thought it was normal until I saw other charts  
  
Any ideas or suggestions?  
  
I have tried to refresh the chart, re-apply template, change time frames back & forth but still the same?  
  
Thanks, John 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: 1-04-2015 9-09-02 AM.png
Size: 365 KB](/attachment/image/1644384/thumbnail?d=1427843709)](/attachment/image/1644384?d=1427843709)   

"Forex a Great Hobby, But Not a Great Job"

[Texas-2-Step](erebus#79 "View Trade Explorer") All Time Return: 8.8%

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#157](/thread/post/8177086#post8177086 "Post Permalink")

  * Apr 1, 2015 8:46am  Apr 1, 2015 8:46am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar389954_3.gif) honestknave](honestknave)

  * Joined Nov 2014 | Status: Trader | [1,300 Posts](/search?do=process&provider=Member&searchuser=389954)

> [Quoting rmndschmidt](/thread/post/8176710#post8176710 "View Quoted Post")
> 
> Disliked
> 
> The EA has problems sometimes to recognize an account as a demo account. I have opened a new demo account and now it works.![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)
> 
> Ignored

Out of interest, did you change brokers? I know there are a few brokers' servers that are setup incorrectly i.e. they flag demo for live, and live for demo.  
  
I guess there is a market niche for brokers catering to people who want to use demo-only stuff on a live account ![](https://resources.faireconomy.media/images/emojis/64/1f923.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#158](/thread/post/8177098#post8177098 "Post Permalink")

  * Apr 1, 2015 9:04am  Apr 1, 2015 9:04am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar378281_1.gif) ChrisGC](chrisgc)

  * | Joined Jul 2014  | Status: Trader | [192 Posts](/search?do=process&provider=Member&searchuser=378281)

> [Quoting Erebus](/thread/post/8177065#post8177065 "View Quoted Post")
> 
> Disliked
> 
> Hey everybody, I've been following along for a few days now, even though I think a PT of 5 pips is...??? So, big congratulation to skyline for developing the EA I have the same trade as mentioned in last few posts I notice on my chart that the News indicator seem to be missing bars I thought it was normal until I saw other charts Any ideas or suggestions? I have tried to refresh the chart, re-apply template, change time frames back & forth but still the same? Thanks, John {image}
> 
> Ignored

It is normal. Everytime you close / open it gets rid of some old data. 

The problem is not giving offence but taking offence!

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#159](/thread/post/8177429#post8177429 "Post Permalink")

  * Apr 1, 2015 3:13pm  Apr 1, 2015 3:13pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar393445_1.gif) Vlad13685](vlad13685)

  * Joined Dec 2014 | Status: Professional Demo Trader | [536 Posts](/search?do=process&provider=Member&searchuser=393445)

Hi everyone,  
  
For those struggling with DLL errors, just remember you need to "Allow DLL Imports" both in the MT4 Settings, AND the properties of the EA itself.  
  
Vlad 

Attached Images

![](/attachment/image/1644513?d=1427868767) ![](/attachment/image/1644514?d=1427868772)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#160](/thread/post/8177557#post8177557 "Post Permalink")

  * Apr 1, 2015 4:34pm  Apr 1, 2015 4:34pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar185229_8.gif) Erebus](erebus)

  * Joined Jul 2011 | Status: Trader | [8,576 Posts](/search?do=process&provider=Member&searchuser=185229)

There is pending for EUR-JPY   
  
Calendar is different, is that a problem or feature?  
  
Thanks for support, John  
  
![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

Attached Image (click to enlarge)

[![Click to Enlarge

Name: 1-04-2015 5-32-31 PM.png
Size: 185 KB](/attachment/image/1644561/thumbnail?d=1427873672)](/attachment/image/1644561?d=1427873672)   

"Forex a Great Hobby, But Not a Great Job"

[Texas-2-Step](erebus#79 "View Trade Explorer") All Time Return: 8.8%

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * UdineEA Official Thread
  *   * [ **Reply to Thread** ](/thread/533099-udineea-official-thread/reply#reply)

  * More

[](https://www.forexfactory.com "Homepage")

  * [Forums](forums)
  * [Trades](trades)
  * [Calendar](calendar)
  * [News](news)
  * [Market](market)
  * [Brokers](brokers)

****

[](https://www.faireconomy.com/)

  * 

[The Official "Ok, now I'm pissed" Thread](/thread/73546-the-official-ok-now-im-pissed-thread "Hello Everyone, 
 
Seeing the apparent lack of threads of this nature \(just kidding, but read on\) I have decided to set up a respectable...") 51 replies

[Historic Charts: NZ Official Cash Rate](/thread/20380-historic-charts-nz-official-cash-rate "Sep 14, 2005") 15 replies

[Is there an official exchange rate?!](/thread/11571-is-there-an-official-exchange-rate "Different brokers have different bid and ask prices for every cross or pair.  However, the bid and ask price is based on something...I am...") 14 replies

[Official forex time zone](/thread/9940-official-forex-time-zone "is there a standard forex time zone? do i follow gmt or NY time? i use 4 hour charts and sometimes the time is way off because of time zone...") 3 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/533099-udineea-official-thread/reply#reply)
  * Subscribe
  * [100](javascript:void\(0\);)

Attachments: UdineEA Official Thread

Tags: UdineEA Official Thread

#  [](/thread/533099-udineea-official-thread)UdineEA Official Thread 

  * 

  * [#161](/thread/post/8177565#post8177565 "Post Permalink")

  * Apr 1, 2015 4:38pm  Apr 1, 2015 4:38pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

Morning All ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
UdineEA opened wrongly an order on GJ when there's red bar on WUKAR_News  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot2.png
Size: 12 KB](/attachment/image/1644564/thumbnail?d=1427873854)](/attachment/image/1644564?d=1427873854)   

  
  
I'm looking into this bug and will fix in next release on weekend.  
  
Cheers,  
Skyline 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#162](/thread/post/8177579#post8177579 "Post Permalink")

  * Apr 1, 2015 4:44pm  Apr 1, 2015 4:44pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar393445_1.gif) Vlad13685](vlad13685)

  * Joined Dec 2014 | Status: Professional Demo Trader | [536 Posts](/search?do=process&provider=Member&searchuser=393445)

> [Quoting skyline](/thread/post/8177565#post8177565 "View Quoted Post")
> 
> Disliked
> 
> Morning All ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) UdineEA opened wrongly an order on GJ when there's red bar on WUKAR_News {image} I'm looking into this bug and will fix in next release on weekend. Cheers, Skyline
> 
> Ignored

Cool ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) Thought it was just me  
  
Vlad 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#163](/thread/post/8177586#post8177586 "Post Permalink")

  * Apr 1, 2015 4:46pm  Apr 1, 2015 4:46pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting Erebus](/thread/post/8177557#post8177557 "View Quoted Post")
> 
> Disliked
> 
> There is pending for EUR-JPY Calendar is different, is that a problem or feature? Thanks for support, John ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) {image}
> 
> Ignored

Hi Erebus,  
yes I have too a pending short EJ @ 128.800.  
It's ok that WUKAR_News is different among pairs, this is because it shows impact news (ones in red in FF calendar) related to each currency , so for EURUSD it shows EUR news and USD news, while for GBPJPY shows GBP and JPY news which are different.  
  
Edit : EJ Closed by TS (0 pips). 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#164](/thread/post/8177612#post8177612 "Post Permalink")

  * Apr 1, 2015 4:56pm  Apr 1, 2015 4:56pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar375828_2.gif) JibalaPasan](jibalapasan)

  * Joined Jun 2014 | Status: Trader | [2,498 Posts](/search?do=process&provider=Member&searchuser=375828)

Should not have entered that trade. Pairs are not sync!  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Ashampoo_Snap_2015.04.01_15h52m07s_025_.png
Size: 111 KB](/attachment/image/1644578/thumbnail?d=1427874959)](/attachment/image/1644578?d=1427874959)   

  
Jibala 

PDF & BCC (Patience Discipline Focus & Belief Confidence Consistency)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#165](/thread/post/8177641#post8177641 "Post Permalink")

  * Apr 1, 2015 5:08pm  Apr 1, 2015 5:08pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting JibalaPasan](/thread/post/8177612#post8177612 "View Quoted Post")
> 
> Disliked
> 
> Should not have entered that trade. Pairs are not sync! {image} Jibala
> 
> Ignored

Hi Jibala,  
there would be 1000 reasons to not take that trade but here we are following/testing strictly (simple) rules coded in EA and pair sync analysis isn't coded there ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)  
  
Cheers,  
Skyline 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#166](/thread/post/8177649#post8177649 "Post Permalink")

  * Apr 1, 2015 5:13pm  Apr 1, 2015 5:13pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar185229_8.gif) Erebus](erebus)

  * Joined Jul 2011 | Status: Trader | [8,576 Posts](/search?do=process&provider=Member&searchuser=185229)

> [Quoting JibalaPasan](/thread/post/8177612#post8177612 "View Quoted Post")
> 
> Disliked
> 
> Should not have entered that trade. Pairs are not sync! {image} Jibala
> 
> Ignored

Can you please explain what we are looking for on those chart?  
  
I see the same red bars in the circled area, how do I read it is not in sync?  
  
Thanks, John 

"Forex a Great Hobby, But Not a Great Job"

[Texas-2-Step](erebus#79 "View Trade Explorer") All Time Return: 8.8%

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#167](/thread/post/8177688#post8177688 "Post Permalink")

  * Apr 1, 2015 5:32pm  Apr 1, 2015 5:32pm 

  * [ Bhutugly](bhutugly)

  * | Joined Oct 2011  | Status: Trader | [12 Posts](/search?do=process&provider=Member&searchuser=200586)

Skyline,  
  
Everything working fine here now.  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot3.png
Size: 23 KB](/attachment/image/1644612/thumbnail?d=1427876851)](/attachment/image/1644612?d=1427876851)   

  
  
It triggered fine.  
  
I would not normally take this trade as it was so close to DO Line stopped me out at S/L - 10. But everything working brilliant.  
  
I'm using [IC Markets](/brokers/ic-markets "View IC Markets Broker Profile")  
  
Thanks  
  
Ian 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#168](/thread/post/8177695#post8177695 "Post Permalink")

  * Apr 1, 2015 5:33pm  Apr 1, 2015 5:33pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar375828_2.gif) JibalaPasan](jibalapasan)

  * Joined Jun 2014 | Status: Trader | [2,498 Posts](/search?do=process&provider=Member&searchuser=375828)

> [Quoting Erebus](/thread/post/8177649#post8177649 "View Quoted Post")
> 
> Disliked
> 
> {quote} Can you please explain what we are looking for on those chart? I see the same red bars in the circled area, how do I read it is not in sync? Thanks, John
> 
> Ignored

If you have a closer look you'll see that the candles I added have a green candle (layer) between! I have chosen it that way so that I see it from the far even.  
  
Jibala 

PDF & BCC (Patience Discipline Focus & Belief Confidence Consistency)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#169](/thread/post/8177706#post8177706 "Post Permalink")

  * Apr 1, 2015 5:37pm  Apr 1, 2015 5:37pm 

  * [ Bhutugly](bhutugly)

  * | Joined Oct 2011  | Status: Trader | [12 Posts](/search?do=process&provider=Member&searchuser=200586)

Okay,  
  
Why didn't the following trigger?  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot1.png
Size: 13 KB](/attachment/image/1644620/thumbnail?d=1427877433)](/attachment/image/1644620?d=1427877433)   

  
  
Cheers  
  
Ian 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#170](/thread/post/8177839#post8177839 "Post Permalink")

  * Apr 1, 2015 6:19pm  Apr 1, 2015 6:19pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar375828_2.gif) JibalaPasan](jibalapasan)

  * Joined Jun 2014 | Status: Trader | [2,498 Posts](/search?do=process&provider=Member&searchuser=375828)

> [Quoting skyline](/thread/post/8177641#post8177641 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi Jibala, there would be 1000 reasons to not take that trade but here we are following/testing strictly (simple) rules coded in EA and pair sync analysis isn't coded there ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1) Cheers, Skyline
> 
> Ignored

Of course, there is always a reason "not" to take a trade. I only suggest it to prevent from false signals.  
  
@Erebus: I just took this 2 manual on GU & GJ (only to illustrate the meaning of "pairs have to be sync")  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Ashampoo_Snap_2015.04.01_17h12m01s_027_.png
Size: 51 KB](/attachment/image/1644665/thumbnail?d=1427879828)](/attachment/image/1644665?d=1427879828)   

  
Jibala 

PDF & BCC (Patience Discipline Focus & Belief Confidence Consistency)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#171](/thread/post/8178001#post8178001 "Post Permalink")

  * Apr 1, 2015 7:08pm  Apr 1, 2015 7:08pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar309469_3.gif) gigicualex](gigicualex)

  * | Joined Nov 2012  | Status: Trader | [1,187 Posts](/search?do=process&provider=Member&searchuser=309469)

> [Quoting Bhutugly](/thread/post/8177706#post8177706 "View Quoted Post")
> 
> Disliked
> 
> Okay, Why didn't the following trigger? {image} Cheers Ian
> 
> Ignored

Yea i was wondering the same thing 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#172](/thread/post/8178015#post8178015 "Post Permalink")

  * Apr 1, 2015 7:16pm  Apr 1, 2015 7:16pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar375828_2.gif) JibalaPasan](jibalapasan)

  * Joined Jun 2014 | Status: Trader | [2,498 Posts](/search?do=process&provider=Member&searchuser=375828)

> [Quoting Bhutugly](/thread/post/8177706#post8177706 "View Quoted Post")
> 
> Disliked
> 
> Okay, Why didn't the following trigger? {image} Cheers Ian
> 
> Ignored

Imho too close to the blue DO line.  
  
Jibala 

PDF & BCC (Patience Discipline Focus & Belief Confidence Consistency)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#173](/thread/post/8178027#post8178027 "Post Permalink")

  * Apr 1, 2015 7:20pm  Apr 1, 2015 7:20pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar185229_8.gif) Erebus](erebus)

  * Joined Jul 2011 | Status: Trader | [8,576 Posts](/search?do=process&provider=Member&searchuser=185229)

> [Quoting JibalaPasan](/thread/post/8177695#post8177695 "View Quoted Post")
> 
> Disliked
> 
> {quote} If you have a closer look you'll see that the candles I added have a green candle (layer) between! I have chosen it that way so that I see it from the far even. Jibala
> 
> Ignored

I have looked close, do you mean that this pair is not breaking the 4 Hour low as shown, unlike the EUR-USD ?  
  
Do you trade the 4 Hour candles or just to watch them instead of the 1 Hour candles direction in the original trade specs?  
  
Thanks, John 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: 1-04-2015 8-13-48 PM.png
Size: 905 KB](/attachment/image/1644714/thumbnail?d=1427883517)](/attachment/image/1644714?d=1427883517)   

"Forex a Great Hobby, But Not a Great Job"

[Texas-2-Step](erebus#79 "View Trade Explorer") All Time Return: 8.8%

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#174](/thread/post/8178169#post8178169 "Post Permalink")

  * Apr 1, 2015 8:21pm  Apr 1, 2015 8:21pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar375828_2.gif) JibalaPasan](jibalapasan)

  * Joined Jun 2014 | Status: Trader | [2,498 Posts](/search?do=process&provider=Member&searchuser=375828)

> [Quoting Erebus](/thread/post/8178027#post8178027 "View Quoted Post")
> 
> Disliked
> 
> {quote} I have looked close, do you mean that this pair is not breaking the 4 Hour low as shown, unlike the EUR-USD ? Do you trade the 4 Hour candles or just to watch them instead of the 1 Hour candles direction in the original trade specs? Thanks, John {image}
> 
> Ignored

You didn't! With a closer look you should have seen that there are 3 candles (overlapped) in each of the lower windows. I hope you will see it now and also EURUSD has green candles inside. Therefore it was a "false signal". For further information read post #28236 of @nasap in 00-level thread of Udine.  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Ashampoo_Snap_2015.04.01_19h07m55s_028_.png
Size: 32 KB](/attachment/image/1644756/thumbnail?d=1427887005)](/attachment/image/1644756?d=1427887005)   

  
Jibala 

PDF & BCC (Patience Discipline Focus & Belief Confidence Consistency)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#175](/thread/post/8178215#post8178215 "Post Permalink")

  * Apr 1, 2015 8:43pm  Apr 1, 2015 8:43pm 

  * [ mebarrac](mebarrac)

  * | Joined Feb 2015  | Status: Trader | [38 Posts](/search?do=process&provider=Member&searchuser=402218)

looks like I just got another entry on red news on EU @ 1.07600 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#176](/thread/post/8178231#post8178231 "Post Permalink")

  * Apr 1, 2015 8:52pm  Apr 1, 2015 8:52pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar393445_1.gif) Vlad13685](vlad13685)

  * Joined Dec 2014 | Status: Professional Demo Trader | [536 Posts](/search?do=process&provider=Member&searchuser=393445)

> [Quoting mebarrac](/thread/post/8178215#post8178215 "View Quoted Post")
> 
> Disliked
> 
> looks like I just got another entry on red news on EU @ 1.07600
> 
> Ignored

This was a valid entry mebarrac (apart from the Daily Pivot in the way).  
  
Rule is no entries 1 hour before news, and 30 mins after. This order went through 1:30 before USD news. the WUKAR indicators first red bar is actually just a warning that the next bar is a no-go.  
  
Vlad 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#177](/thread/post/8178240#post8178240 "Post Permalink")

  * Edited 9:06pm  Apr 1, 2015 8:54pm | Edited 9:06pm 

  * [ mebarrac](mebarrac)

  * | Joined Feb 2015  | Status: Trader | [38 Posts](/search?do=process&provider=Member&searchuser=402218)

> [Quoting JibalaPasan](/thread/post/8178169#post8178169 "View Quoted Post")
> 
> Disliked
> 
> {quote} You didn't! With a closer look you should have seen that there are 3 candles (overlapped) in each of the lower windows. I hope you will see it now and also EURUSD has green candles inside. Therefore it was a "false signal". For further information read post #28236 of @nasap in 00-level thread of Udine. {image} Jibala
> 
> Ignored

no offense - can we keep this to the other thread, this thread should just be on level 1 entries and the ea that skyline has kindly developed for Udines system. I'm sure he will add other filters later like pivots and distance from daily open like udine suggests etc..but we need to have the base system working flawlessly on the ea before we proceed with anything else.  
  
edit btw I'm in no way discounting your methods , it looks like a very interesting filter you are using on top of Udines method  
  
Thanks Tom 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#178](/thread/post/8178251#post8178251 "Post Permalink")

  * Apr 1, 2015 8:58pm  Apr 1, 2015 8:58pm 

  * [ mebarrac](mebarrac)

  * | Joined Feb 2015  | Status: Trader | [38 Posts](/search?do=process&provider=Member&searchuser=402218)

> [Quoting Vlad13685](/thread/post/8178231#post8178231 "View Quoted Post")
> 
> Disliked
> 
> {quote} This was a valid entry mebarrac (apart from the Daily Pivot in the way). Rule is no entries 1 hour before news, and 30 mins after. This order went through 1:30 before USD news. the WUKAR indicators first red bar is actually just a warning that the next bar is a no-go. Vlad
> 
> Ignored

Great thank you for explaining that Vlad! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#179](/thread/post/8178270#post8178270 "Post Permalink")

  * Apr 1, 2015 9:04pm  Apr 1, 2015 9:04pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar402612_1.gif) mokuro89](mokuro89)

  * Joined Mar 2015 | Status: Trader | [449 Posts](/search?do=process&provider=Member&searchuser=402612)

> [Quoting JibalaPasan](/thread/post/8178169#post8178169 "View Quoted Post")
> 
> Disliked
> 
> {quote} You didn't! With a closer look you should have seen that there are 3 candles (overlapped) in each of the lower windows. I hope you will see it now and also EURUSD has green candles inside. Therefore it was a "false signal". For further information read post #28236 of @nasap in 00-level thread of Udine. {image} Jibala
> 
> Ignored

Hi JibalaPasan, i got 60 / 1440 layers on price to open only, may I ask you what is your 3 layers? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#180](/thread/post/8178388#post8178388 "Post Permalink")

  * Apr 1, 2015 9:40pm  Apr 1, 2015 9:40pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar53444_2.gif) dagoods](dagoods)

  * Joined Nov 2007 | Status: Trader | [3,059 Posts](/search?do=process&provider=Member&searchuser=53444)

Big Thanks skyline for sharing. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * UdineEA Official Thread
  *   * [ **Reply to Thread** ](/thread/533099-udineea-official-thread/reply#reply)

  * More

[](https://www.forexfactory.com "Homepage")

  * [Forums](forums)
  * [Trades](trades)
  * [Calendar](calendar)
  * [News](news)
  * [Market](market)
  * [Brokers](brokers)

****

[](https://www.faireconomy.com/)

  * 

[The Official "Ok, now I'm pissed" Thread](/thread/73546-the-official-ok-now-im-pissed-thread "Hello Everyone, 
 
Seeing the apparent lack of threads of this nature \(just kidding, but read on\) I have decided to set up a respectable...") 51 replies

[Historic Charts: NZ Official Cash Rate](/thread/20380-historic-charts-nz-official-cash-rate "Sep 14, 2005") 15 replies

[Is there an official exchange rate?!](/thread/11571-is-there-an-official-exchange-rate "Different brokers have different bid and ask prices for every cross or pair.  However, the bid and ask price is based on something...I am...") 14 replies

[Official forex time zone](/thread/9940-official-forex-time-zone "is there a standard forex time zone? do i follow gmt or NY time? i use 4 hour charts and sometimes the time is way off because of time zone...") 3 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/533099-udineea-official-thread/reply#reply)
  * Subscribe
  * [100](javascript:void\(0\);)

Attachments: UdineEA Official Thread

Tags: UdineEA Official Thread

#  [](/thread/533099-udineea-official-thread)UdineEA Official Thread 

  * 

  * [#181](/thread/post/8178617#post8178617 "Post Permalink")

  * Apr 1, 2015 10:52pm  Apr 1, 2015 10:52pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting mebarrac](/thread/post/8178240#post8178240 "View Quoted Post")
> 
> Disliked
> 
> {quote} no offense - can we keep this to the other thread, this thread should just be on level 1 entries and the ea that skyline has kindly developed for Udines system. I'm sure he will add other filters later like pivots and distance from daily open like udine suggests etc..but we need to have the base system working flawlessly on the ea before we proceed with anything else. edit btw I'm in no way discounting your methods , it looks like a very interesting filter you are using on top of Udines method Thanks Tom
> 
> Ignored

Exactly as explained by mebarrac, at this stage my goal is to improve stability and remove bugs , then go to live trading , actually i'm not planning to add further filters otherwise it would be a never ending loop and i don't have such time available. Another reason is that all changes cannot be backtested so there's no way to evaluate beforehand if there's some benefit adding them.  
Cheers,  
  
Skyline 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#182](/thread/post/8178901#post8178901 "Post Permalink")

  * Apr 2, 2015 12:15am  Apr 2, 2015 12:15am 

  * [ Mariodrugs](mariodrugs)

  * | Membership Revoked  | Joined Dec 2014 | [379 Posts](/search?do=process&provider=Member&searchuser=394832)

_I have to officialy says that:**Udine EA doesn't works.** DONT USE IT ON REAL ACCOUNTS, IT MAKES LOOSES.  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: EURUSD Udine EA dont works.png
Size: 242 KB](/attachment/image/1644957/thumbnail?d=1427901309)](/attachment/image/1644957?d=1427901309)   

_

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#183](/thread/post/8178907#post8178907 "Post Permalink")

  * Apr 2, 2015 12:17am  Apr 2, 2015 12:17am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar338950_1.gif) cescof](cescof)

  * Joined Jun 2013 | Status: Trader | [1,006 Posts](/search?do=process&provider=Member&searchuser=338950)

> [Quoting skyline](/thread/post/8177565#post8177565 "View Quoted Post")
> 
> Disliked
> 
> Morning All ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) UdineEA opened wrongly an order on GJ when there's red bar on WUKAR_News {image} I'm looking into this bug and will fix in next release on weekend. Cheers, Skyline
> 
> Ignored

Not in my platform..... todsay just 3 order for eur/jpy 1be 1 tp and 1 sl  
Regards 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#184](/thread/post/8178922#post8178922 "Post Permalink")

  * Apr 2, 2015 12:21am  Apr 2, 2015 12:21am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar338950_1.gif) cescof](cescof)

  * Joined Jun 2013 | Status: Trader | [1,006 Posts](/search?do=process&provider=Member&searchuser=338950)

> [Quoting Mariodrugs](/thread/post/8178901#post8178901 "View Quoted Post")
> 
> Disliked
> 
> I have to officialy says that: Udine EA doesn't works. DONT USE IT ON REAL ACCOUNTS, IT MAKES LOOSES. {image}
> 
> Ignored

If you read fist post you know that's impossibile use it in real at this stage.... Many of us are really gratetful to Skyline for this really good work considering that 's totally free....So i 'think and is my own opinion your post is not very appropriate here...  
Kind regards 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#185](/thread/post/8178924#post8178924 "Post Permalink")

  * Apr 2, 2015 12:23am  Apr 2, 2015 12:23am 

  * [ Mariodrugs](mariodrugs)

  * | Membership Revoked  | Joined Dec 2014 | [379 Posts](/search?do=process&provider=Member&searchuser=394832)

> [Quoting cescof](/thread/post/8178922#post8178922 "View Quoted Post")
> 
> Disliked
> 
> {quote} If you read fist post you know that's impossibile use it in real at this stage.... Many of us are really gratetful to Skyline for this really good work considering that 's totally free....So i 'think and is my own opinion your post is not very appropriate here... Kind regards
> 
> Ignored

Yes, its demo but this strategy doesnt works so far.. I have my PC turned on 24 / h. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#186](/thread/post/8178937#post8178937 "Post Permalink")

  * Apr 2, 2015 12:28am  Apr 2, 2015 12:28am 

  * [ Godwin Igili](godwin*igili)

  * Joined May 2011 | Status: Trader | [541 Posts](/search?do=process&provider=Member&searchuser=179642)

> [Quoting Mariodrugs](/thread/post/8178901#post8178901 "View Quoted Post")
> 
> Disliked
> 
> I have to officialy says that: Udine EA doesn't works. DONT USE IT ON REAL ACCOUNTS, IT MAKES LOOSES. {image}
> 
> Ignored

  
Mariodrugs,  
  
How long have you used it?  
  
Did you read post 1? It can not be used on live/real accounts  
  
Skyline wants it to be tested to stabilise it and remove bugs for the whole of April  
  
Why not have some patience and report bugs  
  
**PLEASE STOP FLAMING THE THREAD**

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#187](/thread/post/8178957#post8178957 "Post Permalink")

  * Apr 2, 2015 12:35am  Apr 2, 2015 12:35am 

  * [ rmndschmidt](rmndschmidt)

  * | Joined Mar 2014  | Status: Trader | [42 Posts](/search?do=process&provider=Member&searchuser=365689)

> [Quoting honestknave](/thread/post/8177086#post8177086 "View Quoted Post")
> 
> Disliked
> 
> {quote} Out of interest, did you change brokers? I know there are a few brokers' servers that are setup incorrectly i.e. they flag demo for live, and live for demo. I guess there is a market niche for brokers catering to people who want to use demo-only stuff on a live account ![](https://resources.faireconomy.media/images/emojis/64/1f923.png?v=15.1)
> 
> Ignored

Hi, no I did´nt. My broker is Global Prime. I opened the 2. Demo and the EA works without problems. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#188](/thread/post/8178962#post8178962 "Post Permalink")

  * Apr 2, 2015 12:37am  Apr 2, 2015 12:37am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar389954_3.gif) honestknave](honestknave)

  * Joined Nov 2014 | Status: Trader | [1,300 Posts](/search?do=process&provider=Member&searchuser=389954)

> [Quoting rmndschmidt](/thread/post/8178957#post8178957 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi, no I didnt. My broker is Global Prime. I opened the 2. Demo and the EA works without problems.
> 
> Ignored

Thanks for the reply ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#189](/thread/post/8178992#post8178992 "Post Permalink")

  * Apr 2, 2015 12:50am  Apr 2, 2015 12:50am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting Mariodrugs](/thread/post/8178901#post8178901 "View Quoted Post")
> 
> Disliked
> 
> I have to officialy says that: Udine EA doesn't works. DONT USE IT ON REAL ACCOUNTS, IT MAKES LOOSES. {image}
> 
> Ignored

maybe did you think that this EA placed only winning trades or make you rich overnight ? I guess you have to learn a lot what trading is about... ![](https://resources.faireconomy.media/images/emojis/64/1f612.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/231b.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/263a-fe0f.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f4ad.png?v=15.1)  
  
Btw for me today -15 pips (1 w, 1 be , 2 loss) , and one buy stop on EU opened (not triggered yet) @ 1.07800 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#190](/thread/post/8178999#post8178999 "Post Permalink")

  * Apr 2, 2015 12:53am  Apr 2, 2015 12:53am 

  * [ DerBerliner](derberliner)

  * | Joined Feb 2011  | Status: Trader | [822 Posts](/search?do=process&provider=Member&searchuser=168827)

It seems to me the actual result now, following your trade explorer above, is: 1 w, 1 be, **2** loss ... right ? I have the same numbers for today. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#191](/thread/post/8179152#post8179152 "Post Permalink")

  * Apr 2, 2015 1:49am  Apr 2, 2015 1:49am 

  * [ rmndschmidt](rmndschmidt)

  * | Joined Mar 2014  | Status: Trader | [42 Posts](/search?do=process&provider=Member&searchuser=365689)

Hello to all! My results for today: 3 won, 2 loss; 1 be. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Unbenannt2.png
Size: 570 KB](/attachment/image/1645039/thumbnail?d=1427906976)](/attachment/image/1645039?d=1427906976)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#192](/thread/post/8179203#post8179203 "Post Permalink")

  * Apr 2, 2015 2:14am  Apr 2, 2015 2:14am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting DerBerliner](/thread/post/8178999#post8178999 "View Quoted Post")
> 
> Disliked
> 
> It seems to me the actual result now, following your trade explorer above, is: 1 w, 1 be, 2 loss ... right ? I have the same numbers for today.
> 
> Ignored

you're right DerBerliner, i've modified my previous post, today not a good day, not a problem let's see tomorrow ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)  
  
Cheers,  
Skyline 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#193](/thread/post/8179204#post8179204 "Post Permalink")

  * Apr 2, 2015 2:14am  Apr 2, 2015 2:14am 

  * [ Johanl66](johanl66)

  * | Joined Jan 2011  | Status: Trader | [36 Posts](/search?do=process&provider=Member&searchuser=168624)

I really like to thank you do SkyLine what you are doing Sir  
And thanks for sharing and give people an opportunity to trade the Forex market fully automated with some great guidelines that makes sense..  
  
So far I tested this system started from this week....  
  
On Monday:  
1 Loss  
  
Tuesday  
No trades  
  
Wensday  
3losses and 1 Win  
  
so this week total  
4 and 1 W  
  
Lets make this the worlds #1 System/EA in the world  
  
Lets work together and make this happen 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#194](/thread/post/8179218#post8179218 "Post Permalink")

  * Apr 2, 2015 2:20am  Apr 2, 2015 2:20am 

  * [ DerBerliner](derberliner)

  * | Joined Feb 2011  | Status: Trader | [822 Posts](/search?do=process&provider=Member&searchuser=168827)

@rmndschmidt  
  
Hi bro ! Thats "funny" - I'm with GP too, but absolutly no trades with GBPJPY ocured in my fu...ng demo !  
  
I think you didn't any special intervention ? (Have exactly the same results like skyline got them !)  
  
![](https://resources.faireconomy.media/images/emojis/64/1f61f.png?v=15.1) ![](https://resources.faireconomy.media/images/emojis/64/1f630.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#195](/thread/post/8179337#post8179337 "Post Permalink")

  * Apr 2, 2015 3:13am  Apr 2, 2015 3:13am 

  * [ rmndschmidt](rmndschmidt)

  * | Joined Mar 2014  | Status: Trader | [42 Posts](/search?do=process&provider=Member&searchuser=365689)

> [Quoting DerBerliner](/thread/post/8179218#post8179218 "View Quoted Post")
> 
> Disliked
> 
> @rmndschmidt Hi bro ! Thats "funny" - I'm with GP too, but absolutly no trades with GBPJPY ocured in my fu...ng demo ! I think you didn't any special intervention ? (Have exactly the same results like skyline got them !) ![](https://resources.faireconomy.media/images/emojis/64/1f61f.png?v=15.1) ![](https://resources.faireconomy.media/images/emojis/64/1f630.png?v=15.1)
> 
> Ignored

Hi, no intervention and no changes in the settings. Just installed and turned on.![](https://resources.faireconomy.media/images/emojis/64/1f917.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#196](/thread/post/8179598#post8179598 "Post Permalink")

  * Apr 2, 2015 6:21am  Apr 2, 2015 6:21am 

  * [ Mariodrugs](mariodrugs)

  * | Membership Revoked  | Joined Dec 2014 | [379 Posts](/search?do=process&provider=Member&searchuser=394832)

> [Quoting rmndschmidt](/thread/post/8179152#post8179152 "View Quoted Post")
> 
> Disliked
> 
> Hello to all! My results for today: 3 won, 2 loss; 1 be. {image}
> 
> Ignored

Why i have other trades ? When we use the same EA in this same time?? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#197](/thread/post/8179634#post8179634 "Post Permalink")

  * Apr 2, 2015 6:53am  Apr 2, 2015 6:53am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar402612_1.gif) mokuro89](mokuro89)

  * Joined Mar 2015 | Status: Trader | [449 Posts](/search?do=process&provider=Member&searchuser=402612)

> [Quoting Mariodrugs](/thread/post/8179598#post8179598 "View Quoted Post")
> 
> Disliked
> 
> {quote} Why i have other trades ? When we use the same EA in this same time??
> 
> Ignored

probably different brokers  
do your broker allow you to put a pending order at 0points distance from actual price? mine only allow me to put at 20points distance, so if the EA triggers to open an order in less than this the order is not set 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#198](/thread/post/8179639#post8179639 "Post Permalink")

  * Apr 2, 2015 6:56am  Apr 2, 2015 6:56am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

Guys it's quite normal that we cannot have **_exactly_** the same trades each day, there's difference between broker (daily open line, ash indicators, quotes and so on..), I see there is difference also between the same broker on demo maybe due to different server where platform is connected, so be quite and continue test if you enjoy to do this otherwise you always step out and trade manually Udine's strategy as much as you like and most probably with better result than using my EA which is only an experiment.  
As I wrote in first post , for me this EA is just a test, I don't rely at all on it because any information on past performance cannot be properly analized, maybe there's some potential but we can discover only by forward live test and this means a looot of patience from our side is required ! ![](https://resources.faireconomy.media/images/emojis/64/1f61f.png?v=15.1) ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)  
  
Cheers,  
Skyline 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#199](/thread/post/8179758#post8179758 "Post Permalink")

  * Apr 2, 2015 8:35am  Apr 2, 2015 8:35am 

  * [ mebarrac](mebarrac)

  * | Joined Feb 2015  | Status: Trader | [38 Posts](/search?do=process&provider=Member&searchuser=402218)

Here are my trades for today  
looks like 1 win 1 loss and 3 BE  
  
<http://i.imgur.com/LnykBVc.jpg>

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#200](/thread/post/8180394#post8180394 "Post Permalink")

  * Apr 2, 2015 4:24pm  Apr 2, 2015 4:24pm 

  * [ Mariodrugs](mariodrugs)

  * | Membership Revoked  | Joined Dec 2014 | [379 Posts](/search?do=process&provider=Member&searchuser=394832)

> [Quoting mokuro89](/thread/post/8179634#post8179634 "View Quoted Post")
> 
> Disliked
> 
> {quote} probably different brokers do your broker allow you to put a pending order at 0points distance from actual price? mine only allow me to put at 20points distance, so if the EA triggers to open an order in less than this the order is not set
> 
> Ignored

I have [IC Markets](/brokers/ic-markets "View IC Markets Broker Profile") broker. Same as the creator of EA. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * UdineEA Official Thread
  *   * [ **Reply to Thread** ](/thread/533099-udineea-official-thread/reply#reply)

  * More

[](https://www.forexfactory.com "Homepage")

  * [Forums](forums)
  * [Trades](trades)
  * [Calendar](calendar)
  * [News](news)
  * [Market](market)
  * [Brokers](brokers)

****

[](https://www.faireconomy.com/)

  * 

[The Official "Ok, now I'm pissed" Thread](/thread/73546-the-official-ok-now-im-pissed-thread "Hello Everyone, 
 
Seeing the apparent lack of threads of this nature \(just kidding, but read on\) I have decided to set up a respectable...") 51 replies

[Historic Charts: NZ Official Cash Rate](/thread/20380-historic-charts-nz-official-cash-rate "Sep 14, 2005") 15 replies

[Is there an official exchange rate?!](/thread/11571-is-there-an-official-exchange-rate "Different brokers have different bid and ask prices for every cross or pair.  However, the bid and ask price is based on something...I am...") 14 replies

[Official forex time zone](/thread/9940-official-forex-time-zone "is there a standard forex time zone? do i follow gmt or NY time? i use 4 hour charts and sometimes the time is way off because of time zone...") 3 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/533099-udineea-official-thread/reply#reply)
  * Subscribe
  * [100](javascript:void\(0\);)

Attachments: UdineEA Official Thread

Tags: UdineEA Official Thread

#  [](/thread/533099-udineea-official-thread)UdineEA Official Thread 

  * 

  * [#201](/thread/post/8180420#post8180420 "Post Permalink")

  * Apr 2, 2015 4:38pm  Apr 2, 2015 4:38pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar388093_1.gif) firewight](firewight)

  * | Joined Oct 2014  | Status: Trader | [817 Posts](/search?do=process&provider=Member&searchuser=388093)

> [Quoting skyline](/thread/post/8178992#post8178992 "View Quoted Post")
> 
> Disliked
> 
> {quote} maybe did you think that this EA placed only winning trades or make you rich overnight ? I guess you have to learn a lot what trading is about... ![](https://resources.faireconomy.media/images/emojis/64/1f612.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/231b.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/263a-fe0f.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f4ad.png?v=15.1)
> 
> Ignored

I agree, lets not complain, but work together to help this EA see it's true potential! 

Life is like a snickers, its full of nuts!

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#202](/thread/post/8180535#post8180535 "Post Permalink")

  * Apr 2, 2015 5:35pm  Apr 2, 2015 5:35pm 

  * [ trader34](trader34)

  * Joined Jan 2014 | Status: Sad to see this site's demise | [467 Posts](/search?do=process&provider=Member&searchuser=361210)

> [Quoting Mariodrugs](/thread/post/8178901#post8178901 "View Quoted Post")
> 
> Disliked
> 
> I have to officialy says that: Udine EA doesn't works. DONT USE IT ON REAL ACCOUNTS, IT MAKES LOOSES. {image}
> 
> Ignored

Hi,  
@Mariodrugs;  
I know it has been said, but it's not really fair to say the EA doesn't work. Aside from a couple of glitches which have been/are being resolved it actually seems well coded and performs as it should. I Have run it all this week and (once i remembered to allow DLL imports ![](https://resources.faireconomy.media/images/emojis/64/1f62b.png?v=15.1)). It took entries as I would expect. So, you really can't take issue with the EA.  
Did you follow the original thread and trade the method manually?  
  
If you did then you should not be surprised that you suffer losses.  
  
Actually, in this way I think the choice of Udine's method for an EA test is a curious one.  
  
@skyline, please don't get me wrong; I really appreciate your effort and your coding abilities, but as someone who has followed Udine's thread you must have realized that mechanical execution via an EA would not go so well? Probably not the best reflection of your clearly good coding skills.  
  
Also, most are probably aware that a short time ago, another member released a dashboard for this method. It's worth asking yourself why he didn't release an EA?  
  
I followed the thread for a long time, demo trading for a while, but I moved to live trading smaller risk within a month. In my opinion live trading is the only way to really test something with such tight pip parameters. I traded it for around 6 months before I decided to discontinue.   
Over that time I was profitable, but my results didn't come close to the ones posted by Udine.  
  
Udine's method works for him because he uses his own discretionary analysis to filter the low probability trades. Someone else here has already alluded to such filters, with pair sync, proximity to DO line etc.   
Without these filters, and without viewing the charts objectively as they evolve dynamically, the 00 method will be a losing one.   
  
Mathematically; excluding costs and with the RR ration of 2:1, you must maintain a 66% winning rate to break even overall. With costs and execution factors such as slippage and commissions, that creeps to more like +70%.   
Just to break even!  
  
The overall principle of the method is simple, but making it work is just as difficult as any other.  
The biggest problem is; once you suffer DD, you will need an excellent win rate to get back on track. 2 wins are needed to not quite cover one full loss, so once you are sitting in around -6% DD, you would need 3 clear winning days to get back to BE. It was for this reason I stopped. I am simply not as good as Udine at filtering.  
  
You may ask why I'm bothering to test the EA if I think it will not do well?  
Simply put; it's always good to know where to find a good coder ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)  
I know the method, I know how the EA should operate.   
If it does this well, I may want to employ skyline's services if he is willing.  
  
Will still be testing and watching. Good luck all! 

Wealth comes from what you keep, not what you earn

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#203](/thread/post/8180629#post8180629 "Post Permalink")

  * Apr 2, 2015 6:04pm  Apr 2, 2015 6:04pm 

  * [ Mariodrugs](mariodrugs)

  * | Membership Revoked  | Joined Dec 2014 | [379 Posts](/search?do=process&provider=Member&searchuser=394832)

> [Quoting trader34](/thread/post/8180535#post8180535 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi, @Mariodrugs; I know it has been said, but it's not really fair to say the EA doesn't work. Aside from a couple of glitches which have been/are being resolved it actually seems well coded and performs as it should. I Have run it all this week and (once i remembered to allow DLL imports ![](https://resources.faireconomy.media/images/emojis/64/1f62b.png?v=15.1)). It took entries as I would expect. So, you really can't take issue with the EA. Did you follow the original thread and trade the method manually? If you did then you should not be surprised that you suffer losses. Actually, in this way I think the...
> 
> Ignored

Yes i was following first original thread of Udine 00 level trading. I couldnt earn by that system. More looses -10 sl than +5 tp. That system was not profitable for me. I though I dont understand that system so exit from that. Now I saw Udine EA Robot! Wow. Maybe this will help me to understand that system! ...nope. it didn't. This is making me that futher confirmed much more that Udine 00. level trading is a scam and doesnt works. You need 100 others techniques and analyses to confirm entry on Udine 00. level. If you dont use 100 other analyses S/R and all other stuff - Udine's startegy won't work!! You do not need Udine entry. You need 100 others analyses and other stuff to enter.  
So I came to the conclusion that that is not important where we enter or it will be .00 level, .010 level .0234 level 0.456 level 0.900 level .100 level, .6785, .2734, .7654 - The Price Will Do What They Want. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#204](/thread/post/8180700#post8180700 "Post Permalink")

  * Apr 2, 2015 6:33pm  Apr 2, 2015 6:33pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

Hi Trader34,  
thank you for your post !  
I completely agree with you, infact I wrote multiple times that I don't believe in this EA to be profitable in the long run (+1 years) for a lot of reasons mostly because it cannot backtested with good accuracy.  
I just coded it as a challenge to see if Udine's strategy could be automatized , the problem I faced then was that original method posted by him was changed over and over adding multiple indicators, filter and so on, so as you said it's impossible to code the whole strategy because a lot of discrectionary is involved and this is the reason why I decided to lock it only to run on demo account to prevent users (as MarioDrugs) in search of the holy grail could burn the account then coming here to complain because lost money.  
  
Regards,  
Skyline 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#205](/thread/post/8180858#post8180858 "Post Permalink")

  * Apr 2, 2015 7:25pm  Apr 2, 2015 7:25pm 

  * [ trader34](trader34)

  * Joined Jan 2014 | Status: Sad to see this site's demise | [467 Posts](/search?do=process&provider=Member&searchuser=361210)

> [Quoting skyline](/thread/post/8180700#post8180700 "View Quoted Post")
> 
> Disliked
> 
> Hi Trader34, thank you for your post ! I completely agree with you, infact I wrote multiple times that I don't believe in this EA to be profitable in the long run (+1 years) for a lot of reasons mostly because it cannot backtested with good accuracy. I just coded it as a challenge to see if Udine's strategy could be automatized , the problem I faced then was that original method posted by him was changed over and over adding multiple indicators, filter and so on, so as you said it's impossible to code the whole strategy because a lot of discrectionary...
> 
> Ignored

It's a worthy challenge, for sure!  
But I like your EA. I'm no coder, but I appreciate the complexities of getting this method right. As I said, I think you've done a good job. Frankly I don't care if it blows the account. I'm fairly sure it won't be positive.  
  
Mariodrugs;  
It should be obvious to a trader that if you can't manually profit from a system, an EA won't change that. All the mechanical information is in the EA from Skyline. Despite best efforts, it's impossible to code in all the discretionary filters.   
In the best case, if I were a 00 trader, I would have used this EA to alert me to potential entries. This way, I could focus on other things, and if/when an alert came, I could decide whether or not to trade it. But, I don't trade 00 anymore.  
  
Also, fine 00 didn't work for you. But I don't see how you can call it a scam.   
Udine hasn't sold anything. Hasn't asked for anything (other than a coffee in person! ![](https://resources.faireconomy.media/images/emojis/64/1f923.png?v=15.1))   
I have my own very negative opinions regarding the dashboard, but that was not from Udine himself. Nor as I understand, does he profit from any sales.  
Udine is still there, offering support, answering questions and updating in that thread, not asking for a cent.   
I fail to see how this is a scam.  
  
I used it, and I made money. Not a lot, and not enough to hold my attention, but I don't blame the method.  
I don't doubt Udine uses it, and makes money.   
I can't use the system well, but I don't take it personally. It just doesn't fit my style.   
Am I a crap trader because I can't replicate Udine's results?  
If I shared my methods, would you be a crap trader if you could not replicate mine?  
  
I'm not picking on you, but it seems you are taking all this too personally.  
If there was one single answer on how to make money in FX then there would be no need for forums such as this.  
  
In a way, you are absolutely right. it doesn't matter what imaginary line the price crosses.   
All that matters is that you can react to a certain price action, and make money from it. 

Wealth comes from what you keep, not what you earn

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#206](/thread/post/8181139#post8181139 "Post Permalink")

  * Apr 2, 2015 9:07pm  Apr 2, 2015 9:07pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar389954_3.gif) honestknave](honestknave)

  * Joined Nov 2014 | Status: Trader | [1,300 Posts](/search?do=process&provider=Member&searchuser=389954)

> [Quoting skyline](/thread/post/8180700#post8180700 "View Quoted Post")
> 
> Disliked
> 
> Hi Trader34, thank you for your post ! I completely agree with you, infact I wrote multiple times that I don't believe in this EA to be profitable in the long run (+1 years) for a lot of reasons mostly because it cannot backtested with good accuracy. I just coded it as a challenge to see if Udine's strategy could be automatized , the problem I faced then was that original method posted by him was changed over and over adding multiple indicators, filter and so on, so as you said it's impossible to code the whole strategy because a lot of discrectionary...
> 
> Ignored

I integrated the 00 method into my trading for a while, back when I was looking for something involving less screen time.  
  
It worked out OK for me but ultimately I dropped it. The main reason was that I was just trading my normal (discretional) way within the 00 framework.  
  
Because of the discretional aspect required, I commented to Udine that I doubted it would be viable as an EA. He agreed. That being said, I applaud skyline for his efforts and I look forward to seeing where the project goes next ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) Code is reusable, and the project may well spawn on to bigger and better things!  
  
In more general terms, I think it is very unlikely that the humble masses will ever manage to create a hands-off EA that can consistently make profits over an extended period of time without manual intervention. Doesn't stop us all from trying though ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)  
  
Thanks for sharing skyline ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#207](/thread/post/8181179#post8181179 "Post Permalink")

  * Apr 2, 2015 9:24pm  Apr 2, 2015 9:24pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting honestknave](/thread/post/8181139#post8181139 "View Quoted Post")
> 
> Disliked
> 
> {quote} I integrated the 00 method into my trading for a while, back when I was looking for something involving less screen time. It worked out OK for me but ultimately I dropped it. The main reason was that I was just trading my normal (discretional) way within the 00 framework. Because of the discretional aspect required, I commented to Udine that I doubted it would be viable as an EA. He agreed. That being said, I applaud skyline for his efforts and I look forward to seeing where the project goes next ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) Code is reusable, and the project may...
> 
> Ignored

Hi Honestknave,  
yes I can ultimately add a parameter option that turn on/off placing trades so that this ea could act also as a normal indicator that only alert for potential entries , and will be only users care to place the trades, btw we'll see what future bring to us ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)  
  
Cheers,  
Skyline 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#208](/thread/post/8181356#post8181356 "Post Permalink")

  * Apr 2, 2015 10:17pm  Apr 2, 2015 10:17pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar389954_3.gif) honestknave](honestknave)

  * Joined Nov 2014 | Status: Trader | [1,300 Posts](/search?do=process&provider=Member&searchuser=389954)

> [Quoting skyline](/thread/post/8181179#post8181179 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi Honestknave, yes I can ultimately add a parameter option that turn on/off placing trades so that this ea could act also as a normal indicator that only alert for potential entries , and will be only users care to place the trades, btw we'll see what future bring to us ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1) Cheers, Skyline
> 
> Ignored

Excellent! I look forward to it ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#209](/thread/post/8181393#post8181393 "Post Permalink")

  * Apr 2, 2015 10:25pm  Apr 2, 2015 10:25pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377617_1.gif) merrygold](merrygold)

  * Joined Jul 2014 | Status: Trader | [736 Posts](/search?do=process&provider=Member&searchuser=377617)

> [Quoting Mariodrugs](/thread/post/8180629#post8180629 "View Quoted Post")
> 
> Disliked
> 
> {quote} Yes i was following first original thread of Udine 00 level trading. I couldnt earn by that system. More looses -10 sl than +5 tp. That system was not profitable for me. I though I dont understand that system so exit from that. Now I saw Udine EA Robot! Wow. Maybe this will help me to understand that system! ...nope. it didn't. This is making me that futher confirmed much more that Udine 00. level trading is a scam and doesnt works. You need 100 others techniques and analyses to confirm entry on Udine 00. level. If you dont use 100 other...
> 
> Ignored

Funny to see how you jump from system to system, trying them out for about a week, and then make a conclusion its scam.  
you have been member of FF since December 14, and you have been jumping from system to system, and saying its scam and forex is based on luck. Hope you soon realize that Trading was never made for you. 

MY SITTING, NEVER MY THINKING!

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#210](/thread/post/8181428#post8181428 "Post Permalink")

  * Apr 2, 2015 10:33pm  Apr 2, 2015 10:33pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting merrygold](/thread/post/8181393#post8181393 "View Quoted Post")
> 
> Disliked
> 
> {quote} Funny to see how you jump from system to system, trying them out for about a week, and then make a conclusion its scam. you have been member of FF since December 14, and you have been jumping from system to system, and saying its scam and forex is based on luck. Hope you soon realize that Trading was never made for you.
> 
> Ignored

![](https://resources.faireconomy.media/images/emojis/64/1f44f.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#211](/thread/post/8181434#post8181434 "Post Permalink")

  * Apr 2, 2015 10:35pm  Apr 2, 2015 10:35pm 

  * [ Mariodrugs](mariodrugs)

  * | Membership Revoked  | Joined Dec 2014 | [379 Posts](/search?do=process&provider=Member&searchuser=394832)

> [Quoting merrygold](/thread/post/8181393#post8181393 "View Quoted Post")
> 
> Disliked
> 
> {quote} Funny to see how you jump from system to system, trying them out for about a week, and then make a conclusion its scam. you have been member of FF since December 14, and you have been jumping from system to system, and saying its scam and forex is based on luck. Hope you soon realize that Trading was never made for you.
> 
> Ignored

Naaah, im much longer. I just changed accounts many times ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#212](/thread/post/8181438#post8181438 "Post Permalink")

  * Apr 2, 2015 10:36pm  Apr 2, 2015 10:36pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377617_1.gif) merrygold](merrygold)

  * Joined Jul 2014 | Status: Trader | [736 Posts](/search?do=process&provider=Member&searchuser=377617)

> [Quoting Mariodrugs](/thread/post/8181434#post8181434 "View Quoted Post")
> 
> Disliked
> 
> {quote} Naaah, im much longer. I just changed accounts many times ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)
> 
> Ignored

Think there is a reason for that ![](https://resources.faireconomy.media/images/emojis/64/1f644.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)

MY SITTING, NEVER MY THINKING!

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#213](/thread/post/8181489#post8181489 "Post Permalink")

  * Apr 2, 2015 10:51pm  Apr 2, 2015 10:51pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar65017_5.gif) t3ric](t3ric)

  * | Joined Mar 2008  | Status: Trader | [8 Posts](/search?do=process&provider=Member&searchuser=65017)

> [Quoting skyline](/thread/post/8181179#post8181179 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi Honestknave, yes I can ultimately add a parameter option that turn on/off placing trades so that this ea could act also as a normal indicator that only alert for potential entries , and will be only users care to place the trades, btw we'll see what future bring to us ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1) Cheers, Skyline
> 
> Ignored

Hi Skyline . . good job on your EA, I've been a lurker in Udine system from almost the beginning but never post anything. Just observe and try it on my own account. From what I learn by Udine's Charts and comments, there are more support / resistance levels that we must take into account when we are going to place an entry. (besides pivot levels, big round number, etc). Those levels are happening when the price in the sideways mode, and in my understanding an EA can not locate a dinamic levels like those ( please correct me if I am wrong).   
  
That's why by giving an option to make this EA as an indicator to help identifying the possibility of entry will be very useful.   
  
may the green pips be with us in the next trade ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
  
t3ric 

Always Set Stop Loss !! Trade what you see .... Not what you think !!

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#214](/thread/post/8182200#post8182200 "Post Permalink")

  * Apr 3, 2015 3:57am  Apr 3, 2015 3:57am 

  * [ Mariodrugs](mariodrugs)

  * | Membership Revoked  | Joined Dec 2014 | [379 Posts](/search?do=process&provider=Member&searchuser=394832)

> [Quoting merrygold](/thread/post/8181438#post8181438 "View Quoted Post")
> 
> Disliked
> 
> {quote} Think there is a reason for that ![](https://resources.faireconomy.media/images/emojis/64/1f644.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)
> 
> Ignored

Jumping from system to system like you are all here ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1) ![](https://resources.faireconomy.media/images/emojis/64/1f923.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#215](/thread/post/8182207#post8182207 "Post Permalink")

  * Apr 3, 2015 4:02am  Apr 3, 2015 4:02am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting Mariodrugs](/thread/post/8182200#post8182200 "View Quoted Post")
> 
> Disliked
> 
> {quote} Jumping from system to system like you are all here ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1) ![](https://resources.faireconomy.media/images/emojis/64/1f923.png?v=15.1)
> 
> Ignored

yes absolutely, at least for me, but i don't complain yelling about scam alert if I'm unable to make money using a trading system. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#216](/thread/post/8182210#post8182210 "Post Permalink")

  * Apr 3, 2015 4:04am  Apr 3, 2015 4:04am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377617_1.gif) merrygold](merrygold)

  * Joined Jul 2014 | Status: Trader | [736 Posts](/search?do=process&provider=Member&searchuser=377617)

> [Quoting skyline](/thread/post/8182207#post8182207 "View Quoted Post")
> 
> Disliked
> 
> {quote} yes absolutely, at least for me, but i don't complain yelling about scam alert if I'm unable to make money using a trading system.
> 
> Ignored

Spot on!![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)

MY SITTING, NEVER MY THINKING!

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#217](/thread/post/8182376#post8182376 "Post Permalink")

  * Apr 3, 2015 6:07am  Apr 3, 2015 6:07am 

  * [ Mariodrugs](mariodrugs)

  * | Membership Revoked  | Joined Dec 2014 | [379 Posts](/search?do=process&provider=Member&searchuser=394832)

ok, no more spam ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) lets hope EA will work soon ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) ! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#218](/thread/post/8182393#post8182393 "Post Permalink")

  * Apr 3, 2015 6:27am  Apr 3, 2015 6:27am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377617_1.gif) merrygold](merrygold)

  * Joined Jul 2014 | Status: Trader | [736 Posts](/search?do=process&provider=Member&searchuser=377617)

> [Quoting Mariodrugs](/thread/post/8182376#post8182376 "View Quoted Post")
> 
> Disliked
> 
> ok, no more spam ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) lets hope EA will work soon ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) !
> 
> Ignored

![](https://resources.faireconomy.media/images/emojis/64/1f44f.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f973.png?v=15.1) \- Happy trading ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)

MY SITTING, NEVER MY THINKING!

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#219](/thread/post/8183238#post8183238 "Post Permalink")

  * Apr 3, 2015 7:54pm  Apr 3, 2015 7:54pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar309469_3.gif) gigicualex](gigicualex)

  * | Joined Nov 2012  | Status: Trader | [1,187 Posts](/search?do=process&provider=Member&searchuser=309469)

> [Quoting trader34](/thread/post/8180535#post8180535 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi, @Mariodrugs; I know it has been said, but it's not really fair to say the EA doesn't work. Aside from a couple of glitches which have been/are being resolved it actually seems well coded and performs as it should. I Have run it all this week and (once i remembered to allow DLL imports ![](https://resources.faireconomy.media/images/emojis/64/1f62b.png?v=15.1)). It took entries as I would expect. So, you really can't take issue with the EA. Did you follow the original thread and trade the method manually? If you did then you should not be surprised that you suffer losses. Actually, in this way I think the...
> 
> Ignored

Fully agree with trader34 here. Been following Udine's thread for few months now and guarantee that there is no scam there. Udine is a good person, a giver which offered FF's community a free system asking nothing in return. The system works for some ppl, for some doesn't work ..all depends on ones personality, experience and other factors.  
Trader34's experience is similar to mine, the system doesn't work for me either and as already mentioned on that thread as well, you need that so called "6th sense" that the successful traders posses to stay away from bad trades.  
I congratulate Skyline for his effort of creating an EA based on Udine's 1st post and I'm pleased to be a part of this testing group. Even though I also think that, if u are not able to be profitable manually trading a system, an EA won't change the result, I like the general idea of this program placing trades according to the rules and without any discretion(that us humans get affected). I'm looking forward to the end of the month results and if the results would get as bad as I suppose they will be, this system could prove a great reverse trading idea(placing buy instead of sells with 1:2 RR) 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#220](/thread/post/8183949#post8183949 "Post Permalink")

  * Apr 3, 2015 11:13pm  Apr 3, 2015 11:13pm 

  * [ turboguru](turboguru)

  * | Joined Aug 2008  | Status: Trader | [555 Posts](/search?do=process&provider=Member&searchuser=76392)

Just a suggestion and no I'm not running the EA but one of the main things for the 00 system is just 2 hrs each session not running 24/5 maybe this can help with the win rate of the EA. It might work it just might not work running full time. It's all about momentum and liquidity and we are heading to the time of year that it's going to start thinning out. I haven't seen where yall are running session times if you are. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * UdineEA Official Thread
  *   * [ **Reply to Thread** ](/thread/533099-udineea-official-thread/reply#reply)

  * More

[](https://www.forexfactory.com "Homepage")

  * [Forums](forums)
  * [Trades](trades)
  * [Calendar](calendar)
  * [News](news)
  * [Market](market)
  * [Brokers](brokers)

****

[](https://www.faireconomy.com/)

  * 

[The Official "Ok, now I'm pissed" Thread](/thread/73546-the-official-ok-now-im-pissed-thread "Hello Everyone, 
 
Seeing the apparent lack of threads of this nature \(just kidding, but read on\) I have decided to set up a respectable...") 51 replies

[Historic Charts: NZ Official Cash Rate](/thread/20380-historic-charts-nz-official-cash-rate "Sep 14, 2005") 15 replies

[Is there an official exchange rate?!](/thread/11571-is-there-an-official-exchange-rate "Different brokers have different bid and ask prices for every cross or pair.  However, the bid and ask price is based on something...I am...") 14 replies

[Official forex time zone](/thread/9940-official-forex-time-zone "is there a standard forex time zone? do i follow gmt or NY time? i use 4 hour charts and sometimes the time is way off because of time zone...") 3 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/533099-udineea-official-thread/reply#reply)
  * Subscribe
  * [100](javascript:void\(0\);)

Attachments: UdineEA Official Thread

Tags: UdineEA Official Thread

#  [](/thread/533099-udineea-official-thread)UdineEA Official Thread 

  * 

  * [#221](/thread/post/8184016#post8184016 "Post Permalink")

  * Apr 3, 2015 11:38pm  Apr 3, 2015 11:38pm 

  * [ DerBerliner](derberliner)

  * | Joined Feb 2011  | Status: Trader | [822 Posts](/search?do=process&provider=Member&searchuser=168827)

Hmm .... no trades in skylines treade explorer ? I had 3 trades = 3 winners today:  
[http://www.myfxbook.com/members/TGT_...rading/1201341](http://www.myfxbook.com/members/TGT_FX/udine-ea-v114-00level-trading/1201341)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#222](/thread/post/8184119#post8184119 "Post Permalink")

  * Apr 4, 2015 12:19am  Apr 4, 2015 12:19am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

Hi DerBerliner good results ! ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)  
I had internet problem with my laptop, btw took 2 win and 1 be on another demo account running on my vps ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)  
  
Cheers,  
Skyline 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#223](/thread/post/8185281#post8185281 "Post Permalink")

  * Apr 4, 2015 11:34pm  Apr 4, 2015 11:34pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar379623_3.gif) RoneyFX](roneyfx)

  * | Joined Aug 2014  | Status: Trader | [129 Posts](/search?do=process&provider=Member&searchuser=379623)

This EA is good to find ideal SL/TP/TS for each pair, modelling quality seems to be not good but testing it manually the results are same.  
In the third image you can see the elevate TP in london session(and little sl), now im triying to find a method to take only it without the little constant losses, i find that the most of this big moves are starting on london session, and doing only 2 frist trades the results are awesome, it would be cool if skyline make a string to select trading hours and each TP/SL/TL, the system would make elevate profits because every session need different setting and it would be even more powerful if working on lesses timeframes like m1, i know its different from Udine method but absolutly more profitable  
**What do you guys think about this?**  
  
<http://i.share.pho.to/46f60869_o.gif>  
<http://i.share.pho.to/c7b4843d_o.gif>  
<http://i.share.pho.to/81a132ac_o.gif>  
<http://i.share.pho.to/c1b68727_o.gif>  
<http://i.share.pho.to/c2bd5f91_o.gif>  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: tua.PNG
Size: 11 KB](/attachment/image/1646944/thumbnail?d=1428158372)](/attachment/image/1646944?d=1428158372)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#224](/thread/post/8185543#post8185543 "Post Permalink")

  * Apr 5, 2015 4:47am  Apr 5, 2015 4:47am 

  * [ DerBerliner](derberliner)

  * | Joined Feb 2011  | Status: Trader | [822 Posts](/search?do=process&provider=Member&searchuser=168827)

No offense bro, but nobody wont relay on BT's with 65% or n/a modelling quality ! If you can get any settings from a BT you are convinced of, anyway be that as it may: so put them into a forward test !! ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#225](/thread/post/8186157#post8186157 "Post Permalink")

  * Apr 6, 2015 3:29am  Apr 6, 2015 3:29am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar379623_3.gif) RoneyFX](roneyfx)

  * | Joined Aug 2014  | Status: Trader | [129 Posts](/search?do=process&provider=Member&searchuser=379623)

> [Quoting DerBerliner](/thread/post/8185543#post8185543 "View Quoted Post")
> 
> Disliked
> 
> No offense bro, but nobody wont relay on BT's with 65% or n/a modelling quality ! If you can get any settings from a BT you are convinced of, anyway be that as it may: so put them into a forward test !! ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)
> 
> Ignored

I have tested it manually with same results 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#226](/thread/post/8186343#post8186343 "Post Permalink")

  * Apr 6, 2015 7:25am  Apr 6, 2015 7:25am 

  * [ DerBerliner](derberliner)

  * | Joined Feb 2011  | Status: Trader | [822 Posts](/search?do=process&provider=Member&searchuser=168827)

> [Quoting RoneyFX](/thread/post/8186157#post8186157 "View Quoted Post")
> 
> Disliked
> 
> {quote} I have tested it manually with same results
> 
> Ignored

Ok mate - that sounds good ! So, in this case you could simply post the best setfiles ? Right ? ![](https://resources.faireconomy.media/images/emojis/64/1f918.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#227](/thread/post/8186944#post8186944 "Post Permalink")

  * Apr 6, 2015 7:26pm  Apr 6, 2015 7:26pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar350360_20.gif) AKCodingEye](akcodingeye)

  * Joined Sep 2013 | Status: Such a Silly Game It is | [181 Posts](/search?do=process&provider=Member&searchuser=350360)

Skyline  
  
What's spread you set for each pairs please? On first page it says below 2 pips but it shows Spread Too high for most pairs. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: IG Udine.jpg
Size: 77 KB](/attachment/image/1647430/thumbnail?d=1428315928)](/attachment/image/1647430?d=1428315928)   

Whats get measured get improved

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#228](/thread/post/8187184#post8187184 "Post Permalink")

  * Apr 6, 2015 10:05pm  Apr 6, 2015 10:05pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting AKCodingEye](/thread/post/8186944#post8186944 "View Quoted Post")
> 
> Disliked
> 
> Skyline What's spread you set for each pairs please? On first page it says below 2 pips but it shows Spread Too high for most pairs. {image}
> 
> Ignored

Hi AkCodingEye,  
that write is only a visual alert it doesn't prevent opening order by EA, infact I'll remove because there's a lot of questions about this spread thing.  
Btw the limit are set as follow :  
  
EU ,GU,EJ : 1 pips  
GJ : 1.5 pips  
  
if your broker comes with spread higher than above (as in your case) then it's better to not use UdineEA nor trading Udine method at all (it's only my opinion). 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#229](/thread/post/8187319#post8187319 "Post Permalink")

  * Apr 6, 2015 11:15pm  Apr 6, 2015 11:15pm 

  * [ DerBerliner](derberliner)

  * | Joined Feb 2011  | Status: Trader | [822 Posts](/search?do=process&provider=Member&searchuser=168827)

Although some news have been out - today I didn't got any trades ... so far. A boring day, monday plus bank holiday ... sit and wait ... ![](https://resources.faireconomy.media/images/emojis/64/1f634.png?v=15.1) ![](https://resources.faireconomy.media/images/emojis/64/1f634.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#230](/thread/post/8187344#post8187344 "Post Permalink")

  * Apr 6, 2015 11:27pm  Apr 6, 2015 11:27pm 

  * [ unimak](unimak)

  * Joined Nov 2009 | Status: Trader | [709 Posts](/search?do=process&provider=Member&searchuser=124331)

Hi  
  
I am looking for somebody who will help in coding a EA which will be trading almost all pairs yet it is very simple . 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#231](/thread/post/8187375#post8187375 "Post Permalink")

  * Apr 6, 2015 11:42pm  Apr 6, 2015 11:42pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting DerBerliner](/thread/post/8187319#post8187319 "View Quoted Post")
> 
> Disliked
> 
> Although some news have been out - today I didn't got any trades ... so far. A boring day, monday plus bank holiday ... sit and wait ... ![](https://resources.faireconomy.media/images/emojis/64/1f634.png?v=15.1) ![](https://resources.faireconomy.media/images/emojis/64/1f634.png?v=15.1)
> 
> Ignored

Indeed very boring day, I had only one EJ long trade +5 pips , better than nothing ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)  
  
Cheers,  
Skyline 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#232](/thread/post/8187396#post8187396 "Post Permalink")

  * Apr 6, 2015 11:54pm  Apr 6, 2015 11:54pm 

  * [ unimak](unimak)

  * Joined Nov 2009 | Status: Trader | [709 Posts](/search?do=process&provider=Member&searchuser=124331)

EJ Superb day buy at 130.74 hits 131.29 super trade . I have trades in all the pairs .   
  
  
Skype ID : unimakFF 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#233](/thread/post/8189886#post8189886 "Post Permalink")

  * Apr 7, 2015 11:59pm  Apr 7, 2015 11:59pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

Today results 3 wins , 3 be (+15 pips) :  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot1.png
Size: 12 KB](/attachment/image/1648405/thumbnail?d=1428418724)](/attachment/image/1648405?d=1428418724)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#234](/thread/post/8190073#post8190073 "Post Permalink")

  * Apr 8, 2015 1:15am  Apr 8, 2015 1:15am 

  * [ Johanl66](johanl66)

  * | Joined Jan 2011  | Status: Trader | [36 Posts](/search?do=process&provider=Member&searchuser=168624)

this is cool  
  
I had 5 wins and 1 small loss  
  
awesome 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#235](/thread/post/8191353#post8191353 "Post Permalink")

  * Apr 8, 2015 4:45pm  Apr 8, 2015 4:45pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

EJ long @130.20 to TP 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot1.png
Size: 15 KB](/attachment/image/1648874/thumbnail?d=1428479099)](/attachment/image/1648874?d=1428479099)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#236](/thread/post/8191413#post8191413 "Post Permalink")

  * Apr 8, 2015 5:07pm  Apr 8, 2015 5:07pm 

  * [ Bhutugly](bhutugly)

  * | Joined Oct 2011  | Status: Trader | [12 Posts](/search?do=process&provider=Member&searchuser=200586)

Skyline,  
  
Any reason why this is happening, it didn't trigger a trade, just confused me!(Doesn't take a lot)!  
  

Attached Image

![](/attachment/image/1648905?d=1428480452)

  
  
Cheers  
  
Ian 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#237](/thread/post/8191482#post8191482 "Post Permalink")

  * Apr 8, 2015 5:30pm  Apr 8, 2015 5:30pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar309469_3.gif) gigicualex](gigicualex)

  * | Joined Nov 2012  | Status: Trader | [1,187 Posts](/search?do=process&provider=Member&searchuser=309469)

Yes, I was wondering about same thing.  
GBPJPY London Open Candle from .200 level 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot1.png
Size: 32 KB](/attachment/image/1648929/thumbnail?d=1428481811)](/attachment/image/1648929?d=1428481811)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#238](/thread/post/8191566#post8191566 "Post Permalink")

  * Apr 8, 2015 6:19pm  Apr 8, 2015 6:19pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting Bhutugly](/thread/post/8191413#post8191413 "View Quoted Post")
> 
> Disliked
> 
> Skyline, Any reason why this is happening, it didn't trigger a trade, just confused me!(Doesn't take a lot)! {image} Cheers Ian
> 
> Ignored

Hi Bhutugly,  
it happens because that line is only a *potential* entry point , if all conditions are met then an order is placed otherwise is not placed.  
Btw i'm working on a new version (will share on weekend) where all conditions entry are shown clearly on chart , so that you know why an order is not placed.  
  

Attached Image

![](/attachment/image/1648969?d=1428484705)

  
  
Cheers,  
Skyline 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#239](/thread/post/8191584#post8191584 "Post Permalink")

  * Apr 8, 2015 6:28pm  Apr 8, 2015 6:28pm 

  * [ Bhutugly](bhutugly)

  * | Joined Oct 2011  | Status: Trader | [12 Posts](/search?do=process&provider=Member&searchuser=200586)

Is anyone getting trade entries?  
  
Cheers  
  
Ian 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#240](/thread/post/8191636#post8191636 "Post Permalink")

  * Apr 8, 2015 6:51pm  Apr 8, 2015 6:51pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar338950_1.gif) cescof](cescof)

  * Joined Jun 2013 | Status: Trader | [1,006 Posts](/search?do=process&provider=Member&searchuser=338950)

> [Quoting skyline](/thread/post/8191353#post8191353 "View Quoted Post")
> 
> Disliked
> 
> EJ long @130.20 to TP {image}
> 
> Ignored

Same here![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)  
Waiting for new updates...  
Thanks for effort  
Regards 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * UdineEA Official Thread
  *   * [ **Reply to Thread** ](/thread/533099-udineea-official-thread/reply#reply)

  * More

[](https://www.forexfactory.com "Homepage")

  * [Forums](forums)
  * [Trades](trades)
  * [Calendar](calendar)
  * [News](news)
  * [Market](market)
  * [Brokers](brokers)

****

[](https://www.faireconomy.com/)

  * 

[The Official "Ok, now I'm pissed" Thread](/thread/73546-the-official-ok-now-im-pissed-thread "Hello Everyone, 
 
Seeing the apparent lack of threads of this nature \(just kidding, but read on\) I have decided to set up a respectable...") 51 replies

[Historic Charts: NZ Official Cash Rate](/thread/20380-historic-charts-nz-official-cash-rate "Sep 14, 2005") 15 replies

[Is there an official exchange rate?!](/thread/11571-is-there-an-official-exchange-rate "Different brokers have different bid and ask prices for every cross or pair.  However, the bid and ask price is based on something...I am...") 14 replies

[Official forex time zone](/thread/9940-official-forex-time-zone "is there a standard forex time zone? do i follow gmt or NY time? i use 4 hour charts and sometimes the time is way off because of time zone...") 3 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/533099-udineea-official-thread/reply#reply)
  * Subscribe
  * [100](javascript:void\(0\);)

Attachments: UdineEA Official Thread

Tags: UdineEA Official Thread

#  [](/thread/533099-udineea-official-thread)UdineEA Official Thread 

  * 

  * [#241](/thread/post/8191685#post8191685 "Post Permalink")

  * Apr 8, 2015 7:12pm  Apr 8, 2015 7:12pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar402612_1.gif) mokuro89](mokuro89)

  * Joined Mar 2015 | Status: Trader | [449 Posts](/search?do=process&provider=Member&searchuser=402612)

> [Quoting skyline](/thread/post/8191566#post8191566 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi Bhutugly, it happens because that line is only a *potential* entry point , if all conditions are met then an order is placed otherwise is not placed. Btw i'm working on a new version (will share on weekend) where all conditions entry are shown clearly on chart , so that you know why an order is not placed. {image} Cheers, Skyline
> 
> Ignored

Very nice filter skyline ![](https://resources.faireconomy.media/images/emojis/64/1f44f.png?v=15.1)  
EA in separated MT4 instance with this filters will help the live account on other MT4 because of the info/checklsit on taking decisions ![](https://resources.faireconomy.media/images/emojis/64/1f973.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#242](/thread/post/8192278#post8192278 "Post Permalink")

  * Apr 8, 2015 11:12pm  Apr 8, 2015 11:12pm 

  * [ arkan1976](arkan1976)

  * | Joined Sep 2009  | Status: Trader | [406 Posts](/search?do=process&provider=Member&searchuser=115431)

Thanks Skyline for the effort, the ea worlks perfectly !  
When do you think to share it for real account ? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#243](/thread/post/8192391#post8192391 "Post Permalink")

  * Apr 8, 2015 11:48pm  Apr 8, 2015 11:48pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting arkan1976](/thread/post/8192278#post8192278 "View Quoted Post")
> 
> Disliked
> 
> Thanks Skyline for the effort, the ea worlks perfectly ! When do you think to share it for real account ?
> 
> Ignored

I'm planning to unlock live account on next month 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#244](/thread/post/8192445#post8192445 "Post Permalink")

  * Apr 8, 2015 11:59pm  Apr 8, 2015 11:59pm 

  * [ arkan1976](arkan1976)

  * | Joined Sep 2009  | Status: Trader | [406 Posts](/search?do=process&provider=Member&searchuser=115431)

> [Quoting skyline](/thread/post/8192391#post8192391 "View Quoted Post")
> 
> Disliked
> 
> {quote} I'm planning to unlock live account on next month
> 
> Ignored

Thanks !! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#245](/thread/post/8194500#post8194500 "Post Permalink")

  * Apr 9, 2015 7:19pm  Apr 9, 2015 7:19pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

No orders opened so far , waiting for NY session.  
In the meantime, I'm still working on new interface for new upcoming version , do you like it ?  
  

Attached Image

![](/attachment/image/1649955?d=1428574754)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#246](/thread/post/8194518#post8194518 "Post Permalink")

  * Apr 9, 2015 7:24pm  Apr 9, 2015 7:24pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar352224_1.gif) dafa](dafa)

  * | Joined Oct 2013  | Status: Trader | [320 Posts](/search?do=process&provider=Member&searchuser=352224)

> [Quoting skyline](/thread/post/8194500#post8194500 "View Quoted Post")
> 
> Disliked
> 
> No orders opened so far , waiting for NY session. In the meantime, I'm still working on new interface for new upcoming version , do you like it ? {image}
> 
> Ignored

Looks great. ;-) Design is everytime on first place. :-D 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#247](/thread/post/8194525#post8194525 "Post Permalink")

  * Apr 9, 2015 7:27pm  Apr 9, 2015 7:27pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar402612_1.gif) mokuro89](mokuro89)

  * Joined Mar 2015 | Status: Trader | [449 Posts](/search?do=process&provider=Member&searchuser=402612)

> [Quoting skyline](/thread/post/8194500#post8194500 "View Quoted Post")
> 
> Disliked
> 
> No orders opened so far , waiting for NY session. In the meantime, I'm still working on new interface for new upcoming version , do you like it ? {image}
> 
> Ignored

Looks very good!! ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#248](/thread/post/8194539#post8194539 "Post Permalink")

  * Apr 9, 2015 7:33pm  Apr 9, 2015 7:33pm 

  * [ anuj20jain](anuj20jain)

  * | Joined Jan 2015  | Status: Trader | [88 Posts](/search?do=process&provider=Member&searchuser=395235)

> [Quoting skyline](/thread/post/8194500#post8194500 "View Quoted Post")
> 
> Disliked
> 
> No orders opened so far , waiting for NY session. In the meantime, I'm still working on new interface for new upcoming version , do you like it ? {image}
> 
> Ignored

Looks great. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#249](/thread/post/8194574#post8194574 "Post Permalink")

  * Apr 9, 2015 7:47pm  Apr 9, 2015 7:47pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

Ty guys ! ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)  
Mmm i think i have to use a different font since that one (Century Gothic) maybe could not be installed on each pc, so I will use Arial which is standard font :  
  

Attached Image

![](/attachment/image/1649969?d=1428576399)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#250](/thread/post/8194608#post8194608 "Post Permalink")

  * Apr 9, 2015 7:58pm  Apr 9, 2015 7:58pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar352224_1.gif) dafa](dafa)

  * | Joined Oct 2013  | Status: Trader | [320 Posts](/search?do=process&provider=Member&searchuser=352224)

> [Quoting skyline](/thread/post/8194574#post8194574 "View Quoted Post")
> 
> Disliked
> 
> Ty guys ! ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1) Mmm i think i have to use a different font since that one (Century Gothic) maybe could not be installed on each pc, so I will use Arial which is standard font : {image}
> 
> Ignored

I like Tahoma but it's up to you.;-) 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#251](/thread/post/8194653#post8194653 "Post Permalink")

  * Edited 8:31pm  Apr 9, 2015 8:16pm | Edited 8:31pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar389954_3.gif) honestknave](honestknave)

  * Joined Nov 2014 | Status: Trader | [1,300 Posts](/search?do=process&provider=Member&searchuser=389954)

May I humbly suggest a **mono-spaced font** such as Courier New? Makes it far easier (for you) to line everything up.  
Example:  
Mono-spaced (Courier New)  

Attached Image

![](/attachment/image/1650027?d=1428579048)

  
Not mono-spaced (Arial)  

Attached Image

![](/attachment/image/1650028?d=1428579061)

  
And a spacing option for those who have changed their font DPI :nerd: (high res monitors)  
  
Just a couple of thoughts ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#252](/thread/post/8194670#post8194670 "Post Permalink")

  * Apr 9, 2015 8:20pm  Apr 9, 2015 8:20pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar185229_8.gif) Erebus](erebus)

  * Joined Jul 2011 | Status: Trader | [8,576 Posts](/search?do=process&provider=Member&searchuser=185229)

Heck, just put a Font option in there ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)  
  
PS: I really like **Trebuchet MS**  
  
![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

"Forex a Great Hobby, But Not a Great Job"

[Texas-2-Step](erebus#79 "View Trade Explorer") All Time Return: 8.8%

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#253](/thread/post/8194713#post8194713 "Post Permalink")

  * Apr 9, 2015 8:39pm  Apr 9, 2015 8:39pm 

  * [ Bhutugly](bhutugly)

  * | Joined Oct 2011  | Status: Trader | [12 Posts](/search?do=process&provider=Member&searchuser=200586)

Really nice, Roll on the weekend!  
  
Cheers  
  
Ian 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#254](/thread/post/8194719#post8194719 "Post Permalink")

  * Apr 9, 2015 8:43pm  Apr 9, 2015 8:43pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar11046_3.gif) chaveznqoos](chaveznqoos)

  * Joined Jun 2006 | Status: Trader | [450 Posts](/search?do=process&provider=Member&searchuser=11046)

> [Quoting skyline](/thread/post/8194500#post8194500 "View Quoted Post")
> 
> Disliked
> 
> No orders opened so far , waiting for NY session. In the meantime, I'm still working on new interface for new upcoming version , do you like it ? {image}
> 
> Ignored

Molto grande !!!! skyline , non si può immaginare quanto aiuto si sta facendo tutta la comunità di FF (ovviamente Udine ...) ![](https://resources.faireconomy.media/images/emojis/64/1f647-200d-2642-fe0f.png?v=15.1)  
  
Grazie per il vostro grande lavoro. ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)  
  
Great, you can not imagine how much help, doing the whole community of FF (of course also Udine)  
  
thanks for your great work. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#255](/thread/post/8194744#post8194744 "Post Permalink")

  * Apr 9, 2015 9:00pm  Apr 9, 2015 9:00pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

Ty all for suggest and help ! ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)  
Yes I was thinking about mono type font but I don't like very much Courier New even if solve space issue.  
Also adding an external parameter Font seems to be not ideal because when font is changed the orizzontal separator lines which are something like ________________ is messed up due to difference between fonts so i have to decide beforehand for a fixed font and one that is always found in a pc (like Arial).  
I have to admit i'm not so good with graphical interface aspect, btw it could be further improved with time ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)  
  
Cheers,  
Skyline 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#256](/thread/post/8195093#post8195093 "Post Permalink")

  * Apr 9, 2015 11:15pm  Apr 9, 2015 11:15pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar360850_1.gif) Clipi](clipi)

  * | Joined Jan 2014  | Status: Trader | [482 Posts](/search?do=process&provider=Member&searchuser=360850)

today open trades:  
  
[EUR/JPY Sell 128.90](http://www.forexfactory.com/clipi#03-list+trade41909857) 02 min ago  
[EUR/USD Sell 1.0740](http://www.forexfactory.com/clipi#03-list+trade41909863) 26 min ago 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#257](/thread/post/8195119#post8195119 "Post Permalink")

  * Apr 9, 2015 11:21pm  Apr 9, 2015 11:21pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar350360_20.gif) AKCodingEye](akcodingeye)

  * Joined Sep 2013 | Status: Such a Silly Game It is | [181 Posts](/search?do=process&provider=Member&searchuser=350360)

> [Quoting skyline](/thread/post/8194574#post8194574 "View Quoted Post")
> 
> Disliked
> 
> Ty guys ! ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1) Mmm i think i have to use a different font since that one (Century Gothic) maybe could not be installed on each pc, so I will use Arial which is standard font : {image}
> 
> Ignored

It's really looks nice. Great job so far skyline ![](https://resources.faireconomy.media/images/emojis/64/1f44f.png?v=15.1). I had some drawdown on forward test with Fxcm account but looks healthy and green now again. Can't see any error or bug at this moment. Just wonder if you can unlock only pairs in next version so we can test more low spread pairs and it will take same time for testing so atleast after a month we can see which pairs are doing well and will have more chances to catch any bug/error if anyone come across. Just a thought![](https://resources.faireconomy.media/images/emojis/64/1f914.png?v=15.1)  
  
-AK- 

Whats get measured get improved

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#258](/thread/post/8195209#post8195209 "Post Permalink")

  * Apr 9, 2015 11:43pm  Apr 9, 2015 11:43pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting Clipi](/thread/post/8195093#post8195093 "View Quoted Post")
> 
> Disliked
> 
> today open trades: [EUR/JPY Sell 128.90](http://www.forexfactory.com/clipi#03-list+trade41909857) 02 min ago [EUR/USD Sell 1.0740](http://www.forexfactory.com/clipi#03-list+trade41909863) 26 min ago
> 
> Ignored

Both trade for me but not triggered so no trades opened today 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#259](/thread/post/8195218#post8195218 "Post Permalink")

  * Apr 9, 2015 11:46pm  Apr 9, 2015 11:46pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar338950_1.gif) cescof](cescof)

  * Joined Jun 2013 | Status: Trader | [1,006 Posts](/search?do=process&provider=Member&searchuser=338950)

> [Quoting skyline](/thread/post/8195209#post8195209 "View Quoted Post")
> 
> Disliked
> 
> {quote} Both trade for me but not triggered so no trades opened today
> 
> Ignored

Why? Triggered for me same broker all closed at tp.  
Regards 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#260](/thread/post/8195242#post8195242 "Post Permalink")

  * Apr 9, 2015 11:54pm  Apr 9, 2015 11:54pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar360850_1.gif) Clipi](clipi)

  * | Joined Jan 2014  | Status: Trader | [482 Posts](/search?do=process&provider=Member&searchuser=360850)

> [Quoting skyline](/thread/post/8195209#post8195209 "View Quoted Post")
> 
> Disliked
> 
> {quote} Both trade for me but not triggered so no trades opened today
> 
> Ignored

As the problem is the broker, I am using [IC MARKETS](/brokers/ic-markets "View IC Markets Broker Profile"), with TP: 10, TS: 3.5 and SL 10 

Attached Image

![](/attachment/image/1650193?d=1428591258)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * UdineEA Official Thread
  *   * [ **Reply to Thread** ](/thread/533099-udineea-official-thread/reply#reply)

  * More

[](https://www.forexfactory.com "Homepage")

  * [Forums](forums)
  * [Trades](trades)
  * [Calendar](calendar)
  * [News](news)
  * [Market](market)
  * [Brokers](brokers)

****

[](https://www.faireconomy.com/)

  * 

[The Official "Ok, now I'm pissed" Thread](/thread/73546-the-official-ok-now-im-pissed-thread "Hello Everyone, 
 
Seeing the apparent lack of threads of this nature \(just kidding, but read on\) I have decided to set up a respectable...") 51 replies

[Historic Charts: NZ Official Cash Rate](/thread/20380-historic-charts-nz-official-cash-rate "Sep 14, 2005") 15 replies

[Is there an official exchange rate?!](/thread/11571-is-there-an-official-exchange-rate "Different brokers have different bid and ask prices for every cross or pair.  However, the bid and ask price is based on something...I am...") 14 replies

[Official forex time zone](/thread/9940-official-forex-time-zone "is there a standard forex time zone? do i follow gmt or NY time? i use 4 hour charts and sometimes the time is way off because of time zone...") 3 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/533099-udineea-official-thread/reply#reply)
  * Subscribe
  * [100](javascript:void\(0\);)

Attachments: UdineEA Official Thread

Tags: UdineEA Official Thread

#  [](/thread/533099-udineea-official-thread)UdineEA Official Thread 

  * 

  * [#261](/thread/post/8195284#post8195284 "Post Permalink")

  * Apr 10, 2015 12:04am  Apr 10, 2015 12:04am 

  * [ Johanl66](johanl66)

  * | Joined Jan 2011  | Status: Trader | [36 Posts](/search?do=process&provider=Member&searchuser=168624)

Well had those trades open and they are winners  
  
EU and EJ both are winners and are Sell trades  
  
I like the Design Skyline  
  
Maybe we have to make an option so people can select from what time the day should start, maybe its nothing, and maybe we have all the criteria are met and then we have the same results...  
But now I see differ results.....we all have to be sure why that is...  
  
Just my 2 cents though 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#262](/thread/post/8195456#post8195456 "Post Permalink")

  * Apr 10, 2015 1:09am  Apr 10, 2015 1:09am 

  * [ Udine](udine)

  * Joined Jul 2008 | Status: Trader | [5,763 Posts](/search?do=process&provider=Member&searchuser=75976)

Doing great Skyline ![](https://resources.faireconomy.media/images/emojis/64/1f44f.png?v=15.1)  
  
Cheers  
  
Udine 

Sleep less, live fast, as it aint gonna last ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#263](/thread/post/8195507#post8195507 "Post Permalink")

  * Apr 10, 2015 1:27am  Apr 10, 2015 1:27am 

  * [ raylin](raylin)

  * | Commercial User  | Joined Nov 2007 | [402 Posts](/search?do=process&provider=Member&searchuser=55123)

Hi Skyliner Looking good on demo  
What broker will you be using when you decide to go live 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#264](/thread/post/8195542#post8195542 "Post Permalink")

  * Apr 10, 2015 1:43am  Apr 10, 2015 1:43am 

  * [ DerBerliner](derberliner)

  * | Joined Feb 2011  | Status: Trader | [822 Posts](/search?do=process&provider=Member&searchuser=168827)

I can confirm "Clipi" ! Have the same two winning trades:  
[http://www.myfxbook.com/members/TGT_...rading/1201341](http://www.myfxbook.com/members/TGT_FX/udine-ea-v114-00level-trading/1201341)  
  
![](https://resources.faireconomy.media/images/emojis/64/1f918.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)  
  
  
At the other side: in the near past I (and perhaps some others here) didn't got the same trades like skyline got ! So: obviously we see now already in demos the sensitivity to brokers ! Depending on the brokers the results will even more differ in the case of life trading ! ![](https://resources.faireconomy.media/images/emojis/64/1f64f.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f62b.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#265](/thread/post/8195577#post8195577 "Post Permalink")

  * Apr 10, 2015 2:02am  Apr 10, 2015 2:02am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting cescof](/thread/post/8195218#post8195218 "View Quoted Post")
> 
> Disliked
> 
> {quote} Why? Triggered for me same broker all closed at tp. Regards
> 
> Ignored

My orders was deleted at the end of M30 candle it's a designed feature and weren't triggered, so no trade for me today ![](https://resources.faireconomy.media/images/emojis/64/1f641.png?v=15.1)  
  
As outlined by DerBerliner this EA (and all EA for what can matter) has very high broker dependancy, I saw also different trades **_on the same broker_** with 2 different demo accounts , so it's not a surprise to have such differences, we cannot overcome this. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#266](/thread/post/8195584#post8195584 "Post Permalink")

  * Apr 10, 2015 2:05am  Apr 10, 2015 2:05am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting Udine](/thread/post/8195456#post8195456 "View Quoted Post")
> 
> Disliked
> 
> Doing great Skyline ![](https://resources.faireconomy.media/images/emojis/64/1f44f.png?v=15.1) Cheers Udine
> 
> Ignored

Thank you Master Udine ! ![](https://resources.faireconomy.media/images/emojis/64/1f917.png?v=15.1)  
Without your generosity sharing your trading system, none of this would have been possible ! ![](https://resources.faireconomy.media/images/emojis/64/1f647-200d-2642-fe0f.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#267](/thread/post/8195814#post8195814 "Post Permalink")

  * Apr 10, 2015 3:29am  Apr 10, 2015 3:29am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar298742_5.gif) bluejack](bluejack)

  * | Joined Oct 2012  | Status: Trader | [493 Posts](/search?do=process&provider=Member&searchuser=298742)

I got 3 trades today.. Broker - [Tickmill](/brokers/tickmill "View Tickmill Broker Profile") (armada markets)   
Skyline, Thank You ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot1.png
Size: 18 KB](/attachment/image/1650365/thumbnail?d=1428604053)](/attachment/image/1650365?d=1428604053)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#268](/thread/post/8195842#post8195842 "Post Permalink")

  * Apr 10, 2015 3:34am  Apr 10, 2015 3:34am 

  * [ DerBerliner](derberliner)

  * | Joined Feb 2011  | Status: Trader | [822 Posts](/search?do=process&provider=Member&searchuser=168827)

> [Quoting bluejack](/thread/post/8195814#post8195814 "View Quoted Post")
> 
> Disliked
> 
> I got 3 trades today.. Broker - Tickmill (armada markets) Skyline, Thank You ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1) {image}
> 
> Ignored

  
Thanks bro for posting these figures ! Yep ... and again: different results, depending on the broker we/you use !!![](https://resources.faireconomy.media/images/emojis/64/1f62c.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#269](/thread/post/8195851#post8195851 "Post Permalink")

  * Apr 10, 2015 3:38am  Apr 10, 2015 3:38am 

  * [ DerBerliner](derberliner)

  * | Joined Feb 2011  | Status: Trader | [822 Posts](/search?do=process&provider=Member&searchuser=168827)

> [Quoting skyline](/thread/post/8195577#post8195577 "View Quoted Post")
> 
> Disliked
> 
> {quote}.... has very high broker dependancy, I saw also different trades on the same broker with 2 different demo accounts , so it's not a surprise to have such differences, __we cannot overcome this__.
> 
> Ignored

Yep that's right, unfortunately. But let's try our best, how we can get _optimal_ gains - whichever broker we use ! In any case the spread is most important + the reputation/reliability/honesty of the coosen broker ![](https://resources.faireconomy.media/images/emojis/64/1f617.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f3b6.png?v=15.1) ![](https://resources.faireconomy.media/images/emojis/64/1f914.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#270](/thread/post/8196055#post8196055 "Post Permalink")

  * Apr 10, 2015 5:13am  Apr 10, 2015 5:13am 

  * [ leancuisine](leancuisine)

  * | Joined Jul 2014  | Status: Trader | [38 Posts](/search?do=process&provider=Member&searchuser=376648)

With ThinkForex I got two trades, seems like one was stopped out by the trailing loss, while the other one ran to TP of 10 pips. ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot1.png
Size: 24 KB](/attachment/image/1650430/thumbnail?d=1428610363)](/attachment/image/1650430?d=1428610363)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#271](/thread/post/8196171#post8196171 "Post Permalink")

  * Apr 10, 2015 6:48am  Apr 10, 2015 6:48am 

  * [ DerBerliner](derberliner)

  * | Joined Feb 2011  | Status: Trader | [822 Posts](/search?do=process&provider=Member&searchuser=168827)

Yep ! Especially _scalper EAs_ extremly depend on the brokers datasheet ! Like Skyline posted above: even using the same broker on different accounts with the same bot you may get different results !  
AND: Take into account: atm we are all on demos ! Imagine what will happen at live accounts !! ![](https://resources.faireconomy.media/images/emojis/64/1f64f.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#272](/thread/post/8196229#post8196229 "Post Permalink")

  * Apr 10, 2015 8:00am  Apr 10, 2015 8:00am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377617_1.gif) merrygold](merrygold)

  * Joined Jul 2014 | Status: Trader | [736 Posts](/search?do=process&provider=Member&searchuser=377617)

Happy to see everything is going well. Keep up the good work, Skyline :-) 

MY SITTING, NEVER MY THINKING!

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#273](/thread/post/8196403#post8196403 "Post Permalink")

  * Apr 10, 2015 11:18am  Apr 10, 2015 11:18am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar185229_8.gif) Erebus](erebus)

  * Joined Jul 2011 | Status: Trader | [8,576 Posts](/search?do=process&provider=Member&searchuser=185229)

You guys like trading EA's and scalping, check out the results on this ARBITRAGE trading EA  
  
![](https://resources.faireconomy.media/images/emojis/64/1f633.png?v=15.1)

Attached Image (click to enlarge)

[![Click to Enlarge

Name: PZ_ARB.png
Size: 350 KB](/attachment/image/1650551/thumbnail?d=1428632273)](/attachment/image/1650551?d=1428632273)   

"Forex a Great Hobby, But Not a Great Job"

[Texas-2-Step](erebus#79 "View Trade Explorer") All Time Return: 8.8%

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#274](/thread/post/8196720#post8196720 "Post Permalink")

  * Apr 10, 2015 4:24pm  Apr 10, 2015 4:24pm 

  * [ DerBerliner](derberliner)

  * | Joined Feb 2011  | Status: Trader | [822 Posts](/search?do=process&provider=Member&searchuser=168827)

As I understand it - this thread is about 00level trading EA ? Right ? .... only about 00level trading EA !  
  
Anyway, so why don't you post anywhere this bot ? Or do you have a link to it ? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#275](/thread/post/8197099#post8197099 "Post Permalink")

  * Apr 10, 2015 6:44pm  Apr 10, 2015 6:44pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar185229_8.gif) Erebus](erebus)

  * Joined Jul 2011 | Status: Trader | [8,576 Posts](/search?do=process&provider=Member&searchuser=185229)

> [Quoting DerBerliner](/thread/post/8196720#post8196720 "View Quoted Post")
> 
> Disliked
> 
> As I understand it - this thread is about 00level trading EA ? Right ? .... **only about 00level trading EA !** Anyway, so why don't you post anywhere this bot ? Or do you have a link to it ?
> 
> Ignored

**Yes, only about the EA**  
  
I hate to say it, but did you read **Post # 1**  
  
If you don't have comprehension for that, you will not be able to trade this EA  
  
Regards, John  
  
<http://www.forexfactory.com/showthread.php?t=533099>

"Forex a Great Hobby, But Not a Great Job"

[Texas-2-Step](erebus#79 "View Trade Explorer") All Time Return: 8.8%

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#276](/thread/post/8197271#post8197271 "Post Permalink")

  * Apr 10, 2015 7:50pm  Apr 10, 2015 7:50pm 

  * [ rmndschmidt](rmndschmidt)

  * | Joined Mar 2014  | Status: Trader | [42 Posts](/search?do=process&provider=Member&searchuser=365689)

> [Quoting Erebus](/thread/post/8197099#post8197099 "View Quoted Post")
> 
> Disliked
> 
> {quote} Yes, only about the EA I hate to say it, but did you read Post # 1 If you don't have comprehension for that, you will not be able to trade this EA Regards, John <http://www.forexfactory.com/showthread.php?t=533099>
> 
> Ignored

I do not understand the relationship between this EA and the 00-level trading? Can you explain this. I have read post 1. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#277](/thread/post/8197298#post8197298 "Post Permalink")

  * Edited 8:28pm  Apr 10, 2015 8:02pm | Edited 8:28pm 

  * [ mhz](mhz)

  * | Joined Mar 2015  | Status: Trader | [9 Posts](/search?do=process&provider=Member&searchuser=405566)

why no open position?  
  
and Error  
2015.04.10 19:20:07.731 2015.03.26 00:00 FFCal-WUKAR EURUSD,M30: Closing URL web connection 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#278](/thread/post/8197427#post8197427 "Post Permalink")

  * Apr 10, 2015 8:58pm  Apr 10, 2015 8:58pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar185229_8.gif) Erebus](erebus)

  * Joined Jul 2011 | Status: Trader | [8,576 Posts](/search?do=process&provider=Member&searchuser=185229)

> [Quoting rmndschmidt](/thread/post/8197271#post8197271 "View Quoted Post")
> 
> Disliked
> 
> {quote} I do not understand the relationship between this EA and the 00-level trading? Can you explain this. I have read post 1.
> 
> Ignored

How that is my problem?  
  
What is it you don't understand?  
  
Udine trades on 00 level - EA trades 00 level 

"Forex a Great Hobby, But Not a Great Job"

[Texas-2-Step](erebus#79 "View Trade Explorer") All Time Return: 8.8%

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#279](/thread/post/8198441#post8198441 "Post Permalink")

  * Apr 11, 2015 4:04am  Apr 11, 2015 4:04am 

  * [ rmndschmidt](rmndschmidt)

  * | Joined Mar 2014  | Status: Trader | [42 Posts](/search?do=process&provider=Member&searchuser=365689)

> [Quoting Erebus](/thread/post/8197427#post8197427 "View Quoted Post")
> 
> Disliked
> 
> {quote} How that is my problem? What is it you don't understand? Udine trades on 00 level - EA trades 00 level
> 
> Ignored

Nevertheless, I do not understand the reason for your message. You write: "This signal is for illustrative purposes only, trades are too fast to be copied Do not subscribe." 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#280](/thread/post/8198502#post8198502 "Post Permalink")

  * Apr 11, 2015 5:15am  Apr 11, 2015 5:15am 

  * [ leancuisine](leancuisine)

  * | Joined Jul 2014  | Status: Trader | [38 Posts](/search?do=process&provider=Member&searchuser=376648)

I have been trading this EA's signals live, you could also check my history on [http://www.myfxbook.com/members/lean...system/1208350](http://www.myfxbook.com/members/leancuisine/leancuisines-golden-system/1208350)  
  
So yes, this EA does work with live trading. However I do have to mention that I have it has only been running for one week, and there is some slippage with from my demo account, which is also at the same broker. The slippage is between 0.2-0.5 pips, not that much. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * UdineEA Official Thread
  *   * [ **Reply to Thread** ](/thread/533099-udineea-official-thread/reply#reply)

  * More

[](https://www.forexfactory.com "Homepage")

  * [Forums](forums)
  * [Trades](trades)
  * [Calendar](calendar)
  * [News](news)
  * [Market](market)
  * [Brokers](brokers)

****

[](https://www.faireconomy.com/)

  * 

[The Official "Ok, now I'm pissed" Thread](/thread/73546-the-official-ok-now-im-pissed-thread "Hello Everyone, 
 
Seeing the apparent lack of threads of this nature \(just kidding, but read on\) I have decided to set up a respectable...") 51 replies

[Historic Charts: NZ Official Cash Rate](/thread/20380-historic-charts-nz-official-cash-rate "Sep 14, 2005") 15 replies

[Is there an official exchange rate?!](/thread/11571-is-there-an-official-exchange-rate "Different brokers have different bid and ask prices for every cross or pair.  However, the bid and ask price is based on something...I am...") 14 replies

[Official forex time zone](/thread/9940-official-forex-time-zone "is there a standard forex time zone? do i follow gmt or NY time? i use 4 hour charts and sometimes the time is way off because of time zone...") 3 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/533099-udineea-official-thread/reply#reply)
  * Subscribe
  * [100](javascript:void\(0\);)

Attachments: UdineEA Official Thread

Tags: UdineEA Official Thread

#  [](/thread/533099-udineea-official-thread)UdineEA Official Thread 

  * 

  * [#281](/thread/post/8198965#post8198965 "Post Permalink")

  * Apr 11, 2015 9:38pm  Apr 11, 2015 9:38pm 

  * [ leebsurag](leebsurag)

  * | Membership Revoked  | Joined Oct 2013 | [877 Posts](/search?do=process&provider=Member&searchuser=353350)

Anybody have live trading results with this EA? Their posting (especially profit stats![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)) would be much appreciated.. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#282](/thread/post/8199194#post8199194 "Post Permalink")

  * Apr 12, 2015 2:49am  Apr 12, 2015 2:49am 

  * [ saek1985](saek1985)

  * | Joined Apr 2015  | Status: Trader | [4 Posts](/search?do=process&provider=Member&searchuser=407757)

Hello everyone. ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
(Sorry for my English)  
From Monday I will also test the EA.  
Regards. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#283](/thread/post/8200205#post8200205 "Post Permalink")

  * Apr 13, 2015 6:11am  Apr 13, 2015 6:11am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

**New v1.1.5 released in 1st post !**  
  
I've only reorganized the UI to better show all details at once, please test it and report back errors.  
Now it should be clear when EA place a pending order (all green check marks, if there is at least 1 red cross order is not placed).  
(note : if you click on 'FF thread link' it should open this thread ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)  
  

Attached Image

![](/attachment/image/1651792?d=1428872941)

  
  
Cheers,  
Skyline 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#284](/thread/post/8200870#post8200870 "Post Permalink")

  * Apr 13, 2015 4:15pm  Apr 13, 2015 4:15pm 

  * [ Bhutugly](bhutugly)

  * | Joined Oct 2011  | Status: Trader | [12 Posts](/search?do=process&provider=Member&searchuser=200586)

Okay,  
  
Downloaded New EA, went upstairs for a shower, come back down +10 pips,  
very nice. Just 1 pip off hitting target for the day, where can i change this so i can continue testing it today?  
  
  
Just need to check everything triggered correctly.  
  
  
Cheers  
  
Ian 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#285](/thread/post/8200895#post8200895 "Post Permalink")

  * Apr 13, 2015 4:24pm  Apr 13, 2015 4:24pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting Bhutugly](/thread/post/8200870#post8200870 "View Quoted Post")
> 
> Disliked
> 
> Okay, Downloaded New EA, went upstairs for a shower, come back down +10 pips, very nice. Just 1 pip off hitting target for the day, where can i change this so i can continue testing it today? Just need to check everything triggered correctly. Cheers Ian
> 
> Ignored

Hi Ian,  
for me EU to TP and EJ to TS so only +5 pips but still a good start ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)  
Daily Target is based on percentage of your equity not on pips, you can change it by raising DailyTargetPercentage variable.  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot1.png
Size: 5 KB](/attachment/image/1652075/thumbnail?d=1428909839)](/attachment/image/1652075?d=1428909839)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#286](/thread/post/8201467#post8201467 "Post Permalink")

  * Apr 13, 2015 8:15pm  Apr 13, 2015 8:15pm 

  * [ Johanl66](johanl66)

  * | Joined Jan 2011  | Status: Trader | [36 Posts](/search?do=process&provider=Member&searchuser=168624)

I have 3 Winners and 1 loss  
  
E/U, E/J and G/J BUY orders where Winners  
E/U SELL was a loss  
  
a good day start 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#287](/thread/post/8201530#post8201530 "Post Permalink")

  * Apr 13, 2015 8:41pm  Apr 13, 2015 8:41pm 

  * [ Luy](luy)

  * | Joined Jan 2015  | Status: Trader | [7 Posts](/search?do=process&provider=Member&searchuser=396096)

Hello skyline!  
  
From today Im testing the EA. Thank you very much for sharing!  
  
Greetings, Luy 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#288](/thread/post/8201549#post8201549 "Post Permalink")

  * Apr 13, 2015 8:51pm  Apr 13, 2015 8:51pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar283013_1.gif) Juan007](juan007)

  * | Joined Aug 2012  | Status: Trader | [1,275 Posts](/search?do=process&provider=Member&searchuser=283013)

thanks i start test the EA 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#289](/thread/post/8201856#post8201856 "Post Permalink")

  * Apr 13, 2015 10:29pm  Apr 13, 2015 10:29pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar364825_3.gif) eak154](eak154)

  * | Joined Feb 2014  | Status: Patience is the key. | [58 Posts](/search?do=process&provider=Member&searchuser=364825)

GJ TP 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: GBPJPYeM30.png
Size: 18 KB](/attachment/image/1652410/thumbnail?d=1428931727)](/attachment/image/1652410?d=1428931727)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#290](/thread/post/8202207#post8202207 "Post Permalink")

  * Apr 14, 2015 12:57am  Apr 14, 2015 12:57am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar352224_1.gif) dafa](dafa)

  * | Joined Oct 2013  | Status: Trader | [320 Posts](/search?do=process&provider=Member&searchuser=352224)

hi skyline. is it possible to open Ea for live yet? i would like to test it on cent account rather than demo. thanks 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#291](/thread/post/8202252#post8202252 "Post Permalink")

  * Apr 14, 2015 1:26am  Apr 14, 2015 1:26am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar360850_1.gif) Clipi](clipi)

  * | Joined Jan 2014  | Status: Trader | [482 Posts](/search?do=process&provider=Member&searchuser=360850)

I think something does not work well, I'm trying to TP = 10 and TS = 3.5.  
If you look at today's operations, EJ open 127.7, the price has reached 127.82, should they have closed trade at 127.8 and closed in BE.  
GJ same, the operation buy at 176.30 seems to have reached a minimum at 176.35, which TrailingStop seems to have failed.  
very thanks! 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: GBPJPYM30.png
Size: 52 KB](/attachment/image/1652524/thumbnail?d=1428941811)](/attachment/image/1652524?d=1428941811)   
[![Click to Enlarge

Name: EURJPYM30.png
Size: 53 KB](/attachment/image/1652525/thumbnail?d=1428941839)](/attachment/image/1652525?d=1428941839)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#292](/thread/post/8202261#post8202261 "Post Permalink")

  * Apr 14, 2015 1:32am  Apr 14, 2015 1:32am 

  * [ Kazuma](kazuma)

  * | Joined Jun 2013  | Status: Trader | [3 Posts](/search?do=process&provider=Member&searchuser=339194)

mille grazie Skyline! ![](https://resources.faireconomy.media/images/emojis/64/1f917.png?v=15.1)  
Cant wait for the live version 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#293](/thread/post/8202364#post8202364 "Post Permalink")

  * Apr 14, 2015 2:07am  Apr 14, 2015 2:07am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting dafa](/thread/post/8202207#post8202207 "View Quoted Post")
> 
> Disliked
> 
> hi skyline. is it possible to open Ea for live yet? i would like to test it on cent account rather than demo. thanks
> 
> Ignored

Hi Dafa,  
if there will be no major bug during this week, I will release open live trade on next monday ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)  
  
Cheers,  
Skyline 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#294](/thread/post/8202401#post8202401 "Post Permalink")

  * Apr 14, 2015 2:20am  Apr 14, 2015 2:20am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting Clipi](/thread/post/8202252#post8202252 "View Quoted Post")
> 
> Disliked
> 
> I think something does not work well, I'm trying to TP = 10 and TS = 3.5. If you look at today's operations, EJ open 127.7, the price has reached 127.82, should they have closed trade at 127.8 and closed in BE. GJ same, the operation buy at 176.30 seems to have reached a minimum at 176.35, which TrailingStop seems to have failed. very thanks! {image} {image}
> 
> Ignored

Hi Clipi,  
ts in my account is working (and also in other users account as far as i can see), keep in mind that trailingstop done with low value 3.5 pips is very sensible to broker spread, latency, requotes and so on, so it's not a very precise function and sometime does not work as intendeed (this is the same as if you use ts built in mt4 or other ts ea like wukar).  
  
Cheers,  
Skyline 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#295](/thread/post/8202424#post8202424 "Post Permalink")

  * Apr 14, 2015 2:29am  Apr 14, 2015 2:29am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar352224_1.gif) dafa](dafa)

  * | Joined Oct 2013  | Status: Trader | [320 Posts](/search?do=process&provider=Member&searchuser=352224)

> [Quoting skyline](/thread/post/8202364#post8202364 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi Dafa, if there will be no major bug during this week, I will release open live trade on next monday ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1) Cheers, Skyline
> 
> Ignored

Great.;-) 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#296](/thread/post/8202512#post8202512 "Post Permalink")

  * Apr 14, 2015 3:11am  Apr 14, 2015 3:11am 

  * [ Luy](luy)

  * | Joined Jan 2015  | Status: Trader | [7 Posts](/search?do=process&provider=Member&searchuser=396096)

> [Quoting skyline](/thread/post/8202364#post8202364 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi Dafa, if there will be no major bug during this week, I will release open live trade on next monday ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1) Cheers, Skyline
> 
> Ignored

Hi skyline!  
  
Looking forward to go live next week with a small account. Are you planing in the future to add .05 level entrys also?  
  
Thanks again,  
Luy 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#297](/thread/post/8202788#post8202788 "Post Permalink")

  * Apr 14, 2015 6:54am  Apr 14, 2015 6:54am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar283013_1.gif) Juan007](juan007)

  * | Joined Aug 2012  | Status: Trader | [1,275 Posts](/search?do=process&provider=Member&searchuser=283013)

Skyline  
  
its possible have a settings  
  
time start  
time end  
  
for example we can run on NY time only 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#298](/thread/post/8203316#post8203316 "Post Permalink")

  * Apr 14, 2015 3:35pm  Apr 14, 2015 3:35pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

@ Luy : Actually i'm not planning to modify core entry logic adding .50 level to not over complicated EA which is now more than 1100 lines code ![](https://resources.faireconomy.media/images/emojis/64/1f633.png?v=15.1)  
  
@ Juan007 : Maybe in future I could add different switch to let user choose different times to trade, for now you can set TradeOnlyLondon= false so that EA will be enabled to trade full time (I suggest to set this as per default to true which is best period to trade)  
  
Cheers,  
Skyline 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#299](/thread/post/8204441#post8204441 "Post Permalink")

  * Apr 14, 2015 11:03pm  Apr 14, 2015 11:03pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1024_7.gif) diallist](diallist)

  * Joined Sep 2004 | Status: Trader | [1,464 Posts](/search?do=process&provider=Member&searchuser=1024)

> [Quoting skyline](/thread/post/8202364#post8202364 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi Dafa, if there will be no major bug during this week, I will release open live trade on next monday ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1) Cheers, Skyline
> 
> Ignored

Hi skyline,  
  
I haven't had time, due to other projects, to try your EA yet. But, I did want to make this post to tell you that I admire your preventing the EA from being used on Live until it is fully tested. Your concern for other traders' best interest is evident in this decision, and I applaud you for it!  
You are a wise and good person! ![](https://resources.faireconomy.media/images/emojis/64/1f44f.png?v=15.1)  
  
Dial 

sxaxlxvxaxtxixoxnxbxyxgxrxaxcxexdxoxtxoxrxgx

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#300](/thread/post/8204533#post8204533 "Post Permalink")

  * Apr 14, 2015 11:37pm  Apr 14, 2015 11:37pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting diallist](/thread/post/8204441#post8204441 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi skyline, I haven't had time, due to other projects, to try your EA yet. But, I did want to make this post to tell you that I admire your preventing the EA from being used on Live until it is fully tested. Your concern for other traders' best interest is evident in this decision, and I applaud you for it! You are a wise and good person! ![](https://resources.faireconomy.media/images/emojis/64/1f44f.png?v=15.1) Dial
> 
> Ignored

Ty Diallist for your kind word , very appreciated! ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)  
I'm also thinking to lock max risk allowed to not more than 2% per each pair so to avoid overleverage the account that could lead to big losses and I don't want this to happen to me and other users using this EA.  
  
Cheers,  
Skyline 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * UdineEA Official Thread
  *   * [ **Reply to Thread** ](/thread/533099-udineea-official-thread/reply#reply)

  * More

[](https://www.forexfactory.com "Homepage")

  * [Forums](forums)
  * [Trades](trades)
  * [Calendar](calendar)
  * [News](news)
  * [Market](market)
  * [Brokers](brokers)

****

[](https://www.faireconomy.com/)

  * 

[The Official "Ok, now I'm pissed" Thread](/thread/73546-the-official-ok-now-im-pissed-thread "Hello Everyone, 
 
Seeing the apparent lack of threads of this nature \(just kidding, but read on\) I have decided to set up a respectable...") 51 replies

[Historic Charts: NZ Official Cash Rate](/thread/20380-historic-charts-nz-official-cash-rate "Sep 14, 2005") 15 replies

[Is there an official exchange rate?!](/thread/11571-is-there-an-official-exchange-rate "Different brokers have different bid and ask prices for every cross or pair.  However, the bid and ask price is based on something...I am...") 14 replies

[Official forex time zone](/thread/9940-official-forex-time-zone "is there a standard forex time zone? do i follow gmt or NY time? i use 4 hour charts and sometimes the time is way off because of time zone...") 3 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/533099-udineea-official-thread/reply#reply)
  * Subscribe
  * [100](javascript:void\(0\);)

Attachments: UdineEA Official Thread

Tags: UdineEA Official Thread

#  [](/thread/533099-udineea-official-thread)UdineEA Official Thread 

  * 

  * [#301](/thread/post/8204613#post8204613 "Post Permalink")

  * Apr 15, 2015 12:03am  Apr 15, 2015 12:03am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1024_7.gif) diallist](diallist)

  * Joined Sep 2004 | Status: Trader | [1,464 Posts](/search?do=process&provider=Member&searchuser=1024)

> [Quoting skyline](/thread/post/8204533#post8204533 "View Quoted Post")
> 
> Disliked
> 
> {quote} Ty Diallist for your kind word , very appreciated! ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1) I'm also thinking to lock max risk allowed to not more than 2% per each pair so to avoid overleverage the account that could lead to big losses and I don't want this to happen to me and other users using this EA. Cheers, Skyline
> 
> Ignored

I think that is a good idea too, skyline. 

sxaxlxvxaxtxixoxnxbxyxgxrxaxcxexdxoxtxoxrxgx

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#302](/thread/post/8204912#post8204912 "Post Permalink")

  * Apr 15, 2015 2:00am  Apr 15, 2015 2:00am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1024_7.gif) diallist](diallist)

  * Joined Sep 2004 | Status: Trader | [1,464 Posts](/search?do=process&provider=Member&searchuser=1024)

> [Quoting diallist](/thread/post/8204613#post8204613 "View Quoted Post")
> 
> Disliked
> 
> {quote} I think that is a good idea too, skyline.
> 
> Ignored

Actually, skyline, on further consideration, I will sometimes limit myself to a single, strongest, pair during a trading session, and use 4% risk per trade.  
  
So, I would suggest that your live version default to 2%, but be adjustable up to 4%.  
  
To everyone reading this: If skyline chooses to adopt my suggestion above, it is up to each of you to manage their risk responsibly.  
  
Dial 

sxaxlxvxaxtxixoxnxbxyxgxrxaxcxexdxoxtxoxrxgx

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#303](/thread/post/8204956#post8204956 "Post Permalink")

  * Apr 15, 2015 2:27am  Apr 15, 2015 2:27am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting diallist](/thread/post/8204912#post8204912 "View Quoted Post")
> 
> Disliked
> 
> {quote} Actually, skyline, on further consideration, I will sometimes limit myself to a single, strongest, pair during a trading session, and use 4% risk per trade. So, I would suggest that your live version default to 2%, but be adjustable up to 4%. To everyone reading this: If skyline chooses to adopt my suggestion above, it is up to each of you to manage their risk responsibly. Dial
> 
> Ignored

Hi Diallist,  
thank you for your input.  
The problem I see is that raising risk to 4% per each pair means a potential overall risk of 16% if EA is used on all pairs allowed (EU,EJ,GU,GJ).  
So to avoid this EA to be turned into a fast burning account robot, I would prefer to set max risk per trade to 2% which still means a quite high overall 8% risk if used in all 4 pairs.  
  
Cheers,  
Skyline 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#304](/thread/post/8205314#post8205314 "Post Permalink")

  * Apr 15, 2015 7:18am  Apr 15, 2015 7:18am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1024_7.gif) diallist](diallist)

  * Joined Sep 2004 | Status: Trader | [1,464 Posts](/search?do=process&provider=Member&searchuser=1024)

> [Quoting skyline](/thread/post/8204956#post8204956 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi Diallist, thank you for your input. The problem I see is that raising risk to 4% per each pair means a potential overall risk of 16% if EA is used on all pairs allowed (EU,EJ,GU,GJ). So to avoid this EA to be turned into a fast burning account robot, I would prefer to set max risk per trade to 2% which still means a quite high overall 8% risk if used in all 4 pairs. Cheers, Skyline
> 
> Ignored

Agreed!  
  
If I ever truly need a custom version, I'll hire you for the purpose.  
  
Thanks skyline. I've got the EA installed and running. I'll keep you apprised of any bugs.  
  
Thanks again for all your hard work on this (1100 lines of code! Whew!)  
  
Dial 

sxaxlxvxaxtxixoxnxbxyxgxrxaxcxexdxoxtxoxrxgx

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#305](/thread/post/8205339#post8205339 "Post Permalink")

  * Apr 15, 2015 7:38am  Apr 15, 2015 7:38am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting diallist](/thread/post/8205314#post8205314 "View Quoted Post")
> 
> Disliked
> 
> {quote} Agreed! If I ever truly need a custom version, I'll hire you for the purpose. Thanks skyline. I've got the EA installed and running. I'll keep you apprised of any bugs. Thanks again for all your hard work on this (1100 lines of code! Whew!) Dial
> 
> Ignored

Ty Dial ! ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#306](/thread/post/8205501#post8205501 "Post Permalink")

  * Apr 15, 2015 10:16am  Apr 15, 2015 10:16am 

  * [ brucech](brucech)

  * | Joined Sep 2006  | Status: Trader | [594 Posts](/search?do=process&provider=Member&searchuser=18716)

> [Quoting skyline](/thread/post/8204956#post8204956 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi Diallist, thank you for your input. The problem I see is that raising risk to 4% per each pair means a potential overall risk of 16% if EA is used on all pairs allowed (EU,EJ,GU,GJ). So to avoid this EA to be turned into a fast burning account robot, I would prefer to set max risk per trade to 2% which still means a quite high overall 8% risk if used in all 4 pairs. Cheers, Skyline
> 
> Ignored

Skyline,  
  
Great work on the EA! I agree with the 2%. Steady and consistent! The account will grow! Thanks for the time you have put into this EA and your willingness to share it here with others. Looking forward to putting this on a live account next week, too.  
  
Bruce 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#307](/thread/post/8205505#post8205505 "Post Permalink")

  * Apr 15, 2015 10:17am  Apr 15, 2015 10:17am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1024_7.gif) diallist](diallist)

  * Joined Sep 2004 | Status: Trader | [1,464 Posts](/search?do=process&provider=Member&searchuser=1024)

@skyline  
  
A bug, methinks...  
  
For both long and short conditions the condition "ADR room down" is the same.  
I would expect it to toggle to "ADR room up" for long conditions. 

sxaxlxvxaxtxixoxnxbxyxgxrxaxcxexdxoxtxoxrxgx

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#308](/thread/post/8205516#post8205516 "Post Permalink")

  * Apr 15, 2015 10:25am  Apr 15, 2015 10:25am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar364825_3.gif) eak154](eak154)

  * | Joined Feb 2014  | Status: Patience is the key. | [58 Posts](/search?do=process&provider=Member&searchuser=364825)

Hi Skyline, I have been testing this EA for a while. I can confirm that it is working in order so far. Every trade has met all entry& exit rules. I have not seen any major bugs yet.  
  
Thank you again for your great EA. I appreciate your time and effort. Keep up your excellent work ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#309](/thread/post/8205661#post8205661 "Post Permalink")

  * Edited 1:02pm  Apr 15, 2015 11:55am | Edited 1:02pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1024_7.gif) diallist](diallist)

  * Joined Sep 2004 | Status: Trader | [1,464 Posts](/search?do=process&provider=Member&searchuser=1024)

Hi skyline,  
  
Not a bug but a concern. I noticed that when a pending order is placed, there is no SL or TP value. Does this mean we are dependent on the EA to apply them at the appropriate price? I'm am not a fan of "hidden" SL or TP. If my platform goes down right after the trade is triggered, and the market makes a monster move, then our accounts are screwed.  
  
Could we have the option to send the SL and TP to the broker, rather than have it hidden?  
  
Thanks  
  
Dial  
  
EDIT: Never mind. I just saw a pending order trigger and the TP and SL appeared. Thanks. 

sxaxlxvxaxtxixoxnxbxyxgxrxaxcxexdxoxtxoxrxgx

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#310](/thread/post/8205897#post8205897 "Post Permalink")

  * Apr 15, 2015 3:17pm  Apr 15, 2015 3:17pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting diallist](/thread/post/8205505#post8205505 "View Quoted Post")
> 
> Disliked
> 
> @skyline A bug, methinks... For both long and short conditions the condition "ADR room down" is the same. I would expect it to toggle to "ADR room up" for long conditions.
> 
> Ignored

Hi Dial,  
good catch ! ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)  
I checked code, it's only an error in gui label which I'll fix in next release, btw the logic is still correct so EA even if it's showing ADR room down for long is checking for adr room up condition.  
  
Thank you for reporting !  
  
Cheers,  
Giacomo 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#311](/thread/post/8205915#post8205915 "Post Permalink")

  * Apr 15, 2015 3:27pm  Apr 15, 2015 3:27pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting diallist](/thread/post/8205661#post8205661 "View Quoted Post")
> 
> Disliked
> 
> Hi skyline, Not a bug but a concern. I noticed that when a pending order is placed, there is no SL or TP value. Does this mean we are dependent on the EA to apply them at the appropriate price? I'm am not a fan of "hidden" SL or TP. If my platform goes down right after the trade is triggered, and the market makes a monster move, then our accounts are screwed. Could we have the option to send the SL and TP to the broker, rather than have it hidden? Thanks Dial EDIT: Never mind. I just saw a pending order trigger and the TP and SL appeared. Thanks....
> 
> Ignored

Hi Dial,  
yes I'm not a fan of hidden sl and tp too for the same reason, but I had to implement pending order in this way (placing them without any sl and tp) because some mt4 brokers don't allow to set SL/TP beforehand so I prefer to set them by code after pending order is triggered.  
Doing so there's still the remote chance that a pending order is triggered (turning into a market order) and connection to server is lost before EA could set SL and TP , so it's safe to check platform from time to time (this isn't a set-and-forget EA).  
  
Cheers,  
Skyline 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#312](/thread/post/8206226#post8206226 "Post Permalink")

  * Apr 15, 2015 6:00pm  Apr 15, 2015 6:00pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1024_7.gif) diallist](diallist)

  * Joined Sep 2004 | Status: Trader | [1,464 Posts](/search?do=process&provider=Member&searchuser=1024)

Thanks skyline! 

sxaxlxvxaxtxixoxnxbxyxgxrxaxcxexdxoxtxoxrxgx

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#313](/thread/post/8206674#post8206674 "Post Permalink")

  * Apr 15, 2015 9:17pm  Apr 15, 2015 9:17pm 

  * [ leancuisine](leancuisine)

  * | Joined Jul 2014  | Status: Trader | [38 Posts](/search?do=process&provider=Member&searchuser=376648)

Did anyone else get a sell GBPUSD trade today? It seems like skyline's didn't get that one. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#314](/thread/post/8207491#post8207491 "Post Permalink")

  * Apr 16, 2015 1:03am  Apr 16, 2015 1:03am 

  * [ saek1985](saek1985)

  * | Joined Apr 2015  | Status: Trader | [4 Posts](/search?do=process&provider=Member&searchuser=407757)

Hello.  
Daily % achieved. There is no losing positions. EA shows max losses per day reached.  
Regards.  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Udine EA.png
Size: 56 KB](/attachment/image/1654227/thumbnail?d=1429113729)](/attachment/image/1654227?d=1429113729)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#315](/thread/post/8207552#post8207552 "Post Permalink")

  * Apr 16, 2015 1:33am  Apr 16, 2015 1:33am 

  * [ Kazuma](kazuma)

  * | Joined Jun 2013  | Status: Trader | [3 Posts](/search?do=process&provider=Member&searchuser=339194)

sell stop, but was deleted. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#316](/thread/post/8207791#post8207791 "Post Permalink")

  * Apr 16, 2015 3:07am  Apr 16, 2015 3:07am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar261568_2.gif) senanata](senanata)

  * | Joined Jun 2012  | Status: Trader | [267 Posts](/search?do=process&provider=Member&searchuser=261568)

Hi Skyline  
Thanks very much for your effort for this EA. I've just downloaded your EA and will test it on my demo account. Hoping the best result for this EA. Once again, I'm very appreciate for your hard work.  
  
  
Cheers,  
Senanata 

MAKE SURE you still can TRADE tomorrow

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#317](/thread/post/8208037#post8208037 "Post Permalink")

  * Apr 16, 2015 6:06am  Apr 16, 2015 6:06am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting saek1985](/thread/post/8207491#post8207491 "View Quoted Post")
> 
> Disliked
> 
> Hello. Daily % achieved. There is no losing positions. EA shows max losses per day reached. Regards. {image}
> 
> Ignored

Hi Saek, thank you for reporting !  
Will check into this bug and fix asap  
  
Cheers,  
Skyline 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#318](/thread/post/8208359#post8208359 "Post Permalink")

  * Apr 16, 2015 10:34am  Apr 16, 2015 10:34am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar261568_2.gif) senanata](senanata)

  * | Joined Jun 2012  | Status: Trader | [267 Posts](/search?do=process&provider=Member&searchuser=261568)

Hi Skyline  
  
This is my first report about UdineEA. I was successful when load the EA and template to the chart. Worked normally on GU, EU and GJ. But I can not attach template to EJ's chart. Everytime I try to do that, my mt4 always crash/hang and not responding as shown on my attachment. Can you tell me what I miss?  
  
Regards,  
Senanata 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: UdineEA EJ.jpg
Size: 151 KB](/attachment/image/1654532/thumbnail?d=1429147782)](/attachment/image/1654532?d=1429147782)   
[![Click to Enlarge

Name: UdineEA GU.jpg
Size: 201 KB](/attachment/image/1654533/thumbnail?d=1429147821)](/attachment/image/1654533?d=1429147821)   

MAKE SURE you still can TRADE tomorrow

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#319](/thread/post/8208509#post8208509 "Post Permalink")

  * Apr 16, 2015 12:21pm  Apr 16, 2015 12:21pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar393445_1.gif) Vlad13685](vlad13685)

  * Joined Dec 2014 | Status: Professional Demo Trader | [536 Posts](/search?do=process&provider=Member&searchuser=393445)

> [Quoting senanata](/thread/post/8208359#post8208359 "View Quoted Post")
> 
> Disliked
> 
> Hi Skyline This is my first report about UdineEA. I was successful when load the EA and template to the chart. Worked normally on GU, EU and GJ. But I can not attach template to EJ's chart. Everytime I try to do that, my mt4 always crash/hang and not responding as shown on my attachment. Can you tell me what I miss? Regards, Senanata {image} {image}
> 
> Ignored

Hi senanata,  
  
first put the Chart on D1 timeframe, then load the template and drop it back down to M30. Sometimes the indicators struggle to load on the lower timeframes.  
  
Regards  
  
Vlad 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#320](/thread/post/8208851#post8208851 "Post Permalink")

  * Apr 16, 2015 4:32pm  Apr 16, 2015 4:32pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting saek1985](/thread/post/8207491#post8207491 "View Quoted Post")
> 
> Disliked
> 
> Hello. Daily % achieved. There is no losing positions. EA shows max losses per day reached. Regards. {image}
> 
> Ignored

Hi Saek,  
i checked for your issue , the calc routine seems to be correct, the only thing that could cause wrong counts is if you have orders in the same account opened (manually or by other EAs) which are taken into account in win/be/losses calculations. If this is the case then just be carefull to use this EA only on account where no other trading systems are used.  
  
Cheers,  
Skyline 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * UdineEA Official Thread
  *   * [ **Reply to Thread** ](/thread/533099-udineea-official-thread/reply#reply)

  * More

[](https://www.forexfactory.com "Homepage")

  * [Forums](forums)
  * [Trades](trades)
  * [Calendar](calendar)
  * [News](news)
  * [Market](market)
  * [Brokers](brokers)

****

[](https://www.faireconomy.com/)

  * 

[The Official "Ok, now I'm pissed" Thread](/thread/73546-the-official-ok-now-im-pissed-thread "Hello Everyone, 
 
Seeing the apparent lack of threads of this nature \(just kidding, but read on\) I have decided to set up a respectable...") 51 replies

[Historic Charts: NZ Official Cash Rate](/thread/20380-historic-charts-nz-official-cash-rate "Sep 14, 2005") 15 replies

[Is there an official exchange rate?!](/thread/11571-is-there-an-official-exchange-rate "Different brokers have different bid and ask prices for every cross or pair.  However, the bid and ask price is based on something...I am...") 14 replies

[Official forex time zone](/thread/9940-official-forex-time-zone "is there a standard forex time zone? do i follow gmt or NY time? i use 4 hour charts and sometimes the time is way off because of time zone...") 3 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/533099-udineea-official-thread/reply#reply)
  * Subscribe
  * [100](javascript:void\(0\);)

Attachments: UdineEA Official Thread

Tags: UdineEA Official Thread

#  [](/thread/533099-udineea-official-thread)UdineEA Official Thread 

  * 

  * [#321](/thread/post/8208930#post8208930 "Post Permalink")

  * Apr 16, 2015 4:57pm  Apr 16, 2015 4:57pm 

  * [ Godwin Igili](godwin*igili)

  * Joined May 2011 | Status: Trader | [541 Posts](/search?do=process&provider=Member&searchuser=179642)

Skyline ,  
Have you considered including the Currency Strength Meter indicator for further filter  
as been done manually in Udine thread?  
Kindly look at Robinho and Cycle most recent posts 

Attached File(s)

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [Currency Strength - Giraia.mq4](/attachment/file/1654744?d=1429170828) 18 KB | 282 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#322](/thread/post/8208990#post8208990 "Post Permalink")

  * Apr 16, 2015 5:19pm  Apr 16, 2015 5:19pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting Godwin Igili](/thread/post/8208930#post8208930 "View Quoted Post")
> 
> Disliked
> 
> Skyline , Have you considered including the Currency Strength Meter indicator for further filter as been done manually in Udine thread? Kindly look at Robinho and Cycle most recent posts {file}
> 
> Ignored

Hi Godwin,  
  
Short Answer : No  
  
Long Answer : I'd like to keep this EA very simple in it's logic without adding filter over filter, following basic Udine level 1 rules otherwise we can go further in an endless loop and I have no time nor will to follow this path ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
  
Cheers,  
Skyline 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#323](/thread/post/8209044#post8209044 "Post Permalink")

  * Apr 16, 2015 5:41pm  Apr 16, 2015 5:41pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar261568_2.gif) senanata](senanata)

  * | Joined Jun 2012  | Status: Trader | [267 Posts](/search?do=process&provider=Member&searchuser=261568)

> [Quoting Vlad13685](/thread/post/8208509#post8208509 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi senanata, first put the Chart on D1 timeframe, then load the template and drop it back down to M30. Sometimes the indicators struggle to load on the lower timeframes. Regards Vlad
> 
> Ignored

Abrakadabra..!! It works, Vlad. Thank you so much. You're very genius..  
  
And here my result today. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Udine Result1.jpg
Size: 235 KB](/attachment/image/1654790/thumbnail?d=1429173661)](/attachment/image/1654790?d=1429173661)   

MAKE SURE you still can TRADE tomorrow

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#324](/thread/post/8209223#post8209223 "Post Permalink")

  * Apr 16, 2015 6:54pm  Apr 16, 2015 6:54pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar185229_8.gif) Erebus](erebus)

  * Joined Jul 2011 | Status: Trader | [8,576 Posts](/search?do=process&provider=Member&searchuser=185229)

> [Quoting skyline](/thread/post/8200205#post8200205 "View Quoted Post")
> 
> Disliked
> 
> New v1.1.5 released in 1st post ! I've only reorganized the UI to better show all details at once, please test it and report back errors. Now it should be clear when EA place a pending order (all green check marks, if there is at least 1 red cross order is not placed). (note : if you click on 'FF thread link' it should open this thread ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1) Cheers, Skyline
> 
> Ignored

Since this new version no one has reported any problems running the EA ??  
  
I have all the indicators in right folder, template apply OK, 30 minutes chart looks same as posted here but when I put the EA on, it gives error message  
  
Only for Demo accounts - it is demo account, what could be the problem? See the picture  
  
Thanks, John 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: 16-04-2015 7-47-56 PM.png
Size: 209 KB](/attachment/image/1654846/thumbnail?d=1429178066)](/attachment/image/1654846?d=1429178066)   

"Forex a Great Hobby, But Not a Great Job"

[Texas-2-Step](erebus#79 "View Trade Explorer") All Time Return: 8.8%

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#325](/thread/post/8209233#post8209233 "Post Permalink")

  * Apr 16, 2015 6:59pm  Apr 16, 2015 6:59pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar389954_3.gif) honestknave](honestknave)

  * Joined Nov 2014 | Status: Trader | [1,300 Posts](/search?do=process&provider=Member&searchuser=389954)

> [Quoting Erebus](/thread/post/8209223#post8209223 "View Quoted Post")
> 
> Disliked
> 
> {quote} Since this new version no one has reported any problems running the EA ?? I have all the indicators in right folder, template apply OK, 30 minutes chart looks same as posted here but when I put the EA on, it gives error message Only for Demo accounts - it is demo account, what could be the problem? See the picture Thanks, John {image}
> 
> Ignored

2 possibilities:  
1\. Some brokers have their servers incorrectly configured (so they flag demo for live, and live for demo)  
2\. Depending on how the demo check is coded, it could be that the terminal is not connected yet. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#326](/thread/post/8209234#post8209234 "Post Permalink")

  * Apr 16, 2015 6:59pm  Apr 16, 2015 6:59pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting Erebus](/thread/post/8209223#post8209223 "View Quoted Post")
> 
> Disliked
> 
> {quote} Since this new version no one has reported any problems running the EA ?? I have all the indicators in right folder, template apply OK, 30 minutes chart looks same as posted here but when I put the EA on, it gives error message Only for Demo accounts - it is demo account, what could be the problem? See the picture Thanks, John {image}
> 
> Ignored

Hi Erebus,  
that's very strange, to check demo account I'm using the very basic instruction IsDemo() provided by mql language which returns true if EA is running on a demo account, false otherwise, so there should be some wrong settings on broker server side related to your account which is set as real account even if it's not.  
I have no other explanation about this sorry ![](https://resources.faireconomy.media/images/emojis/64/1f641.png?v=15.1)  
  
Cheers,  
Skyline 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#327](/thread/post/8209254#post8209254 "Post Permalink")

  * Apr 16, 2015 7:05pm  Apr 16, 2015 7:05pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar389954_3.gif) honestknave](honestknave)

  * Joined Nov 2014 | Status: Trader | [1,300 Posts](/search?do=process&provider=Member&searchuser=389954)

> [Quoting honestknave](/thread/post/8209233#post8209233 "View Quoted Post")
> 
> Disliked
> 
> {quote} 2 possibilities: 1. Some brokers have their servers incorrectly configured (so they flag demo for live, and live for demo) 2. Depending on how the demo check is coded, it could be that the terminal is not connected yet.
> 
> Ignored

Try dropping this script onto a chart and see what the pop-up alert says: 

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [ServerCheck.ex4](/attachment/file/1654860?d=1429178741) 4 KB | 251 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#328](/thread/post/8209265#post8209265 "Post Permalink")

  * Apr 16, 2015 7:08pm  Apr 16, 2015 7:08pm 

  * [ unionnone](unionnone)

  * | Joined Jun 2011  | Status: Stalker | [21 Posts](/search?do=process&provider=Member&searchuser=182352)

can we add paratemer for long only and sell only? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#329](/thread/post/8209267#post8209267 "Post Permalink")

  * Edited 7:11pm  Apr 16, 2015 7:09pm | Edited 7:11pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar185229_8.gif) Erebus](erebus)

  * Joined Jul 2011 | Status: Trader | [8,576 Posts](/search?do=process&provider=Member&searchuser=185229)

**Thanks skyline**  
  
I'll try the Global Prime account, I had 1.14 working there  
  
Edit: the script says, you are connected, this server is marked as live   
  
![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)

"Forex a Great Hobby, But Not a Great Job"

[Texas-2-Step](erebus#79 "View Trade Explorer") All Time Return: 8.8%

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#330](/thread/post/8209285#post8209285 "Post Permalink")

  * Apr 16, 2015 7:17pm  Apr 16, 2015 7:17pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar389954_3.gif) honestknave](honestknave)

  * Joined Nov 2014 | Status: Trader | [1,300 Posts](/search?do=process&provider=Member&searchuser=389954)

> [Quoting unionnone](/thread/post/8209265#post8209265 "View Quoted Post")
> 
> Disliked
> 
> can we add paratemer for long only and sell only?
> 
> Ignored

Have you tried the standard EA setting in the Common tab?  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Common.png
Size: 50 KB](/attachment/image/1654866/thumbnail?d=1429179426)](/attachment/image/1654866?d=1429179426)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#331](/thread/post/8209661#post8209661 "Post Permalink")

  * Apr 16, 2015 9:18pm  Apr 16, 2015 9:18pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

@ Honestknave : Thank you for helping ! ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
  
@ Erebus : Could you please also try attached script, and report back related screenshot ?  
  
Ty  
Cheers,  
Skyline 

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [CheckAccount.ex4](/attachment/file/1655012?d=1429186668) 4 KB | 312 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#332](/thread/post/8209724#post8209724 "Post Permalink")

  * Apr 16, 2015 9:43pm  Apr 16, 2015 9:43pm 

  * [ FireFries](firefries)

  * | Joined Apr 2015  | Status: Trader | [67 Posts](/search?do=process&provider=Member&searchuser=406710)

Hi Skyline,  
  
Am having the same issue with demo acct, pls see screenshot. All else is working right. 

Attached Image

![](/attachment/image/1655023?d=1429187968)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#333](/thread/post/8209878#post8209878 "Post Permalink")

  * Apr 16, 2015 10:38pm  Apr 16, 2015 10:38pm 

  * [ saek1985](saek1985)

  * | Joined Apr 2015  | Status: Trader | [4 Posts](/search?do=process&provider=Member&searchuser=407757)

> [Quoting skyline](/thread/post/8208851#post8208851 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi Saek, i checked for your issue , the calc routine seems to be correct, the only thing that could cause wrong counts is if you have orders in the same account opened (manually or by other EAs) which are taken into account in win/be/losses calculations. If this is the case then just be carefull to use this EA only on account where no other trading systems are used. Cheers, Skyline
> 
> Ignored

Hey Skyline.   
On this account only works Udine EA. No other transactions.  
Possible cause:  
On this account MM 4%>2% daily target, daily target reached. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#334](/thread/post/8209899#post8209899 "Post Permalink")

  * Apr 16, 2015 10:46pm  Apr 16, 2015 10:46pm 

  * [ saek1985](saek1985)

  * | Joined Apr 2015  | Status: Trader | [4 Posts](/search?do=process&provider=Member&searchuser=407757)

> [Quoting senanata](/thread/post/8208359#post8208359 "View Quoted Post")
> 
> Disliked
> 
> Hi Skyline This is my first report about UdineEA. I was successful when load the EA and template to the chart. Worked normally on GU, EU and GJ. But I can not attach template to EJ's chart. Everytime I try to do that, my mt4 always crash/hang and not responding as shown on my attachment. Can you tell me what I miss? Regards, Senanata {image} {image}
> 
> Ignored

Hey Senanata.  
  
Indicator xADR_0.2renko crash. Save the template without xADR_0.2renko. Add it separately. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#335](/thread/post/8210138#post8210138 "Post Permalink")

  * Apr 17, 2015 12:13am  Apr 17, 2015 12:13am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar389954_3.gif) honestknave](honestknave)

  * Joined Nov 2014 | Status: Trader | [1,300 Posts](/search?do=process&provider=Member&searchuser=389954)

> [Quoting skyline](/thread/post/8209661#post8209661 "View Quoted Post")
> 
> Disliked
> 
> @ Honestknave : Thank you for helping ! ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) @ Erebus : Could you please also try attached script, and report back related screenshot ? Ty Cheers, Skyline {file}
> 
> Ignored

No problem . if it helps , Erebus edited his earlier post to confirm that the server is returning !IsDemo() 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#336](/thread/post/8210143#post8210143 "Post Permalink")

  * Apr 17, 2015 12:14am  Apr 17, 2015 12:14am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting FireFries](/thread/post/8209724#post8209724 "View Quoted Post")
> 
> Disliked
> 
> Hi Skyline, Am having the same issue with demo acct, pls see screenshot. All else is working right. {image}
> 
> Ignored

Hi FireFries,  
as you see from script , server has flagged your account as real account (wrongly), you have to ask to your broker why they are doing this (maybe a bug on their side), I cannot do anything in this particular case.  
  
Cheers,  
Skyline 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#337](/thread/post/8210190#post8210190 "Post Permalink")

  * Apr 17, 2015 12:29am  Apr 17, 2015 12:29am 

  * [ kofix11](kofix11)

  * | Joined Dec 2011  | Status: Trader | [828 Posts](/search?do=process&provider=Member&searchuser=209345)

Hi Skyline  
  
On the first page you wrote: _* **EA is provided as is, there maybe several bugs that could damage seriously your account , so it's completely your decision and your risk to use it with real money**._  
  
Does it matter, if it only works on a demo account? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#338](/thread/post/8210212#post8210212 "Post Permalink")

  * Apr 17, 2015 12:38am  Apr 17, 2015 12:38am 

  * [ FireFries](firefries)

  * | Joined Apr 2015  | Status: Trader | [67 Posts](/search?do=process&provider=Member&searchuser=406710)

Thanks for the reply, Skyline, will just wait for the release of live trading. ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
Thanks for the nice template setup too, make it very easy to get it up, Cheers. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#339](/thread/post/8210222#post8210222 "Post Permalink")

  * Apr 17, 2015 12:45am  Apr 17, 2015 12:45am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar338950_1.gif) cescof](cescof)

  * Joined Jun 2013 | Status: Trader | [1,006 Posts](/search?do=process&provider=Member&searchuser=338950)

> [Quoting kofix11](/thread/post/8210190#post8210190 "View Quoted Post")
> 
> Disliked
> 
> Hi Skyline On the first page you wrote: * EA is provided as is, there maybe several bugs that could damage seriously your account , so it's completely your decision and your risk to use it with real money. Does it matter, if it only works on a demo account?
> 
> Ignored

Just for this trial time as he wrote....so whats the problemRegards 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#340](/thread/post/8210249#post8210249 "Post Permalink")

  * Apr 17, 2015 12:55am  Apr 17, 2015 12:55am 

  * [ kofix11](kofix11)

  * | Joined Dec 2011  | Status: Trader | [828 Posts](/search?do=process&provider=Member&searchuser=209345)

Hi cescof  
  
I have the same problem as Erebus. That's the situation I can't test it.  
Would it be life i could test it too.  
  
Thanks and good luck! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * UdineEA Official Thread
  *   * [ **Reply to Thread** ](/thread/533099-udineea-official-thread/reply#reply)

  * More

[](https://www.forexfactory.com "Homepage")

  * [Forums](forums)
  * [Trades](trades)
  * [Calendar](calendar)
  * [News](news)
  * [Market](market)
  * [Brokers](brokers)

****

[](https://www.faireconomy.com/)

  * 

[The Official "Ok, now I'm pissed" Thread](/thread/73546-the-official-ok-now-im-pissed-thread "Hello Everyone, 
 
Seeing the apparent lack of threads of this nature \(just kidding, but read on\) I have decided to set up a respectable...") 51 replies

[Historic Charts: NZ Official Cash Rate](/thread/20380-historic-charts-nz-official-cash-rate "Sep 14, 2005") 15 replies

[Is there an official exchange rate?!](/thread/11571-is-there-an-official-exchange-rate "Different brokers have different bid and ask prices for every cross or pair.  However, the bid and ask price is based on something...I am...") 14 replies

[Official forex time zone](/thread/9940-official-forex-time-zone "is there a standard forex time zone? do i follow gmt or NY time? i use 4 hour charts and sometimes the time is way off because of time zone...") 3 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/533099-udineea-official-thread/reply#reply)
  * Subscribe
  * [100](javascript:void\(0\);)

Attachments: UdineEA Official Thread

Tags: UdineEA Official Thread

#  [](/thread/533099-udineea-official-thread)UdineEA Official Thread 

  * 

  * [#341](/thread/post/8210278#post8210278 "Post Permalink")

  * Apr 17, 2015 1:09am  Apr 17, 2015 1:09am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting kofix11](/thread/post/8210190#post8210190 "View Quoted Post")
> 
> Disliked
> 
> Hi Skyline On the first page you wrote: * EA is provided as is, there maybe several bugs that could damage seriously your account , so it's completely your decision and your risk to use it with real money. Does it matter, if it only works on a demo account?
> 
> Ignored

Hi Kofix,  
of course that statement is not referred to demo account but only if you use (when I'll release) live version of this EA. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#342](/thread/post/8210311#post8210311 "Post Permalink")

  * Edited 1:42am  Apr 17, 2015 1:32am | Edited 1:42am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting saek1985](/thread/post/8209878#post8209878 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hey Skyline. On this account only works Udine EA. No other transactions. Possible cause: On this account MM 4%>2% daily target, daily target reached.
> 
> Ignored

Hi Saek,  
ok I've found the error : logic conditions to show both Daily Target and Max Losses Per Day labels were inverted, so that red cross had been referred to above label Daily Target (which it was reached in your case) and viceversa.  
It'll be fixed in next release.  
  
Ty for helping find this nasty bug ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)  
  
Cheers,  
Skyline 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#343](/thread/post/8210833#post8210833 "Post Permalink")

  * Apr 17, 2015 5:28am  Apr 17, 2015 5:28am 

  * [ rmndschmidt](rmndschmidt)

  * | Joined Mar 2014  | Status: Trader | [42 Posts](/search?do=process&provider=Member&searchuser=365689)

My results for today: 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Unbenannt.png
Size: 682 KB](/attachment/image/1655382/thumbnail?d=1429216075)](/attachment/image/1655382?d=1429216075)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#344](/thread/post/8211428#post8211428 "Post Permalink")

  * Apr 17, 2015 2:44pm  Apr 17, 2015 2:44pm 

  * [ brucech](brucech)

  * | Joined Sep 2006  | Status: Trader | [594 Posts](/search?do=process&provider=Member&searchuser=18716)

Skyline,  
  
Great work on this EA! Its seems to be working great!  
  
Question.  
TradeOnlyLondon (default = true) // If I set this to false so that I can let it run 24/5  
  
DailyTargetPercentage (default = 2) // And set the Daily target as percentage of account balance to 10%, will the EA continue until this value (10%) is reached and then stop trading for the rest of the day?  
  
I want to know if the Live account EA will take all trades daily. And not be **too restricted** by time (24/7) or target percentage (10%).  
  
Looking forward to testing this EA on a Live account.  
  
Thanks.  
  
Bruce 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#345](/thread/post/8211452#post8211452 "Post Permalink")

  * Apr 17, 2015 3:01pm  Apr 17, 2015 3:01pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar388093_1.gif) firewight](firewight)

  * | Joined Oct 2014  | Status: Trader | [817 Posts](/search?do=process&provider=Member&searchuser=388093)

@ Skyline  
  
I'd also like to say thanks and show the last 2 days since I loaded the latest version EA have been doing great.  
  
Good work to everyone involved in the development!  
  

Attached Image

![](/attachment/image/1655583?d=1429250462)

Life is like a snickers, its full of nuts!

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#346](/thread/post/8211688#post8211688 "Post Permalink")

  * Apr 17, 2015 5:03pm  Apr 17, 2015 5:03pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting brucech](/thread/post/8211428#post8211428 "View Quoted Post")
> 
> Disliked
> 
> Skyline, Great work on this EA! Its seems to be working great! Question. TradeOnlyLondon (default = true) // If I set this to false so that I can let it run 24/5 DailyTargetPercentage (default = 2) // And set the Daily target as percentage of account balance to 10%, will the EA continue until this value (10%) is reached and then stop trading for the rest of the day? I want to know if the Live account EA will take all trades daily. And not be too restricted by time (24/7) or target percentage (10%). Looking forward to testing this EA on a Live account....
> 
> Ignored

Hi Brucech,  
altough I do not endorse such use, if you want to enable EA to trade non stop, you could use something like this :  
  
TradeOnlyLondon = false;  
DailyTargetPercentage = 100; (most unlikely you can hit this on a daily base also because live version will be limited to 4% risk per trade)  
MaxLossesPerDay = 100; (this will be the worst thing to be done, it's far better to limit to 3-4 max losses per day)  
  
In this way EA should work continuosly, please just in case report back possible issue since I've never tester such extreme settings (and never will since are too much risky for my taste).  
  
Cheers,  
Skyline 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#347](/thread/post/8212117#post8212117 "Post Permalink")

  * Apr 17, 2015 7:47pm  Apr 17, 2015 7:47pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1024_7.gif) diallist](diallist)

  * Joined Sep 2004 | Status: Trader | [1,464 Posts](/search?do=process&provider=Member&searchuser=1024)

Hi skyline,  
Watching your EA perform these last two days has been like observing the inner workings of a fully-jeweled, fine Swiss watch!  
  
I did notice a bug tonight. A short pending order was placed correctly, but the note said potential long instead of potential short.  
  
Thanks  
  
Dial 

sxaxlxvxaxtxixoxnxbxyxgxrxaxcxexdxoxtxoxrxgx

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#348](/thread/post/8212156#post8212156 "Post Permalink")

  * Apr 17, 2015 8:05pm  Apr 17, 2015 8:05pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting diallist](/thread/post/8212117#post8212117 "View Quoted Post")
> 
> Disliked
> 
> Hi skyline, Watching your EA perform these last two days has been like observing the inner workings of a fully-jeweled, fine Swiss watch! I did notice a bug tonight. A short pending order was placed correctly, but the note said potential long instead of potential short. Thanks Dial
> 
> Ignored

Hi Dial,  
ty for your kind words ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)  
  
I'll check into issue you reported but I have to replicate on my platform before to be able to fix it  
  
Cheers,  
Skyline 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#349](/thread/post/8212514#post8212514 "Post Permalink")

  * Apr 17, 2015 10:08pm  Apr 17, 2015 10:08pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar338950_1.gif) cescof](cescof)

  * Joined Jun 2013 | Status: Trader | [1,006 Posts](/search?do=process&provider=Member&searchuser=338950)

On my side today 2 orders in sl -20pips EUR/JPY anyone?  
Regards 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#350](/thread/post/8212535#post8212535 "Post Permalink")

  * Apr 17, 2015 10:15pm  Apr 17, 2015 10:15pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting cescof](/thread/post/8212514#post8212514 "View Quoted Post")
> 
> Disliked
> 
> On my side today 2 orders in sl -20pips EUR/JPY anyone? Regards
> 
> Ignored

only one losing order form me up until now on EJ 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#351](/thread/post/8212543#post8212543 "Post Permalink")

  * Apr 17, 2015 10:18pm  Apr 17, 2015 10:18pm 

  * [ brucech](brucech)

  * | Joined Sep 2006  | Status: Trader | [594 Posts](/search?do=process&provider=Member&searchuser=18716)

> [Quoting cescof](/thread/post/8212514#post8212514 "View Quoted Post")
> 
> Disliked
> 
> On my side today 2 orders in sl -20pips EUR/JPY anyone? Regards
> 
> Ignored

For London session losing trades  
EURUSD -$20  
EURJPY -$20 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#352](/thread/post/8212658#post8212658 "Post Permalink")

  * Apr 17, 2015 10:49pm  Apr 17, 2015 10:49pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar338950_1.gif) cescof](cescof)

  * Joined Jun 2013 | Status: Trader | [1,006 Posts](/search?do=process&provider=Member&searchuser=338950)

> [Quoting skyline](/thread/post/8212535#post8212535 "View Quoted Post")
> 
> Disliked
> 
> {quote} only one losing order form me up until now on EJ
> 
> Ignored

Really strange... so you don't have the second order for EUR/JPY? We have same broker...  
Regards 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#353](/thread/post/8212782#post8212782 "Post Permalink")

  * Apr 17, 2015 11:33pm  Apr 17, 2015 11:33pm 

  * [ DerBerliner](derberliner)

  * | Joined Feb 2011  | Status: Trader | [822 Posts](/search?do=process&provider=Member&searchuser=168827)

Ok, the last posts are a good occasion for writing my honest view about this EA.  
No offense, but I have only little hope now after testing the bot myself and watching the testing of others here. I think the high sensitivity to the brokers resulting in serious differences between the single traders here shows step by step that this EA will fail ... yes, of course there will be good days/phases, no doubt, BUT one day its good with one broker, another day its good with another broker ... in a nutshell it's to instabile, not reliable enough ... AND we haven't had here live trading so far !! ![](https://resources.faireconomy.media/images/emojis/64/1f61e.png?v=15.1)  
And in my mind the improper R:R of 2:1 isn't a basic for success ! So, all in all sooner or later the equity will slow down in a stepwise manner .... unfortunately !  
Dunno really what to change to improve this bot, but perhaps the 00level startegy is indeed a manual method and the automatisation is impossible or nearly impossible ? ![](https://resources.faireconomy.media/images/emojis/64/1f937-200d-2642-fe0f.png?v=15.1)  
  
  
_All that's only my two pennnies worth !_ ![](https://resources.faireconomy.media/images/emojis/64/1f647-200d-2642-fe0f.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#354](/thread/post/8212870#post8212870 "Post Permalink")

  * Apr 18, 2015 12:06am  Apr 18, 2015 12:06am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar350360_20.gif) AKCodingEye](akcodingeye)

  * Joined Sep 2013 | Status: Such a Silly Game It is | [181 Posts](/search?do=process&provider=Member&searchuser=350360)

> [Quoting DerBerliner](/thread/post/8212782#post8212782 "View Quoted Post")
> 
> Disliked
> 
> Ok, the last posts are a good occasion for writing my honest view about this EA. No offense, but I have only little hope now after testing the bot myself and watching the testing of others here. I think the high sensitivity to the brokers resulting in serious differences between the single traders here shows step by step that this EA will fail ... yes, of course there will be good days/phases, no doubt, BUT one day its good with one broker, another day its good with another broker ... in a nutshell it's to instabile, not reliable enough ... AND...
> 
> Ignored

I have nothing personal against you. This is one of most promising ea I have ever seen. It's all on demo account ofcourse and can't wait to test on live with small position size and then I can tell more. I come to this thread after every few hours to check- has skyline released for live early and in case if he surprise us.  
  
Even I can see lots of download of EA, atleast say Thanks who share for nothing his more than 1000 line coding ea.  
  
  
Skyline, Again thanks for your EA. Great sole and programmer  
-AK- 

Whats get measured get improved

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#355](/thread/post/8212915#post8212915 "Post Permalink")

  * Edited 1:09am  Apr 18, 2015 12:26am | Edited 1:09am 

  * [ DerBerliner](derberliner)

  * | Joined Feb 2011  | Status: Trader | [822 Posts](/search?do=process&provider=Member&searchuser=168827)

No emotions are needed. In any case I/we have to say a big thank you to people like skyline, BUT: Its simply a business for all of us here ... including skyline himself ! At the end, the _only_ important thing is: will an EA (any EA) bring money for a long time or not. If an EA (any EA) fails - that usually happens unfortunately with nearly all of them - we have to accept that ! Nothing more we have to consider. ![](https://resources.faireconomy.media/images/emojis/64/1f610.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#356](/thread/post/8213068#post8213068 "Post Permalink")

  * Apr 18, 2015 1:39am  Apr 18, 2015 1:39am 

  * [ leancuisine](leancuisine)

  * | Joined Jul 2014  | Status: Trader | [38 Posts](/search?do=process&provider=Member&searchuser=376648)

That's odd, I didn't get the second buy EUR/JPY order for both my ThinkForex and FXOpen live accounts.  
  
Good thing it was a loss though. ![](https://resources.faireconomy.media/images/emojis/64/1f61c.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#357](/thread/post/8213090#post8213090 "Post Permalink")

  * Apr 18, 2015 1:50am  Apr 18, 2015 1:50am 

  * [ DerBerliner](derberliner)

  * | Joined Feb 2011  | Status: Trader | [822 Posts](/search?do=process&provider=Member&searchuser=168827)

I got it - like in skylines account. So you see it again: its a pity, but it's too doubtful .... ![](https://resources.faireconomy.media/images/emojis/64/1f612.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f615.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/2753.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#358](/thread/post/8213152#post8213152 "Post Permalink")

  * Apr 18, 2015 2:26am  Apr 18, 2015 2:26am 

  * [ leancuisine](leancuisine)

  * | Joined Jul 2014  | Status: Trader | [38 Posts](/search?do=process&provider=Member&searchuser=376648)

I also see that Skyline's lots increased, for EUR/JPY yesterday it was 0.05 lots, and today it's at 0.13 lots. ![](https://resources.faireconomy.media/images/emojis/64/1f61c.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#359](/thread/post/8213159#post8213159 "Post Permalink")

  * Apr 18, 2015 2:31am  Apr 18, 2015 2:31am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar338950_1.gif) cescof](cescof)

  * Joined Jun 2013 | Status: Trader | [1,006 Posts](/search?do=process&provider=Member&searchuser=338950)

3 orders today and -30pip EUR/JPY....  
Monitoring this pair for ignore list![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#360](/thread/post/8213177#post8213177 "Post Permalink")

  * Apr 18, 2015 2:43am  Apr 18, 2015 2:43am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

Hi DerBerliner,  
I completely agree with you, this EA in the long run will not gain any money , I'm quite sure about that infact I also wrote this in 1st post :  
  
_'To be noted that this EA cannot be properly backtested due to news filter presence, so _**I do not trust it completely**_ because I cannot figure out its statistical behaviour so I cannot evaluate its weakness and limit (max drawdown, max consecutive losses,...)'_  
  
There's no doubt that this kind of EA with few pips in TP,SL,TS are very sensible to broker data, I've already wrote here that I had (few) different trades using the same EA on two different account in the same broker but it's not an EA issue or some programming bug (at least not that I've yet discovered), so you cannot fix this by adding 'filter'.  
  
For the above reason I'll release a 'risk-controlled' live verison where mak risk per trade will be limited to 4% , because EA of this kind could seriously damage a real account.  
  
Then will be up to each of you to decide if try to test it in live or not , I think I'll do but with a very little account (less than 500 euro) with 2% risk per trade and will stop at -30% no matter what.  
  
Regads,  
Skyline 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * UdineEA Official Thread
  *   * [ **Reply to Thread** ](/thread/533099-udineea-official-thread/reply#reply)

  * More

[](https://www.forexfactory.com "Homepage")

  * [Forums](forums)
  * [Trades](trades)
  * [Calendar](calendar)
  * [News](news)
  * [Market](market)
  * [Brokers](brokers)

****

[](https://www.faireconomy.com/)

  * 

[The Official "Ok, now I'm pissed" Thread](/thread/73546-the-official-ok-now-im-pissed-thread "Hello Everyone, 
 
Seeing the apparent lack of threads of this nature \(just kidding, but read on\) I have decided to set up a respectable...") 51 replies

[Historic Charts: NZ Official Cash Rate](/thread/20380-historic-charts-nz-official-cash-rate "Sep 14, 2005") 15 replies

[Is there an official exchange rate?!](/thread/11571-is-there-an-official-exchange-rate "Different brokers have different bid and ask prices for every cross or pair.  However, the bid and ask price is based on something...I am...") 14 replies

[Official forex time zone](/thread/9940-official-forex-time-zone "is there a standard forex time zone? do i follow gmt or NY time? i use 4 hour charts and sometimes the time is way off because of time zone...") 3 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/533099-udineea-official-thread/reply#reply)
  * Subscribe
  * [100](javascript:void\(0\);)

Attachments: UdineEA Official Thread

Tags: UdineEA Official Thread

#  [](/thread/533099-udineea-official-thread)UdineEA Official Thread 

  * 

  * [#361](/thread/post/8213182#post8213182 "Post Permalink")

  * Apr 18, 2015 2:44am  Apr 18, 2015 2:44am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting leancuisine](/thread/post/8213152#post8213152 "View Quoted Post")
> 
> Disliked
> 
> I also see that Skyline's lots increased, for EUR/JPY yesterday it was 0.05 lots, and today it's at 0.13 lots. ![](https://resources.faireconomy.media/images/emojis/64/1f61c.png?v=15.1)
> 
> Ignored

yes I changed the version yesterday to test latest bug fix , but I forgot to change risk setting which I've changed for today which was a losing day ![](https://resources.faireconomy.media/images/emojis/64/1f641.png?v=15.1)  
  
Cheers,  
Skyline 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#362](/thread/post/8213187#post8213187 "Post Permalink")

  * Apr 18, 2015 2:46am  Apr 18, 2015 2:46am 

  * [ DerBerliner](derberliner)

  * | Joined Feb 2011  | Status: Trader | [822 Posts](/search?do=process&provider=Member&searchuser=168827)

> [Quoting cescof](/thread/post/8213159#post8213159 "View Quoted Post")
> 
> Disliked
> 
> .... Monitoring this pair for ignore list![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)
> 
> Ignored

My friend - do you really think that makes sense ? ![](https://resources.faireconomy.media/images/emojis/64/1f44e.png?v=15.1)  
  
Never ! One day you have good trades with one pair, another day another pair isn't doing in _your_ favour ...  
  
So it'll make no difference trading with or without that EURJPY ...  
  
(Remember this funny saying: Monday and friday are bad days for trading - the other bad days are tuesday, wednesday and thursday ! ![](https://resources.faireconomy.media/images/emojis/64/1f923.png?v=15.1)) 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#363](/thread/post/8213483#post8213483 "Post Permalink")

  * Apr 18, 2015 8:50am  Apr 18, 2015 8:50am 

  * [ dlouw](dlouw)

  * | Joined Feb 2009  | Status: Trader | [136 Posts](/search?do=process&provider=Member&searchuser=94177)

skyline, Thank you for your efforts here. I look forward to testing this. In the best case we will all make a lot of profit. In the worst case we will learn about "discretionary" variables that separate those successful with Udine's 00 strategy from the rest. We both know success is possible. This could be a boon to those like myself (West Coast USA, PST) who have challenges trading the London session and managing a day job. I do hope that you will make MT4 files available so that those so included can stand on the shoulders on Udine and yourself and explore other "discretionary" variables and share the results.  
  
It is interesting that this EA is getting different results for different platforms. It is using the same information that manual traders are using to base decisions. Different broker feeds and [spreads](/brokers/spreads "View Live Spreads on the Broker Guide") are expected. We can always change brokers. Are the differences being measured on the same broker feed and location? With the same feed and internet connection this may be cause for concern, ei "stacking the deck"  
  
All the Best!  
dlouw 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#364](/thread/post/8213527#post8213527 "Post Permalink")

  * Apr 18, 2015 10:44am  Apr 18, 2015 10:44am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar261568_2.gif) senanata](senanata)

  * | Joined Jun 2012  | Status: Trader | [267 Posts](/search?do=process&provider=Member&searchuser=261568)

Nothing happened yesterday. No opened trades at all. Open pending order once but cancelled. Don't know why. 

MAKE SURE you still can TRADE tomorrow

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#365](/thread/post/8213545#post8213545 "Post Permalink")

  * Apr 18, 2015 11:51am  Apr 18, 2015 11:51am 

  * [ unionnone](unionnone)

  * | Joined Jun 2011  | Status: Stalker | [21 Posts](/search?do=process&provider=Member&searchuser=182352)

> [Quoting honestknave](/thread/post/8209285#post8209285 "View Quoted Post")
> 
> Disliked
> 
> {quote} Have you tried the standard EA setting in the Common tab? {image}
> 
> Ignored

damn, such an easy thing i miss out. thank!!!![](https://resources.faireconomy.media/images/emojis/64/1f60d.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#366](/thread/post/8213717#post8213717 "Post Permalink")

  * Apr 18, 2015 7:30pm  Apr 18, 2015 7:30pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting senanata](/thread/post/8213527#post8213527 "View Quoted Post")
> 
> Disliked
> 
> Nothing happened yesterday. No opened trades at all. Open pending order once but cancelled. Don't know why.
> 
> Ignored

Hi Senanata, pending orders that are not triggered at the end of candle are deleted.  
  
Cheers,  
Skyline 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#367](/thread/post/8213739#post8213739 "Post Permalink")

  * Apr 18, 2015 8:06pm  Apr 18, 2015 8:06pm 

  * [ DerBerliner](derberliner)

  * | Joined Feb 2011  | Status: Trader | [822 Posts](/search?do=process&provider=Member&searchuser=168827)

@senanata  
  
Ups ... **no trades at all**?  
  
That's quite different to all of us here ....  
  
That's good luck for you ! God grant that your broker would do all that further in your favour .... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#368](/thread/post/8213848#post8213848 "Post Permalink")

  * Apr 18, 2015 11:09pm  Apr 18, 2015 11:09pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1024_7.gif) diallist](diallist)

  * Joined Sep 2004 | Status: Trader | [1,464 Posts](/search?do=process&provider=Member&searchuser=1024)

It is too early to pass judgement on this EA. Common sense and mathematics tells us that this EA has an edge.  
  
Any edge, however small will bring the AWR above the BEWR curve, but the question that remains is whether it is far enough above the BEWR curve to cover transaction costs, and further still above to yield a profit.  
  
If it is sufficient, it may do so at a very slow rate, dithering above and below the starting balance, but yielding only a small return each week or month, but a positive return nonetheless.  
  
I say we let the EA do its work over a series of 500 or (better) a 1000 trades.  
  
Even if it proves to be unprofitable over time, it will at the very least serve as an instructor to us by giving us the opportunity to examine each losing trade for discretionary variables that would have kept us out of the trade. By this I mean, for example, seeing SR or Pivot levels on the chart that are invisible to the EA.  
  
Even if it only serves in that capacity, it is still a very valuable tool and was worth all the effort that skyline put into it.  
  
As for myself, I withhold judgement until at least 500 trades have been taken.  
  
Dial 

sxaxlxvxaxtxixoxnxbxyxgxrxaxcxexdxoxtxoxrxgx

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#369](/thread/post/8213884#post8213884 "Post Permalink")

  * Apr 18, 2015 11:43pm  Apr 18, 2015 11:43pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting diallist](/thread/post/8213848#post8213848 "View Quoted Post")
> 
> Disliked
> 
> It is too early to pass judgement on this EA. Common sense and mathematics tells us that this EA has an edge. Any edge, however small will bring the AWR above the BEWR curve, but the question that remains is whether it is far enough above the BEWR curve to cover transaction costs, and further still above to yield a profit. If it is sufficient, it may do so at a very slow rate, dithering above and below the starting balance, but yielding only a small return each week or month, but a positive return nonetheless. I say we let the EA do its work over...
> 
> Ignored

  
This post should be sticky at each sub-forum here in FF ! ![](https://resources.faireconomy.media/images/emojis/64/1f917.png?v=15.1)  
  
Thank You Dial ! ![](https://resources.faireconomy.media/images/emojis/64/1f647-200d-2642-fe0f.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#370](/thread/post/8213900#post8213900 "Post Permalink")

  * Apr 18, 2015 11:58pm  Apr 18, 2015 11:58pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

Looking at actual stats in my demo account UdineEA is opened since 25 days and were placed 36 trades, if my math are correct and trades will be placed at the same pace, to reach 500 trades there would need :  
  
Days = (25*500)/36 = 347 days  
  
so around 1 year to be able , as Dial said, to evaluate this EA.  
Do you have the necessary will to accomplish this task ?  
Do not forget that drawdown period surely will occurs and could be also prolonged (months and months without any equity high).  
  
Just to speak, I'm trading a completely different EA (portfolio of 5 EAs) running on real account that is in drawdown (-26%) since when it's started (around 6 months ago).  
Why do I keep trading it ? Because in that case I've calculated precise statistical numbers and whole portfolio is still below its limits.  
UdineEA is different because no backtest could be done so we don't know how behaved in past , so we have only to test in forward live.  
  
Regards,  
Skyline 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#371](/thread/post/8214013#post8214013 "Post Permalink")

  * Apr 19, 2015 2:49am  Apr 19, 2015 2:49am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar350360_20.gif) AKCodingEye](akcodingeye)

  * Joined Sep 2013 | Status: Such a Silly Game It is | [181 Posts](/search?do=process&provider=Member&searchuser=350360)

> [Quoting dlouw](/thread/post/8213483#post8213483 "View Quoted Post")
> 
> Disliked
> 
> skyline, Thank you for your efforts here. I look forward to testing this. In the best case we will all make a lot of profit. In the worst case we will learn about "discretionary" variables that separate those successful with Udine's 00 strategy from the rest. We both know success is possible. This could be a boon to those like myself (West Coast USA, PST) who have challenges trading the London session and managing a day job. **I do hope that you will make MT4 files available so that those so included can stand on the shoulders on Udine and yourself**...
> 
> Ignored

I am also hoping same as there is edge in this ea and we can try different variation and idea and test on same time and share result here 

Whats get measured get improved

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#372](/thread/post/8214859#post8214859 "Post Permalink")

  * Apr 20, 2015 2:56am  Apr 20, 2015 2:56am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

Hi all,  
I'd like to send my thank to all fellow traders who send me here and my pm , appreciations message and also for testing and reporting bugs. ![](https://resources.faireconomy.media/images/emojis/64/1f917.png?v=15.1)  
  
As promised after a month of demo test, I've just released UdineEA v1.1.6 in 1st post which is enabled to trade on real account.  
  
_**To avoid improper use, I've locked max risk per pair to 4%; if you try to set RiskPerTrade more than 4%, EA will throw an alert and stop trading.**_  
  
I'll manage at the start of next month to fund a tiny live account and link the account here.  
  
My task will be to let the UdineEA to run at least 1 year until May 2016 to see real performance.  
  
Trade Well!  
  
Regards,  
Skyline 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#373](/thread/post/8214892#post8214892 "Post Permalink")

  * Edited 3:42am  Apr 20, 2015 3:30am | Edited 3:42am 

  * [ Maxlor](maxlor)

  * | Joined Apr 2015  | Status: Trader | [2 Posts](/search?do=process&provider=Member&searchuser=408736)

Good evening everyone, I'm very interested in the trial of your udineEA since I'm using a complex indicator pre buy or sell manually , Nihilist_Ultra_Trend_V2 Currently I'm testing your udineEA 115 , but I saw that was released a new version . Thanks for any help you can give me 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#374](/thread/post/8214964#post8214964 "Post Permalink")

  * Apr 20, 2015 4:23am  Apr 20, 2015 4:23am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar298742_5.gif) bluejack](bluejack)

  * | Joined Oct 2012  | Status: Trader | [493 Posts](/search?do=process&provider=Member&searchuser=298742)

Thank You Skyline. ![](https://resources.faireconomy.media/images/emojis/64/1f917.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#375](/thread/post/8215000#post8215000 "Post Permalink")

  * Apr 20, 2015 4:56am  Apr 20, 2015 4:56am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar350360_20.gif) AKCodingEye](akcodingeye)

  * Joined Sep 2013 | Status: Such a Silly Game It is | [181 Posts](/search?do=process&provider=Member&searchuser=350360)

Thank you skyline again  
  
Is that possible to unlock pairs, so we test more low spread pairs please? 

Whats get measured get improved

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#376](/thread/post/8215216#post8215216 "Post Permalink")

  * Apr 20, 2015 7:37am  Apr 20, 2015 7:37am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar261568_2.gif) senanata](senanata)

  * | Joined Jun 2012  | Status: Trader | [267 Posts](/search?do=process&provider=Member&searchuser=261568)

> [Quoting skyline](/thread/post/8214859#post8214859 "View Quoted Post")
> 
> Disliked
> 
> Hi all, I'd like to send my thank to all fellow traders who send me here and my pm , appreciations message and also for testing and reporting bugs. ![](https://resources.faireconomy.media/images/emojis/64/1f917.png?v=15.1) As promised after a month of demo test, I've just released UdineEA v1.1.6 in 1st post which is enabled to trade on real account. To avoid improper use, I've locked max risk per pair to 4%; if you try to set RiskPerTrade more than 4%, EA will throw an alert and stop trading. I'll manage at the start of next month to fund a tiny live account and link the account here. My task will be to let the UdineEA...
> 
> Ignored

Hi Skyline,  
  
Can't wait for this. Thanks a lot for your effort, once again. I'll give my live reports asap.  
  
Regards,  
Senanata 

MAKE SURE you still can TRADE tomorrow

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#377](/thread/post/8215222#post8215222 "Post Permalink")

  * Apr 20, 2015 7:42am  Apr 20, 2015 7:42am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar261568_2.gif) senanata](senanata)

  * | Joined Jun 2012  | Status: Trader | [267 Posts](/search?do=process&provider=Member&searchuser=261568)

> [Quoting AKCodingEye](/thread/post/8215000#post8215000 "View Quoted Post")
> 
> Disliked
> 
> Thank you skyline again Is that possible to unlock pairs, so we test more low spread pairs please?
> 
> Ignored

HI AKCodingEye,  
  
Pls see at the 1st post about EA Rules.  
.....EA is designed to open only at .00 level (not .50 level) and work only on EJ,EU,GU,GJ (**_please don't ask for other currencies,index,metals,cfd and so on...!_**)  
  
Happy Trade,  
Senanata

MAKE SURE you still can TRADE tomorrow

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#378](/thread/post/8215260#post8215260 "Post Permalink")

  * Apr 20, 2015 8:05am  Apr 20, 2015 8:05am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar388093_1.gif) firewight](firewight)

  * | Joined Oct 2014  | Status: Trader | [817 Posts](/search?do=process&provider=Member&searchuser=388093)

@Skyline,  
  
Thanks for the update mate!  
  
Can you tell me, is there anything else changed in the new version of the EA, or just the live trading option?  
  
Cheers! 

Life is like a snickers, its full of nuts!

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#379](/thread/post/8215405#post8215405 "Post Permalink")

  * Apr 20, 2015 11:05am  Apr 20, 2015 11:05am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar388093_1.gif) firewight](firewight)

  * | Joined Oct 2014  | Status: Trader | [817 Posts](/search?do=process&provider=Member&searchuser=388093)

@Skyline,  
  
Hey mate, I noticed something interesting today, I know it's intentional but not sure if it's accurate.  
  
I know there's a max of 1 order per pair, per hour. My EA placed a pending order with did not get taken after 30 mins and so was deleted. This is expected as far as I understand it.  
  
However, the max 1 order filter then kicked in and would not trade until the next hour, even though no order was actually filled.  
  
This is just for your information, I am not complaining LOL  
  
Cheers mate! 

Life is like a snickers, its full of nuts!

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#380](/thread/post/8215690#post8215690 "Post Permalink")

  * Apr 20, 2015 4:02pm  Apr 20, 2015 4:02pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

Hi Firewight,  
new v1.1.6 has some minor bug fixed nothing to do with logic entry, so in essence is the same as previous 1.1.5, the only difference is that now is able to trade on live account and risk is maxed at 4% per pair (so no fixed risk and money management always on).  
  
The '1 max order per hour' rule kicks in only if pending order is actually triggered into a market order (Ive checked again code) so in your case it shouldn't prevent to place another pending order in next M30 candle (of course if entry conditions are met). I've never see such issue , I'll monitor closely to see if I can replicate it.  
  
Ty  
Cheers,  
Skyline 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * UdineEA Official Thread
  *   * [ **Reply to Thread** ](/thread/533099-udineea-official-thread/reply#reply)

  * More

[](https://www.forexfactory.com "Homepage")

  * [Forums](forums)
  * [Trades](trades)
  * [Calendar](calendar)
  * [News](news)
  * [Market](market)
  * [Brokers](brokers)

****

[](https://www.faireconomy.com/)

  * 

[The Official "Ok, now I'm pissed" Thread](/thread/73546-the-official-ok-now-im-pissed-thread "Hello Everyone, 
 
Seeing the apparent lack of threads of this nature \(just kidding, but read on\) I have decided to set up a respectable...") 51 replies

[Historic Charts: NZ Official Cash Rate](/thread/20380-historic-charts-nz-official-cash-rate "Sep 14, 2005") 15 replies

[Is there an official exchange rate?!](/thread/11571-is-there-an-official-exchange-rate "Different brokers have different bid and ask prices for every cross or pair.  However, the bid and ask price is based on something...I am...") 14 replies

[Official forex time zone](/thread/9940-official-forex-time-zone "is there a standard forex time zone? do i follow gmt or NY time? i use 4 hour charts and sometimes the time is way off because of time zone...") 3 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/533099-udineea-official-thread/reply#reply)
  * Subscribe
  * [100](javascript:void\(0\);)

Attachments: UdineEA Official Thread

Tags: UdineEA Official Thread

#  [](/thread/533099-udineea-official-thread)UdineEA Official Thread 

  * 

  * [#381](/thread/post/8215693#post8215693 "Post Permalink")

  * Apr 20, 2015 4:04pm  Apr 20, 2015 4:04pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting senanata](/thread/post/8215222#post8215222 "View Quoted Post")
> 
> Disliked
> 
> {quote} HI AKCodingEye, Pls see at the 1st post about EA Rules. .....EA is designed to open only at .00 level (not .50 level) and work only on EJ,EU,GU,GJ (please don't ask for other currencies,index,metals,cfd and so on...!) Happy Trade, Senanata
> 
> Ignored

![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#382](/thread/post/8215728#post8215728 "Post Permalink")

  * Apr 20, 2015 4:19pm  Apr 20, 2015 4:19pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar360850_1.gif) Clipi](clipi)

  * | Joined Jan 2014  | Status: Trader | [482 Posts](/search?do=process&provider=Member&searchuser=360850)

a question, because ASH this with a red cross if at ASH bar is red, and the search for short ASH should be red. with what should execute short order.  
thank you very much. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: EURJPYM30.png
Size: 46 KB](/attachment/image/1657151/thumbnail?d=1429514368)](/attachment/image/1657151?d=1429514368)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#383](/thread/post/8215771#post8215771 "Post Permalink")

  * Apr 20, 2015 4:42pm  Apr 20, 2015 4:42pm 

  * [ Luy](luy)

  * | Joined Jan 2015  | Status: Trader | [7 Posts](/search?do=process&provider=Member&searchuser=396096)

> [Quoting skyline](/thread/post/8215690#post8215690 "View Quoted Post")
> 
> Disliked
> 
> Hi Firewight, new v1.1.6 has some minor bug fixed nothing to do with logic entry, so in essence is the same as previous 1.1.5, the only difference is that now is able to trade on live account and risk is maxed at 4% per pair (so no fixed risk and money management always on). The '1 max order per hour' rule kicks in only if pending order is actually triggered into a market order (Ive checked again code) so in your case it shouldn't prevent to place another pending order in next M30 candle (of course if entry conditions are met). I've never see such...
> 
> Ignored

  
Hi skyline!  
  
Thanks again for your work.  
I saw the same thing like firewight. A trade wasn´t opened cause of the 1 trade per hour rule. But there was only a potential trade this hour not a real trade. See picture.  
  
Hope you all have a good start in the fresh week,  
Luy 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: bug.png
Size: 62 KB](/attachment/image/1657167/thumbnail?d=1429515707)](/attachment/image/1657167?d=1429515707)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#384](/thread/post/8215788#post8215788 "Post Permalink")

  * Apr 20, 2015 4:51pm  Apr 20, 2015 4:51pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting Clipi](/thread/post/8215728#post8215728 "View Quoted Post")
> 
> Disliked
> 
> a question, because ASH this with a red cross if at ASH bar is red, and the search for short ASH should be red. with what should execute short order. thank you very much. {image}
> 
> Ignored

Hi Clipi,  
to give a valid entry ASH has to change its color from green to red , in your screenshot is all the way red so there is no signal for ASH.  
  
Cheers,  
Skyline 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#385](/thread/post/8215798#post8215798 "Post Permalink")

  * Apr 20, 2015 4:53pm  Apr 20, 2015 4:53pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting Luy](/thread/post/8215771#post8215771 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi skyline! Thanks again for your work. I saw the same thing like firewight. A trade wasnt opened cause of the 1 trade per hour rule. But there was only a potential trade this hour not a real trade. See picture. Hope you all have a good start in the fresh week, Luy {image}
> 
> Ignored

Hi Luy,  
ty for reporting bug with screenshot, will check more deeply in source code. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#386](/thread/post/8215960#post8215960 "Post Permalink")

  * Apr 20, 2015 6:21pm  Apr 20, 2015 6:21pm 

  * [ FireFries](firefries)

  * | Joined Apr 2015  | Status: Trader | [67 Posts](/search?do=process&provider=Member&searchuser=406710)

hi Skyline,  
  
while testing, all checks were green till it reach Pot, didn't trigger. EA looking good, smiley and then mark "Price above pot" as negative. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot1.png
Size: 64 KB](/attachment/image/1657251/thumbnail?d=1429521322)](/attachment/image/1657251?d=1429521322)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#387](/thread/post/8215963#post8215963 "Post Permalink")

  * Apr 20, 2015 6:23pm  Apr 20, 2015 6:23pm 

  * [ Luy](luy)

  * | Joined Jan 2015  | Status: Trader | [7 Posts](/search?do=process&provider=Member&searchuser=396096)

Get anyone triggered the gu long @ 1.4970?  
I saw that skyline get the short @ 1.4940. I was triggered long and so the short couldn´t get triggered cause of the 1 trade per hour rule. ![](https://resources.faireconomy.media/images/emojis/64/1f641.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#388](/thread/post/8215964#post8215964 "Post Permalink")

  * Apr 20, 2015 6:24pm  Apr 20, 2015 6:24pm 

  * [ Luy](luy)

  * | Joined Jan 2015  | Status: Trader | [7 Posts](/search?do=process&provider=Member&searchuser=396096)

picture 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: long gu.png
Size: 17 KB](/attachment/image/1657265/thumbnail?d=1429521834)](/attachment/image/1657265?d=1429521834)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#389](/thread/post/8216001#post8216001 "Post Permalink")

  * Apr 20, 2015 6:42pm  Apr 20, 2015 6:42pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar350360_20.gif) AKCodingEye](akcodingeye)

  * Joined Sep 2013 | Status: Such a Silly Game It is | [181 Posts](/search?do=process&provider=Member&searchuser=350360)

> [Quoting senanata](/thread/post/8215222#post8215222 "View Quoted Post")
> 
> Disliked
> 
> {quote} HI AKCodingEye, Pls see at the 1st post about EA Rules. .....EA is designed to open only at .00 level (not .50 level) and work only on EJ,EU,GU,GJ (please don't ask for other currencies,index,metals,cfd and so on...!) Happy Trade, Senanata
> 
> Ignored

I always read 1st post of thread before posting in any thread. Yes i saw that line as well. If you forward test four pairs or eight pairs, does it make any difference. **NO.** Why can't we test eight pairs on same time and save some time for forward testing. I am not requesting for any changes but requested for more pairs to open. I am seeing this EA has an Edge and Potential. So i couldn't sleep last night and it opened usd/chf trade today just after gbp/usd![](https://resources.faireconomy.media/images/emojis/64/1f914.png?v=15.1). Add me as friend and you might be able to see my Trade Explorer. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: usdchf.jpg
Size: 14 KB](/attachment/image/1657284/thumbnail?d=1429522718)](/attachment/image/1657284?d=1429522718)   

Whats get measured get improved

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#390](/thread/post/8216436#post8216436 "Post Permalink")

  * Apr 20, 2015 9:51pm  Apr 20, 2015 9:51pm 

  * [ jiaxingx](jiaxingx)

  * | Joined Apr 2012  | Status: Trader | [22 Posts](/search?do=process&provider=Member&searchuser=250425)

get a error:  
2015.04.20 20:47:59.487 Udine EA_v116 GBPJPY,M30: Errore SELL(3) : invalid trade parameters - EntryLong = 177.4 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#391](/thread/post/8216541#post8216541 "Post Permalink")

  * Apr 20, 2015 10:38pm  Apr 20, 2015 10:38pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting jiaxingx](/thread/post/8216436#post8216436 "View Quoted Post")
> 
> Disliked
> 
> get a error: 2015.04.20 20:47:59.487 Udine EA_v116 GBPJPY,M30: Errore SELL(3) : invalid trade parameters - EntryLong = 177.4
> 
> Ignored

Hi jiaxingx, maybe you're using a broker with high spread for GJ and it won't let place trade because entryprice is too much near to actual bid. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#392](/thread/post/8216549#post8216549 "Post Permalink")

  * Apr 20, 2015 10:40pm  Apr 20, 2015 10:40pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting Luy](/thread/post/8215963#post8215963 "View Quoted Post")
> 
> Disliked
> 
> Get anyone triggered the gu long @ 1.4970? I saw that skyline get the short @ 1.4940. I was triggered long and so the short couldnt get triggered cause of the 1 trade per hour rule. ![](https://resources.faireconomy.media/images/emojis/64/1f641.png?v=15.1)
> 
> Ignored

Hi Luy,  
as repeted over and over , is it possible to experience broker feed dependancy using this EA, in my case (ICMarkets Demo) only a short was triggered on that trade at 1.4940  
  
Cheers,  
Skyline 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#393](/thread/post/8216773#post8216773 "Post Permalink")

  * Apr 20, 2015 11:54pm  Apr 20, 2015 11:54pm 

  * [ jiaxingx](jiaxingx)

  * | Joined Apr 2012  | Status: Trader | [22 Posts](/search?do=process&provider=Member&searchuser=250425)

> [Quoting skyline](/thread/post/8216541#post8216541 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi jiaxingx, maybe you're using a broker with high spread for GJ and it won't let place trade because entryprice is too much near to actual bid.
> 
> Ignored

I use [Ic markets](/brokers/ic-markets "View IC Markets Broker Profile") broker,same as yours. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#394](/thread/post/8216801#post8216801 "Post Permalink")

  * Apr 21, 2015 12:07am  Apr 21, 2015 12:07am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting jiaxingx](/thread/post/8216773#post8216773 "View Quoted Post")
> 
> Disliked
> 
> {quote} I use Ic markets broker,same as yours.
> 
> Ignored

that's strange, I don't have that error in my platform , is demo or real account ? maybe something to do with connection to broker server... it's quite difficult for me to debug if I cannot replicate in my platform ![](https://resources.faireconomy.media/images/emojis/64/1f615.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/2753.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#395](/thread/post/8217638#post8217638 "Post Permalink")

  * Apr 21, 2015 10:46am  Apr 21, 2015 10:46am 

  * [ jiaxingx](jiaxingx)

  * | Joined Apr 2012  | Status: Trader | [22 Posts](/search?do=process&provider=Member&searchuser=250425)

> [Quoting skyline](/thread/post/8216801#post8216801 "View Quoted Post")
> 
> Disliked
> 
> {quote} that's strange, I don't have that error in my platform , is demo or real account ? maybe something to do with connection to broker server... it's quite difficult for me to debug if I cannot replicate in my platform ![](https://resources.faireconomy.media/images/emojis/64/1f615.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/2753.png?v=15.1)
> 
> Ignored

demo account,continue to test. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#396](/thread/post/8217646#post8217646 "Post Permalink")

  * Apr 21, 2015 10:49am  Apr 21, 2015 10:49am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar388093_1.gif) firewight](firewight)

  * | Joined Oct 2014  | Status: Trader | [817 Posts](/search?do=process&provider=Member&searchuser=388093)

> [Quoting skyline](/thread/post/8216549#post8216549 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi Luy, as repeted over and over , is it possible to experience broker feed dependancy using this EA, in my case (ICMarkets Demo) only a short was triggered on that trade at 1.4940 Cheers, Skyline
> 
> Ignored

I can also confirm many data feed freezes from ICM Demo server...  
  
This could be contributing to the issues... 

Life is like a snickers, its full of nuts!

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#397](/thread/post/8217946#post8217946 "Post Permalink")

  * Apr 21, 2015 3:50pm  Apr 21, 2015 3:50pm 

  * [ Bhutugly](bhutugly)

  * | Joined Oct 2011  | Status: Trader | [12 Posts](/search?do=process&provider=Member&searchuser=200586)

Skyline,  
  
Like yourself I use IC Markets.  
  
Strange how we have different days! (Ignore the last order as I was testing another strat but EA kicked in and closed it)!  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot1.png
Size: 34 KB](/attachment/image/1657989/thumbnail?d=1429598993)](/attachment/image/1657989?d=1429598993)   

  
  
Strange!  
  
Keep up the good work!  
  
Ian 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#398](/thread/post/8218053#post8218053 "Post Permalink")

  * Apr 21, 2015 4:32pm  Apr 21, 2015 4:32pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar92244_3.gif) pret](pret)

  * | Joined Jan 2009  | Status: Trader | [217 Posts](/search?do=process&provider=Member&searchuser=92244) | Online Now 

Hi Skyline  
Thank you for this EA  
I currently run this EA on 24 hrs [Pepperstone](/brokers/pepperstone "View Pepperstone Broker Profile") account since Monday What i would like to do is to override trailing stop , is this possible  
Thank you 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#399](/thread/post/8218061#post8218061 "Post Permalink")

  * Apr 21, 2015 4:36pm  Apr 21, 2015 4:36pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting Bhutugly](/thread/post/8217946#post8217946 "View Quoted Post")
> 
> Disliked
> 
> Skyline, Like yourself I use IC Markets. Strange how we have different days! (Ignore the last order as I was testing another strat but EA kicked in and closed it)! {image} Strange! Keep up the good work! Ian
> 
> Ignored

Hi Bhutugly,  
I've experienced the same thing using two different account on IC Markets, the EA using low tp,sl and ts is very sensible to connection to the broker server, quotes, and so on, something we already talked about , so no surprise at all. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#400](/thread/post/8218081#post8218081 "Post Permalink")

  * Apr 21, 2015 4:40pm  Apr 21, 2015 4:40pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting pret](/thread/post/8218053#post8218053 "View Quoted Post")
> 
> Disliked
> 
> Hi Skyline Thank you for this EA I currently run this EA on 24 hrs Pepperstone account since Monday What i would like to do is to override trailing stop , is this possible Thank you
> 
> Ignored

Hi Pret, just set TrailingStop to 0 and it will be disabled. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * UdineEA Official Thread
  *   * [ **Reply to Thread** ](/thread/533099-udineea-official-thread/reply#reply)

  * More

[](https://www.forexfactory.com "Homepage")

  * [Forums](forums)
  * [Trades](trades)
  * [Calendar](calendar)
  * [News](news)
  * [Market](market)
  * [Brokers](brokers)

****

[](https://www.faireconomy.com/)

  * 

[The Official "Ok, now I'm pissed" Thread](/thread/73546-the-official-ok-now-im-pissed-thread "Hello Everyone, 
 
Seeing the apparent lack of threads of this nature \(just kidding, but read on\) I have decided to set up a respectable...") 51 replies

[Historic Charts: NZ Official Cash Rate](/thread/20380-historic-charts-nz-official-cash-rate "Sep 14, 2005") 15 replies

[Is there an official exchange rate?!](/thread/11571-is-there-an-official-exchange-rate "Different brokers have different bid and ask prices for every cross or pair.  However, the bid and ask price is based on something...I am...") 14 replies

[Official forex time zone](/thread/9940-official-forex-time-zone "is there a standard forex time zone? do i follow gmt or NY time? i use 4 hour charts and sometimes the time is way off because of time zone...") 3 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/533099-udineea-official-thread/reply#reply)
  * Subscribe
  * [100](javascript:void\(0\);)

Attachments: UdineEA Official Thread

Tags: UdineEA Official Thread

#  [](/thread/533099-udineea-official-thread)UdineEA Official Thread 

  * 

  * [#401](/thread/post/8218124#post8218124 "Post Permalink")

  * Apr 21, 2015 4:58pm  Apr 21, 2015 4:58pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar92244_3.gif) pret](pret)

  * | Joined Jan 2009  | Status: Trader | [217 Posts](/search?do=process&provider=Member&searchuser=92244) | Online Now 

Thanks Skyline will post results later 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#402](/thread/post/8218385#post8218385 "Post Permalink")

  * Apr 21, 2015 6:13pm  Apr 21, 2015 6:13pm 

  * [ hashzar](hashzar)

  * | Joined Apr 2015  | Status: Trader | [186 Posts](/search?do=process&provider=Member&searchuser=408497)

Hi Skyline and everyone. I have been testing this EA only recently and I have it working only today on my [IC Markets](/brokers/ic-markets "View IC Markets Broker Profile") deomo account. It just closed a profitable trade. I was pleasantly surprised.. I will update future results / issues as I see them..  
  
Keep up the good work Skyline...  
  
HZ 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Profitable entry-exit.png
Size: 190 KB](/attachment/image/1658146/thumbnail?d=1429607310)](/attachment/image/1658146?d=1429607310)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#403](/thread/post/8218661#post8218661 "Post Permalink")

  * Apr 21, 2015 8:11pm  Apr 21, 2015 8:11pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar299111_1.gif) dimdel](dimdel)

  * Joined Oct 2012 | Status: Trader | [2,555 Posts](/search?do=process&provider=Member&searchuser=299111)

hi  
one stupid question  
  
i must have different number in each ea pair? or just drag in to the chart with no changes  
thanks 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#404](/thread/post/8219048#post8219048 "Post Permalink")

  * Apr 21, 2015 10:49pm  Apr 21, 2015 10:49pm 

  * [ Mariodrugs](mariodrugs)

  * | Membership Revoked  | Joined Dec 2014 | [379 Posts](/search?do=process&provider=Member&searchuser=394832)

Two looses today. GU and EU. -10 pips.  
![](https://resources.faireconomy.media/images/emojis/64/1f641.png?v=15.1)( still not working correctly EA .. ![](https://resources.faireconomy.media/images/emojis/64/1f641.png?v=15.1)  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Not working uea.png
Size: 273 KB](/attachment/image/1658398/thumbnail?d=1429624144)](/attachment/image/1658398?d=1429624144)   

  
  
and my 5 cents..  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: First level.png
Size: 97 KB](/attachment/image/1658399/thumbnail?d=1429624290)](/attachment/image/1658399?d=1429624290)   

  
  
=) 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#405](/thread/post/8219136#post8219136 "Post Permalink")

  * Apr 21, 2015 11:23pm  Apr 21, 2015 11:23pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting Mariodrugs](/thread/post/8219048#post8219048 "View Quoted Post")
> 
> Disliked
> 
> Two looses today. GU and EU. -10 pips. ![](https://resources.faireconomy.media/images/emojis/64/1f641.png?v=15.1)( still not working correctly EA .. ![](https://resources.faireconomy.media/images/emojis/64/1f641.png?v=15.1) {image} and my 5 cents.. {image} =)
> 
> Ignored

Hi Mariodrugs,  
i also took that losses on EU and GU (and a win on GJ) but what you noticed is wrong, in your case EA had worked fine ![](https://resources.faireconomy.media/images/emojis/64/1f644.png?v=15.1)  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: EA_workingfine.jpg
Size: 478 KB](/attachment/image/1658420/thumbnail?d=1429626095)](/attachment/image/1658420?d=1429626095)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#406](/thread/post/8219653#post8219653 "Post Permalink")

  * Apr 22, 2015 2:51am  Apr 22, 2015 2:51am 

  * [ hashzar](hashzar)

  * | Joined Apr 2015  | Status: Trader | [186 Posts](/search?do=process&provider=Member&searchuser=408497)

Ok, I too took a loss on the EU. It took about 27 minutes and the stop loss was hit. For this trade I had changed the EA to TP 8 pips / SL 15 pips to increase the odds.   
  
EA is running 24 hrs for all market hours and see how it works out with these TP and SL settings. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: EU lose.png
Size: 200 KB](/attachment/image/1658598/thumbnail?d=1429638313)](/attachment/image/1658598?d=1429638313)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#407](/thread/post/8219866#post8219866 "Post Permalink")

  * Apr 22, 2015 4:50am  Apr 22, 2015 4:50am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar350360_20.gif) AKCodingEye](akcodingeye)

  * Joined Sep 2013 | Status: Such a Silly Game It is | [181 Posts](/search?do=process&provider=Member&searchuser=350360)

I had two losses same for eu and GU today. Next trade whenever it takes must be +5 mathematically in order to have an edge. That's my view and watching for next trade. 

Whats get measured get improved

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#408](/thread/post/8220211#post8220211 "Post Permalink")

  * Apr 22, 2015 10:10am  Apr 22, 2015 10:10am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar325727_50.gif) iamgotzaa](iamgotzaa)

  * Joined Feb 2013 | Status: One step closer! | [765 Posts](/search?do=process&provider=Member&searchuser=325727)

I use to write these rules into mechanical ea.  
If you want, I can share the code I have.  
  
the ex4 file is here. [http://www.forexfactory.com/showthre...40#post7840640](http://www.forexfactory.com/showthread.php?p=7840640#post7840640)  
  
God bless, 

Holy grail, pls pm ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#409](/thread/post/8220509#post8220509 "Post Permalink")

  * Apr 22, 2015 3:17pm  Apr 22, 2015 3:17pm 

  * [ hashzar](hashzar)

  * | Joined Apr 2015  | Status: Trader | [186 Posts](/search?do=process&provider=Member&searchuser=408497)

Hi iamgotzaa, good to see you here. Was there any reason why you did not pursue your project further? What were your results? Any challenges?  
  
HZ 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#410](/thread/post/8220693#post8220693 "Post Permalink")

  * Apr 22, 2015 4:45pm  Apr 22, 2015 4:45pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

**[Mandatory Update v1.1.7]**  
* (bug fix) : fixed bug reported by Luy ([here](http://www.forexfactory.com/showthread.php?p=8215771#post8215771))  
* (bug fix) : fixed minor GUI issue related to LotSize which display multiple decimal digits in some cases.  
  
You can download it from 1st post as usual.  
  
Cheers,  
Skyline 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#411](/thread/post/8220740#post8220740 "Post Permalink")

  * Apr 22, 2015 5:06pm  Apr 22, 2015 5:06pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar388093_1.gif) firewight](firewight)

  * | Joined Oct 2014  | Status: Trader | [817 Posts](/search?do=process&provider=Member&searchuser=388093)

> [Quoting skyline](/thread/post/8220693#post8220693 "View Quoted Post")
> 
> Disliked
> 
> [Mandatory Update v1.1.7] * (bug fix) : fixed bug reported by Luy ([here](http://www.forexfactory.com/showthread.php?p=8215771#post8215771)) * (bug fix) : fixed minor GUI issue related to LotSize which display multiple decimal digits in some cases. You can download it from 1st post as usual. Cheers, Skyline
> 
> Ignored

Thanks mate, loading it now! 

Life is like a snickers, its full of nuts!

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#412](/thread/post/8220781#post8220781 "Post Permalink")

  * Apr 22, 2015 5:25pm  Apr 22, 2015 5:25pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar325727_50.gif) iamgotzaa](iamgotzaa)

  * Joined Feb 2013 | Status: One step closer! | [765 Posts](/search?do=process&provider=Member&searchuser=325727)

> [Quoting hashzar](/thread/post/8220509#post8220509 "View Quoted Post")
> 
> Disliked
> 
> Hi iamgotzaa, good to see you here. Was there any reason why you did not pursue your project further? What were your results? Any challenges? HZ
> 
> Ignored

Thanks for asking. well, i'm working on the new project, personally, that integrating economic news calendar in it. Afraid to share and then it fail. hahaha (actually I don't care) 

Holy grail, pls pm ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#413](/thread/post/8220784#post8220784 "Post Permalink")

  * Apr 22, 2015 5:26pm  Apr 22, 2015 5:26pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar325727_50.gif) iamgotzaa](iamgotzaa)

  * Joined Feb 2013 | Status: One step closer! | [765 Posts](/search?do=process&provider=Member&searchuser=325727)

> [Quoting skyline](/thread/post/8220693#post8220693 "View Quoted Post")
> 
> Disliked
> 
> [Mandatory Update v1.1.7] * (bug fix) : fixed bug reported by Luy ([here](http://www.forexfactory.com/showthread.php?p=8215771#post8215771)) * (bug fix) : fixed minor GUI issue related to LotSize which display multiple decimal digits in some cases. You can download it from 1st post as usual. Cheers, Skyline
> 
> Ignored

nice, let me try too. 

Holy grail, pls pm ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#414](/thread/post/8221000#post8221000 "Post Permalink")

  * Apr 22, 2015 6:43pm  Apr 22, 2015 6:43pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar11046_3.gif) chaveznqoos](chaveznqoos)

  * Joined Jun 2006 | Status: Trader | [450 Posts](/search?do=process&provider=Member&searchuser=11046)

> [Quoting skyline](/thread/post/8220693#post8220693 "View Quoted Post")
> 
> Disliked
> 
> [Mandatory Update v1.1.7] * (bug fix) : fixed bug reported by Luy ([here](http://www.forexfactory.com/showthread.php?p=8215771#post8215771)) * (bug fix) : fixed minor GUI issue related to LotSize which display multiple decimal digits in some cases. You can download it from 1st post as usual. Cheers, Skyline
> 
> Ignored

Hi skyline;  
  
Is there a version is possible, for all pairs, without sending orders, only to use it as an indicator?  
  
Thanks ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#415](/thread/post/8222427#post8222427 "Post Permalink")

  * Apr 23, 2015 3:52am  Apr 23, 2015 3:52am 

  * [ hashzar](hashzar)

  * | Joined Apr 2015  | Status: Trader | [186 Posts](/search?do=process&provider=Member&searchuser=408497)

> [Quoting iamgotzaa](/thread/post/8220781#post8220781 "View Quoted Post")
> 
> Disliked
> 
> {quote} Thanks for asking. well, i'm working on the new project, personally, that integrating economic news calendar in it. Afraid to share and then it fail. hahaha (actually I don't care)
> 
> Ignored

Hey iamgotzaa, there are no failures here, only feedback. Thank you for your contribution... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#416](/thread/post/8222663#post8222663 "Post Permalink")

  * Apr 23, 2015 7:06am  Apr 23, 2015 7:06am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar394157_1.gif) forexaz](forexaz)

  * | Joined Dec 2014  | Status: Trader | [321 Posts](/search?do=process&provider=Member&searchuser=394157)

> [Quoting iamgotzaa](/thread/post/8220781#post8220781 "View Quoted Post")
> 
> Disliked
> 
> {quote} Thanks for asking. well, i'm working on the new project, personally, that integrating economic news calendar in it. Afraid to share and then it fail. hahaha (actually I don't care)
> 
> Ignored

I would love to try it out ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#417](/thread/post/8224807#post8224807 "Post Permalink")

  * Apr 24, 2015 1:34am  Apr 24, 2015 1:34am 

  * [ leancuisine](leancuisine)

  * | Joined Jul 2014  | Status: Trader | [38 Posts](/search?do=process&provider=Member&searchuser=376648)

It's losing a lot of pips now, I wonder when it would turn around again. ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#418](/thread/post/8224857#post8224857 "Post Permalink")

  * Apr 24, 2015 2:04am  Apr 24, 2015 2:04am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting leancuisine](/thread/post/8224807#post8224807 "View Quoted Post")
> 
> Disliked
> 
> It's losing a lot of pips now, I wonder when it would turn around again. ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)
> 
> Ignored

it's the market, maybe tomorrow will be a better trading day ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#419](/thread/post/8224889#post8224889 "Post Permalink")

  * Apr 24, 2015 2:19am  Apr 24, 2015 2:19am 

  * [ DerBerliner](derberliner)

  * | Joined Feb 2011  | Status: Trader | [822 Posts](/search?do=process&provider=Member&searchuser=168827)

> [Quoting leancuisine](/thread/post/8224807#post8224807 "View Quoted Post")
> 
> Disliked
> 
> It's losing a lot of pips now, I wonder when it would turn around again. ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)
> 
> Ignored

Sure - it will turn around again, definitely ... may be even tomorrow ... yep, bevor going deeper again the day after tomorrow ... and the account will burst more sooner then later ...  
  
_IMHO_ it's impossible to win using this bot with a RR 2:1 .... only manually trading the 00level can bring gains, at least for some experienced tarders, having what ever additional tools .... ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)  
  
There is absolutly no offense against skyline ! I truly wish he could win using his bot ! But something must be changed ... haven't a clue what to do although ... unfortunately. ![](https://resources.faireconomy.media/images/emojis/64/1f647-200d-2642-fe0f.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#420](/thread/post/8225102#post8225102 "Post Permalink")

  * Apr 24, 2015 4:00am  Apr 24, 2015 4:00am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting DerBerliner](/thread/post/8224889#post8224889 "View Quoted Post")
> 
> Disliked
> 
> {quote} Sure - it will turn around again, definitely ... may be even tomorrow ... yep, bevor going deeper again the day after tomorrow ... and the account will burst more sooner then later ... IMHO it's impossible to win using this bot with a RR 2:1 .... only manually trading the 00level can bring gains, at least for some experienced tarders, having what ever additional tools .... ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1) There is absolutly no offense against skyline ! I truly wish he could win using his bot ! But something must be changed ... haven't a clue what to do although ... unfortunately....
> 
> Ignored

  
I completely agree, this ea will not gain any money in the long term. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * UdineEA Official Thread
  *   * [ **Reply to Thread** ](/thread/533099-udineea-official-thread/reply#reply)

  * More

[](https://www.forexfactory.com "Homepage")

  * [Forums](forums)
  * [Trades](trades)
  * [Calendar](calendar)
  * [News](news)
  * [Market](market)
  * [Brokers](brokers)

****

[](https://www.faireconomy.com/)

  * 

[The Official "Ok, now I'm pissed" Thread](/thread/73546-the-official-ok-now-im-pissed-thread "Hello Everyone, 
 
Seeing the apparent lack of threads of this nature \(just kidding, but read on\) I have decided to set up a respectable...") 51 replies

[Historic Charts: NZ Official Cash Rate](/thread/20380-historic-charts-nz-official-cash-rate "Sep 14, 2005") 15 replies

[Is there an official exchange rate?!](/thread/11571-is-there-an-official-exchange-rate "Different brokers have different bid and ask prices for every cross or pair.  However, the bid and ask price is based on something...I am...") 14 replies

[Official forex time zone](/thread/9940-official-forex-time-zone "is there a standard forex time zone? do i follow gmt or NY time? i use 4 hour charts and sometimes the time is way off because of time zone...") 3 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/533099-udineea-official-thread/reply#reply)
  * Subscribe
  * [100](javascript:void\(0\);)

Attachments: UdineEA Official Thread

Tags: UdineEA Official Thread

#  [](/thread/533099-udineea-official-thread)UdineEA Official Thread 

  * 

  * [#421](/thread/post/8225729#post8225729 "Post Permalink")

  * Apr 24, 2015 2:52pm  Apr 24, 2015 2:52pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar309469_3.gif) gigicualex](gigicualex)

  * | Joined Nov 2012  | Status: Trader | [1,187 Posts](/search?do=process&provider=Member&searchuser=309469)

> [Quoting skyline](/thread/post/8225102#post8225102 "View Quoted Post")
> 
> Disliked
> 
> {quote} I completely agree, this ea will not gain any money in the long term.
> 
> Ignored

Hi Skyline,  
  
Fully agree with you, so in this case why not reversing the trades, setting pending sell instead of buy stop?. Having also the RR 1:2 on our side.  
Think about it  
  
Cheers,  
G. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#422](/thread/post/8225757#post8225757 "Post Permalink")

  * Edited 6:58pm  Apr 24, 2015 3:26pm | Edited 6:58pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

Hi All,  
_I want**again** to state very clear that I'm not going to do ANY changes to the logic of UdineEA._  
  
**This is final version and will be not changed anymore (bugfix apart)**  
  
Take it or leave it.  
  
Thank You  
Skyline 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#423](/thread/post/8228922#post8228922 "Post Permalink")

  * Apr 27, 2015 2:12am  Apr 27, 2015 2:12am 

  * [ dlouw](dlouw)

  * | Joined Feb 2009  | Status: Trader | [136 Posts](/search?do=process&provider=Member&searchuser=94177)

Skyline,  
  
I am a bit confused here. You have done a tremendous amount of work to code the Udine00 system rules into an EA. I applaud you for this effort.  
  
Then you say that you agree it will not make any money in the long term. OK, then you believe there are obviously some discretionary factors in the Udine00 system that are not included in your code. I agree. It seems that if you will not make modifications or release MT4 code to allow others to make modifications the whole project will only establish that the base rules are a win/ no win scenario. What am I missing here? How do you propose to test and identify these factors in a scientific manor if there are no variations or ability to record other data factors with the trades?  
  
Respectfully,  
dlouw 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#424](/thread/post/8228983#post8228983 "Post Permalink")

  * Apr 27, 2015 4:13am  Apr 27, 2015 4:13am 

  * [ DerBerliner](derberliner)

  * | Joined Feb 2011  | Status: Trader | [822 Posts](/search?do=process&provider=Member&searchuser=168827)

@dlouw  
  
Yes man - you hit the bull's eye ! ![](https://resources.faireconomy.media/images/emojis/64/1f61f.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#425](/thread/post/8229082#post8229082 "Post Permalink")

  * Apr 27, 2015 6:10am  Apr 27, 2015 6:10am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

Hi dlouw,  
let's start from the begin....  
  
I approached Udine strategy method starting to study his thread, I soon realized that a lot of discrectionality were involved so I stopped at level 1 rules which was 'quite' easy to be turned into an EA, also because I don't had the time to place and babysit trades due to my daily job. Then someone asked me to share this EA for all and I did.  
  
The plain and simple truth is that all of Udine's rules cannot be coded into an EA just because there's too much discrectionality involved, while an EA needs some mathematical and fixed rules that can be coded using Mql language.  
  
By the way after a good start with some positive trades, UdineEA hits some bad trades (now we are in a drawdown period in my demo account), so users like you started to yell asking to 'filter', to add 'things' , to do this or do that..., based on what ? On nothing , just because there were some losing trades in a row.  
  
So Dlouw do you think that I'm here to code whatever 'idea' comes around just because seems nice to be coded or because there is a losing streak? Forget it !  
  
Moreover, where did I wrote that I intend to code 'discretional' Udine rules ? This is UdineEA level1 rules thread not UdineEA all rules thread, i've never thought to do something like that also because as i said before is simply impossible to do.  
  
UdineEA logic code phase, as far as I'm concerned, is done; I released live version so now we can only test it as is for at least 1 year (or 500+ trades) to gather some statistical evidence.  
  
I'm quite sure this EA will not gain money in the long run , maybe I'm wrong who knows ? The only way to verify this is by testing it as is in live not by changing it (otherwise you have to start again and again your live test)  
  
I'm sorry if you, or others, are not comfortable with this, you can always start to code your UdineEA and do whatever you want with it, share your code, add filters, and so on....  
  
Regards,  
Skyline 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#426](/thread/post/8230831#post8230831 "Post Permalink")

  * Apr 28, 2015 4:38am  Apr 28, 2015 4:38am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1024_7.gif) diallist](diallist)

  * Joined Sep 2004 | Status: Trader | [1,464 Posts](/search?do=process&provider=Member&searchuser=1024)

> [Quoting dlouw](/thread/post/8228922#post8228922 "View Quoted Post")
> 
> Disliked
> 
> Skyline, I am a bit confused here. You have done a tremendous amount of work to code the Udine00 system rules into an EA. I applaud you for this effort. Then you say that you agree it will not make any money in the long term. OK, then you believe there are obviously some discretionary factors in the Udine00 system that are not included in your code. I agree. It seems that if you will not make modifications or release MT4 code to allow others to make modifications the whole project will only establish that the base rules are a win/ no win scenario....
> 
> Ignored

Hi dlouw, it is always refreshing for me to read a post that is both intelligent and eloquent. I wish more people had your facility with language!  
  
That aside, while I understand what you are saying and requesting, given that skyline has chosen (as is his right) to make no more changes and will not release the source code, then it only remains to make use of the EA as a teacher to help us see the very discretionary elements of which you speak. Let the EA run, and then keep a log of all the losing trades and note, when possible, identifiable reasons not to have taken that losing trade. It might be due to SR or Pivots or Fibonacci levels, or channels or any myriad of other things. If enough data is gathered, in an ordered and scientific fashion, then you would then have a very valuable set of reasons not to take trades when trading L1 trades manually. Udine puts it succinctly: "If you don't see a reason to stay out, then take the trade!" Which implies that if you see any reason, or even think you see a reason, then it is better to stay out of the trade.  
  
In summary, since no EA changes are forthcoming, then make use of the EA as a grand teacher.  
  
Dial  
  
P.S. BTW, I am impressed with skyline because he is one of the few people I know who truly understands how trading works and why adding extra filters almost always results in worse trading, and begins a cycle of filter on filter on filter etc. 

sxaxlxvxaxtxixoxnxbxyxgxrxaxcxexdxoxtxoxrxgx

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#427](/thread/post/8233488#post8233488 "Post Permalink")

  * Apr 29, 2015 7:53am  Apr 29, 2015 7:53am 

  * [ dlouw](dlouw)

  * | Joined Feb 2009  | Status: Trader | [136 Posts](/search?do=process&provider=Member&searchuser=94177)

skyline, Please no offense intended. I have a great interest in your work here. I would love to be able to code this myself from scratch. Alas my coding skills are in the rank beginner stages and I am relegated to rely on those with superior skills such as yourself. ![](https://resources.faireconomy.media/images/emojis/64/1f647-200d-2642-fe0f.png?v=15.1) I can only hack existing code to a degree at this time. By standing on the shoulders of those who have traveled this road the view is much clearer. That being said the idea of having a EA that can monitor the System is very appealing to my selfish side. You see, here in Oregon the London session opens at 12:00 AM and NY at 4:00 PM. It is difficult for me to monitor any of the other discretionary variables and contribute value to your efforts without a significant loss of sleep.  
  
All this being said your position is understood and respected. I thank you for your contribution and will look forward to the knowledge gained by this endeavor.  
  
And daillist, I sincerely hope that I can make an impact on these forums as eloquent and positive as your own. You contributions are a credit to traders and humanity. Thank you.  
  
Green Pips and All the Best,  
dlouw 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#428](/thread/post/8233953#post8233953 "Post Permalink")

  * Apr 29, 2015 4:36pm  Apr 29, 2015 4:36pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

HI dlouw,  
ty for your kind reply.  
I see a lot of you like to explore further deeply Udine strategy to evaluate and try to automatize all rules involved but that's wasn't my intention when I started this thread; I do not have the time nor the will to deeply analyze possible evolution of this strategy.  
  
Maybe in future I could share a lite version with source code with just entry rules coded so that it could be further developed if someone want to.  
  
Regards,  
Skyline 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#429](/thread/post/8234061#post8234061 "Post Permalink")

  * Apr 29, 2015 5:20pm  Apr 29, 2015 5:20pm 

  * [ rmndschmidt](rmndschmidt)

  * | Joined Mar 2014  | Status: Trader | [42 Posts](/search?do=process&provider=Member&searchuser=365689)

Hello skyline,  
I test also your EA and I write from a neutral point of view, because that's not my focus. If dlouw the EA would like to develop: Please give him a chance and share the code with him! It is then possible to test both EA's and that can only be positive but not harm anyone. I hope dlouw would his EA then also share here with all.  
Best regards  
Raimund 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#430](/thread/post/8234309#post8234309 "Post Permalink")

  * Apr 29, 2015 7:16pm  Apr 29, 2015 7:16pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar298742_5.gif) bluejack](bluejack)

  * | Joined Oct 2012  | Status: Trader | [493 Posts](/search?do=process&provider=Member&searchuser=298742)

Anyone tried with different TP and SL? I have been testing with various SL and TP. Right now i have 30 SL and 300 TP running with 20 TS. London only - false.   
  
[http://www.myfxbook.com/members/blue...ine-ea/1211489](http://www.myfxbook.com/members/bluejack/long-range-trades-udine-ea/1211489)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#431](/thread/post/8234376#post8234376 "Post Permalink")

  * Apr 29, 2015 7:47pm  Apr 29, 2015 7:47pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar350360_20.gif) AKCodingEye](akcodingeye)

  * Joined Sep 2013 | Status: Such a Silly Game It is | [181 Posts](/search?do=process&provider=Member&searchuser=350360)

> [Quoting dlouw](/thread/post/8228922#post8228922 "View Quoted Post")
> 
> Disliked
> 
> Skyline, I am a bit confused here. You have done a tremendous amount of work to code the Udine00 system rules into an EA. I applaud you for this effort. Then you say that you agree it will not make any money in the long term. OK, then you believe there are obviously some discretionary factors in the Udine00 system that are not included in your code. I agree. It seems that if you will not make modifications or release MT4 code to allow others to make modifications the whole project will only establish that the base rules are a win/ no win scenario....
> 
> Ignored

I am totally with you on this. Skyline is right from his side as well. What Skyline shared with us is more than enough![](https://resources.faireconomy.media/images/emojis/64/1f647-200d-2642-fe0f.png?v=15.1). i was frustrated at one stage when i saw potential in this EA but can't do anything. I tried to PM you to give you direction so you make your own way like me as i don't want to disturb flow here. Looks like your PM is turned off. 

Whats get measured get improved

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#432](/thread/post/8235278#post8235278 "Post Permalink")

  * Apr 30, 2015 12:36am  Apr 30, 2015 12:36am 

  * [ Maxlor](maxlor)

  * | Joined Apr 2015  | Status: Trader | [2 Posts](/search?do=process&provider=Member&searchuser=408736)

I'm sorry Skyline, I'm a new member in this forum.  
I'm testing the new version UdineEA V1.1.7 to last week.  
It seems to be a great project and so far has been positive .  
I saw , however, that the trailing stop does not work and always causes a closure to BREAK EVEN.  
is it the fault of the broker ? I use [Pepperstone](/brokers/pepperstone "View Pepperstone Broker Profile") .  
thanks 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#433](/thread/post/8235563#post8235563 "Post Permalink")

  * Apr 30, 2015 2:47am  Apr 30, 2015 2:47am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar53444_2.gif) dagoods](dagoods)

  * Joined Nov 2007 | Status: Trader | [3,059 Posts](/search?do=process&provider=Member&searchuser=53444)

> [Quoting skyline](/thread/post/8233953#post8233953 "View Quoted Post")
> 
> Disliked
> 
> HI dlouw, ty for your kind reply. I see a lot of you like to explore further deeply Udine strategy to evaluate and try to automatize all rules involved but that's wasn't my intention when I started this thread; I do not have the time nor the will to deeply analyze possible evolution of this strategy. Maybe in future _I could share a lite version with source code with just entry rules coded so that it could be further developed if someone want to._ Regards, Skyline
> 
> Ignored

  
Thanks for your consideration! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#434](/thread/post/8235662#post8235662 "Post Permalink")

  * Apr 30, 2015 3:13am  Apr 30, 2015 3:13am 

  * [ dlouw](dlouw)

  * | Joined Feb 2009  | Status: Trader | [136 Posts](/search?do=process&provider=Member&searchuser=94177)

Thank you for the consideration skyline.  
  
My PM is on now ![](https://resources.faireconomy.media/images/emojis/64/1f61e.png?v=15.1).  
  
Warmest Regards,  
dlouw 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#435](/thread/post/8248278#post8248278 "Post Permalink")

  * May 7, 2015 1:50am  May 7, 2015 1:50am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar396980_1.gif) thevarkoon](thevarkoon)

  * | Joined Jan 2015  | Status: Trader | [7 Posts](/search?do=process&provider=Member&searchuser=396980)

Hi,  
  
Anyone still running the UdineEA ?  
  
Had one winning trade today on EJ  
  
Is the EA still running in the Trade manager ? Dont see any trades apear.  
  
Hope this thread doesn't die.  
  
Cheers  
  
Thevarkoon 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#436](/thread/post/8248675#post8248675 "Post Permalink")

  * May 7, 2015 6:08am  May 7, 2015 6:08am 

  * [ leancuisine](leancuisine)

  * | Joined Jul 2014  | Status: Trader | [38 Posts](/search?do=process&provider=Member&searchuser=376648)

> [Quoting thevarkoon](/thread/post/8248278#post8248278 "View Quoted Post")
> 
> Disliked
> 
> Hi, Anyone still running the UdineEA ? Had one winning trade today on EJ Is the EA still running in the Trade manager ? Dont see any trades apear. Hope this thread doesn't die. Cheers Thevarkoon
> 
> Ignored

I actually got four trades today, two GBP/JPY were losers, and GBP/USD and EUR/JPY being winners. ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#437](/thread/post/8250765#post8250765 "Post Permalink")

  * May 8, 2015 3:18am  May 8, 2015 3:18am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar396980_1.gif) thevarkoon](thevarkoon)

  * | Joined Jan 2015  | Status: Trader | [7 Posts](/search?do=process&provider=Member&searchuser=396980)

Hi all,  
  
2 winners 2day  
  
EJ + EU  
  
Cheers  
  
Thevarkoon 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#438](/thread/post/8293206#post8293206 "Post Permalink")

  * May 30, 2015 6:00pm  May 30, 2015 6:00pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

**[Published in first post latest version v1.1.8]**  
  
* (feature) Removed time limit , UdineEA will work forever  
  
_Do not ask for changes/improve/optimizazion/whatever to UdineEA, this is final version and in final testing live stage, I no longer modify its code._

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#439](/thread/post/8325755#post8325755 "Post Permalink")

  * Jun 15, 2015 8:29am  Jun 15, 2015 8:29am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar339829_1.gif) chayon](chayon)

  * | Joined Jun 2013  | Status: Trader | [37 Posts](/search?do=process&provider=Member&searchuser=339829)

> [Quoting skyline](/thread/post/8229082#post8229082 "View Quoted Post")
> 
> Disliked
> 
> Hi dlouw, let's start from the begin.... I approached Udine strategy method starting to study his thread, I soon realized that a lot of discrectionality were involved so I stopped at level 1 rules which was 'quite' easy to be turned into an EA, also because I don't had the time to place and babysit trades due to my daily job. Then someone asked me to share this EA for all and I did. The plain and simple truth is that all of Udine's rules cannot be coded into an EA just because there's too much discrectionality involved, while an EA needs some mathematical...
> 
> Ignored

and so on still in a healthy drawdown 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#440](/thread/post/8326087#post8326087 "Post Permalink")

  * Jun 15, 2015 3:19pm  Jun 15, 2015 3:19pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting chayon](/thread/post/8325755#post8325755 "View Quoted Post")
> 
> Disliked
> 
> {quote} and so on still in a healthy drawdown
> 
> Ignored

and so what do you want exactly ? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * UdineEA Official Thread
  *   * [ **Reply to Thread** ](/thread/533099-udineea-official-thread/reply#reply)

  * More

[](https://www.forexfactory.com "Homepage")

  * [Forums](forums)
  * [Trades](trades)
  * [Calendar](calendar)
  * [News](news)
  * [Market](market)
  * [Brokers](brokers)

****

[](https://www.faireconomy.com/)

  * 

[The Official "Ok, now I'm pissed" Thread](/thread/73546-the-official-ok-now-im-pissed-thread "Hello Everyone, 
 
Seeing the apparent lack of threads of this nature \(just kidding, but read on\) I have decided to set up a respectable...") 51 replies

[Historic Charts: NZ Official Cash Rate](/thread/20380-historic-charts-nz-official-cash-rate "Sep 14, 2005") 15 replies

[Is there an official exchange rate?!](/thread/11571-is-there-an-official-exchange-rate "Different brokers have different bid and ask prices for every cross or pair.  However, the bid and ask price is based on something...I am...") 14 replies

[Official forex time zone](/thread/9940-official-forex-time-zone "is there a standard forex time zone? do i follow gmt or NY time? i use 4 hour charts and sometimes the time is way off because of time zone...") 3 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/533099-udineea-official-thread/reply#reply)
  * Subscribe
  * [100](javascript:void\(0\);)

Attachments: UdineEA Official Thread

Tags: UdineEA Official Thread

#  [](/thread/533099-udineea-official-thread)UdineEA Official Thread 

  * 

  * [#441](/thread/post/8327094#post8327094 "Post Permalink")

  * Jun 15, 2015 11:47pm  Jun 15, 2015 11:47pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar298742_5.gif) bluejack](bluejack)

  * | Joined Oct 2012  | Status: Trader | [493 Posts](/search?do=process&provider=Member&searchuser=298742)

Hi Skyline,  
Thanks a lot for your efforts. The EA is giving good results with 10 SL and 50 TP. I have 20 pip trailing, but the trailing option is working as "Break Even" instead of trailing the profit. I could be wrong. Can you please check? Thanks in advance.  
  
Bluejack 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#442](/thread/post/8329581#post8329581 "Post Permalink")

  * Jun 16, 2015 11:51pm  Jun 16, 2015 11:51pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting bluejack](/thread/post/8327094#post8327094 "View Quoted Post")
> 
> Disliked
> 
> Hi Skyline, Thanks a lot for your efforts. The EA is giving good results with 10 SL and 50 TP. I have 20 pip trailing, but the trailing option is working as "Break Even" instead of trailing the profit. I could be wrong. Can you please check? Thanks in advance. Bluejack
> 
> Ignored

Hi BlueJack,  
trailing stop internal mechanism has been coded based on Wukar EA used in Udine's thread, so that when profit reach TrailingStop value (deafult 3.5 pips) then stoploss is set to breakeven.  
Hope this answer your question.  
  
Regards,  
Skyline 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#443](/thread/post/8331682#post8331682 "Post Permalink")

  * Jun 17, 2015 11:38pm  Jun 17, 2015 11:38pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar298742_5.gif) bluejack](bluejack)

  * | Joined Oct 2012  | Status: Trader | [493 Posts](/search?do=process&provider=Member&searchuser=298742)

> [Quoting skyline](/thread/post/8329581#post8329581 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi BlueJack, trailing stop internal mechanism has been coded based on Wukar EA used in Udine's thread, so that when profit reach TrailingStop value (deafult 3.5 pips) then stoploss is set to breakeven. Hope this answer your question. Regards, Skyline
> 
> Ignored

Skyline,  
Thank You. ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#444](/thread/post/8338859#post8338859 "Post Permalink")

  * Jun 22, 2015 2:07pm  Jun 22, 2015 2:07pm 

  * [ nghuuthanh](nghuuthanh)

  * | Joined Dec 2012  | Status: Trader | [4 Posts](/search?do=process&provider=Member&searchuser=318764)

Dear Skyline  
  
Thank you very much for your effort and sharing the EA.  
Your work is always appreciated.  
  
Have good health to continue your work and giving us good Forex EA.  
  
Thanks and Best regards, 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#445](/thread/post/8390788#post8390788 "Post Permalink")

  * Jul 21, 2015 12:52am  Jul 21, 2015 12:52am 

  * [ Bullilulli](bullilulli)

  * | Joined Jul 2015  | Status: Trader | [83 Posts](/search?do=process&provider=Member&searchuser=419042)

> [Quoting bluejack](/thread/post/8327094#post8327094 "View Quoted Post")
> 
> Disliked
> 
> The EA is giving good results with 10 SL and 50 TP.
> 
> Ignored

Hello BlueJack,  
may I ask you what this means in numbers? Would you please enlighten me?  
Thanks in advance and a lot of green pips 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#446](/thread/post/8450202#post8450202 "Post Permalink")

  * Aug 23, 2015 4:40am  Aug 23, 2015 4:40am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

After six months of use in the demo it is clear that this EA as expected will never be profitable.  
The situation, however, changes dramatically if EA had removed the TP by setting it to 0 (so that trades will never be closed in profit but only at B/E or they run undefinitely), completely changing the initial idea behind original Udine's trading system.  
What I have infact carried out, on the basis of trades accounted in mt4 history tab, is to consider trades as it were taken with TP = 0 and SL = 10; in particular if a trade was closed at 5 pips in profit I considered it as if it had been closed at breakeven unless price never went to breakeven point (remember that Udine EA trail sl to be when 3,5 pips profit is reached for each order placed so at +5 pips we are sure sl is already at be).  
  
The results of my experiment are quite interesting, I summarize them here:  
  
[GBPJPY]  
41 trades B / E  
19 Loss trades (-190 pips)  
1 Trade still running (around 680 pips profit floating)  
  
[EURJPY]  
56 trades B / E  
26 Loss trades (-260 pips)  
3 trades still running (around 2090 pips floating profit)  
  
[GBPUSD]  
50 trades B / E  
13 Loss trades (-130 pips)  
1 trade still running (around 790 pips profit floating)  
  
[EURUSD]  
62 trades B / E  
18 Loss trades (-180 pips)  
1 trade still running (around 240 pips profit floating)  
  
where for each loss I considered 10 pips (SL = 10) and in total we would have:  
  
Tot Lost pips: -580 (commission costs not accounted)  
Tot Unrealized pips: +3560  
  
so around +3000 pips (less commisson costs) of unrealized profit from trading this Udine EA by simply removing TP, with still 6 trades alive and running for further more higher potential profit. On other hand i see in my experiment that there was some trades which also went up in profit (> 500 pips) then went back to b/e so partial profit could also have taken for a much better final result.  
  
Obviously, this approach involves the use of very tiny lot size otherwise drawdown could be too deep to be able to recover (absolutely too much high 4% per trade!! Maybe 0.5% per trade or a (low) fixed lot size is the best approach for this method.  
  
And what about running trades ? They are not managed by Udine EA so it would be the trader to take care of them and eventually at some point close some of it to replenish balance and smooth equity curve (for more reference study deeply [Millipede thread](http://www.forexfactory.com/showthread.php?t=245149) by Pipeasy)  
  
All of this once again proves, if proof were needed again, that the approach to limit losses and let profits run is the way to go.  
  
Greetings,  
Skyline 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#447](/thread/post/8450357#post8450357 "Post Permalink")

  * Aug 23, 2015 12:36pm  Aug 23, 2015 12:36pm 

  * [ cjtylor](cjtylor)

  * | Joined Jan 2015  | Status: Trader | [170 Posts](/search?do=process&provider=Member&searchuser=395076)

> [Quoting skyline](/thread/post/8450202#post8450202 "View Quoted Post")
> 
> Disliked
> 
> After six months of use in the demo it is clear that this EA as expected will never be profitable. The situation, however, changes dramatically if EA had removed the TP by setting it to 0 (so that trades will never be closed in profit but only at B/E or they run undefinitely), completely changing the initial idea behind original Udine's trading system. What I have infact carried out, on the basis of trades accounted in mt4 history tab, is to consider trades as it were taken with TP = 0 and SL = 10; in particular if a trade was closed at 5 pips in...
> 
> Ignored

Hi Skyline, great that you come back again!!  
Not sure i have understand you correctly - so you adjusted your trades by assuming the TP =0 / SL = 10, and re-calculate the pips - it turns out TP=0 will give us about 3000 pips.  
in this case, that will be a great news.  
  
Also, btw, for your EA118, is there a way to backtest it - i am not able to because it tries to read the FF Cal news...  
  
Appreciate your thoughts ! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#448](/thread/post/8450455#post8450455 "Post Permalink")

  * Aug 23, 2015 5:13pm  Aug 23, 2015 5:13pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting cjtylor](/thread/post/8450357#post8450357 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi Skyline, great that you come back again!! Not sure i have understand you correctly - so you adjusted your trades by assuming the TP =0 / SL = 10, and re-calculate the pips - it turns out TP=0 will give us about 3000 pips. in this case, that will be a great news. Also, btw, for your EA118, is there a way to backtest it - i am not able to because it tries to read the FF Cal news... Appreciate your thoughts !
> 
> Ignored

Hi Cjtylor, yes that's exactly what I did, it's a sort of backtest on trades already closed just to see different scenario and different outcomes. It's an interesting try that every trader should do, go in history of you account and take note of all trades taken , you will find very few trades that never come back to open price nor touched stoploss running for hundred or more pips.  
Of course this experiment should be tried in real live market to draw some conclusion, infact i'm planning to open a tiny live account to try out this variation of Udine EA trading with 0.01 lot using an ECN broker with low spread. Btw I'll attach a trade explorer of this new real live test as soon as it's ready.  
  
Unfortunately UdineEA , as stated in 1st post here, cannot be backtested because news filter cannot be simulated , this is why I never trusted it since it was impossible for me to do a deep analysis on statistical behaviour.  
  
Regards,  
Skyline 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#449](/thread/post/8450687#post8450687 "Post Permalink")

  * Aug 23, 2015 11:22pm  Aug 23, 2015 11:22pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar350360_20.gif) AKCodingEye](akcodingeye)

  * Joined Sep 2013 | Status: Such a Silly Game It is | [181 Posts](/search?do=process&provider=Member&searchuser=350360)

Hi Skyline and All  
  
I have just created [FXCM](/brokers/fxcm "View FXCM Broker Profile")-TE-Demo-Public with all default settings except TP:0 and RiskperTrade: 1% as Skyline mentioned earlier for TP.  
Let's see how it performs  
  
\--AK-- 

Whats get measured get improved

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#450](/thread/post/8450692#post8450692 "Post Permalink")

  * Aug 23, 2015 11:30pm  Aug 23, 2015 11:30pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting AKCodingEye](/thread/post/8450687#post8450687 "View Quoted Post")
> 
> Disliked
> 
> Hi Skyline and All I have just created FXCM-TE-Demo-Public with all default settings except TP:0 and RiskperTrade: 1% as Skyline mentioned earlier for TP. Let's see how it performs --AK--
> 
> Ignored

Hi AKCodingEye,  
I've setup a real account using 0.01 lot (min lot size allowed in my account), I think 1% risk per trade could be too much to go through drawdown.  
Btw you have to be very very patient to trade like this suffering B/E trades and losses trade after trade for prolonged period. ![](https://resources.faireconomy.media/images/emojis/64/1f641.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#451](/thread/post/8451511#post8451511 "Post Permalink")

  * Aug 24, 2015 1:24pm  Aug 24, 2015 1:24pm 

  * [ cjtylor](cjtylor)

  * | Joined Jan 2015  | Status: Trader | [170 Posts](/search?do=process&provider=Member&searchuser=395076)

> [Quoting skyline](/thread/post/8450692#post8450692 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi AKCodingEye, I've setup a real account using 0.01 lot (min lot size allowed in my account), I think 1% risk per trade could be too much to go through drawdown. Btw you have to be very very patient to trade like this suffering B/E trades and losses trade after trade for prolonged period. ![](https://resources.faireconomy.media/images/emojis/64/1f641.png?v=15.1)
> 
> Ignored

Hi Skyline,   
do you have a trade explorer for this?  
  
Also i have forward test-ed your ea previous but somehow it does not open an trade for a week - i am bit surprise.\  
On avg, how many trades do it open in your case?  
  
Green pips to you...! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#452](/thread/post/8451731#post8451731 "Post Permalink")

  * Edited 4:55pm  Aug 24, 2015 3:47pm | Edited 4:55pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting cjtylor](/thread/post/8451511#post8451511 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi Skyline, do you have a trade explorer for this? Also i have forward test-ed your ea previous but somehow it does not open an trade for a week - i am bit surprise.\ On avg, how many trades do it open in your case? Green pips to you...!
> 
> Ignored

Yes i've just created trade explorer but yet no trade opened.  
  
Trades opened per week are not so much due to a lot of filters , btw 2/3 trades/weeks for each pair in average should be opened by UdineEA  
Please recheck if everything is set correctly in your platform.  
  
Regards,  
Skyline 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#453](/thread/post/8452387#post8452387 "Post Permalink")

  * Aug 24, 2015 8:49pm  Aug 24, 2015 8:49pm 

  * [ cjtylor](cjtylor)

  * | Joined Jan 2015  | Status: Trader | [170 Posts](/search?do=process&provider=Member&searchuser=395076)

> [Quoting skyline](/thread/post/8451731#post8451731 "View Quoted Post")
> 
> Disliked
> 
> {quote} Yes i've just created trade explorer but yet no trade opened. Trades opened per week are not so much due to a lot of filters , btw 2/3 trades/weeks for each pair in average should be opened by UdineEA Please recheck if everything is set correctly in your platform. Regards, Skyline
> 
> Ignored

Hi Skyline,  
it tried to open trades today but there is 2 error occured..  
1\. Pending order deleted because it's not triggered on M30 Candle --> i actually put EA on M30, do you know why this happend?  
  
2\. Set StopLoss Long Invalid trade parameter.  
Could you help to see what i did wrong?  
Green pips to you! 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screen Shot 2015-08-24 at 7.48.25 PM.png
Size: 99 KB](/attachment/image/1739014/thumbnail?d=1440416934)](/attachment/image/1739014?d=1440416934)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#454](/thread/post/8452420#post8452420 "Post Permalink")

  * Aug 24, 2015 8:57pm  Aug 24, 2015 8:57pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting cjtylor](/thread/post/8452387#post8452387 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi Skyline, it tried to open trades today but there is 2 error occured.. 1. Pending order deleted because it's not triggered on M30 Candle --> i actually put EA on M30, do you know why this happend? 2. Set StopLoss Long Invalid trade parameter. Could you help to see what i did wrong? Green pips to you! {image}
> 
> Ignored

  
Hi Cjtylor,  
first one is not an error , is simply a text log added by me to see when a pending order is deleted by EA since pending order was not triggered at the end of current M30 candle.  
The other one seems to be some issue related to your broker maybe some issue on platform when trade was placed.  
  
Cheers,  
Skyline 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#455](/thread/post/8482779#post8482779 "Post Permalink")

  * Sep 11, 2015 2:08am  Sep 11, 2015 2:08am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar11046_3.gif) chaveznqoos](chaveznqoos)

  * Joined Jun 2006 | Status: Trader | [450 Posts](/search?do=process&provider=Member&searchuser=11046)

> [Quoting skyline](/thread/post/8451731#post8451731 "View Quoted Post")
> 
> Disliked
> 
> {quote} Yes i've just created trade explorer but yet no trade opened. Trades opened per week are not so much due to a lot of filters , btw 2/3 trades/weeks for each pair in average should be opened by UdineEA Please recheck if everything is set correctly in your platform. Regards, Skyline
> 
> Ignored

Hi skyline;  
  
Good entry into EURJPY, patience is the key...![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)  
  
I have a few doubts about the expert;  
  
Do you use the last V118?  
A part of BE, TP and SL, the other parameters are default?  
Thanks 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#456](/thread/post/8482814#post8482814 "Post Permalink")

  * Sep 11, 2015 2:31am  Sep 11, 2015 2:31am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting chaveznqoos](/thread/post/8482779#post8482779 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi skyline; Good entry into EURJPY, patience is the key...![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1) I have a few doubts about the expert; Do you use the last V118? A part of BE, TP and SL, the other parameters are default? Thanks
> 
> Ignored

Hi chavenznqoos,  
yes i'm testing it latest v1.18 on demo account with default parameters.  
But if you look at trade explorer is clear that this EA doesn't have any edge, it's very dangerous to be used in live trading account, so be very carefull.  
  
Regards,  
Skyline 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#457](/thread/post/8482836#post8482836 "Post Permalink")

  * Sep 11, 2015 2:41am  Sep 11, 2015 2:41am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar11046_3.gif) chaveznqoos](chaveznqoos)

  * Joined Jun 2006 | Status: Trader | [450 Posts](/search?do=process&provider=Member&searchuser=11046)

> [Quoting skyline](/thread/post/8482814#post8482814 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi chavenznqoos, yes i'm testing it latest v1.18 on demo account with default parameters. But if you look at trade explorer is clear that this EA doesn't have any edge, it's very dangerous to be used in live trading account, so be very carefull. Regards, Skyline
> 
> Ignored

But I mean your "Live Udine no TP".It is not based on your last change, with 0,001, SL = 20, BE = 5 and TP = 0?  
Forgive my ignorance ![](https://resources.faireconomy.media/images/emojis/64/1f61e.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#458](/thread/post/8482889#post8482889 "Post Permalink")

  * Edited 3:46am  Sep 11, 2015 3:21am | Edited 3:46am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting chaveznqoos](/thread/post/8482836#post8482836 "View Quoted Post")
> 
> Disliked
> 
> {quote} But I mean your "Live Udine no TP".It is not based on your last change, with 0,001, SL = 20, BE = 5 and TP = 0? Forgive my ignorance ![](https://resources.faireconomy.media/images/emojis/64/1f61e.png?v=15.1)
> 
> Ignored

Ops sorry I've misunderstand your question, yes i'm using it with SL = 10 , BE 5 and TP = 0 , actually I have only one runner in EJ around 140 pips in profit ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1) But in the meantime there was a lot of trades closed at B/E or in loss , so it's still not in profit.  
  
Regards,  
Skyline 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#459](/thread/post/8493411#post8493411 "Post Permalink")

  * Sep 17, 2015 3:26pm  Sep 17, 2015 3:26pm 

  * [ cjtylor](cjtylor)

  * | Joined Jan 2015  | Status: Trader | [170 Posts](/search?do=process&provider=Member&searchuser=395076)

> [Quoting skyline](/thread/post/8482889#post8482889 "View Quoted Post")
> 
> Disliked
> 
> {quote} Ops sorry I've misunderstand your question, yes i'm using it with SL = 10 , BE 5 and TP = 0 , actually I have only one runner in EJ around 140 pips in profit ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1) But in the meantime there was a lot of trades closed at B/E or in loss , so it's still not in profit. Regards, Skyline
> 
> Ignored

hi Skyline, time flies - one month now - how is your forward testing now? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#460](/thread/post/8493427#post8493427 "Post Permalink")

  * Sep 17, 2015 3:39pm  Sep 17, 2015 3:39pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

Hi Cjtylor,  
I've discontinued Demo Udine EA that you can see in Trade Explorer (will remove soon from there) since is it obvious that this EA is not profitable.  
Speaking about the live account running without any TP set, actually I have only one position opened on EJ long @134.70 so around 180 pips right now in floating profit but a lot of other positions closed in loss or at B/E. There would need to catch some other big move so that equity will start to go in positive territory.  
Numbers in my account :  
  
Balance : -8.27%  
Equity : +7.14%  
  
Will attach soon a new Trade Explorer related to this live account ! ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)  
  
Cheers,  
Skyline 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * UdineEA Official Thread
  *   * [ **Reply to Thread** ](/thread/533099-udineea-official-thread/reply#reply)

  * More

[](https://www.forexfactory.com "Homepage")

  * [Forums](forums)
  * [Trades](trades)
  * [Calendar](calendar)
  * [News](news)
  * [Market](market)
  * [Brokers](brokers)

****

[](https://www.faireconomy.com/)

  * 

[The Official "Ok, now I'm pissed" Thread](/thread/73546-the-official-ok-now-im-pissed-thread "Hello Everyone, 
 
Seeing the apparent lack of threads of this nature \(just kidding, but read on\) I have decided to set up a respectable...") 51 replies

[Historic Charts: NZ Official Cash Rate](/thread/20380-historic-charts-nz-official-cash-rate "Sep 14, 2005") 15 replies

[Is there an official exchange rate?!](/thread/11571-is-there-an-official-exchange-rate "Different brokers have different bid and ask prices for every cross or pair.  However, the bid and ask price is based on something...I am...") 14 replies

[Official forex time zone](/thread/9940-official-forex-time-zone "is there a standard forex time zone? do i follow gmt or NY time? i use 4 hour charts and sometimes the time is way off because of time zone...") 3 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/533099-udineea-official-thread/reply#reply)
  * Subscribe
  * [100](javascript:void\(0\);)

Attachments: UdineEA Official Thread

Tags: UdineEA Official Thread

#  [](/thread/533099-udineea-official-thread)UdineEA Official Thread 

  * 

  * [#461](/thread/post/8494076#post8494076 "Post Permalink")

  * Sep 17, 2015 9:21pm  Sep 17, 2015 9:21pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar11046_3.gif) chaveznqoos](chaveznqoos)

  * Joined Jun 2006 | Status: Trader | [450 Posts](/search?do=process&provider=Member&searchuser=11046)

> [Quoting skyline](/thread/post/8493427#post8493427 "View Quoted Post")
> 
> Disliked
> 
> Hi Cjtylor, I've discontinued Demo Udine EA that you can see in Trade Explorer (will remove soon from there) since is it obvious that this EA is not profitable. Speaking about the live account running without any TP set, actually I have only one position opened on EJ long @134.70 so around 180 pips right now in floating profit but a lot of other positions closed in loss or at B/E. There would need to catch some other big move so that equity will start to go in positive territory. Numbers in my account : Balance : -8.27% Equity : +7.14% Will attach...
> 
> Ignored

Hi skyline;  
  
With +200 pips you Do not have any plan to protect part of this good entry?  
  
Grazie ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#462](/thread/post/8494111#post8494111 "Post Permalink")

  * Sep 17, 2015 9:32pm  Sep 17, 2015 9:32pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting chaveznqoos](/thread/post/8494076#post8494076 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi skyline; With +200 pips you Do not have any plan to protect part of this good entry? Grazie ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)
> 
> Ignored

Hi Chaveznqoos,  
200 pips are too low amount to even consider some action, at least I would wait up to 500 pips before start some form of trail by using a daily Donchian Channel or something based on daily ATR. Keep in mind that this kind of approach is a position/long term trading style with 500-1000 or even more profit from a single order as main goal.  
  
An early trailing could avoid such big gains, I know very hard to keep trading like this (a lot of losing trades coupled by very few winning).  
  
I could further consider some future changes to implement some trailing mechanism automatically handled by EA.  
  
Regards,  
Skyline 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#463](/thread/post/8494134#post8494134 "Post Permalink")

  * Sep 17, 2015 9:40pm  Sep 17, 2015 9:40pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar11046_3.gif) chaveznqoos](chaveznqoos)

  * Joined Jun 2006 | Status: Trader | [450 Posts](/search?do=process&provider=Member&searchuser=11046)

> [Quoting skyline](/thread/post/8494111#post8494111 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi Chaveznqoos, 200 pips are too low amount to even consider some action, at least I would wait up to 500 pips before start some form of trail by using a daily Donchian Channel or something based on daily ATR. Keep in mind that this kind of approach is a position/long term trading style with 500-1000 or even more profit from a single order as main goal. An early trailing could avoid such big gains, I know very hard to keep trading like this (a lot of losing trades coupled by very few winning). I could further consider some future changes...
> 
> Ignored

Yes, makes sense !!!!![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)  
  
Regards. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#464](/thread/post/8501676#post8501676 "Post Permalink")

  * Sep 22, 2015 8:45pm  Sep 22, 2015 8:45pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar11046_3.gif) chaveznqoos](chaveznqoos)

  * Joined Jun 2006 | Status: Trader | [450 Posts](/search?do=process&provider=Member&searchuser=11046)

> [Quoting skyline](/thread/post/8494111#post8494111 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi Chaveznqoos, 200 pips are too low amount to even consider some action, at least I would wait up to 500 pips before start some form of trail by using a daily Donchian Channel or something based on daily ATR. Keep in mind that this kind of approach is a position/long term trading style with 500-1000 or even more profit from a single order as main goal. An early trailing could avoid such big gains, I know very hard to keep trading like this (a lot of losing trades coupled by very few winning). I could further consider some future changes...
> 
> Ignored

Grrrrrrrrrrr !!!! bad luck with the entry of EURJPY, but is part of this business in Forex. ![](https://resources.faireconomy.media/images/emojis/64/1f624.png?v=15.1)  
  
Regards Skyline ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#465](/thread/post/8501692#post8501692 "Post Permalink")

  * Last Post: Sep 22, 2015 8:59pm  Sep 22, 2015 8:59pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar8826_5.gif) skyline](skyline)

  * Joined Apr 2006 | Status: Metatrader Programmer | [1,417 Posts](/search?do=process&provider=Member&searchuser=8826)

> [Quoting chaveznqoos](/thread/post/8501676#post8501676 "View Quoted Post")
> 
> Disliked
> 
> {quote} Grrrrrrrrrrr !!!! bad luck with the entry of EURJPY, but is part of this business in Forex. ![](https://resources.faireconomy.media/images/emojis/64/1f624.png?v=15.1) Regards Skyline ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)
> 
> Ignored

![](https://resources.faireconomy.media/images/emojis/64/1f61f.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/263a-fe0f.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f4ad.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * UdineEA Official Thread
  *   * [ **Reply to Thread** ](/thread/533099-udineea-official-thread/reply#reply)

[](https://www.forexfactory.com "Homepage")

  * [Forums](forums)
  * [Trades](trades)
  * [Calendar](calendar)
  * [News](news)
  * [Market](market)
  * [Brokers](brokers)

****

[](https://www.faireconomy.com/)
