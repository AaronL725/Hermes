

  * 

[The Bouncing Pip](/thread/88277-the-bouncing-pip "Hi everyone. 
 
I present to you a system called &quot;The Bouncing Pip&quot; 
 
This is a system that was originally developed by BigBear, so full...") 26 replies

[Price bouncing off of sma](/thread/228922-price-bouncing-off-of-sma "What is the logic behind a price bouncing off an SMA? 
 
For example if a price bounces of a 35 day sma, i should short it if bounces of...") 2 replies

[Developing a correlated bouncing system](/thread/158016-developing-a-correlated-bouncing-system "The above indicator is a simple ma indicator with the weekly ma set to 40. 
 
I like most of my bouncing signals to be in the direction of...") 9 replies

[bouncing candle indicator](/thread/105826-bouncing-candle-indicator "I once had an indicator that would  send  off an alert whenever a candle touched back on its  moving average.  Lost it somehow, but I do...") 0 replies

[Price bouncing off support or resistance,your thoughts](/thread/30984-price-bouncing-off-support-or-resistanceyour-thoughts "I would like to start a discussuion about price movement at support/resistance, Fib and pivot levels.  
  
Time and again I see the price...") 11 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/157406-fx30m-bouncing-system/reply#reply)
  * Subscribe
  * [72](javascript:void\(0\);)

Attachments: FX_30M Bouncing System

Tags: FX_30M Bouncing System

#  [](/thread/157406-fx30m-bouncing-system)FX_30M Bouncing System 

  * 

  * Opened Mar 17, 2009 | Never Closes | 41 Votes
  * ## Poll Results

  * 

  * rate this EA
  * hit daily target of 20 pip
  * I always lose using this EA although I follow the rules
  * No trade open, so I decided to stop test on it
  * View Poll Results (will be public)

rate this EA |   
---|---  
_hit daily target of 20 pip_ | 22 Votes |  | 54%  
| _None_  
 _I always lose using this EA although I follow the rules_ | 7 Votes |  | 17%  
| _None_  
 _No trade open, so I decided to stop test on it_ | 12 Votes |  | 29%  
| _None_  
  
  * [#1](/thread/157406-fx30m-bouncing-system "Post Permalink")

  * First Post: Mar 11, 2009 12:24pm  Mar 11, 2009 12:24pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83889_5.gif) siobi](siobi)

  * | Joined Oct 2008  | Status: Trader | [717 Posts](/search?do=process&provider=Member&searchuser=83889)

trading rules:  
place this EA to EUR/USD 30M chart.  
  
turn it on and trade for non news hour.  
  
setting:  
Num_Of_digit = False (set to true if you are using 5 digit platform)  
CloseHour= 11(set to 30 if you do not want EA to close the trade)  
HourStart=0 (always trade on Japan or non news session)  
HourEnd=10 (always trade on Japan or non news session)  
  
indicator required:  
slope_directional(customised)  
Storch RSI(customised)  
PSAR(standard from mt4)  
ADX(standard from mt4)  
  
template:  
V104R8.tpl  
  
EA:  
FX_30M_Bouncing_V104.ex4  
  
additional configuration:  
this EA needs to be configure once a month to ensure we have good pip hunting.  
  
FEE:  
it is FREE!!!!!!!(unless you wanna contribute ![](https://resources.faireconomy.media/images/emojis/64/1f61c.png?v=15.1))  
  
effectiveness:  
I'm trading it in Live acct after 6 months of testing in DEMO from V101R1.  
  
testing platform:  
IBFX,FXDD,Alpari  
  
MM:  
Daily target 20 pip.  
Stop and exit if it is totally out of trend... (this not yet happend and hope it wouldn't happend)  
slowly increase your lot size.  
  
BackTest:  
you do it yourself and do not post it here, we are looking at forward testing. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: 20090310.JPG
Size: 78 KB](/attachment/image/216678/thumbnail?d=1365564656)](/attachment/image/216678?d=1236741788)   

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [Slope Direction Line.ex4](/attachment/file/216670?d=1236741254) 4 KB | 1,946 downloads 

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [Stoch RSI.ex4](/attachment/file/216671?d=1236741254) 4 KB | 1,906 downloads 

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [FX_30M_Bouncing_V104.ex4](/attachment/file/216673?d=1236741380) 16 KB | 2,030 downloads 

![File Type: tpl](https://assets.faireconomy.media/images/attach/tpl.gif) [v104_r8.tpl](/attachment/file/216677?d=1236741772) 32 KB | 1,885 downloads 

  * [#2](/thread/post/2594160#post2594160 "Post Permalink")

  * Mar 11, 2009 12:27pm  Mar 11, 2009 12:27pm 

  * [ artov](artov)

  * | Joined Sep 2008  | Status: Trader | [567 Posts](/search?do=process&provider=Member&searchuser=79619)

Nice Siobi, is it the same one from the other thread? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#3](/thread/post/2594361#post2594361 "Post Permalink")

  * Mar 11, 2009 1:37pm  Mar 11, 2009 1:37pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83889_5.gif) siobi](siobi)

  * | Joined Oct 2008  | Status: Trader | [717 Posts](/search?do=process&provider=Member&searchuser=83889)

artov,  
  
Yes is the same.. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#4](/thread/post/2594379#post2594379 "Post Permalink")

  * Mar 11, 2009 1:44pm  Mar 11, 2009 1:44pm 

  * [ Dan Johnston](dan*johnston)

  * | Joined May 2008  | Status: Trader | [354 Posts](/search?do=process&provider=Member&searchuser=69420)

Siobi, with the great performance of v104r7 I'm almost hesitant to replace it with v104r8 above.![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#5](/thread/post/2594453#post2594453 "Post Permalink")

  * Mar 11, 2009 2:21pm  Mar 11, 2009 2:21pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83889_5.gif) siobi](siobi)

  * | Joined Oct 2008  | Status: Trader | [717 Posts](/search?do=process&provider=Member&searchuser=83889)

this EA can be trade in any session EXCEPT news session.  
  
I choose Asian session because it is less news and ........... the most important I'm living in Asian country!!!! here is my time zone babe!!!  
  
![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#6](/thread/post/2594456#post2594456 "Post Permalink")

  * Mar 11, 2009 2:23pm  Mar 11, 2009 2:23pm 

  * [ samer960](samer960)

  * | Joined Dec 2008  | Status: Trader | [673 Posts](/search?do=process&provider=Member&searchuser=89670)

hi   
the ea do not enter any position in backtesting ,this is my screen , is there anything i should do ?  
thanks 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: siobi.gif
Size: 25 KB](/attachment/image/216745/thumbnail?d=1365564656)](/attachment/image/216745?d=1236749005)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#7](/thread/post/2594499#post2594499 "Post Permalink")

  * Mar 11, 2009 2:50pm  Mar 11, 2009 2:50pm 

  * [ Peacelover](peacelover)

  * | Joined Mar 2007  | Status: Trader | [110 Posts](/search?do=process&provider=Member&searchuser=36182)

place this EA to EUR/USD 30M chart.  
  
turn it on and trade for non news hour.  
  
setting:  
Num_Of_digit = False (set to true if you are using 5 digit platform)  
CloseHour= 11(set to 30 if you do not want EA to close the trade)  
HourStart=0 (always trade on Japan or non news session)  
HourEnd=10 (always trade on Japan or non news session)  
  
**__What are the settings for these indicators?__**  
indicator required:  
slope_directional(customised)  
Storch RSI(customised)  
PSAR(standard from mt4)  
ADX(standard from mt4)  
  
template:  
V104R8.tpl  
  
EA:  
FX_30M_Bouncing_V104.ex4  
  
additional configuration:  
this EA needs to be configure once a month to ensure we have good pip hunting.  
  
FEE:  
it is FREE!!!!!!!(unless you wanna contribute ![](https://resources.faireconomy.media/images/emojis/64/1f61c.png?v=15.1))  
  
effectiveness:  
I'm trading it in Live acct after 6 months of testing in DEMO from V101R1.  
  
testing platform:  
IBFX,FXDD,Alpari  
  
MM:  
Daily target 20 pip.  
Stop and exit if it is totally out of trend... (this not yet happend and hope it wouldn't happend)  
slowly increase your lot size.  
  
BackTest:  
you do it yourself and do not post it here, we are looking at forward testing.[/quote] 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#8](/thread/post/2594506#post2594506 "Post Permalink")

  * Mar 11, 2009 2:57pm  Mar 11, 2009 2:57pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83889_5.gif) siobi](siobi)

  * | Joined Oct 2008  | Status: Trader | [717 Posts](/search?do=process&provider=Member&searchuser=83889)

> [Quoting Peacelover](/thread/post/2594499#post2594499 "View Quoted Post")
> 
> Disliked
> 
> place this EA to EUR/USD 30M chart.  
>    
>  turn it on and trade for non news hour.  
>    
>  setting:  
>  Num_Of_digit = False (set to true if you are using 5 digit platform)  
>  CloseHour= 11(set to 30 if you do not want EA to close the trade)  
>  HourStart=0 (always trade on Japan or non news session)  
>  HourEnd=10 (always trade on Japan or non news session)  
>    
>  **__What are the settings for these indicators?__**  
>  indicator required:  
>  slope_directional(customised)  
>  Storch RSI(customised)  
>  PSAR(standard from mt4)  
>  ADX(standard from...
> 
> Ignored

[/quote]  
  
FOLLOW THE   
template given...... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#9](/thread/post/2594512#post2594512 "Post Permalink")

  * Mar 11, 2009 3:00pm  Mar 11, 2009 3:00pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83889_5.gif) siobi](siobi)

  * | Joined Oct 2008  | Status: Trader | [717 Posts](/search?do=process&provider=Member&searchuser=83889)

> [Quoting samer960](/thread/post/2594456#post2594456 "View Quoted Post")
> 
> Disliked
> 
> hi   
>  the ea do not enter any position in backtesting ,this is my screen , is there anything i should do ?  
>  thanks
> 
> Ignored

hm..  
1) what platform u r using?  
2) back Test period?  
3) is your expert/journal tab showing any error loading indicator? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#10](/thread/post/2594519#post2594519 "Post Permalink")

  * Mar 11, 2009 3:04pm  Mar 11, 2009 3:04pm 

  * [ samer960](samer960)

  * | Joined Dec 2008  | Status: Trader | [673 Posts](/search?do=process&provider=Member&searchuser=89670)

hi   
i am using ibfx and i am trying to backtest 2008 . nothing wrong in the journal   
thanks 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#11](/thread/post/2594536#post2594536 "Post Permalink")

  * Mar 11, 2009 3:13pm  Mar 11, 2009 3:13pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83889_5.gif) siobi](siobi)

  * | Joined Oct 2008  | Status: Trader | [717 Posts](/search?do=process&provider=Member&searchuser=83889)

1) what platform u r using?  
\--> you are using IBFX...  
  
2) back Test period?  
\--> you said 2008, here is my screen result for backtest.  
  
3) is your expert/journal tab showing any error loading indicator?  
\--> you say no, so the only difference is the period.  
  
try change the period as mine.... 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: backtest.JPG
Size: 31 KB](/attachment/image/216761/thumbnail?d=1365564689)](/attachment/image/216761?d=1236751933)   
[![Click to Enlarge

Name: backtest1.JPG
Size: 39 KB](/attachment/image/216762/thumbnail?d=1365564689)](/attachment/image/216762?d=1236751933)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#12](/thread/post/2594562#post2594562 "Post Permalink")

  * Mar 11, 2009 3:28pm  Mar 11, 2009 3:28pm 

  * [ samer960](samer960)

  * | Joined Dec 2008  | Status: Trader | [673 Posts](/search?do=process&provider=Member&searchuser=89670)

thanks siobi it works now , strange why it didnt take 2008 . anyway thank you 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#13](/thread/post/2595218#post2595218 "Post Permalink")

  * Mar 11, 2009 8:51pm  Mar 11, 2009 8:51pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83889_5.gif) siobi](siobi)

  * | Joined Oct 2008  | Status: Trader | [717 Posts](/search?do=process&provider=Member&searchuser=83889)

+19 pip. EA close 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: 20090311.jpg
Size: 130 KB](/attachment/image/216914/thumbnail?d=1365564712)](/attachment/image/216914?d=1236772280)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#14](/thread/post/2595288#post2595288 "Post Permalink")

  * Mar 11, 2009 9:36pm  Mar 11, 2009 9:36pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar95566_5.gif) stifland](stifland)

  * | Joined Mar 2009  | Status: Trader | [304 Posts](/search?do=process&provider=Member&searchuser=95566)

Good morning. I still had no trads. Going to delete everything and start over with the new posts. Thanks for new thread siobi. Dan , send along new template complete with color manual and some snacks while reading. lol. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#15](/thread/post/2595291#post2595291 "Post Permalink")

  * Edited 10:20pm  Mar 11, 2009 9:37pm | Edited 10:20pm 

  * [ Dan Johnston](dan*johnston)

  * | Joined May 2008  | Status: Trader | [354 Posts](/search?do=process&provider=Member&searchuser=69420)

Siobi, so far it seems ea is good at picking up on strong trends, in which case why only limit yourself to TP of 20 pips.  
  
I know the downside of not using a TP is that if price reaches 20 then retraces, you only end up with 5 pips I think - with trailing of 15 anyway.  
My thinking may be completely off though, as one trade doesn't prove anything, but wow!!!!:  
(Max drawdown on this last trade was only -15 pips I believe - as has mostly been the case for the last previous trades, I believe. Max stoploss setting so far may be as low as 20 or 30. If that proves to be true, that would be something!!!) Someone with a faster computer may want to do an optimization. All my computers are older and stuffed full.  
  
(At least one other account took in TP of 20 pips.) 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: v104r7 3 11 09.gif
Size: 55 KB](/attachment/image/216938/thumbnail?d=1365564712)](/attachment/image/216938?d=1236775039)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#16](/thread/post/2595294#post2595294 "Post Permalink")

  * Mar 11, 2009 9:38pm  Mar 11, 2009 9:38pm 

  * [ Dan Johnston](dan*johnston)

  * | Joined May 2008  | Status: Trader | [354 Posts](/search?do=process&provider=Member&searchuser=69420)

> [Quoting stifland](/thread/post/2595288#post2595288 "View Quoted Post")
> 
> Disliked
> 
> Good morning. I still had no trads. Going to delete everything and start over with the new posts. Thanks for new thread siobi. Dan , send along new template complete with color manual and some snacks while reading. lol.
> 
> Ignored

Barbeque chips allright? LOL 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#17](/thread/post/2595295#post2595295 "Post Permalink")

  * Mar 11, 2009 9:38pm  Mar 11, 2009 9:38pm 

  * [ kramlon](kramlon)

  * | Joined Sep 2007  | Status: Trader | [52 Posts](/search?do=process&provider=Member&searchuser=48919)

Does EA adjust broker time automatically?  
  
Thanks.  
  

> [Quoting siobi](/thread/post/2594453#post2594453 "View Quoted Post")
> 
> Disliked
> 
> this EA can be trade in any session EXCEPT news session.  
>    
>  I choose Asian session because it is less news and ........... the most important I'm living in Asian country!!!! here is my time zone babe!!!  
>    
>  ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#18](/thread/post/2595325#post2595325 "Post Permalink")

  * Mar 11, 2009 9:52pm  Mar 11, 2009 9:52pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar80573_5.gif) Rastaman](rastaman)

  * Joined Sep 2008 | Status: Trader | [2,298 Posts](/search?do=process&provider=Member&searchuser=80573)

Siobi  
  
As I am here in Japan, this seems like a good system for me to use.  
  
Is this only effective in the Asian session and should be closed when the Tokyo market ends?  
  
Also, do we leave the SL at 100? Seems a bit extreme? 

Starting to see instead of just looking.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#19](/thread/post/2595362#post2595362 "Post Permalink")

  * Mar 11, 2009 10:15pm  Mar 11, 2009 10:15pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar95566_5.gif) stifland](stifland)

  * | Joined Mar 2009  | Status: Trader | [304 Posts](/search?do=process&provider=Member&searchuser=95566)

Still no trades! I hate to be a problem but it is very frustrating. I have other experts that work no prob. Any ideas? I am on fxdd.  
billy 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: notrade.gif
Size: 21 KB](/attachment/image/216953/thumbnail?d=1365564712)](/attachment/image/216953?d=1236777353)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#20](/thread/post/2595387#post2595387 "Post Permalink")

  * Mar 11, 2009 10:26pm  Mar 11, 2009 10:26pm 

  * [ Dan Johnston](dan*johnston)

  * | Joined May 2008  | Status: Trader | [354 Posts](/search?do=process&provider=Member&searchuser=69420)

> [Quoting stifland](/thread/post/2595362#post2595362 "View Quoted Post")
> 
> Disliked
> 
> Still no trades! I hate to be a problem but it is very frustrating. I have other experts that work no prob. Any ideas? I am on fxdd.  
>  billy
> 
> Ignored

You may be allright now, since mine only took one trade about 2 1/2 hrs or so ago, probably when you were having that problem.  
  
Do you get any messages, and what are all your settings?  
It says "within trading times", but it's no "scalper" in the true meaning of the word, so a couple of trades per day only is about right. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * FX_30M Bouncing System
  *   * [ **Reply to Thread** ](/thread/157406-fx30m-bouncing-system/reply#reply)

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

[The Bouncing Pip](/thread/88277-the-bouncing-pip "Hi everyone. 
 
I present to you a system called &quot;The Bouncing Pip&quot; 
 
This is a system that was originally developed by BigBear, so full...") 26 replies

[Price bouncing off of sma](/thread/228922-price-bouncing-off-of-sma "What is the logic behind a price bouncing off an SMA? 
 
For example if a price bounces of a 35 day sma, i should short it if bounces of...") 2 replies

[Developing a correlated bouncing system](/thread/158016-developing-a-correlated-bouncing-system "The above indicator is a simple ma indicator with the weekly ma set to 40. 
 
I like most of my bouncing signals to be in the direction of...") 9 replies

[bouncing candle indicator](/thread/105826-bouncing-candle-indicator "I once had an indicator that would  send  off an alert whenever a candle touched back on its  moving average.  Lost it somehow, but I do...") 0 replies

[Price bouncing off support or resistance,your thoughts](/thread/30984-price-bouncing-off-support-or-resistanceyour-thoughts "I would like to start a discussuion about price movement at support/resistance, Fib and pivot levels.  
  
Time and again I see the price...") 11 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/157406-fx30m-bouncing-system/reply#reply)
  * Subscribe
  * [72](javascript:void\(0\);)

Attachments: FX_30M Bouncing System

Tags: FX_30M Bouncing System

#  [](/thread/157406-fx30m-bouncing-system)FX_30M Bouncing System 

  * 

  * [#21](/thread/post/2595395#post2595395 "Post Permalink")

  * Mar 11, 2009 10:31pm  Mar 11, 2009 10:31pm 

  * [ mueen2419](mueen2419)

  * | Joined Sep 2008  | Status: Trader | [6 Posts](/search?do=process&provider=Member&searchuser=80949)

one question why to place indicators if EA works and calculates everythiing itself,  
Thnaks 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#22](/thread/post/2595397#post2595397 "Post Permalink")

  * Mar 11, 2009 10:32pm  Mar 11, 2009 10:32pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar95566_5.gif) stifland](stifland)

  * | Joined Mar 2009  | Status: Trader | [304 Posts](/search?do=process&provider=Member&searchuser=95566)

24,0,24,2,100,20,15  
  
It wasn't running then maybe? Will it show trades in hindsight or only going forward as they happen? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#23](/thread/post/2595411#post2595411 "Post Permalink")

  * Mar 11, 2009 10:39pm  Mar 11, 2009 10:39pm 

  * [ Dan Johnston](dan*johnston)

  * | Joined May 2008  | Status: Trader | [354 Posts](/search?do=process&provider=Member&searchuser=69420)

The indicators give you a hud effect. Heads up display, to get an idea of what it's doing.   
  
Always have to keep an eye on those pesky machines, you know!![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)  
  
Stifland try **30** ,0,24,2...  
  
You may also try dropping ea on 1m timeframes of diff. pairs just to see if it's alive. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: experts tab.gif
Size: 50 KB](/attachment/image/216966/thumbnail?d=1365564712)](/attachment/image/216966?d=1236778942)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#24](/thread/post/2595464#post2595464 "Post Permalink")

  * Mar 11, 2009 11:02pm  Mar 11, 2009 11:02pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar95566_5.gif) stifland](stifland)

  * | Joined Mar 2009  | Status: Trader | [304 Posts](/search?do=process&provider=Member&searchuser=95566)

no nothing. are you using the expert from page 1 here?? I do notice on chart it says system type=none. Is that a problem? I saw picture of siobi's said super scalp. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#25](/thread/post/2595472#post2595472 "Post Permalink")

  * Mar 11, 2009 11:06pm  Mar 11, 2009 11:06pm 

  * [ Dan Johnston](dan*johnston)

  * | Joined May 2008  | Status: Trader | [354 Posts](/search?do=process&provider=Member&searchuser=69420)

> [Quoting stifland](/thread/post/2595464#post2595464 "View Quoted Post")
> 
> Disliked
> 
> no nothing. are you using the expert from page 1 here?? I do notice on chart it says system type=none. Is that a problem? I saw picture of siobi's said super scalp.
> 
> Ignored

I actually have both r7 and r8 running on various accounts, and have lost track.  
  
The "none" will stay there untill your next trade I think according to what Siobi said to someone posting same question in the past.   
  
Do a screenshot of your experts tab and let's take a look. I'm no expert, just been lucky so far. ...And not a drop of Irish in me.![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#26](/thread/post/2595500#post2595500 "Post Permalink")

  * Mar 11, 2009 11:19pm  Mar 11, 2009 11:19pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar95566_5.gif) stifland](stifland)

  * | Joined Mar 2009  | Status: Trader | [304 Posts](/search?do=process&provider=Member&searchuser=95566)

umm, don't know how to do screenshot with other window open. Just dings.  
![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1) i'm mostly scottish so maybe it's all the drinking for breakfast. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#27](/thread/post/2595511#post2595511 "Post Permalink")

  * Mar 11, 2009 11:24pm  Mar 11, 2009 11:24pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar95566_5.gif) stifland](stifland)

  * | Joined Mar 2009  | Status: Trader | [304 Posts](/search?do=process&provider=Member&searchuser=95566)

But I have the 4 Left buttons checked.  
Enable Expert Advisors  
Allow live Trading  
Allow DLL  
Allow external  
  
None of the inner boxes checked 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#28](/thread/post/2595603#post2595603 "Post Permalink")

  * Mar 11, 2009 11:56pm  Mar 11, 2009 11:56pm 

  * [ majorbillion](majorbillion)

  * | Joined Mar 2008  | Status: Trader | [33 Posts](/search?do=process&provider=Member&searchuser=64787)

Stifland:  
  
Like you, I'm on FXDD. Can you PM me? I'd like compare notes with you on settings offline. We can share with the rest of the group once we've got it all figured out.  
  
I can't PM you because it appears your PM is shut off.  
  
Thanks,  
Majorbillion  
  
  
  
  
  

> [Quoting stifland](/thread/post/2595511#post2595511 "View Quoted Post")
> 
> Disliked
> 
> But I have the 4 Left buttons checked.  
>  Enable Expert Advisors  
>  Allow live Trading  
>  Allow DLL  
>  Allow external  
>    
>  None of the inner boxes checked
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#29](/thread/post/2595704#post2595704 "Post Permalink")

  * Mar 12, 2009 12:26am  Mar 12, 2009 12:26am 

  * [ DiemTrader](diemtrader)

  * | Joined Dec 2008  | Status: Trader | [39 Posts](/search?do=process&provider=Member&searchuser=87750)

Definately FXDD issue. I have the same problem. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#30](/thread/post/2595715#post2595715 "Post Permalink")

  * Mar 12, 2009 12:28am  Mar 12, 2009 12:28am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar95566_5.gif) stifland](stifland)

  * | Joined Mar 2009  | Status: Trader | [304 Posts](/search?do=process&provider=Member&searchuser=95566)

hmmm, well that blows ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#31](/thread/post/2595768#post2595768 "Post Permalink")

  * Mar 12, 2009 12:49am  Mar 12, 2009 12:49am 

  * [ qz10cq](qz10cq)

  * | Joined Dec 2006  | Status: Trader | [303 Posts](/search?do=process&provider=Member&searchuser=29720)

> [Quoting DiemTrader](/thread/post/2595704#post2595704 "View Quoted Post")
> 
> Disliked
> 
> Definately FXDD issue. I have the same problem.
> 
> Ignored

FXDD is working fine for me>

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#32](/thread/post/2595803#post2595803 "Post Permalink")

  * Mar 12, 2009 1:04am  Mar 12, 2009 1:04am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar95566_5.gif) stifland](stifland)

  * | Joined Mar 2009  | Status: Trader | [304 Posts](/search?do=process&provider=Member&searchuser=95566)

qz, could you share Tools-Experts settings and the expert settings for comparison. thanks. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#33](/thread/post/2595858#post2595858 "Post Permalink")

  * Edited 1:35am  Mar 12, 2009 1:20am | Edited 1:35am 

  * [ Dan Johnston](dan*johnston)

  * | Joined May 2008  | Status: Trader | [354 Posts](/search?do=process&provider=Member&searchuser=69420)

My desktop fxdd:  
  
Guys, any strange comments in experts tab at bottom of fxdd platform? Maybe also check journal tab next to it for any clues.   
  
Remember both my ibfx and fxdd only had one trade for the 11th so far.  
  
....From the performance, I'll soon be using 100 lots! LOL  
  
(On ibfx I didn't use a TP, so it ran all the way up and eventually got stopped out with magnificent profit!) ...Yet I happened to be there to see the trade progress and could have stopped it manually for even more. Even so 43 sexy pips!  
  
Only 20 on fxdd.![](https://resources.faireconomy.media/images/emojis/64/1f641.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)

Attached Image (click to enlarge)

[![Click to Enlarge

Name: v104fxdd3 11 09.gif
Size: 49 KB](/attachment/image/217048/thumbnail?d=1365564742)](/attachment/image/217048?d=1236788305)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#34](/thread/post/2595912#post2595912 "Post Permalink")

  * Mar 12, 2009 1:38am  Mar 12, 2009 1:38am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar95566_5.gif) stifland](stifland)

  * | Joined Mar 2009  | Status: Trader | [304 Posts](/search?do=process&provider=Member&searchuser=95566)

no, my screen look exactly like yours except for no long entry and system type=none.  
  
Dan, what are the manual rules? Cross of the yellow with psar flip and slop confirm? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#35](/thread/post/2595938#post2595938 "Post Permalink")

  * Mar 12, 2009 1:45am  Mar 12, 2009 1:45am 

  * [ Dan Johnston](dan*johnston)

  * | Joined May 2008  | Status: Trader | [354 Posts](/search?do=process&provider=Member&searchuser=69420)

> [Quoting stifland](/thread/post/2595912#post2595912 "View Quoted Post")
> 
> Disliked
> 
> no, my screen look exactly like yours except for no long entry and system type=none.  
>    
>  Dan, what are the manual rules? Cross of the yellow with psar flip and slop confirm?
> 
> Ignored

  
I'm embarrassed to say that I'm not even sure, but it sure does work. ...When it's working. My manual rules are different, and don't want to get off the subject of 104 like I did in other thread.  
  
So you downloaded and installed all the indicators, etc. obviously. Your settings seem to be just fine except change the 24 to 30 as posted earlier.  
  
Your "none" should go away once you get a trade, ...unless I dreamed that, and that's unlikely.  
  
And you have no funny messages in your experts and journal tabs at the very bottom of mt4.  
  
Are you using Vista??? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#36](/thread/post/2595945#post2595945 "Post Permalink")

  * Mar 12, 2009 1:47am  Mar 12, 2009 1:47am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar95566_5.gif) stifland](stifland)

  * | Joined Mar 2009  | Status: Trader | [304 Posts](/search?do=process&provider=Member&searchuser=95566)

yeah, vista. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#37](/thread/post/2595950#post2595950 "Post Permalink")

  * Mar 12, 2009 1:48am  Mar 12, 2009 1:48am 

  * [ Dan Johnston](dan*johnston)

  * | Joined May 2008  | Status: Trader | [354 Posts](/search?do=process&provider=Member&searchuser=69420)

HHHHMMMM!  
  
I kind of thought so. Do you have another comp with xp or 2000?  
  
Have you had _any_ ea working before? Google mt4 problems with vista and see what comes up. You are not the first!!!!  
  
Vista and MT4 don't always see eye to eye. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#38](/thread/post/2595985#post2595985 "Post Permalink")

  * Mar 12, 2009 2:02am  Mar 12, 2009 2:02am 

  * [ Dan Johnston](dan*johnston)

  * | Joined May 2008  | Status: Trader | [354 Posts](/search?do=process&provider=Member&searchuser=69420)

If you didn't already find it try the following for Vista and MT4 problems:  
  
[http://www.howtofixcomputers.com/for...ing-61051.html](http://www.howtofixcomputers.com/forums/windows-vista/meta-trader-mt4-stopped-working-61051.html)  
  
You're not the first and probably not the last, unfortunately. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#39](/thread/post/2596056#post2596056 "Post Permalink")

  * Mar 12, 2009 2:34am  Mar 12, 2009 2:34am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar95566_5.gif) stifland](stifland)

  * | Joined Mar 2009  | Status: Trader | [304 Posts](/search?do=process&provider=Member&searchuser=95566)

well, i don't have problems with mt4 in general and i can successfully run other ea's...... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#40](/thread/post/2596082#post2596082 "Post Permalink")

  * Mar 12, 2009 2:45am  Mar 12, 2009 2:45am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar95566_5.gif) stifland](stifland)

  * | Joined Mar 2009  | Status: Trader | [304 Posts](/search?do=process&provider=Member&searchuser=95566)

> [Quoting Dan Johnston](/thread/post/2595411#post2595411 "View Quoted Post")
> 
> Disliked
> 
> The indicators give you a hud effect. Heads up display, to get an idea of what it's doing.   
>    
>  Always have to keep an eye on those pesky machines, you know!![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)  
>    
>  Stifland try **30** ,0,24,2...  
>    
>  You may also try dropping ea on 1m timeframes of diff. pairs just to see if it's alive.
> 
> Ignored

  
here loading on both if you can see 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: loading.gif
Size: 110 KB](/attachment/image/217087/thumbnail?d=1365564742)](/attachment/image/217087?d=1236793522)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * FX_30M Bouncing System
  *   * [ **Reply to Thread** ](/thread/157406-fx30m-bouncing-system/reply#reply)

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

[The Bouncing Pip](/thread/88277-the-bouncing-pip "Hi everyone. 
 
I present to you a system called &quot;The Bouncing Pip&quot; 
 
This is a system that was originally developed by BigBear, so full...") 26 replies

[Price bouncing off of sma](/thread/228922-price-bouncing-off-of-sma "What is the logic behind a price bouncing off an SMA? 
 
For example if a price bounces of a 35 day sma, i should short it if bounces of...") 2 replies

[Developing a correlated bouncing system](/thread/158016-developing-a-correlated-bouncing-system "The above indicator is a simple ma indicator with the weekly ma set to 40. 
 
I like most of my bouncing signals to be in the direction of...") 9 replies

[bouncing candle indicator](/thread/105826-bouncing-candle-indicator "I once had an indicator that would  send  off an alert whenever a candle touched back on its  moving average.  Lost it somehow, but I do...") 0 replies

[Price bouncing off support or resistance,your thoughts](/thread/30984-price-bouncing-off-support-or-resistanceyour-thoughts "I would like to start a discussuion about price movement at support/resistance, Fib and pivot levels.  
  
Time and again I see the price...") 11 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/157406-fx30m-bouncing-system/reply#reply)
  * Subscribe
  * [72](javascript:void\(0\);)

Attachments: FX_30M Bouncing System

Tags: FX_30M Bouncing System

#  [](/thread/157406-fx30m-bouncing-system)FX_30M Bouncing System 

  * 

  * [#41](/thread/post/2596103#post2596103 "Post Permalink")

  * Mar 12, 2009 2:51am  Mar 12, 2009 2:51am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar95560_6.gif) rss](rss)

  * | Joined Mar 2009  | Status: Trader | [4 Posts](/search?do=process&provider=Member&searchuser=95560)

is this atrue signal or not?? 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: ل.gif
Size: 20 KB](/attachment/image/217091/thumbnail?d=1365564742)](/attachment/image/217091?d=1236793876)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#42](/thread/post/2596352#post2596352 "Post Permalink")

  * Mar 12, 2009 4:18am  Mar 12, 2009 4:18am 

  * [ Dan Johnston](dan*johnston)

  * | Joined May 2008  | Status: Trader | [354 Posts](/search?do=process&provider=Member&searchuser=69420)

In hindsight looked like a great signal since v104 took a buy way up from there and got 20 pips.![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)  
  
Stifland, you should have gotten that last trade if your platform is up and running. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#43](/thread/post/2596406#post2596406 "Post Permalink")

  * Mar 12, 2009 4:39am  Mar 12, 2009 4:39am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar95566_5.gif) stifland](stifland)

  * | Joined Mar 2009  | Status: Trader | [304 Posts](/search?do=process&provider=Member&searchuser=95566)

no, but i am getting backtest results now where i wasn't before. Not sure what i did but will leave it running and report back... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#44](/thread/post/2596429#post2596429 "Post Permalink")

  * Mar 12, 2009 4:47am  Mar 12, 2009 4:47am 

  * [ Dan Johnston](dan*johnston)

  * | Joined May 2008  | Status: Trader | [354 Posts](/search?do=process&provider=Member&searchuser=69420)

> [Quoting stifland](/thread/post/2596406#post2596406 "View Quoted Post")
> 
> Disliked
> 
> no, but i am getting backtest results now where i wasn't before. Not sure what i did but will leave it running and report back...
> 
> Ignored

Some progress.  
  
Actually my ibfx didn't take that last trade either where fxdd did. ![](https://resources.faireconomy.media/images/emojis/64/1f615.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/2753.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#45](/thread/post/2596455#post2596455 "Post Permalink")

  * Mar 12, 2009 4:59am  Mar 12, 2009 4:59am 

  * [ kramlon](kramlon)

  * | Joined Sep 2007  | Status: Trader | [52 Posts](/search?do=process&provider=Member&searchuser=48919)

Works fine on IBFX but not on Alpari or other 5 digits brokers. Any idea?  
  

> [Quoting Dan Johnston](/thread/post/2596429#post2596429 "View Quoted Post")
> 
> Disliked
> 
> Some progress.  
>    
>  Actually my ibfx didn't take that last trade either where fxdd did. ![](https://resources.faireconomy.media/images/emojis/64/1f615.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/2753.png?v=15.1)
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#46](/thread/post/2596477#post2596477 "Post Permalink")

  * Mar 12, 2009 5:10am  Mar 12, 2009 5:10am 

  * [ Dan Johnston](dan*johnston)

  * | Joined May 2008  | Status: Trader | [354 Posts](/search?do=process&provider=Member&searchuser=69420)

> [Quoting kramlon](/thread/post/2596455#post2596455 "View Quoted Post")
> 
> Disliked
> 
> Works fine on IBFX but not on Alpari or other 5 digits brokers. Any idea?
> 
> Ignored

Look at "remark digit" in ea properties. I think "true" for 5 digit. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#47](/thread/post/2596529#post2596529 "Post Permalink")

  * Mar 12, 2009 5:35am  Mar 12, 2009 5:35am 

  * [ majorbillion](majorbillion)

  * | Joined Mar 2008  | Status: Trader | [33 Posts](/search?do=process&provider=Member&searchuser=64787)

Hi this morning, I set 30MBS to look for trades for the entire 24 hour trading period.   
  
So far I've gotten one trade and it was profitable. Thank you Siobi and everybody on this thread for their contributions!  
  
Question for Siobi or any veterans of this EA: 

  1. Does 100 pips really have to be the stop-loss? Does the trailing stop of 15 only kick in if the price moves your favor? If so, is there any research on the maximum that price action will typically move against a position before it becomes profitable?
  2. Is it everybody's intention to watch this EA and exit manually if an adverse move occurs?
  3. The actual logic and methodology underlying the system seems to have evolved since the beginning of the previous thread. Is there some place where I download the latest manual version of the AND THE RULES so that I can so I can play around with it?

I know it irritates people like crazy when somebody asks questions like these that already answered in the thread. But I looked and to the best of my knowledge I couldn't find anything on it.  
  
Thanks! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#48](/thread/post/2596610#post2596610 "Post Permalink")

  * Mar 12, 2009 6:14am  Mar 12, 2009 6:14am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar91849_4.gif) royconnell](royconnell)

  * | Joined Jan 2009  | Status: Trader | [10 Posts](/search?do=process&provider=Member&searchuser=91849)

Thx for this EA Siobi. Demo testing now on IBFX.  
Any chance i could get the .mq4 file of the expert? I don't know how to run it during all sessions, but not news. 

"If we knew what we were doing we wouldn't call it research." A. Einstein

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#49](/thread/post/2596701#post2596701 "Post Permalink")

  * Mar 12, 2009 7:05am  Mar 12, 2009 7:05am 

  * [ Mungo2](mungo2)

  * | Joined Mar 2009  | Status: Trader | [6 Posts](/search?do=process&provider=Member&searchuser=95488)

I have increased spread from 2 to 3. Running it live in IBFX. Thanks to siobi, Dan J and the rest of the team Kino et all. Has anyone mastered kino all in one siobi indicator????? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#50](/thread/post/2596732#post2596732 "Post Permalink")

  * Mar 12, 2009 7:22am  Mar 12, 2009 7:22am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83889_5.gif) siobi](siobi)

  * | Joined Oct 2008  | Status: Trader | [717 Posts](/search?do=process&provider=Member&searchuser=83889)

guys!!!! the feedback is so encouraging!!!  
  
20090311 resulted 39 pip !!!!  
  
Q&A:  
1) does it really need 100 pip sl?  
->NO, I'm now running in live using 50 pip, the lowest I seen before is -23 pip, so I think -50 pip is quite secure.  
  
2) Vista got an problem?  
-> No, my live acct running at Vista  
  
3) mq4?  
->No, reason, ask dan... ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
  
4) manual exit?  
->most of the time no need. this EA exit is still based on stop lose pip until we find out a good exit strategy. my Manual exit is depanding on the slope direction.once there is 2 same BAR for oposite direction, I'll exit manually. This case still havent hapend and still this EA is in correct direction.  
  
5) The manual of the trading is still in progress... (untill I got free time... dan is asking for another EA development... no resting time ![](https://resources.faireconomy.media/images/emojis/64/1f61c.png?v=15.1))  
  
happy pipping!!! 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: 20090311.jpg
Size: 130 KB](/attachment/image/217214/thumbnail?d=1365564770)](/attachment/image/217214?d=1236810339)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#51](/thread/post/2596757#post2596757 "Post Permalink")

  * Mar 12, 2009 7:34am  Mar 12, 2009 7:34am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83889_5.gif) siobi](siobi)

  * | Joined Oct 2008  | Status: Trader | [717 Posts](/search?do=process&provider=Member&searchuser=83889)

total trafr open: 7  
total win : 7  
  
winning rate = 100%  
  
winning pip = 88 pips  
  
the best part is.... I'm trading this in LIVE acct....!!!!!  
  
broker: IBFX  
internet speed= 1M line  
OS= Vista  
  
what else? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#52](/thread/post/2596801#post2596801 "Post Permalink")

  * Mar 12, 2009 7:55am  Mar 12, 2009 7:55am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83889_5.gif) siobi](siobi)

  * | Joined Oct 2008  | Status: Trader | [717 Posts](/search?do=process&provider=Member&searchuser=83889)

today will be tons of news 10 hours from now...  
  
setting  
hourStart =0  
hourends=10  
  
Do not trade on news!!!! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#53](/thread/post/2596927#post2596927 "Post Permalink")

  * Edited 9:28am  Mar 12, 2009 9:06am | Edited 9:28am 

  * [ Dan Johnston](dan*johnston)

  * | Joined May 2008  | Status: Trader | [354 Posts](/search?do=process&provider=Member&searchuser=69420)

Thanks yet again Siobi!!  
  
Oh, man, you mean I gotta reset the hrs. in all the different instances of v104 I've got running?! Can't you make that automatic??? ....**__JUST KIDDING!!!!!!!!!!!LOL![](https://resources.faireconomy.media/images/emojis/64/1f61c.png?v=15.1)__**  
  
Check it out:On desktop;  
And minimal DD. Doesn't get any better. Should have used one fxdd minilot from the start. (10 ibfx minilots, which are really micro I think)![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)  
IBFX = +40pips today. (Total acc. loss on IBFX because of fapturbo and two 100 pip stopouts of v106 which I replaced with both r7 and r8 v104's differentiated by lot size now.)  
  
...And time to minimize lot size on fapturbo!![](https://resources.faireconomy.media/images/emojis/64/1f923.png?v=15.1) I'm doing infinitely better manual scalping the 1m!!![](https://resources.faireconomy.media/images/emojis/64/1f923.png?v=15.1)  
  
Siobi, any decision you make concerning ANYTHING is ok by me.  
I'm sure Karma will be coming back your way very soon. 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: v104fxdd3 11a 09.gif
Size: 48 KB](/attachment/image/217264/thumbnail?d=1365564770)](/attachment/image/217264?d=1236816099)   
[![Click to Enlarge

Name: v1043 11 ibfx.gif
Size: 49 KB](/attachment/image/217266/thumbnail?d=1365564796)](/attachment/image/217266?d=1236816988)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#54](/thread/post/2596971#post2596971 "Post Permalink")

  * Mar 12, 2009 9:38am  Mar 12, 2009 9:38am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar95566_5.gif) stifland](stifland)

  * | Joined Mar 2009  | Status: Trader | [304 Posts](/search?do=process&provider=Member&searchuser=95566)

I finally got trades!! Boy did I . Trading live on a micro account and put it on the 1 minute., went to eat dinner and now short from 5 entries! We'll see how it turns out. If it hits the -100, then lil acct in trouble ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)

Attached Image (click to enlarge)

[![Click to Enlarge

Name: igottrades.gif
Size: 24 KB](/attachment/image/217273/thumbnail?d=1365564796)](/attachment/image/217273?d=1236818305)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#55](/thread/post/2596973#post2596973 "Post Permalink")

  * Mar 12, 2009 9:39am  Mar 12, 2009 9:39am 

  * [ Dan Johnston](dan*johnston)

  * | Joined May 2008  | Status: Trader | [354 Posts](/search?do=process&provider=Member&searchuser=69420)

> [Quoting Mungo2](/thread/post/2596701#post2596701 "View Quoted Post")
> 
> Disliked
> 
> I have increased spread from 2 to 3. Running it live in IBFX. Thanks to siobi, Dan J and the rest of the team Kino et all. Has anyone mastered kino all in one siobi indicator?????
> 
> Ignored

Thanks for the kind words, but it's Siobi's show, although I'll do my amateurish best to help in any way I can. Which is usually more of a hinderance, actually.  
  
Yes, thanks go out to __everyone__ here. We all contribute more than we know.  
  
Personally, I'm not sure I've ever mastered anything, so my answer would be no. Not consistently anyway.   
  
We each have our own take on sometimes the very same thing, so what works for one may not work for someone else. But without Kino's kind contributions, along with mtuppers - for me - and countless others in this awsome community, where the hell would any of us be???  
  
I personally would probably be drunk in an alley somewhere in Tampa. Things are getting tough here!  
  
Y'all my last chance!!!!![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#56](/thread/post/2596978#post2596978 "Post Permalink")

  * Mar 12, 2009 9:41am  Mar 12, 2009 9:41am 

  * [ paradoxical](paradoxical)

  * | Joined Nov 2007  | Status: Trader | [1,186 Posts](/search?do=process&provider=Member&searchuser=54706)

Recently came across this thread and see the EA is working like a charm. Am trying it on demo from 0 to 23 hours (I need an hours rest), and with a take profit of 100.   
BUT...No trades after 15 minutes? Anyone know what might be wrong with my EA? (just kidding). Looking forward to the same results (100%) as SIOBI, or even as good as Dan Johnson, and will be ready to go live next week at 100 lots a pop! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#57](/thread/post/2596979#post2596979 "Post Permalink")

  * Mar 12, 2009 9:41am  Mar 12, 2009 9:41am 

  * [ Dan Johnston](dan*johnston)

  * | Joined May 2008  | Status: Trader | [354 Posts](/search?do=process&provider=Member&searchuser=69420)

> [Quoting stifland](/thread/post/2596971#post2596971 "View Quoted Post")
> 
> Disliked
> 
> I finally got trades!! Boy did I . Trading live on a micro account and put it on the 1 minute., went to eat dinner and now short from 5 entries! We'll see how it turns out. If it hits the -100, then lil acct in trouble ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)
> 
> Ignored

You don't mess around, huh! LOL  
  
Remember 30m now.![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#58](/thread/post/2596989#post2596989 "Post Permalink")

  * Mar 12, 2009 9:44am  Mar 12, 2009 9:44am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar95566_5.gif) stifland](stifland)

  * | Joined Mar 2009  | Status: Trader | [304 Posts](/search?do=process&provider=Member&searchuser=95566)

yeah, need to turn this one off, jeez.  
have no idea why it started working Dan. lol. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#59](/thread/post/2596990#post2596990 "Post Permalink")

  * Mar 12, 2009 9:44am  Mar 12, 2009 9:44am 

  * [ Dan Johnston](dan*johnston)

  * | Joined May 2008  | Status: Trader | [354 Posts](/search?do=process&provider=Member&searchuser=69420)

> [Quoting paradoxical](/thread/post/2596978#post2596978 "View Quoted Post")
> 
> Disliked
> 
> Recently came across this thread and see the EA is working like a charm. Am trying it on demo from 0 to 23 hours (I need an hours rest), and with a take profit of 100.   
>  BUT...No trades after 15 minutes? Anyone know what might be wrong with my EA? (just kidding). Looking forward to the same results (100%) as SIOBI, or even as good as Dan Johnson, and will be ready to go live next week at 100 lots a pop!
> 
> Ignored

Hehehe. If this doesn't work out for you, HBO's short on comedians my friend.![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)  
Good ones anyway.![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#60](/thread/post/2596994#post2596994 "Post Permalink")

  * Mar 12, 2009 9:47am  Mar 12, 2009 9:47am 

  * [ Dan Johnston](dan*johnston)

  * | Joined May 2008  | Status: Trader | [354 Posts](/search?do=process&provider=Member&searchuser=69420)

> [Quoting stifland](/thread/post/2596989#post2596989 "View Quoted Post")
> 
> Disliked
> 
> yeah, need to turn this one off, jeez.  
>  have no idea why it started working Dan. lol.
> 
> Ignored

Oh s%#t. It was me that suggested that you put it on lower timeframes, .......**__and different pairs__**. LOL  
  
....Didn't know you were **LIVE!![](https://resources.faireconomy.media/images/emojis/64/1f923.png?v=15.1)**

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * FX_30M Bouncing System
  *   * [ **Reply to Thread** ](/thread/157406-fx30m-bouncing-system/reply#reply)

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

[The Bouncing Pip](/thread/88277-the-bouncing-pip "Hi everyone. 
 
I present to you a system called &quot;The Bouncing Pip&quot; 
 
This is a system that was originally developed by BigBear, so full...") 26 replies

[Price bouncing off of sma](/thread/228922-price-bouncing-off-of-sma "What is the logic behind a price bouncing off an SMA? 
 
For example if a price bounces of a 35 day sma, i should short it if bounces of...") 2 replies

[Developing a correlated bouncing system](/thread/158016-developing-a-correlated-bouncing-system "The above indicator is a simple ma indicator with the weekly ma set to 40. 
 
I like most of my bouncing signals to be in the direction of...") 9 replies

[bouncing candle indicator](/thread/105826-bouncing-candle-indicator "I once had an indicator that would  send  off an alert whenever a candle touched back on its  moving average.  Lost it somehow, but I do...") 0 replies

[Price bouncing off support or resistance,your thoughts](/thread/30984-price-bouncing-off-support-or-resistanceyour-thoughts "I would like to start a discussuion about price movement at support/resistance, Fib and pivot levels.  
  
Time and again I see the price...") 11 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/157406-fx30m-bouncing-system/reply#reply)
  * Subscribe
  * [72](javascript:void\(0\);)

Attachments: FX_30M Bouncing System

Tags: FX_30M Bouncing System

#  [](/thread/157406-fx30m-bouncing-system)FX_30M Bouncing System 

  * 

  * [#61](/thread/post/2597010#post2597010 "Post Permalink")

  * Mar 12, 2009 9:53am  Mar 12, 2009 9:53am 

  * [ paradoxical](paradoxical)

  * | Joined Nov 2007  | Status: Trader | [1,186 Posts](/search?do=process&provider=Member&searchuser=54706)

Someone said "it was working", and I went to check to see if it opened any trades on MY account, and none made. It's been a whole 30 minutes, and NO trades. My EA must be broken. Dan, if I sent you my settings, and my history file, and my life story, along with my laptop, could you tell me what's wrong!?#@!  
I do stand up comedy, but for forex boards, I do it sitting down. Let's all have fun and keep on winning. Let the games BEGIN! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#62](/thread/post/2597027#post2597027 "Post Permalink")

  * Mar 12, 2009 10:02am  Mar 12, 2009 10:02am 

  * [ Dan Johnston](dan*johnston)

  * | Joined May 2008  | Status: Trader | [354 Posts](/search?do=process&provider=Member&searchuser=69420)

HAHA. Yes, what he said:  
  
_**"Let the games BEGIN!"**_  
  
And yes, do send the laptop. Will PM you where.![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)  
  
...Ok, ...back to making millions of demo pips!   
  
Let's get serious now. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#63](/thread/post/2597038#post2597038 "Post Permalink")

  * Mar 12, 2009 10:19am  Mar 12, 2009 10:19am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar95566_5.gif) stifland](stifland)

  * | Joined Mar 2009  | Status: Trader | [304 Posts](/search?do=process&provider=Member&searchuser=95566)

yeah, it's all your fault, I will send my address so you can send a check. Stick around folks, I'll be here allll week!  
How do eat an elephant or an upside down market?  
  
  
And, I thought the Asian market was Quiet! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#64](/thread/post/2597043#post2597043 "Post Permalink")

  * Mar 12, 2009 10:23am  Mar 12, 2009 10:23am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83889_5.gif) siobi](siobi)

  * | Joined Oct 2008  | Status: Trader | [717 Posts](/search?do=process&provider=Member&searchuser=83889)

just got exited !!!! -50 pip !!! pain...pain... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#65](/thread/post/2597051#post2597051 "Post Permalink")

  * Mar 12, 2009 10:28am  Mar 12, 2009 10:28am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar91849_4.gif) royconnell](royconnell)

  * | Joined Jan 2009  | Status: Trader | [10 Posts](/search?do=process&provider=Member&searchuser=91849)

i just got exited too. thought i did something wrong, but AUD news moved the markets 

"If we knew what we were doing we wouldn't call it research." A. Einstein

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#66](/thread/post/2597059#post2597059 "Post Permalink")

  * Mar 12, 2009 10:32am  Mar 12, 2009 10:32am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83889_5.gif) siobi](siobi)

  * | Joined Oct 2008  | Status: Trader | [717 Posts](/search?do=process&provider=Member&searchuser=83889)

I'm pain because I trade live... dont tell u u too............  
  
pain pain.... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#67](/thread/post/2597060#post2597060 "Post Permalink")

  * Mar 12, 2009 10:33am  Mar 12, 2009 10:33am 

  * [ Dan Johnston](dan*johnston)

  * | Joined May 2008  | Status: Trader | [354 Posts](/search?do=process&provider=Member&searchuser=69420)

> [Quoting siobi](/thread/post/2597043#post2597043 "View Quoted Post")
> 
> Disliked
> 
> just got exited !!!! -50 pip !!! pain...pain...
> 
> Ignored

I'm still in!![](https://resources.faireconomy.media/images/emojis/64/1f61c.png?v=15.1) **_Edit: Oh sorry, forgot you're live!_**   
  
On some accounts that still have the 100pip stop, anyway.  
  
I think it did what I did the other day. Meant to press the buy and pressed the sell instead. Not doing that in live acc. that fo sho!!!!!!!![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#68](/thread/post/2597063#post2597063 "Post Permalink")

  * Mar 12, 2009 10:35am  Mar 12, 2009 10:35am 

  * [ paradoxical](paradoxical)

  * | Joined Nov 2007  | Status: Trader | [1,186 Posts](/search?do=process&provider=Member&searchuser=54706)

What!??? A loss?? It was something like 7 and 0, and not more than an hour after I come on board, a LOSS? I must have jinxed it. I better move on to an EA that never loses. OOPS. I forgot. It loses as soon as I get there!

> [Quoting siobi](/thread/post/2597043#post2597043 "View Quoted Post")
> 
> Disliked
> 
> just got exited !!!! -50 pip !!! pain...pain...
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#69](/thread/post/2597065#post2597065 "Post Permalink")

  * Mar 12, 2009 10:36am  Mar 12, 2009 10:36am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar95566_5.gif) stifland](stifland)

  * | Joined Mar 2009  | Status: Trader | [304 Posts](/search?do=process&provider=Member&searchuser=95566)

well, i must sally forth to "the theater" to get my daughter. I'll check in around 10:30 central and see how this turns out for the dumbass Louisiana 1 minute trader![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#70](/thread/post/2597072#post2597072 "Post Permalink")

  * Mar 12, 2009 10:38am  Mar 12, 2009 10:38am 

  * [ Dan Johnston](dan*johnston)

  * | Joined May 2008  | Status: Trader | [354 Posts](/search?do=process&provider=Member&searchuser=69420)

Yea, but made so much it was bound to give a little back.  
  
I hope your account grew to the point where you can easily take this loss Siobi. Still not fun I know from a bit of bad experience live too.  
  
You'll make it back one way or the other, if I can help it anyway!![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#71](/thread/post/2597074#post2597074 "Post Permalink")

  * Edited 10:51am  Mar 12, 2009 10:39am | Edited 10:51am 

  * [ Dan Johnston](dan*johnston)

  * | Joined May 2008  | Status: Trader | [354 Posts](/search?do=process&provider=Member&searchuser=69420)

> [Quoting paradoxical](/thread/post/2597063#post2597063 "View Quoted Post")
> 
> Disliked
> 
> What!??? A loss?? It was something like 7 and 0, and not more than an hour after I come on board, a LOSS? I must have jinxed it. I better move on to an EA that never loses. OOPS. I forgot. It loses as soon as I get there!
> 
> Ignored

9 and 0 for me.  
  
It has made $3930 (9 trades) in one week on a $5k account demo -had I used same lots as I do now from beginning -, so giving $500 back to the market is not bad at all. Yes, I know overleveraged a bit, but hey if it keeps this up....even with the one loss....  
  
....As long as it doesn't do it often enough to eat the amazing gains! 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: v104fxdd3 11b09.gif
Size: 42 KB](/attachment/image/217296/thumbnail?d=1365564796)](/attachment/image/217296?d=1236822232)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#72](/thread/post/2597290#post2597290 "Post Permalink")

  * Mar 12, 2009 12:49pm  Mar 12, 2009 12:49pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar95566_5.gif) stifland](stifland)

  * | Joined Mar 2009  | Status: Trader | [304 Posts](/search?do=process&provider=Member&searchuser=95566)

still in.............triple top? hope, hope. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#73](/thread/post/2597316#post2597316 "Post Permalink")

  * Mar 12, 2009 12:57pm  Mar 12, 2009 12:57pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83889_5.gif) siobi](siobi)

  * | Joined Oct 2008  | Status: Trader | [717 Posts](/search?do=process&provider=Member&searchuser=83889)

wow wow... i think u better exit the SHORT position....seems like it gonna climb high to 1.2888, which is 32 pip from now.  
  
godd luck 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#74](/thread/post/2597654#post2597654 "Post Permalink")

  * Mar 12, 2009 4:23pm  Mar 12, 2009 4:23pm 

  * [ censura](censura)

  * | Joined Sep 2006  | Status: Trader | [405 Posts](/search?do=process&provider=Member&searchuser=17875)

hi hope you can help , i loaded template indicators and ea all looks fine, have smile face and all correct boxs ticked i am with [fxpro](/brokers/fxpro "View FxPro Broker Profile") 5digit broker so set num of digit to true. looked in log and got this any ideas 

Attached File(s)

![File Type: zip](https://assets.faireconomy.media/images/attach/zip.gif) [untitled.zip](/attachment/file/217451?d=1236842596) 65 KB | 455 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#75](/thread/post/2597687#post2597687 "Post Permalink")

  * Mar 12, 2009 4:46pm  Mar 12, 2009 4:46pm 

  * [ kramlon](kramlon)

  * | Joined Sep 2007  | Status: Trader | [52 Posts](/search?do=process&provider=Member&searchuser=48919)

It was changed for "true" of course, still no trades.  
  

> [Quoting Dan Johnston](/thread/post/2596477#post2596477 "View Quoted Post")
> 
> Disliked
> 
> Look at "remark digit" in ea properties. I think "true" for 5 digit.
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#76](/thread/post/2597758#post2597758 "Post Permalink")

  * Mar 12, 2009 5:28pm  Mar 12, 2009 5:28pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83889_5.gif) siobi](siobi)

  * | Joined Oct 2008  | Status: Trader | [717 Posts](/search?do=process&provider=Member&searchuser=83889)

yes, till now no trade,  
today only having 1 valid signal which is at 00:00 ibfx time 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#77](/thread/post/2597826#post2597826 "Post Permalink")

  * Mar 12, 2009 5:55pm  Mar 12, 2009 5:55pm 

  * [ kramlon](kramlon)

  * | Joined Sep 2007  | Status: Trader | [52 Posts](/search?do=process&provider=Member&searchuser=48919)

Siobi, could you please check the code once again as it doesn't work on 5 digits brokers. Thanks.  
  

> [Quoting siobi](/thread/post/2597758#post2597758 "View Quoted Post")
> 
> Disliked
> 
> yes, till now no trade,  
>  today only having 1 valid signal which is at 00:00 ibfx time
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#78](/thread/post/2597831#post2597831 "Post Permalink")

  * Mar 12, 2009 5:57pm  Mar 12, 2009 5:57pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83889_5.gif) siobi](siobi)

  * | Joined Oct 2008  | Status: Trader | [717 Posts](/search?do=process&provider=Member&searchuser=83889)

> [Quoting kramlon](/thread/post/2597826#post2597826 "View Quoted Post")
> 
> Disliked
> 
> Siobi, could you please check the code once again as it doesn't work on 5 digits brokers. Thanks.
> 
> Ignored

arh... I dont have alpari with me... can it be later?  
  
bz with dan's request.... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#79](/thread/post/2597972#post2597972 "Post Permalink")

  * Mar 12, 2009 6:57pm  Mar 12, 2009 6:57pm 

  * [ kramlon](kramlon)

  * | Joined Sep 2007  | Status: Trader | [52 Posts](/search?do=process&provider=Member&searchuser=48919)

Yes, sure. I think some more traders have the same problem with their 5 digits brokers. Just let us know what was the problem.  
  
Thanks a lot.  
  

> [Quoting siobi](/thread/post/2597831#post2597831 "View Quoted Post")
> 
> Disliked
> 
> arh... I dont have alpari with me... can it be later?  
>    
>  bz with dan's request....
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#80](/thread/post/2598207#post2598207 "Post Permalink")

  * Mar 12, 2009 9:15pm  Mar 12, 2009 9:15pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar95566_5.gif) stifland](stifland)

  * | Joined Mar 2009  | Status: Trader | [304 Posts](/search?do=process&provider=Member&searchuser=95566)

I'm sure your all on pins and needles how those trades came out. wel, 5 for 5 actually so 100 sl did job although if it had been regular account I would have been $&%@ing bricks![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1). Will be back mid-morning with usual round of questions. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: okwhew.gif
Size: 94 KB](/attachment/image/217602/thumbnail?d=1365564849)](/attachment/image/217602?d=1236860112)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * FX_30M Bouncing System
  *   * [ **Reply to Thread** ](/thread/157406-fx30m-bouncing-system/reply#reply)

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

[The Bouncing Pip](/thread/88277-the-bouncing-pip "Hi everyone. 
 
I present to you a system called &quot;The Bouncing Pip&quot; 
 
This is a system that was originally developed by BigBear, so full...") 26 replies

[Price bouncing off of sma](/thread/228922-price-bouncing-off-of-sma "What is the logic behind a price bouncing off an SMA? 
 
For example if a price bounces of a 35 day sma, i should short it if bounces of...") 2 replies

[Developing a correlated bouncing system](/thread/158016-developing-a-correlated-bouncing-system "The above indicator is a simple ma indicator with the weekly ma set to 40. 
 
I like most of my bouncing signals to be in the direction of...") 9 replies

[bouncing candle indicator](/thread/105826-bouncing-candle-indicator "I once had an indicator that would  send  off an alert whenever a candle touched back on its  moving average.  Lost it somehow, but I do...") 0 replies

[Price bouncing off support or resistance,your thoughts](/thread/30984-price-bouncing-off-support-or-resistanceyour-thoughts "I would like to start a discussuion about price movement at support/resistance, Fib and pivot levels.  
  
Time and again I see the price...") 11 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/157406-fx30m-bouncing-system/reply#reply)
  * Subscribe
  * [72](javascript:void\(0\);)

Attachments: FX_30M Bouncing System

Tags: FX_30M Bouncing System

#  [](/thread/157406-fx30m-bouncing-system)FX_30M Bouncing System 

  * 

  * [#81](/thread/post/2598395#post2598395 "Post Permalink")

  * Mar 12, 2009 10:23pm  Mar 12, 2009 10:23pm 

  * [ paradoxical](paradoxical)

  * | Joined Nov 2007  | Status: Trader | [1,186 Posts](/search?do=process&provider=Member&searchuser=54706)

Happy to report that the EA opened one trade while I was asleep, at 12:00 IBFX time, and it was a winner for 13 pips after the 15 trail stop hit. Good to know that the EA works without a problem, and nice to start off with a winner. Planning my retirement on Wakiki now. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#82](/thread/post/2598420#post2598420 "Post Permalink")

  * Mar 12, 2009 10:28pm  Mar 12, 2009 10:28pm 

  * [ Dan Johnston](dan*johnston)

  * | Joined May 2008  | Status: Trader | [354 Posts](/search?do=process&provider=Member&searchuser=69420)

> [Quoting paradoxical](/thread/post/2598395#post2598395 "View Quoted Post")
> 
> Disliked
> 
> Happy to report that the EA opened one trade while I was asleep, at 12:00 IBFX time, and it was a winner for 13 pips after the 15 trail stop hit. Good to know that the EA works without a problem, and nice to start off with a winner. Planning my retirement on Wakiki now.
> 
> Ignored

Starting to come around to our way of thinking are you??!! LOL  
....Now watch how **I** jinxed us now.... 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: v104fxdd3 1209.gif
Size: 45 KB](/attachment/image/217654/thumbnail?d=1365564849)](/attachment/image/217654?d=1236864483)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#83](/thread/post/2598539#post2598539 "Post Permalink")

  * Mar 12, 2009 10:52pm  Mar 12, 2009 10:52pm 

  * [ Dan Johnston](dan*johnston)

  * | Joined May 2008  | Status: Trader | [354 Posts](/search?do=process&provider=Member&searchuser=69420)

I originally asked Siobi to develop a 1m/5m scalping ea for **me** according to my rules - _which of course are not really my rules_. Just my take on some other wonderful soul here at FF.  
  
I am starting to believe that some of the "personality" of the ea that I asked him to code, could perhaps be transplanted to the current v104 to make it even better. What I mean by better, is a bit better entries to combat the large stop loss that we MAY need at this point. (The largest draw down encountered thus far I believe is approx. 67 pips. Usually it's much less.)   
  
Even so, as I stated to Siobi, yesterday's trade was in the wrong direction in my opinion and according to the indicators - yea, I know that dirty word **indicators -** lagging at that![](https://resources.faireconomy.media/images/emojis/64/1f61c.png?v=15.1) \- on my chart.  
  
In my humble opinion, _perhaps_ v104 hug the slope direction more closely and also look for stochastic crosses - which yesterday would have kept it on the right side of that "ultimately winning" but "initially losing" trade.   
  
We can get our 20 or more pips by experiencing less of that SH***ING BRICKS feeling by maybe tweaking our entries.   
  
In other words why go 3 hard rounds in an ultimate fight when you can get a first minute of the first round knockout. ...Yea, I know easier said than done.  
  
It has been stated that exits are more important than entries, but in my humble opinion, that is not alway true. In our case we more or less have exits covered to the point that if we enter better, we make money quick and without excessive DD.  
  
I think we are on our way to achieving that with Siobi at the helm.  
  
....Destination Waikiki!!!!![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#84](/thread/post/2598978#post2598978 "Post Permalink")

  * Mar 13, 2009 12:31am  Mar 13, 2009 12:31am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar95566_5.gif) stifland](stifland)

  * | Joined Mar 2009  | Status: Trader | [304 Posts](/search?do=process&provider=Member&searchuser=95566)

waikiki is very crowded and commercial. Maybe one of the outer islands would be better. I know someone asked Dan, but if you or Siobi could give us a basic understanding of when and why the ea takes an entry, it would help as we all apply noodle power to it. Wouldn't want to stray too far as it seems to be very, very nice already. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#85](/thread/post/2599207#post2599207 "Post Permalink")

  * Mar 13, 2009 1:27am  Mar 13, 2009 1:27am 

  * [ Dan Johnston](dan*johnston)

  * | Joined May 2008  | Status: Trader | [354 Posts](/search?do=process&provider=Member&searchuser=69420)

> [Quoting stifland](/thread/post/2598978#post2598978 "View Quoted Post")
> 
> Disliked
> 
> waikiki is very crowded and commercial. Maybe one of the outer islands would be better. I know someone asked Dan, but if you or Siobi could give us a basic understanding of when and why the ea takes an entry, it would help as we all apply noodle power to it. Wouldn't want to stray too far as it seems to be very, very nice already.
> 
> Ignored

Well, we know that it uses the following indicators according to the template:  
  
Slope dir. line  
Stoch RSI  
50sma  
psar  
and it checks adx on 1m-15m depending on whether it's r7 or r8  
  
We should next plot some trades and try to glean any direct insights if possible;  
  
**EDIT; Actually second to last trade (the sell) I thought was a buy and it actually is the opposite of what it should have done. That I think is the losing trade we had. .....Getting confused with all the mt4 instances I have running on 2 comps, so sorry for the mixup.**

Attached Image (click to enlarge)

[![Click to Enlarge

Name: v104 template 3 12 09.gif
Size: 64 KB](/attachment/image/217743/thumbnail?d=1365564885)](/attachment/image/217743?d=1236875220)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#86](/thread/post/2599208#post2599208 "Post Permalink")

  * Mar 13, 2009 1:28am  Mar 13, 2009 1:28am 

  * [ paradoxical](paradoxical)

  * | Joined Nov 2007  | Status: Trader | [1,186 Posts](/search?do=process&provider=Member&searchuser=54706)

I'm with you. I just came across this thread, so I know very little about it. Was/is there another thread that discusses it in more detail?

> [Quoting stifland](/thread/post/2598978#post2598978 "View Quoted Post")
> 
> Disliked
> 
> waikiki is very crowded and commercial. Maybe one of the outer islands would be better. I know someone asked Dan, but if you or Siobi could give us a basic understanding of when and why the ea takes an entry, it would help as we all apply noodle power to it. Wouldn't want to stray too far as it seems to be very, very nice already.
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#87](/thread/post/2599242#post2599242 "Post Permalink")

  * Mar 13, 2009 1:36am  Mar 13, 2009 1:36am 

  * [ Dan Johnston](dan*johnston)

  * | Joined May 2008  | Status: Trader | [354 Posts](/search?do=process&provider=Member&searchuser=69420)

Yes, this is the last page of the previous thread:  
  
[http://www.forexfactory.com/showthre...139685&page=47](http://www.forexfactory.com/showthread.php?t=139685&page=47)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#88](/thread/post/2599271#post2599271 "Post Permalink")

  * Mar 13, 2009 1:43am  Mar 13, 2009 1:43am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar95566_5.gif) stifland](stifland)

  * | Joined Mar 2009  | Status: Trader | [304 Posts](/search?do=process&provider=Member&searchuser=95566)

OK, i will study a bit more on it. I don't get those entry arrows in hindsight. I am set outside trading time right now so maybe that's it. 1 more thing. I am taking a new j.o.b. tomorrow--a 9 to fiver. uggh. so I will only be here Asian sessions which I guess is perfect for Siobi-san. So my fxdd starts day at 0000 at 4 central. Is that Asian open?? And if there was news at 0400. I guess i could open 1 chart start=0, close=3 or manual. Then a second chart start at 5 stop at 10. In case I wasn't here for example.  
Also, will the 30 minute take the 5 different entries like the 1 did yesterday?  
OK, enough question. LUNCH. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#89](/thread/post/2599277#post2599277 "Post Permalink")

  * Mar 13, 2009 1:45am  Mar 13, 2009 1:45am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar95566_5.gif) stifland](stifland)

  * | Joined Mar 2009  | Status: Trader | [304 Posts](/search?do=process&provider=Member&searchuser=95566)

oh yeah, i still need yin-yang setup lol. Buy you a pina colada in Maui 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#90](/thread/post/2599293#post2599293 "Post Permalink")

  * Mar 13, 2009 1:49am  Mar 13, 2009 1:49am 

  * [ Dan Johnston](dan*johnston)

  * | Joined May 2008  | Status: Trader | [354 Posts](/search?do=process&provider=Member&searchuser=69420)

I may be wrong, but upon further reflection of that losing trade (the sell posted above) which I mistakenly called a good trade on the chart, may have been seen by the ea as a continuation of the previous down move. Although the stoch rsi was bottomed and starting to go up as it took that sell.  
Maybe dinapoli stoch cross etc. would further help it to stay with the trend, as we are only targeting 20 pips not 200.  
  
One can make a case for that, since it continued up for 67 pips or so and kept bumping up against some kind of resistance and then proceeded to continue down.  
  
Only problem is the 67 pip drawdown!  
  
We shall see. Maybe with 100 pip stop loss we will never see it hit!!!![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)  
  
One can hope!!! ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)  
  
And I hope none of us gives up on trying to find the answer to making consistent pips.   
  
**We can do this!!!!**

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#91](/thread/post/2599303#post2599303 "Post Permalink")

  * Mar 13, 2009 1:52am  Mar 13, 2009 1:52am 

  * [ paradoxical](paradoxical)

  * | Joined Nov 2007  | Status: Trader | [1,186 Posts](/search?do=process&provider=Member&searchuser=54706)

Thanks, Dan. I will check it out.

> [Quoting Dan Johnston](/thread/post/2599242#post2599242 "View Quoted Post")
> 
> Disliked
> 
> Yes, this is the last page of the previous thread:  
>    
>  [http://www.forexfactory.com/showthre...139685&page=47](http://www.forexfactory.com/showthread.php?t=139685&page=47)
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#92](/thread/post/2599589#post2599589 "Post Permalink")

  * Mar 13, 2009 3:34am  Mar 13, 2009 3:34am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar95566_5.gif) stifland](stifland)

  * | Joined Mar 2009  | Status: Trader | [304 Posts](/search?do=process&provider=Member&searchuser=95566)

ok, i don't see any medium or high impact jpy news today. there is some for nzd but I don't know the correlation there.  
Going to set start and stop for 30m at 0 (4 central) and stop at 8 with close at 9 at euro open.  
see what happens. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#93](/thread/post/2599628#post2599628 "Post Permalink")

  * Mar 13, 2009 3:53am  Mar 13, 2009 3:53am 

  * [ andypips](andypips)

  * | Joined Mar 2008  | Status: Trader | [228 Posts](/search?do=process&provider=Member&searchuser=64512)

Hi Guys  
I would like to ask for some help with the techy side of the EA.   
Having never used an EA , I loaded and ran it today. I have all the right boxes checked and ticked and smiley face on the top of my chart. I may be wrong here but thought that the ea would open the trade for me. What i got on the last m30 candle (not the current one) was a buy signal popped up in a window to buy at 1.2833. I did that manually and the d/down was -20 but currently around +15. Do I need to do anything else to initiate the automatic entry and closing with this. I don't know yet if it will close me out at 20 as its not yet there and the trailing stop doesn't seem to be working either.   
Any help would be most useful  
Yours  
Andy  
  
edit: the mt4 keeps throwing out a modified stop loss to confirm very much like the trailing stop would do on its own. it didn't close out and i now have been closed for +27. If I can just work out the above it seems very good. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#94](/thread/post/2599631#post2599631 "Post Permalink")

  * Mar 13, 2009 3:54am  Mar 13, 2009 3:54am 

  * [ Dan Johnston](dan*johnston)

  * | Joined May 2008  | Status: Trader | [354 Posts](/search?do=process&provider=Member&searchuser=69420)

Currently in a buy at +9 pips.  
  
I would have entered sooner, but let's see what happens.  
  
...Ok, got it's 20 pips, and another account that has no TP is still going up I think.  
  
That acc. stopped out at 20 pips and had a high of another 13 pips or so.  
  
![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#95](/thread/post/2599688#post2599688 "Post Permalink")

  * Edited 4:20am  Mar 13, 2009 4:10am | Edited 4:20am 

  * [ Dan Johnston](dan*johnston)

  * | Joined May 2008  | Status: Trader | [354 Posts](/search?do=process&provider=Member&searchuser=69420)

> [Quoting andypips](/thread/post/2599628#post2599628 "View Quoted Post")
> 
> Disliked
> 
> Hi Guys  
>  I would like to ask for some help with the techy side of the EA.   
>  Having never used an EA , I loaded and ran it today. I have all the right boxes checked and ticked and smiley face on the top of my chart. I may be wrong here but thought that the ea would open the trade for me. What i got on the last m30 candle (not the current one) was a buy signal popped up in a window to buy at 1.2833. I did that manually and the d/down was -20 but currently around +15. Do I need to do anything else to initiate the automatic entry and closing with this....
> 
> Ignored

  
Strange yours entered 7 or so pips sooner than any of mine at 1.2841.  
But who's complaining! Maybe diff. dealer.  
  
If it didn't open trade automatically, maybe go to mt4 "tools", "options", and then check enable expert advisors.  
  
As for the rest, will try to keep an eye to see exactly how the trailing stop works. ...Maybe at +15 we go to breakeven and follow price from there?  
  
That may account for why my acc. that has no TP (20 pips on my others) stopped out at exactly 20, having gone up to 35 or so pips positive then retraced. (Two pip spread factored in there somewhere)  
  
Not sure yet. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#96](/thread/post/2599732#post2599732 "Post Permalink")

  * Mar 13, 2009 4:20am  Mar 13, 2009 4:20am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar95566_5.gif) stifland](stifland)

  * | Joined Mar 2009  | Status: Trader | [304 Posts](/search?do=process&provider=Member&searchuser=95566)

so you must be running 24 hours dan? mine will start at 4cdt. today.. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#97](/thread/post/2599737#post2599737 "Post Permalink")

  * Edited 4:33am  Mar 13, 2009 4:22am | Edited 4:33am 

  * [ Dan Johnston](dan*johnston)

  * | Joined May 2008  | Status: Trader | [354 Posts](/search?do=process&provider=Member&searchuser=69420)

Might as well, and we'll factor out the trades taken during news hrs. later. (Only on demo for now)  
  
Plus I can never get GMT, military, broker, and EST, etc. straight in my head. Not to mention goind on and off Daylight Savings, which recently changed my ibfx and fxdd broker time difference from 2 to 3. When I go live will need help from someone who was in the military and has all that straight. LOL  
  
No NFP Friday though. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#98](/thread/post/2599874#post2599874 "Post Permalink")

  * Mar 13, 2009 5:02am  Mar 13, 2009 5:02am 

  * [ andypips](andypips)

  * | Joined Mar 2008  | Status: Trader | [228 Posts](/search?do=process&provider=Member&searchuser=64512)

Hi Dan.  
Thanks for the answer.   
I was trading this demo with whc/broco so that may explain the difference. The chart has a small blue arrow on at the point of entry alert.   
When I right click on the chart and open ea properties it shows that live trading is allowed. When I went via tools as you suggest then it wasn't enabled in there. I have changed that now. The enable ea is ticked and also disable experts(both of them) are ticked . Is that correct. Hopefully it will enter for me now.   
I have set the inputs to 30, 0, 24, 2, 100, 20 and 15 as was mentioned before.  
Is it ok to move down to m1 to see if it enters for me.? Do I need to change any other parameters to make that happen?  
Thanks  
Andy  
ps. hope your in the mood for all these questions. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#99](/thread/post/2599923#post2599923 "Post Permalink")

  * Mar 13, 2009 5:17am  Mar 13, 2009 5:17am 

  * [ Dan Johnston](dan*johnston)

  * | Joined May 2008  | Status: Trader | [354 Posts](/search?do=process&provider=Member&searchuser=69420)

If I'm at the computer always in the mood to answer if I know the answer.   
  
Many times I just don't know though, and I'll make one up.![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)  
  
Yea, I got everything checked, except ask manual confirm., and confirm DLL function calls.  
  
You can put it on lower timeframes, but you'll know if you're good to go once one of us posts a new trade.  
  
You should be ok. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#100](/thread/post/2599944#post2599944 "Post Permalink")

  * Mar 13, 2009 5:23am  Mar 13, 2009 5:23am 

  * [ andypips](andypips)

  * | Joined Mar 2008  | Status: Trader | [228 Posts](/search?do=process&provider=Member&searchuser=64512)

![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)  
Thanks Dan.  
It doesn't produce as many signals as I would have expected on the m1. In fact none yet.  
I'll sit tight and see if it enters for me.  
andy 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * FX_30M Bouncing System
  *   * [ **Reply to Thread** ](/thread/157406-fx30m-bouncing-system/reply#reply)

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

[The Bouncing Pip](/thread/88277-the-bouncing-pip "Hi everyone. 
 
I present to you a system called &quot;The Bouncing Pip&quot; 
 
This is a system that was originally developed by BigBear, so full...") 26 replies

[Price bouncing off of sma](/thread/228922-price-bouncing-off-of-sma "What is the logic behind a price bouncing off an SMA? 
 
For example if a price bounces of a 35 day sma, i should short it if bounces of...") 2 replies

[Developing a correlated bouncing system](/thread/158016-developing-a-correlated-bouncing-system "The above indicator is a simple ma indicator with the weekly ma set to 40. 
 
I like most of my bouncing signals to be in the direction of...") 9 replies

[bouncing candle indicator](/thread/105826-bouncing-candle-indicator "I once had an indicator that would  send  off an alert whenever a candle touched back on its  moving average.  Lost it somehow, but I do...") 0 replies

[Price bouncing off support or resistance,your thoughts](/thread/30984-price-bouncing-off-support-or-resistanceyour-thoughts "I would like to start a discussuion about price movement at support/resistance, Fib and pivot levels.  
  
Time and again I see the price...") 11 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/157406-fx30m-bouncing-system/reply#reply)
  * Subscribe
  * [72](javascript:void\(0\);)

Attachments: FX_30M Bouncing System

Tags: FX_30M Bouncing System

#  [](/thread/157406-fx30m-bouncing-system)FX_30M Bouncing System 

  * 

  * [#101](/thread/post/2600117#post2600117 "Post Permalink")

  * Mar 13, 2009 6:40am  Mar 13, 2009 6:40am 

  * [ andypips](andypips)

  * | Joined Mar 2008  | Status: Trader | [228 Posts](/search?do=process&provider=Member&searchuser=64512)

Siobi.  
Sorry to clutter up your thread.  
Dan.  
Got it I think. On the common tab on the ea properties i had 'ask manual confirmation' checked. not any longer so should enter on its own now. we will see.   
andy 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#102](/thread/post/2600123#post2600123 "Post Permalink")

  * Mar 13, 2009 6:43am  Mar 13, 2009 6:43am 

  * [ paradoxical](paradoxical)

  * | Joined Nov 2007  | Status: Trader | [1,186 Posts](/search?do=process&provider=Member&searchuser=54706)

I just finished reading the other thread to get a sense of what this is all about. I was a little confused between the EA, and Dan's manual system. Have reloaded the EA onto a new IBFX demo account, as my other one crashed due to too many indicators. Might try this live starting at a dime next week. Who else is live, and what is your success? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#103](/thread/post/2600181#post2600181 "Post Permalink")

  * Edited 7:21am  Mar 13, 2009 7:20am | Edited 7:21am 

  * [ Mungo2](mungo2)

  * | Joined Mar 2009  | Status: Trader | [6 Posts](/search?do=process&provider=Member&searchuser=95488)

Hi. Running it live on IBFX, it doesn't trade often as describe here. It traded (long) around the Swissy news time yesterday. The TS was taken out for +17 lovely pips. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#104](/thread/post/2600295#post2600295 "Post Permalink")

  * Mar 13, 2009 8:45am  Mar 13, 2009 8:45am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar95566_5.gif) stifland](stifland)

  * | Joined Mar 2009  | Status: Trader | [304 Posts](/search?do=process&provider=Member&searchuser=95566)

Hey dudes. I'm back and "inside trading time" No trades here yet. Hope thats right.  
Dan, stop making up answers 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#105](/thread/post/2600335#post2600335 "Post Permalink")

  * Mar 13, 2009 9:10am  Mar 13, 2009 9:10am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar84807_4.gif) todd960960](todd960960)

  * | Joined Nov 2008  | Status: Trader | [470 Posts](/search?do=process&provider=Member&searchuser=84807)

I've had the EA active for 24hrs now and still no trades. Have the settings the same as on page one. Any ideas? Using IBFX and the only thing I changed was lot size.  
  
thx,  
todd 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#106](/thread/post/2600341#post2600341 "Post Permalink")

  * Mar 13, 2009 9:12am  Mar 13, 2009 9:12am 

  * [ paradoxical](paradoxical)

  * | Joined Nov 2007  | Status: Trader | [1,186 Posts](/search?do=process&provider=Member&searchuser=54706)

stifland, I have both EAs for the 15 minute and 30 minute loaded on my IBFX demo account as of an hour or so ago. I'll let the board know of any trades made. All seems fine. 

> [Quoting stifland](/thread/post/2600295#post2600295 "View Quoted Post")
> 
> Disliked
> 
> Hey dudes. I'm back and "inside trading time" No trades here yet. Hope thats right.  
>  Dan, stop making up answers
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#107](/thread/post/2600399#post2600399 "Post Permalink")

  * Mar 13, 2009 9:44am  Mar 13, 2009 9:44am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar95566_5.gif) stifland](stifland)

  * | Joined Mar 2009  | Status: Trader | [304 Posts](/search?do=process&provider=Member&searchuser=95566)

OK, I've got it on a 30 and a 1. Will do the same. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#108](/thread/post/2600420#post2600420 "Post Permalink")

  * Mar 13, 2009 9:57am  Mar 13, 2009 9:57am 

  * [ Dan Johnston](dan*johnston)

  * | Joined May 2008  | Status: Trader | [354 Posts](/search?do=process&provider=Member&searchuser=69420)

> [Quoting todd960960](/thread/post/2600335#post2600335 "View Quoted Post")
> 
> Disliked
> 
> I've had the EA active for 24hrs now and still no trades. Have the settings the same as on page one. Any ideas? Using IBFX and the only thing I changed was lot size.  
>    
>  thx,  
>  todd
> 
> Ignored

Post 98 and thereabouts may help. (mt4 _tools, options,_ check everything except ask manual confirm., and confirm DLL function calls.)  
If not let us know, and we'll get you going.   
  
Just don't take up paradoxical's suggestion that you send him your laptop for him to fix things for you! ![](https://resources.faireconomy.media/images/emojis/64/1f44e.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#109](/thread/post/2600448#post2600448 "Post Permalink")

  * Mar 13, 2009 10:12am  Mar 13, 2009 10:12am 

  * [ qz10cq](qz10cq)

  * | Joined Dec 2006  | Status: Trader | [303 Posts](/search?do=process&provider=Member&searchuser=29720)

Siobi, have your ea on fxdd attached to all pairs under a 10 spread. Have won several and lost a few, eur/usd has been quite lately. My goal is to elimanate the pairs that lose twice and see what I have left in a week or so. Will keep the thread informed. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#110](/thread/post/2600454#post2600454 "Post Permalink")

  * Mar 13, 2009 10:13am  Mar 13, 2009 10:13am 

  * [ paradoxical](paradoxical)

  * | Joined Nov 2007  | Status: Trader | [1,186 Posts](/search?do=process&provider=Member&searchuser=54706)

If this system don't work, my laptop will turned in for a typewriter. I'll give that EA 24 hours to start talking. 

> [Quoting Dan Johnston](/thread/post/2600420#post2600420 "View Quoted Post")
> 
> Disliked
> 
> Post 98 and thereabouts may help. (mt4 _tools, options,_ check everything except ask manual confirm., and confirm DLL function calls.)  
>  If not let us know, and we'll get you going.   
>    
>  Just don't take up paradoxical's suggestion that you send him your laptop for him to fix things for you! ![](https://resources.faireconomy.media/images/emojis/64/1f44e.png?v=15.1)
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#111](/thread/post/2600469#post2600469 "Post Permalink")

  * Mar 13, 2009 10:21am  Mar 13, 2009 10:21am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar95566_5.gif) stifland](stifland)

  * | Joined Mar 2009  | Status: Trader | [304 Posts](/search?do=process&provider=Member&searchuser=95566)

Made 50 pips on eurjpy. total luck I'm afraid. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: eurjpy.gif
Size: 85 KB](/attachment/image/217951/thumbnail?d=1365564939)](/attachment/image/217951?d=1236907261)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#112](/thread/post/2600537#post2600537 "Post Permalink")

  * Mar 13, 2009 11:07am  Mar 13, 2009 11:07am 

  * [ Dan Johnston](dan*johnston)

  * | Joined May 2008  | Status: Trader | [354 Posts](/search?do=process&provider=Member&searchuser=69420)

> [Quoting stifland](/thread/post/2600469#post2600469 "View Quoted Post")
> 
> Disliked
> 
> Made 50 pips on eurjpy. total luck I'm afraid.
> 
> Ignored

  
What did you use for a trailing stop?  
  
That was definitely a good sustained uptrend for the 1m, but at one point, it seems that it would have retraced a little more than the default 15 pip trailing stop, so with those 15m settings some luck must have come into play.  
  
Nice one though. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#113](/thread/post/2600541#post2600541 "Post Permalink")

  * Mar 13, 2009 11:08am  Mar 13, 2009 11:08am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar95566_5.gif) stifland](stifland)

  * | Joined Mar 2009  | Status: Trader | [304 Posts](/search?do=process&provider=Member&searchuser=95566)

wasn't an ea trade. haven't had any Bounce trades since asian session start. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#114](/thread/post/2600551#post2600551 "Post Permalink")

  * Mar 13, 2009 11:12am  Mar 13, 2009 11:12am 

  * [ Dan Johnston](dan*johnston)

  * | Joined May 2008  | Status: Trader | [354 Posts](/search?do=process&provider=Member&searchuser=69420)

> [Quoting stifland](/thread/post/2600541#post2600541 "View Quoted Post")
> 
> Disliked
> 
> wasn't an ea trade. haven't had any Bounce trades since asian session start.
> 
> Ignored

Keep it up, and I'll be asking you to trade my acc. for me. ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#115](/thread/post/2600597#post2600597 "Post Permalink")

  * Mar 13, 2009 11:38am  Mar 13, 2009 11:38am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83889_5.gif) siobi](siobi)

  * | Joined Oct 2008  | Status: Trader | [717 Posts](/search?do=process&provider=Member&searchuser=83889)

keep it up... coz I also need you to trade my acct later if you keep up the good work ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#116](/thread/post/2600635#post2600635 "Post Permalink")

  * Mar 13, 2009 12:04pm  Mar 13, 2009 12:04pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar95566_5.gif) stifland](stifland)

  * | Joined Mar 2009  | Status: Trader | [304 Posts](/search?do=process&provider=Member&searchuser=95566)

lol, question siobi. If I am in a eur trade on another chart manually. will that impact the Bouncing EA? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#117](/thread/post/2600647#post2600647 "Post Permalink")

  * Mar 13, 2009 12:19pm  Mar 13, 2009 12:19pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83889_5.gif) siobi](siobi)

  * | Joined Oct 2008  | Status: Trader | [717 Posts](/search?do=process&provider=Member&searchuser=83889)

Hi there,  
this EA will not interfere withmanual trade. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#118](/thread/post/2601455#post2601455 "Post Permalink")

  * Mar 13, 2009 7:50pm  Mar 13, 2009 7:50pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar43332_2.gif) willmalou](willmalou)

  * | Joined Jul 2007  | Status: Think before you act!!! | [113 Posts](/search?do=process&provider=Member&searchuser=43332)

These are the trades the EA made the last two days. I have one on 30M and the other on 1M. The 1M I only has run for 1 day. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: fx_30.JPG
Size: 176 KB](/attachment/image/218192/thumbnail?d=1365564966)](/attachment/image/218192?d=1236941406)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#119](/thread/post/2601607#post2601607 "Post Permalink")

  * Mar 13, 2009 9:22pm  Mar 13, 2009 9:22pm 

  * [ paradoxical](paradoxical)

  * | Joined Nov 2007  | Status: Trader | [1,186 Posts](/search?do=process&provider=Member&searchuser=54706)

No trades yet on my V104 and V106 EAs. 

> [Quoting willmalou](/thread/post/2601455#post2601455 "View Quoted Post")
> 
> Disliked
> 
> These are the trades the EA made the last two days. I have one on 30M and the other on 1M. The 1M I only has run for 1 day.
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#120](/thread/post/2601725#post2601725 "Post Permalink")

  * Mar 13, 2009 10:07pm  Mar 13, 2009 10:07pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar95566_5.gif) stifland](stifland)

  * | Joined Mar 2009  | Status: Trader | [304 Posts](/search?do=process&provider=Member&searchuser=95566)

i did not fire any trades last night in asian session. Off to new job. woohoo!:nerd: 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * FX_30M Bouncing System
  *   * [ **Reply to Thread** ](/thread/157406-fx30m-bouncing-system/reply#reply)

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

[The Bouncing Pip](/thread/88277-the-bouncing-pip "Hi everyone. 
 
I present to you a system called &quot;The Bouncing Pip&quot; 
 
This is a system that was originally developed by BigBear, so full...") 26 replies

[Price bouncing off of sma](/thread/228922-price-bouncing-off-of-sma "What is the logic behind a price bouncing off an SMA? 
 
For example if a price bounces of a 35 day sma, i should short it if bounces of...") 2 replies

[Developing a correlated bouncing system](/thread/158016-developing-a-correlated-bouncing-system "The above indicator is a simple ma indicator with the weekly ma set to 40. 
 
I like most of my bouncing signals to be in the direction of...") 9 replies

[bouncing candle indicator](/thread/105826-bouncing-candle-indicator "I once had an indicator that would  send  off an alert whenever a candle touched back on its  moving average.  Lost it somehow, but I do...") 0 replies

[Price bouncing off support or resistance,your thoughts](/thread/30984-price-bouncing-off-support-or-resistanceyour-thoughts "I would like to start a discussuion about price movement at support/resistance, Fib and pivot levels.  
  
Time and again I see the price...") 11 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/157406-fx30m-bouncing-system/reply#reply)
  * Subscribe
  * [72](javascript:void\(0\);)

Attachments: FX_30M Bouncing System

Tags: FX_30M Bouncing System

#  [](/thread/157406-fx30m-bouncing-system)FX_30M Bouncing System 

  * 

  * [#121](/thread/post/2601738#post2601738 "Post Permalink")

  * Mar 13, 2009 10:13pm  Mar 13, 2009 10:13pm 

  * [ paradoxical](paradoxical)

  * | Joined Nov 2007  | Status: Trader | [1,186 Posts](/search?do=process&provider=Member&searchuser=54706)

OK, stifland. Congrats on your new job, too. Anyone working today should consider themselves fortunate.

> [Quoting stifland](/thread/post/2601725#post2601725 "View Quoted Post")
> 
> Disliked
> 
> i did not fire any trades last night in asian session. Off to new job. woohoo!:nerd:
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#122](/thread/post/2601752#post2601752 "Post Permalink")

  * Mar 13, 2009 10:17pm  Mar 13, 2009 10:17pm 

  * [ Dan Johnston](dan*johnston)

  * | Joined May 2008  | Status: Trader | [354 Posts](/search?do=process&provider=Member&searchuser=69420)

One of my accounts seems to have a "magic touch" so far.  
The others have been stopped out with 50 sl, and last trade still running I suppose if using 100 pip sl.  
  
Anyone still have that ibfx 1.2949 buy still running waiting to hit the 100 pip stop, or 20 tp? (v104r**8**) 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: v104fxdd3 1309.gif
Size: 48 KB](/attachment/image/218241/thumbnail?d=1365565001)](/attachment/image/218241?d=1236950188)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#123](/thread/post/2601800#post2601800 "Post Permalink")

  * Mar 13, 2009 10:37pm  Mar 13, 2009 10:37pm 

  * [ FXPuppy](fxpuppy)

  * | Joined Apr 2006  | Status: Trader | [13 Posts](/search?do=process&provider=Member&searchuser=8196)

Hello Siobi,  
  
I recently came across this thread and decided to join it. Thanks for the EA and all the support that you are providing. It is greatly appreciated.  
  
I have copied the indicators, EA, and template from post #1 on two different computers running demos from two different brokers, one with 5 decimals ([FxPro](/brokers/fxpro "View FxPro Broker Profile")) and the other with 4 decimals ([Forex.com](/brokers/forexcom "View FOREX.com Broker Profile")). On EurUsd 30Min, the EA settings are as follow:  
Lots 0.5  
Num_Of_Digit true (for 5 decimal account), false for the other  
Close Hour 11  
HourStart 0  
HourEnd 24 (tried different times)  
Spread 2  
StopLoss 100  
TakeProfit 20  
TrailingStop 15  
  
On FxPro demo the EA is running since Monday Mar 9th, I have no trades. I run Strategy Tester from Mar 2 to 6 no trades and no errors reported on the Journal tab.  
  
Today I started running the EA on Forex.com demo, no trades yet. The Strategy Tester from Mar 8 to 10 reported 3 “Order Send error 130” errors in the Journal tab.  
  
The smiley face is on and I am running other EAs OK.   
  
Any help is greatly appreciated. Regards  
FxPuppy 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#124](/thread/post/2601802#post2601802 "Post Permalink")

  * Mar 13, 2009 10:38pm  Mar 13, 2009 10:38pm 

  * [ Dan Johnston](dan*johnston)

  * | Joined May 2008  | Status: Trader | [354 Posts](/search?do=process&provider=Member&searchuser=69420)

This is my other v104r7 IBFX (laptop) results.  
Please pay attention only to e/u trades and please note that when it has a losing position (2) it is against slope direction line.  
  
In my opinion, ea must never take a trade AGAINST slope direction line.   
It should take a position soon after the close of the first bar that caused the slope direction line to change color.   
Again imho, doing so will almost always net us the 20 pips we want on the 30M.  
  
I may be wrong, but it should be noted that the losing positions were toward the end of the previous trend. (Missed getting on the bus but grabbed the bumper and got roughed up.) 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: v104r7lapt3 13 09.gif
Size: 66 KB](/attachment/image/218249/thumbnail?d=1365565001)](/attachment/image/218249?d=1236951445)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#125](/thread/post/2601829#post2601829 "Post Permalink")

  * Mar 13, 2009 10:53pm  Mar 13, 2009 10:53pm 

  * [ Dan Johnston](dan*johnston)

  * | Joined May 2008  | Status: Trader | [354 Posts](/search?do=process&provider=Member&searchuser=69420)

Please zoom in and note the last two trades on chart:  
  
In my mind, we should go with the current flow - that being the slope direction line color for 20 pips. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: fapturbo3 13 09.gif
Size: 67 KB](/attachment/image/218254/thumbnail?d=1365565001)](/attachment/image/218254?d=1236952415)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#126](/thread/post/2602026#post2602026 "Post Permalink")

  * Mar 13, 2009 11:52pm  Mar 13, 2009 11:52pm 

  * [ paradoxical](paradoxical)

  * | Joined Nov 2007  | Status: Trader | [1,186 Posts](/search?do=process&provider=Member&searchuser=54706)

Dan, I see your EA took trades recently, whereas mine didn't. I have the v104 and v106 running 24/5. Oh, well, I guess. Can you send me the laptop that your EA works on?

> [Quoting Dan Johnston](/thread/post/2601829#post2601829 "View Quoted Post")
> 
> Disliked
> 
> Please zoom in and note the last two trades on chart:  
>    
>  In my mind, we should go with the current flow - that being the slope direction line color for 20 pips.
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#127](/thread/post/2602080#post2602080 "Post Permalink")

  * Mar 14, 2009 12:09am  Mar 14, 2009 12:09am 

  * [ Dan Johnston](dan*johnston)

  * | Joined May 2008  | Status: Trader | [354 Posts](/search?do=process&provider=Member&searchuser=69420)

LOL. You don't want it.  
  
2 laptops (1 I built from spare parts from ebay)  
2 desktops (1 I built from scratch in 2000, including beautiful aluminum case -products.s5.com - that one you might want old as it is)  
  
And my 2 year old crappy HP desktop "pride and joy" that currently houses the "magical" _**demo**_ ![](https://resources.faireconomy.media/images/emojis/64/1f62d.png?v=15.1)account.) 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#128](/thread/post/2604638#post2604638 "Post Permalink")

  * Mar 16, 2009 5:22am  Mar 16, 2009 5:22am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar95566_5.gif) stifland](stifland)

  * | Joined Mar 2009  | Status: Trader | [304 Posts](/search?do=process&provider=Member&searchuser=95566)

you guys gonna fire up the EA for Sunday evening session?? Or does any potential gap post a risk there. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#129](/thread/post/2604816#post2604816 "Post Permalink")

  * Mar 16, 2009 7:45am  Mar 16, 2009 7:45am 

  * [ Dan Johnston](dan*johnston)

  * | Joined May 2008  | Status: Trader | [354 Posts](/search?do=process&provider=Member&searchuser=69420)

![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)

Attached Image (click to enlarge)

[![Click to Enlarge

Name: v104fxdd3 1509.gif
Size: 46 KB](/attachment/image/218949/thumbnail?d=1365565105)](/attachment/image/218949?d=1237157101)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#130](/thread/post/2604828#post2604828 "Post Permalink")

  * Mar 16, 2009 7:52am  Mar 16, 2009 7:52am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar95566_5.gif) stifland](stifland)

  * | Joined Mar 2009  | Status: Trader | [304 Posts](/search?do=process&provider=Member&searchuser=95566)

yes, prefecto way to start week.  
Fired on 30m and 1m 1 pip apart 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: tradesunday.gif
Size: 80 KB](/attachment/image/218951/thumbnail?d=1365565105)](/attachment/image/218951?d=1237157551)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#131](/thread/post/2604836#post2604836 "Post Permalink")

  * Mar 16, 2009 7:59am  Mar 16, 2009 7:59am 

  * [ paradoxical](paradoxical)

  * | Joined Nov 2007  | Status: Trader | [1,186 Posts](/search?do=process&provider=Member&searchuser=54706)

My EA not taking any trades on V104 or V106. Smiley face on, live trading on....Damn!! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#132](/thread/post/2604839#post2604839 "Post Permalink")

  * Mar 16, 2009 8:01am  Mar 16, 2009 8:01am 

  * [ nickmead](nickmead)

  * | Commercial User  | Joined Feb 2008 | [66 Posts](/search?do=process&provider=Member&searchuser=61524)

I just loaded the EA and it scored a quick 20. Great work. I look foward to watching it this week ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#133](/thread/post/2604843#post2604843 "Post Permalink")

  * Mar 16, 2009 8:03am  Mar 16, 2009 8:03am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar95566_5.gif) stifland](stifland)

  * | Joined Mar 2009  | Status: Trader | [304 Posts](/search?do=process&provider=Member&searchuser=95566)

Just trying to figure out rules still. this 1 minute is active! I know I'm not supposed to trade it Dan! So if you see the 2 short entries, blue slope is UP and PSAR is below. seems odd to short. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: entryquestion.gif
Size: 21 KB](/attachment/image/218955/thumbnail?d=1365565105)](/attachment/image/218955?d=1237158224)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#134](/thread/post/2604880#post2604880 "Post Permalink")

  * Mar 16, 2009 8:37am  Mar 16, 2009 8:37am 

  * [ Dan Johnston](dan*johnston)

  * | Joined May 2008  | Status: Trader | [354 Posts](/search?do=process&provider=Member&searchuser=69420)

> [Quoting stifland](/thread/post/2604843#post2604843 "View Quoted Post")
> 
> Disliked
> 
> Just trying to figure out rules still. this 1 minute is active! I know I'm not supposed to trade it Dan! So if you see the 2 short entries, blue slope is UP and PSAR is below. seems odd to short.
> 
> Ignored

When you have it on 1m it may still be looking at the 30m slope dir. line. Don't know the code, so couldn't say definitively.  
  
r8 also looks at ADX 5 and 15 min, so on the 1m chart to get 20 pips, entries will not look as if they are following the 1m slope dir.  
  
On the 1m, unless it's trending nicely, you will usually not pick up 20 pips before the slope line changes color.   
  
On the 30m it's a whole different ballgame. 20 is not that hard if you enter when there are market participants and you enter early on the slope direction color change. (No narrow ranging market.)  
  
That's _my_ take anyway. I could be wrong. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#135](/thread/post/2604915#post2604915 "Post Permalink")

  * Mar 16, 2009 9:07am  Mar 16, 2009 9:07am 

  * [ paradoxical](paradoxical)

  * | Joined Nov 2007  | Status: Trader | [1,186 Posts](/search?do=process&provider=Member&searchuser=54706)

What the bllep!? You "just" loaded your EA and scored a quick twenty!?@! I've had the EA loaded since Friday, and nothing!?  
The forex gods have it in for me. That's the only answer.

> [Quoting nickmead](/thread/post/2604839#post2604839 "View Quoted Post")
> 
> Disliked
> 
> I just loaded the EA and it scored a quick 20. Great work. I look foward to watching it this week ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#136](/thread/post/2604930#post2604930 "Post Permalink")

  * Mar 16, 2009 9:18am  Mar 16, 2009 9:18am 

  * [ Dan Johnston](dan*johnston)

  * | Joined May 2008  | Status: Trader | [354 Posts](/search?do=process&provider=Member&searchuser=69420)

Results will vary according to r7 or r8 and also different brokers, among other variables.  
  
My results are all over the map also. I do like that fxdd acct. though!  
  
Changed some indicators and templates in it, so I hope I didn't screw it up.   
  
13 and 0 is no joke! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#137](/thread/post/2605043#post2605043 "Post Permalink")

  * Mar 16, 2009 10:41am  Mar 16, 2009 10:41am 

  * [ paradoxical](paradoxical)

  * | Joined Nov 2007  | Status: Trader | [1,186 Posts](/search?do=process&provider=Member&searchuser=54706)

Is there an EA doctor in the house? I need a diagnosis. Dan, how about you and I swapping out laptops? I'll take the one that's 13 and 0, and give you mine after the doctor is done operating on it. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#138](/thread/post/2605059#post2605059 "Post Permalink")

  * Mar 16, 2009 10:48am  Mar 16, 2009 10:48am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar95566_5.gif) stifland](stifland)

  * | Joined Mar 2009  | Status: Trader | [304 Posts](/search?do=process&provider=Member&searchuser=95566)

OK, i think I will eschew the 1m after today. 1 thing I didn't know could happen. I am still short 2 entries and nor long 3 entries!  
It will hedge. Interesting to see how it works out.  
Paradox--do you have other EA's running?? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#139](/thread/post/2605070#post2605070 "Post Permalink")

  * Mar 16, 2009 10:57am  Mar 16, 2009 10:57am 

  * [ Dan Johnston](dan*johnston)

  * | Joined May 2008  | Status: Trader | [354 Posts](/search?do=process&provider=Member&searchuser=69420)

> [Quoting paradoxical](/thread/post/2605043#post2605043 "View Quoted Post")
> 
> Disliked
> 
> Is there an EA doctor in the house? I need a diagnosis. Dan, how about you and I swapping out laptops? I'll take the one that's 13 and 0, and give you mine after the doctor is done operating on it.
> 
> Ignored

LOL.  
  
Yea, but statistically, I'm way past due for a loss.  
  
Watch it come just as I go live!!! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#140](/thread/post/2605074#post2605074 "Post Permalink")

  * Mar 16, 2009 11:00am  Mar 16, 2009 11:00am 

  * [ Dan Johnston](dan*johnston)

  * | Joined May 2008  | Status: Trader | [354 Posts](/search?do=process&provider=Member&searchuser=69420)

> [Quoting stifland](/thread/post/2605059#post2605059 "View Quoted Post")
> 
> Disliked
> 
> OK, i think I will eschew the 1m after today. 1 thing I didn't know could happen. I am still short 2 entries and nor long 3 entries!  
>  It will hedge. Interesting to see how it works out.  
>  Paradox--do you have other EA's running??
> 
> Ignored

That's how I managed to save my first live acct. By hedging. HATED EVERY SINGLE SECOND OF IT!!!!!!!  
  
But managed to only lose 1/3 or so of it, from that quick lesson in hedging.  
  
  
...On one acct. I have a long open at 1.2903. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * FX_30M Bouncing System
  *   * [ **Reply to Thread** ](/thread/157406-fx30m-bouncing-system/reply#reply)

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

[The Bouncing Pip](/thread/88277-the-bouncing-pip "Hi everyone. 
 
I present to you a system called &quot;The Bouncing Pip&quot; 
 
This is a system that was originally developed by BigBear, so full...") 26 replies

[Price bouncing off of sma](/thread/228922-price-bouncing-off-of-sma "What is the logic behind a price bouncing off an SMA? 
 
For example if a price bounces of a 35 day sma, i should short it if bounces of...") 2 replies

[Developing a correlated bouncing system](/thread/158016-developing-a-correlated-bouncing-system "The above indicator is a simple ma indicator with the weekly ma set to 40. 
 
I like most of my bouncing signals to be in the direction of...") 9 replies

[bouncing candle indicator](/thread/105826-bouncing-candle-indicator "I once had an indicator that would  send  off an alert whenever a candle touched back on its  moving average.  Lost it somehow, but I do...") 0 replies

[Price bouncing off support or resistance,your thoughts](/thread/30984-price-bouncing-off-support-or-resistanceyour-thoughts "I would like to start a discussuion about price movement at support/resistance, Fib and pivot levels.  
  
Time and again I see the price...") 11 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/157406-fx30m-bouncing-system/reply#reply)
  * Subscribe
  * [72](javascript:void\(0\);)

Attachments: FX_30M Bouncing System

Tags: FX_30M Bouncing System

#  [](/thread/157406-fx30m-bouncing-system)FX_30M Bouncing System 

  * 

  * [#141](/thread/post/2605100#post2605100 "Post Permalink")

  * Mar 16, 2009 11:15am  Mar 16, 2009 11:15am 

  * [ Dan Johnston](dan*johnston)

  * | Joined May 2008  | Status: Trader | [354 Posts](/search?do=process&provider=Member&searchuser=69420)

Hi Siobi.   
  
Great work on the ea, but if you can make it enter earlier according to the slope direction line, or maybe a cross thereof like below.  
  
Could have closed this last trade manually for more, but had ea entered earlier in the obvious uptrend, we would have gotten the 20 easily.  
  
Still not bad though, as this acct. is now 14 and 0!!! 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: v104fxdd3 15a09.gif
Size: 42 KB](/attachment/image/219013/thumbnail?d=1365565128)](/attachment/image/219013?d=1237169608)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#142](/thread/post/2605112#post2605112 "Post Permalink")

  * Mar 16, 2009 11:22am  Mar 16, 2009 11:22am 

  * [ Dan Johnston](dan*johnston)

  * | Joined May 2008  | Status: Trader | [354 Posts](/search?do=process&provider=Member&searchuser=69420)

Sorry posted the 15m chart above.   
  
30m is below:  
(Same holds true as above for this timeframe also.) 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: v104fxdd3 15b09.gif
Size: 42 KB](/attachment/image/219014/thumbnail?d=1365565128)](/attachment/image/219014?d=1237170145)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#143](/thread/post/2606014#post2606014 "Post Permalink")

  * Mar 16, 2009 9:56pm  Mar 16, 2009 9:56pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar95566_5.gif) stifland](stifland)

  * | Joined Mar 2009  | Status: Trader | [304 Posts](/search?do=process&provider=Member&searchuser=95566)

so I'm not real sure which chart took which trades, but i ended up down 57 pips. If I had quit after 20 or stayed on 30m, daily goal would have been met.  
  
Dan, If on the 15, I assume it takes different entries than the 30m? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#144](/thread/post/2606172#post2606172 "Post Permalink")

  * Edited 11:15pm  Mar 16, 2009 11:03pm | Edited 11:15pm 

  * [ qz10cq](qz10cq)

  * | Joined Dec 2006  | Status: Trader | [303 Posts](/search?do=process&provider=Member&searchuser=29720)

> [Quoting qz10cq](/thread/post/2600448#post2600448 "View Quoted Post")
> 
> Disliked
> 
> Siobi, have your ea on fxdd attached to all pairs under a 10 spread. Have won several and lost a few, eur/usd has been quiet lately. My goal is to eliminate the pairs that lose twice and see what I have left in a week or so. Will keep the thread informed.
> 
> Ignored

Well I made overall 230 pips last week with 3 losses (r8), have eliminated those pairs that loss and over night I'm +270. Will keep the thread informed. 

Attached Image

![](/attachment/image/219227?d=1237212909)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#145](/thread/post/2606226#post2606226 "Post Permalink")

  * Edited 11:20pm  Mar 16, 2009 11:19pm | Edited 11:20pm 

  * [ nickmead](nickmead)

  * | Commercial User  | Joined Feb 2008 | [66 Posts](/search?do=process&provider=Member&searchuser=61524)

Wow. great work. aRe you trading 24 hours or just the Asian session. May I ask which pairs you are down to. If I want to let it run longer I assume I have to change close hour also. For example   
Hour Start 0  
Hour End 23  
Close Hour 24  
  
is that right  
  
thx for your help  
  
Nick 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#146](/thread/post/2606392#post2606392 "Post Permalink")

  * Edited 12:28am  Mar 17, 2009 12:13am | Edited 12:28am 

  * [ Dan Johnston](dan*johnston)

  * | Joined May 2008  | Status: Trader | [354 Posts](/search?do=process&provider=Member&searchuser=69420)

We'll have to wait for Siobi to make an appearance and try to answer any questions more definitively.   
  
While we do that, let's keep up the testing - forward, back, side to side, and all around.   
  
...Shake this thing up and make sure we know what we have before going live.  
  
Happy pipping everyone!  
  
15 and 0 on this acct.: ( running both r7 and more recently r8 added - r7; 1.0 lots, r8; 0.5 lots)  
  
Hopefully they will not interfere with one another's entries etc., as I'd obviously like to keep this kind of preformance going! 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: v104fxdd3 1609.gif
Size: 45 KB](/attachment/image/219265/thumbnail?d=1365565188)](/attachment/image/219265?d=1237217049)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#147](/thread/post/2606427#post2606427 "Post Permalink")

  * Mar 17, 2009 12:29am  Mar 17, 2009 12:29am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83889_5.gif) siobi](siobi)

  * | Joined Oct 2008  | Status: Trader | [717 Posts](/search?do=process&provider=Member&searchuser=83889)

hi all,the 2 signals generated is causing me losing 50 pip each because I'm running 50pip as my SL...I'm now adding a new indicator to filter off the bad trade, but need some time for testing... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#148](/thread/post/2606449#post2606449 "Post Permalink")

  * Mar 17, 2009 12:40am  Mar 17, 2009 12:40am 

  * [ Dan Johnston](dan*johnston)

  * | Joined May 2008  | Status: Trader | [354 Posts](/search?do=process&provider=Member&searchuser=69420)

> [Quoting siobi](/thread/post/2606427#post2606427 "View Quoted Post")
> 
> Disliked
> 
> hi all,the 2 signals generated is causing me losing 50 pip each because I'm running 50pip as my SL...I'm now adding a new indicator to filter off the bad trade, but need some time for testing...
> 
> Ignored

Thanks Siobi.  
  
It seems fxdd and r7/r8 make a good combination so far, as I don't believe that we have experienced over 50 pip dd on fxdd to date, ...somehow.  
  
IBFX is less successful, even though the priceaction on a chart looks similar.   
...Interesting, and maybe someone who knows more about how tick data - or whatever - comes through to the ea may elaborate further on the performance discrepancies between the two brokers. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#149](/thread/post/2606458#post2606458 "Post Permalink")

  * Mar 17, 2009 12:42am  Mar 17, 2009 12:42am 

  * [ paradoxical](paradoxical)

  * | Joined Nov 2007  | Status: Trader | [1,186 Posts](/search?do=process&provider=Member&searchuser=54706)

Neither EA working on my IBFX demo account. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#150](/thread/post/2606514#post2606514 "Post Permalink")

  * Edited 4:26am  Mar 17, 2009 12:58am | Edited 4:26am 

  * [ Dan Johnston](dan*johnston)

  * | Joined May 2008  | Status: Trader | [354 Posts](/search?do=process&provider=Member&searchuser=69420)

> [Quoting nickmead](/thread/post/2606226#post2606226 "View Quoted Post")
> 
> Disliked
> 
> Wow. great work. aRe you trading 24 hours or just the Asian session. May I ask which pairs you are down to. If I want to let it run longer I assume I have to change close hour also. For example   
>  Hour Start 0  
>  Hour End 23  
>  Close Hour 24  
>    
>  is that right  
>    
>  thx for your help  
>    
>  Nick
> 
> Ignored

Paradoxical, I would do a fresh reinstall of the ea and or entire mt4 platform, and also download fxdd demo and compare the two apples to apples. Unfortunately all my accounts are too erratic and do not want to screw up a good thing with the one fxdd acct. that is doing amazingly well, otherwise I would do what I suggested myself with another fxdd and ibfx instance.   
  
Nickmead, additionally to your questions I would like to know what stoploss, trailing stop etc. gz10cq is using?  
It does seem he is having early success with the following further pairs:  
gbpusd  
audusd   
eruchf  
eurcad  
usdchf  
gbpjpy  
  
Would be simply wonderful if it kept up!!!![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)  
  
**PS: I also noticed that the ea itself has been downloaded more times than the template and indicators. I don't know if there are different versions of the slope dir. line and stoch rsi out there that may be causing a conflict with those accounts that are not taking trades.**  
**As a further assurance that we are all on the same page and have the ea take trades, I would download the _indicators_ from _page 1_ along with the ea.**

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#151](/thread/post/2606518#post2606518 "Post Permalink")

  * Edited 1:02am  Mar 17, 2009 12:59am | Edited 1:02am 

  * [ Wizhoo](wizhoo)

  * | Joined Sep 2008  | Status: Trader | [33 Posts](/search?do=process&provider=Member&searchuser=79692)

I ran across this thread last night and have been back testing with good results. Today I started forward test and got a winning trade with Eur/Usd in a 1M TF. I used 1M to see if the system was making auto trades. My system is setup and charts are set at 30M now. This system look very promising. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#152](/thread/post/2606688#post2606688 "Post Permalink")

  * Mar 17, 2009 1:51am  Mar 17, 2009 1:51am 

  * [ Snowdogg](snowdogg)

  * | Joined Mar 2005  | Status: Trader | [38 Posts](/search?do=process&provider=Member&searchuser=1871)

I am sure I have all the indicators downloaded and installed correctly. I am on EUR/USD and GBP/USD with ITFX broker. I started it yesterday when the markets opened and let it run to now so that is approx. 20 hours. I am in CST so it ran through all sessions. Just testing on Demo. No trades fired yet. Should I have had some, or could there be a problem? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#153](/thread/post/2606719#post2606719 "Post Permalink")

  * Mar 17, 2009 2:06am  Mar 17, 2009 2:06am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar43332_2.gif) willmalou](willmalou)

  * | Joined Jul 2007  | Status: Think before you act!!! | [113 Posts](/search?do=process&provider=Member&searchuser=43332)

> [Quoting Snowdogg](/thread/post/2606688#post2606688 "View Quoted Post")
> 
> Disliked
> 
> I am sure I have all the indicators downloaded and installed correctly. I am on EUR/USD and GBP/USD with ITFX broker. I started it yesterday when the markets opened and let it run to now so that is approx. 20 hours. I am in CST so it ran through all sessions. Just testing on Demo. No trades fired yet. Should I have had some, or could there be a problem?
> 
> Ignored

  
If you are using defaults, it is only going to trade during the Asian session. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#154](/thread/post/2606757#post2606757 "Post Permalink")

  * Mar 17, 2009 2:25am  Mar 17, 2009 2:25am 

  * [ fxea](fxea)

  * | Joined Nov 2008  | Status: Trader | [1 Post](/search?do=process&provider=Member&searchuser=85510)

Hello  
can anyone help on this?  
what is the Japan hour setting on FXDD?   
HourStart = 2  
HourEnd = 12  
closeHour = 13 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#155](/thread/post/2606760#post2606760 "Post Permalink")

  * Mar 17, 2009 2:28am  Mar 17, 2009 2:28am 

  * [ Snowdogg](snowdogg)

  * | Joined Mar 2005  | Status: Trader | [38 Posts](/search?do=process&provider=Member&searchuser=1871)

No, I should have stated earlier (sorry), I am not using defaults. I changed the times to 0, 24, and 30 , like I read in one of the posts. Should I be changing something else? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#156](/thread/post/2606766#post2606766 "Post Permalink")

  * Mar 17, 2009 2:30am  Mar 17, 2009 2:30am 

  * [ paradoxical](paradoxical)

  * | Joined Nov 2007  | Status: Trader | [1,186 Posts](/search?do=process&provider=Member&searchuser=54706)

Dan, Thanks. I'll do that. I've had the demo account crash twice, so there's a problem somewhere. I also do have a FXDD demo account that I haven't used & I'll try the EAs on that.

> [Quoting Dan Johnston](/thread/post/2606514#post2606514 "View Quoted Post")
> 
> Disliked
> 
> Paradoxical, I would do a fresh reinstall of the ea and or entire mt4 platform, and also download fxdd demo and compare the two apples to apples. Unfortunately all my accounts are too erratic and do not want to screw up a good thing with the one fxdd acct. that is doing amazingly well, otherwise I would do what I suggested myself with another fxdd and ibfx instance.   
>    
>  Nickmead, additionally to your questions I would like to know what stoploss, trailing stop etc. gz10cq is using?  
>  It does seem he is having early success with the following further...
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#157](/thread/post/2606790#post2606790 "Post Permalink")

  * Mar 17, 2009 2:45am  Mar 17, 2009 2:45am 

  * [ michaelhryu](michaelhryu)

  * | Joined Oct 2008  | Status: Trader | [142 Posts](/search?do=process&provider=Member&searchuser=81864)

> [Quoting Dan Johnston](/thread/post/2606392#post2606392 "View Quoted Post")
> 
> Disliked
> 
> 15 and 0 on this acct.: ( running both r7 and more recently r8 added - r7; 1.0 lots, r8; 0.5 lots)
> 
> Ignored

Where can I find the version r7, please? I couldn't find it anywhere though I keep hearing about it. Is r7 for 1M TF, 15M TF, or 30M TF? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#158](/thread/post/2606795#post2606795 "Post Permalink")

  * Mar 17, 2009 2:50am  Mar 17, 2009 2:50am 

  * [ nickmead](nickmead)

  * | Commercial User  | Joined Feb 2008 | [66 Posts](/search?do=process&provider=Member&searchuser=61524)

I have E/U G/U U/CHF A/U and U/CAD set up for the asian open. I will post results  
  
all the best   
  
Nick 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#159](/thread/post/2606808#post2606808 "Post Permalink")

  * Mar 17, 2009 2:58am  Mar 17, 2009 2:58am 

  * [ nickmead](nickmead)

  * | Commercial User  | Joined Feb 2008 | [66 Posts](/search?do=process&provider=Member&searchuser=61524)

> [Quoting michaelhryu](/thread/post/2606790#post2606790 "View Quoted Post")
> 
> Disliked
> 
> Where can I find the version r7, please? I couldn't find it anywhere though I keep hearing about it. Is r7 for 1M TF, 15M TF, or 30M TF?
> 
> Ignored

regards  
Nick 

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [FX_30M_Bouncing_V104.ex4](/attachment/file/219329?d=1237226249) 16 KB | 256 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#160](/thread/post/2606816#post2606816 "Post Permalink")

  * Mar 17, 2009 3:00am  Mar 17, 2009 3:00am 

  * [ nickmead](nickmead)

  * | Commercial User  | Joined Feb 2008 | [66 Posts](/search?do=process&provider=Member&searchuser=61524)

I think r7 is on the old 1m thread   
  
<http://www.forexfactory.com/showthread.php?t=139685>

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * FX_30M Bouncing System
  *   * [ **Reply to Thread** ](/thread/157406-fx30m-bouncing-system/reply#reply)

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

[The Bouncing Pip](/thread/88277-the-bouncing-pip "Hi everyone. 
 
I present to you a system called &quot;The Bouncing Pip&quot; 
 
This is a system that was originally developed by BigBear, so full...") 26 replies

[Price bouncing off of sma](/thread/228922-price-bouncing-off-of-sma "What is the logic behind a price bouncing off an SMA? 
 
For example if a price bounces of a 35 day sma, i should short it if bounces of...") 2 replies

[Developing a correlated bouncing system](/thread/158016-developing-a-correlated-bouncing-system "The above indicator is a simple ma indicator with the weekly ma set to 40. 
 
I like most of my bouncing signals to be in the direction of...") 9 replies

[bouncing candle indicator](/thread/105826-bouncing-candle-indicator "I once had an indicator that would  send  off an alert whenever a candle touched back on its  moving average.  Lost it somehow, but I do...") 0 replies

[Price bouncing off support or resistance,your thoughts](/thread/30984-price-bouncing-off-support-or-resistanceyour-thoughts "I would like to start a discussuion about price movement at support/resistance, Fib and pivot levels.  
  
Time and again I see the price...") 11 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/157406-fx30m-bouncing-system/reply#reply)
  * Subscribe
  * [72](javascript:void\(0\);)

Attachments: FX_30M Bouncing System

Tags: FX_30M Bouncing System

#  [](/thread/157406-fx30m-bouncing-system)FX_30M Bouncing System 

  * 

  * [#161](/thread/post/2606910#post2606910 "Post Permalink")

  * Mar 17, 2009 3:51am  Mar 17, 2009 3:51am 

  * [ paradoxical](paradoxical)

  * | Joined Nov 2007  | Status: Trader | [1,186 Posts](/search?do=process&provider=Member&searchuser=54706)

IBFX has taken no trades & I re-downloaded the platform and EAS. Still nothing. I loaded the EAs onto a FXDD demo account, and within a few minutes, the v106 EA made a trade. I immediately checked IBFX to see if it also made a trade, and it didn't. Same settings, same everything.  
Is there anything that needs to be changed on these EAs to make them work with IBFX? I thought maybe change the number of digits to "true", but I don't believe IBFX is a 5 digit broker; whereas I think FXDD IS, and I made no changes there. Confusede why it works on one broker, and not the other. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#162](/thread/post/2606929#post2606929 "Post Permalink")

  * Edited 4:16am  Mar 17, 2009 4:00am | Edited 4:16am 

  * [ Dan Johnston](dan*johnston)

  * | Joined May 2008  | Status: Trader | [354 Posts](/search?do=process&provider=Member&searchuser=69420)

I believe that the 21kb file is r7 and the 16kb file is r8.  
  
Please verify by looking at version and date in it's properties box and then on the upper left once dropped onto the **30m** chart.  
  
I have had ibfx trades, but not as successful. You may want to open an fxdd acct. if we find that it doesn't work that well with ibfx - _for whatever crazy reason_. (should be same settings as they are both 4 digits)  
I have read somewhere that filtered and non-filtered tick data from certain brokers work differently with certain ea's. I could be way off base though. Just don't know, and am also confused.  
  
Oh, and disregard that r7 says "1m". Use both on 30m.   
Siobi is working on new versions as we post, so this may soon be moot. 

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [FX_1M_Bouncing_V104R7.ex4](/attachment/file/219351?d=1237229959) 21 KB | 355 downloads 

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [FX_30M_Bouncing_V104.ex4](/attachment/file/219352?d=1237230008) 16 KB | 301 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#163](/thread/post/2606972#post2606972 "Post Permalink")

  * Mar 17, 2009 4:26am  Mar 17, 2009 4:26am 

  * [ paradoxical](paradoxical)

  * | Joined Nov 2007  | Status: Trader | [1,186 Posts](/search?do=process&provider=Member&searchuser=54706)

The FXDD short trade on the EUR/USD is up 14 PIPS as I write. Would consider putting some money in a live account if it kept up. It was down about 17 PIPS at one point. Don't like a 100 pip stop with a 20 PIP take profit, but I know these TP and SL can and have been changed. Still would like the same results with IBFX & will await Siobi's modification and maybe the new EA will work with IBFX.  
OOPS...spoke too soon. The short trade just closed out at 20 PIPS profit! Dan, let's make some plans for a few beers in Cancun, or maybe three, or twelve. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#164](/thread/post/2606995#post2606995 "Post Permalink")

  * Mar 17, 2009 4:34am  Mar 17, 2009 4:34am 

  * [ Dan Johnston](dan*johnston)

  * | Joined May 2008  | Status: Trader | [354 Posts](/search?do=process&provider=Member&searchuser=69420)

> [Quoting paradoxical](/thread/post/2606972#post2606972 "View Quoted Post")
> 
> Disliked
> 
> The FXDD short trade on the EUR/USD is up 14 PIPS as I write. Would consider putting some money in a live account if it kept up. It was down about 17 PIPS at one point. Don't like a 100 pip stop with a 20 PIP take profit, but I know these TP and SL can and have been changed. Still would like the same results with IBFX & will await Siobi's modification and maybe the new EA will work with IBFX.  
>  OOPS...spoke too soon. The short trade just closed out at 20 PIPS profit! Dan, let's make some plans for a few beers in Cancun, or maybe three, or twelve.
> 
> Ignored

Sounds good!!![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)  
(A quick plane ride from FL.) 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#165](/thread/post/2607366#post2607366 "Post Permalink")

  * Mar 17, 2009 7:36am  Mar 17, 2009 7:36am 

  * [ Dan Johnston](dan*johnston)

  * | Joined May 2008  | Status: Trader | [354 Posts](/search?do=process&provider=Member&searchuser=69420)

For the purpose of providing any insights that I can, the following are some facts about the 15 winning trades taken on the fxdd account posted earlier by me (worst trade by far is the one highlighted and shown on the chart below - 67 pip drawdown):  
  
The rest of the trades have the following drawdowns;  
-8,-8,-21,-11,-13,-16,-18,-10,-3,*-**67** *,-3,-30,-1,-6,-12  
  
Not too damn bad thus far!!! 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: v104fxdd3 16b09.gif
Size: 43 KB](/attachment/image/219435/thumbnail?d=1365565216)](/attachment/image/219435?d=1237242983)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#166](/thread/post/2607389#post2607389 "Post Permalink")

  * Mar 17, 2009 8:00am  Mar 17, 2009 8:00am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83889_5.gif) siobi](siobi)

  * | Joined Oct 2008  | Status: Trader | [717 Posts](/search?do=process&provider=Member&searchuser=83889)

hi dan and others,  
  
I plan to put in 2 additional filter which act as buy or sell trend usage so the EA will not take the trade during the bouncing/retracement...  
  
regarding to take the trade earlier, I'm still lokking into it...  
  
regards,  
siobi (with both sleepy eyes...![](https://resources.faireconomy.media/images/emojis/64/1f61c.png?v=15.1)) 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#167](/thread/post/2607498#post2607498 "Post Permalink")

  * Edited 10:23am  Mar 17, 2009 9:23am | Edited 10:23am 

  * [ Dan Johnston](dan*johnston)

  * | Joined May 2008  | Status: Trader | [354 Posts](/search?do=process&provider=Member&searchuser=69420)

> [Quoting siobi](/thread/post/2607389#post2607389 "View Quoted Post")
> 
> Disliked
> 
> hi dan and others,  
>    
>  I plan to put in 2 additional filter which act as buy or sell trend usage so the EA will not take the trade during the bouncing/retracement...  
>    
>  regarding to take the trade earlier, I'm still lokking into it...  
>    
>  regards,  
>  siobi (with both sleepy eyes...![](https://resources.faireconomy.media/images/emojis/64/1f61c.png?v=15.1))
> 
> Ignored

Your efforts are greatly appreciated by us all Siobi.  
  
By the way, I'm using 2 same timeframe - with different settings - slope direction lines on the previous charts + one for the next higher timeframe on the same chart. I think maybe when both the 10,2,0,0 and the 12,3,0,0 slope dir. lines agree in color is maybe good time to look to other indicators to take trade. Maybe even also look at the next higher timeframe slope dir. line also for further confirmation that 20 pips is safe to target for. If all 2 or 3 are same color then enter based on your other indicators? ...Just some ideas.   
  
Get some sleep my friend! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#168](/thread/post/2607891#post2607891 "Post Permalink")

  * Mar 17, 2009 1:09pm  Mar 17, 2009 1:09pm 

  * [ stinger007](stinger007)

  * | Joined Sep 2008  | Status: Trader | [94 Posts](/search?do=process&provider=Member&searchuser=80985)

hay all, Just wondering if anyone has this working on alpari 5 digit account. Setup seems fine and i've had it working on 2 other demo accounts...but unable to get working on live alpari account... Cheers 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#169](/thread/post/2608021#post2608021 "Post Permalink")

  * Mar 17, 2009 2:45pm  Mar 17, 2009 2:45pm 

  * [ qz10cq](qz10cq)

  * | Joined Dec 2006  | Status: Trader | [303 Posts](/search?do=process&provider=Member&searchuser=29720)

> [Quoting qz10cq](/thread/post/2606172#post2606172 "View Quoted Post")
> 
> Disliked
> 
> Well I made overall 230 pips last week with 3 losses (r8), have eliminated those pairs that loss and over night I'm +270. Will keep the thread informed.
> 
> Ignored

Up another 85 pips today with a total dd now of 110. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: 1.gif
Size: 44 KB](/attachment/image/219570/thumbnail?d=1365565247)](/attachment/image/219570?d=1237268713)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#170](/thread/post/2608093#post2608093 "Post Permalink")

  * Mar 17, 2009 3:50pm  Mar 17, 2009 3:50pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83889_5.gif) siobi](siobi)

  * | Joined Oct 2008  | Status: Trader | [717 Posts](/search?do=process&provider=Member&searchuser=83889)

hahahahah today a clear win 20 pip for V104 R9 in live IBFX!!!  
  
yes... is R9.....  
  
hm.. I think this EA is good enough for an entry and tp of 20 pips per day per pair.  
  
dan in reading,  
yeah, comparing to hieher timeframe might be a good filter as well.  
  
so, R9 will b having  
1) 200 SMA filtering (if BUY signal generated, then price Must be above 200SMA)  
2) prev day pivot(new indicator,if BUY signal generated, then price Must be above this indicator)  
3) cross check slope direction for higher timeframe.  
  
hm.. I need another week for this testing in my LIVE acct before release to public...  
  
as agreed, this EA is going to be configured monthly basis and R9 will be only release during the end of March'09.  
  
I'll email to dan for in house testing once completed.  
  
PS: I'm still running at 50 pip stop loss strategy.... ![](https://resources.faireconomy.media/images/emojis/64/1f61c.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#171](/thread/post/2608276#post2608276 "Post Permalink")

  * Mar 17, 2009 6:17pm  Mar 17, 2009 6:17pm 

  * [ Dan Johnston](dan*johnston)

  * | Joined May 2008  | Status: Trader | [354 Posts](/search?do=process&provider=Member&searchuser=69420)

Excellent work Siobi!!!  
  
....And everyone else here!!!  
  
![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#172](/thread/post/2608432#post2608432 "Post Permalink")

  * Mar 17, 2009 7:52pm  Mar 17, 2009 7:52pm 

  * [ Dan Johnston](dan*johnston)

  * | Joined May 2008  | Status: Trader | [354 Posts](/search?do=process&provider=Member&searchuser=69420)

This last trade managed to squeak by and get it's 20 with approx. -18 pip drawdown.  
  
Now 16 and 0 for this account! 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: v104fxdd3 1709.gif
Size: 46 KB](/attachment/image/219653/thumbnail?d=1365565272)](/attachment/image/219653?d=1237287102)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#173](/thread/post/2608448#post2608448 "Post Permalink")

  * Mar 17, 2009 8:04pm  Mar 17, 2009 8:04pm 

  * [ Dan Johnston](dan*johnston)

  * | Joined May 2008  | Status: Trader | [354 Posts](/search?do=process&provider=Member&searchuser=69420)

> [Quoting qz10cq](/thread/post/2608021#post2608021 "View Quoted Post")
> 
> Disliked
> 
> Up another 85 pips today with a total dd now of 110.
> 
> Ignored

Thanks for keeping us in the loop!!!  
  
Are you using default settings?  
  
Excellent performance thus far!!!![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#174](/thread/post/2608584#post2608584 "Post Permalink")

  * Mar 17, 2009 9:16pm  Mar 17, 2009 9:16pm 

  * [ qz10cq](qz10cq)

  * | Joined Dec 2006  | Status: Trader | [303 Posts](/search?do=process&provider=Member&searchuser=29720)

> [Quoting Dan Johnston](/thread/post/2608448#post2608448 "View Quoted Post")
> 
> Disliked
> 
> Thanks for keeping us in the loop!!!  
>    
>  Are you using default settings?  
>    
>  Excellent performance thus far!!!![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)
> 
> Ignored

Dan I thought I was running defaults but I had a template of r7, so when I put the template on r8 if gave me the 100sl and 150 tp. Will correct that now, lost gbp/usd last night (-100) so I removed it from the test. Dan you stepped up to 1.0 lots. Is anyone still testing V106?  
  
Siobi, this is one of the best EA's, I hope you don't filter this EA into a loser but I guess this is why we are testing......Dan 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#175](/thread/post/2608599#post2608599 "Post Permalink")

  * Mar 17, 2009 9:22pm  Mar 17, 2009 9:22pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar95566_5.gif) stifland](stifland)

  * | Joined Mar 2009  | Status: Trader | [304 Posts](/search?do=process&provider=Member&searchuser=95566)

just 1 trade for me in a 15m timeframe. Asian session only. +20!  
Off to work.... 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: lastnight.gif
Size: 27 KB](/attachment/image/219682/thumbnail?d=1365565272)](/attachment/image/219682?d=1237292560)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#176](/thread/post/2608626#post2608626 "Post Permalink")

  * Mar 17, 2009 9:32pm  Mar 17, 2009 9:32pm 

  * [ qz10cq](qz10cq)

  * | Joined Dec 2006  | Status: Trader | [303 Posts](/search?do=process&provider=Member&searchuser=29720)

> [Quoting qz10cq](/thread/post/2608584#post2608584 "View Quoted Post")
> 
> Disliked
> 
> Dan I thought I was running defaults but I had a template of r7, so when I put the template on r8 if gave me the 100sl and 150 tp. Will correct that now, lost gbp/usd last night (-100) so I removed it from the test. Dan you stepped up to 1.0 lots. Is anyone still testing V106?  
>    
>  Siobi, this is one of the best EA's, I hope you don't filter this EA into a loser but I guess this is why we are testing......Dan
> 
> Ignored

Now set up for 30m chart, 20tp and 50sl on 13 pairs running r8 with .1 lots. Will keep thread informed...Dan 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#177](/thread/post/2608908#post2608908 "Post Permalink")

  * Mar 17, 2009 11:16pm  Mar 17, 2009 11:16pm 

  * [ Dan Johnston](dan*johnston)

  * | Joined May 2008  | Status: Trader | [354 Posts](/search?do=process&provider=Member&searchuser=69420)

> [Quoting qz10cq](/thread/post/2608626#post2608626 "View Quoted Post")
> 
> Disliked
> 
> Now set up for 30m chart, 20tp and 50sl on 13 pairs running r8 with .1 lots. Will keep thread informed...Dan
> 
> Ignored

We'll all get there!!!![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)  
  
Below, "no harm no foul":  
0 pips with -22 drawdown, but no **_loss_**. Still looking mighty fine!!!  
  
17 and 0!!! 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: v104fxdd3 17a09.gif
Size: 43 KB](/attachment/image/219748/thumbnail?d=1365565272)](/attachment/image/219748?d=1237299373)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#178](/thread/post/2608934#post2608934 "Post Permalink")

  * Edited 11:44pm  Mar 17, 2009 11:32pm | Edited 11:44pm 

  * [ Dan Johnston](dan*johnston)

  * | Joined May 2008  | Status: Trader | [354 Posts](/search?do=process&provider=Member&searchuser=69420)

Just something I noticed, is that if we could just shift everything over to the left by one bar or so, we would have better entries. Just a small **tweak** to enter **slightly** earlier, as can be seen by the red vertical lines I put on the chart. When I have time I will go back and test this hypothesis on all the trades this account has taken.   
It also seems that the stochastic rsi at bottom also bears this out as it is already nearly in oversold/overbought territory when trades are triggered.   
  
...Just a **__tiny little__** correction to the left of the chart should do it to make this as perfect - so far - as any man made fx machine can be! (Siobi, I know you are looking into this already, and for fxdd, that is all this might need. As for ibfx, the project you're working on sounds amazing, as I - and many others, you included - also have an account with them.)  
  
....Or I may just need more sleep....![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)  
  
(Look at me complaining about this kind of performance. Man what a unrealistic ungreatful perfectionist I am!!!![](https://resources.faireconomy.media/images/emojis/64/1f61e.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1))  
  
It may very well be that with time this very version will prove to be the best with fxdd, but one can never rest on "_near_ " perfection can one?![](https://resources.faireconomy.media/images/emojis/64/1f61c.png?v=15.1)

Attached Image (click to enlarge)

[![Click to Enlarge

Name: v104fxdd3 17a109.gif
Size: 49 KB](/attachment/image/219754/thumbnail?d=1365565299)](/attachment/image/219754?d=1237300387)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#179](/thread/post/2608953#post2608953 "Post Permalink")

  * Mar 17, 2009 11:41pm  Mar 17, 2009 11:41pm 

  * [ paradoxical](paradoxical)

  * | Joined Nov 2007  | Status: Trader | [1,186 Posts](/search?do=process&provider=Member&searchuser=54706)

One 20 PIP win last night on a buy at 1.3008 which just barely squeaked out the win. Another breakeven on a sell at 1.2955. This is on the v104V8 on a 30 minute chart.  
The v106 on the 15 minute chart had 2 very small losers.  
VERY impressed so far, Siobi & also thanks to Dan for his informative posts. The possibility of this EA working on other pairs is a very nice thought also. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#180](/thread/post/2608974#post2608974 "Post Permalink")

  * Mar 17, 2009 11:51pm  Mar 17, 2009 11:51pm 

  * [ Dan Johnston](dan*johnston)

  * | Joined May 2008  | Status: Trader | [354 Posts](/search?do=process&provider=Member&searchuser=69420)

> [Quoting paradoxical](/thread/post/2608953#post2608953 "View Quoted Post")
> 
> Disliked
> 
> One 20 PIP win last night on a buy at 1.3008 which just barely squeaked out the win. Another breakeven on a sell at 1.2955. This is on the v104V8 on a 30 minute chart.  
>  The v106 on the 15 minute chart had 2 very small losers.  
>  VERY impressed so far, Siobi & also thanks to Dan for his informative posts. The possibility of this EA working on other pairs is a very nice thought also.
> 
> Ignored

I'm glad to see yours synched up finally. Consistent performance may just be around the corner for everyone here.   
  
And yes, if indeed it can work with other pairs, ....**WOW**!  
  
But for now I'm still wowed by the performance, and waiting for that inevitable "**L** " word, ....that will most likely come the minute I go live!!!!![](https://resources.faireconomy.media/images/emojis/64/1f923.png?v=15.1)  
  
(I better laugh it up now while I'm in the mood.![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)) 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * FX_30M Bouncing System
  *   * [ **Reply to Thread** ](/thread/157406-fx30m-bouncing-system/reply#reply)

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

[The Bouncing Pip](/thread/88277-the-bouncing-pip "Hi everyone. 
 
I present to you a system called &quot;The Bouncing Pip&quot; 
 
This is a system that was originally developed by BigBear, so full...") 26 replies

[Price bouncing off of sma](/thread/228922-price-bouncing-off-of-sma "What is the logic behind a price bouncing off an SMA? 
 
For example if a price bounces of a 35 day sma, i should short it if bounces of...") 2 replies

[Developing a correlated bouncing system](/thread/158016-developing-a-correlated-bouncing-system "The above indicator is a simple ma indicator with the weekly ma set to 40. 
 
I like most of my bouncing signals to be in the direction of...") 9 replies

[bouncing candle indicator](/thread/105826-bouncing-candle-indicator "I once had an indicator that would  send  off an alert whenever a candle touched back on its  moving average.  Lost it somehow, but I do...") 0 replies

[Price bouncing off support or resistance,your thoughts](/thread/30984-price-bouncing-off-support-or-resistanceyour-thoughts "I would like to start a discussuion about price movement at support/resistance, Fib and pivot levels.  
  
Time and again I see the price...") 11 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/157406-fx30m-bouncing-system/reply#reply)
  * Subscribe
  * [72](javascript:void\(0\);)

Attachments: FX_30M Bouncing System

Tags: FX_30M Bouncing System

#  [](/thread/157406-fx30m-bouncing-system)FX_30M Bouncing System 

  * 

  * [#181](/thread/post/2609016#post2609016 "Post Permalink")

  * Mar 18, 2009 12:14am  Mar 18, 2009 12:14am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar94654_2.gif) walrus_78](walrus_78)

  * | Joined Feb 2009  | Status: Trader | [19 Posts](/search?do=process&provider=Member&searchuser=94654)

Hello, I'm new in this forum but i find this EA very promising,   
  
I have some questions, which inputs do you use for the EA and also for the Indicators?, can it be used in several pairs at the same time in the same account?  
  
thank you 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#182](/thread/post/2609052#post2609052 "Post Permalink")

  * Mar 18, 2009 12:35am  Mar 18, 2009 12:35am 

  * [ stinger007](stinger007)

  * | Joined Sep 2008  | Status: Trader | [94 Posts](/search?do=process&provider=Member&searchuser=80985)

> [Quoting stinger007](/thread/post/2607891#post2607891 "View Quoted Post")
> 
> Disliked
> 
> hay all, Just wondering if anyone has this working on alpari 5 digit account. Setup seems fine and i've had it working on 2 other demo accounts...but unable to get working on live alpari account... Cheers
> 
> Ignored

nearly 24 hours and no trades on live, working fine on my demo account ARRRGGGG  
  
Anyone help??  
  
many thanks 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#183](/thread/post/2609080#post2609080 "Post Permalink")

  * Mar 18, 2009 12:47am  Mar 18, 2009 12:47am 

  * [ nickmead](nickmead)

  * | Commercial User  | Joined Feb 2008 | [66 Posts](/search?do=process&provider=Member&searchuser=61524)

> [Quoting qz10cq](/thread/post/2608626#post2608626 "View Quoted Post")
> 
> Disliked
> 
> Now set up for 30m chart, 20tp and 50sl on 13 pairs running r8 with .1 lots. Will keep thread informed...Dan
> 
> Ignored

what are your time settings  
  
thx  
Nick  
  
great work by the way....some serious pippige there ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#184](/thread/post/2609083#post2609083 "Post Permalink")

  * Mar 18, 2009 12:48am  Mar 18, 2009 12:48am 

  * [ nickmead](nickmead)

  * | Commercial User  | Joined Feb 2008 | [66 Posts](/search?do=process&provider=Member&searchuser=61524)

20 pips on GU, 1 pip on EU  
  
![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#185](/thread/post/2609099#post2609099 "Post Permalink")

  * Mar 18, 2009 12:57am  Mar 18, 2009 12:57am 

  * [ Wizhoo](wizhoo)

  * | Joined Sep 2008  | Status: Trader | [33 Posts](/search?do=process&provider=Member&searchuser=79692)

> [Quoting nickmead](/thread/post/2609083#post2609083 "View Quoted Post")
> 
> Disliked
> 
> 20 pips on GU, 1 pip on EU  
>    
>  ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)
> 
> Ignored

Yeah, I got the 1 pip on EU but nada for GU. ![](https://resources.faireconomy.media/images/emojis/64/1f641.png?v=15.1)  
  
Did you do anything different for the GU chart? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#186](/thread/post/2609204#post2609204 "Post Permalink")

  * Mar 18, 2009 1:42am  Mar 18, 2009 1:42am 

  * [ nickmead](nickmead)

  * | Commercial User  | Joined Feb 2008 | [66 Posts](/search?do=process&provider=Member&searchuser=61524)

> [Quoting Wizhoo](/thread/post/2609099#post2609099 "View Quoted Post")
> 
> Disliked
> 
> Yeah, I got the 1 pip on EU but nada for GU. ![](https://resources.faireconomy.media/images/emojis/64/1f641.png?v=15.1)  
>    
>  Did you do anything different for the GU chart?
> 
> Ignored

I have the same. Demo trade account on FXDD  
  
regards  
Nick 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#187](/thread/post/2609350#post2609350 "Post Permalink")

  * Mar 18, 2009 2:40am  Mar 18, 2009 2:40am 

  * [ paradoxical](paradoxical)

  * | Joined Nov 2007  | Status: Trader | [1,186 Posts](/search?do=process&provider=Member&searchuser=54706)

The 104r8 just got another 20 pip win, buying at 1.2997 and closing not too long afterwards. I looked at the trade and thought it was buying too late in the trend. What do I know, eh? ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
Any more of this, and I'll be forced to move a little bit of money over to FXDD! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#188](/thread/post/2609446#post2609446 "Post Permalink")

  * Mar 18, 2009 3:14am  Mar 18, 2009 3:14am 

  * [ Wizhoo](wizhoo)

  * | Joined Sep 2008  | Status: Trader | [33 Posts](/search?do=process&provider=Member&searchuser=79692)

> [Quoting nickmead](/thread/post/2609204#post2609204 "View Quoted Post")
> 
> Disliked
> 
> I have the same. Demo trade account on FXDD  
>    
>  regards  
>  Nick
> 
> Ignored

Thanks for your reply.   
  
I'm on FXDD too, and have 8 pairs open but EUR is the only pair that has produced any action. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#189](/thread/post/2609450#post2609450 "Post Permalink")

  * Mar 18, 2009 3:15am  Mar 18, 2009 3:15am 

  * [ Wizhoo](wizhoo)

  * | Joined Sep 2008  | Status: Trader | [33 Posts](/search?do=process&provider=Member&searchuser=79692)

> [Quoting paradoxical](/thread/post/2609350#post2609350 "View Quoted Post")
> 
> Disliked
> 
> The 104r8 just got another 20 pip win, buying at 1.2997 and closing not too long afterwards. I looked at the trade and thought it was buying too late in the trend. What do I know, eh? ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
>  Any more of this, and I'll be forced to move a little bit of money over to FXDD!
> 
> Ignored

Ditto ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#190](/thread/post/2609534#post2609534 "Post Permalink")

  * Mar 18, 2009 4:00am  Mar 18, 2009 4:00am 

  * [ Dan Johnston](dan*johnston)

  * | Joined May 2008  | Status: Trader | [354 Posts](/search?do=process&provider=Member&searchuser=69420)

FXDD will have to compensate us somehow at the end of all this...For all the business we'll be bringing them.![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)  
  
Hope they don't mind their customers making money too! They say they welcome that, as they should if they are who and what they say they are.  
  
Now 18 and 0 on my fxdd account! Last trade got 20 with only -16 pips dd if that.  
  
Siobi should start charging us.![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)

Attached Image (click to enlarge)

[![Click to Enlarge

Name: v104fxdd3 17b109.gif
Size: 45 KB](/attachment/image/219871/thumbnail?d=1365565299)](/attachment/image/219871?d=1237316187)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#191](/thread/post/2609584#post2609584 "Post Permalink")

  * Edited 4:37am  Mar 18, 2009 4:23am | Edited 4:37am 

  * [ Dan Johnston](dan*johnston)

  * | Joined May 2008  | Status: Trader | [354 Posts](/search?do=process&provider=Member&searchuser=69420)

> [Quoting stinger007](/thread/post/2609052#post2609052 "View Quoted Post")
> 
> Disliked
> 
> nearly 24 hours and no trades on live, working fine on my demo account ARRRGGGG  
>    
>  Anyone help??  
>    
>  many thanks
> 
> Ignored

I hope the tick data is the same from demo to live account in Alpari, and FXDD for that matter. Otherwise we may have to enter manually from demo signal, and be satisfied with less than 20.  
  
If all your settings are identical, we will have to wait for Siobi, or someone who has some experience with an ea on live account. (When I was live I only traded manually.)  
  
I would give it some more time and see if it's just more selective or dead in the water.  
  
I am going to test the waters with my live fxdd acct. which has a $100 bonus that they were kind enough to offer me when I opened it.  
....Wish they still had that 3% match though!![](https://resources.faireconomy.media/images/emojis/64/1f641.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#192](/thread/post/2609590#post2609590 "Post Permalink")

  * Mar 18, 2009 4:25am  Mar 18, 2009 4:25am 

  * [ nickmead](nickmead)

  * | Commercial User  | Joined Feb 2008 | [66 Posts](/search?do=process&provider=Member&searchuser=61524)

OK, Those of you trading NY and London sessions, are you setting it to Hourstart 0 and Hourend 24 in which case what do you set closehour to?  
  
thx in advance  
  
Nick 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#193](/thread/post/2609591#post2609591 "Post Permalink")

  * Mar 18, 2009 4:25am  Mar 18, 2009 4:25am 

  * [ Wizhoo](wizhoo)

  * | Joined Sep 2008  | Status: Trader | [33 Posts](/search?do=process&provider=Member&searchuser=79692)

> [Quoting Dan Johnston](/thread/post/2609534#post2609534 "View Quoted Post")
> 
> Disliked
> 
>   
>  Siobi should start charging us.![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)
> 
> Ignored

  
Shhhh.....![](https://resources.faireconomy.media/images/emojis/64/1f910.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#194](/thread/post/2609633#post2609633 "Post Permalink")

  * Mar 18, 2009 4:41am  Mar 18, 2009 4:41am 

  * [ qz10cq](qz10cq)

  * | Joined Dec 2006  | Status: Trader | [303 Posts](/search?do=process&provider=Member&searchuser=29720)

> [Quoting nickmead](/thread/post/2609080#post2609080 "View Quoted Post")
> 
> Disliked
> 
> what are your time settings  
>    
>  thx  
>  Nick  
>    
>  great work by the way....some serious pippige there ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)
> 
> Ignored

Nick, I'm testing all day to see what happens, Siobi recommends you run it out of the box and he's the master of this EA. To make it run all day you set close hours to 30, hour start to 0 and hour end to 24. Siobi built this EA to run on eur/usd only, I'm just testing to see if it is profitable on other pairs under a 10 spread. I also set spread at 10.  
  
Remember guys Siobi set this up to run the asian market and only on eur/usd. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#195](/thread/post/2609648#post2609648 "Post Permalink")

  * Edited 5:01am  Mar 18, 2009 4:46am | Edited 5:01am 

  * [ Dan Johnston](dan*johnston)

  * | Joined May 2008  | Status: Trader | [354 Posts](/search?do=process&provider=Member&searchuser=69420)

Lol, Wizhoo.  
  
Ok, I'm now officially trading my live fxdd .01 lots for 10 cents a pip account. ($100 live mini account to test for now.) 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#196](/thread/post/2609675#post2609675 "Post Permalink")

  * Mar 18, 2009 4:55am  Mar 18, 2009 4:55am 

  * [ paradoxical](paradoxical)

  * | Joined Nov 2007  | Status: Trader | [1,186 Posts](/search?do=process&provider=Member&searchuser=54706)

Dan, I think that's right. Also, your trade and mine matched identically on FXDD, which is a good sign. I just KNOWWWW live will work just as well. (no negative vibes here) 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#197](/thread/post/2609699#post2609699 "Post Permalink")

  * Edited 5:23am  Mar 18, 2009 5:05am | Edited 5:23am 

  * [ Dan Johnston](dan*johnston)

  * | Joined May 2008  | Status: Trader | [354 Posts](/search?do=process&provider=Member&searchuser=69420)

> [Quoting paradoxical](/thread/post/2609675#post2609675 "View Quoted Post")
> 
> Disliked
> 
> Dan, I think that's right. Also, your trade and mine matched identically on FXDD, which is a good sign. I just KNOWWWW live will work just as well. (no negative vibes here)
> 
> Ignored

Yea, I called fxdd and they confirmed that .01 is 10 cents on my mini account. ...__Before_ you answered_. LOL .  
  
I actually opened this account quite a while ago but never used it and wasn't absolutely sure it was a "mini" live account.  
  
Thanks bud!  
  
![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#198](/thread/post/2609741#post2609741 "Post Permalink")

  * Mar 18, 2009 5:24am  Mar 18, 2009 5:24am 

  * [ rewing](rewing)

  * | Joined Feb 2009  | Status: Trader | [8 Posts](/search?do=process&provider=Member&searchuser=94576)

When I attach it to my chart...I do not gat a smiley face...  
I have all the indicators & the template...what could I be doing wrong?  
Ron 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#199](/thread/post/2609777#post2609777 "Post Permalink")

  * Mar 18, 2009 5:40am  Mar 18, 2009 5:40am 

  * [ paradoxical](paradoxical)

  * | Joined Nov 2007  | Status: Trader | [1,186 Posts](/search?do=process&provider=Member&searchuser=54706)

Make sure that "Allow live trading" on the EA itself is checked. You do that by clicking on "Properties" and then going to the "Common" folder. Also, up top, on the chart, you have to make sure you click the "Expert Advisors" to ON

> [Quoting rewing](/thread/post/2609741#post2609741 "View Quoted Post")
> 
> Disliked
> 
> When I attach it to my chart...I do not gat a smiley face...  
>  I have all the indicators & the template...what could I be doing wrong?  
>  Ron
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#200](/thread/post/2609784#post2609784 "Post Permalink")

  * Mar 18, 2009 5:44am  Mar 18, 2009 5:44am 

  * [ rewing](rewing)

  * | Joined Feb 2009  | Status: Trader | [8 Posts](/search?do=process&provider=Member&searchuser=94576)

The ea box was not on.... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * FX_30M Bouncing System
  *   * [ **Reply to Thread** ](/thread/157406-fx30m-bouncing-system/reply#reply)

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

[The Bouncing Pip](/thread/88277-the-bouncing-pip "Hi everyone. 
 
I present to you a system called &quot;The Bouncing Pip&quot; 
 
This is a system that was originally developed by BigBear, so full...") 26 replies

[Price bouncing off of sma](/thread/228922-price-bouncing-off-of-sma "What is the logic behind a price bouncing off an SMA? 
 
For example if a price bounces of a 35 day sma, i should short it if bounces of...") 2 replies

[Developing a correlated bouncing system](/thread/158016-developing-a-correlated-bouncing-system "The above indicator is a simple ma indicator with the weekly ma set to 40. 
 
I like most of my bouncing signals to be in the direction of...") 9 replies

[bouncing candle indicator](/thread/105826-bouncing-candle-indicator "I once had an indicator that would  send  off an alert whenever a candle touched back on its  moving average.  Lost it somehow, but I do...") 0 replies

[Price bouncing off support or resistance,your thoughts](/thread/30984-price-bouncing-off-support-or-resistanceyour-thoughts "I would like to start a discussuion about price movement at support/resistance, Fib and pivot levels.  
  
Time and again I see the price...") 11 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/157406-fx30m-bouncing-system/reply#reply)
  * Subscribe
  * [72](javascript:void\(0\);)

Attachments: FX_30M Bouncing System

Tags: FX_30M Bouncing System

#  [](/thread/157406-fx30m-bouncing-system)FX_30M Bouncing System 

  * 

  * [#201](/thread/post/2609900#post2609900 "Post Permalink")

  * Mar 18, 2009 6:44am  Mar 18, 2009 6:44am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar95636_4.gif) Tank007](tank007)

  * | Joined Mar 2009  | Status: Trader | [4 Posts](/search?do=process&provider=Member&searchuser=95636)

Guys - interested in this and have the EA loaded but one question. I have a 5 digit broker and have set it to true but do I still need to change the TP and SL to 200 and 1000 respectively because of the 5 digits ( or does the EA take care of that?)  
  
Can someone let me know so I can get this going tonight.  
  
Cheers  
DT 

Light dawns on marble head DT

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#202](/thread/post/2609951#post2609951 "Post Permalink")

  * Mar 18, 2009 7:15am  Mar 18, 2009 7:15am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar95566_5.gif) stifland](stifland)

  * | Joined Mar 2009  | Status: Trader | [304 Posts](/search?do=process&provider=Member&searchuser=95566)

Dan, we are all jinxed now![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)  
Good luck with the micro.  
I am trying eur/jpy today...  
Now have to fill out bracket so I can make some real money. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#203](/thread/post/2609965#post2609965 "Post Permalink")

  * Mar 18, 2009 7:27am  Mar 18, 2009 7:27am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83889_5.gif) siobi](siobi)

  * | Joined Oct 2008  | Status: Trader | [717 Posts](/search?do=process&provider=Member&searchuser=83889)

> [Quoting walrus_78](/thread/post/2609016#post2609016 "View Quoted Post")
> 
> Disliked
> 
> Hello, I'm new in this forum but i find this EA very promising,   
>    
>  I have some questions, which inputs do you use for the EA and also for the Indicators?, can it be used in several pairs at the same time in the same account?  
>    
>  thank you
> 
> Ignored

hi there,  
sorry for the late reply.... people here are now doing all sorts of testing.... very noisy... ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
  
in the first post, I hadmentioned I trade it in live for EU pair ONLY.  
  
but some of them test it on other pairs and it is also quite promising...  
  
good luck.. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#204](/thread/post/2609971#post2609971 "Post Permalink")

  * Mar 18, 2009 7:31am  Mar 18, 2009 7:31am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83889_5.gif) siobi](siobi)

  * | Joined Oct 2008  | Status: Trader | [717 Posts](/search?do=process&provider=Member&searchuser=83889)

> [Quoting rewing](/thread/post/2609784#post2609784 "View Quoted Post")
> 
> Disliked
> 
> The ea box was not on....
> 
> Ignored

are you able to get it runnning now? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#205](/thread/post/2609976#post2609976 "Post Permalink")

  * Mar 18, 2009 7:32am  Mar 18, 2009 7:32am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83889_5.gif) siobi](siobi)

  * | Joined Oct 2008  | Status: Trader | [717 Posts](/search?do=process&provider=Member&searchuser=83889)

> [Quoting Wizhoo](/thread/post/2609591#post2609591 "View Quoted Post")
> 
> Disliked
> 
> Shhhh.....![](https://resources.faireconomy.media/images/emojis/64/1f910.png?v=15.1)
> 
> Ignored

No worries, as mentioned, no charge nad it is free...  
  
but we need to keep on configure it monthly basis,  
there is no EA can work for whole life.... must keep tuning...  
  
keep the pace on and well done all... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#206](/thread/post/2609979#post2609979 "Post Permalink")

  * Edited 7:46am  Mar 18, 2009 7:33am | Edited 7:46am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83889_5.gif) siobi](siobi)

  * | Joined Oct 2008  | Status: Trader | [717 Posts](/search?do=process&provider=Member&searchuser=83889)

> [Quoting Tank007](/thread/post/2609900#post2609900 "View Quoted Post")
> 
> Disliked
> 
> Guys - interested in this and have the EA loaded but one question. I have a 5 digit broker and have set it to true but do I still need to change the TP and SL to 200 and 1000 respectively because of the 5 digits ( or does the EA take care of that?)  
>    
>  Can someone let me know so I can get this going tonight.  
>    
>  Cheers  
>  DT
> 
> Ignored

  
TP and SL can be normal pip stop to 20 and 100. the EA will take care of this once u set the num_of_digit to true. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#207](/thread/post/2610021#post2610021 "Post Permalink")

  * Mar 18, 2009 7:57am  Mar 18, 2009 7:57am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83889_5.gif) siobi](siobi)

  * | Joined Oct 2008  | Status: Trader | [717 Posts](/search?do=process&provider=Member&searchuser=83889)

guys, is time for a vote!!! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#208](/thread/post/2610040#post2610040 "Post Permalink")

  * Mar 18, 2009 8:05am  Mar 18, 2009 8:05am 

  * [ Dan Johnston](dan*johnston)

  * | Joined May 2008  | Status: Trader | [354 Posts](/search?do=process&provider=Member&searchuser=69420)

Guys and gals, I will now be dependent on you all to compare your "demo" fxdd accounts to my "live" mini small deposit - fxdd $100 bonus - account.   
  
Hopefully, the amazing performance will keep up on all our accounts!!!  
  
Why can't I vote twice, dammit!!! ...I'm special!!!![](https://resources.faireconomy.media/images/emojis/64/1f61c.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#209](/thread/post/2610045#post2610045 "Post Permalink")

  * Mar 18, 2009 8:09am  Mar 18, 2009 8:09am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83889_5.gif) siobi](siobi)

  * | Joined Oct 2008  | Status: Trader | [717 Posts](/search?do=process&provider=Member&searchuser=83889)

> [Quoting Dan Johnston](/thread/post/2610040#post2610040 "View Quoted Post")
> 
> Disliked
> 
> Guys and gals, I will now be dependent on you all to compare your "demo" fxdd accounts to my "live" mini small deposit - fxdd $100 bonus - account.   
>    
>  Hopefully, the amazing performance will keep up on all our accounts!!!  
>    
>  Why can't I vote twice, dammit!!! ...I'm special!!!![](https://resources.faireconomy.media/images/emojis/64/1f61c.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)
> 
> Ignored

  
wow,  
who else trade in live?  
  
1) siobi (IBFX mini)(R9 dev ver)  
2) dan (FXDD mini)(R8 release ver) 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#210](/thread/post/2610053#post2610053 "Post Permalink")

  * Mar 18, 2009 8:15am  Mar 18, 2009 8:15am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar95566_5.gif) stifland](stifland)

  * | Joined Mar 2009  | Status: Trader | [304 Posts](/search?do=process&provider=Member&searchuser=95566)

Live-FXDD mini.  
Just let me know exact settings you want to run for forward test. Prefer only Asian as at work during day and I tend to mess with settings![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#211](/thread/post/2610063#post2610063 "Post Permalink")

  * Mar 18, 2009 8:21am  Mar 18, 2009 8:21am 

  * [ ClearTrade](cleartrade)

  * | Joined Dec 2008  | Status: Trader | [75 Posts](/search?do=process&provider=Member&searchuser=88051)

I've been convinced. I'll be trading the R8 version live with IBFX starting today on the 30min chart. Be it known that I will only be using .1 lots which amounts to .10 cents a lot until I'm fully convinced.  
  
I will still be trading manually but due to my J.O.B I really need something to give me some positive pips while at work.   
  
Dan, I know that you asked me a while ago about the number of EA's I use. However since then I had given up on EA's until now. I have been trading successfully manually using John Edwards strategy but have always been a fan of Siobi and the work he does on this forum.  
  
Hopefully IBFX don't try any stupid tricks like freezing platforms and other games that they play with live trading when this EA starts producing real $$ for people. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#212](/thread/post/2610067#post2610067 "Post Permalink")

  * Mar 18, 2009 8:23am  Mar 18, 2009 8:23am 

  * [ stinger007](stinger007)

  * | Joined Sep 2008  | Status: Trader | [94 Posts](/search?do=process&provider=Member&searchuser=80985)

> [Quoting siobi](/thread/post/2610045#post2610045 "View Quoted Post")
> 
> Disliked
> 
> wow,  
>  who else trade in live?  
>    
>  1) siobi (IBFX mini)(R9 dev ver)  
>  2) dan (FXDD mini)(R8 release ver)
> 
> Ignored

Had my ea running for 2 days in live acccount with no trades taken, i'm beginning to think this is never going to work with Alpari Live 5 digits.....works on demo great 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#213](/thread/post/2610078#post2610078 "Post Permalink")

  * Mar 18, 2009 8:34am  Mar 18, 2009 8:34am 

  * [ paradoxical](paradoxical)

  * | Joined Nov 2007  | Status: Trader | [1,186 Posts](/search?do=process&provider=Member&searchuser=54706)

I haven't gotten any trades on IBFX, but works fine on FXDD. Good luck trying it live. I'd like it to work on IBFX live, as my account is with them.

> [Quoting ClearTrade](/thread/post/2610063#post2610063 "View Quoted Post")
> 
> Disliked
> 
> I've been convinced. I'll be trading the R8 version live with IBFX starting today on the 30min chart. Be it known that I will only be using .1 lots which amounts to .10 cents a lot until I'm fully convinced.  
>    
>  I will still be trading manually but due to my J.O.B I really need something to give me some positive pips while at work.   
>    
>  Dan, I know that you asked me a while ago about the number of EA's I use. However since then I had given up on EA's until now. I have been trading successfully manually using John Edwards strategy but have always been...
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#214](/thread/post/2610081#post2610081 "Post Permalink")

  * Mar 18, 2009 8:38am  Mar 18, 2009 8:38am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83889_5.gif) siobi](siobi)

  * | Joined Oct 2008  | Status: Trader | [717 Posts](/search?do=process&provider=Member&searchuser=83889)

> [Quoting paradoxical](/thread/post/2610078#post2610078 "View Quoted Post")
> 
> Disliked
> 
> I haven't gotten any trades on IBFX, but works fine on FXDD. Good luck trying it live. I'd like it to work on IBFX live, as my account is with them.
> 
> Ignored

haha, my live acct also with IBFX.... haiz... maybe later when I got more money, for sure I'll move to FXDD.....  
  
and help FXDD to make free advertisement!!!!! hahahahahah  
  
damn IBFX 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#215](/thread/post/2610128#post2610128 "Post Permalink")

  * Mar 18, 2009 9:17am  Mar 18, 2009 9:17am 

  * [ paradoxical](paradoxical)

  * | Joined Nov 2007  | Status: Trader | [1,186 Posts](/search?do=process&provider=Member&searchuser=54706)

Siobi, you're saying you're using the EA live on IBFX? If so, that's great! I wonder why I can't get any trades on the demo. Using v104R8 on 30 minute chart.

> [Quoting siobi](/thread/post/2610081#post2610081 "View Quoted Post")
> 
> Disliked
> 
> haha, my live acct also with IBFX.... haiz... maybe later when I got more money, for sure I'll move to FXDD.....  
>    
>  and help FXDD to make free advertisement!!!!! hahahahahah  
>    
>  damn IBFX
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#216](/thread/post/2610150#post2610150 "Post Permalink")

  * Mar 18, 2009 9:25am  Mar 18, 2009 9:25am 

  * [ ClearTrade](cleartrade)

  * | Joined Dec 2008  | Status: Trader | [75 Posts](/search?do=process&provider=Member&searchuser=88051)

I agree, IBFX is acting very shady lately, don't quite know what is going on but it's obvious that they are trying to prevent successful trades from happening. I've had a trade that was positive 30 pips but could not close it due to them freezing my platform. When it started working again the trade was in the negative but I kept it open for two more hours and closed it with a positive 4 pips. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#217](/thread/post/2610171#post2610171 "Post Permalink")

  * Mar 18, 2009 9:38am  Mar 18, 2009 9:38am 

  * [ paradoxical](paradoxical)

  * | Joined Nov 2007  | Status: Trader | [1,186 Posts](/search?do=process&provider=Member&searchuser=54706)

Let me know if your EA works on IBFX live. If it does, I'll go live at small lots to start. One guy I know claims proof that they fool around with the spread, and others claim they hunt for stops. Haven't heard they freeze platforms so you can't close out a trade. Of course, they have the requotes in a fast moving market. I have no problem in moving some $ to FXDD if they're better with this EA. 

> [Quoting ClearTrade](/thread/post/2610150#post2610150 "View Quoted Post")
> 
> Disliked
> 
> I agree, IBFX is acting very shady lately, don't quite know what is going on but it's obvious that they are trying to prevent successful trades from happening. I've had a trade that was positive 30 pips but could not close it due to them freezing my platform. When it started working again the trade was in the negative but I kept it open for two more hours and closed it with a positive 4 pips.
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#218](/thread/post/2610507#post2610507 "Post Permalink")

  * Mar 18, 2009 1:46pm  Mar 18, 2009 1:46pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83889_5.gif) siobi](siobi)

  * | Joined Oct 2008  | Status: Trader | [717 Posts](/search?do=process&provider=Member&searchuser=83889)

guys, I had mentioned, I trade in live acct with IBFX mini acct.  
  
so far 2 loser kick out -50 pip with my stoploss.  
  
1 trade skip due to platform FREEZE...  
  
this EA having spread control so no worries on it.  
  
others who is using 100 pip SL, still in the winning track...  
  
Regards,  
Siobi 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#219](/thread/post/2610534#post2610534 "Post Permalink")

  * Mar 18, 2009 2:08pm  Mar 18, 2009 2:08pm 

  * [ paradoxical](paradoxical)

  * | Joined Nov 2007  | Status: Trader | [1,186 Posts](/search?do=process&provider=Member&searchuser=54706)

Siobi, I'll try the EA live soon on my IBFX account to see if it works. On my FXDD demo account, trade opened at a sell at 1.3016 and was down 40 PIPS, and had me thinking the reason was that Dan Johnson must have just gone live. Now it's only down 18 PIPS. so maybe Dan hasn't gone live yet. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#220](/thread/post/2610552#post2610552 "Post Permalink")

  * Mar 18, 2009 2:25pm  Mar 18, 2009 2:25pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83889_5.gif) siobi](siobi)

  * | Joined Oct 2008  | Status: Trader | [717 Posts](/search?do=process&provider=Member&searchuser=83889)

I had no idea who had went to live.  
  
the true is I'm trade in live...  
  
I trade it with my own risk......  
  
you can choose not to is all up to u... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * FX_30M Bouncing System
  *   * [ **Reply to Thread** ](/thread/157406-fx30m-bouncing-system/reply#reply)

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

[The Bouncing Pip](/thread/88277-the-bouncing-pip "Hi everyone. 
 
I present to you a system called &quot;The Bouncing Pip&quot; 
 
This is a system that was originally developed by BigBear, so full...") 26 replies

[Price bouncing off of sma](/thread/228922-price-bouncing-off-of-sma "What is the logic behind a price bouncing off an SMA? 
 
For example if a price bounces of a 35 day sma, i should short it if bounces of...") 2 replies

[Developing a correlated bouncing system](/thread/158016-developing-a-correlated-bouncing-system "The above indicator is a simple ma indicator with the weekly ma set to 40. 
 
I like most of my bouncing signals to be in the direction of...") 9 replies

[bouncing candle indicator](/thread/105826-bouncing-candle-indicator "I once had an indicator that would  send  off an alert whenever a candle touched back on its  moving average.  Lost it somehow, but I do...") 0 replies

[Price bouncing off support or resistance,your thoughts](/thread/30984-price-bouncing-off-support-or-resistanceyour-thoughts "I would like to start a discussuion about price movement at support/resistance, Fib and pivot levels.  
  
Time and again I see the price...") 11 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/157406-fx30m-bouncing-system/reply#reply)
  * Subscribe
  * [72](javascript:void\(0\);)

Attachments: FX_30M Bouncing System

Tags: FX_30M Bouncing System

#  [](/thread/157406-fx30m-bouncing-system)FX_30M Bouncing System 

  * 

  * [#221](/thread/post/2610663#post2610663 "Post Permalink")

  * Mar 18, 2009 3:55pm  Mar 18, 2009 3:55pm 

  * [ ebpippin](ebpippin)

  * | Joined Jun 2008  | Status: Trader | [24 Posts](/search?do=process&provider=Member&searchuser=71058)

hi everybody. i just wanted to know is it normal for this ea to have 2 positions open at the same time because it opened 1 sell at 2:00 then a buy at 7:30. Both are still presently open at the time. I am using Alpari also. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#222](/thread/post/2610710#post2610710 "Post Permalink")

  * Mar 18, 2009 4:23pm  Mar 18, 2009 4:23pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar82982_5.gif) Naresh](naresh)

  * | Joined Oct 2008  | Status: Mind Matters | [28 Posts](/search?do=process&provider=Member&searchuser=82982)

> [Quoting siobi](/thread/post/2610045#post2610045 "View Quoted Post")
> 
> Disliked
> 
> wow,  
>  who else trade in live?  
>    
>  1) siobi (IBFX mini)(R9 dev ver)  
>  2) dan (FXDD mini)(R8 release ver)
> 
> Ignored

I have been testing this live on IBFX. Not 24 hours though so I must be missing all the winners.  
  
I only have 2 loosing trades.  
  
regards  
  
Naresh 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#223](/thread/post/2610765#post2610765 "Post Permalink")

  * Mar 18, 2009 4:52pm  Mar 18, 2009 4:52pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83889_5.gif) siobi](siobi)

  * | Joined Oct 2008  | Status: Trader | [717 Posts](/search?do=process&provider=Member&searchuser=83889)

shit!!!!!!!!!!!  
  
  
losing another 50 pip!!! I had no idea why my R9 behave like this!!!!!!  
I'm MAD 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#224](/thread/post/2610948#post2610948 "Post Permalink")

  * Mar 18, 2009 6:25pm  Mar 18, 2009 6:25pm 

  * [ Dan Johnston](dan*johnston)

  * | Joined May 2008  | Status: Trader | [354 Posts](/search?do=process&provider=Member&searchuser=69420)

> [Quoting paradoxical](/thread/post/2610534#post2610534 "View Quoted Post")
> 
> Disliked
> 
> Siobi, I'll try the EA live soon on my IBFX account to see if it works. On my FXDD demo account, trade opened at a sell at 1.3016 and was down 40 PIPS, and had me thinking the reason was that Dan Johnson must have just gone live. Now it's only down 18 PIPS. so maybe Dan hasn't gone live yet.
> 
> Ignored

I'd be laughing my ass off if my life didn't depend on this!  
  
Oh, hell, I'm still laughing!  
  
We all gotta die sometime!![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)  
  
_...Just kidding. Ain't nobody gonna be dying on this thread!!!_  
  
  
  
PS: so far, no trades taken on fxdd live acct., winning or otherwise. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#225](/thread/post/2611336#post2611336 "Post Permalink")

  * Mar 18, 2009 9:25pm  Mar 18, 2009 9:25pm 

  * [ qz10cq](qz10cq)

  * | Joined Dec 2006  | Status: Trader | [303 Posts](/search?do=process&provider=Member&searchuser=29720)

> [Quoting ebpippin](/thread/post/2610663#post2610663 "View Quoted Post")
> 
> Disliked
> 
> hi everybody. i just wanted to know is it normal for this ea to have 2 positions open at the same time because it opened 1 sell at 2:00 then a buy at 7:30. Both are still presently open at the time. I am using Alpari also.
> 
> Ignored

I have the same thing going on right now, first time I've seen this with Siobi's EA. The market has been real strange lately, don't know if this is the time to go live guys but you can't win if you don't play. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#226](/thread/post/2611493#post2611493 "Post Permalink")

  * Mar 18, 2009 10:09pm  Mar 18, 2009 10:09pm 

  * [ paradoxical](paradoxical)

  * | Joined Nov 2007  | Status: Trader | [1,186 Posts](/search?do=process&provider=Member&searchuser=54706)

As far as opening two positions, I'm using the v014R8 also on the AUD/USD and it opened a sell at 11:00, which was down 28 PIPS, and opened a BUY at 16:00, and I have two positions open on that pair now.  
On the EUR/USD, it has opened 6 positions, and 5 were 20 PIP winners, and one broke even.  
Also tried it on USD/JPY for a 20 PIP winner. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#227](/thread/post/2611535#post2611535 "Post Permalink")

  * Mar 18, 2009 10:18pm  Mar 18, 2009 10:18pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar95566_5.gif) stifland](stifland)

  * | Joined Mar 2009  | Status: Trader | [304 Posts](/search?do=process&provider=Member&searchuser=95566)

I will forward test live fxdd.  
open 0  
stop 10 close 11  
30m  
  
If I was confident mt4 would always be on, no power outages or internet etc. i would go 24 hour , but not gonna do it yet .. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#228](/thread/post/2612145#post2612145 "Post Permalink")

  * Mar 19, 2009 1:24am  Mar 19, 2009 1:24am 

  * [ ClearTrade](cleartrade)

  * | Joined Dec 2008  | Status: Trader | [75 Posts](/search?do=process&provider=Member&searchuser=88051)

Went live with it last night and has had two trades. One went for 10 pips and the other broke even. I'm using an additional trade manager so most of the time I won't get the 20pip profit but it saves me from the large losses. The version is R8 on a 30min chart. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#229](/thread/post/2612174#post2612174 "Post Permalink")

  * Mar 19, 2009 1:35am  Mar 19, 2009 1:35am 

  * [ paradoxical](paradoxical)

  * | Joined Nov 2007  | Status: Trader | [1,186 Posts](/search?do=process&provider=Member&searchuser=54706)

Thanks, Clear Trade. Posts that show how people have fared, particularly live, are very helpful to me in making decisions. From what you posted, was probably the same two trades my FXDD demo took. As you also have a live IBFX account that's working, that's good to know, too. Just as soon as the fed is done saying whatever it is they have to say today, I'm going to start the EA on my live account. For who knows what reason, it doesn't work on my IBFX demo.

> [Quoting ClearTrade](/thread/post/2612145#post2612145 "View Quoted Post")
> 
> Disliked
> 
> Went live with it last night and has had two trades. One went for 10 pips and the other broke even. I'm using an additional trade manager so most of the time I won't get the 20pip profit but it saves me from the large losses. The version is R8 on a 30min chart.
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#230](/thread/post/2612235#post2612235 "Post Permalink")

  * Mar 19, 2009 2:02am  Mar 19, 2009 2:02am 

  * [ Wizhoo](wizhoo)

  * | Joined Sep 2008  | Status: Trader | [33 Posts](/search?do=process&provider=Member&searchuser=79692)

I'm running FXDD Demo and entering live trades to my [Oanda](/brokers/oanda "View OANDA Broker Profile") account manually when I get an alert signal. Sometimes I get in on the trade a little late but it has not hurt the winners too much.   
  
All of my trades, using this system, have been winners with the exception of one 50 pip loss last night. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#231](/thread/post/2613724#post2613724 "Post Permalink")

  * Mar 19, 2009 9:45am  Mar 19, 2009 9:45am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar95566_5.gif) stifland](stifland)

  * | Joined Mar 2009  | Status: Trader | [304 Posts](/search?do=process&provider=Member&searchuser=95566)

fxdd here went short 1.3444 on 03:30 bar......  
current trade 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#232](/thread/post/2613736#post2613736 "Post Permalink")

  * Mar 19, 2009 9:49am  Mar 19, 2009 9:49am 

  * [ Wizhoo](wizhoo)

  * | Joined Sep 2008  | Status: Trader | [33 Posts](/search?do=process&provider=Member&searchuser=79692)

Did anyone get any trades today?  
  
Crazy bull run today ![](https://resources.faireconomy.media/images/emojis/64/1f923.png?v=15.1)   
How long will it take for things to settle before signals are valid again? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#233](/thread/post/2613742#post2613742 "Post Permalink")

  * Mar 19, 2009 9:51am  Mar 19, 2009 9:51am 

  * [ Wizhoo](wizhoo)

  * | Joined Sep 2008  | Status: Trader | [33 Posts](/search?do=process&provider=Member&searchuser=79692)

> [Quoting stifland](/thread/post/2613724#post2613724 "View Quoted Post")
> 
> Disliked
> 
> fxdd here went short 1.3444 on 03:30 bar......  
>  current trade
> 
> Ignored

Oh yeah, just notice a trade while I was typing. ![](https://resources.faireconomy.media/images/emojis/64/1f64f.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#234](/thread/post/2613749#post2613749 "Post Permalink")

  * Mar 19, 2009 9:53am  Mar 19, 2009 9:53am 

  * [ Wizhoo](wizhoo)

  * | Joined Sep 2008  | Status: Trader | [33 Posts](/search?do=process&provider=Member&searchuser=79692)

GBP just took a short trade also. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#235](/thread/post/2613790#post2613790 "Post Permalink")

  * Mar 19, 2009 10:13am  Mar 19, 2009 10:13am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83889_5.gif) siobi](siobi)

  * | Joined Oct 2008  | Status: Trader | [717 Posts](/search?do=process&provider=Member&searchuser=83889)

hm... since I'm running R9, so the EA do not take this trade.  
  
because overall trend is UP trend, it is risky to take SELL trade...  
  
R9 additional filter  
1) 200SMA  
2) slope for 1h timeframe  
3) previous day Pivot.  
  
hi dan in reading,  
I forgot to send this indicator to you for R9 testing!!! 

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [PrevDayAndFloatingPivot_O.ex4](/attachment/file/220593?d=1237425123) 3 KB | 266 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#236](/thread/post/2613828#post2613828 "Post Permalink")

  * Mar 19, 2009 10:38am  Mar 19, 2009 10:38am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83889_5.gif) siobi](siobi)

  * | Joined Oct 2008  | Status: Trader | [717 Posts](/search?do=process&provider=Member&searchuser=83889)

seems like u guys is having another winning trade of SELL 1.3444... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#237](/thread/post/2613836#post2613836 "Post Permalink")

  * Mar 19, 2009 10:41am  Mar 19, 2009 10:41am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar95566_5.gif) stifland](stifland)

  * | Joined Mar 2009  | Status: Trader | [304 Posts](/search?do=process&provider=Member&searchuser=95566)

we will see siobi. is r9 to be released to forum (worldwide) ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) soon or just in testing?  
It did take sell a bit in a big uptrend on r8. but up 8 pips at moment..... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#238](/thread/post/2613843#post2613843 "Post Permalink")

  * Mar 19, 2009 10:47am  Mar 19, 2009 10:47am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83889_5.gif) siobi](siobi)

  * | Joined Oct 2008  | Status: Trader | [717 Posts](/search?do=process&provider=Member&searchuser=83889)

stifland,  
u just ding me and idea!!!  
  
under the big trend of LONG... once there is a Short signal, why dont the EA take the SELL signal and pickup some quick pip like 10 pip with SL 30 pip?  
  
hm... should give it a try later in R9...  
  
by the way, R9 is now in testing stage... soon will be release before April.  
  
as promised... once a month we configure it. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#239](/thread/post/2613892#post2613892 "Post Permalink")

  * Mar 19, 2009 11:12am  Mar 19, 2009 11:12am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar95566_5.gif) stifland](stifland)

  * | Joined Mar 2009  | Status: Trader | [304 Posts](/search?do=process&provider=Member&searchuser=95566)

I think that is solid. If trend is overextended by X amount, can take a counter trend trade for a smaller tp.  
  
Hit 1.3427. SL moved to breakeven. Then a double bottom and out there at BE.  
  
Nighty night. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#240](/thread/post/2615187#post2615187 "Post Permalink")

  * Mar 19, 2009 9:53pm  Mar 19, 2009 9:53pm 

  * [ FX Warrior](fx*warrior)

  * | Joined Nov 2008  | Status: Trader | [5 Posts](/search?do=process&provider=Member&searchuser=86749)

Hi all!  
  
Want to thank everyone for all the hard work that has gone into this system. I have tested many EA's and this is the most promising yet. I do have a problem with it. I have read similar problems posted here, but there are no solutions to date. I am running IBFX, FXDD MT4 terminals.I have checked all the boxes necesary to engage the EA,running both 1M,30M TF, but have 0 trades taken after 10Hrs Any suggestions? 

" I love humanity - it's people that I have a problem with".......

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * FX_30M Bouncing System
  *   * [ **Reply to Thread** ](/thread/157406-fx30m-bouncing-system/reply#reply)

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

[The Bouncing Pip](/thread/88277-the-bouncing-pip "Hi everyone. 
 
I present to you a system called &quot;The Bouncing Pip&quot; 
 
This is a system that was originally developed by BigBear, so full...") 26 replies

[Price bouncing off of sma](/thread/228922-price-bouncing-off-of-sma "What is the logic behind a price bouncing off an SMA? 
 
For example if a price bounces of a 35 day sma, i should short it if bounces of...") 2 replies

[Developing a correlated bouncing system](/thread/158016-developing-a-correlated-bouncing-system "The above indicator is a simple ma indicator with the weekly ma set to 40. 
 
I like most of my bouncing signals to be in the direction of...") 9 replies

[bouncing candle indicator](/thread/105826-bouncing-candle-indicator "I once had an indicator that would  send  off an alert whenever a candle touched back on its  moving average.  Lost it somehow, but I do...") 0 replies

[Price bouncing off support or resistance,your thoughts](/thread/30984-price-bouncing-off-support-or-resistanceyour-thoughts "I would like to start a discussuion about price movement at support/resistance, Fib and pivot levels.  
  
Time and again I see the price...") 11 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/157406-fx30m-bouncing-system/reply#reply)
  * Subscribe
  * [72](javascript:void\(0\);)

Attachments: FX_30M Bouncing System

Tags: FX_30M Bouncing System

#  [](/thread/157406-fx30m-bouncing-system)FX_30M Bouncing System 

  * 

  * [#241](/thread/post/2615211#post2615211 "Post Permalink")

  * Mar 19, 2009 10:05pm  Mar 19, 2009 10:05pm 

  * [ Orenn](orenn)

  * | Joined Mar 2009  | Status: Trader | [11 Posts](/search?do=process&provider=Member&searchuser=96427)

Actually I have this EA running (in demo) for the last two weeks taking trades with no problem and the last one was 12 hours ago, so you don't have a problem, yet...  
  
Oren 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#242](/thread/post/2615241#post2615241 "Post Permalink")

  * Mar 19, 2009 10:14pm  Mar 19, 2009 10:14pm 

  * [ FX Warrior](fx*warrior)

  * | Joined Nov 2008  | Status: Trader | [5 Posts](/search?do=process&provider=Member&searchuser=86749)

Okay, thanks for the quick response Orenn. Will be watching for the trades. 

" I love humanity - it's people that I have a problem with".......

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#243](/thread/post/2615300#post2615300 "Post Permalink")

  * Mar 19, 2009 10:36pm  Mar 19, 2009 10:36pm 

  * [ paradoxical](paradoxical)

  * | Joined Nov 2007  | Status: Trader | [1,186 Posts](/search?do=process&provider=Member&searchuser=54706)

Mine won't work on IBFX live or demo. Works fine on FXDD.

> [Quoting Orenn](/thread/post/2615211#post2615211 "View Quoted Post")
> 
> Disliked
> 
> Actually I have this EA running (in demo) for the last two weeks taking trades with no problem and the last one was 12 hours ago, so you don't have a problem, yet...  
>    
>  Oren
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#244](/thread/post/2615353#post2615353 "Post Permalink")

  * Mar 19, 2009 10:51pm  Mar 19, 2009 10:51pm 

  * [ FX Warrior](fx*warrior)

  * | Joined Nov 2008  | Status: Trader | [5 Posts](/search?do=process&provider=Member&searchuser=86749)

Paradoxical,  
I will keep monitoring the thread to see if others post trades in just case there is something not right with my setup. 

" I love humanity - it's people that I have a problem with".......

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#245](/thread/post/2615526#post2615526 "Post Permalink")

  * Mar 19, 2009 11:49pm  Mar 19, 2009 11:49pm 

  * [ paradoxical](paradoxical)

  * | Joined Nov 2007  | Status: Trader | [1,186 Posts](/search?do=process&provider=Member&searchuser=54706)

Thanks, FXWarrior. Siobi trades live on IBFX, and I think a few others do. I can't get trades either live or demo. Possibly someone who trades live on IBFX can give me the EA version and whether or not they changed any settings to get it to trade on IBFX? Working very well on FXDD.  

> [Quoting FX Warrior](/thread/post/2615353#post2615353 "View Quoted Post")
> 
> Disliked
> 
> Paradoxical,  
>  I will keep monitoring the thread to see if others post trades in just case there is something not right with my setup.
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#246](/thread/post/2615650#post2615650 "Post Permalink")

  * Mar 20, 2009 12:29am  Mar 20, 2009 12:29am 

  * [ drcubi](drcubi)

  * | Joined Mar 2009  | Status: Trader | [6 Posts](/search?do=process&provider=Member&searchuser=97236)

I have a newbie question, if someone has patience for a newbie ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
  
I am new to MT4, and don't know how to use EA or indeed how to install custom EA's. What Siobi has done seems amazing, and I want to test on a demo account. Just failed to get it going so far. What I did was copy the files on this forum to the "indicators" folder and after that I see it the Custom Indicators list, but what now?  
  
Has anyone written a step by step? If not help me understand what to do and I'll happily write that for the next newbie that comes along.  
  
Darren  
**"non si dimentichi mai"**

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#247](/thread/post/2615679#post2615679 "Post Permalink")

  * Mar 20, 2009 12:37am  Mar 20, 2009 12:37am 

  * [ paradoxical](paradoxical)

  * | Joined Nov 2007  | Status: Trader | [1,186 Posts](/search?do=process&provider=Member&searchuser=54706)

drcubi, we all need to start somewhere. You copied the EA into "indicators", and it needs to be in the "experts" folder. EA stands for Expert Advisor & an EA is nothing more than a computer program containing mathematical equations that do X when Y happens. In this case, if the right amount of "Ys" happen, the EA places a trade.  
When you download the EA, put it in the "experts" folder.  
There are some tabs inside the EA itself. To get there, you click on "properties" on the EA, and it brings them up. On the "COMMON" tab, you need to be sure that "Live Trading" is checked.  
After you do the above, you need to look up top of the chart, and you'll see a icon that looks like a hat called "Expert Advisors". You need to click that to "ON", which makes it turn green. When it's green, it's a GO, and ALL expert advisors you have will then be engaged.  
Finally, on the right hand upper corner of the chart, you'll see the EA you have attatched to that chart. If the face is smiling, it's ON. If it's frowning, it's OFF.  
Also, there's a site called Baby Pips that yopu can check. It's a beginners site that has lots of good info.

> [Quoting drcubi](/thread/post/2615650#post2615650 "View Quoted Post")
> 
> Disliked
> 
> I have a newbie question, if someone has patience for a newbie ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
>    
>  I am new to MT4, and don't know how to use EA or indeed how to install custom EA's. What Siobi has done seems amazing, and I want to test on a demo account. Just failed to get it going so far. What I did was copy the files on this forum to the "indicators" folder and after that I see it the Custom Indicators list, but what now?  
>    
>  Has anyone written a step by step? If not help me understand what to do and I'll happily write that for the next newbie that comes along.  
>    
>  Darren  
>  [b]"non...
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#248](/thread/post/2616073#post2616073 "Post Permalink")

  * Mar 20, 2009 3:01am  Mar 20, 2009 3:01am 

  * [ Wizhoo](wizhoo)

  * | Joined Sep 2008  | Status: Trader | [33 Posts](/search?do=process&provider=Member&searchuser=79692)

I just got a sell signal.  
  
EUR 1.3638 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#249](/thread/post/2616170#post2616170 "Post Permalink")

  * Mar 20, 2009 3:48am  Mar 20, 2009 3:48am 

  * [ Dan Johnston](dan*johnston)

  * | Joined May 2008  | Status: Trader | [354 Posts](/search?do=process&provider=Member&searchuser=69420)

**No trades** at all on fxdd live account.  
  
Please someone do a screenshot of the last 2 or 3 days of trades in fxdd demo account so I can compare with my fxdd live account.  
  
Thanks. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#250](/thread/post/2616213#post2616213 "Post Permalink")

  * Mar 20, 2009 4:10am  Mar 20, 2009 4:10am 

  * [ Wizhoo](wizhoo)

  * | Joined Sep 2008  | Status: Trader | [33 Posts](/search?do=process&provider=Member&searchuser=79692)

Dan, here a shot of my trades for the past few days.  
  
It's a Demo account on FXDD. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: eur.gif
Size: 47 KB](/attachment/image/221091/thumbnail?d=1365565585)](/attachment/image/221091?d=1237489779)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#251](/thread/post/2616271#post2616271 "Post Permalink")

  * Mar 20, 2009 4:29am  Mar 20, 2009 4:29am 

  * [ paradoxical](paradoxical)

  * | Joined Nov 2007  | Status: Trader | [1,186 Posts](/search?do=process&provider=Member&searchuser=54706)

Dan, Here's my FXDD Demo account. Only one trade on the EUR/USD yesterday that got one PIP. Ignore the rest of the trades. Trying this on other pairs. Does NOT work on AUD/USD very well at all.

> [Quoting Dan Johnston](/thread/post/2616170#post2616170 "View Quoted Post")
> 
> Disliked
> 
> **No trades** at all on fxdd live account.  
>    
>  Please someone do a screenshot of the last 2 or 3 days of trades in fxdd demo account so I can compare with my fxdd live account.  
>    
>  Thanks.
> 
> Ignored

Attached Image (click to enlarge)

[![Click to Enlarge

Name: fxdd shot.gif
Size: 103 KB](/attachment/image/221097/thumbnail?d=1365565585)](/attachment/image/221097?d=1237490850)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#252](/thread/post/2616282#post2616282 "Post Permalink")

  * Mar 20, 2009 4:34am  Mar 20, 2009 4:34am 

  * [ Dan Johnston](dan*johnston)

  * | Joined May 2008  | Status: Trader | [354 Posts](/search?do=process&provider=Member&searchuser=69420)

> [Quoting Wizhoo](/thread/post/2616213#post2616213 "View Quoted Post")
> 
> Disliked
> 
> Dan, here a shot of my trades for the past few days.  
>    
>  It's a Demo account on FXDD.
> 
> Ignored

Thank you guys!  
  
Anyone else that's using defaults please do likewise and include drawdowns also.  
  
(Default is 100 pip hard stop.)  
  
Before I went live, the largest drawdown was -67 pips I think. The rest were usually less than -20, so this is quite strange. 18 and 0 with an average of less than -20 pip drawdown is why I decided to test live. So far no results. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#253](/thread/post/2616310#post2616310 "Post Permalink")

  * Mar 20, 2009 4:44am  Mar 20, 2009 4:44am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar94654_2.gif) walrus_78](walrus_78)

  * | Joined Feb 2009  | Status: Trader | [19 Posts](/search?do=process&provider=Member&searchuser=94654)

So what would be the problem with the FXDD live account? why you have no trades and Demo accounts have?  
  
have you tried making back test just to see if the EA trades there?, I do that when I try to be sure that an EA makes trades. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#254](/thread/post/2616311#post2616311 "Post Permalink")

  * Mar 20, 2009 4:44am  Mar 20, 2009 4:44am 

  * [ Wizhoo](wizhoo)

  * | Joined Sep 2008  | Status: Trader | [33 Posts](/search?do=process&provider=Member&searchuser=79692)

> [Quoting Dan Johnston](/thread/post/2616282#post2616282 "View Quoted Post")
> 
> Disliked
> 
> Thank you!  
>    
>  Anyone else that's using defaults please do likewise and include drawdowns also.  
>    
>  (Default is 100 pip hard stop.)
> 
> Ignored

Yeah, I have my stops at 50 except AUD was set at s/l of 30.  
  
100 s/l is hard to stomach for me even on a demo. ![](https://resources.faireconomy.media/images/emojis/64/1f630.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#255](/thread/post/2616319#post2616319 "Post Permalink")

  * Mar 20, 2009 4:47am  Mar 20, 2009 4:47am 

  * [ Wizhoo](wizhoo)

  * | Joined Sep 2008  | Status: Trader | [33 Posts](/search?do=process&provider=Member&searchuser=79692)

It's strange that some of the trades that 'paradoxical' got were not triggered in my account.  
  
Perhaps it has something to do with a different server on FXDD's side. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#256](/thread/post/2616350#post2616350 "Post Permalink")

  * Mar 20, 2009 4:59am  Mar 20, 2009 4:59am 

  * [ ClearTrade](cleartrade)

  * | Joined Dec 2008  | Status: Trader | [75 Posts](/search?do=process&provider=Member&searchuser=88051)

Only one trade taken today so far for a loss of 29 pips on EUR/USD. My trade manager stopped it before it got too ugly and by the way, the trade was a "sell" which is pretty dangerous this week. The trend has definitely been up all week. Only lost $2.90 which I made back up manually but will definitely keep testing.   
  
I'm thinking about testing it in a lower timeframe because the 30min is not showing much movement, Siobi or someone tell me what you think about version R8 running on lets say the 15min or 5min timeframe. Or would version R7 be better. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#257](/thread/post/2616380#post2616380 "Post Permalink")

  * Mar 20, 2009 5:11am  Mar 20, 2009 5:11am 

  * [ paradoxical](paradoxical)

  * | Joined Nov 2007  | Status: Trader | [1,186 Posts](/search?do=process&provider=Member&searchuser=54706)

That can happen. My settings are the default settings, except I chaged the times so it would trade all the time. On one of the trades where you got a loss of 50 PIPS, I barely eeked out 20 pips, before it went back up. If that was on a live account, I would have missed by one pip!@!

> [Quoting Wizhoo](/thread/post/2616319#post2616319 "View Quoted Post")
> 
> Disliked
> 
> It's strange that some of the trades that 'paradoxical' got were not triggered in my account.  
>    
>  Perhaps it has something to do with a different server on FXDD's side.
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#258](/thread/post/2616645#post2616645 "Post Permalink")

  * Mar 20, 2009 7:30am  Mar 20, 2009 7:30am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83889_5.gif) siobi](siobi)

  * | Joined Oct 2008  | Status: Trader | [717 Posts](/search?do=process&provider=Member&searchuser=83889)

> [Quoting Wizhoo](/thread/post/2616073#post2616073 "View Quoted Post")
> 
> Disliked
> 
> I just got a sell signal.  
>    
>  EUR 1.3638
> 
> Ignored

  
hi there, R9 didnt take this trade....  
  
due to .... overall it it still up trend...  
  
if u able to get a quick pip of 10... then u may exit 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#259](/thread/post/2616648#post2616648 "Post Permalink")

  * Mar 20, 2009 7:34am  Mar 20, 2009 7:34am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83889_5.gif) siobi](siobi)

  * | Joined Oct 2008  | Status: Trader | [717 Posts](/search?do=process&provider=Member&searchuser=83889)

> [Quoting ClearTrade](/thread/post/2616350#post2616350 "View Quoted Post")
> 
> Disliked
> 
> Only one trade taken today so far for a loss of 29 pips on EUR/USD. My trade manager stopped it before it got too ugly and by the way, the trade was a "sell" which is pretty dangerous this week. The trend has definitely been up all week. Only lost $2.90 which I made back up manually but will definitely keep testing.   
>    
>  I'm thinking about testing it in a lower timeframe because the 30min is not showing much movement, Siobi or someone tell me what you think about version R8 running on lets say the 15min or 5min timeframe. Or would version R7 be...
> 
> Ignored

hm.. yes.. we all notice about the big trend this week...thus R9 is adding higher timeframe + MA to further filter it off.  
  
for you information, R9 here still no taken any trade yesterday... going to release very soon somewhere after next week testing 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#260](/thread/post/2616654#post2616654 "Post Permalink")

  * Mar 20, 2009 7:41am  Mar 20, 2009 7:41am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83889_5.gif) siobi](siobi)

  * | Joined Oct 2008  | Status: Trader | [717 Posts](/search?do=process&provider=Member&searchuser=83889)

current R8 do NOT take any higher timeframe for the trend filtering purpose!!!  
  
so if you encounter any trade open for the opposite direction, please be carefull and take quick pip to get out if possible.  
  
I do not have any patform running R8   
last trade taken for R9 is at 18Mac 11:00 (ibfx) Buy 1.3048  
  
no trade taken for 19-Mac for R9. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * FX_30M Bouncing System
  *   * [ **Reply to Thread** ](/thread/157406-fx30m-bouncing-system/reply#reply)

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

[The Bouncing Pip](/thread/88277-the-bouncing-pip "Hi everyone. 
 
I present to you a system called &quot;The Bouncing Pip&quot; 
 
This is a system that was originally developed by BigBear, so full...") 26 replies

[Price bouncing off of sma](/thread/228922-price-bouncing-off-of-sma "What is the logic behind a price bouncing off an SMA? 
 
For example if a price bounces of a 35 day sma, i should short it if bounces of...") 2 replies

[Developing a correlated bouncing system](/thread/158016-developing-a-correlated-bouncing-system "The above indicator is a simple ma indicator with the weekly ma set to 40. 
 
I like most of my bouncing signals to be in the direction of...") 9 replies

[bouncing candle indicator](/thread/105826-bouncing-candle-indicator "I once had an indicator that would  send  off an alert whenever a candle touched back on its  moving average.  Lost it somehow, but I do...") 0 replies

[Price bouncing off support or resistance,your thoughts](/thread/30984-price-bouncing-off-support-or-resistanceyour-thoughts "I would like to start a discussuion about price movement at support/resistance, Fib and pivot levels.  
  
Time and again I see the price...") 11 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/157406-fx30m-bouncing-system/reply#reply)
  * Subscribe
  * [72](javascript:void\(0\);)

Attachments: FX_30M Bouncing System

Tags: FX_30M Bouncing System

#  [](/thread/157406-fx30m-bouncing-system)FX_30M Bouncing System 

  * 

  * [#261](/thread/post/2617705#post2617705 "Post Permalink")

  * Mar 20, 2009 5:57pm  Mar 20, 2009 5:57pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar92141_5.gif) tex](tex)

  * | Joined Jan 2009  | Status: Trader | [272 Posts](/search?do=process&provider=Member&searchuser=92141)

hello guys,  
  
v08 took a buy trade today in the morning at 9.00 german time zone. i am down to -50 pips but still in the market. demo account @ [activtrades](/brokers/activtrades "View ActivTrades Broker Profile") (england).  
  
screen : 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: 2009-03-20.jpg
Size: 386 KB](/attachment/image/221382/thumbnail?d=1365565638)](/attachment/image/221382?d=1237539385)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#262](/thread/post/2617725#post2617725 "Post Permalink")

  * Mar 20, 2009 6:09pm  Mar 20, 2009 6:09pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83889_5.gif) siobi](siobi)

  * | Joined Oct 2008  | Status: Trader | [717 Posts](/search?do=process&provider=Member&searchuser=83889)

BUY signal at 1.3716. (IBFX 08:00)  
  
DD -53 pip 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#263](/thread/post/2617803#post2617803 "Post Permalink")

  * Mar 20, 2009 6:53pm  Mar 20, 2009 6:53pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83889_5.gif) siobi](siobi)

  * | Joined Oct 2008  | Status: Trader | [717 Posts](/search?do=process&provider=Member&searchuser=83889)

hm... noticed something...  
  
every time of DD of -50pip, I should have a step order with another 20 pip profit from there with SL 50 pip which is same as first rtade.  
  
eg:  
trade BUY at 1.3716.  
SL 1.3616  
TP 1.3736  
  
DD reach -50 pip,  
another BUY order at 1.3666  
SL 1.3616  
TP 1.3686  
  
![](https://resources.faireconomy.media/images/emojis/64/1f61c.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#264](/thread/post/2617848#post2617848 "Post Permalink")

  * Mar 20, 2009 7:17pm  Mar 20, 2009 7:17pm 

  * [ Wizhoo](wizhoo)

  * | Joined Sep 2008  | Status: Trader | [33 Posts](/search?do=process&provider=Member&searchuser=79692)

My FXDD Demo took a EUR buy at 1.3667 for a +20 pips at 6:30 platform time. Curiously, it also took a GBP sell at 6:11 for a loss.   
  
EUR is doing well. It has a 6/1 win lose ratio for me this week. Testing around the clock. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#265](/thread/post/2617905#post2617905 "Post Permalink")

  * Mar 20, 2009 7:43pm  Mar 20, 2009 7:43pm 

  * [ Orenn](orenn)

  * | Joined Mar 2009  | Status: Trader | [11 Posts](/search?do=process&provider=Member&searchuser=96427)

Siobi,  
  
I think having another order triggered once you hit the 50 pips DD will have similar results as setting a 100 pips SL on the original order, that is - Sometimes it will save some of you losses but when it doesn't work you will be hit hard.  
Personaly I don't think it is worth it.  
  
I have been following your EA from somewhere around the middle of the old thread (1M scalping) and I am very imperessed with it. I am running it on demo for the last two weeks with very good results.  
  
I don't think you will be able to make it a 100% winnig trades. 70% - 80% success will be great. The rest is up to money management to make sure the bottom line is profitable.  
  
Looking forward for further development of this EA  
  
Thanks for everything so far,  
  
Oren 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#266](/thread/post/2618072#post2618072 "Post Permalink")

  * Mar 20, 2009 9:00pm  Mar 20, 2009 9:00pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar95566_5.gif) stifland](stifland)

  * | Joined Mar 2009  | Status: Trader | [304 Posts](/search?do=process&provider=Member&searchuser=95566)

I had same trade last night as wizhoo. Got the +20 before the big tank. Talk to you all over the weekend.  
fxdd. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: lastnight.gif
Size: 84 KB](/attachment/image/221461/thumbnail?d=1365565666)](/attachment/image/221461?d=1237550446)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#267](/thread/post/2618303#post2618303 "Post Permalink")

  * Mar 20, 2009 10:38pm  Mar 20, 2009 10:38pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar94654_2.gif) walrus_78](walrus_78)

  * | Joined Feb 2009  | Status: Trader | [19 Posts](/search?do=process&provider=Member&searchuser=94654)

I had that same order but the EA took another long on EurUsd at 11:00 with -100 pips 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#268](/thread/post/2618506#post2618506 "Post Permalink")

  * Mar 20, 2009 11:47pm  Mar 20, 2009 11:47pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar92141_5.gif) tex](tex)

  * | Joined Jan 2009  | Status: Trader | [272 Posts](/search?do=process&provider=Member&searchuser=92141)

> [Quoting walrus_78](/thread/post/2618303#post2618303 "View Quoted Post")
> 
> Disliked
> 
> I had that same order but the EA took another long on EurUsd at 11:00 with -100 pips
> 
> Ignored

same thing here,the last buy trade hit the -100p hard stop. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#269](/thread/post/2618628#post2618628 "Post Permalink")

  * Mar 21, 2009 12:33am  Mar 21, 2009 12:33am 

  * [ paradoxical](paradoxical)

  * | Joined Nov 2007  | Status: Trader | [1,186 Posts](/search?do=process&provider=Member&searchuser=54706)

Happy to report that the version R8 EA attactched to my live IBFX account is now taking trades. Not so happy that there was a a 20 PIP win and a 100 PIP loss to start, but am only going 10 cents a pip, so no big deal. Also, these two trades were almost identical to the ones taken on my FXDD account, with just a one pip difference on the entries on both.  
Has anyone done a back test on this EA to see if a 50 pip stop is better than a 100 pip stop? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#270](/thread/post/2619975#post2619975 "Post Permalink")

  * Mar 22, 2009 3:06am  Mar 22, 2009 3:06am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar70187_5.gif) WileECoyote](wileecoyote)

  * | Joined May 2008  | Status: Trader | [8 Posts](/search?do=process&provider=Member&searchuser=70187)

Mine did the same thing. 20 Pip win, followed by a -100 pip stop loss. I'm on an IBFX Demo with y'all! 

Changes aren't permanent; but, change is!

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#271](/thread/post/2620516#post2620516 "Post Permalink")

  * Mar 22, 2009 10:25pm  Mar 22, 2009 10:25pm 

  * [ qz10cq](qz10cq)

  * | Joined Dec 2006  | Status: Trader | [303 Posts](/search?do=process&provider=Member&searchuser=29720)

> [Quoting Orenn](/thread/post/2617905#post2617905 "View Quoted Post")
> 
> Disliked
> 
> Siobi,  
>    
>  I think having another order triggered once you hit the 50 pips DD will have similar results as setting a 100 pips SL on the original order, that is - Sometimes it will save some of you losses but when it doesn't work you will be hit hard.  
>  Personaly I don't think it is worth it.  
>    
>  I have been following your EA from somewhere around the middle of the old thread (1M scalping) and I am very imperessed with it. I am running it on demo for the last two weeks with very good results.  
>    
>  I don't think you will be able to make it a 100% winnig trades....
> 
> Ignored

I agree Oren, played last week with a 20tp, 50sl on 10 pairs and ended up losing 300 for the first time with Siobi's EA. Actually thats not bad at all considering what the markets were doing. I like the 100sl, 150tp and 25ts. I don't mind losing 100 every once in awhile as long as the bottom line ends with profit at the end of the week. One of the golden rules of trading is let your profits run and with a 20tp we are not doing that. Will keep the thread informed. Thanks Siobi....Dan 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#272](/thread/post/2620600#post2620600 "Post Permalink")

  * Mar 22, 2009 11:41pm  Mar 22, 2009 11:41pm 

  * [ Dan Johnston](dan*johnston)

  * | Joined May 2008  | Status: Trader | [354 Posts](/search?do=process&provider=Member&searchuser=69420)

> [Quoting qz10cq](/thread/post/2620516#post2620516 "View Quoted Post")
> 
> Disliked
> 
> I agree Oren, played last week with a 20tp, 50sl on 10 pairs and ended up losing 300 for the first time with Siobi's EA. Actually thats not bad at all considering what the markets were doing. I like the 100sl, 150tp and 25ts. I don't mind losing 100 every once in awhile as long as the bottom line ends with profit at the end of the week. One of the golden rules of trading is let your profits run and with a 20tp we are not doing that. Will keep the thread informed. Thanks Siobi....Dan
> 
> Ignored

Thanks qz10cq!!  
  
Can I call you qz? lol  
  
A more important question is if you did some backtests and found your above settings to be profitable? In principle of course you are correct anyway, just wondered about backtesting since none of my computers are up to the task apparently. For some reason - I guess because they are all loaded up with anything and everything - optimized backtests work painfully slowly, at best.  
(Not at all for v104)  
  
I want to go live with a relatively larger acct. but I can't even get any trades at all on my $100 live fxdd acct. I think it goes without saying that I'll need optimized settings with profitability before I feel comfortable though.   
(Had 18 and 0 on fxdd demo, and then went live and no trades for me and bad trades for everyone else. Just coincidence???!!!)![](https://resources.faireconomy.media/images/emojis/64/1f644.png?v=15.1) I sure hope so, otherwise the pitchforks will be coming out of the barn!![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)  
  
Thanks for your contributions!![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#273](/thread/post/2620688#post2620688 "Post Permalink")

  * Edited 1:54am  Mar 23, 2009 1:16am | Edited 1:54am 

  * [ qz10cq](qz10cq)

  * | Joined Dec 2006  | Status: Trader | [303 Posts](/search?do=process&provider=Member&searchuser=29720)

> [Quoting Dan Johnston](/thread/post/2620600#post2620600 "View Quoted Post")
> 
> Disliked
> 
> Thanks qz10cq!!  
>    
>  Can I call you qz? lol  
>    
>  A more important question is if you did some backtests and found your above settings to be profitable? In principle of course you are correct anyway, just wondered about backtesting since none of my computers are up to the task apparently. For some reason - I guess because they are all loaded up with anything and everything - optimized backtests work painfully slowly, at best.  
>  (Not at all for v104)  
>    
>  I want to go live with a relatively larger acct. but I can't even get any trades at all on my $100 live...
> 
> Ignored

Didn't back test this Dan, but up until last week was using the 110/150/25 settings with a steady 250/400 hundred pips weekly, changed over to the 20/50 settings and lost 300. The markets were crazy last week so not a real good test for the new settings, I'm trading 10 pairs which of course this ea is set for only eur/usd. I feel better with a 100 pip sl so the market can breath a little more, and I've always thought to let ur profits run and cut ur losses short so this week it's back to the 100/150/25 settings. Trying to get those 10 pairs I'm trading down to 4 and will go live with those if ever thing continues to run right.   
  
Siobi is a very smart, Conservative trader and has the right approach to getting 20 pips daily as his goal. 20 pips daily with the right mm puts you into big bucks within a year. The only trouble I have with his approach is that 1 loss equals 5 wins. It's all a question of balance. I test 5 different ea's weekly and really like this EA. Of the 5 I test only 2 survived with profit last week they are a semi-martingale (big profits) and fabturbo (small profits but profit). Will keep the thread posted. Thanks Siobi....Dan  
  
Dan, when you figure out whats up with your live account please infor the thread and yes you can call me "qz" in fact you can call me anything except "late for dinner".......Dan 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#274](/thread/post/2620920#post2620920 "Post Permalink")

  * Mar 23, 2009 5:23am  Mar 23, 2009 5:23am 

  * [ paradoxical](paradoxical)

  * | Joined Nov 2007  | Status: Trader | [1,186 Posts](/search?do=process&provider=Member&searchuser=54706)

QZ, I don't like the 1 to 5 ratio, either, and asked if anyone had done a backtest on a 50 Take profit. Initially, this was a scalping EA (I think) and generally you don't scalp for a hundred pips. I'd like a 1 to 1 ratio, or a to 2 or 2 and a half myself. Of course, as long as you win 6 times to one with this EA, you're ahead of the game, but 6-1 aint easy, at least consistently.

> [Quoting qz10cq](/thread/post/2620688#post2620688 "View Quoted Post")
> 
> Disliked
> 
> Didn't back test this Dan, but up until last week was using the 110/150/25 settings with a steady 250/400 hundred pips weekly, changed over to the 20/50 settings and lost 300. The markets were crazy last week so not a real good test for the new settings, I'm trading 10 pairs which of course this ea is set for only eur/usd. I feel better with a 100 pip sl so the market can breath a little more, and I've always thought to let ur profits run and cut ur losses short so this week it's back to the 100/150/25 settings. Trying to get those 10 pairs I'm...
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#275](/thread/post/2620973#post2620973 "Post Permalink")

  * Mar 23, 2009 6:08am  Mar 23, 2009 6:08am 

  * [ qz10cq](qz10cq)

  * | Joined Dec 2006  | Status: Trader | [303 Posts](/search?do=process&provider=Member&searchuser=29720)

> [Quoting paradoxical](/thread/post/2620920#post2620920 "View Quoted Post")
> 
> Disliked
> 
> QZ, I don't like the 1 to 5 ratio, either, and asked if anyone had done a backtest on a 50 Take profit. Initially, this was a scalping EA (I think) and generally you don't scalp for a hundred pips. I'd like a 1 to 1 ratio, or a to 2 or 2 and a half myself. Of course, as long as you win 6 times to one with this EA, you're ahead of the game, but 6-1 aint easy, at least consistently.
> 
> Ignored

Yeah Par that 1 to 5 bothers me to. Been thinking about a 20sl and 20tp just to see if the indicators Siobi uses will kick us towards a winning % (give us a steady 60% win 40% loss and we are all on easy street). Cheers bud......Dan 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#276](/thread/post/2620998#post2620998 "Post Permalink")

  * Mar 23, 2009 6:32am  Mar 23, 2009 6:32am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar95566_5.gif) stifland](stifland)

  * | Joined Mar 2009  | Status: Trader | [304 Posts](/search?do=process&provider=Member&searchuser=95566)

buy 1.3632 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#277](/thread/post/2621073#post2621073 "Post Permalink")

  * Mar 23, 2009 7:26am  Mar 23, 2009 7:26am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar95566_5.gif) stifland](stifland)

  * | Joined Mar 2009  | Status: Trader | [304 Posts](/search?do=process&provider=Member&searchuser=95566)

+20. ea off. ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#278](/thread/post/2621597#post2621597 "Post Permalink")

  * Mar 23, 2009 2:12pm  Mar 23, 2009 2:12pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83889_5.gif) siobi](siobi)

  * | Joined Oct 2008  | Status: Trader | [717 Posts](/search?do=process&provider=Member&searchuser=83889)

grab +9pip from R9.  
  
buy at 1.3667, exited at 1.3677. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#279](/thread/post/2622023#post2622023 "Post Permalink")

  * Mar 23, 2009 6:44pm  Mar 23, 2009 6:44pm 

  * [ Orenn](orenn)

  * | Joined Mar 2009  | Status: Trader | [11 Posts](/search?do=process&provider=Member&searchuser=96427)

Siobi, All,  
  
Did some backtests. Results attached.  
I run the tests on the last 3 week. Since I'm running this EA in demo for the last 2 weeks logging all activity I was able to tell that the backtests are pretty close to what hannped in real time.  
I checked different Stop loss, Take profit and Trailing Stops.  
I even checked what happens on 15M time frame and how r7 is doing.  
  
Each can draw his own conclusion, since we might have different trading styles (like different risk taking) the conclusions may differ. Parhaps I'll write my own later  
  
I hope this is helpful  
  
Oren 

Attached File(s)

![File Type: xls](https://assets.faireconomy.media/images/attach/xls.gif) [Siobi EA backtests.xls](/attachment/file/222339?d=1237801182) 22 KB | 305 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#280](/thread/post/2622277#post2622277 "Post Permalink")

  * Mar 23, 2009 8:58pm  Mar 23, 2009 8:58pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83889_5.gif) siobi](siobi)

  * | Joined Oct 2008  | Status: Trader | [717 Posts](/search?do=process&provider=Member&searchuser=83889)

hi all,  
I had carefully gone through R8 and found that the main problem for the last losing trade of 100 pip is due to the redraw of Slope Direction Line!!!  
  
in R9 dated 23th version, I'll take care of it and hope this will not happend again.  
  
tentative release date will be on 29-Mac-2009.  
  
Regards,  
siobi 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * FX_30M Bouncing System
  *   * [ **Reply to Thread** ](/thread/157406-fx30m-bouncing-system/reply#reply)

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

[The Bouncing Pip](/thread/88277-the-bouncing-pip "Hi everyone. 
 
I present to you a system called &quot;The Bouncing Pip&quot; 
 
This is a system that was originally developed by BigBear, so full...") 26 replies

[Price bouncing off of sma](/thread/228922-price-bouncing-off-of-sma "What is the logic behind a price bouncing off an SMA? 
 
For example if a price bounces of a 35 day sma, i should short it if bounces of...") 2 replies

[Developing a correlated bouncing system](/thread/158016-developing-a-correlated-bouncing-system "The above indicator is a simple ma indicator with the weekly ma set to 40. 
 
I like most of my bouncing signals to be in the direction of...") 9 replies

[bouncing candle indicator](/thread/105826-bouncing-candle-indicator "I once had an indicator that would  send  off an alert whenever a candle touched back on its  moving average.  Lost it somehow, but I do...") 0 replies

[Price bouncing off support or resistance,your thoughts](/thread/30984-price-bouncing-off-support-or-resistanceyour-thoughts "I would like to start a discussuion about price movement at support/resistance, Fib and pivot levels.  
  
Time and again I see the price...") 11 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/157406-fx30m-bouncing-system/reply#reply)
  * Subscribe
  * [72](javascript:void\(0\);)

Attachments: FX_30M Bouncing System

Tags: FX_30M Bouncing System

#  [](/thread/157406-fx30m-bouncing-system)FX_30M Bouncing System 

  * 

  * [#281](/thread/post/2622909#post2622909 "Post Permalink")

  * Edited 1:36am  Mar 24, 2009 1:21am | Edited 1:36am 

  * [ Dan Johnston](dan*johnston)

  * | Joined May 2008  | Status: Trader | [354 Posts](/search?do=process&provider=Member&searchuser=69420)

I predict we'll be "**__state of the art__** " very soon!  
  
Hope it's before I go under financially! ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)  
  
PS:When fapturbo wins, it wins fairly small. When it loses, although less often, it loses _BIG_! ...At least lately and with my default "scalp" only settings. Too scary for live, at least for me.  
  
Hope they keep working on **it** and not so much the sales part of it. It's always nice to have different avenues to profitability!  
  
...But like I said, I think good things are in store for **us, here!!!**  
  
PPS: Still no trades on my fxdd live acct. so went down to 1 cent per pip. If it didn't work then on live fxdd, don't think it will now. Must be some kind of tick data filter or something, or maybe not... . So pessimistic I am sometimes! LOL 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#282](/thread/post/2622973#post2622973 "Post Permalink")

  * Mar 24, 2009 1:49am  Mar 24, 2009 1:49am 

  * [ nickmead](nickmead)

  * | Commercial User  | Joined Feb 2008 | [66 Posts](/search?do=process&provider=Member&searchuser=61524)

> [Quoting siobi](/thread/post/2622277#post2622277 "View Quoted Post")
> 
> Disliked
> 
> hi all,  
>  I had carefully gone through R8 and found that the main problem for the last losing trade of 100 pip is due to the redraw of Slope Direction Line!!!  
>    
>  in R9 dated 23th version, I'll take care of it and hope this will not happend again.  
>    
>  tentative release date will be on 29-Mac-2009.  
>    
>  Regards,  
>  siobi
> 
> Ignored

Thx Siobi I'll look foward to it. 15 pips last night thank you. I currently have the EA set to 15sl and 15tp. So far 5 winners and one loser  
  
best wishes   
Nick 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#283](/thread/post/2622975#post2622975 "Post Permalink")

  * Mar 24, 2009 1:49am  Mar 24, 2009 1:49am 

  * [ michaelhryu](michaelhryu)

  * | Joined Oct 2008  | Status: Trader | [142 Posts](/search?do=process&provider=Member&searchuser=81864)

> [Quoting Orenn](/thread/post/2622023#post2622023 "View Quoted Post")
> 
> Disliked
> 
> Siobi, All,  
>  Did some backtests. Results attached.  
>  I run the tests on the last 3 week. Since I'm running this EA in demo for the last 2 weeks logging all activity I was able to tell that the backtests are pretty close to what hannped in real time.  
>  I checked different Stop loss, Take profit and Trailing Stops.  
>  I even checked what happens on 15M time frame and how r7 is doing.  
>  Oren
> 
> Ignored

I am very much interested in your results. Is your backtest result from trading Japanese Session only, or trading 24/5? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#284](/thread/post/2623238#post2623238 "Post Permalink")

  * Mar 24, 2009 4:17am  Mar 24, 2009 4:17am 

  * [ qz10cq](qz10cq)

  * | Joined Dec 2006  | Status: Trader | [303 Posts](/search?do=process&provider=Member&searchuser=29720)

> [Quoting nickmead](/thread/post/2622973#post2622973 "View Quoted Post")
> 
> Disliked
> 
> Thx Siobi I'll look foward to it. 15 pips last night thank you. I currently have the EA set to 15sl and 15tp. So far 5 winners and one loser  
>    
>  best wishes   
>  Nick
> 
> Ignored

Nick I have mine set to 20tp/20sl/10ts. Playing 5 pairs 24/5, my 3000 demo account is down 60 pips with 19 trades taken since last night. Do you trade 24/5? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#285](/thread/post/2623287#post2623287 "Post Permalink")

  * Mar 24, 2009 4:40am  Mar 24, 2009 4:40am 

  * [ paradoxical](paradoxical)

  * | Joined Nov 2007  | Status: Trader | [1,186 Posts](/search?do=process&provider=Member&searchuser=54706)

Two trades on my live IBFX account last night for one pip each. Mde 20 cents! Will look into changing the TP and SL settings after reviewing siobi's spreadsheet settings. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#286](/thread/post/2623314#post2623314 "Post Permalink")

  * Mar 24, 2009 4:53am  Mar 24, 2009 4:53am 

  * [ Orenn](orenn)

  * | Joined Mar 2009  | Status: Trader | [11 Posts](/search?do=process&provider=Member&searchuser=96427)

michaelhryu - The becktests are 24/5  
  
qz10cq - Which pairs are to playing?  
I am also running this EA on several pairs for a few days now I chose pairs I usally work on my manual trading (and use 25sl 100tp 20ts). Maybe its too soon to tell but my current impresions are:  
  
None make the winning precentage of the EU  
USDJPY - more winners than lossers  
GBPUSD - 50/50 but winners run long  
EURGBP - very few trades mostly losers  
EURJPY - more lossers than winners (looks like the EA chooses the worse timing for entering this pair)  
  
Anything sounds familiar? let me know  
  
Oren 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#287](/thread/post/2623348#post2623348 "Post Permalink")

  * Mar 24, 2009 5:15am  Mar 24, 2009 5:15am 

  * [ Orenn](orenn)

  * | Joined Mar 2009  | Status: Trader | [11 Posts](/search?do=process&provider=Member&searchuser=96427)

Just writing the last post the pairs decided to prove me wrong:  
USDJPY took a loosing trade and EURJPY is currenty +40pips and going.  
Not going to mess up with these guys again..,  
  
Oren 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#288](/thread/post/2623419#post2623419 "Post Permalink")

  * Mar 24, 2009 5:56am  Mar 24, 2009 5:56am 

  * [ paradoxical](paradoxical)

  * | Joined Nov 2007  | Status: Trader | [1,186 Posts](/search?do=process&provider=Member&searchuser=54706)

Dan, maybe you need to switch to IBFX!! LOL  
I'm on my way to financial freedom. Had two wins in a row at 1 pip each for a profit of .20  
Hurry on over.

> [Quoting Dan Johnston](/thread/post/2622909#post2622909 "View Quoted Post")
> 
> Disliked
> 
> I predict we'll be "**__state of the art__** " very soon!  
>    
>  Hope it's before I go under financially! ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)  
>    
>  PS:When fapturbo wins, it wins fairly small. When it loses, although less often, it loses _BIG_! ...At least lately and with my default "scalp" only settings. Too scary for live, at least for me.  
>    
>  Hope they keep working on **it** and not so much the sales part of it. It's always nice to have different avenues to profitability!  
>    
>  ...But like I said, I think good things are in store for **us, here!!!**  
>    
>  PPS: Still...
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#289](/thread/post/2623468#post2623468 "Post Permalink")

  * Mar 24, 2009 6:35am  Mar 24, 2009 6:35am 

  * [ Dan Johnston](dan*johnston)

  * | Joined May 2008  | Status: Trader | [354 Posts](/search?do=process&provider=Member&searchuser=69420)

> [Quoting paradoxical](/thread/post/2623419#post2623419 "View Quoted Post")
> 
> Disliked
> 
> Dan, maybe you need to switch to IBFX!! LOL  
>  I'm on my way to financial freedom. Had two wins in a row at 1 pip each for a profit of .20  
>  Hurry on over.
> 
> Ignored

LOL. I have an acct. with ibfx also. Just not trading live with them at the moment any more. Will prob. trade both accounts at some point. At least I hope.  
  
We shall see....![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#290](/thread/post/2623519#post2623519 "Post Permalink")

  * Mar 24, 2009 7:18am  Mar 24, 2009 7:18am 

  * [ paradoxical](paradoxical)

  * | Joined Nov 2007  | Status: Trader | [1,186 Posts](/search?do=process&provider=Member&searchuser=54706)

siobi, in looking at your spread sheet, looks like a TP and SL of 100 is the best setting on both the 15 minute and 30 minute time frames, with a 20 trail stop. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#291](/thread/post/2623613#post2623613 "Post Permalink")

  * Mar 24, 2009 8:40am  Mar 24, 2009 8:40am 

  * [ nickmead](nickmead)

  * | Commercial User  | Joined Feb 2008 | [66 Posts](/search?do=process&provider=Member&searchuser=61524)

> [Quoting qz10cq](/thread/post/2623238#post2623238 "View Quoted Post")
> 
> Disliked
> 
> Nick I have mine set to 20tp/20sl/10ts. Playing 5 pairs 24/5, my 3000 demo account is down 60 pips with 19 trades taken since last night. Do you trade 24/5?
> 
> Ignored

I am currently just trading asian market on EU only  
  
Nick 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#292](/thread/post/2623824#post2623824 "Post Permalink")

  * Mar 24, 2009 10:38am  Mar 24, 2009 10:38am 

  * [ qz10cq](qz10cq)

  * | Joined Dec 2006  | Status: Trader | [303 Posts](/search?do=process&provider=Member&searchuser=29720)

> [Quoting Orenn](/thread/post/2623314#post2623314 "View Quoted Post")
> 
> Disliked
> 
> michaelhryu - The becktests are 24/5  
>    
>  qz10cq - Which pairs are to playing?  
>  I am also running this EA on several pairs for a few days now I chose pairs I usally work on my manual trading (and use 25sl 100tp 20ts). Maybe its too soon to tell but my current impresions are:  
>    
>  None make the winning precentage of the EU  
>  USDJPY - more winners than lossers  
>  GBPUSD - 50/50 but winners run long  
>  EURGBP - very few trades mostly losers  
>  EURJPY - more lossers than winners (looks like the EA chooses the worse timing for entering this pair)  
>    
>  Anything sounds familiar?...
> 
> Ignored

Orenn, I'm trading all pairs that have 10 or less spread. Testing a 20tp/20sl/and a 10 trailing stop. I'm down 120 pips since last night's open. I'll give another day or so with these settings and then keep testing till something works. Actually listening to Siobi is what works here. One pair only (eur/usd) and the european session only. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#293](/thread/post/2624313#post2624313 "Post Permalink")

  * Mar 24, 2009 4:17pm  Mar 24, 2009 4:17pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83889_5.gif) siobi](siobi)

  * | Joined Oct 2008  | Status: Trader | [717 Posts](/search?do=process&provider=Member&searchuser=83889)

hi guys....  
  
if market is in trend... this EA can grab the 20 pip easily... but if not... it tooks around 4 BARs to take the profit...  
  
any longer bar always resulted bad trade...  
  
I think the SL 100 pip is abit off...  
  
the draw down of this EA is about 20~30 pip after the trade open.  
  
I'm thinking to put in step pip to grab the pulback/retracement once the DD happend for about 30 pips.  
  
eg:   
SELL at 1.2345, SL = 1.2445, TP 1.2325.  
  
price go high at 1.2375, then I check the higher timeframe trend, if it is still DOWN trend in action, then I add in another   
SELL at 1.2375, SL 1.2445, TP 1.2345   
  
since R9 had taking good care of false signal as of today, I'm thinking of addin this step in feature to further hunting more pips during the retracement/pullback.  
  
this concept might be only working for EUR/USD pair as it nature is always retrace and pullback within 200~300 pip range in a day.  
  
PS: dont play too much on the sl and TP, due to market condition, it doesnt help much.  
  
TP of 20 pip is reasonable for 30M   
SL of 100 pip is NOT reasonable for 30M, but if I can figure out the best entry time, I dont need the step pip...  
  
perhaps....  
  
I can !!!  
  
hahah while writting this, I'm thinking of another idea!!!  
  
good .... later will share it out!!! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#294](/thread/post/2624426#post2624426 "Post Permalink")

  * Mar 24, 2009 5:26pm  Mar 24, 2009 5:26pm 

  * [ Bobcat2](bobcat2)

  * | Joined Aug 2006  | Status: Trader | [1,024 Posts](/search?do=process&provider=Member&searchuser=16828)

Hi Siobi,  
  
Many thanks for sharing your trading system. I just found this thread about 30 minutes ago. I loaded the template, indicators and EA about 10 minutes ago. I turned on the EA, and the system has already made me 25 pips profit!  
  
At this rate, I'll be rich by morning! LOL  
  
In one of your posts, you stated that this system works in any time frame other than during news events. Should I continue to run the EA, even though I have already made more than 20 pips for the day? Or can I continue to make more trades throughout the day?  
  
Best regards,  
Bob in Wisconsin 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#295](/thread/post/2624445#post2624445 "Post Permalink")

  * Mar 24, 2009 5:40pm  Mar 24, 2009 5:40pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83889_5.gif) siobi](siobi)

  * | Joined Oct 2008  | Status: Trader | [717 Posts](/search?do=process&provider=Member&searchuser=83889)

daily target was set to 20 pip...  
this is my way of trading...  
  
I had a big loss.... last round... -100 pip...  
still feel the pain...  
  
anyway, I'll stick to my trading plan as 20 pip per day. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#296](/thread/post/2624539#post2624539 "Post Permalink")

  * Mar 24, 2009 6:41pm  Mar 24, 2009 6:41pm 

  * [ qz10cq](qz10cq)

  * | Joined Dec 2006  | Status: Trader | [303 Posts](/search?do=process&provider=Member&searchuser=29720)

> [Quoting siobi](/thread/post/2624445#post2624445 "View Quoted Post")
> 
> Disliked
> 
> daily target was set to 20 pip...  
>  this is my way of trading...  
>    
>  I had a big loss.... last round... -100 pip...  
>  still feel the pain...  
>    
>  anyway, I'll stick to my trading plan as 20 pip per day.
> 
> Ignored

Looking forward to testing your V9, Siobi are you averaging 20 pips daily? Do you only trade one session daily? One loss equals 5 wins. V9 sounds safer than ealier versions. Are you only trading eur/usd? I really like this ea and it sounds like it's getting better.....Thanks 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#297](/thread/post/2624593#post2624593 "Post Permalink")

  * Mar 24, 2009 7:12pm  Mar 24, 2009 7:12pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83889_5.gif) siobi](siobi)

  * | Joined Oct 2008  | Status: Trader | [717 Posts](/search?do=process&provider=Member&searchuser=83889)

hihi,  
  
I'm able to make 20 pip perday...  
  
like my previous day, I was able to grab 9 pip and that is!!!  
  
I only trade EUR/USD (because it is always hving huge retrace /pullback)  
  
I like EU because less spread  
  
I like to trade for all time zone today except News date..  
  
R9 later version Mac 24 was completed today with below's setting:  
  
1) PSARFac = 60  
2) SL = 50 pip  
3) TP = 30 pip  
4) TS = 15 pip  
  
resulted very well...  
  
hi dan in reading, the one I send to you is Mac 23,  
later I'll send this Mac 24 to you....  
  
Release date and backtest result will be posted very soon next week sunday...  
  
Good luck guys and happy pipping!!! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#298](/thread/post/2624995#post2624995 "Post Permalink")

  * Mar 24, 2009 10:46pm  Mar 24, 2009 10:46pm 

  * [ paradoxical](paradoxical)

  * | Joined Nov 2007  | Status: Trader | [1,186 Posts](/search?do=process&provider=Member&searchuser=54706)

A 16 PIP win on the EUR/USD last night when it hit the trail stop. Also a 9 PIP win on the GBP. Both live trades. The GBP/USD works very well so far. As someone reported in a previous post, the other pairs don't work so well. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#299](/thread/post/2625776#post2625776 "Post Permalink")

  * Mar 25, 2009 5:17am  Mar 25, 2009 5:17am 

  * [ Dan Johnston](dan*johnston)

  * | Joined May 2008  | Status: Trader | [354 Posts](/search?do=process&provider=Member&searchuser=69420)

> [Quoting siobi](/thread/post/2624593#post2624593 "View Quoted Post")
> 
> Disliked
> 
> hihi,  
>    
>  I'm able to make 20 pip perday...  
>    
>  like my previous day, I was able to grab 9 pip and that is!!!  
>    
>  I only trade EUR/USD (because it is always hving huge retrace /pullback)  
>    
>  I like EU because less spread  
>    
>  I like to trade for all time zone today except News date..  
>    
>  R9 later version Mac 24 was completed today with below's setting:  
>    
>  1) PSARFac = 60  
>  2) SL = 50 pip  
>  3) TP = 30 pip  
>  4) TS = 15 pip  
>    
>  resulted very well...  
>    
>  hi dan in reading, the one I send to you is Mac 23,  
>  later I'll send this Mac 24 to you....  
>    
>  Release date and backtest result...
> 
> Ignored

Thank you Siobi, but I may already have latest version. Not sure.  
  
You can send latest anyway and I'll just replace the one you see below. (No trades on r9 yet - maybe because I have Feb. 22 r7 running on same account?)  
  
(Last trades you see are r7 trades)  
  
Thanks again! 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: no trades 3 24.gif
Size: 49 KB](/attachment/image/223189/thumbnail?d=1365566016)](/attachment/image/223189?d=1237925818)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#300](/thread/post/2626015#post2626015 "Post Permalink")

  * Mar 25, 2009 7:44am  Mar 25, 2009 7:44am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83889_5.gif) siobi](siobi)

  * | Joined Oct 2008  | Status: Trader | [717 Posts](/search?do=process&provider=Member&searchuser=83889)

hi dan,  
please take a close look at R9 on the date... the latest one is dated Mac24 which I send couple hours ago...  
  
YES... it cannot run together with other version of FX_bouncing as I'm checking it on the magic number....   
  
anyway... R9 no result for 24-Mac yet.... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * FX_30M Bouncing System
  *   * [ **Reply to Thread** ](/thread/157406-fx30m-bouncing-system/reply#reply)

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

[The Bouncing Pip](/thread/88277-the-bouncing-pip "Hi everyone. 
 
I present to you a system called &quot;The Bouncing Pip&quot; 
 
This is a system that was originally developed by BigBear, so full...") 26 replies

[Price bouncing off of sma](/thread/228922-price-bouncing-off-of-sma "What is the logic behind a price bouncing off an SMA? 
 
For example if a price bounces of a 35 day sma, i should short it if bounces of...") 2 replies

[Developing a correlated bouncing system](/thread/158016-developing-a-correlated-bouncing-system "The above indicator is a simple ma indicator with the weekly ma set to 40. 
 
I like most of my bouncing signals to be in the direction of...") 9 replies

[bouncing candle indicator](/thread/105826-bouncing-candle-indicator "I once had an indicator that would  send  off an alert whenever a candle touched back on its  moving average.  Lost it somehow, but I do...") 0 replies

[Price bouncing off support or resistance,your thoughts](/thread/30984-price-bouncing-off-support-or-resistanceyour-thoughts "I would like to start a discussuion about price movement at support/resistance, Fib and pivot levels.  
  
Time and again I see the price...") 11 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/157406-fx30m-bouncing-system/reply#reply)
  * Subscribe
  * [72](javascript:void\(0\);)

Attachments: FX_30M Bouncing System

Tags: FX_30M Bouncing System

#  [](/thread/157406-fx30m-bouncing-system)FX_30M Bouncing System 

  * 

  * [#301](/thread/post/2627344#post2627344 "Post Permalink")

  * Mar 25, 2009 9:21pm  Mar 25, 2009 9:21pm 

  * [ paradoxical](paradoxical)

  * | Joined Nov 2007  | Status: Trader | [1,186 Posts](/search?do=process&provider=Member&searchuser=54706)

Two more wins last night on the EUR/USD for 8 and 23 PIPS on my live IBFX account at .10 a trade. I changed the setting to 100 TP and 100 SL and with a 20 trail stop. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#302](/thread/post/2627446#post2627446 "Post Permalink")

  * Mar 25, 2009 10:14pm  Mar 25, 2009 10:14pm 

  * [ qz10cq](qz10cq)

  * | Joined Dec 2006  | Status: Trader | [303 Posts](/search?do=process&provider=Member&searchuser=29720)

> [Quoting paradoxical](/thread/post/2627344#post2627344 "View Quoted Post")
> 
> Disliked
> 
> Two more wins last night on the EUR/USD for 8 and 23 PIPS on my live IBFX account at .10 a trade. I changed the setting to 100 TP and 100 SL and with a 20 trail stop.
> 
> Ignored

Yeah me to P, went back to the original 100sl, 150tp and 15 ts. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#303](/thread/post/2627454#post2627454 "Post Permalink")

  * Mar 25, 2009 10:19pm  Mar 25, 2009 10:19pm 

  * [ uafx](uafx)

  * | Joined Oct 2008  | Status: Trader | [224 Posts](/search?do=process&provider=Member&searchuser=82896)

I am trying the R8 version of the EA:  
  
last night there were 2 trades on my IBFX demo account, but no trade on the Alpari real account. What could be the problem?  
  
The differences were:  
\- IBFX: 4 digits, Alpari: 5 digits price  
\- IBFX demo: 50 SL, 20 TP, 10 TS  
\- Alpari real: 100 SL, 150 TP, 25 TS  
\- Tokyo hours on both  
  
On both platforms there were the "smiling face" for the EA, so trading wasn't disabled...  
  
Anyone else has the same experience, or am I missing something? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#304](/thread/post/2627487#post2627487 "Post Permalink")

  * Mar 25, 2009 10:33pm  Mar 25, 2009 10:33pm 

  * [ PotPlant](potplant)

  * | Joined Mar 2009  | Status: Trader | [4 Posts](/search?do=process&provider=Member&searchuser=97875)

Yep ran this on 5 digit Alpari for 3 days and didn't get a single trade. Have to have another look 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#305](/thread/post/2627495#post2627495 "Post Permalink")

  * Mar 25, 2009 10:36pm  Mar 25, 2009 10:36pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar95566_5.gif) stifland](stifland)

  * | Joined Mar 2009  | Status: Trader | [304 Posts](/search?do=process&provider=Member&searchuser=95566)

I have set to original siobi settings which close trade at 11:00 after Asian. If not, it would have been a winner. Sometimes, however, this would probably save a bigger loser so not sure on this point. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: lastnight.gif
Size: 22 KB](/attachment/image/223587/thumbnail?d=1365566095)](/attachment/image/223587?d=1237988181)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#306](/thread/post/2627675#post2627675 "Post Permalink")

  * Mar 25, 2009 11:13pm  Mar 25, 2009 11:13pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83889_5.gif) siobi](siobi)

  * | Joined Oct 2008  | Status: Trader | [717 Posts](/search?do=process&provider=Member&searchuser=83889)

> [Quoting uafx](/thread/post/2627454#post2627454 "View Quoted Post")
> 
> Disliked
> 
> I am trying the R8 version of the EA:  
>    
>  last night there were 2 trades on my IBFX demo account, but no trade on the Alpari real account. What could be the problem?  
>    
>  The differences were:  
>  \- IBFX: 4 digits, Alpari: 5 digits price  
>  \- IBFX demo: 50 SL, 20 TP, 10 TS  
>  \- Alpari real: 100 SL, 150 TP, 25 TS  
>  \- Tokyo hours on both  
>    
>  On both platforms there were the "smiling face" for the EA, so trading wasn't disabled...  
>    
>  Anyone else has the same experience, or am I missing something?
> 
> Ignored

  
ALpari SL and TP and TS will be auto set by the EA...so... leave it to default and change only Num_of_digit to true 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#307](/thread/post/2627824#post2627824 "Post Permalink")

  * Mar 25, 2009 11:36pm  Mar 25, 2009 11:36pm 

  * [ uafx](uafx)

  * | Joined Oct 2008  | Status: Trader | [224 Posts](/search?do=process&provider=Member&searchuser=82896)

> [Quoting siobi](/thread/post/2627675#post2627675 "View Quoted Post")
> 
> Disliked
> 
> ALpari SL and TP and TS will be auto set by the EA...so... leave it to default and change only Num_of_digit to true
> 
> Ignored

OK, but I wanted to use the 100/150/25 version of the trading. Where else can I set this? Or is version R8 not capable to trade this way?  
  
And num_of_digit was set to true...  
  
And no traces in the experts log, that the EA tried anything to do... (I expect some error message if something wrong in the settings)... so it seemed, that the EA didn't do anything whole night... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#308](/thread/post/2628672#post2628672 "Post Permalink")

  * Edited 6:05am  Mar 26, 2009 4:53am | Edited 6:05am 

  * [ Elovv](elovv)

  * | Joined Aug 2007  | Status: Trader | [747 Posts](/search?do=process&provider=Member&searchuser=46754)

Thankyou for dealing your system. A question about start and end time. 0 and 10 is brooker time? So if I use ODL or IBFX and set start 0, end 10 it start take possible trades at 0 GMT and stops 10 GMT (GMT is the same time as ODL and IBFX)  
  
You trade all time but not news. What do you set end and close before big news? And when do you start trade again?  
  
Is it possible to turn close off so EA trades without closing any trades?  
  
I´m testing the system on ODL from now 19.50 GMT, default settings. I will test trading all time without news. End 10 and close 12 (GMT) because of 12:30 USD  
Unemployment Claims   
  
I let you know my result.  
  
Elovv 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#309](/thread/post/2629885#post2629885 "Post Permalink")

  * Mar 26, 2009 5:20pm  Mar 26, 2009 5:20pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83889_5.gif) siobi](siobi)

  * | Joined Oct 2008  | Status: Trader | [717 Posts](/search?do=process&provider=Member&searchuser=83889)

> [Quoting Elovv](/thread/post/2628672#post2628672 "View Quoted Post")
> 
> Disliked
> 
> Thankyou for dealing your system. A question about start and end time....
> 
> Ignored

not sure u r good in manipulating EA...  
  
this EA can be tunr on and off, it will not close the trade because it does not have any exit strategy.  
  
as for trading time setting. it is solely on your broker time.  
since it can be trade for all time zone, so u can just set it to 0 ~ 24.  
  
tunr off the EA during news hour and the EA will not take any trade!!! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#310](/thread/post/2630380#post2630380 "Post Permalink")

  * Mar 26, 2009 10:32pm  Mar 26, 2009 10:32pm 

  * [ Elovv](elovv)

  * | Joined Aug 2007  | Status: Trader | [747 Posts](/search?do=process&provider=Member&searchuser=46754)

> [Quoting siobi](/thread/post/2629885#post2629885 "View Quoted Post")
> 
> Disliked
> 
> not sure u r good in manipulating EA...  
>    
>  this EA can be tunr on and off, it will not close the trade because it does not have any exit strategy.  
>    
>  as for trading time setting. it is solely on your broker time.  
>  since it can be trade for all time zone, so u can just set it to 0 ~ 24.  
>    
>  tunr off the EA during news hour and the EA will not take any trade!!!
> 
> Ignored

From your first post CloseHour= 11(set to 30 if you do not want EA to close the trade)  
Doesn´t that mean the EA close the trade 11.00 if CloseHour=11? Ore do I missunderstand?  
No trades so far on my ODL demo  
  
Elovv 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#311](/thread/post/2630844#post2630844 "Post Permalink")

  * Mar 27, 2009 1:44am  Mar 27, 2009 1:44am 

  * [ paradoxical](paradoxical)

  * | Joined Nov 2007  | Status: Trader | [1,186 Posts](/search?do=process&provider=Member&searchuser=54706)

A 10 pip win on a long EUR/USD trade at 12:00 IBFX time. The 20 pip trail stop saved what would be a loss at this time of about 70 pips.  
Very impressed with this EA, SIOBI.   
I also have it running on a FXDD demo, which took a short trade awhile ago for plus 20 that my IBFX account didn't. Oh well, can't win em all. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#312](/thread/post/2630989#post2630989 "Post Permalink")

  * Edited 5:23am  Mar 27, 2009 3:06am | Edited 5:23am 

  * [ Elovv](elovv)

  * | Joined Aug 2007  | Status: Trader | [747 Posts](/search?do=process&provider=Member&searchuser=46754)

> [Quoting paradoxical](/thread/post/2630844#post2630844 "View Quoted Post")
> 
> Disliked
> 
> A 10 pip win on a long EUR/USD trade at 12:00 IBFX time. The 20 pip trail stop saved what would be a loss at this time of about 70 pips.  
>  Very impressed with this EA, SIOBI.   
>  I also have it running on a FXDD demo, which took a short trade awhile ago for plus 20 that my IBFX account didn't. Oh well, can't win em all.
> 
> Ignored

Can anybody explain under wich sircumstances the EA takes a trade? I haven´t any trades since yesterday 19.50 GMT (the same as IBFX time) but my EA whas of today at 12.00 because of news 12.30.  
If we know the sircumstances for a buy/sell with could better understand the EA.  
  
From today 20.00 GMT I have it on ODL, IBFX and FXDD, all demo. But if it works as promise in the tread I will test it with my live acounts  
  
Regards  
Elovv 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#313](/thread/post/2631734#post2631734 "Post Permalink")

  * Mar 27, 2009 11:28am  Mar 27, 2009 11:28am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83889_5.gif) siobi](siobi)

  * | Joined Oct 2008  | Status: Trader | [717 Posts](/search?do=process&provider=Member&searchuser=83889)

hi all,  
as I do not run on R8 at the moment, I do not know whether it takes any trade or not...  
  
I cant answer you directly.  
  
I can only trade R9 in my live acct now.... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#314](/thread/post/2631759#post2631759 "Post Permalink")

  * Mar 27, 2009 11:44am  Mar 27, 2009 11:44am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar95566_5.gif) stifland](stifland)

  * | Joined Mar 2009  | Status: Trader | [304 Posts](/search?do=process&provider=Member&searchuser=95566)

i can say I am long 1.355 live fxdd at 03:30 bar. it seems it does vary with data feed 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#315](/thread/post/2631785#post2631785 "Post Permalink")

  * Mar 27, 2009 12:00pm  Mar 27, 2009 12:00pm 

  * [ Bobcat2](bobcat2)

  * | Joined Aug 2006  | Status: Trader | [1,024 Posts](/search?do=process&provider=Member&searchuser=16828)

> [Quoting stifland](/thread/post/2631759#post2631759 "View Quoted Post")
> 
> Disliked
> 
> i can say I am long 1.355 live fxdd at 03:30 bar. it seems it does vary with data feed
> 
> Ignored

I have the same Buy entry, as well.,,currently up 13 pips 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#316](/thread/post/2631788#post2631788 "Post Permalink")

  * Mar 27, 2009 12:01pm  Mar 27, 2009 12:01pm 

  * [ Elovv](elovv)

  * | Joined Aug 2007  | Status: Trader | [747 Posts](/search?do=process&provider=Member&searchuser=46754)

My first trade 090327 00.30 GMT and IBFX time (03.30 FXDD time)  
Buy  
ODL 1.3556  
IBFX 1.3555  
FXDD 1.3555  
  
Se what happens. Let EA run till market close. No important news what I can se. End time 20, close time 21. Market close 22. See what happens 21 if I´m in a trade. Does EA close the trade?  
I´m happy, EA works!   
  
Elovv 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#317](/thread/post/2631817#post2631817 "Post Permalink")

  * Mar 27, 2009 12:17pm  Mar 27, 2009 12:17pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar95566_5.gif) stifland](stifland)

  * | Joined Mar 2009  | Status: Trader | [304 Posts](/search?do=process&provider=Member&searchuser=95566)

got to plus 19, wow. gonna watch a little more basketball and may take it if it doesn't break resistance up there. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#318](/thread/post/2631843#post2631843 "Post Permalink")

  * Mar 27, 2009 12:36pm  Mar 27, 2009 12:36pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83889_5.gif) siobi](siobi)

  * | Joined Oct 2008  | Status: Trader | [717 Posts](/search?do=process&provider=Member&searchuser=83889)

take 20 pip and run away...... sweet pip huh?  
  
in R9 I'll put in another feature is call NON trade on friday!!! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#319](/thread/post/2631848#post2631848 "Post Permalink")

  * Mar 27, 2009 12:41pm  Mar 27, 2009 12:41pm 

  * [ Elovv](elovv)

  * | Joined Aug 2007  | Status: Trader | [747 Posts](/search?do=process&provider=Member&searchuser=46754)

ODL +2  
IBFX +2  
FXDD +4  
  
TS closed the trades  
  
Elovv 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#320](/thread/post/2631876#post2631876 "Post Permalink")

  * Mar 27, 2009 12:59pm  Mar 27, 2009 12:59pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83889_5.gif) siobi](siobi)

  * | Joined Oct 2008  | Status: Trader | [717 Posts](/search?do=process&provider=Member&searchuser=83889)

is the profit is too little for u?  
  
![](https://resources.faireconomy.media/images/emojis/64/1f61c.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * FX_30M Bouncing System
  *   * [ **Reply to Thread** ](/thread/157406-fx30m-bouncing-system/reply#reply)

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

[The Bouncing Pip](/thread/88277-the-bouncing-pip "Hi everyone. 
 
I present to you a system called &quot;The Bouncing Pip&quot; 
 
This is a system that was originally developed by BigBear, so full...") 26 replies

[Price bouncing off of sma](/thread/228922-price-bouncing-off-of-sma "What is the logic behind a price bouncing off an SMA? 
 
For example if a price bounces of a 35 day sma, i should short it if bounces of...") 2 replies

[Developing a correlated bouncing system](/thread/158016-developing-a-correlated-bouncing-system "The above indicator is a simple ma indicator with the weekly ma set to 40. 
 
I like most of my bouncing signals to be in the direction of...") 9 replies

[bouncing candle indicator](/thread/105826-bouncing-candle-indicator "I once had an indicator that would  send  off an alert whenever a candle touched back on its  moving average.  Lost it somehow, but I do...") 0 replies

[Price bouncing off support or resistance,your thoughts](/thread/30984-price-bouncing-off-support-or-resistanceyour-thoughts "I would like to start a discussuion about price movement at support/resistance, Fib and pivot levels.  
  
Time and again I see the price...") 11 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/157406-fx30m-bouncing-system/reply#reply)
  * Subscribe
  * [72](javascript:void\(0\);)

Attachments: FX_30M Bouncing System

Tags: FX_30M Bouncing System

#  [](/thread/157406-fx30m-bouncing-system)FX_30M Bouncing System 

  * 

  * [#321](/thread/post/2631890#post2631890 "Post Permalink")

  * Mar 27, 2009 1:22pm  Mar 27, 2009 1:22pm 

  * [ Elovv](elovv)

  * | Joined Aug 2007  | Status: Trader | [747 Posts](/search?do=process&provider=Member&searchuser=46754)

> [Quoting siobi](/thread/post/2631876#post2631876 "View Quoted Post")
> 
> Disliked
> 
> is the profit is too little for u?  
>    
>  ![](https://resources.faireconomy.media/images/emojis/64/1f61c.png?v=15.1)
> 
> Ignored

![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) of cource not! If I know I do 2 pip/day it will be great! Then it would be a question of money management before quit ordinarie job! ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#322](/thread/post/2631899#post2631899 "Post Permalink")

  * Mar 27, 2009 1:27pm  Mar 27, 2009 1:27pm 

  * [ paradoxical](paradoxical)

  * | Joined Nov 2007  | Status: Trader | [1,186 Posts](/search?do=process&provider=Member&searchuser=54706)

Long here also at 1.3555 on IBFX live account. Tempted to close at a profit, but will let run while I go to bed & see what happens. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#323](/thread/post/2631932#post2631932 "Post Permalink")

  * Mar 27, 2009 1:55pm  Mar 27, 2009 1:55pm 

  * [ Bobcat2](bobcat2)

  * | Joined Aug 2006  | Status: Trader | [1,024 Posts](/search?do=process&provider=Member&searchuser=16828)

Siobi,  
  
I am still somewhat confused about how to keep the EA running throughout the day. Could you clarify for me, please? Here are the current settings. Please optimize them.  
  
Close Hour = 11  
Hour Start = 0  
Hour End = 24  
  
Stop Loss = 50  
Take Profit = 30  
Trailing Stop = 15  
  
You mentioned a newer version of the EA: 1.04R9 I am currently running 1.04R8. Could you send me the newest version?  
  
I much appreciate what you are doing. By the way, are you familiar with your fellow countryman, Microsuck? He is a very intelligent trader and a very nice guy to boot.  
  
Bob in Wisconsin 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#324](/thread/post/2631943#post2631943 "Post Permalink")

  * Mar 27, 2009 2:05pm  Mar 27, 2009 2:05pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83889_5.gif) siobi](siobi)

  * | Joined Oct 2008  | Status: Trader | [717 Posts](/search?do=process&provider=Member&searchuser=83889)

> [Quoting Bobcat2](/thread/post/2631932#post2631932 "View Quoted Post")
> 
> Disliked
> 
> Siobi,  
>    
>  I am still somewhat confused about how to keep the EA running throughout the day. Could you clarify for me, please? Here are the current settings. Please optimize them.  
>    
>  Close Hour = 11  
>  Hour Start = 0  
>  Hour End = 24  
>    
>  Stop Loss = 50  
>  Take Profit = 30  
>  Trailing Stop = 15  
>    
>  You mentioned a newer version of the EA: 1.04R9 I am currently running 1.04R8. Could you send me the newest version?  
>    
>  I much appreciate what you are doing. By the way, are you familiar with your fellow countryman, Microsuck? He is a very intelligent trader and a very nice...
> 
> Ignored

Close hour set to 30 if you want it to open whole day.  
  
Stop Loss = 100 (for R8)  
Take Profit = 20 (for R8)  
Trailing Stop = 15 (for R8)  
  
  
Stop Loss = 50 (for R9)  
Take Profit = 30 (for R9)  
Trailing Stop = 15 (for R9)  
  
  
I'm from Malaysia..... not sure who is Microsuck?  
  
if Micorsoft then I knew ... ![](https://resources.faireconomy.media/images/emojis/64/1f61c.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#325](/thread/post/2631952#post2631952 "Post Permalink")

  * Mar 27, 2009 2:09pm  Mar 27, 2009 2:09pm 

  * [ nickmead](nickmead)

  * | Commercial User  | Joined Feb 2008 | [66 Posts](/search?do=process&provider=Member&searchuser=61524)

> [Quoting Bobcat2](/thread/post/2631932#post2631932 "View Quoted Post")
> 
> Disliked
> 
> Siobi,  
>    
>  I am still somewhat confused about how to keep the EA running throughout the day. Could you clarify for me, please? Here are the current settings. Please optimize them.  
>    
>  Close Hour = 11  
>  Hour Start = 0  
>  Hour End = 24  
>    
>  Stop Loss = 50  
>  Take Profit = 30  
>  Trailing Stop = 15  
>    
>  You mentioned a newer version of the EA: 1.04R9 I am currently running 1.04R8. Could you send me the newest version?  
>    
>  I much appreciate what you are doing. By the way, are you familiar with your fellow countryman, Microsuck? He is a very intelligent trader and a very nice...
> 
> Ignored

set close hour to 30 and you should be good 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#326](/thread/post/2631957#post2631957 "Post Permalink")

  * Mar 27, 2009 2:12pm  Mar 27, 2009 2:12pm 

  * [ nickmead](nickmead)

  * | Commercial User  | Joined Feb 2008 | [66 Posts](/search?do=process&provider=Member&searchuser=61524)

is r9 available I'd love to have a peek  
  
regards  
  
nick 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#327](/thread/post/2632029#post2632029 "Post Permalink")

  * Mar 27, 2009 3:16pm  Mar 27, 2009 3:16pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83889_5.gif) siobi](siobi)

  * | Joined Oct 2008  | Status: Trader | [717 Posts](/search?do=process&provider=Member&searchuser=83889)

Hi all,  
R9 release date will be on this coming sunday 29-Mac-2009.  
  
safety setting :  
default setting  
  
aggresive setting:  
turn off MA_Check   
turn off SLope_Check  
  
For me,   
I prefer risky seting and change the SL to 100 pip and the rest remain the same.  
Same thing, DONOT trade on news hour!!! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#328](/thread/post/2632127#post2632127 "Post Permalink")

  * Mar 27, 2009 4:10pm  Mar 27, 2009 4:10pm 

  * [ Elovv](elovv)

  * | Joined Aug 2007  | Status: Trader | [747 Posts](/search?do=process&provider=Member&searchuser=46754)

> [Quoting siobi](/thread/post/2632029#post2632029 "View Quoted Post")
> 
> Disliked
> 
> Hi all,  
>  R9 release date will be on this coming sunday 29-Mac-2009.  
>    
>  safety setting :  
>  default setting  
>    
>  aggresive setting:  
>  turn off MA_Check   
>  turn off SLope_Check  
>    
>  For me,   
>  I prefer risky seting and change the SL to 100 pip and the rest remain the same.  
>  Same thing, DONOT trade on news hour!!!
> 
> Ignored

Looks fun. Is it possible to use 2 versions of the EA with the same brooker but with different settings, one safe and one aggresive? Different Magic number?  
  
Elovv 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#329](/thread/post/2632175#post2632175 "Post Permalink")

  * Mar 27, 2009 4:36pm  Mar 27, 2009 4:36pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83889_5.gif) siobi](siobi)

  * | Joined Oct 2008  | Status: Trader | [717 Posts](/search?do=process&provider=Member&searchuser=83889)

no......... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#330](/thread/post/2632183#post2632183 "Post Permalink")

  * Mar 27, 2009 4:39pm  Mar 27, 2009 4:39pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar82875_7.gif) Ezzy](ezzy)

  * | Joined Oct 2008  | Status: Learning | [1,057 Posts](/search?do=process&provider=Member&searchuser=82875)

Hi guys , Siobi and the rest of this thread.  
  
I read the entire (well most ) of the thread last night. I attached the EA on Alpari demo account EU 30 min with settings as per first few posts by Siobi and I have had no trades in almost 24hrs.   
  
Any suggestions why?  
  
I have the smile face on my chart the template etc, but no action.  
  
Any suggestions are greatle appreciated.  
  
Cheers  
Ezzy 

What you do is a reflection of you....what I do is a reflection of me.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#331](/thread/post/2632198#post2632198 "Post Permalink")

  * Mar 27, 2009 4:50pm  Mar 27, 2009 4:50pm 

  * [ cashearner](cashearner)

  * | Joined Aug 2007  | Status: Trader | [8 Posts](/search?do=process&provider=Member&searchuser=46480)

Hi Siobi & all,  
  
I've gone thru all of this thread posts and now on a way to attach the EA to my account, have one question though will it work on Masterforex account? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#332](/thread/post/2632221#post2632221 "Post Permalink")

  * Mar 27, 2009 4:58pm  Mar 27, 2009 4:58pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar82875_7.gif) Ezzy](ezzy)

  * | Joined Oct 2008  | Status: Learning | [1,057 Posts](/search?do=process&provider=Member&searchuser=82875)

Just wondering...  
  
Is Num_of Digit suposed to be on false for 5 digit brokers?  
  
Thanks  
Ezzy 

What you do is a reflection of you....what I do is a reflection of me.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#333](/thread/post/2632230#post2632230 "Post Permalink")

  * Mar 27, 2009 5:03pm  Mar 27, 2009 5:03pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar41845_13.gif) RisingSun](risingsun)

  * Joined Jun 2007 | Status: trader | [1,703 Posts](/search?do=process&provider=Member&searchuser=41845)

> [Quoting Ezzy](/thread/post/2632221#post2632221 "View Quoted Post")
> 
> Disliked
> 
> Just wondering...  
>    
>  Is Num_of Digit suposed to be on false for 5 digit brokers?  
>    
>  Thanks  
>  Ezzy
> 
> Ignored

Just take a look at the remark right above the false/true choice: it says set to "True for 5 digit platform"![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#334](/thread/post/2632237#post2632237 "Post Permalink")

  * Mar 27, 2009 5:05pm  Mar 27, 2009 5:05pm 

  * [ jerrykhor](jerrykhor)

  * | Joined Oct 2008  | Status: Trader | [62 Posts](/search?do=process&provider=Member&searchuser=82338)

hi ezzy, true to 5 digits broker.   
i'm using ibfx (4 digits broker) and i set it to false.  
this ea take not many trade / day....at least during asia session.. ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#335](/thread/post/2632246#post2632246 "Post Permalink")

  * Mar 27, 2009 5:11pm  Mar 27, 2009 5:11pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83889_5.gif) siobi](siobi)

  * | Joined Oct 2008  | Status: Trader | [717 Posts](/search?do=process&provider=Member&searchuser=83889)

to : cashearner  
  
I had never try in masterforex platform... sorry.  
  
to : jerrykhor  
  
what is the SL and TP and TS?  
  
perhaps u post the screen of the setting here... I'm sure Alpari is working fine. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#336](/thread/post/2632250#post2632250 "Post Permalink")

  * Mar 27, 2009 5:13pm  Mar 27, 2009 5:13pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar82875_7.gif) Ezzy](ezzy)

  * | Joined Oct 2008  | Status: Learning | [1,057 Posts](/search?do=process&provider=Member&searchuser=82875)

Cheers gentleman <http://www.forexfactory.com/images/icons/icon7.gif>  
  
Will try again.  
  
Ezzy 

What you do is a reflection of you....what I do is a reflection of me.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#337](/thread/post/2633022#post2633022 "Post Permalink")

  * Mar 27, 2009 10:30pm  Mar 27, 2009 10:30pm 

  * [ paradoxical](paradoxical)

  * | Joined Nov 2007  | Status: Trader | [1,186 Posts](/search?do=process&provider=Member&searchuser=54706)

Another 15 PIPS last night on IBFX live account using a 100 PIP SL and TP. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#338](/thread/post/2633450#post2633450 "Post Permalink")

  * Mar 28, 2009 1:34am  Mar 28, 2009 1:34am 

  * [ Elovv](elovv)

  * | Joined Aug 2007  | Status: Trader | [747 Posts](/search?do=process&provider=Member&searchuser=46754)

Siobi, the difference betwen R7 and R8 are ADX 1/5 min R7 and 5/15 min R8 if I understand correct.  
On the first page of this tread it looks like ADX is 1 and 5 min on you attached tumbnails (but Í´m not sure)  
If so´Your result is from R7?  
  
Elovv 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#339](/thread/post/2633468#post2633468 "Post Permalink")

  * Mar 28, 2009 1:44am  Mar 28, 2009 1:44am 

  * [ paradoxical](paradoxical)

  * | Joined Nov 2007  | Status: Trader | [1,186 Posts](/search?do=process&provider=Member&searchuser=54706)

Dan Johnson, where have you been, and how are you? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#340](/thread/post/2633683#post2633683 "Post Permalink")

  * Mar 28, 2009 3:29am  Mar 28, 2009 3:29am 

  * [ Elovv](elovv)

  * | Joined Aug 2007  | Status: Trader | [747 Posts](/search?do=process&provider=Member&searchuser=46754)

> [Quoting paradoxical](/thread/post/2633468#post2633468 "View Quoted Post")
> 
> Disliked
> 
> Dan Johnson, where have you been, and how are you?
> 
> Ignored

Hi Dan have read everything in the tread. Hope everything goes well for you. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * FX_30M Bouncing System
  *   * [ **Reply to Thread** ](/thread/157406-fx30m-bouncing-system/reply#reply)

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

[The Bouncing Pip](/thread/88277-the-bouncing-pip "Hi everyone. 
 
I present to you a system called &quot;The Bouncing Pip&quot; 
 
This is a system that was originally developed by BigBear, so full...") 26 replies

[Price bouncing off of sma](/thread/228922-price-bouncing-off-of-sma "What is the logic behind a price bouncing off an SMA? 
 
For example if a price bounces of a 35 day sma, i should short it if bounces of...") 2 replies

[Developing a correlated bouncing system](/thread/158016-developing-a-correlated-bouncing-system "The above indicator is a simple ma indicator with the weekly ma set to 40. 
 
I like most of my bouncing signals to be in the direction of...") 9 replies

[bouncing candle indicator](/thread/105826-bouncing-candle-indicator "I once had an indicator that would  send  off an alert whenever a candle touched back on its  moving average.  Lost it somehow, but I do...") 0 replies

[Price bouncing off support or resistance,your thoughts](/thread/30984-price-bouncing-off-support-or-resistanceyour-thoughts "I would like to start a discussuion about price movement at support/resistance, Fib and pivot levels.  
  
Time and again I see the price...") 11 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/157406-fx30m-bouncing-system/reply#reply)
  * Subscribe
  * [72](javascript:void\(0\);)

Attachments: FX_30M Bouncing System

Tags: FX_30M Bouncing System

#  [](/thread/157406-fx30m-bouncing-system)FX_30M Bouncing System 

  * 

  * [#341](/thread/post/2633698#post2633698 "Post Permalink")

  * Mar 28, 2009 3:36am  Mar 28, 2009 3:36am 

  * [ Dan Johnston](dan*johnston)

  * | Joined May 2008  | Status: Trader | [354 Posts](/search?do=process&provider=Member&searchuser=69420)

> [Quoting paradoxical](/thread/post/2633468#post2633468 "View Quoted Post")
> 
> Disliked
> 
> Dan Johnson, where have you been, and how are you?
> 
> Ignored

  
Thank you for asking my friend!  
  
Been a bit busy, but hope to soon get back here more.  
  
Will also be trying to do more chart watching as nothing beats that to learn priceaction.  
  
Still no trades on my live account, so will have to reinstall ea and try again next week.  
  
But got some trades below; 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: 3 27 09.gif
Size: 52 KB](/attachment/image/224861/thumbnail?d=1365566377)](/attachment/image/224861?d=1238178980)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#342](/thread/post/2633717#post2633717 "Post Permalink")

  * Mar 28, 2009 3:45am  Mar 28, 2009 3:45am 

  * [ paradoxical](paradoxical)

  * | Joined Nov 2007  | Status: Trader | [1,186 Posts](/search?do=process&provider=Member&searchuser=54706)

OK. Mine (version r8) is working on both FXDD demo and IBFX live & using a 100 PIP SL & TP with a 20 pip trail stop. Don't think I've had a loss yet. Started at .10 & now .20 & next week will bump it up some more gradually. Siobi coming out with version 9. Hard to think it's better than the version 8 I'm using. I know it's early in the game & possibly just a good time for this EA & things could change. But, looking VERY good so far.

> [Quoting Dan Johnston](/thread/post/2633698#post2633698 "View Quoted Post")
> 
> Disliked
> 
> Thank you for asking my friend!  
>    
>  Been a bit busy, but hope to soon get back here more.  
>    
>  Will also be trying to do more chart watching as nothing beats that to learn priceaction.  
>    
>  Still no trades on my live account, so will have to reinstall ea and try again next week.  
>    
>  But got some trades below;
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#343](/thread/post/2633726#post2633726 "Post Permalink")

  * Mar 28, 2009 3:49am  Mar 28, 2009 3:49am 

  * [ Dan Johnston](dan*johnston)

  * | Joined May 2008  | Status: Trader | [354 Posts](/search?do=process&provider=Member&searchuser=69420)

> [Quoting Elovv](/thread/post/2633683#post2633683 "View Quoted Post")
> 
> Disliked
> 
> Hi Dan have read everything in the tread. Hope everything goes well for you.
> 
> Ignored

Thank you also.   
  
It's nice to be up in here with good people! ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)  
  
Now let's make some money!![](https://resources.faireconomy.media/images/emojis/64/1f911.png?v=15.1)  
  
PS: That trade simulator is great!!! Speed up the priceaction and see how good or bad your latest indicators are together. ...Will be doing that this weekend. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#344](/thread/post/2633731#post2633731 "Post Permalink")

  * Mar 28, 2009 3:52am  Mar 28, 2009 3:52am 

  * [ Dan Johnston](dan*johnston)

  * | Joined May 2008  | Status: Trader | [354 Posts](/search?do=process&provider=Member&searchuser=69420)

> [Quoting paradoxical](/thread/post/2633717#post2633717 "View Quoted Post")
> 
> Disliked
> 
> OK. Mine (version r8) is working on both FXDD demo and IBFX live & using a 100 PIP SL & TP with a 20 pip trail stop. Don't think I've had a loss yet. Started at .10 & now .20 & next week will bump it up some more gradually. Siobi coming out with version 9. Hard to think it's better than the version 8 I'm using. I know it's early in the game & possibly just a good time for this EA & things could change. But, looking VERY good so far.
> 
> Ignored

Excellent news!   
  
Please continue to keep us informed every step of the way and screenshots of actual trades and drawdowns if you can. ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#345](/thread/post/2633733#post2633733 "Post Permalink")

  * Mar 28, 2009 3:52am  Mar 28, 2009 3:52am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar92141_5.gif) tex](tex)

  * | Joined Jan 2009  | Status: Trader | [272 Posts](/search?do=process&provider=Member&searchuser=92141)

hello dan, ah i read ur fine -> very good ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
  
seems ppl started to miss u here (me included ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1) )  
  
which simulator do u mean ? i think i missed that   
  
many greets,  
tex 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#346](/thread/post/2633753#post2633753 "Post Permalink")

  * Mar 28, 2009 4:04am  Mar 28, 2009 4:04am 

  * [ Dan Johnston](dan*johnston)

  * | Joined May 2008  | Status: Trader | [354 Posts](/search?do=process&provider=Member&searchuser=69420)

> [Quoting tex](/thread/post/2633733#post2633733 "View Quoted Post")
> 
> Disliked
> 
> hello dan, ah i read ur fine -> very good ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
>    
>  seems ppl started to miss u here (me included ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1) )  
>    
>  which simulator do u mean ? i think i missed that   
>    
>  many greets,  
>  tex
> 
> Ignored

Thank you tex.  
  
Yea, I kind of hogged this thread too much in the past.![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)  
  
The trade simulator is below courtesy of Lohad:  
  
[http://www.forexfactory.com/showthre...156653&page=19](http://www.forexfactory.com/showthread.php?t=156653&page=19)  
Post 273. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#347](/thread/post/2633754#post2633754 "Post Permalink")

  * Mar 28, 2009 4:04am  Mar 28, 2009 4:04am 

  * [ Elovv](elovv)

  * | Joined Aug 2007  | Status: Trader | [747 Posts](/search?do=process&provider=Member&searchuser=46754)

> [Quoting paradoxical](/thread/post/2633717#post2633717 "View Quoted Post")
> 
> Disliked
> 
> OK. Mine (version r8) is working on both FXDD demo and IBFX live & using a 100 PIP SL & TP with a 20 pip trail stop. Don't think I've had a loss yet. Started at .10 & now .20 & next week will bump it up some more gradually. Siobi coming out with version 9. Hard to think it's better than the version 8 I'm using. I know it's early in the game & possibly just a good time for this EA & things could change. But, looking VERY good so far.
> 
> Ignored

Hi there Paradoxial  
I guess you use r8 (ADX=5 and 15)  
I look at gz10cg´s backtest. His best result is 15 min 100-100-20.  
2/3-20/3 34 win 1 lose wins 808-100=708 pips!  
second best 30 min 100-100-20 =659 pips  
  
For how long time have you test your setting and what is your result?  
  
Elovv 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#348](/thread/post/2633787#post2633787 "Post Permalink")

  * Mar 28, 2009 4:29am  Mar 28, 2009 4:29am 

  * [ paradoxical](paradoxical)

  * | Joined Nov 2007  | Status: Trader | [1,186 Posts](/search?do=process&provider=Member&searchuser=54706)

I forgot about the 100 PIP loss that happened on this EA, as this is on my live account & I have other EAs and other trades, etc. I started live on 3-20 and had a 20 PIP win and 100 PIP loss. On 3-23, I had two wins of 1 pip each. On 3-24, one win for 16 PIPS. On 3-25, two wins of 23 and 8 PIPS, and on 3-26, one win for 10 pips, and on 3-27, one win for 15 PIPS.  
I have it attached to a 30 minute chart & will switch to a 15 minute chart.   
8 wins totalling 96 PIPS and one loss of 100 PIPS.  
Siobi said you can't use this same EA on the same account? I'd like to experiment with different trail stops, take profit & stops on both time frames. Would the EA conflict with other open trades if I attached it to separate charts? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#349](/thread/post/2633800#post2633800 "Post Permalink")

  * Mar 28, 2009 4:37am  Mar 28, 2009 4:37am 

  * [ Elovv](elovv)

  * | Joined Aug 2007  | Status: Trader | [747 Posts](/search?do=process&provider=Member&searchuser=46754)

I think it is not possible to have many charts on the same brooker and use the EA with differenrt settings. I have done it with other EA´s but with different magic numbers. I don´t think we can separate the charts with different magic numbers with this EA  
  
Elovv 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#350](/thread/post/2633814#post2633814 "Post Permalink")

  * Mar 28, 2009 4:47am  Mar 28, 2009 4:47am 

  * [ dougragan](dougragan)

  * | Joined Mar 2009  | Status: Trader | [13 Posts](/search?do=process&provider=Member&searchuser=98170)

Ok, I am the new guy so I ask for patience. I looked at the first post over and over and have no idea how to set this up to test. I am using the [FXCM](/brokers/fxcm "View FXCM Broker Profile") demo. Does this only work on certain platforms? I have a lot of time in forex, but have never actually set up a strategy.   
  
Need help, thanks. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#351](/thread/post/2633819#post2633819 "Post Permalink")

  * Mar 28, 2009 4:51am  Mar 28, 2009 4:51am 

  * [ Elovv](elovv)

  * | Joined Aug 2007  | Status: Trader | [747 Posts](/search?do=process&provider=Member&searchuser=46754)

> [Quoting dougragan](/thread/post/2633814#post2633814 "View Quoted Post")
> 
> Disliked
> 
> Ok, I am the new guy so I ask for patience. I looked at the first post over and over and have no idea how to set this up to test. I am using the FXCM demo. Does this only work on certain platforms? I have a lot of time in forex, but have never actually set up a strategy.   
>    
>  Need help, thanks.
> 
> Ignored

You must have a MT4 platform if you will use it.  
  
Elovv 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#352](/thread/post/2634298#post2634298 "Post Permalink")

  * Mar 28, 2009 2:22pm  Mar 28, 2009 2:22pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83889_5.gif) siobi](siobi)

  * | Joined Oct 2008  | Status: Trader | [717 Posts](/search?do=process&provider=Member&searchuser=83889)

hi all,  
  
thanks for all the feedback and testing.  
  
u can run multiple different EA in the same acct. BUT not multiple same EA in the same acct.  
  
I had strictly control based on prefix magicnumber to ensure only 1 V104 is running at a time.  
  
if u have 2 different version of V104 running on the same machine, then you might be having signal for lower version but not higher version.  
  
because the entry strategy is a little bit different between each version(no exit strategy yet), so u might experience lower version to tak a trade but not the higher version.  
  
since higher version having more filteration, thus it might filter off more bad trade.  
  
you may choose to turn off thos EXTRA filter in R9 then it should behave same as R8. Get it? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#353](/thread/post/2634332#post2634332 "Post Permalink")

  * Mar 28, 2009 3:46pm  Mar 28, 2009 3:46pm 

  * [ Elovv](elovv)

  * | Joined Aug 2007  | Status: Trader | [747 Posts](/search?do=process&provider=Member&searchuser=46754)

Wouldn´t that be possible if they had different magic number? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#354](/thread/post/2635436#post2635436 "Post Permalink")

  * Mar 29, 2009 8:10pm  Mar 29, 2009 8:10pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83889_5.gif) siobi](siobi)

  * | Joined Oct 2008  | Status: Trader | [717 Posts](/search?do=process&provider=Member&searchuser=83889)

hi all,  
  
R9 released...  
  
Please take the default setting.  
  
safty setting as below:  
SL = 100  
TP = 100  
TS = 20  
  
this EA trying its very best to secure when breakeven of 1 pip when u have 10 pip in your favor.  
  
aggresive setting as below:  
SL = 50  
TP = 30  
TS = 15  
  
This EA had improved from its entering strategy by taking out the slope checking for 30 minutes, having higher timeframe checking and MA checking.  
  
Good luck!!! 

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [FX_30M_Bouncing_V104_R9.ex4](/attachment/file/225323?d=1238324546) 18 KB | 602 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#355](/thread/post/2635581#post2635581 "Post Permalink")

  * Mar 29, 2009 11:34pm  Mar 29, 2009 11:34pm 

  * [ nickmead](nickmead)

  * | Commercial User  | Joined Feb 2008 | [66 Posts](/search?do=process&provider=Member&searchuser=61524)

> [Quoting siobi](/thread/post/2635436#post2635436 "View Quoted Post")
> 
> Disliked
> 
> hi all,  
>    
>  R9 released...  
>    
>  Please take the default setting.  
>    
>  safty setting as below:  
>  SL = 100  
>  TP = 100  
>  TS = 20  
>    
>  this EA trying its very best to secure when breakeven of 1 pip when u have 10 pip in your favor.  
>    
>  aggresive setting as below:  
>  SL = 50  
>  TP = 30  
>  TS = 15  
>    
>  This EA had improved from its entering strategy by taking out the slope checking for 30 minutes, having higher timeframe checking and MA checking.  
>    
>  Good luck!!!
> 
> Ignored

Thx Siobi I look forward to trying r9 this week. My question is how do I replace r8 in the template, or will you issue a new template for r9.  
  
thx  
  
Nick 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#356](/thread/post/2635620#post2635620 "Post Permalink")

  * Mar 30, 2009 12:18am  Mar 30, 2009 12:18am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83889_5.gif) siobi](siobi)

  * | Joined Oct 2008  | Status: Trader | [717 Posts](/search?do=process&provider=Member&searchuser=83889)

R9 is working same as R8, just only the entry strategy filetering process.... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#357](/thread/post/2635646#post2635646 "Post Permalink")

  * Mar 30, 2009 12:42am  Mar 30, 2009 12:42am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar95566_5.gif) stifland](stifland)

  * | Joined Mar 2009  | Status: Trader | [304 Posts](/search?do=process&provider=Member&searchuser=95566)

hey siobi. are you still only going to trade this in Asian session? i.e start 0, stop 10 close 11 as before? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#358](/thread/post/2635647#post2635647 "Post Permalink")

  * Mar 30, 2009 12:42am  Mar 30, 2009 12:42am 

  * [ nickmead](nickmead)

  * | Commercial User  | Joined Feb 2008 | [66 Posts](/search?do=process&provider=Member&searchuser=61524)

> [Quoting siobi](/thread/post/2635620#post2635620 "View Quoted Post")
> 
> Disliked
> 
> R9 is working same as R8, just only the entry strategy filetering process....
> 
> Ignored

When I load the template it brings up r8. How do I get it to load r9  
  
thx for your help  
  
Nick 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#359](/thread/post/2635674#post2635674 "Post Permalink")

  * Mar 30, 2009 1:03am  Mar 30, 2009 1:03am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar95566_5.gif) stifland](stifland)

  * | Joined Mar 2009  | Status: Trader | [304 Posts](/search?do=process&provider=Member&searchuser=95566)

Just remove the expert from existing chart and place on new expert. The above siobi post is not a template, just the new EA. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#360](/thread/post/2635739#post2635739 "Post Permalink")

  * Mar 30, 2009 2:06am  Mar 30, 2009 2:06am 

  * [ nickmead](nickmead)

  * | Commercial User  | Joined Feb 2008 | [66 Posts](/search?do=process&provider=Member&searchuser=61524)

> [Quoting stifland](/thread/post/2635674#post2635674 "View Quoted Post")
> 
> Disliked
> 
> Just remove the expert from existing chart and place on new expert. The above siobi post is not a template, just the new EA.
> 
> Ignored

got it. Thanks  
  
Nick 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * FX_30M Bouncing System
  *   * [ **Reply to Thread** ](/thread/157406-fx30m-bouncing-system/reply#reply)

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

[The Bouncing Pip](/thread/88277-the-bouncing-pip "Hi everyone. 
 
I present to you a system called &quot;The Bouncing Pip&quot; 
 
This is a system that was originally developed by BigBear, so full...") 26 replies

[Price bouncing off of sma](/thread/228922-price-bouncing-off-of-sma "What is the logic behind a price bouncing off an SMA? 
 
For example if a price bounces of a 35 day sma, i should short it if bounces of...") 2 replies

[Developing a correlated bouncing system](/thread/158016-developing-a-correlated-bouncing-system "The above indicator is a simple ma indicator with the weekly ma set to 40. 
 
I like most of my bouncing signals to be in the direction of...") 9 replies

[bouncing candle indicator](/thread/105826-bouncing-candle-indicator "I once had an indicator that would  send  off an alert whenever a candle touched back on its  moving average.  Lost it somehow, but I do...") 0 replies

[Price bouncing off support or resistance,your thoughts](/thread/30984-price-bouncing-off-support-or-resistanceyour-thoughts "I would like to start a discussuion about price movement at support/resistance, Fib and pivot levels.  
  
Time and again I see the price...") 11 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/157406-fx30m-bouncing-system/reply#reply)
  * Subscribe
  * [72](javascript:void\(0\);)

Attachments: FX_30M Bouncing System

Tags: FX_30M Bouncing System

#  [](/thread/157406-fx30m-bouncing-system)FX_30M Bouncing System 

  * 

  * [#361](/thread/post/2635760#post2635760 "Post Permalink")

  * Mar 30, 2009 2:39am  Mar 30, 2009 2:39am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar95566_5.gif) stifland](stifland)

  * | Joined Mar 2009  | Status: Trader | [304 Posts](/search?do=process&provider=Member&searchuser=95566)

Siobi, my Ma check and slope check come set to false. Is that correct for default setting? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#362](/thread/post/2635970#post2635970 "Post Permalink")

  * Mar 30, 2009 6:25am  Mar 30, 2009 6:25am 

  * [ Dan Johnston](dan*johnston)

  * | Joined May 2008  | Status: Trader | [354 Posts](/search?do=process&provider=Member&searchuser=69420)

Ok, got mine on aggressive settings ibfx demo testing, so if anyone else doesn't mind to test on default settings on demo?  
  
....Or vice versa is allright with me, just let me know. (We should maybe delegate some tasks as to not duplicate too much perhaps.)  
  
Thanks Siobi and everyone!!!  
  
PS: Let's stop in to the old thread once in a while to try out new ideas if it's ok with you Siobi.  
  
![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#363](/thread/post/2636114#post2636114 "Post Permalink")

  * Mar 30, 2009 7:57am  Mar 30, 2009 7:57am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83889_5.gif) siobi](siobi)

  * | Joined Oct 2008  | Status: Trader | [717 Posts](/search?do=process&provider=Member&searchuser=83889)

hi all,  
  
the setting for slope check and MA check is defaulted to FALSE.  
  
these 2 checking is mainly for securefilteration on higher timeframe.  
  
MA check is to ensure if pricing below 200SMA, then the EA only takes the SHORT signal and vice versa.  
  
Slope check is to ensure 60M timeframe slope line is in same direction before placing a trade.  
  
I had put both default to FALSE, u may turn it on if u wanna be more secure.  
  
trading time is now open to all market time but still only on EUR/USD and NON news hour.  
  
extra thing is NO trade on Friday!!!   
This EA had been preset so NO trade on friday and it is our EA holiday!!!!   
  
![](https://resources.faireconomy.media/images/emojis/64/1f61c.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#364](/thread/post/2636183#post2636183 "Post Permalink")

  * Mar 30, 2009 8:36am  Mar 30, 2009 8:36am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar95566_5.gif) stifland](stifland)

  * | Joined Mar 2009  | Status: Trader | [304 Posts](/search?do=process&provider=Member&searchuser=95566)

i got it on the default Dan. Both on False. Live but just Micro lot. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#365](/thread/post/2636222#post2636222 "Post Permalink")

  * Mar 30, 2009 9:05am  Mar 30, 2009 9:05am 

  * [ Dan Johnston](dan*johnston)

  * | Joined May 2008  | Status: Trader | [354 Posts](/search?do=process&provider=Member&searchuser=69420)

> [Quoting stifland](/thread/post/2636183#post2636183 "View Quoted Post")
> 
> Disliked
> 
> i got it on the default Dan. Both on False. Live but just Micro lot.
> 
> Ignored

As they say... NICE!!!![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)  
  
Good luck so we may all scale up!!! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#366](/thread/post/2637465#post2637465 "Post Permalink")

  * Mar 30, 2009 8:56pm  Mar 30, 2009 8:56pm 

  * [ Elovv](elovv)

  * | Joined Aug 2007  | Status: Trader | [747 Posts](/search?do=process&provider=Member&searchuser=46754)

Any trades, anybody? I have no trades, started EA 0 GMT  
  
Elovv 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#367](/thread/post/2637493#post2637493 "Post Permalink")

  * Mar 30, 2009 9:13pm  Mar 30, 2009 9:13pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83889_5.gif) siobi](siobi)

  * | Joined Oct 2008  | Status: Trader | [717 Posts](/search?do=process&provider=Member&searchuser=83889)

hi all,  
me also no trade today... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#368](/thread/post/2637586#post2637586 "Post Permalink")

  * Mar 30, 2009 9:56pm  Mar 30, 2009 9:56pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar95566_5.gif) stifland](stifland)

  * | Joined Mar 2009  | Status: Trader | [304 Posts](/search?do=process&provider=Member&searchuser=95566)

no, if you notice, both adx say "range" and it has been compared to friday. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#369](/thread/post/2637614#post2637614 "Post Permalink")

  * Mar 30, 2009 10:13pm  Mar 30, 2009 10:13pm 

  * [ mshari](mshari)

  * | Joined Jan 2009  | Status: Trader | [2 Posts](/search?do=process&provider=Member&searchuser=92559)

Any trades, anybody? I have no trades 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#370](/thread/post/2637676#post2637676 "Post Permalink")

  * Mar 30, 2009 10:38pm  Mar 30, 2009 10:38pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar92141_5.gif) tex](tex)

  * | Joined Jan 2009  | Status: Trader | [272 Posts](/search?do=process&provider=Member&searchuser=92141)

same here, no trades by now.. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#371](/thread/post/2637697#post2637697 "Post Permalink")

  * Mar 30, 2009 10:45pm  Mar 30, 2009 10:45pm 

  * [ paradoxical](paradoxical)

  * | Joined Nov 2007  | Status: Trader | [1,186 Posts](/search?do=process&provider=Member&searchuser=54706)

I didn't get a chance to load the R9. Left the R8 running and no trades. A question for Siobi or anyone that may know. Can I run the R8 and the R9 on two separate charts?

> [Quoting tex](/thread/post/2637676#post2637676 "View Quoted Post")
> 
> Disliked
> 
> same here, no trades by now..
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#372](/thread/post/2637825#post2637825 "Post Permalink")

  * Mar 30, 2009 11:29pm  Mar 30, 2009 11:29pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83889_5.gif) siobi](siobi)

  * | Joined Oct 2008  | Status: Trader | [717 Posts](/search?do=process&provider=Member&searchuser=83889)

> [Quoting paradoxical](/thread/post/2637697#post2637697 "View Quoted Post")
> 
> Disliked
> 
> I didn't get a chance to load the R9. Left the R8 running and no trades. A question for Siobi or anyone that may know. Can I run the R8 and the R9 on two separate charts?
> 
> Ignored

  
I think I had mentioned.  
  
you may run R8 and R9 on same platform, but most likely R8 is the one will be opening the trade!!! R9 is just having additional and it is solely basedon R8 with addionatiol filtering. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#373](/thread/post/2639248#post2639248 "Post Permalink")

  * Mar 31, 2009 10:08am  Mar 31, 2009 10:08am 

  * [ besiege31](besiege31)

  * | Joined Mar 2009  | Status: Trader | [8 Posts](/search?do=process&provider=Member&searchuser=96795)

Just to make sure I got this right, if I leave the setting to default then it should trade the japan time frame correct? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#374](/thread/post/2639303#post2639303 "Post Permalink")

  * Mar 31, 2009 10:28am  Mar 31, 2009 10:28am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83889_5.gif) siobi](siobi)

  * | Joined Oct 2008  | Status: Trader | [717 Posts](/search?do=process&provider=Member&searchuser=83889)

hi there, this R9 is able to trade for all time zone but only EUR/USD pair... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#375](/thread/post/2639352#post2639352 "Post Permalink")

  * Mar 31, 2009 11:02am  Mar 31, 2009 11:02am 

  * [ besiege31](besiege31)

  * | Joined Mar 2009  | Status: Trader | [8 Posts](/search?do=process&provider=Member&searchuser=96795)

I'm just started r8. I didn't see an r9 and I thought I read all the posts. can you repost it. I back tested r8 and it did great. I didn't get any trades today though so I want to make sure my settings are right. Thanks in advance. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#376](/thread/post/2639407#post2639407 "Post Permalink")

  * Mar 31, 2009 11:30am  Mar 31, 2009 11:30am 

  * [ paradoxical](paradoxical)

  * | Joined Nov 2007  | Status: Trader | [1,186 Posts](/search?do=process&provider=Member&searchuser=54706)

Currently in a buy trade at 1.3213 using version R8, and up 28 pips. With the 20 pip trail stop, would still be a plus 19 pips even if it drops from here. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: eu 3-30.gif
Size: 37 KB](/attachment/image/226211/thumbnail?d=1365566674)](/attachment/image/226211?d=1238466432)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#377](/thread/post/2639455#post2639455 "Post Permalink")

  * Mar 31, 2009 12:00pm  Mar 31, 2009 12:00pm 

  * [ besiege31](besiege31)

  * | Joined Mar 2009  | Status: Trader | [8 Posts](/search?do=process&provider=Member&searchuser=96795)

paradox,  
would you post your setting so I can see what is different. I trade fxdd, and have .1 lot. I see you have .2 That's the only thing I see right off. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#378](/thread/post/2640339#post2640339 "Post Permalink")

  * Mar 31, 2009 7:43pm  Mar 31, 2009 7:43pm 

  * [ currymonster](currymonster)

  * | Joined Feb 2007  | Status: Trader | [92 Posts](/search?do=process&provider=Member&searchuser=34011)

Thanks for the great method and EA Siobhi. Two trades today but I am running on 15 and 30 min eur usd. No trades yesterday.  
  
Running on an IBFX demo- IBFX are known as tyhe worst broker for running EAs but curious to see if it trades live. Will put it live next week on 0.01 lots just for curiosity sakes!  
  
Thanks again!  
  
Cal ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

Attached Image (click to enlarge)

[![Click to Enlarge

Name: ScreenHunter_01 Mar. 31 11.38.gif
Size: 26 KB](/attachment/image/226382/thumbnail?d=1365566699)](/attachment/image/226382?d=1238496195)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#379](/thread/post/2640593#post2640593 "Post Permalink")

  * Mar 31, 2009 9:24pm  Mar 31, 2009 9:24pm 

  * [ qz10cq](qz10cq)

  * | Joined Dec 2006  | Status: Trader | [303 Posts](/search?do=process&provider=Member&searchuser=29720)

Siobi, guys, trading 10 pairs all with less than 10 spread on FXDD, lots .1 using r9 with slope true. Since open of markets Sunday. I've had 4 trades for a total profit of +5 and all of them were winners. Siobi maybe it's to safe? I don't know exactly what you did between r8 - r9 (about the 1 pip profit thing) but it seems that only trailing stop was the way to go? Will test remainder of week and keep you informed....Dan 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#380](/thread/post/2640681#post2640681 "Post Permalink")

  * Mar 31, 2009 10:08pm  Mar 31, 2009 10:08pm 

  * [ paradoxical](paradoxical)

  * | Joined Nov 2007  | Status: Trader | [1,186 Posts](/search?do=process&provider=Member&searchuser=54706)

besiege, the .2 lots should have nothing to do with whether or not it makes trades. The price feeds are different between the two brokers. ON occasion, one will make a trade, and the other won't.   
My settings are to trade all day, which is; Close hour 30, Hour Start 0, and Hour End 24.

> [Quoting besiege31](/thread/post/2639455#post2639455 "View Quoted Post")
> 
> Disliked
> 
> paradox,  
>  would you post your setting so I can see what is different. I trade fxdd, and have .1 lot. I see you have .2 That's the only thing I see right off.
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * FX_30M Bouncing System
  *   * [ **Reply to Thread** ](/thread/157406-fx30m-bouncing-system/reply#reply)

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

[The Bouncing Pip](/thread/88277-the-bouncing-pip "Hi everyone. 
 
I present to you a system called &quot;The Bouncing Pip&quot; 
 
This is a system that was originally developed by BigBear, so full...") 26 replies

[Price bouncing off of sma](/thread/228922-price-bouncing-off-of-sma "What is the logic behind a price bouncing off an SMA? 
 
For example if a price bounces of a 35 day sma, i should short it if bounces of...") 2 replies

[Developing a correlated bouncing system](/thread/158016-developing-a-correlated-bouncing-system "The above indicator is a simple ma indicator with the weekly ma set to 40. 
 
I like most of my bouncing signals to be in the direction of...") 9 replies

[bouncing candle indicator](/thread/105826-bouncing-candle-indicator "I once had an indicator that would  send  off an alert whenever a candle touched back on its  moving average.  Lost it somehow, but I do...") 0 replies

[Price bouncing off support or resistance,your thoughts](/thread/30984-price-bouncing-off-support-or-resistanceyour-thoughts "I would like to start a discussuion about price movement at support/resistance, Fib and pivot levels.  
  
Time and again I see the price...") 11 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/157406-fx30m-bouncing-system/reply#reply)
  * Subscribe
  * [72](javascript:void\(0\);)

Attachments: FX_30M Bouncing System

Tags: FX_30M Bouncing System

#  [](/thread/157406-fx30m-bouncing-system)FX_30M Bouncing System 

  * 

  * [#381](/thread/post/2640684#post2640684 "Post Permalink")

  * Mar 31, 2009 10:09pm  Mar 31, 2009 10:09pm 

  * [ paradoxical](paradoxical)

  * | Joined Nov 2007  | Status: Trader | [1,186 Posts](/search?do=process&provider=Member&searchuser=54706)

currymonster, I've been trading the R8 live on IBFX. 

> [Quoting currymonster](/thread/post/2640339#post2640339 "View Quoted Post")
> 
> Disliked
> 
> Thanks for the great method and EA Siobhi. Two trades today but I am running on 15 and 30 min eur usd. No trades yesterday.  
>    
>  Running on an IBFX demo- IBFX are known as tyhe worst broker for running EAs but curious to see if it trades live. Will put it live next week on 0.01 lots just for curiosity sakes!  
>    
>  Thanks again!  
>    
>  Cal ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#382](/thread/post/2640824#post2640824 "Post Permalink")

  * Mar 31, 2009 11:07pm  Mar 31, 2009 11:07pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83889_5.gif) siobi](siobi)

  * | Joined Oct 2008  | Status: Trader | [717 Posts](/search?do=process&provider=Member&searchuser=83889)

> [Quoting qz10cq](/thread/post/2640593#post2640593 "View Quoted Post")
> 
> Disliked
> 
> Siobi, guys, trading 10 pairs all with less than 10 spread on FXDD, lots .1 using r9 with slope true. Since open of markets Sunday. I've had 4 trades for a total profit of +5 and all of them were winners. Siobi maybe it's to safe? I don't know exactly what you did between r8 - r9 (about the 1 pip profit thing) but it seems that only trailing stop was the way to go? Will test remainder of week and keep you informed....Dan
> 
> Ignored

I had also inserted a move step profit protection of 1 pip once the price is in our favor of 10 pip 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#383](/thread/post/2640842#post2640842 "Post Permalink")

  * Mar 31, 2009 11:12pm  Mar 31, 2009 11:12pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar95566_5.gif) stifland](stifland)

  * | Joined Mar 2009  | Status: Trader | [304 Posts](/search?do=process&provider=Member&searchuser=95566)

no trades this week on default.....so far 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#384](/thread/post/2641114#post2641114 "Post Permalink")

  * Apr 1, 2009 12:45am  Apr 1, 2009 12:45am 

  * [ qz10cq](qz10cq)

  * | Joined Dec 2006  | Status: Trader | [303 Posts](/search?do=process&provider=Member&searchuser=29720)

> [Quoting siobi](/thread/post/2640824#post2640824 "View Quoted Post")
> 
> Disliked
> 
> I had also inserted a move step profit protection of 1 pip once the price is in our favor of 10 pip
> 
> Ignored

To make it clear for myself and others:  
  
* Plus 10 pips means the EA will kick in and protect 1 pip  
  
* Plus 20 pips means trailing stop is kickin in so your protected  
  
* If your above the 200 ma it only takes long trades  
  
* If your below the 200 ma it only takes short trades  
  
* The 30m slope must agree with the 1hr slope for a trade to be taken  
  
**** GOOD THINKING SIOBI.   
  
This sure sounds like a winner. Lets see how it plays out. Only thing I could suggest is to have the 30m slope agree with the 4hr instead of the 1hr. A trailing stop starting at 10 and increasing as profit increased would be nice. Last night I was up 16-17 pips and ended with 1 (not complaining) but could have had 6-7 which is BIG difference. My 4 trades could have been 30 instead of 5. Great EA Siobi, Thank you... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#385](/thread/post/2641186#post2641186 "Post Permalink")

  * Apr 1, 2009 1:09am  Apr 1, 2009 1:09am 

  * [ Snowdogg](snowdogg)

  * | Joined Mar 2005  | Status: Trader | [38 Posts](/search?do=process&provider=Member&searchuser=1871)

I have no trades yet this week either. I checked everything and looks all right. In the Experts tab I found some messages saying 1. Slope direction line deinitialized, then 2. Slope Direction Line uninit reason 5, then 3. Slope Direction Line initialized. Is there a problem with this? What else can I check? I am on EUR/USD 30M ITFX demo. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#386](/thread/post/2641989#post2641989 "Post Permalink")

  * Apr 1, 2009 5:47am  Apr 1, 2009 5:47am 

  * [ besiege31](besiege31)

  * | Joined Mar 2009  | Status: Trader | [8 Posts](/search?do=process&provider=Member&searchuser=96795)

> [Quoting paradoxical](/thread/post/2640681#post2640681 "View Quoted Post")
> 
> Disliked
> 
> besiege, the .2 lots should have nothing to do with whether or not it makes trades. The price feeds are different between the two brokers. ON occasion, one will make a trade, and the other won't.   
>  My settings are to trade all day, which is; Close hour 30, Hour Start 0, and Hour End 24.
> 
> Ignored

  
Paradoxical,  
I agree on the lot size, and I didn't believe that was the problem, but that is the only thing I saw different from your pictured chart. I don't have all day set up. when I back tested it seemed to do better on the japan session...everything else I have set up is default, other then TP and SL. which I adjusted to what I believed works best for me. Thanks for the help and happy trading.! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#387](/thread/post/2642215#post2642215 "Post Permalink")

  * Apr 1, 2009 7:53am  Apr 1, 2009 7:53am 

  * [ paradoxical](paradoxical)

  * | Joined Nov 2007  | Status: Trader | [1,186 Posts](/search?do=process&provider=Member&searchuser=54706)

Am in a sell trade at 1.3241 that traded at 22:01 IBFX time (GMT). Was down 18 pips but now coming back around. Down 12. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#388](/thread/post/2642235#post2642235 "Post Permalink")

  * Apr 1, 2009 8:04am  Apr 1, 2009 8:04am 

  * [ currymonster](currymonster)

  * | Joined Feb 2007  | Status: Trader | [92 Posts](/search?do=process&provider=Member&searchuser=34011)

> [Quoting paradoxical](/thread/post/2640684#post2640684 "View Quoted Post")
> 
> Disliked
> 
> currymonster, I've been trading the R8 live on IBFX.
> 
> Ignored

That's good news, your results are on a par with the demo? They have a bad reputation live for EAs I've witnessed the requotes etc myself before.  
  
Cheers para dude!  
  
Cal ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)) 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#389](/thread/post/2642247#post2642247 "Post Permalink")

  * Apr 1, 2009 8:10am  Apr 1, 2009 8:10am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83889_5.gif) siobi](siobi)

  * | Joined Oct 2008  | Status: Trader | [717 Posts](/search?do=process&provider=Member&searchuser=83889)

> [Quoting qz10cq](/thread/post/2641114#post2641114 "View Quoted Post")
> 
> Disliked
> 
> To make it clear for myself and others:  
>    
>  * Plus 10 pips means the EA will kick in and protect 1 pip  
>    
>  * Plus 20 pips means trailing stop is kickin in so your protected  
>    
>  * If your above the 200 ma it only takes long trades  
>    
>  * If your below the 200 ma it only takes short trades  
>    
>  * The 30m slope must agree with the 1hr slope for a trade to be taken  
>    
>  **** GOOD THINKING SIOBI.   
>    
>  This sure sounds like a winner. Lets see how it plays out. Only thing I could suggest is to have the 30m slope agree with the 4hr instead of the 1hr. A trailing stop starting...
> 
> Ignored

  
thanks!!! good idea of comapring 4H.... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#390](/thread/post/2642456#post2642456 "Post Permalink")

  * Apr 1, 2009 9:42am  Apr 1, 2009 9:42am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar94654_2.gif) walrus_78](walrus_78)

  * | Joined Feb 2009  | Status: Trader | [19 Posts](/search?do=process&provider=Member&searchuser=94654)

I've been trading manually with the r9 method and I think it's enough to have:  
  
ADX 5m - down  
ADX 15m - down  
SD 240 - Short  
SD 30 - Short  
PSAR 30 - Short  
PSAR 30_1 - Short  
  
Having at least this I have had good results manually, to buy you have to wait for the opposite. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#391](/thread/post/2642541#post2642541 "Post Permalink")

  * Apr 1, 2009 10:20am  Apr 1, 2009 10:20am 

  * [ paradoxical](paradoxical)

  * | Joined Nov 2007  | Status: Trader | [1,186 Posts](/search?do=process&provider=Member&searchuser=54706)

Can't say for a demo IBFX account, as I'm trading it live only, and only at .2 lots. The trade mentioned earlier was down, but reversed and closed for a 9 pip profit, due to the trail stop. As it stands, would have 29 PIPS more profit if I didn't have a trail stop. Not complaining. 

> [Quoting currymonster](/thread/post/2642235#post2642235 "View Quoted Post")
> 
> Disliked
> 
> That's good news, your results are on a par with the demo? They have a bad reputation live for EAs I've witnessed the requotes etc myself before.  
>    
>  Cheers para dude!  
>    
>  Cal ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1))
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#392](/thread/post/2643652#post2643652 "Post Permalink")

  * Apr 1, 2009 8:26pm  Apr 1, 2009 8:26pm 

  * [ Orenn](orenn)

  * | Joined Mar 2009  | Status: Trader | [11 Posts](/search?do=process&provider=Member&searchuser=96427)

I did some backtesting of the last four weeks to compare R8 to R9 results.  
I used Siobi settings, both safe and aggresive and my own favorite R8 setting.  
The results in the attached Excel surprised me a bit because it mostly showed R8 did better than R9. Maybe I got something wrong or missed something. If anybody else can do some backtesting and let me know if he gets other results I'll be thankfull.  
  
So far I'm running R8 on live account (0.04lot) with great results and R9 on demo account (separate insallation) with almost no trades.  
  
For the meantime I'll stick to R8 until R9 results are more conclusive.  
  
Thanks again Siobi, I can't stop being amazed by this EA.  
  
Oren 

Attached File(s)

![File Type: xls](https://assets.faireconomy.media/images/attach/xls.gif) [R9vsR8.xls](/attachment/file/227100?d=1238585059) 14 KB | 375 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#393](/thread/post/2643881#post2643881 "Post Permalink")

  * Apr 1, 2009 9:38pm  Apr 1, 2009 9:38pm 

  * [ qz10cq](qz10cq)

  * | Joined Dec 2006  | Status: Trader | [303 Posts](/search?do=process&provider=Member&searchuser=29720)

> [Quoting qz10cq](/thread/post/2640593#post2640593 "View Quoted Post")
> 
> Disliked
> 
> Siobi, guys, trading 10 pairs all with less than 10 spread on FXDD, lots .1 using r9 with slope true. Since open of markets Sunday. I've had 4 trades for a total profit of +5 and all of them were winners.
> 
> Ignored

Had 2 more winners, both were up 16-17 pips and ended with +1. 6 wins total profit +7. The NFP on Friday always makes the markets strange for that week. Will keep you informed. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#394](/thread/post/2644216#post2644216 "Post Permalink")

  * Apr 1, 2009 11:31pm  Apr 1, 2009 11:31pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar95566_5.gif) stifland](stifland)

  * | Joined Mar 2009  | Status: Trader | [304 Posts](/search?do=process&provider=Member&searchuser=95566)

still no trades this week since switching to r9. will update. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#395](/thread/post/2644243#post2644243 "Post Permalink")

  * Apr 1, 2009 11:39pm  Apr 1, 2009 11:39pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar92141_5.gif) tex](tex)

  * | Joined Jan 2009  | Status: Trader | [272 Posts](/search?do=process&provider=Member&searchuser=92141)

same here, no trades with r09. switched back to r08 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#396](/thread/post/2644251#post2644251 "Post Permalink")

  * Apr 1, 2009 11:41pm  Apr 1, 2009 11:41pm 

  * [ paradoxical](paradoxical)

  * | Joined Nov 2007  | Status: Trader | [1,186 Posts](/search?do=process&provider=Member&searchuser=54706)

Thanks for taking the time to post the back test results. While back test results aren't always accurate, I think that you can still get a sense for the difference between two EAs using slightly different entry parameters. Also, your test shows that the setting of 100 TP, 100 SL, and 20 pip trail stop is the best, which are the same results as previously reported by Siobi.

> [Quoting Orenn](/thread/post/2643652#post2643652 "View Quoted Post")
> 
> Disliked
> 
> I did some backtesting of the last four weeks to compare R8 to R9 results.  
>  I used Siobi settings, both safe and aggresive and my own favorite R8 setting.  
>  The results in the attached Excel surprised me a bit because it mostly showed R8 did better than R9. Maybe I got something wrong or missed something. If anybody else can do some backtesting and let me know if he gets other results I'll be thankfull.  
>    
>  So far I'm running R8 on live account (0.04lot) with great results and R9 on demo account (separate insallation) with almost no trades.  
>    
>  For the...
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#397](/thread/post/2644565#post2644565 "Post Permalink")

  * Apr 2, 2009 1:50am  Apr 2, 2009 1:50am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar48030_6.gif) shinny](shinny)

  * Joined Sep 2007 | Status: Trading The Matrix | [819 Posts](/search?do=process&provider=Member&searchuser=48030)

Hello Everyone,  
  
I have tried back testing, forward testing etc and the ea wont open trades on either.  
  
I am using R9 on Alpari (5 digit).  
  
Help!!!!!  
  
Cheers  
  
Shinny 

Nobody can be told what The Matrix is. You'll have to see it yourself.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#398](/thread/post/2644795#post2644795 "Post Permalink")

  * Apr 2, 2009 3:19am  Apr 2, 2009 3:19am 

  * [ paradoxical](paradoxical)

  * | Joined Nov 2007  | Status: Trader | [1,186 Posts](/search?do=process&provider=Member&searchuser=54706)

A small win of 3 pips at 15:00 hours on a sell. Stopped out with the 20 trailing stop by only two pips before it continued on it's way. Would be plus 36 at this time if not stopped out. But, I go with the law of averages and that a 20 PIP trail stop has worked in the past. I think it will all work for the best in the long run. I'll take wins, no matter how small, instead of losses, no matter how small, any day of the week. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#399](/thread/post/2647288#post2647288 "Post Permalink")

  * Apr 2, 2009 11:19pm  Apr 2, 2009 11:19pm 

  * [ nickmead](nickmead)

  * | Commercial User  | Joined Feb 2008 | [66 Posts](/search?do=process&provider=Member&searchuser=61524)

> [Quoting Orenn](/thread/post/2643652#post2643652 "View Quoted Post")
> 
> Disliked
> 
> I did some backtesting of the last four weeks to compare R8 to R9 results.  
>  I used Siobi settings, both safe and aggresive and my own favorite R8 setting.  
>  The results in the attached Excel surprised me a bit because it mostly showed R8 did better than R9. Maybe I got something wrong or missed something. If anybody else can do some backtesting and let me know if he gets other results I'll be thankfull.  
>    
>  So far I'm running R8 on live account (0.04lot) with great results and R9 on demo account (separate insallation) with almost no trades.  
>    
>  For the...
> 
> Ignored

Were your tests running the EA 24 hours or just the asian session  
  
thx  
Nick 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#400](/thread/post/2647414#post2647414 "Post Permalink")

  * Apr 3, 2009 12:12am  Apr 3, 2009 12:12am 

  * [ paradoxical](paradoxical)

  * | Joined Nov 2007  | Status: Trader | [1,186 Posts](/search?do=process&provider=Member&searchuser=54706)

100 PIP loss last night on a sell at 1.3265, using R8 version 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * FX_30M Bouncing System
  *   * [ **Reply to Thread** ](/thread/157406-fx30m-bouncing-system/reply#reply)

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

[The Bouncing Pip](/thread/88277-the-bouncing-pip "Hi everyone. 
 
I present to you a system called &quot;The Bouncing Pip&quot; 
 
This is a system that was originally developed by BigBear, so full...") 26 replies

[Price bouncing off of sma](/thread/228922-price-bouncing-off-of-sma "What is the logic behind a price bouncing off an SMA? 
 
For example if a price bounces of a 35 day sma, i should short it if bounces of...") 2 replies

[Developing a correlated bouncing system](/thread/158016-developing-a-correlated-bouncing-system "The above indicator is a simple ma indicator with the weekly ma set to 40. 
 
I like most of my bouncing signals to be in the direction of...") 9 replies

[bouncing candle indicator](/thread/105826-bouncing-candle-indicator "I once had an indicator that would  send  off an alert whenever a candle touched back on its  moving average.  Lost it somehow, but I do...") 0 replies

[Price bouncing off support or resistance,your thoughts](/thread/30984-price-bouncing-off-support-or-resistanceyour-thoughts "I would like to start a discussuion about price movement at support/resistance, Fib and pivot levels.  
  
Time and again I see the price...") 11 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/157406-fx30m-bouncing-system/reply#reply)
  * Subscribe
  * [72](javascript:void\(0\);)

Attachments: FX_30M Bouncing System

Tags: FX_30M Bouncing System

#  [](/thread/157406-fx30m-bouncing-system)FX_30M Bouncing System 

  * 

  * [#401](/thread/post/2648004#post2648004 "Post Permalink")

  * Apr 3, 2009 4:17am  Apr 3, 2009 4:17am 

  * [ qz10cq](qz10cq)

  * | Joined Dec 2006  | Status: Trader | [303 Posts](/search?do=process&provider=Member&searchuser=29720)

> [Quoting paradoxical](/thread/post/2647414#post2647414 "View Quoted Post")
> 
> Disliked
> 
> 100 PIP loss last night on a sell at 1.3265, using R8 version
> 
> Ignored

Are you just playing eur/usd? I was using r9 until yesterday (not many trades on r9) switched back to r8 and had 1 eur/usd trade since with 0 profit because of the 15 ts. Since yesterday I've had 16 trades over the 5 pairs I'm trading with a +150. FXDD is the demo broker. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#402](/thread/post/2648066#post2648066 "Post Permalink")

  * Apr 3, 2009 4:52am  Apr 3, 2009 4:52am 

  * [ paradoxical](paradoxical)

  * | Joined Nov 2007  | Status: Trader | [1,186 Posts](/search?do=process&provider=Member&searchuser=54706)

Yes. Just using it, R8 version, live on the EUR/USD with a 100 TP and SL, and a 20 pip trail stop. I did demo some other pairs on FXDD without much success. I think Siobi said before he recommended it only for the E/U. If you have continued success on other pairs, let me know & I'll try them myself live on IBFX with small lots. 

> [Quoting qz10cq](/thread/post/2648004#post2648004 "View Quoted Post")
> 
> Disliked
> 
> Are you just playing eur/usd? I was using r9 until yesterday (not many trades on r9) switched back to r8 and had 1 eur/usd trade since with 0 profit because of the 15 ts. Since yesterday I've had 16 trades over the 5 pairs I'm trading with a +150. FXDD is the demo broker.
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#403](/thread/post/2648096#post2648096 "Post Permalink")

  * Apr 3, 2009 5:09am  Apr 3, 2009 5:09am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar92141_5.gif) tex](tex)

  * | Joined Jan 2009  | Status: Trader | [272 Posts](/search?do=process&provider=Member&searchuser=92141)

hey para,  
  
same here got a -100p trade with r08.   
  
i am on demo account with [activtrades](/brokers/activtrades "View ActivTrades Broker Profile"), uk.  
  
tex 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#404](/thread/post/2648298#post2648298 "Post Permalink")

  * Apr 3, 2009 6:50am  Apr 3, 2009 6:50am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar95566_5.gif) stifland](stifland)

  * | Joined Mar 2009  | Status: Trader | [304 Posts](/search?do=process&provider=Member&searchuser=95566)

1\. QZ, would you mind posting your settings and pairs used?  
2\. R9 has 0 trades since put on. Siobi, do I need to have inicators referenced like 200ma for it to work?  
  
Example below where it looks like a trade should be opened 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: trade.gif
Size: 25 KB](/attachment/image/228064/thumbnail?d=1365567054)](/attachment/image/228064?d=1238709009)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#405](/thread/post/2648387#post2648387 "Post Permalink")

  * Apr 3, 2009 7:53am  Apr 3, 2009 7:53am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83889_5.gif) siobi](siobi)

  * | Joined Oct 2008  | Status: Trader | [717 Posts](/search?do=process&provider=Member&searchuser=83889)

hi guys, R9 still no trade open...  
  
it was filtered off by the PSARFac 60.  
  
it save me from losing of an pip up to now but also it doesnt bring in any profit to me.  
  
As long as we survive in Forex, u r consider still winning...... ![](https://resources.faireconomy.media/images/emojis/64/1f61c.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#406](/thread/post/2648392#post2648392 "Post Permalink")

  * Apr 3, 2009 7:58am  Apr 3, 2009 7:58am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar95566_5.gif) stifland](stifland)

  * | Joined Mar 2009  | Status: Trader | [304 Posts](/search?do=process&provider=Member&searchuser=95566)

That's cool. as long as we match. No trade sometime best. even if we get 1 trade a week and they are winners it would be 400 pips ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#407](/thread/post/2649061#post2649061 "Post Permalink")

  * Apr 3, 2009 3:16pm  Apr 3, 2009 3:16pm 

  * [ Orenn](orenn)

  * | Joined Mar 2009  | Status: Trader | [11 Posts](/search?do=process&provider=Member&searchuser=96427)

> [Quoting nickmead](/thread/post/2647288#post2647288 "View Quoted Post")
> 
> Disliked
> 
> Were your tests running the EA 24 hours or just the asian session  
>    
>  thx  
>  Nick
> 
> Ignored

My backtests were 24h.  
  
Oren 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#408](/thread/post/2649589#post2649589 "Post Permalink")

  * Apr 3, 2009 8:22pm  Apr 3, 2009 8:22pm 

  * [ qz10cq](qz10cq)

  * | Joined Dec 2006  | Status: Trader | [303 Posts](/search?do=process&provider=Member&searchuser=29720)

> [Quoting qz10cq](/thread/post/2648004#post2648004 "View Quoted Post")
> 
> Disliked
> 
> Are you just playing eur/usd? I was using r9 until yesterday (not many trades on r9) switched back to r8 and had 1 eur/usd trade since with 0 profit because of the 15 ts. Since yesterday I've had 16 trades over the 5 pairs I'm trading with a +150. FXDD is the demo broker.
> 
> Ignored

Siobi, thread, I'm trading 10 pairs not 5 pairs, my settings: r8, close hour 30, hour start 0, hour end 24, spread 10, 100sl, 150tp, 15 ts. Profits for the 10 pairs are 180 with a dd right now of 220. Every time I lose with a pair I eliminate it.   
  
Siobi, had 6 trades with r9 for +7 profit over the 10 pairs and was in a dd of 60 when I switched back to your r8. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#409](/thread/post/2649935#post2649935 "Post Permalink")

  * Apr 3, 2009 11:11pm  Apr 3, 2009 11:11pm 

  * [ qz10cq](qz10cq)

  * | Joined Dec 2006  | Status: Trader | [303 Posts](/search?do=process&provider=Member&searchuser=29720)

> [Quoting qz10cq](/thread/post/2649589#post2649589 "View Quoted Post")
> 
> Disliked
> 
> Siobi, thread, I'm trading 10 pairs not 5 pairs, my settings: r8, close hour 30, hour start 0, hour end 24, spread 10, 100sl, 150tp, 15 ts. Profits for the 10 pairs are 180 with a dd right now of 220. Every time I lose with a pair I eliminate it.   
>    
>  Siobi, had 6 trades with r9 for +7 profit over the 10 pairs and was in a dd of 60 when I switched back to your r8.
> 
> Ignored

  
Siobi:  
  
* Eur/jpy opened a long on **April 2** , price 0.9151  
* Eur/jpy opened a long on **April 3** , price 0.9151  
  
It had 2 longs at the same time which closed out at -148 ignoring my 100sl. Did something different with eur/aud but the sl worked on that one. I think the ea got confused or I'm confused. So I turned a +300 account into a -200 because I traded thru the news. This is the first news day to get me. I'm using r8, did anyone trade thru the NFP, if so how did you do and either r8 or r9? 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: 1.gif
Size: 36 KB](/attachment/image/228452/thumbnail?d=1365567113)](/attachment/image/228452?d=1238767918)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#410](/thread/post/2650120#post2650120 "Post Permalink")

  * Apr 4, 2009 12:37am  Apr 4, 2009 12:37am 

  * [ paradoxical](paradoxical)

  * | Joined Nov 2007  | Status: Trader | [1,186 Posts](/search?do=process&provider=Member&searchuser=54706)

I turned the EA off last night. No way to know what would have happened, so no trade = no loss. There's always another day. Yesterday afternoon, the R8 picked up 13 PIPS on a sell trade. Still in the minus, though, due to a 100 PIP loss a few days back. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#411](/thread/post/2650427#post2650427 "Post Permalink")

  * Apr 4, 2009 3:52am  Apr 4, 2009 3:52am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar94654_2.gif) walrus_78](walrus_78)

  * | Joined Feb 2009  | Status: Trader | [19 Posts](/search?do=process&provider=Member&searchuser=94654)

today one trade with r9, 1 pip profit in EurUsd 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#412](/thread/post/2650476#post2650476 "Post Permalink")

  * Apr 4, 2009 4:25am  Apr 4, 2009 4:25am 

  * [ Orenn](orenn)

  * | Joined Mar 2009  | Status: Trader | [11 Posts](/search?do=process&provider=Member&searchuser=96427)

> [Quoting qz10cq](/thread/post/2649935#post2649935 "View Quoted Post")
> 
> Disliked
> 
> Siobi:  
>    
>  * Eur/jpy opened a long on **April 2** , price 0.9151  
>  * Eur/jpy opened a long on **April 3** , price 0.9151  
>    
>  It had 2 longs at the same time which closed out at -148 ignoring my 100sl. Did something different with eur/aud but the sl worked on that one. I think the ea got confused or I'm confused. So I turned a +300 account into a -200 because I traded thru the news. This is the first news day to get me. I'm using r8, did anyone trade thru the NFP, if so how did you do and either r8 or r9?
> 
> Ignored

qz10cq,  
  
First you probably mean Eur/Gbp and not Eur/Jpy...  
Second your 100 pips sl was not ignored (you exited on 0.9051 ) just that in this pair each pip is ~1.5 times a eur/usd pip  
I have eur/gbp only on R9 demo and no trades were taken there so I cant help you on this one  
  
Oren 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#413](/thread/post/2650745#post2650745 "Post Permalink")

  * Apr 4, 2009 8:35am  Apr 4, 2009 8:35am 

  * [ qz10cq](qz10cq)

  * | Joined Dec 2006  | Status: Trader | [303 Posts](/search?do=process&provider=Member&searchuser=29720)

> [Quoting Orenn](/thread/post/2650476#post2650476 "View Quoted Post")
> 
> Disliked
> 
> qz10cq,  
>    
>  First you probably mean Eur/Gbp and not Eur/Jpy...  
>  Second your 100 pips sl was not ignored (you exited on 0.9051 ) just that in this pair each pip is ~1.5 times a eur/usd pip  
>  I have eur/gbp only on R9 demo and no trades were taken there so I cant help you on this one  
>    
>  Oren
> 
> Ignored

Thanks Oren, your right, eur/gbp and sl did take me out right were it was suppose to. You took away half of my confusion , how about the 2 entries at the same time? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#414](/thread/post/2650792#post2650792 "Post Permalink")

  * Apr 4, 2009 10:25am  Apr 4, 2009 10:25am 

  * [ caputoe](caputoe)

  * | Joined Feb 2009  | Status: Trader | [14 Posts](/search?do=process&provider=Member&searchuser=92673)

Wonder if someone can help me.  
  
I installed the FX_30M_Bouncing_V104_R9 EA onto my MT4 platform last Sunday evening and it has not made one trade as yet.  
  
I have a smiley face on the 30M EUR/USD chart it's attached to; when I select "properties" on the EA, the common tab has all outside boxes checked; the EA button on the MT4 platform is clicked in; and the journal says the EA loaded successfully.  
  
Any ideas on why no trades ?  
  
Appreciate the help. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#415](/thread/post/2650834#post2650834 "Post Permalink")

  * Apr 4, 2009 12:24pm  Apr 4, 2009 12:24pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83889_5.gif) siobi](siobi)

  * | Joined Oct 2008  | Status: Trader | [717 Posts](/search?do=process&provider=Member&searchuser=83889)

hi all,  
looks great for EU pair...  
  
I tweak abit of the setting here at my R9 and guess what? ...  
  
  
I lose 100 pip....  
  
damn.... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#416](/thread/post/2650835#post2650835 "Post Permalink")

  * Apr 4, 2009 12:25pm  Apr 4, 2009 12:25pm 

  * [ adsanders](adsanders)

  * | Joined May 2007  | Status: Trader | [137 Posts](/search?do=process&provider=Member&searchuser=40067)

I have read the entire thread and I am really impressed. I am going to test out this EA and have downloaded the files I need including the latest r9 version but where can I find the previous version v104r8? I would like to test this one as well.  
  
Thanks to Siobi for creating this EA and also for every one elses input to this thread. ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#417](/thread/post/2650908#post2650908 "Post Permalink")

  * Apr 4, 2009 3:59pm  Apr 4, 2009 3:59pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83889_5.gif) siobi](siobi)

  * | Joined Oct 2008  | Status: Trader | [717 Posts](/search?do=process&provider=Member&searchuser=83889)

guys, remember to set the Num_of_digit to TRUE when trade using 5 digit platform 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#418](/thread/post/2651439#post2651439 "Post Permalink")

  * Apr 5, 2009 9:35am  Apr 5, 2009 9:35am 

  * [ caputoe](caputoe)

  * | Joined Feb 2009  | Status: Trader | [14 Posts](/search?do=process&provider=Member&searchuser=92673)

Please read back a few posts to #414; anyone know why I haven't gotten any trades ?  
  
Thanks. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#419](/thread/post/2651510#post2651510 "Post Permalink")

  * Apr 5, 2009 12:28pm  Apr 5, 2009 12:28pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83889_5.gif) siobi](siobi)

  * | Joined Oct 2008  | Status: Trader | [717 Posts](/search?do=process&provider=Member&searchuser=83889)

> [Quoting caputoe](/thread/post/2651439#post2651439 "View Quoted Post")
> 
> Disliked
> 
> Please read back a few posts to #414; anyone know why I haven't gotten any trades ?  
>    
>  Thanks.
> 
> Ignored

if yuo turn on for 24 hours, it shuld be opened 1 trade. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#420](/thread/post/2651692#post2651692 "Post Permalink")

  * Edited 9:33pm  Apr 5, 2009 7:56pm | Edited 9:33pm 

  * [ qz10cq](qz10cq)

  * | Joined Dec 2006  | Status: Trader | [303 Posts](/search?do=process&provider=Member&searchuser=29720)

> [Quoting adsanders](/thread/post/2650835#post2650835 "View Quoted Post")
> 
> Disliked
> 
> I have read the entire thread and I am really impressed. I am going to test out this EA and have downloaded the files I need including the latest r9 version but where can I find the previous version v104r8? I would like to test this one as well.  
>    
>  Thanks to Siobi for creating this EA and also for every one elses input to this thread. ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)
> 
> Ignored

There's a paper clip at the top of the pages next to the page numbers, click on that and all attachments for that thread comes up. I think that paper clip right now says 61. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * FX_30M Bouncing System
  *   * [ **Reply to Thread** ](/thread/157406-fx30m-bouncing-system/reply#reply)

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

[The Bouncing Pip](/thread/88277-the-bouncing-pip "Hi everyone. 
 
I present to you a system called &quot;The Bouncing Pip&quot; 
 
This is a system that was originally developed by BigBear, so full...") 26 replies

[Price bouncing off of sma](/thread/228922-price-bouncing-off-of-sma "What is the logic behind a price bouncing off an SMA? 
 
For example if a price bounces of a 35 day sma, i should short it if bounces of...") 2 replies

[Developing a correlated bouncing system](/thread/158016-developing-a-correlated-bouncing-system "The above indicator is a simple ma indicator with the weekly ma set to 40. 
 
I like most of my bouncing signals to be in the direction of...") 9 replies

[bouncing candle indicator](/thread/105826-bouncing-candle-indicator "I once had an indicator that would  send  off an alert whenever a candle touched back on its  moving average.  Lost it somehow, but I do...") 0 replies

[Price bouncing off support or resistance,your thoughts](/thread/30984-price-bouncing-off-support-or-resistanceyour-thoughts "I would like to start a discussuion about price movement at support/resistance, Fib and pivot levels.  
  
Time and again I see the price...") 11 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/157406-fx30m-bouncing-system/reply#reply)
  * Subscribe
  * [72](javascript:void\(0\);)

Attachments: FX_30M Bouncing System

Tags: FX_30M Bouncing System

#  [](/thread/157406-fx30m-bouncing-system)FX_30M Bouncing System 

  * 

  * [#421](/thread/post/2652060#post2652060 "Post Permalink")

  * Apr 6, 2009 4:39am  Apr 6, 2009 4:39am 

  * [ adsanders](adsanders)

  * | Joined May 2007  | Status: Trader | [137 Posts](/search?do=process&provider=Member&searchuser=40067)

Thanks qz10cq! ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#422](/thread/post/2652340#post2652340 "Post Permalink")

  * Apr 6, 2009 8:48am  Apr 6, 2009 8:48am 

  * [ caputoe](caputoe)

  * | Joined Feb 2009  | Status: Trader | [14 Posts](/search?do=process&provider=Member&searchuser=92673)

Siobi,  
  
I have had my MT4 platform opened 24/5 all week and still no trades. Can you please send me all of the indicator files as I think that may be the problem,  
  
Thanks. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#423](/thread/post/2652998#post2652998 "Post Permalink")

  * Apr 6, 2009 5:10pm  Apr 6, 2009 5:10pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83889_5.gif) siobi](siobi)

  * | Joined Oct 2008  | Status: Trader | [717 Posts](/search?do=process&provider=Member&searchuser=83889)

hi there,  
all indicator is defaulted in all mq4 platform.... ![](https://resources.faireconomy.media/images/emojis/64/1f61c.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#424](/thread/post/2656778#post2656778 "Post Permalink")

  * Apr 8, 2009 6:17am  Apr 8, 2009 6:17am 

  * [ paradoxical](paradoxical)

  * | Joined Nov 2007  | Status: Trader | [1,186 Posts](/search?do=process&provider=Member&searchuser=54706)

Where did everyone go? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#425](/thread/post/2656908#post2656908 "Post Permalink")

  * Apr 8, 2009 7:56am  Apr 8, 2009 7:56am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83889_5.gif) siobi](siobi)

  * | Joined Oct 2008  | Status: Trader | [717 Posts](/search?do=process&provider=Member&searchuser=83889)

letting the EA runs... so everybody is sleeping...... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#426](/thread/post/2660730#post2660730 "Post Permalink")

  * Apr 9, 2009 10:52pm  Apr 9, 2009 10:52pm 

  * [ Dan Johnston](dan*johnston)

  * | Joined May 2008  | Status: Trader | [354 Posts](/search?do=process&provider=Member&searchuser=69420)

Hi Siobi.  
  
Have a look at the following - courtesy of Paulus - and maybe you can incorporate it into the ea if you think it worthwhile.   
  
(Makes an interesting combination with BBand stops bar indicator.) 

Attached File(s)

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [1nonlagdot.mq4](/attachment/file/231151?d=1239284974) 5 KB | 226 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#427](/thread/post/2660881#post2660881 "Post Permalink")

  * Apr 9, 2009 11:59pm  Apr 9, 2009 11:59pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar95566_5.gif) stifland](stifland)

  * | Joined Mar 2009  | Status: Trader | [304 Posts](/search?do=process&provider=Member&searchuser=95566)

Hi guys just checking in. Never gotten a signal since changing to r9. anyone else have it fire?  
billy 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#428](/thread/post/2660913#post2660913 "Post Permalink")

  * Apr 10, 2009 12:10am  Apr 10, 2009 12:10am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar43332_2.gif) willmalou](willmalou)

  * | Joined Jul 2007  | Status: Think before you act!!! | [113 Posts](/search?do=process&provider=Member&searchuser=43332)

I have had 3 trades this week with r9. 2 wins and 1 loss, default settings. Still like r8 better. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#429](/thread/post/2661354#post2661354 "Post Permalink")

  * Apr 10, 2009 3:19am  Apr 10, 2009 3:19am 

  * [ Dan Johnston](dan*johnston)

  * | Joined May 2008  | Status: Trader | [354 Posts](/search?do=process&provider=Member&searchuser=69420)

Paper traded the alert version of the nonlagdots indicator today, and it did an amazing job!!!  
Just stay out of sideways consolidation periods (constricted bollingers).  
  
Definitely worth looking at!![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)  
  
If anyone wants the alert version I'll post it.  
  
r8 had 6 trades for a total of -50 pips.  
r9 had one trade for a total of +1 pip. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#430](/thread/post/2661750#post2661750 "Post Permalink")

  * Apr 10, 2009 6:50am  Apr 10, 2009 6:50am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar92141_5.gif) tex](tex)

  * | Joined Jan 2009  | Status: Trader | [272 Posts](/search?do=process&provider=Member&searchuser=92141)

hello dan,   
  
please post that indicator, i want to test it too.   
  
many thanks,  
tex 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#431](/thread/post/2661771#post2661771 "Post Permalink")

  * Apr 10, 2009 7:17am  Apr 10, 2009 7:17am 

  * [ Dan Johnston](dan*johnston)

  * | Joined May 2008  | Status: Trader | [354 Posts](/search?do=process&provider=Member&searchuser=69420)

> [Quoting tex](/thread/post/2661750#post2661750 "View Quoted Post")
> 
> Disliked
> 
> hello dan,   
>    
>  please post that indicator, i want to test it too.   
>    
>  many thanks,  
>  tex
> 
> Ignored

Enjoy guys.  
  
Also the following link is interesting.  
  
<http://www.forex-tsd.com/128022-post1027.html>

Attached File(s)

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [nonlagdotalert.mq4](/attachment/file/231353?d=1239315326) 5 KB | 250 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#432](/thread/post/2661807#post2661807 "Post Permalink")

  * Apr 10, 2009 7:56am  Apr 10, 2009 7:56am 

  * [ Dan Johnston](dan*johnston)

  * | Joined May 2008  | Status: Trader | [354 Posts](/search?do=process&provider=Member&searchuser=69420)

Just found the ea that utilized the above indicator. Maybe we (Siobi) can improve upon the code of the ea below. (The posted forward test looks very promising, but I don't know what became of it.)  
  
Perhaps we should revisit that KusKus ea. Does anyone have any experience with it?  
  
<http://www.forex-tsd.com/253218-post1969.html>

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#433](/thread/post/2661816#post2661816 "Post Permalink")

  * Edited 8:30am  Apr 10, 2009 8:18am | Edited 8:30am 

  * [ Dan Johnston](dan*johnston)

  * | Joined May 2008  | Status: Trader | [354 Posts](/search?do=process&provider=Member&searchuser=69420)

And Siobi, since you are a coder, you may find the following interesting:  
  
[http://www.forex-tsd.com/expert-advi...-kuskus-i.html](http://www.forex-tsd.com/expert-advisors-metatrader-4/13796-isakas-ashi-kuskus-i.html)  
  
**Edit:** Just read the last page and it seems it died on the vine, although it had a good run when you look at the forward test they did. I still like the above indicator. It helps me to stay in the trend without getting out too soon, like I usually do. ...Today anyway.![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#434](/thread/post/2662236#post2662236 "Post Permalink")

  * Apr 10, 2009 2:42pm  Apr 10, 2009 2:42pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83889_5.gif) siobi](siobi)

  * | Joined Oct 2008  | Status: Trader | [717 Posts](/search?do=process&provider=Member&searchuser=83889)

dan,  
can you post it here? I mean the zip file together with all those password?  
  
I'm lazy to register an acct there........![](https://resources.faireconomy.media/images/emojis/64/1f61c.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#435](/thread/post/2662612#post2662612 "Post Permalink")

  * Edited 10:23pm  Apr 10, 2009 10:12pm | Edited 10:23pm 

  * [ Dan Johnston](dan*johnston)

  * | Joined May 2008  | Status: Trader | [354 Posts](/search?do=process&provider=Member&searchuser=69420)

I wasn't able to access the demo acct. but here is the old info anyway:  
  
Broker: **FXDD**  
Login: **5435342**  
Password: **tr7zpkg**

Attached File(s)

![File Type: zip](https://assets.faireconomy.media/images/attach/zip.gif) [Isakas Kuskus I.zip](/attachment/file/231528?d=1239369099) 12 KB | 267 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#436](/thread/post/2663020#post2663020 "Post Permalink")

  * Apr 11, 2009 3:15am  Apr 11, 2009 3:15am 

  * [ Dan Johnston](dan*johnston)

  * | Joined May 2008  | Status: Trader | [354 Posts](/search?do=process&provider=Member&searchuser=69420)

Did a little backtesting on the KusKus and very disappointing.  
  
Took an excellent first demo entry sell, and then proceeded to lose the 9 pips that it gained initially with 1 pip drawdown. Then took another sell in a weak uprend and then I closed both at -16.  
  
Was hoping for it to take good entries that I can babysit, but that second sell turned me off.  
  
Optimization was not very successful so far... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#437](/thread/post/2663168#post2663168 "Post Permalink")

  * Apr 11, 2009 5:00am  Apr 11, 2009 5:00am 

  * [ Dan Johnston](dan*johnston)

  * | Joined May 2008  | Status: Trader | [354 Posts](/search?do=process&provider=Member&searchuser=69420)

Nice trade on r8, but had a 100 pip stop the other day. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: 4 10 09r8.gif
Size: 49 KB](/attachment/image/231626/thumbnail?d=1365567765)](/attachment/image/231626?d=1239393617)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#438](/thread/post/2663304#post2663304 "Post Permalink")

  * Apr 11, 2009 9:46am  Apr 11, 2009 9:46am 

  * [ tropheus](tropheus)

  * | Joined Mar 2009  | Status: Trader | [49 Posts](/search?do=process&provider=Member&searchuser=98184)

I am having problems with alpari uk 5 digit 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#439](/thread/post/2663912#post2663912 "Post Permalink")

  * Apr 12, 2009 8:02am  Apr 12, 2009 8:02am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar98196_4.gif) khaos420](khaos420)

  * | Joined Mar 2009  | Status: Trader | [17 Posts](/search?do=process&provider=Member&searchuser=98196)

Great System, siobi !! and thank you for sharing for free ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
  
Here is something I discover:  
  
When I add Langueree Indicator into the chart I notice that almost all the big moves occur in the Overbought(LG>0.8) and Oversold(LG<0.2)area  
  
The big Down/Up move tend to be the last down/up move that make the LG leave the overbought/oversold) area. Those moves tend to last for 100-200pips with down risks around 35 pips, thus they have an excellent risk/reward ratio.   
  
if we can locate these "last wave" we can find the ultimate low risk/ high probability profit opports. I have tried several indicators but still with no good results  
  
here is some pics and the LG indicator, set as following:  
gamma = 0.9  
countbars= 950000  
  
Any ideas? 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: p01.jpg
Size: 140 KB](/attachment/image/231865/thumbnail?d=1365567798)](/attachment/image/231865?d=1239490826)   
[![Click to Enlarge

Name: p02.jpg
Size: 137 KB](/attachment/image/231866/thumbnail?d=1365567798)](/attachment/image/231866?d=1239490826)   

Attached File(s)

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [Laguerre.mq4](/attachment/file/231867?d=1239490846) 3 KB | 254 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#440](/thread/post/2664299#post2664299 "Post Permalink")

  * Apr 12, 2009 9:29pm  Apr 12, 2009 9:29pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83889_5.gif) siobi](siobi)

  * | Joined Oct 2008  | Status: Trader | [717 Posts](/search?do=process&provider=Member&searchuser=83889)

hi all IBFX is going to be 5 digit platform...  
please spare me to have a week of testing before releasing R9 for 5 digit platform...  
  
  
  
thanks...  
  
and for the laguarre indicator... I'll also take a look into it....  
  
new version of R10 will be release for   
1) 5 digit  
2) Laguarre  
  
guys... for R9 to R10, I'll try to advise on the optimise setting... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * FX_30M Bouncing System
  *   * [ **Reply to Thread** ](/thread/157406-fx30m-bouncing-system/reply#reply)

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

[The Bouncing Pip](/thread/88277-the-bouncing-pip "Hi everyone. 
 
I present to you a system called &quot;The Bouncing Pip&quot; 
 
This is a system that was originally developed by BigBear, so full...") 26 replies

[Price bouncing off of sma](/thread/228922-price-bouncing-off-of-sma "What is the logic behind a price bouncing off an SMA? 
 
For example if a price bounces of a 35 day sma, i should short it if bounces of...") 2 replies

[Developing a correlated bouncing system](/thread/158016-developing-a-correlated-bouncing-system "The above indicator is a simple ma indicator with the weekly ma set to 40. 
 
I like most of my bouncing signals to be in the direction of...") 9 replies

[bouncing candle indicator](/thread/105826-bouncing-candle-indicator "I once had an indicator that would  send  off an alert whenever a candle touched back on its  moving average.  Lost it somehow, but I do...") 0 replies

[Price bouncing off support or resistance,your thoughts](/thread/30984-price-bouncing-off-support-or-resistanceyour-thoughts "I would like to start a discussuion about price movement at support/resistance, Fib and pivot levels.  
  
Time and again I see the price...") 11 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/157406-fx30m-bouncing-system/reply#reply)
  * Subscribe
  * [72](javascript:void\(0\);)

Attachments: FX_30M Bouncing System

Tags: FX_30M Bouncing System

#  [](/thread/157406-fx30m-bouncing-system)FX_30M Bouncing System 

  * 

  * [#441](/thread/post/2664743#post2664743 "Post Permalink")

  * Apr 13, 2009 7:37am  Apr 13, 2009 7:37am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar95566_5.gif) stifland](stifland)

  * | Joined Mar 2009  | Status: Trader | [304 Posts](/search?do=process&provider=Member&searchuser=95566)

i am again trying 100,100,20 on r9. So far, it has never opened a trade. Could this be because i used r8 template. removed r8 and place r9 on this tpl? wouldn't think so. will keep informed. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#442](/thread/post/2664793#post2664793 "Post Permalink")

  * Apr 13, 2009 8:52am  Apr 13, 2009 8:52am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83889_5.gif) siobi](siobi)

  * | Joined Oct 2008  | Status: Trader | [717 Posts](/search?do=process&provider=Member&searchuser=83889)

maybe is the PSARFac setting...  
  
it is defaulted to be 60...  
  
you may change it to 30...  
  
what is this about...?  
  
actually it is used to compare the PSAR different...  
  
the bigger the gap, means the bigger the reversal of the trend.... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#443](/thread/post/2665169#post2665169 "Post Permalink")

  * Apr 13, 2009 4:35pm  Apr 13, 2009 4:35pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83889_5.gif) siobi](siobi)

  * | Joined Oct 2008  | Status: Trader | [717 Posts](/search?do=process&provider=Member&searchuser=83889)

![](https://resources.faireconomy.media/images/emojis/64/1f61c.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#444](/thread/post/2665583#post2665583 "Post Permalink")

  * Apr 13, 2009 10:14pm  Apr 13, 2009 10:14pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar95566_5.gif) stifland](stifland)

  * | Joined Mar 2009  | Status: Trader | [304 Posts](/search?do=process&provider=Member&searchuser=95566)

Rp opened trade at 3190, stopped out at 3191 for +1. so small win but at least I know its working now. did change psar to 30 so maybe that was it siobi. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#445](/thread/post/2665753#post2665753 "Post Permalink")

  * Apr 13, 2009 11:31pm  Apr 13, 2009 11:31pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83889_5.gif) siobi](siobi)

  * | Joined Oct 2008  | Status: Trader | [717 Posts](/search?do=process&provider=Member&searchuser=83889)

TP 20 pip to ensure winning 20 pip per day.that is my strategy...today a total win of 30 pip...wonderfull day... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#446](/thread/post/2665908#post2665908 "Post Permalink")

  * Apr 14, 2009 12:30am  Apr 14, 2009 12:30am 

  * [ tropheus](tropheus)

  * | Joined Mar 2009  | Status: Trader | [49 Posts](/search?do=process&provider=Member&searchuser=98184)

> [Quoting siobi](/thread/post/2665753#post2665753 "View Quoted Post")
> 
> Disliked
> 
> TP 20 pip to ensure winning 20 pip per day.that is my strategy...today a total win of 30 pip...wonderfull day...
> 
> Ignored

Hi iam having problems getting this to take trades on alpari uk mini and insta trader did every thing on 1 post 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#447](/thread/post/2666011#post2666011 "Post Permalink")

  * Edited 1:22am  Apr 14, 2009 1:07am | Edited 1:22am 

  * [ Dan Johnston](dan*johnston)

  * | Joined May 2008  | Status: Trader | [354 Posts](/search?do=process&provider=Member&searchuser=69420)

> [Quoting siobi](/thread/post/2665753#post2665753 "View Quoted Post")
> 
> Disliked
> 
> TP 20 pip to ensure winning 20 pip per day.that is my strategy...today a total win of 30 pip...wonderfull day...
> 
> Ignored

Hi Siobi. What is your total pips with this version and the psarfac at 30?  
  
Thanks.  
  
Had the following with psar at 60. Now changed it to 30. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: 4 13 09 r9.gif
Size: 67 KB](/attachment/image/232338/thumbnail?d=1365567900)](/attachment/image/232338?d=1239639740)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#448](/thread/post/2666082#post2666082 "Post Permalink")

  * Apr 14, 2009 1:47am  Apr 14, 2009 1:47am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar95566_5.gif) stifland](stifland)

  * | Joined Mar 2009  | Status: Trader | [304 Posts](/search?do=process&provider=Member&searchuser=95566)

> [Quoting siobi](/thread/post/2665753#post2665753 "View Quoted Post")
> 
> Disliked
> 
> TP 20 pip to ensure winning 20 pip per day.that is my strategy...today a total win of 30 pip...wonderfull day...
> 
> Ignored

  
OK, well I am letting EA run untouched to get some sense of results that we would get. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#449](/thread/post/2666749#post2666749 "Post Permalink")

  * Apr 14, 2009 7:43am  Apr 14, 2009 7:43am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83889_5.gif) siobi](siobi)

  * | Joined Oct 2008  | Status: Trader | [717 Posts](/search?do=process&provider=Member&searchuser=83889)

20 pip TP still will be my strategy...  
  
I'm running  
10 pip step pip.  
15 pip trailing  
20 pip tp  
100 pip SL. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#450](/thread/post/2671252#post2671252 "Post Permalink")

  * Apr 16, 2009 1:53am  Apr 16, 2009 1:53am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar95566_5.gif) stifland](stifland)

  * | Joined Mar 2009  | Status: Trader | [304 Posts](/search?do=process&provider=Member&searchuser=95566)

I don't know what step pip is but. I am running SL at 100, TP at 100 and trail at 20.  
I entered Short at 1.3187 it got as low as 45 and reversed and gained 1 pip again. now question is after 20 pips shouldn't trail stay 20 pips back and exit would have been at 3265?? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#451](/thread/post/2671444#post2671444 "Post Permalink")

  * Apr 16, 2009 3:16am  Apr 16, 2009 3:16am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar95566_5.gif) stifland](stifland)

  * | Joined Mar 2009  | Status: Trader | [304 Posts](/search?do=process&provider=Member&searchuser=95566)

system is long 3230 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#452](/thread/post/2671854#post2671854 "Post Permalink")

  * Apr 16, 2009 6:45am  Apr 16, 2009 6:45am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar98196_4.gif) khaos420](khaos420)

  * | Joined Mar 2009  | Status: Trader | [17 Posts](/search?do=process&provider=Member&searchuser=98196)

A Quick Question:  
  
How did you guys add fancy avatar pic to your profile? ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#453](/thread/post/2672146#post2672146 "Post Permalink")

  * Apr 16, 2009 9:59am  Apr 16, 2009 9:59am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83889_5.gif) siobi](siobi)

  * | Joined Oct 2008  | Status: Trader | [717 Posts](/search?do=process&provider=Member&searchuser=83889)

> [Quoting stifland](/thread/post/2671252#post2671252 "View Quoted Post")
> 
> Disliked
> 
> I don't know what step pip is but. I am running SL at 100, TP at 100 and trail at 20.  
>  I entered Short at 1.3187 it got as low as 45 and reversed and gained 1 pip again. now question is after 20 pips shouldn't trail stay 20 pips back and exit would have been at 3265??
> 
> Ignored

hm... weird... but the EA should trail it without any problem...  
  
it works well at my NB running  
  
windows Vista Pro  
mt4 build 223  
ibfxmini live acct.  
  
not sure about your side..  
  
by the way, I'm always running 20tp, 15 TS and 100 SL. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#454](/thread/post/2672149#post2672149 "Post Permalink")

  * Apr 16, 2009 10:02am  Apr 16, 2009 10:02am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83889_5.gif) siobi](siobi)

  * | Joined Oct 2008  | Status: Trader | [717 Posts](/search?do=process&provider=Member&searchuser=83889)

> [Quoting stifland](/thread/post/2671444#post2671444 "View Quoted Post")
> 
> Disliked
> 
> system is long 3230
> 
> Ignored

u should be taking ur profit at 20 pip by the time I type this message...  
  
yet another sweet 20 pip in pocket... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#455](/thread/post/2672152#post2672152 "Post Permalink")

  * Apr 16, 2009 10:05am  Apr 16, 2009 10:05am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83889_5.gif) siobi](siobi)

  * | Joined Oct 2008  | Status: Trader | [717 Posts](/search?do=process&provider=Member&searchuser=83889)

> [Quoting khaos420](/thread/post/2671854#post2671854 "View Quoted Post")
> 
> Disliked
> 
> A Quick Question:  
>    
>  How did you guys add fancy avatar pic to your profile? ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)
> 
> Ignored

fancy avatar?  
  
go check at your control panel... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#456](/thread/post/2672191#post2672191 "Post Permalink")

  * Apr 16, 2009 10:34am  Apr 16, 2009 10:34am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar95566_5.gif) stifland](stifland)

  * | Joined Mar 2009  | Status: Trader | [304 Posts](/search?do=process&provider=Member&searchuser=95566)

Got it Siobi! sweet 20. I may change settings to match yours, but i want the big winner![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
  
Trail was working so don't know why i got 1 pip on the other...mystery. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: +20trailstophit.gif
Size: 26 KB](/attachment/image/233617/thumbnail?d=1365568200)](/attachment/image/233617?d=1239845638)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#457](/thread/post/2672629#post2672629 "Post Permalink")

  * Apr 16, 2009 3:31pm  Apr 16, 2009 3:31pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83889_5.gif) siobi](siobi)

  * | Joined Oct 2008  | Status: Trader | [717 Posts](/search?do=process&provider=Member&searchuser=83889)

tell you... 20 pip per day... soon u will be very rich.... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#458](/thread/post/2673417#post2673417 "Post Permalink")

  * Apr 16, 2009 10:12pm  Apr 16, 2009 10:12pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar98196_4.gif) khaos420](khaos420)

  * | Joined Mar 2009  | Status: Trader | [17 Posts](/search?do=process&provider=Member&searchuser=98196)

Sweat! got the avatar uploaded ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
  
Siobi, I got another question:  
  
the slop direction line does not repaint, right?  
  
and also, does it changes color when the current bar is not complete? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#459](/thread/post/2673899#post2673899 "Post Permalink")

  * Apr 17, 2009 1:12am  Apr 17, 2009 1:12am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar95566_5.gif) stifland](stifland)

  * | Joined Mar 2009  | Status: Trader | [304 Posts](/search?do=process&provider=Member&searchuser=95566)

Si, Do you have slope check and ma check False?  
  

> [Quoting siobi](/thread/post/2672629#post2672629 "View Quoted Post")
> 
> Disliked
> 
> tell you... 20 pip per day... soon u will be very rich....
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#460](/thread/post/2674164#post2674164 "Post Permalink")

  * Apr 17, 2009 3:21am  Apr 17, 2009 3:21am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar98771_9.gif) enewbold](enewbold)

  * | Joined Apr 2009  | Status: Trader | [276 Posts](/search?do=process&provider=Member&searchuser=98771)

I'm kinda new at this stuff, and have never installed or run an EA, so please bear with me. The way I understand it is that I have to download and install (copy to right subdirectories) all of the EAs and scripts associated with this FX-30 EA? Also the .tpl file?  
  
Thanks,  
Ed 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * FX_30M Bouncing System
  *   * [ **Reply to Thread** ](/thread/157406-fx30m-bouncing-system/reply#reply)

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

[The Bouncing Pip](/thread/88277-the-bouncing-pip "Hi everyone. 
 
I present to you a system called &quot;The Bouncing Pip&quot; 
 
This is a system that was originally developed by BigBear, so full...") 26 replies

[Price bouncing off of sma](/thread/228922-price-bouncing-off-of-sma "What is the logic behind a price bouncing off an SMA? 
 
For example if a price bounces of a 35 day sma, i should short it if bounces of...") 2 replies

[Developing a correlated bouncing system](/thread/158016-developing-a-correlated-bouncing-system "The above indicator is a simple ma indicator with the weekly ma set to 40. 
 
I like most of my bouncing signals to be in the direction of...") 9 replies

[bouncing candle indicator](/thread/105826-bouncing-candle-indicator "I once had an indicator that would  send  off an alert whenever a candle touched back on its  moving average.  Lost it somehow, but I do...") 0 replies

[Price bouncing off support or resistance,your thoughts](/thread/30984-price-bouncing-off-support-or-resistanceyour-thoughts "I would like to start a discussuion about price movement at support/resistance, Fib and pivot levels.  
  
Time and again I see the price...") 11 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/157406-fx30m-bouncing-system/reply#reply)
  * Subscribe
  * [72](javascript:void\(0\);)

Attachments: FX_30M Bouncing System

Tags: FX_30M Bouncing System

#  [](/thread/157406-fx30m-bouncing-system)FX_30M Bouncing System 

  * 

  * [#461](/thread/post/2675285#post2675285 "Post Permalink")

  * Apr 17, 2009 1:14pm  Apr 17, 2009 1:14pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83889_5.gif) siobi](siobi)

  * | Joined Oct 2008  | Status: Trader | [717 Posts](/search?do=process&provider=Member&searchuser=83889)

> [Quoting stifland](/thread/post/2673899#post2673899 "View Quoted Post")
> 
> Disliked
> 
> Si, Do you have slope check and ma check False?
> 
> Ignored

  
both setting set to FALSE.  
  
to enewbold,  
just load the EA in... thats it..  
  
to khaos420,  
slope line will always repaint for the previous BAR !!! becarefull... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#462](/thread/post/2676230#post2676230 "Post Permalink")

  * Apr 17, 2009 10:00pm  Apr 17, 2009 10:00pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar98196_4.gif) khaos420](khaos420)

  * | Joined Mar 2009  | Status: Trader | [17 Posts](/search?do=process&provider=Member&searchuser=98196)

> [Quoting siobi](/thread/post/2675285#post2675285 "View Quoted Post")
> 
> Disliked
> 
> both setting set to FALSE.  
>    
>  to enewbold,  
>  just load the EA in... thats it..  
>    
>  to khaos420,  
>  slope line will always repaint for the previous BAR !!! becarefull...
> 
> Ignored

  
  
siobi, thank you for the quick reply but I don't know exactly what you mean:  
  
does SDL repaint everything showing previously on the graph, or just currently unfinished bar? and when you say repaint, do you mean changing of the position or just changing of color?? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#463](/thread/post/2677479#post2677479 "Post Permalink")

  * Apr 18, 2009 12:50pm  Apr 18, 2009 12:50pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83889_5.gif) siobi](siobi)

  * | Joined Oct 2008  | Status: Trader | [717 Posts](/search?do=process&provider=Member&searchuser=83889)

hi there,  
  
for eg:  
Bar no 100, SDL shows blue, then at Bar 101, SDL shows RED due to price drops... then later you will notice during Bar 102 time, Bar 100 change from Blue to RED and bar 101 remains RED.  
  
it repaints !!! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#464](/thread/post/2678089#post2678089 "Post Permalink")

  * Apr 19, 2009 7:21am  Apr 19, 2009 7:21am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar98196_4.gif) khaos420](khaos420)

  * | Joined Mar 2009  | Status: Trader | [17 Posts](/search?do=process&provider=Member&searchuser=98196)

> [Quoting siobi](/thread/post/2677479#post2677479 "View Quoted Post")
> 
> Disliked
> 
> hi there,  
>    
>  for eg:  
>  Bar no 100, SDL shows blue, then at Bar 101, SDL shows RED due to price drops... then later you will notice during Bar 102 time, Bar 100 change from Blue to RED and bar 101 remains RED.  
>    
>  it repaints !!!
> 
> Ignored

  
Gaaaaaaaaaaaaaaaahh!!  
  
Thats too bad, but thanks for the explanation ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)  
  
siobi, do you find the Langueree useful for your system? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#465](/thread/post/2678699#post2678699 "Post Permalink")

  * Apr 20, 2009 12:36am  Apr 20, 2009 12:36am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83889_5.gif) siobi](siobi)

  * | Joined Oct 2008  | Status: Trader | [717 Posts](/search?do=process&provider=Member&searchuser=83889)

hm.......  
Lag seems not helpful for this system...  
  
anyway, I found it usefull in Hit system 5M EU...  
  
16EMA+48EMA +Lag+Confirm5M  
  
great system...  
  
Custom indicator  
1) 2MA crossover  
2) Laguerre  
3) Confirm5M  
  
EMA  
1) 16EMA, Typical Price  
2) 48EMA, Typical Price  
  
will explain later in another new thread....  
got to sleep.... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#466](/thread/post/2679825#post2679825 "Post Permalink")

  * Apr 20, 2009 1:13pm  Apr 20, 2009 1:13pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar71385_1.gif) alpine4133](alpine4133)

  * | Joined Jun 2008  | Status: Trader | [276 Posts](/search?do=process&provider=Member&searchuser=71385)

What do you mean:   
"additional configuration:  
this EA needs to be configure once a month to ensure we have good pip hunting."  
  
How do I reconfigure? What settings need to be reconfigured?  
  

Gary

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#467](/thread/post/2679959#post2679959 "Post Permalink")

  * Apr 20, 2009 2:28pm  Apr 20, 2009 2:28pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83889_5.gif) siobi](siobi)

  * | Joined Oct 2008  | Status: Trader | [717 Posts](/search?do=process&provider=Member&searchuser=83889)

hi there,  
I'll configure it once a month here.....   
  
and release to public every end of month.... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#468](/thread/post/2680873#post2680873 "Post Permalink")

  * Apr 20, 2009 9:16pm  Apr 20, 2009 9:16pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar95566_5.gif) stifland](stifland)

  * | Joined Mar 2009  | Status: Trader | [304 Posts](/search?do=process&provider=Member&searchuser=95566)

R9 entered 2962 short at 12:00. Trail stop hit for +1. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#469](/thread/post/2681017#post2681017 "Post Permalink")

  * Apr 20, 2009 10:16pm  Apr 20, 2009 10:16pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83889_5.gif) siobi](siobi)

  * | Joined Oct 2008  | Status: Trader | [717 Posts](/search?do=process&provider=Member&searchuser=83889)

ho wcan it happend?  
  
r u running on 30M TF? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#470](/thread/post/2681033#post2681033 "Post Permalink")

  * Apr 20, 2009 10:22pm  Apr 20, 2009 10:22pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar95566_5.gif) stifland](stifland)

  * | Joined Mar 2009  | Status: Trader | [304 Posts](/search?do=process&provider=Member&searchuser=95566)

Hope you can see little lines to analyze 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: shorrtrade.gif
Size: 21 KB](/attachment/image/235485/thumbnail?d=1365568588)](/attachment/image/235485?d=1240233761)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#471](/thread/post/2682360#post2682360 "Post Permalink")

  * Apr 21, 2009 8:33am  Apr 21, 2009 8:33am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83889_5.gif) siobi](siobi)

  * | Joined Oct 2008  | Status: Trader | [717 Posts](/search?do=process&provider=Member&searchuser=83889)

can u show me the screen shoot of your PSAR?  
  
I'm using 0.02 and 0.2.... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#472](/thread/post/2682513#post2682513 "Post Permalink")

  * Apr 21, 2009 9:34am  Apr 21, 2009 9:34am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar95566_5.gif) stifland](stifland)

  * | Joined Mar 2009  | Status: Trader | [304 Posts](/search?do=process&provider=Member&searchuser=95566)

.02 and 2 siobi 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#473](/thread/post/2682696#post2682696 "Post Permalink")

  * Apr 21, 2009 11:19am  Apr 21, 2009 11:19am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83889_5.gif) siobi](siobi)

  * | Joined Oct 2008  | Status: Trader | [717 Posts](/search?do=process&provider=Member&searchuser=83889)

oh... my fault....  
  
damn.. why my chart is 0.2 instead of 2?  
  
hm..... losing money because of this................... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#474](/thread/post/2682741#post2682741 "Post Permalink")

  * Apr 21, 2009 11:54am  Apr 21, 2009 11:54am 

  * [ deefar](deefar)

  * | Joined Apr 2007  | Status: Trader | [15 Posts](/search?do=process&provider=Member&searchuser=38196)

This EA seems to be a bit tricky. I am wondering if any of the people having difficulty getting this EA to trade were successful.  
I have read nearly all the posts here and am pretty sure I have it set correctly but it still won`t open any trades, I have installed the latest version and tried it on 1min, 15min & 30min.  
I am using IBFX demo which should be 5 digits now but still shows 4 only, my other IBFX demo shows 5 so I have tried it on both false & true for 2days on each and set for 24 hour aggressive trading. I will adjust some settings if and when I get it working but at this stage I`m not all that optimistic.  
I will try the platform update again and make sure the thing is the current build.  
Any suggestions or help would be greatly appreciated.  
  
deefar 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#475](/thread/post/2682767#post2682767 "Post Permalink")

  * Apr 21, 2009 12:16pm  Apr 21, 2009 12:16pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar83889_5.gif) siobi](siobi)

  * | Joined Oct 2008  | Status: Trader | [717 Posts](/search?do=process&provider=Member&searchuser=83889)

> [Quoting deefar](/thread/post/2682741#post2682741 "View Quoted Post")
> 
> Disliked
> 
> This EA seems to be a bit tricky. I am wondering if any of the people having difficulty getting this EA to trade were successful.  
>  I have read nearly all the posts here and am pretty sure I have it set correctly but it still won`t open any trades, I have installed the latest version and tried it on 1min, 15min & 30min.  
>  I am using IBFX demo which should be 5 digits now but still shows 4 only, my other IBFX demo shows 5 so I have tried it on both false & true for 2days on each and set for 24 hour aggressive trading. I will adjust some settings if and...
> 
> Ignored

  
hm...  
  
tricky huh...  
me too....  
  
ok... coz I'm running in Live, so no time to check on DEMO..  
  
will do it now... give me a minute.... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#476](/thread/post/2685370#post2685370 "Post Permalink")

  * Apr 22, 2009 6:00am  Apr 22, 2009 6:00am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar92484_4.gif) silverngold](silverngold)

  * | Joined Jan 2009  | Status: Veritas Vincit | [64 Posts](/search?do=process&provider=Member&searchuser=92484)

Hi Siobi,  
  
  
How are you doing?  
  
I was wondering, what ever happened to the FX 1m bouncing system?  
  
I tried using it, but it says that it "expired"?  
  
The FX 30m bouncing works pretty good.  
  
Thanks,  
  
Vincent 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#477](/thread/post/2685642#post2685642 "Post Permalink")

  * Apr 22, 2009 8:19am  Apr 22, 2009 8:19am 

  * [ deefar](deefar)

  * | Joined Apr 2007  | Status: Trader | [15 Posts](/search?do=process&provider=Member&searchuser=38196)

The EA finally took a trade for a 1 pip gain. That was 16 hours ago and nothing since. Does that sound normal?  
deefar 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#478](/thread/post/2685926#post2685926 "Post Permalink")

  * Apr 22, 2009 10:51am  Apr 22, 2009 10:51am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar98943_4.gif) Libernati156](libernati156)

  * | Membership Revoked  | Joined Apr 2009 | [5 Posts](/search?do=process&provider=Member&searchuser=98943)

Hi All:  
  
Have the current optimization settings been released yet for this EA? I've just set up v8 since everyone's results with v9 aren't as good as the first version.   
  
Thanks in advance. 

****************** ![](https://resources.faireconomy.media/images/emojis/64/1f918.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1) "The Answer to 1984 is 1776!!"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#479](/thread/post/2685929#post2685929 "Post Permalink")

  * Apr 22, 2009 10:53am  Apr 22, 2009 10:53am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar98943_4.gif) Libernati156](libernati156)

  * | Membership Revoked  | Joined Apr 2009 | [5 Posts](/search?do=process&provider=Member&searchuser=98943)

Hello Siobi;  
  
I'm a burgeoning computer programmer. I am interested in knowing where the best tutorial/training might be located for learning the metatrader programming language.   
  
Thanks in advance. 

****************** ![](https://resources.faireconomy.media/images/emojis/64/1f918.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1) "The Answer to 1984 is 1776!!"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#480](/thread/post/2686002#post2686002 "Post Permalink")

  * Apr 22, 2009 11:41am  Apr 22, 2009 11:41am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar95566_5.gif) stifland](stifland)

  * | Joined Mar 2009  | Status: Trader | [304 Posts](/search?do=process&provider=Member&searchuser=95566)

4 entries today. 3 all hit trail for +1. 1st one still in!  
May need to tweak pt and trail--just not sure yet. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: 4tradestoday.gif
Size: 26 KB](/attachment/image/236415/thumbnail?d=1365568775)](/attachment/image/236415?d=1240368085)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * FX_30M Bouncing System
  *   * [ **Reply to Thread** ](/thread/157406-fx30m-bouncing-system/reply#reply)

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

[The Bouncing Pip](/thread/88277-the-bouncing-pip "Hi everyone. 
 
I present to you a system called &quot;The Bouncing Pip&quot; 
 
This is a system that was originally developed by BigBear, so full...") 26 replies

[Price bouncing off of sma](/thread/228922-price-bouncing-off-of-sma "What is the logic behind a price bouncing off an SMA? 
 
For example if a price bounces of a 35 day sma, i should short it if bounces of...") 2 replies

[Developing a correlated bouncing system](/thread/158016-developing-a-correlated-bouncing-system "The above indicator is a simple ma indicator with the weekly ma set to 40. 
 
I like most of my bouncing signals to be in the direction of...") 9 replies

[bouncing candle indicator](/thread/105826-bouncing-candle-indicator "I once had an indicator that would  send  off an alert whenever a candle touched back on its  moving average.  Lost it somehow, but I do...") 0 replies

[Price bouncing off support or resistance,your thoughts](/thread/30984-price-bouncing-off-support-or-resistanceyour-thoughts "I would like to start a discussuion about price movement at support/resistance, Fib and pivot levels.  
  
Time and again I see the price...") 11 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/157406-fx30m-bouncing-system/reply#reply)
  * Subscribe
  * [72](javascript:void\(0\);)

Attachments: FX_30M Bouncing System

Tags: FX_30M Bouncing System

#  [](/thread/157406-fx30m-bouncing-system)FX_30M Bouncing System 

  * 

  * [#481](/thread/post/2706855#post2706855 "Post Permalink")

  * May 1, 2009 7:22am  May 1, 2009 7:22am 

  * [ Dan Johnston](dan*johnston)

  * | Joined May 2008  | Status: Trader | [354 Posts](/search?do=process&provider=Member&searchuser=69420)

> [Quoting siobi](/thread/post/2678699#post2678699 "View Quoted Post")
> 
> Disliked
> 
> hm.......  
>  Lag seems not helpful for this system...  
>    
>  anyway, I found it usefull in Hit system 5M EU...  
>    
>  16EMA+48EMA +Lag+Confirm5M  
>    
>  great system...  
>    
>  Custom indicator  
>  1) 2MA crossover  
>  2) Laguerre  
>  3) Confirm5M  
>    
>  EMA  
>  1) 16EMA, Typical Price  
>  2) 48EMA, Typical Price  
>    
>  will explain later in another new thread....  
>  got to sleep....
> 
> Ignored

  
How's this system going, Siobi? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#482](/thread/post/2708279#post2708279 "Post Permalink")

  * May 1, 2009 10:35pm  May 1, 2009 10:35pm 

  * [ qz10cq](qz10cq)

  * | Joined Dec 2006  | Status: Trader | [303 Posts](/search?do=process&provider=Member&searchuser=29720)

Siobi, have you updated your R9? All my r9 trades were ending with +1 except for one which lost -100. Went back to your r8 and it's been a steady loser for the last 2 weeks. What else you got up your sleeve?...Dan 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#483](/thread/post/2727126#post2727126 "Post Permalink")

  * May 12, 2009 2:26pm  May 12, 2009 2:26pm 

  * [ qz10cq](qz10cq)

  * | Joined Dec 2006  | Status: Trader | [303 Posts](/search?do=process&provider=Member&searchuser=29720)

Siobia, you still here? Are you making your 20 pips daily using r9? Have you made any changes to r9....Dan 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#484](/thread/post/2861557#post2861557 "Post Permalink")

  * Jul 9, 2009 6:15pm  Jul 9, 2009 6:15pm 

  * [ mtuppers](mtuppers)

  * | Joined Mar 2007  | Status: Trader | [397 Posts](/search?do=process&provider=Member&searchuser=34853)

one suggestion  
  
siobi, great EA I will try it soon  
  
I think using stochastic as filiter entry after confirm the trend. (since you know trend is going)  
  
if Higher TF show up trend. entry would be when stochastic going up.  
  
also EA should also do re-entry, when another going up comfirmed. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#485](/thread/post/2946614#post2946614 "Post Permalink")

  * Aug 12, 2009 12:20am  Aug 12, 2009 12:20am 

  * [ BadB0Y](badb0y)

  * | Joined Jun 2009  | Status: Trader | [14 Posts](/search?do=process&provider=Member&searchuser=107256)

Hi:  
  
Thanks for this EA, but i got message "System had expired" in backtest.....  
  
any solution?  
  
Regards 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#486](/thread/post/2968259#post2968259 "Post Permalink")

  * Aug 19, 2009 11:23pm  Aug 19, 2009 11:23pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar107371_2.gif) sasavisnic67](sasavisnic67)

  * | Joined Jun 2009  | Status: Trader | [261 Posts](/search?do=process&provider=Member&searchuser=107371)

Hi All, I have contacted my broker with same problem and have got following answer:  
  
"Dear Sasa,  
  
Please notice that our platform just allows EA’s with a Market execution. Instant Execution EA’s are not accepted by Varengold.  
Please contact your programmer and make sure that the EA is programmed in Market execution form."  
  
Can anybody help get the EA programed like this?  
  
Sasa  
  
  

> [Quoting BadB0Y](/thread/post/2946614#post2946614 "View Quoted Post")
> 
> Disliked
> 
> Hi:  
>    
>  Thanks for this EA, but i got message "System had expired" in backtest.....  
>    
>  any solution?  
>    
>  Regards
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#487](/thread/post/3199890#post3199890 "Post Permalink")

  * Nov 3, 2009 1:10am  Nov 3, 2009 1:10am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar108275_9.gif) leafarct](leafarct)

  * Joined Jul 2009 | Status: ... | [557 Posts](/search?do=process&provider=Member&searchuser=108275)

hello, I'm trying to download the files to test the strategy, however the files are not found. someone more with the same problem? 

Let us be green

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#488](/thread/post/3200215#post3200215 "Post Permalink")

  * Last Post: Edited 3:10am  Nov 3, 2009 2:59am | Edited 3:10am 

  * [ Dan Johnston](dan*johnston)

  * | Joined May 2008  | Status: Trader | [354 Posts](/search?do=process&provider=Member&searchuser=69420)

I bellieve that everything is in the paperclip icon on top of thread.   
  
I have since moved on - I highly recommend spud's stochastic threads among many others and I've made tremendous progress by being eclectic and educating myself from _all_ the great people here.   
  
I hope my old friends here are doing well in all aspects of life.   
  
Good trading all!  
  
PS: Can't wait for NFP Friday![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * FX_30M Bouncing System
  *   * [ **Reply to Thread** ](/thread/157406-fx30m-bouncing-system/reply#reply)

[](https://www.forexfactory.com "Homepage")

  * [Forums](forums)
  * [Trades](trades)
  * [Calendar](calendar)
  * [News](news)
  * [Market](market)
  * [Brokers](brokers)

****

[](https://www.faireconomy.com/)
