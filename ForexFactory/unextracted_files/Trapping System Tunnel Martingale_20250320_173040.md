

  * 

[Martingale, Anti-martingale, and Compounding](/thread/571233-martingale-anti-martingale-and-compounding "Hi all traders, 
i started this thread to meet others people interested in money management. 
We all know that martingale strategies are...") 40 replies

[Martingale, Reverse Martingale, Modified Martingale, Maths](/thread/736165-martingale-reverse-martingale-modified-martingale-maths "Hi all, so Martingale has been a risky yet maybe non profitable system. While roulette has an edge of \(2.7%/5.4%\) 
  
Inspired by Adam...") 1 reply

[How to change this Martingale to Reverse Martingale ?](/thread/546755-how-to-change-this-martingale-to-reverse-martingale "How to change this Martingale to Reverse Martingale ?") 3 replies

[Trapping System: Way to Fully-Automated Trading System](/thread/509226-trapping-system-way-to-fully-automated-trading-system "Hi fellow Traders! 
This is my first time to write a new thread. Would like to share a trading method, which at least made me happy right...") 47 replies

[Martingale vs. Non Martingale (Simplified RoR vs Profit)](/thread/526308-martingale-vs-non-martingale-simplified-ror-vs-profit "Martingale: The gambler doubles his bet after every loss... 
  
Martingale vs. Non Martingale \(Simplified RoR vs Profit in 3 trade runs...") 1 reply

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/524198-trapping-system-tunnel-martingale/reply#reply)
  * Subscribe
  * [221](javascript:void\(0\);)

Attachments: Trapping System: Tunnel Martingale

Tags: Trapping System: Tunnel Martingale

#  [](/thread/524198-trapping-system-tunnel-martingale)Trapping System: Tunnel Martingale 

  * 

  * [#1](/thread/524198-trapping-system-tunnel-martingale "Post Permalink")

  * First Post: Edited Apr 20, 2015 11:20pm  Jan 30, 2015 3:13pm | Edited Apr 20, 2015 11:20pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

Hi All,  
would like to share to all of you guys about the "never loss" system (practically), which is PM'ed to me a few days ago. A bro asked me to build EA which is based on martingale series, with the series of BUY and SELL at the upper price and lower price divided by gap. So it will form like a tunnel.  
Actually I was building the same martingale series long time before, but it was on different variant and wasn't successful. Then this idea popped out from [KanGKunG](http://www.forexfactory.com/kangkung).  
  
The elements:  
\- Gaps (in points, not pips)  
\- Support / Resistance  
\- Lot as martingale series (0.01, 0.02, 0.04, 0.08....)  
\- TP as 2x of the gaps (as requested by KanGKunG) or configured fixed value.  
\- SL as min SL value + Gaps + spread (as requested by KanGKunG), or configured fixed value, or no SL at all.  
\- Without TP and SL is possible, by take profit as total profit.  
  
In short, it will do as following (in 1 cycle):  
\- Firstly, it will do BUY 0.01 lot at the current price, then SELL STOP 0.02 lots at the current BUY price - Gaps. This will form a **TUNNEL** , with upper price and lower price.  
<http://i62.tinypic.com/29ys95c.jpg>  
  
\- If let us say the price goes up and reaches TP (of the first order), then it will close the cycle and start a new one.  
\- If not (of course it will go down), once reaches the SELL STOP 0.02, then this time will do BUY STOP 0.04.  
\- If the price goes down and reaches SL, then the cycle closed and start a new one.  
\- If the price goes back up, and reaches the first order price, then it will do SELL STOP 0.08.  
\- If the price ranging much, then cycle most likely will never close and series of BUY STOP or SELL STOP with more and more lots will be placed.  
  
During my observation,  
with settings as:  
\- EUR/USD.  
\- martingale factor 1, 2, 4.  
\- Start AnyTime from 12:00:00 - 00:00:00 Singapore / Malaysia time (no Support and Resistance).  
\- Start with 0.01.  
\- Start with $5000.  
\- Take profit at money-based (Total Profit), at $0.10 for each cycle.  
\- Always BUY first.  
  
I found that:  
\- The most martingale index used is 9. You'll end up with lot size 2.56, that would be 5.11 lots in total.  
\- The average martingale will close around the index of 2 (0.3 lots total) - 4 (0.15 lots total).  
\- Daily profit around $10 - $20.  
\- Lowest Margin Available ..... I'm still observing this.  
\- During market sleep time, the most martingale index can be higher, because of the price is ranging.  
\- During opening of US or Europe time, the least martingale index can be 1. Which means once open, then < 1 min the cycle closed and restarted again.  
  
Below are the configuration screenshot:  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot2.png
Size: 48 KB](/attachment/image/1610495/thumbnail?d=1423805063)](/attachment/image/1610495?d=1423805063)   

  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot3.png
Size: 60 KB](/attachment/image/1610496/thumbnail?d=1423805120)](/attachment/image/1610496?d=1423805120)   

  
  
Too much configuration, huh?  
Yes, I did this just to cater many scenarios.  
  
I will explain it as following (note that RED fonts means not yet implemented!)  
**Start Type**  
There are 4 settings, Start Anytime (within time), Start from Support and Resistance, Start from Daily High and Low, Start at X points from current price.  
_Start Anytime_ will start literally the moment you click OK, but if it is not within time (Start Time and Stop Time), then EA will wait until the time is reached inside.  
_Start from Support and Resistance_ , will start from Support or Resistance point. If it is reaching Support, it will do BUY first. If it is reaching Resistance, it will do SELL first. Support and Resistance (and Pivot) calculated based on [http://www.investopedia.com/ask/answ...vot-points.asp](http://www.investopedia.com/ask/answers/forex/forex-pivot-points.asp).  
_Start from Daily High and Low_ , basically is same as Start from Support and Resistance. But will start from Daily High and Low for today.  
_Start at X points from current price_.  
  
**Take Profit line color**  
Line color for Take Profit (if Target is Fixed Points).  
**Text color**  
The text color.  
**Upper Gap Price color**  
The color of the upper gap.  
**Lower Gap Price color**  
The color of the lower gap.  
**Text size**  
The text size  
**Magic Number**  
The magic number to identify this EA. Basically this will be used if you want to run more than 2 different EAs on your account.  
**Line Style, Line Width, Line Height**  
as described  
**Use Slippage**  
if you want to use slippage when closing orders.  
**Slippage**  
the slippage value.  
**Type of Start Lots**  
The type of Starting lots. Either Dynamic or Fixed.  
**Dynamic Lots**  
If you expect 0.01 as starting, put 0.000002 as the value for $5000 balance. That means, Dynamic Lots = Expected Lots / Balance. This only applies for Start Lots = Dynamic.  
**Fixed Lots**  
Fixed starting lots, that's it. This only applies for Start Lots = Fixed.  
**Martingale Factor, Martingale Factor Multiplier, Max Martingale Factor**  
Martingale factor of 1, 2, 3 with Martingale Factor Multiplier = 2, and Max Martingale Factor = 25, will produce: 1, 2, 3, 6, 12, 24, 48, ..... until 25 sequences.  
Martingale factor of 1, 2, 4 (common martingale) with Martingale Factor Multiplier = 2, and Max Martingale Factor = 25, will produce: 1, 2, 4, 8, 16, ..... until 25 sequences.  
**Gaps**  
The Upper and Lower price gap in _points_. Points is the lowest unit. In most broker with 5 digits, 10 points = 1 pip. For 4 digits broker, 1 point = 1 pip. Please be careful with your broker. My calculation is calculated with how many digits I have.  
**Max Cycle**  
Max cycle per run. Normally 0 is unlimited.  
**Target Type, Profit Target, Profit Multiplier**  
The way I close the cycle, by target.  
Dynamic money (Balance x this value) -> means the target in $ (Total Profit _all orders in 1 cycle_) will be calculated against balance (NOT equity). Linked to **Profit Multiplier** for the value. Profit Multiplier = Your expected target (in $) / your balance. Once the total profit reaches your expected target, then cycle will be closed. This settings normally be used if you want compounding targets.  
Fixed Money -> target will be only fixed amount of money (Total Profit _all orders in 1 cycle_). Linked to **Profit Target** for the value. Once the total profit reaches this, then cycle will be closed.  
Fixed Points -> calculated by points of the first order in 1 cycle.  
**Points Target Type**  
The target type for **Fixed Points**. Will be calculated based on the first order.  
Fixed Points for both TP and SL -> once reaches Points Target (TP), or Points Stop Loss (SL), cycle will close.  
Note: Fixed point will _never_ put TP and SL explicitly to the first order. _Calculation is done inside EA itself_.  
  
Other options are clearly described.  
<http://i59.tinypic.com/2rp5zqv.jpg>  
  
**Start From**  
A cycle will always start from "BUY first", or "SELL first".  
**Next Cycle, start by**  
Next cycle, will start from, "Follows Start From settings",  
or "Follows from last profit direction" -> if your last cycle profit end up in SELL, then it will start SELL.  
**Date Time base**  
You want Local Time (your PC, VPS, anything you run this), or Server Time (each broker is having different Server Time with another broker).  
**Start Time, Stop Time**  
Start time and stop time for Start Anytime.  
**Debugging Mode, Development Mode**  
These 2 flags are only for my reference in case any error happens.  
  
......the rest are just colors and some hanky wanky settings.  
  
  
  
**WARNING** : To the one who knows what is martingale, yes, it is almost 100% profitable (practically) I don't deny that, but that depends on how much balance you have, and how big is the lot your broker supports. I don't debate on profitability of this method.  
You're curious, you're interested, download and try it first on your demo account. Then if you are 100% sure with your settings, you can start doing it on your live account (if you wish).  
Read this: [http://www.investopedia.com/articles...martingale.asp](http://www.investopedia.com/articles/forex/06/martingale.asp)  
**Your profit, depends on your settings and your money management method...**  
This EA is **HIGHLY CONFIGURABLE**...  
  
I have attached the .mq4, .ex4, and EA Configuration (.set). Note: _ex4 and mq4 is always the latest published EA_.  
There are 2,  
MartingaleKanGKunG.set -> requested by KanGKunG, based on Support and Resistance.  
RadityoMART.set -> my setting, start anytime, follow last.  
When starting this EA, on the right bottom side there'll be "Load" and "Save" button. Click "Load" and select this file.  
<http://i62.tinypic.com/23wpldg.jpg>  
  
Currently, below are the testing site (if you decided to test, let me know your Trade Explorer URL, I will add it here):  
Martingale AnyTime - <http://www.forexfactory.com/radityo.ardi/24>  
Martingale Daily High and Low - <http://www.forexfactory.com/radityo.ardi/80>  
Martingale SNR - <http://www.forexfactory.com/radityo.ardi/81>  
Martingale AnyTime - <http://www.forexfactory.com/radityo.ardi/38> (this is for martingale factor 1, 2, 2, 2).  
  
As mentioned by aahmad29, the basic idea of this EA is described as below:  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot1.png
Size: 130 KB](/attachment/image/1608631/thumbnail?d=1423634311)](/attachment/image/1608631?d=1423634311)   

  
  
There's an interesting facts I've wrote on this link:  
[http://www.forexfactory.com/showthre...37#post8067337](http://www.forexfactory.com/showthread.php?p=8067337#post8067337)  
  
However, bugs may still be there, so please test and report if any issues arise.  
  
NOTE: This EA is licensed under Tunnel Martingale License (terms are derived from MsPL). Which means free to use with open source, but there's a limitations and conditions. Please take time to read the license at: <https://sites.google.com/site/tunnelmartingalecla/>

Attached File(s)

![File Type: zip](https://assets.faireconomy.media/images/attach/zip.gif) [EAConfiguration.zip](/attachment/file/1600453?d=1422598106) 1 KB | 4,551 downloads 

![File Type: txt](https://assets.faireconomy.media/images/attach/txt.gif) [Martingale SNR.set.txt](/attachment/file/1610476?d=1423802287) 1 KB | 2,696 downloads | Uploaded Feb 13, 2015 1:38pm 

![File Type: txt](https://assets.faireconomy.media/images/attach/txt.gif) [Martingale Anytime AUDUSD.set.txt](/attachment/file/1610491?d=1423804960) < 1 KB | 2,425 downloads | Uploaded Feb 13, 2015 2:22pm 

![File Type: txt](https://assets.faireconomy.media/images/attach/txt.gif) [Martingale Anytime EURUSD.set.txt](/attachment/file/1610492?d=1423804968) < 1 KB | 3,557 downloads | Uploaded Feb 13, 2015 2:22pm 

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [TunnelMartingale.mq4](/attachment/file/1642336?d=1427522727) 50 KB | 5,300 downloads | Uploaded Mar 28, 2015 3:05pm 

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [TunnelMartingale.ex4](/attachment/file/1657528?d=1429539612) 86 KB | 3,330 downloads | Uploaded Apr 20, 2015 11:20pm 

If you ask me to code/fix your EA... it's probably not for free...

  * [#2](/thread/post/8034254#post8034254 "Post Permalink")

  * Jan 30, 2015 4:31pm  Jan 30, 2015 4:31pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar370635_1.gif) KanGKunG](kangkung)

  * Joined Apr 2014 | Status: Trader | [36 Posts](/search?do=process&provider=Member&searchuser=370635)

thx bro for doing the martingle trap for me. although your EA is much more setting that what i ask for, but still there is some idea and people can choose which 1 they prefer.. keep it up 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#3](/thread/post/8034272#post8034272 "Post Permalink")

  * Jan 30, 2015 4:38pm  Jan 30, 2015 4:38pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar392182_1.gif) Riyaz555](riyaz555)

  * | Joined Dec 2014  | Status: Trader | [9 Posts](/search?do=process&provider=Member&searchuser=392182)

Great work.. Will give a try as am fond of martingales.. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#4](/thread/post/8034282#post8034282 "Post Permalink")

  * Jan 30, 2015 4:44pm  Jan 30, 2015 4:44pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting KanGKunG](/thread/post/8034254#post8034254 "View Quoted Post")
> 
> Disliked
> 
> thx bro for doing the martingle trap for me. although your EA is much more setting that what i ask for, but still there is some idea and people can choose which 1 they prefer.. keep it up
> 
> Ignored

Thanks to you also, without you popping out to my PM, I wouldn't know this strategy, and find another scenario. Apparently I love the other scenario (the one that you told was wrong), but still logical though, profit was there. ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)  
  
I haven't test the Support and Resistance scenario yet. Just started to test this afternoon before starting new thread. But the logic shouldn't be that hard once I got the basic logic. Would like to ask you to test, and probably (if possible) share the trade explorer u've created. So others can see the result as well. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#5](/thread/post/8034306#post8034306 "Post Permalink")

  * Jan 30, 2015 4:52pm  Jan 30, 2015 4:52pm 

  * [ cuchuflito](cuchuflito)

  * Joined Nov 2008 | Status: Trader | [2,116 Posts](/search?do=process&provider=Member&searchuser=85572)

Martingale= Black Swan....it´s just written in the hidden code of all markets....  
It can only "work", provided you put a limit, and you calculate how many good runs you need to absorb the Black Swan...  
And more often than not, the market could turn in your favour, just after you took that big loss...  
  
It´s just the name of the game brother...Big Boys run the shop, they run the stops...day in day out, collecting retail cash...![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)  
Beware of the stop running right at the gaps that youré looking at.... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#6](/thread/post/8034385#post8034385 "Post Permalink")

  * Jan 30, 2015 5:24pm  Jan 30, 2015 5:24pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar370635_1.gif) KanGKunG](kangkung)

  * Joined Apr 2014 | Status: Trader | [36 Posts](/search?do=process&provider=Member&searchuser=370635)

> [Quoting radityo.ardi](/thread/post/8034282#post8034282 "View Quoted Post")
> 
> Disliked
> 
> {quote} Thanks to you also, without you popping out to my PM, I wouldn't know this strategy, and find another scenario. Apparently I love the other scenario (the one that you told was wrong), but still logical though, profit was there. ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1) I haven't test the Support and Resistance scenario yet. Just started to test this afternoon before starting new thread. But the logic shouldn't be that hard once I got the basic logic. Would like to ask you to test, and probably (if possible) share the trade explorer u've created. So others can see the result as...
> 
> Ignored

  
well about trade explorer is a bit problem due to i dont have vps.. and even i do this kind of trading previously ( by totally manual no EA ) so my trading using the ea is on and off but when its on yes it work as what i want... just that i still prefer it to start trade at SNR level instead of open any level 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#7](/thread/post/8034619#post8034619 "Post Permalink")

  * Jan 30, 2015 6:38pm  Jan 30, 2015 6:38pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting KanGKunG](/thread/post/8034385#post8034385 "View Quoted Post")
> 
> Disliked
> 
> {quote} well about trade explorer is a bit problem due to i dont have vps.. and even i do this kind of trading previously ( by totally manual no EA ) so my trading using the ea is on and off but when its on yes it work as what i want... just that i still prefer it to start trade at SNR level instead of open any level
> 
> Ignored

I think still OK, because Trade Explorer doesn't require VPS. Am I right?  
  
  

> [Quoting cuchuflito](/thread/post/8034306#post8034306 "View Quoted Post")
> 
> Disliked
> 
> Martingale= Black Swan....it´s just written in the hidden code of all markets.... It can only "work", provided you put a limit, and you calculate how many good runs you need to absorb the Black Swan... And more often than not, the market could turn in your favour, just after you took that big loss... It´s just the name of the game brother...Big Boys run the shop, they run the stops...day in day out, collecting retail cash...![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1) Beware of the stop running right at the gaps that youré looking at....
> 
> Ignored

Regarding Black Swan, you are damn right..  
It's a bitter sweet... I would say 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#8](/thread/post/8034765#post8034765 "Post Permalink")

  * Jan 30, 2015 7:24pm  Jan 30, 2015 7:24pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar137376_9.gif) regme](regme)

  * | Joined Mar 2010  | Status: Planning to be like Warren Buffett | [115 Posts](/search?do=process&provider=Member&searchuser=137376)

I am using similar Martingale system, working perfectly. No D-Day yet, but for big lot it needs to be monitor and close whenever it is in profit. High volatility pairs to be consider. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#9](/thread/post/8034919#post8034919 "Post Permalink")

  * Jan 30, 2015 8:26pm  Jan 30, 2015 8:26pm 

  * [ Lopuch](lopuch)

  * | Joined Aug 2006  | Status: Trader | [161 Posts](/search?do=process&provider=Member&searchuser=16379)

Error:  
0 12:18:55.897 TunnelMartingale EURUSD,H1: C06: Updating Labels.  
0 12:18:55.897 TunnelMartingale EURUSD,H1: C07.01: Updating UpperGapPrice to 1.13403.  
0 12:18:55.897 TunnelMartingale EURUSD,H1: C07.02: Updating LowerGapPrice to 1.13343.  
0 12:18:56.740 TunnelMartingale EURUSD,H1: C01: InitOrders method.  
0 12:18:56.740 TunnelMartingale EURUSD,H1: C02: CountStartEndTime method.  
0 12:18:56.740 TunnelMartingale EURUSD,H1: C03: Updating TotalProfit.  
0 12:18:56.740 TunnelMartingale EURUSD,H1: C04: Checking Last Order.  
0 12:18:56.740 TunnelMartingale EURUSD,H1: C04.02: Last was SELL, execute BUYSTOP.  
3 12:18:56.740 TunnelMartingale EURUSD,H1: invalid lots amount for OrderSend function  
0 12:18:56.740 TunnelMartingale EURUSD,H1: Alert: [MartingaleHedging] ERROR -1: invalid function parameter value  
  
EA set in ads, bc upload rename txt to set.  
  
Thank you. 

Attached File(s)

![File Type: txt](https://assets.faireconomy.media/images/attach/txt.gif) [TunelMartingaleNikov.txt](/attachment/file/1600664?d=1422617024) < 1 KB | 961 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#10](/thread/post/8034956#post8034956 "Post Permalink")

  * Edited 9:13pm  Jan 30, 2015 8:44pm | Edited 9:13pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting Lopuch](/thread/post/8034919#post8034919 "View Quoted Post")
> 
> Disliked
> 
> Error: 0 12:18:55.897 TunnelMartingale EURUSD,H1: C06: Updating Labels. 0 12:18:55.897 TunnelMartingale EURUSD,H1: C07.01: Updating UpperGapPrice to 1.13403. 0 12:18:55.897 TunnelMartingale EURUSD,H1: C07.02: Updating LowerGapPrice to 1.13343. 0 12:18:56.740 TunnelMartingale EURUSD,H1: C01: InitOrders method. 0 12:18:56.740 TunnelMartingale EURUSD,H1: C02: CountStartEndTime method. 0 12:18:56.740 TunnelMartingale EURUSD,H1: C03: Updating TotalProfit. 0 12:18:56.740 TunnelMartingale EURUSD,H1: C04: Checking Last Order. 0 12:18:56.740 TunnelMartingale...
> 
> Ignored

hmm.... either your broker having [spreads](/brokers/spreads "View Live Spreads on the Broker Guide") around 6 pips at the time, or something else happening. Your settings seems ok to me, started with 0.01.  
  
The Experts tab actually written in descending based on the time.  
Just curious, can you paste the error before 12:18:56.740?  
  
UPDATED:  
Can you re-download again the EA and set IsDebug to True?  
  
Hei,  
OK. Found out and understood the issue. Max Martingale Factor on your settings is 4, so martingale series is only 1, 1, 2, 4 (based on your settings). Seems that your cycle is reaching 4th index, and that time will try to do BUYSTOP (well, based on your log given).  
Martingale factor since it is only 4, it tries to do BUYSTOP at index 5, it can't find the 5th martingale index. So, this time, martingale series is blank / 0. Then the lot size calculation will also resulting in 0.  
That's why it throws: invalid lots amount for OrderSend function  
  
Please leave Max Martingale Factor to the default value (25). I haven't implement _max orders in a cycle limit_ , and I don't think I should implement that. Since if we stop then no point of having martingale, since that is the concept.  
  
I hope you were not doing this with your real account. ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#11](/thread/post/8035016#post8035016 "Post Permalink")

  * Jan 30, 2015 9:14pm  Jan 30, 2015 9:14pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar383001_1.gif) bypasssbo](bypasssbo)

  * | Joined Sep 2014  | Status: Trader | [53 Posts](/search?do=process&provider=Member&searchuser=383001)

radityo.ardi If I load your set, I get invalid trade parameters and invalid trade volume errors every second 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#12](/thread/post/8035050#post8035050 "Post Permalink")

  * Jan 30, 2015 9:28pm  Jan 30, 2015 9:28pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting bypasssbo](/thread/post/8035016#post8035016 "View Quoted Post")
> 
> Disliked
> 
> radityo.ardi If I load your set, I get invalid trade parameters and invalid trade volume errors every second
> 
> Ignored

I'm going home in a minutes. Meanwhile, can you download the latest, set IsDebug to True, then post whatever log thrown in this thread? 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#13](/thread/post/8035376#post8035376 "Post Permalink")

  * Jan 30, 2015 11:05pm  Jan 30, 2015 11:05pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

Just found in internet:  
  
Forex Trading & Martingale Infographic: [http://forexuseful.com/authors/forex...le-infographic](http://forexuseful.com/authors/forex-useful/forex-trading-martingale-infographic)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#14](/thread/post/8035667#post8035667 "Post Permalink")

  * Jan 31, 2015 12:46am  Jan 31, 2015 12:46am 

  * [ Lopuch](lopuch)

  * | Joined Aug 2006  | Status: Trader | [161 Posts](/search?do=process&provider=Member&searchuser=16379)

> [Quoting radityo.ardi](/thread/post/8034956#post8034956 "View Quoted Post")
> 
> Disliked
> 
> {quote} hmm.... either your broker having spreads around 6 pips at the time, or something else happening. Your settings seems ok to me, started with 0.01. The Experts tab actually written in descending based on the time. Just curious, can you paste the error before 12:18:56.740? UPDATED: Can you re-download again the EA and set IsDebug to True? Hei, OK. Found out and understood the issue. Max Martingale Factor on your settings is 4, so martingale series is only 1, 1, 2, 4 (based on your settings). Seems that your cycle is reaching 4th index, and...
> 
> Ignored

Thank you,  
go tested it with this sett. 

Attached File(s)

![File Type: txt](https://assets.faireconomy.media/images/attach/txt.gif) [TailBeforeErr.txt](/attachment/file/1600894?d=1422632774) 3 KB | 801 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#15](/thread/post/8036074#post8036074 "Post Permalink")

  * Jan 31, 2015 3:02am  Jan 31, 2015 3:02am 

  * [ aahmad29](aahmad29)

  * Joined Aug 2012 | Status: Love for all; Hatred for none | [3,557 Posts](/search?do=process&provider=Member&searchuser=286894)

> [Quoting radityo.ardi](/thread/post/8034155#post8034155 "View Quoted Post")
> 
> Disliked
> 
> Hi All, would like to share to all of you guys about the "never loss" system (practically), which is PM'ed to me a few days ago. A bro asked me to build EA which is based on martingale series, with the series of BUY and SELL at the upper price and lower price divided by gap. So it will form like a tunnel. Actually I was building the same martingale series long time before, but it was on different variant and wasn't successful. Then this idea popped out from [KanGKunG](http://www.forexfactory.com/kangkung). The elements: - Gaps (in points,...
> 
> Ignored

My suggestion is to run this system during London open and NY half time is closing time otherwise you will have huge losses. Why am I giving you suggestion because I introduced same kind of system <http://www.forexfactory.com/showthread.php?t=501215> but I have modified this system just as you mentioned above. 

Love for all; Hatred for none.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#16](/thread/post/8036824#post8036824 "Post Permalink")

  * Jan 31, 2015 6:16pm  Jan 31, 2015 6:16pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting aahmad29](/thread/post/8036074#post8036074 "View Quoted Post")
> 
> Disliked
> 
> {quote} My suggestion is to run this system during London open and NY half time is closing time otherwise you will have huge losses. Why am I giving you suggestion because I introduced same kind of system <http://www.forexfactory.com/showthread.php?t=501215> but I have modified this system just as you mentioned above.
> 
> Ignored

That is what people normally do. I don't suggest to run this when the market is not open. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#17](/thread/post/8036876#post8036876 "Post Permalink")

  * Edited 8:18pm  Jan 31, 2015 8:01pm | Edited 8:18pm 

  * [ aahmad29](aahmad29)

  * Joined Aug 2012 | Status: Love for all; Hatred for none | [3,557 Posts](/search?do=process&provider=Member&searchuser=286894)

> [Quoting radityo.ardi](/thread/post/8034155#post8034155 "View Quoted Post")
> 
> Disliked
> 
> Hi All, would like to share to all of you guys about the "never loss" system (practically), which is PM'ed to me a few days ago. A bro asked me to build EA which is based on martingale series, with the series of BUY and SELL at the upper price and lower price divided by gap. So it will form like a tunnel. Actually I was building the same martingale series long time before, but it was on different variant and wasn't successful. Then this idea popped out from [KanGKunG](http://www.forexfactory.com/kangkung). The elements: - Gaps (in points,...
> 
> Ignored

I agree with you that max lot was 2.56 but I couldn't understand**how did you calculate the Daily profit around $10 - $20. when you are using 0.01 lot**.  
  
  
I have another suggestion that never use less than 10 pips Gap due to spread. 

Love for all; Hatred for none.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#18](/thread/post/8036917#post8036917 "Post Permalink")

  * Jan 31, 2015 9:07pm  Jan 31, 2015 9:07pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting aahmad29](/thread/post/8036876#post8036876 "View Quoted Post")
> 
> Disliked
> 
> {quote} I agree with you that max lot was 2.56 but I couldn't understand how did you calculate the Daily profit around $10 - $20. when you are using 0.01 lot.
> 
> Ignored

Well, first of all, **_daily $10 - $20, is not 1 cycle._**  
During running my EA, it can be hundred of cycles (depends on your settings), my settings was getting profit for $0.5 per cycle. Sometimes (since the market moves much and my take profit per cycle was too low), I got minus as market moves the opposite way, but overall, Friday 30 Jan 2015, my profit was even around ~$40.  
  

> [Quoting aahmad29](/thread/post/8036876#post8036876 "View Quoted Post")
> 
> Disliked
> 
> {quote}I have another suggestion that never use less than 10 pips Gap due to spread.
> 
> Ignored

Yes, I agree with you, never uses gaps less than 10 pips (100 points in equivalent). Help me to test that scenario. Then only we will know which settings that are most profitable... but safest...![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)  
Even for KanGKunG's scenario, he uses 10 pips of gap, TP at 2 x of Gaps and SL at Gaps + Spreads + 10 pips, daily max 3 cycles. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#19](/thread/post/8037174#post8037174 "Post Permalink")

  * Feb 1, 2015 1:49am  Feb 1, 2015 1:49am 

  * [ aahmad29](aahmad29)

  * Joined Aug 2012 | Status: Love for all; Hatred for none | [3,557 Posts](/search?do=process&provider=Member&searchuser=286894)

> [Quoting radityo.ardi](/thread/post/8036917#post8036917 "View Quoted Post")
> 
> Disliked
> 
> {quote} Well, first of all, daily $10 - $20, is not 1 cycle. During running my EA, it can be hundred of cycles (depends on your settings), my settings was getting profit for $0.5 per cycle. Sometimes (since the market moves much and my take profit per cycle was too low), I got minus as market moves the opposite way, but overall, Friday 30 Jan 2015, my profit was even around ~$40. {quote} Yes, I agree with you, never uses gaps less than 10 pips (100 points in equivalent). Help me to test that scenario. Then only we will know which settings that are...
> 
> Ignored

I think I am confusing myself with term cycle. Can you please define it more clearly with example.  
  
My way of working is that I open any buy/sell order then it starts process of adding pending order to opposite side of last open trades with double lot. I set my TP in $.  
  
Suppose when it reaches that Net profit among multiple open positions, I close all orders and start from beginning. 

Love for all; Hatred for none.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#20](/thread/post/8037247#post8037247 "Post Permalink")

  * Edited 4:03am  Feb 1, 2015 3:30am | Edited 4:03am 

  * [ aahmad29](aahmad29)

  * Joined Aug 2012 | Status: Love for all; Hatred for none | [3,557 Posts](/search?do=process&provider=Member&searchuser=286894)

With above given process, I got $695 with 24/5 running EA continuously but sorry I cant share that EA because it is shared by us(group of traders/Friends) for commercial purpose. You can see here my posts [http://www.forexfactory.com/showthre...62#post8035562](http://www.forexfactory.com/showthread.php?p=8035562#post8035562)  
  
Account =$10,000  
Initial lot =0.1  
Gap=20 Pips  
Profit=$10  
  
On my live account, I use 0.01 lot and I use this system only when London market open, if my orders are close before NY market open then I place another trade otherwise I let it running because mostly all orders close during NY. I also use this system when any big report/news is expected. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Untitled.jpg
Size: 69 KB](/attachment/image/1601368/thumbnail?d=1422730712)](/attachment/image/1601368?d=1422730712)   

Love for all; Hatred for none.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Trapping System: Tunnel Martingale
  *   * [ **Reply to Thread** ](/thread/524198-trapping-system-tunnel-martingale/reply#reply)

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

[Martingale, Anti-martingale, and Compounding](/thread/571233-martingale-anti-martingale-and-compounding "Hi all traders, 
i started this thread to meet others people interested in money management. 
We all know that martingale strategies are...") 40 replies

[Martingale, Reverse Martingale, Modified Martingale, Maths](/thread/736165-martingale-reverse-martingale-modified-martingale-maths "Hi all, so Martingale has been a risky yet maybe non profitable system. While roulette has an edge of \(2.7%/5.4%\) 
  
Inspired by Adam...") 1 reply

[How to change this Martingale to Reverse Martingale ?](/thread/546755-how-to-change-this-martingale-to-reverse-martingale "How to change this Martingale to Reverse Martingale ?") 3 replies

[Trapping System: Way to Fully-Automated Trading System](/thread/509226-trapping-system-way-to-fully-automated-trading-system "Hi fellow Traders! 
This is my first time to write a new thread. Would like to share a trading method, which at least made me happy right...") 47 replies

[Martingale vs. Non Martingale (Simplified RoR vs Profit)](/thread/526308-martingale-vs-non-martingale-simplified-ror-vs-profit "Martingale: The gambler doubles his bet after every loss... 
  
Martingale vs. Non Martingale \(Simplified RoR vs Profit in 3 trade runs...") 1 reply

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/524198-trapping-system-tunnel-martingale/reply#reply)
  * Subscribe
  * [221](javascript:void\(0\);)

Attachments: Trapping System: Tunnel Martingale

Tags: Trapping System: Tunnel Martingale

#  [](/thread/524198-trapping-system-tunnel-martingale)Trapping System: Tunnel Martingale 

  * 

  * [#21](/thread/post/8037326#post8037326 "Post Permalink")

  * Feb 1, 2015 5:14am  Feb 1, 2015 5:14am 

  * [ aahmad29](aahmad29)

  * Joined Aug 2012 | Status: Love for all; Hatred for none | [3,557 Posts](/search?do=process&provider=Member&searchuser=286894)

Default settings and initial deposit is $10,000. Modelling Quality is not good but still I posted results here. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Untitled.jpg
Size: 236 KB](/attachment/image/1601376/thumbnail?d=1422735267)](/attachment/image/1601376?d=1422735267)   

Love for all; Hatred for none.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#22](/thread/post/8037959#post8037959 "Post Permalink")

  * Feb 2, 2015 1:28am  Feb 2, 2015 1:28am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

Answering your question, your picture is what this EA about. from start open order, till all closed, I called it 1 cycle.  
Your method seems exactly the same with KanGKunG. 3 cycles max...  
  
I have given many options just to see what will happen. Some may want to close as quickly as possible with hundred cycles, but one may want to be "safe". One may like spices, but other's not... 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#23](/thread/post/8037972#post8037972 "Post Permalink")

  * Feb 2, 2015 1:34am  Feb 2, 2015 1:34am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting aahmad29](/thread/post/8037326#post8037326 "View Quoted Post")
> 
> Disliked
> 
> Default settings and initial deposit is $10,000. Modelling Quality is not good but still I posted results here. {image}
> 
> Ignored

the heck...how come u able to do backtest... I wonder... I never succeed on that... Maybe my history is not good enough... 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#24](/thread/post/8037988#post8037988 "Post Permalink")

  * Feb 2, 2015 1:45am  Feb 2, 2015 1:45am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar200171_4.gif) tylerbose](tylerbose)

  * Joined Oct 2011 | Status: don't trade like i do | [485 Posts](/search?do=process&provider=Member&searchuser=200171)

> Quote
> 
> Disliked
> 
> martingale

  
is it 2008 again ?, so many accounts have been burned because of this, unless you have an unlimited account, every martingale based strategy that i'v seen since i'v been trading had failed miserably. 

i lose money for a living

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#25](/thread/post/8038229#post8038229 "Post Permalink")

  * Feb 2, 2015 5:38am  Feb 2, 2015 5:38am 

  * [ aahmad29](aahmad29)

  * Joined Aug 2012 | Status: Love for all; Hatred for none | [3,557 Posts](/search?do=process&provider=Member&searchuser=286894)

> [Quoting tylerbose](/thread/post/8037988#post8037988 "View Quoted Post")
> 
> Disliked
> 
> {quote} is it 2008 again ?, so many accounts have been burned because of this, unless you have an unlimited account, every martingale based strategy that i'v seen since i'v been trading had failed miserably.
> 
> Ignored

You are right but it also depends on strategy. I found one strategy which keeps opening the orders with double lot in losing direction so obviously you are going to loose your money in any trending market.  
  
Our strategy is good in any trending market and very good in dealing with any report or unexpected news.  
  
Ranging market is not good for this strategy so you can easily avoid Asian session and you can add some more stuff like support and resistance to make it secure. Money management is very important because if trader is greedy and want to make big profit then this strategy is not for him.  
  
Myself, I use $2000 and initial lot is 0.01 but I use only during London and NY market time or when any report is expected.  
  
In this thread, testing is going on with $5000 with small lot.  
  
Even if EA is managing your orders but I stayed in front of computer until EA is running. 

Love for all; Hatred for none.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#26](/thread/post/8038654#post8038654 "Post Permalink")

  * Feb 2, 2015 11:47am  Feb 2, 2015 11:47am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting aahmad29](/thread/post/8038229#post8038229 "View Quoted Post")
> 
> Disliked
> 
> {quote}Money management is very important because if trader is greedy and want to make big profit then this strategy is not for him.
> 
> Ignored

@aahmad29, that is the best line to describe how this EA will work. 100% profitable, it depends on the trader. Me? I'm just giving you guys a tool to do this...  
![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)  
  
And moreover, martingale, has so many variant. I got 1 which was developed a few months ago, but didn't work.  
Some people would do Buy when trend is sell, if it goes down further again do BUY again, so on and so forth, until trends reverting back then you got profit and close it all. Some people would do the same strategy as above, 2 direction, BUY and SELL at the same prict. Some would do random buy sell. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#27](/thread/post/8038851#post8038851 "Post Permalink")

  * Feb 2, 2015 3:20pm  Feb 2, 2015 3:20pm 

  * [ aahmad29](aahmad29)

  * Joined Aug 2012 | Status: Love for all; Hatred for none | [3,557 Posts](/search?do=process&provider=Member&searchuser=286894)

> [Quoting radityo.ardi](/thread/post/8038654#post8038654 "View Quoted Post")
> 
> Disliked
> 
> {quote} @aahmad29, that is the best line to describe how this EA will work. 100% profitable, it depends on the trader. Me? I'm just giving you guys a tool to do this... ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1) And moreover, martingale, has so many variant. I got 1 which was developed a few months ago, but didn't work. Some people would do Buy when trend is sell, if it goes down further again do BUY again, so on and so forth, until trends reverting back then you got profit and close it all. Some people would do the same strategy as above, 2 direction, BUY and SELL at the same prict....
> 
> Ignored

EA which I am using it has disadvantage that it takes only sell or buy as first trade; If last successful trade was sell then it did not open sell trade. 

Love for all; Hatred for none.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#28](/thread/post/8038874#post8038874 "Post Permalink")

  * Feb 2, 2015 3:34pm  Feb 2, 2015 3:34pm 

  * [ aahmad29](aahmad29)

  * Joined Aug 2012 | Status: Love for all; Hatred for none | [3,557 Posts](/search?do=process&provider=Member&searchuser=286894)

> [Quoting radityo.ardi](/thread/post/8038654#post8038654 "View Quoted Post")
> 
> Disliked
> 
> {quote} @aahmad29, that is the best line to describe how this EA will work. 100% profitable, it depends on the trader. Me? I'm just giving you guys a tool to do this... ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1) And moreover, martingale, has so many variant. I got 1 which was developed a few months ago, but didn't work. Some people would do Buy when trend is sell, if it goes down further again do BUY again, so on and so forth, until trends reverting back then you got profit and close it all. Some people would do the same strategy as above, 2 direction, BUY and SELL at the same prict....
> 
> Ignored

I have set your EA for forward testing.  
  
Gap=100 points  
Fixed lots =0.03  
Target type = Fixed money  
Profit target = 0.4  
  
all other settings are default  
  
Starting Balance is $4,298 

Love for all; Hatred for none.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#29](/thread/post/8038945#post8038945 "Post Permalink")

  * Feb 2, 2015 4:34pm  Feb 2, 2015 4:34pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

Finally....!!!![](https://resources.faireconomy.media/images/emojis/64/1f923.png?v=15.1)  
Reaching the max martingale I can get..., on the 11th index. I will try release new version today evening (my local time)...  
No pending order succeeded to execute... 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot1.png
Size: 107 KB](/attachment/image/1601909/thumbnail?d=1422862361)](/attachment/image/1601909?d=1422862361)   

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#30](/thread/post/8039710#post8039710 "Post Permalink")

  * Feb 2, 2015 9:44pm  Feb 2, 2015 9:44pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

I've uploaded v1.03.  
A few changes:  
Start by Support and Resistance is supported now. But in the middle of testing (Support and Resistance is never reached since Friday and today).  
Close by Fixed Points is supported as well.  
  
Moved the file hosting to Dropbox. I hope y'all able to download. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#31](/thread/post/8042216#post8042216 "Post Permalink")

  * Feb 3, 2015 7:46pm  Feb 3, 2015 7:46pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

Aaaah... wow..!  
Finally, first profit using Support Resistance...  
Well done... KanGKunG!  
![](https://resources.faireconomy.media/images/emojis/64/1f918.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)

Attached Image

![](/attachment/image/1603015?d=1422960330)

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#32](/thread/post/8044245#post8044245 "Post Permalink")

  * Feb 4, 2015 9:16am  Feb 4, 2015 9:16am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar370635_1.gif) KanGKunG](kangkung)

  * Joined Apr 2014 | Status: Trader | [36 Posts](/search?do=process&provider=Member&searchuser=370635)

> [Quoting radityo.ardi](/thread/post/8042216#post8042216 "View Quoted Post")
> 
> Disliked
> 
> Aaaah... wow..! Finally, first profit using Support Resistance... Well done... KanGKunG! ![](https://resources.faireconomy.media/images/emojis/64/1f918.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1) {image}
> 
> Ignored

  
haha yeah.. nice... keep it up bro... thx for doing this! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#33](/thread/post/8049574#post8049574 "Post Permalink")

  * Feb 6, 2015 5:42am  Feb 6, 2015 5:42am 

  * [ aahmad29](aahmad29)

  * Joined Aug 2012 | Status: Love for all; Hatred for none | [3,557 Posts](/search?do=process&provider=Member&searchuser=286894)

> [Quoting radityo.ardi](/thread/post/8039710#post8039710 "View Quoted Post")
> 
> Disliked
> 
> I've uploaded v1.03. A few changes: Start by Support and Resistance is supported now. But in the middle of testing (Support and Resistance is never reached since Friday and today). Close by Fixed Points is supported as well. Moved the file hosting to Dropbox. I hope y'all able to download.
> 
> Ignored

Are u still using unlimited cycles to destroy your account? Never do that. I use only one cycle at a time. Next cycle don't start until last cycle is closed.  
  
You can see progress here [http://www.forexfactory.com/showthre...18#post8049318](http://www.forexfactory.com/showthread.php?p=8049318#post8049318)

Love for all; Hatred for none.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#34](/thread/post/8049606#post8049606 "Post Permalink")

  * Feb 6, 2015 6:09am  Feb 6, 2015 6:09am 

  * [ aahmad29](aahmad29)

  * Joined Aug 2012 | Status: Love for all; Hatred for none | [3,557 Posts](/search?do=process&provider=Member&searchuser=286894)

> [Quoting radityo.ardi](/thread/post/8039710#post8039710 "View Quoted Post")
> 
> Disliked
> 
> I've uploaded v1.03. A few changes: Start by Support and Resistance is supported now. But in the middle of testing (Support and Resistance is never reached since Friday and today). Close by Fixed Points is supported as well. Moved the file hosting to Dropbox. I hope y'all able to download.
> 
> Ignored

I have question that why your EA placed so many sell stop orders. There is something wrong but I am not sure what it is. My EA is running fine and profitable but on the other side it is safe to play with support/resistance. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Untitled.jpg
Size: 408 KB](/attachment/image/1605245/thumbnail?d=1423170473)](/attachment/image/1605245?d=1423170473)   

Love for all; Hatred for none.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#35](/thread/post/8050081#post8050081 "Post Permalink")

  * Feb 6, 2015 12:42pm  Feb 6, 2015 12:42pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting aahmad29](/thread/post/8049606#post8049606 "View Quoted Post")
> 
> Disliked
> 
> {quote} I have question that why your EA placed so many sell stop orders. There is something wrong but I am not sure what it is. My EA is running fine and profitable but on the other side it is safe to play with support/resistance. {image}
> 
> Ignored

That's something new.... not sure why, but can you check the version number of the EA?  
I found some bug in Support Resistance though. Still in progress to fix it. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#36](/thread/post/8050088#post8050088 "Post Permalink")

  * Feb 6, 2015 12:47pm  Feb 6, 2015 12:47pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting aahmad29](/thread/post/8049574#post8049574 "View Quoted Post")
> 
> Disliked
> 
> {quote} Are u still using unlimited cycles to destroy your account? Never do that. I use only one cycle at a time. Next cycle don't start until last cycle is closed. You can see progress here [http://www.forexfactory.com/showthre...18#post8049318](http://www.forexfactory.com/showthread.php?p=8049318#post8049318)
> 
> Ignored

I use unlimited not for trading actually. I use it to find the best times to execute it at 1 or 2 cycles.  
  
This parameters includes how many is the martingale factor used, and what is the best scenario and the most profitable one where I can execute 1 or 2 cycles only. From there I can manage my entry later. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#37](/thread/post/8050122#post8050122 "Post Permalink")

  * Feb 6, 2015 1:05pm  Feb 6, 2015 1:05pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar370635_1.gif) KanGKunG](kangkung)

  * Joined Apr 2014 | Status: Trader | [36 Posts](/search?do=process&provider=Member&searchuser=370635)

wonder how this system will survive during NFP.. lets see 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#38](/thread/post/8050178#post8050178 "Post Permalink")

  * Feb 6, 2015 1:43pm  Feb 6, 2015 1:43pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar302005_1.gif) csubbra](csubbra)

  * | Joined Oct 2012  | Status: PA to Warren Buffet | [118 Posts](/search?do=process&provider=Member&searchuser=302005)

thanks for this interesting thread. let me figure it out whether this method is applicable to binary options....![](https://resources.faireconomy.media/images/emojis/64/1f44f.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#39](/thread/post/8050185#post8050185 "Post Permalink")

  * Feb 6, 2015 1:54pm  Feb 6, 2015 1:54pm 

  * [ aahmad29](aahmad29)

  * Joined Aug 2012 | Status: Love for all; Hatred for none | [3,557 Posts](/search?do=process&provider=Member&searchuser=286894)

> [Quoting radityo.ardi](/thread/post/8050088#post8050088 "View Quoted Post")
> 
> Disliked
> 
> {quote} I use unlimited not for trading actually. I use it to find the best times to execute it at 1 or 2 cycles. This parameters includes how many is the martingale factor used, and what is the best scenario and the most profitable one where I can execute 1 or 2 cycles only. From there I can manage my entry later.
> 
> Ignored

I have your old version which is attached on first page but your EA is opening many orders so I stopped testing it. I am using my own EA and results are wonderful. I am confident that if you use (Gap=20 pips and TP=$2 , Account balance=$5000, Initial lot=0.02), you will never loose any account with good leverage.  
  
I have attached the report of this week results so far. I will also post the results after NFP because I am using EA 24/5. If my internet will stay active then I will be able to show the results because without internet EA can not work.  
  
If you want to see the results on candles for today then here is the link [http://www.forexfactory.com/showthre...43#post8049743](http://www.forexfactory.com/showthread.php?p=8049743#post8049743)

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Untitled.jpg
Size: 167 KB](/attachment/image/1605471/thumbnail?d=1423198275)](/attachment/image/1605471?d=1423198275)   

Love for all; Hatred for none.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#40](/thread/post/8051949#post8051949 "Post Permalink")

  * Feb 7, 2015 2:06am  Feb 7, 2015 2:06am 

  * [ aahmad29](aahmad29)

  * Joined Aug 2012 | Status: Love for all; Hatred for none | [3,557 Posts](/search?do=process&provider=Member&searchuser=286894)

I got loss of $49 because of missing candles (no data feeding) and there was big gap on Demo account. But still it is $401 profit for this week.  
  
you can check it here detail report. [http://www.forexfactory.com/showthre...20#post8051920](http://www.forexfactory.com/showthread.php?p=8051920#post8051920)  
  
Next week I am going to test with another broker with balance less than $5000 and initial lot 0.02 

Love for all; Hatred for none.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Trapping System: Tunnel Martingale
  *   * [ **Reply to Thread** ](/thread/524198-trapping-system-tunnel-martingale/reply#reply)

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

[Martingale, Anti-martingale, and Compounding](/thread/571233-martingale-anti-martingale-and-compounding "Hi all traders, 
i started this thread to meet others people interested in money management. 
We all know that martingale strategies are...") 40 replies

[Martingale, Reverse Martingale, Modified Martingale, Maths](/thread/736165-martingale-reverse-martingale-modified-martingale-maths "Hi all, so Martingale has been a risky yet maybe non profitable system. While roulette has an edge of \(2.7%/5.4%\) 
  
Inspired by Adam...") 1 reply

[How to change this Martingale to Reverse Martingale ?](/thread/546755-how-to-change-this-martingale-to-reverse-martingale "How to change this Martingale to Reverse Martingale ?") 3 replies

[Trapping System: Way to Fully-Automated Trading System](/thread/509226-trapping-system-way-to-fully-automated-trading-system "Hi fellow Traders! 
This is my first time to write a new thread. Would like to share a trading method, which at least made me happy right...") 47 replies

[Martingale vs. Non Martingale (Simplified RoR vs Profit)](/thread/526308-martingale-vs-non-martingale-simplified-ror-vs-profit "Martingale: The gambler doubles his bet after every loss... 
  
Martingale vs. Non Martingale \(Simplified RoR vs Profit in 3 trade runs...") 1 reply

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/524198-trapping-system-tunnel-martingale/reply#reply)
  * Subscribe
  * [221](javascript:void\(0\);)

Attachments: Trapping System: Tunnel Martingale

Tags: Trapping System: Tunnel Martingale

#  [](/thread/524198-trapping-system-tunnel-martingale)Trapping System: Tunnel Martingale 

  * 

  * [#41](/thread/post/8052244#post8052244 "Post Permalink")

  * Feb 7, 2015 5:00am  Feb 7, 2015 5:00am 

  * [ aahmad29](aahmad29)

  * Joined Aug 2012 | Status: Love for all; Hatred for none | [3,557 Posts](/search?do=process&provider=Member&searchuser=286894)

> [Quoting KanGKunG](/thread/post/8050122#post8050122 "View Quoted Post")
> 
> Disliked
> 
> wonder how this system will survive during NFP.. lets see
> 
> Ignored

For me, there is no doubt that system works best in NFP or other reports. I faced one issue that there was big gap of missing candle (no data feeding) on my demo account but even then my system managed the loss to keep it limited even with 0.1 lot. FOMC and other big reports gave me huge profit because there was no missing candle during these reports. 

Love for all; Hatred for none.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#42](/thread/post/8054035#post8054035 "Post Permalink")

  * Feb 9, 2015 4:05am  Feb 9, 2015 4:05am 

  * [ aahmad29](aahmad29)

  * Joined Aug 2012 | Status: Love for all; Hatred for none | [3,557 Posts](/search?do=process&provider=Member&searchuser=286894)

I have setup my EA with following settings for testing this week. I will post link here of my trading journal.  
  
[http://www.forexfactory.com/showthre...25#post8054025](http://www.forexfactory.com/showthread.php?p=8054025#post8054025)

Love for all; Hatred for none.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#43](/thread/post/8054440#post8054440 "Post Permalink")

  * Feb 9, 2015 10:12am  Feb 9, 2015 10:12am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar370635_1.gif) KanGKunG](kangkung)

  * Joined Apr 2014 | Status: Trader | [36 Posts](/search?do=process&provider=Member&searchuser=370635)

> [Quoting aahmad29](/thread/post/8052244#post8052244 "View Quoted Post")
> 
> Disliked
> 
> {quote} For me, there is no doubt that system works best in NFP or other reports. I faced one issue that there was big gap of missing candle (no data feeding) on my demo account but even then my system managed the loss to keep it limited even with 0.1 lot. FOMC and other big reports gave me huge profit because there was no missing candle during these reports.
> 
> Ignored

  
nicely done bro.. yeah problem with demo account.. hmmm but i guess should b profit.. cause we use small gap.. and 50pip in one direction to gain some profit is no prob.. unless we had use too much leverage before the result came out 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#44](/thread/post/8054586#post8054586 "Post Permalink")

  * Edited 9:52pm  Feb 9, 2015 12:16pm | Edited 9:52pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

Basically, from my observation, small gap is fine. As long as you always trade on opening market time. Best executed a few minutes before big news, or after big news.  
I'm still trying to find the best time to execute at max 3 cycles with big lots, of course big risks will follows.  
So far the current EA running (Martingale AnyTime, see on top of this thread), is having profit:  
2 Feb - -$1976 -this minus is during a testing time with 0.1 lot, and $0.5 per cycle. So Max martingale is reached and account gone crazy... ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)  
3 Feb - $25  
4 Feb - $205  
5 Feb - $22  
6 Feb - $100  
We'll see on this week how it goes... 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#45](/thread/post/8054689#post8054689 "Post Permalink")

  * Feb 9, 2015 2:46pm  Feb 9, 2015 2:46pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar370635_1.gif) KanGKunG](kangkung)

  * Joined Apr 2014 | Status: Trader | [36 Posts](/search?do=process&provider=Member&searchuser=370635)

> [Quoting radityo.ardi](/thread/post/8054586#post8054586 "View Quoted Post")
> 
> Disliked
> 
> Basically, from my observation, small gap is fine. As long as you always trade on opening market time. Best executed a few minutes before big news, or after big news. I'm still trying to find the best time to execute at max 3 cycles with big lots, of course big risks will follows. So far the current EA running (Martingale AnyTime, see on top of this thread), is having profit: 2 Feb - -$1976 -this minus is during a testing time with 0.1 lot, and $0.5 per cycle. So Max martingale is reached and account gone crazy... ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1) 3 Feb - $25 4 Feb - 205 5 Feb...
> 
> Ignored

  
what pair u use.. only 1 pair or several pair 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#46](/thread/post/8054860#post8054860 "Post Permalink")

  * Feb 9, 2015 4:50pm  Feb 9, 2015 4:50pm 

  * [ aahmad29](aahmad29)

  * Joined Aug 2012 | Status: Love for all; Hatred for none | [3,557 Posts](/search?do=process&provider=Member&searchuser=286894)

Check results of four traps with initial lot 0.02  
  
[http://www.forexfactory.com/showthre...55#post8054855](http://www.forexfactory.com/showthread.php?p=8054855#post8054855)

Love for all; Hatred for none.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#47](/thread/post/8054892#post8054892 "Post Permalink")

  * Feb 9, 2015 5:08pm  Feb 9, 2015 5:08pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting KanGKunG](/thread/post/8054689#post8054689 "View Quoted Post")
> 
> Disliked
> 
> {quote} what pair u use.. only 1 pair or several pair
> 
> Ignored

I was using only 1 EUR/USD. but I realized, EUR/USD I've started from 15:00 SGT and ended at 00:00 SGT, there's a "time-gap" that I can use for another pair.  
So now I set it up for 2, EUR/USD from 15:00 SGT to 00:00 SGT, and USD/JPY 08:00 SGT to 13:00 SGT. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#48](/thread/post/8054949#post8054949 "Post Permalink")

  * Feb 9, 2015 5:27pm  Feb 9, 2015 5:27pm 

  * [ Mariodrugs](mariodrugs)

  * | Membership Revoked  | Joined Dec 2014 | [379 Posts](/search?do=process&provider=Member&searchuser=394832)

How to fix that?!?! Non stop.. all the time.. "invalid stops" invalid stops invalid stops invalid stops... how to fix it?? I put the ea normally default, nothing changed..  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: invalid stops.png
Size: 87 KB](/attachment/image/1606938/thumbnail?d=1423470464)](/attachment/image/1606938?d=1423470464)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#49](/thread/post/8055081#post8055081 "Post Permalink")

  * Feb 9, 2015 6:08pm  Feb 9, 2015 6:08pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting Mariodrugs](/thread/post/8054949#post8054949 "View Quoted Post")
> 
> Disliked
> 
> How to fix that?!?! Non stop.. all the time.. "invalid stops" invalid stops invalid stops invalid stops... how to fix it?? I put the ea normally default, nothing changed.. {image}
> 
> Ignored

Maybe:  
Your gap is too low, too close with the Bid and Ask price. So when it tried to put BUY STOP or SELL STOP, it throws that error.  
Consider checking your spread and possibly your digits (mine is 5 digits, so 1 pip = 10 points). 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#50](/thread/post/8055125#post8055125 "Post Permalink")

  * Feb 9, 2015 6:19pm  Feb 9, 2015 6:19pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar370635_1.gif) KanGKunG](kangkung)

  * Joined Apr 2014 | Status: Trader | [36 Posts](/search?do=process&provider=Member&searchuser=370635)

> [Quoting aahmad29](/thread/post/8054860#post8054860 "View Quoted Post")
> 
> Disliked
> 
> Check results of four traps with initial lot 0.02 [http://www.forexfactory.com/showthre...55#post8054855](http://www.forexfactory.com/showthread.php?p=8054855#post8054855)
> 
> Ignored

  
is there any min gap to put order by broker rules? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#51](/thread/post/8055156#post8055156 "Post Permalink")

  * Feb 9, 2015 6:32pm  Feb 9, 2015 6:32pm 

  * [ Mariodrugs](mariodrugs)

  * | Membership Revoked  | Joined Dec 2014 | [379 Posts](/search?do=process&provider=Member&searchuser=394832)

> [Quoting radityo.ardi](/thread/post/8055081#post8055081 "View Quoted Post")
> 
> Disliked
> 
> {quote} Maybe: Your gap is too low, too close with the Bid and Ask price. So when it tried to put BUY STOP or SELL STOP, it throws that error. Consider checking your spread and possibly your digits (mine is 5 digits, so 1 pip = 10 points).
> 
> Ignored

So which settings i should change ?? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#52](/thread/post/8055282#post8055282 "Post Permalink")

  * Feb 9, 2015 7:15pm  Feb 9, 2015 7:15pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting Mariodrugs](/thread/post/8055156#post8055156 "View Quoted Post")
> 
> Disliked
> 
> {quote} So which settings i should change ??
> 
> Ignored

Just looking at your picture. Not sure you attached EA to which pair. If that is EUR/USD, your current spread is around 16 points, almost same as my broker AGEA.  
In AGEA, I can only set the gaps (safest point) is around > 50 points.  
Play the "Gaps (points)" settings, to more than 50. Otherwise, that error will keeps coming during the high spread times. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#53](/thread/post/8055383#post8055383 "Post Permalink")

  * Feb 9, 2015 7:50pm  Feb 9, 2015 7:50pm 

  * [ Mariodrugs](mariodrugs)

  * | Membership Revoked  | Joined Dec 2014 | [379 Posts](/search?do=process&provider=Member&searchuser=394832)

> [Quoting radityo.ardi](/thread/post/8055282#post8055282 "View Quoted Post")
> 
> Disliked
> 
> {quote} Just looking at your picture. Not sure you attached EA to which pair. If that is EUR/USD, your current spread is around 16 points, almost same as my broker AGEA. In AGEA, I can only set the gaps (safest point) is around > 50 points. Play the "Gaps (points)" settings, to more than 50. Otherwise, that error will keeps coming during the high spread times.
> 
> Ignored

still not understand ![](https://resources.faireconomy.media/images/emojis/64/1f641.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#54](/thread/post/8055546#post8055546 "Post Permalink")

  * Feb 9, 2015 8:51pm  Feb 9, 2015 8:51pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting Mariodrugs](/thread/post/8055383#post8055383 "View Quoted Post")
> 
> Disliked
> 
> {quote} still not understand ![](https://resources.faireconomy.media/images/emojis/64/1f641.png?v=15.1)
> 
> Ignored

I think you should read the very first thread in the first page, to understand what is Gap, and where are the settings, and how to modif the settings. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#55](/thread/post/8055588#post8055588 "Post Permalink")

  * Feb 9, 2015 9:09pm  Feb 9, 2015 9:09pm 

  * [ Mariodrugs](mariodrugs)

  * | Membership Revoked  | Joined Dec 2014 | [379 Posts](/search?do=process&provider=Member&searchuser=394832)

This strategy looks like holy grail! Why you give it to people for free ;-) ? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#56](/thread/post/8055659#post8055659 "Post Permalink")

  * Feb 9, 2015 9:36pm  Feb 9, 2015 9:36pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting Mariodrugs](/thread/post/8055588#post8055588 "View Quoted Post")
> 
> Disliked
> 
> This strategy looks like holy grail! Why you give it to people for free ;-) ?
> 
> Ignored

Probably KanGKunG can answer best for this since he is the one popped out in my PM requested for this EA to be built, but let me try to answer yours. This strategy is free, same free as you can get it from internet. Search it for "martingale", you can get a lot of references regarding this, simple to understand, easy to use. And according to Wikipedia, it is already there since 18th Century.  
  
The reason why I want to share this:

  1. Knowing the fact that this strategy was there since my great-great-grandfather still enjoying his early stubborn life, I don't think it is fair to keep this thing in our pocket. So I decided to wrote EA as requested by KanGKunG and share it freely.
  2. Bear in mind, this strategy requires a lot of money management strategy (as said by KanGKunG). Holy Grail strategy (or whatever you say), but it comes with a great risk as well. Once you put big Lots, or big target, then you'll drop your account to the ground.
  3. No one has ever _coded this strategy and share it freely_ (I think), and [inspired by this thread as well](http://www.forexfactory.com/showthread.php?t=515891) which this guy had decided to share his EA freely. C'mon... 18th century was a loooong time ago, but no one decided to share this free???

  
1 request from me is simple, if you get profit from this EA and decided to pay for this,  
please pay for the needy family and poor childrens for their better educations... ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#57](/thread/post/8055677#post8055677 "Post Permalink")

  * Feb 9, 2015 9:44pm  Feb 9, 2015 9:44pm 

  * [ Mariodrugs](mariodrugs)

  * | Membership Revoked  | Joined Dec 2014 | [379 Posts](/search?do=process&provider=Member&searchuser=394832)

Ha ha ha! Bro you're nice guy! ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1) If i will make suppose 100.000$ i will send you money 10% ;-)   
  
Best wishes! Lets test it on some demo now. ;-) 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#58](/thread/post/8055690#post8055690 "Post Permalink")

  * Edited 10:11pm  Feb 9, 2015 9:47pm | Edited 10:11pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

Guys, just trying to get a good run since it was "perfectly" ran last week, I'm gonna shift the _Trade Explorer "Martingale AnyTime" to 3 Feb_.  
Why? I want a quick preview of the profit started since it was running both EUR/USD and USD/JPY. I'm tired of doing calculation everytime I see Trade Graph by Days... ![](https://resources.faireconomy.media/images/emojis/64/1f61f.png?v=15.1)  
  
I hope it won't reach the max martingale again in the future....  
  
Another news:  
there was an issue with "Start with Support and Resistance" if you attach it day by day. That's because I didn't do any reset when the day is over. I have the fixes, v1.04, but not fully tested yet. So, be patience...  
Moreover, I think in the future I will join this Martingale strategy with my Morning Strike strategy... see this guy's TE, [1 flaw was there, but after that, never fails](http://www.forexfactory.com/edyardy/59) (damn....!) ![](https://resources.faireconomy.media/images/emojis/64/1f911.png?v=15.1)

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#59](/thread/post/8055804#post8055804 "Post Permalink")

  * Feb 9, 2015 10:19pm  Feb 9, 2015 10:19pm 

  * [ Mariodrugs](mariodrugs)

  * | Membership Revoked  | Joined Dec 2014 | [379 Posts](/search?do=process&provider=Member&searchuser=394832)

I have one more question to you my friend. Is this working for couple of pairs? Can I put this EA on EURUSD, USDJPY, GBPUSD in the same time? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#60](/thread/post/8055882#post8055882 "Post Permalink")

  * Feb 9, 2015 10:50pm  Feb 9, 2015 10:50pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting Mariodrugs](/thread/post/8055804#post8055804 "View Quoted Post")
> 
> Disliked
> 
> I have one more question to you my friend. Is this working for couple of pairs? Can I put this EA on EURUSD, USDJPY, GBPUSD in the same time?
> 
> Ignored

Hmm... that depends on the money management you are using. If you (say) have balance for $50000, then you can start with say 5 or more pairs, with say 0.1 starting lots, and targetting at $0.5 for each cycle, probably?  
  
Personally I don't try to overlap the settings between pairs.  
For example, sorry if I use SGT (Singapore Time):  
USDJPY there are 2 times when it will be good for trading, which is when Japan market open, or you can extend it to the whole day until when US market is about to close.  
But if you plan to use 2 pairs, then you have to manage like this:  
USDJPY at 8:00 SGT - 13:00 SGT, and then start for EURUSD 15:00 SGT - 24:00 SGT. This is my current settings, running under VPS 24/7. Started at $3000, targetting at $0.20 per each cycle, and started with 0.02 lots. Which means literally opens 2 chart attached with the same EA, but different settings (time frame).  
  
There are 2 hours gap (13:00 SGT - 15:00 SGT), during that time, my EA will still running, but not for opening new cycle. It will try to complete the existing running cycle. My best suggestion would be to avoid overlapping of 2 different pairs at the same time.  
  
I don't think there's a restriction of what pair you can trade, as long as the chart is moving somewhere... 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Trapping System: Tunnel Martingale
  *   * [ **Reply to Thread** ](/thread/524198-trapping-system-tunnel-martingale/reply#reply)

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

[Martingale, Anti-martingale, and Compounding](/thread/571233-martingale-anti-martingale-and-compounding "Hi all traders, 
i started this thread to meet others people interested in money management. 
We all know that martingale strategies are...") 40 replies

[Martingale, Reverse Martingale, Modified Martingale, Maths](/thread/736165-martingale-reverse-martingale-modified-martingale-maths "Hi all, so Martingale has been a risky yet maybe non profitable system. While roulette has an edge of \(2.7%/5.4%\) 
  
Inspired by Adam...") 1 reply

[How to change this Martingale to Reverse Martingale ?](/thread/546755-how-to-change-this-martingale-to-reverse-martingale "How to change this Martingale to Reverse Martingale ?") 3 replies

[Trapping System: Way to Fully-Automated Trading System](/thread/509226-trapping-system-way-to-fully-automated-trading-system "Hi fellow Traders! 
This is my first time to write a new thread. Would like to share a trading method, which at least made me happy right...") 47 replies

[Martingale vs. Non Martingale (Simplified RoR vs Profit)](/thread/526308-martingale-vs-non-martingale-simplified-ror-vs-profit "Martingale: The gambler doubles his bet after every loss... 
  
Martingale vs. Non Martingale \(Simplified RoR vs Profit in 3 trade runs...") 1 reply

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/524198-trapping-system-tunnel-martingale/reply#reply)
  * Subscribe
  * [221](javascript:void\(0\);)

Attachments: Trapping System: Tunnel Martingale

Tags: Trapping System: Tunnel Martingale

#  [](/thread/524198-trapping-system-tunnel-martingale)Trapping System: Tunnel Martingale 

  * 

  * [#61](/thread/post/8055991#post8055991 "Post Permalink")

  * Feb 9, 2015 11:32pm  Feb 9, 2015 11:32pm 

  * [ addy5280](addy5280)

  * | Joined Nov 2010  | Status: Trader | [28 Posts](/search?do=process&provider=Member&searchuser=160534)

Help!  
Can anyone upload the ea,I can't download it in china.Thank you! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#62](/thread/post/8056016#post8056016 "Post Permalink")

  * Feb 9, 2015 11:41pm  Feb 9, 2015 11:41pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting addy5280](/thread/post/8055991#post8055991 "View Quoted Post")
> 
> Disliked
> 
> Help! Can anyone upload the ea,I can't download it in china.Thank you!
> 
> Ignored

Whhooowww....sorry bro... I thought dropbox is accessible in ur place. See below... 

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [TunnelMartingale.ex4](/attachment/file/1607309?d=1423492847) 53 KB | 644 downloads 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#63](/thread/post/8056265#post8056265 "Post Permalink")

  * Edited 2:33am  Feb 10, 2015 1:36am | Edited 2:33am 

  * [ Mariodrugs](mariodrugs)

  * | Membership Revoked  | Joined Dec 2014 | [379 Posts](/search?do=process&provider=Member&searchuser=394832)

Everything was ok, until its made situation like this:  
  
Sell didnt opened...  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: everything was ok.png
Size: 45 KB](/attachment/image/1607388/thumbnail?d=1423499778)](/attachment/image/1607388?d=1423499778)   

  
  
i think some bugs... ;/  
  
That was because sell closed before at trail stop..  
  
How to turn off trail stop and stop loss ??? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#64](/thread/post/8056478#post8056478 "Post Permalink")

  * Feb 10, 2015 3:56am  Feb 10, 2015 3:56am 

  * [ aahmad29](aahmad29)

  * Joined Aug 2012 | Status: Love for all; Hatred for none | [3,557 Posts](/search?do=process&provider=Member&searchuser=286894)

> [Quoting KanGKunG](/thread/post/8055125#post8055125 "View Quoted Post")
> 
> Disliked
> 
> {quote} is there any min gap to put order by broker rules?
> 
> Ignored

My broker has no minimum gap rule.  
  
More profit [http://www.forexfactory.com/showthre...93#post8056493](http://www.forexfactory.com/showthread.php?p=8056493#post8056493)

Love for all; Hatred for none.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#65](/thread/post/8056741#post8056741 "Post Permalink")

  * Feb 10, 2015 7:52am  Feb 10, 2015 7:52am 

  * [ Mariodrugs](mariodrugs)

  * | Membership Revoked  | Joined Dec 2014 | [379 Posts](/search?do=process&provider=Member&searchuser=394832)

How to delete trail stops and stop loses ?  
  
Because sometimes, positions aren't closing all. Sometimes Only profitable positions are closing, and loses positions arent closing ![](https://resources.faireconomy.media/images/emojis/64/1f641.png?v=15.1) how to fix it ? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#66](/thread/post/8057051#post8057051 "Post Permalink")

  * Feb 10, 2015 11:44am  Feb 10, 2015 11:44am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar370635_1.gif) KanGKunG](kangkung)

  * Joined Apr 2014 | Status: Trader | [36 Posts](/search?do=process&provider=Member&searchuser=370635)

there is no system that is holy grail in fx.. and i just share idea how to trade even the original idea actually had been done by others.. and for me if I already can make money from the market, y should i take money from others. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#67](/thread/post/8057055#post8057055 "Post Permalink")

  * Feb 10, 2015 11:45am  Feb 10, 2015 11:45am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar370635_1.gif) KanGKunG](kangkung)

  * Joined Apr 2014 | Status: Trader | [36 Posts](/search?do=process&provider=Member&searchuser=370635)

> [Quoting aahmad29](/thread/post/8056478#post8056478 "View Quoted Post")
> 
> Disliked
> 
> {quote} My broker has no minimum gap rule. More profit [http://www.forexfactory.com/showthre...93#post8056493](http://www.forexfactory.com/showthread.php?p=8056493#post8056493)
> 
> Ignored

  
hmmm thats weird 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#68](/thread/post/8057077#post8057077 "Post Permalink")

  * Feb 10, 2015 12:05pm  Feb 10, 2015 12:05pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting Mariodrugs](/thread/post/8056741#post8056741 "View Quoted Post")
> 
> Disliked
> 
> How to delete trail stops and stop loses ? Because sometimes, positions aren't closing all. Sometimes Only profitable positions are closing, and loses positions arent closing ![](https://resources.faireconomy.media/images/emojis/64/1f641.png?v=15.1) how to fix it ?
> 
> Ignored

Hmm... would you let me know what is ur broker, and probably dump your settings to a file, then post it here. Let me check it out.  
I never get any issue like yours, when only profitable orders that are closed. The link of the orders and EA is using Magic Number. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#69](/thread/post/8057104#post8057104 "Post Permalink")

  * Edited 12:51pm  Feb 10, 2015 12:39pm | Edited 12:51pm 

  * [ addy5280](addy5280)

  * | Joined Nov 2010  | Status: Trader | [28 Posts](/search?do=process&provider=Member&searchuser=160534)

some bugs？？  
1.Firstly, I want it will do BUY 0.01 lot at the current price, then SELL STOP 0.02 lots at the current BUY price.(ea not do like this)  
2.look,when euraud/gbpaud open 0.02,but not BUY STOP/SELL stop 0.04?  
3.I want to use it in several pair at the same time。  
sorry for my pool English!  
My broker is [exness](/brokers/exness "View Exness Broker Profile").  
I think the ea will be real Holy Grail.  
_radityo.ardi_ ,can you help me ? 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: QQå›¾ç‰‡20150210112912.jpg
Size: 131 KB](/attachment/image/1607712/thumbnail?d=1423539900)](/attachment/image/1607712?d=1423539900)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#70](/thread/post/8057111#post8057111 "Post Permalink")

  * Feb 10, 2015 12:45pm  Feb 10, 2015 12:45pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting addy5280](/thread/post/8057104#post8057104 "View Quoted Post")
> 
> Disliked
> 
> {image} some bugs？？ 1.Firstly, wo want it will do BUY 0.01 lot at the current price, then SELL STOP 0.02 lots at the current BUY price.(ea not do like this) 2.look,when euraud/gbpaud open 0.2,but not BUY STOP/SELL stop 0.4? sorry for my pool English! My broker is exness. I think the ea will be real Holy Grail. radityo.ardi ,can you help me ?
> 
> Ignored

I can't see your image.  
just click Upload Screenshot, and paste the image you copied from your clipboard. That will be easier. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#71](/thread/post/8057169#post8057169 "Post Permalink")

  * Feb 10, 2015 2:02pm  Feb 10, 2015 2:02pm 

  * [ addy5280](addy5280)

  * | Joined Nov 2010  | Status: Trader | [28 Posts](/search?do=process&provider=Member&searchuser=160534)

> [Quoting radityo.ardi](/thread/post/8057111#post8057111 "View Quoted Post")
> 
> Disliked
> 
> {quote} I can't see your image. just click Upload Screenshot, and paste the image you copied from your clipboard. That will be easier.
> 
> Ignored

  
look：usdcad，there is no 0.01 and 0.02,but buy stop 0.04??? 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: QQå›¾ç‰‡20150210125852.png
Size: 56 KB](/attachment/image/1607738/thumbnail?d=1423544459)](/attachment/image/1607738?d=1423544459)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#72](/thread/post/8057192#post8057192 "Post Permalink")

  * Feb 10, 2015 2:21pm  Feb 10, 2015 2:21pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting addy5280](/thread/post/8057104#post8057104 "View Quoted Post")
> 
> Disliked
> 
> some bugs？？ 1.Firstly, I want it will do BUY 0.01 lot at the current price, then SELL STOP 0.02 lots at the current BUY price.(ea not do like this) 2.look,when euraud/gbpaud open 0.02,but not BUY STOP/SELL stop 0.04? 3.I want to use it in several pair at the same time。 sorry for my pool English! My broker is exness. I think the ea will be real Holy Grail. radityo.ardi ,can you help me ? {image}
> 
> Ignored

You created a lot of things there.  
What I can see is:  
1\. eurjpym is good  
2\. gbpjpym is good  
3\. gbpusdm is good  
4\. nzdusdm is good  
5\. usdjpym is good  
  
now for gbpcadm, and euraudm, not sure why it wasn't added new BUY STOP, by my suspect is your EA's magic number is conflicting.  
Can you provide different MagicNumber for each EA you run? Note that this is not a bug. EA will place order and calculate based on magic number. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#73](/thread/post/8057272#post8057272 "Post Permalink")

  * Feb 10, 2015 3:40pm  Feb 10, 2015 3:40pm 

  * [ addy5280](addy5280)

  * | Joined Nov 2010  | Status: Trader | [28 Posts](/search?do=process&provider=Member&searchuser=160534)

I have changed the magic number for every pair,but the ea open new order and close the order frequently.  
I don't know why?

Attached Image (click to enlarge)

[![Click to Enlarge

Name: QQå›¾ç‰‡20150210143538.jpg
Size: 123 KB](/attachment/image/1607783/thumbnail?d=1423550373)](/attachment/image/1607783?d=1423550373)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#74](/thread/post/8057308#post8057308 "Post Permalink")

  * Feb 10, 2015 4:05pm  Feb 10, 2015 4:05pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting addy5280](/thread/post/8057272#post8057272 "View Quoted Post")
> 
> Disliked
> 
> I have changed the magic number for every pair,but the ea open new order and close the order frequently. I don't know why? {image}
> 
> Ignored

Can you give me step by step how you did attach the EA to your chart?  
Probably with some screenshots as well.  
  
I can't tell what's happening by looking at 1 screenshot. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#75](/thread/post/8057424#post8057424 "Post Permalink")

  * Edited 5:34pm  Feb 10, 2015 5:12pm | Edited 5:34pm 

  * [ Mariodrugs](mariodrugs)

  * | Membership Revoked  | Joined Dec 2014 | [379 Posts](/search?do=process&provider=Member&searchuser=394832)

Today i put EA into chart and it doesnt work. Dont even want to open positions..  
  
My demo-broker is [IC MARKETS](/brokers/ic-markets "View IC Markets Broker Profile"). Very low [spreads](/brokers/spreads "View Live Spreads on the Broker Guide").  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: settings martingale.png
Size: 172 KB](/attachment/image/1607827/thumbnail?d=1423555913)](/attachment/image/1607827?d=1423555913)   

  
  
  
Ahh ! I have found solution for open. Its time! There was 10:00 ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) and I changed it into 8:00 ! ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
  
But still not found solution for delete trail stop and trail be.. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#76](/thread/post/8057567#post8057567 "Post Permalink")

  * Feb 10, 2015 6:06pm  Feb 10, 2015 6:06pm 

  * [ Mariodrugs](mariodrugs)

  * | Membership Revoked  | Joined Dec 2014 | [379 Posts](/search?do=process&provider=Member&searchuser=394832)

That is the result by this bug:   
  
Sell position closed at profit. Buy position didnt closed....  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: next bug.png
Size: 64 KB](/attachment/image/1607873/thumbnail?d=1423559197)](/attachment/image/1607873?d=1423559197)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#77](/thread/post/8057629#post8057629 "Post Permalink")

  * Feb 10, 2015 6:25pm  Feb 10, 2015 6:25pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting Mariodrugs](/thread/post/8057567#post8057567 "View Quoted Post")
> 
> Disliked
> 
> That is the result by this bug: Sell position closed at profit. Buy position didnt closed.... {image}
> 
> Ignored

OK, that is genuine bug I think, very strange that this behaviour is not on my running EA.  
  
A few questions:  
1\. Did you clicked on close order accidentally? Or maybe somehow you stop the EA then run again?  
2\. Did you change the content on comment section? I set it as number of 0, 1, 2, in any case that should not be changed.  
3\. Can you get me your "Experts" tab log, or "Journal" log? 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#78](/thread/post/8057868#post8057868 "Post Permalink")

  * Feb 10, 2015 7:35pm  Feb 10, 2015 7:35pm 

  * [ aahmad29](aahmad29)

  * Joined Aug 2012 | Status: Love for all; Hatred for none | [3,557 Posts](/search?do=process&provider=Member&searchuser=286894)

Here is some more profit  
[http://www.forexfactory.com/showthre...17#post8057717](http://www.forexfactory.com/showthread.php?p=8057717#post8057717)

Love for all; Hatred for none.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#79](/thread/post/8058015#post8058015 "Post Permalink")

  * Edited 9:48pm  Feb 10, 2015 8:31pm | Edited 9:48pm 

  * [ Mariodrugs](mariodrugs)

  * | Membership Revoked  | Joined Dec 2014 | [379 Posts](/search?do=process&provider=Member&searchuser=394832)

> [Quoting radityo.ardi](/thread/post/8057629#post8057629 "View Quoted Post")
> 
> Disliked
> 
> {quote} OK, that is genuine bug I think, very strange that this behaviour is not on my running EA. A few questions: 1. Did you clicked on close order accidentally? Or maybe somehow you stop the EA then run again? 2. Did you change the content on comment section? I set it as number of 0, 1, 2, in any case that should not be changed. 3. Can you get me your "Experts" tab log, or "Journal" log?
> 
> Ignored

Ad1. No I didnt clicked accidentally. I didnt stop EA.  
Ad2. I did not change nothing.  
**Ad3. Where is experts tab log and journal log ?**  
  
  
**And here next situation - > no** buy stop.. only sell stop and sell position oppened.. weird..  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: next bug 2.png
Size: 40 KB](/attachment/image/1608005/thumbnail?d=1423568269)](/attachment/image/1608005?d=1423568269)   

  
  
  
Next situation --> sell closed at stop lose. Buy didnt closed. And second opened buy like on screen below:  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Stop loos.png
Size: 107 KB](/attachment/image/1608016/thumbnail?d=1423569283)](/attachment/image/1608016?d=1423569283)   

  
  
That happen on my eyes. I didnt clicked anything!  
  
Next situation.. This EA doesnt work properly in 100%. Strategy is good, but EA is something wrong.. there is some bug.. ;-/  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: next bug 3.png
Size: 49 KB](/attachment/image/1608064/thumbnail?d=1423572266)](/attachment/image/1608064?d=1423572266)   

  
  
Next bug... before it was 6 pips between SELL STOP and BUY STOP, now it changed to 36 pips between SELL STOP and BUY STOP why? bug?  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: next bug 4.png
Size: 26 KB](/attachment/image/1608068/thumbnail?d=1423572475)](/attachment/image/1608068?d=1423572475)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#80](/thread/post/8058340#post8058340 "Post Permalink")

  * Feb 10, 2015 10:06pm  Feb 10, 2015 10:06pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting Mariodrugs](/thread/post/8058015#post8058015 "View Quoted Post")
> 
> Disliked
> 
> {quote} Ad1. No I didnt clicked accidentally. I didnt stop EA. Ad2. I did not change nothing. Ad3. Where is experts tab log and journal log ? And here next situation -> no buy stop.. only sell stop and sell position oppened.. weird.. {image} Next situation --> sell closed at stop lose. Buy didnt closed. And second opened buy like on screen below: {image} That happen on my eyes. I didnt clicked anything! Next situation.. This EA doesnt work properly in 100%. Strategy is good, but EA is something wrong.. there is some bug.. ;-/ {image} Next bug......
> 
> Ignored

Will check that.  
Anyway got another bugs from Support and Resistance scenario. Let me check that up. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Trapping System: Tunnel Martingale
  *   * [ **Reply to Thread** ](/thread/524198-trapping-system-tunnel-martingale/reply#reply)

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

[Martingale, Anti-martingale, and Compounding](/thread/571233-martingale-anti-martingale-and-compounding "Hi all traders, 
i started this thread to meet others people interested in money management. 
We all know that martingale strategies are...") 40 replies

[Martingale, Reverse Martingale, Modified Martingale, Maths](/thread/736165-martingale-reverse-martingale-modified-martingale-maths "Hi all, so Martingale has been a risky yet maybe non profitable system. While roulette has an edge of \(2.7%/5.4%\) 
  
Inspired by Adam...") 1 reply

[How to change this Martingale to Reverse Martingale ?](/thread/546755-how-to-change-this-martingale-to-reverse-martingale "How to change this Martingale to Reverse Martingale ?") 3 replies

[Trapping System: Way to Fully-Automated Trading System](/thread/509226-trapping-system-way-to-fully-automated-trading-system "Hi fellow Traders! 
This is my first time to write a new thread. Would like to share a trading method, which at least made me happy right...") 47 replies

[Martingale vs. Non Martingale (Simplified RoR vs Profit)](/thread/526308-martingale-vs-non-martingale-simplified-ror-vs-profit "Martingale: The gambler doubles his bet after every loss... 
  
Martingale vs. Non Martingale \(Simplified RoR vs Profit in 3 trade runs...") 1 reply

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/524198-trapping-system-tunnel-martingale/reply#reply)
  * Subscribe
  * [221](javascript:void\(0\);)

Attachments: Trapping System: Tunnel Martingale

Tags: Trapping System: Tunnel Martingale

#  [](/thread/524198-trapping-system-tunnel-martingale)Trapping System: Tunnel Martingale 

  * 

  * [#81](/thread/post/8058471#post8058471 "Post Permalink")

  * Feb 10, 2015 10:39pm  Feb 10, 2015 10:39pm 

  * [ Mariodrugs](mariodrugs)

  * | Membership Revoked  | Joined Dec 2014 | [379 Posts](/search?do=process&provider=Member&searchuser=394832)

Settings martingale EA:  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: settings.png
Size: 108 KB](/attachment/image/1608125/thumbnail?d=1423575552)](/attachment/image/1608125?d=1423575552)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#82](/thread/post/8059273#post8059273 "Post Permalink")

  * Feb 11, 2015 4:23am  Feb 11, 2015 4:23am 

  * [ aahmad29](aahmad29)

  * Joined Aug 2012 | Status: Love for all; Hatred for none | [3,557 Posts](/search?do=process&provider=Member&searchuser=286894)

> [Quoting radityo.ardi](/thread/post/8058340#post8058340 "View Quoted Post")
> 
> Disliked
> 
> {quote} Will check that. Anyway got another bugs from Support and Resistance scenario. Let me check that up.
> 
> Ignored

Profit $31. Progress so far for this week with following settings  
  
\- Always buy first (but sometimes I change it to sell)  
\- Initial lot = 0.02  
\- Gap = 20 Pips  
\- Leverage = 1:100 (Bit risky)  
  
[http://www.forexfactory.com/showthre...63#post8059263](http://www.forexfactory.com/showthread.php?p=8059263#post8059263)

Love for all; Hatred for none.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#83](/thread/post/8059790#post8059790 "Post Permalink")

  * Feb 11, 2015 11:14am  Feb 11, 2015 11:14am 

  * [ addy5280](addy5280)

  * | Joined Nov 2010  | Status: Trader | [28 Posts](/search?do=process&provider=Member&searchuser=160534)

Attached Image (click to enlarge)

[![Click to Enlarge

Name: QQå›¾ç‰‡20150211092252.jpg
Size: 116 KB](/attachment/image/1608551/thumbnail?d=1423620844)](/attachment/image/1608551?d=1423620844)   

Attached Image (click to enlarge)

[![Click to Enlarge

Name: QQå›¾ç‰‡20150211092258.jpg
Size: 119 KB](/attachment/image/1608552/thumbnail?d=1423620850)](/attachment/image/1608552?d=1423620850)   

Attached Image (click to enlarge)

[![Click to Enlarge

Name: QQå›¾ç‰‡20150211092626.jpg
Size: 99 KB](/attachment/image/1608553/thumbnail?d=1423620856)](/attachment/image/1608553?d=1423620856)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#84](/thread/post/8059795#post8059795 "Post Permalink")

  * Feb 11, 2015 11:23am  Feb 11, 2015 11:23am 

  * [ addy5280](addy5280)

  * | Joined Nov 2010  | Status: Trader | [28 Posts](/search?do=process&provider=Member&searchuser=160534)

help:  
1.pls help to modify it for using in several pair at the same time;  
2.don't open new order and close the order frequently. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#85](/thread/post/8059803#post8059803 "Post Permalink")

  * Feb 11, 2015 11:33am  Feb 11, 2015 11:33am 

  * [ addy5280](addy5280)

  * | Joined Nov 2010  | Status: Trader | [28 Posts](/search?do=process&provider=Member&searchuser=160534)

> [Quoting SwingMan](/thread/post/8035376#post8035376 "View Quoted Post")
> 
> Disliked
> 
> Just found in internet: Forex Trading & Martingale Infographic: [http://forexuseful.com/authors/forex...le-infographic](http://forexuseful.com/authors/forex-useful/forex-trading-martingale-infographic)
> 
> Ignored

  
hi SwingMan,  
1.pls help to modify it for using in several pair at the same time;  
2.don't open new order and close the order frequently.  
  
Pls help!  
Thank you a lot! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#86](/thread/post/8059810#post8059810 "Post Permalink")

  * Feb 11, 2015 11:41am  Feb 11, 2015 11:41am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting addy5280](/thread/post/8059795#post8059795 "View Quoted Post")
> 
> Disliked
> 
> help: 1.pls help to modify it for using in several pair at the same time; 2.don't open new order and close the order frequently.
> 
> Ignored

Hold on...  
I'm still in the progress of checking it. Don't expect it to be finished in 5 minutes, okay?  
  
I'm in the middle of testing it. Basically should work for multiple currency, as you can see in the Trade Explorer above this thread, that is now using USD/JPY, later on EUR/USD. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#87](/thread/post/8059851#post8059851 "Post Permalink")

  * Feb 11, 2015 1:14pm  Feb 11, 2015 1:14pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting Mariodrugs](/thread/post/8058015#post8058015 "View Quoted Post")
> 
> Disliked
> 
> {quote} Ad1. No I didnt clicked accidentally. I didnt stop EA. Ad2. I did not change nothing. Ad3. Where is experts tab log and journal log ? And here next situation -> no buy stop.. only sell stop and sell position oppened.. weird.. {image} Next situation --> sell closed at stop lose. Buy didnt closed. And second opened buy like on screen below: {image} That happen on my eyes. I didnt clicked anything! Next situation.. This EA doesnt work properly in 100%. Strategy is good, but EA is something wrong.. there is some bug.. ;-/ {image} Next bug......
> 
> Ignored

Mariodrugs,  
let us check the issue 1 by 1, let me list down the issues you've reported so far:

  1. No BUY STOP, only SELL and SELL STOP opened.  
This maybe due to suppressing the Alert (probably alert was there but suppressed). When you attach EA, there's a settings "Disable alert once hit". If this checked, then you no longer receives any alerts in case of error. Most likely the error because of the BUY STOP was too close with Bid price.
  2. SELL closed at STOP LOSS (if I'm not wrong, u typed "lose" means "loss", am I right?), BUY didn't closed  
I'll check again the scenario. But would you mind to export your settings of this EA and attach it to your post reply?
  3. Before it was 6 pips gaps, now changed to 36 pips gaps  
Probably this is known bug from MetaTrader, that if we update the ex4 in the middle of attaching this EA to a chart, the whole settings will be reverted back to defaults. But just to make sure, did you update your EA while attaching it to some chart?

I can't tell anything but please download the latest v1.04 from the first thread and retest. The Experts and Journal tab is on the same tab as your Trade tab.  
  
If bug happens again, please get me these things (attach it to your post reply):  
\- Journal tab log and get the file (see below)  
\- Experts tab log and get the file (see below)  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot1.png
Size: 64 KB](/attachment/image/1608587/thumbnail?d=1423627544)](/attachment/image/1608587?d=1423627544)   

  
  
\- Export the current settings of the EA. This can be done by right clicking the chart that is attached with this EA, then "Expert Advisors" > "Properties". Then on the window that is opening, click "Save". Copy the file and attach it to your post reply as well. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#88](/thread/post/8059857#post8059857 "Post Permalink")

  * Feb 11, 2015 1:21pm  Feb 11, 2015 1:21pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting addy5280](/thread/post/8059795#post8059795 "View Quoted Post")
> 
> Disliked
> 
> help: 1.pls help to modify it for using in several pair at the same time; 2.don't open new order and close the order frequently.
> 
> Ignored

Several pairs at the same time is OK currently for my scenario.  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot1.png
Size: 178 KB](/attachment/image/1608591/thumbnail?d=1423628179)](/attachment/image/1608591?d=1423628179)   

  
And one of them was closed perfectly.  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot2.png
Size: 80 KB](/attachment/image/1608593/thumbnail?d=1423628321)](/attachment/image/1608593?d=1423628321)   

  
How to make it? Make sure you posted a different MagicNumber for each of the chart attached.  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot3.png
Size: 91 KB](/attachment/image/1608594/thumbnail?d=1423628438)](/attachment/image/1608594?d=1423628438)   

  
  
I've uploaded the latest v1.04 to the first thread. Please download and retest it again. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#89](/thread/post/8059862#post8059862 "Post Permalink")

  * Feb 11, 2015 1:26pm  Feb 11, 2015 1:26pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting aahmad29](/thread/post/8059273#post8059273 "View Quoted Post")
> 
> Disliked
> 
> {quote} Profit $31. Progress so far for this week with following settings - Always buy first (but sometimes I change it to sell) - Initial lot = 0.02 - Gap = 20 Pips - Leverage = 1:100 (Bit risky) [http://www.forexfactory.com/showthre...63#post8059263](http://www.forexfactory.com/showthread.php?p=8059263#post8059263)
> 
> Ignored

Great man!!!  
Indeed 1:100 is risky if you decided to run AnyTime. Mine is [tickmill](/brokers/tickmill "View Tickmill Broker Profile"), which is 1:500. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#90](/thread/post/8059890#post8059890 "Post Permalink")

  * Feb 11, 2015 1:57pm  Feb 11, 2015 1:57pm 

  * [ ejikz](ejikz)

  * | Joined Jan 2010  | Status: Trader | [124 Posts](/search?do=process&provider=Member&searchuser=131860)

@ Radityo  
  
Thank you for all the effort you put into the EA development 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#91](/thread/post/8060107#post8060107 "Post Permalink")

  * Feb 11, 2015 4:43pm  Feb 11, 2015 4:43pm 

  * [ Mariodrugs](mariodrugs)

  * | Membership Revoked  | Joined Dec 2014 | [379 Posts](/search?do=process&provider=Member&searchuser=394832)

> [Quoting radityo.ardi](/thread/post/8059851#post8059851 "View Quoted Post")
> 
> Disliked
> 
> {quote} Mariodrugs, let us check the issue 1 by 1, let me list down the issues you've reported so far: No BUY STOP, only SELL and SELL STOP opened. This maybe due to suppressing the Alert (probably alert was there but suppressed). When you attach EA, there's a settings "Disable alert once hit". If this checked, then you no longer receives any alerts in case of error. Most likely the error because of the BUY STOP was too close with Bid price. SELL closed at STOP LOSS (if I'm not wrong, u typed "lose" means "loss", am I right?), BUY didn't closed...
> 
> Ignored

Thanks friend for helping me! I have downloaded 1.04 now and testing. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#92](/thread/post/8060136#post8060136 "Post Permalink")

  * Feb 11, 2015 4:53pm  Feb 11, 2015 4:53pm 

  * [ aahmad29](aahmad29)

  * Joined Aug 2012 | Status: Love for all; Hatred for none | [3,557 Posts](/search?do=process&provider=Member&searchuser=286894)

> [Quoting radityo.ardi](/thread/post/8059862#post8059862 "View Quoted Post")
> 
> Disliked
> 
> {quote} Great man!!! Indeed 1:100 is risky if you decided to run AnyTime. Mine is tickmill, which is 1:500.
> 
> Ignored

My live account is 1:1000 but on Friday 2 hours before closing the market it is changed to 1:200 and then 2 hours after opening the market on Sunday, it changes back to 1:1000 

Love for all; Hatred for none.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#93](/thread/post/8060211#post8060211 "Post Permalink")

  * Edited 5:55pm  Feb 11, 2015 5:20pm | Edited 5:55pm 

  * [ Mariodrugs](mariodrugs)

  * | Membership Revoked  | Joined Dec 2014 | [379 Posts](/search?do=process&provider=Member&searchuser=394832)

ok. there is error now. Channel Martingale ver. 1.04  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: no sell stop situation.png
Size: 55 KB](/attachment/image/1608706/thumbnail?d=1423642641)](/attachment/image/1608706?d=1423642641)   

  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: gap changed.png
Size: 49 KB](/attachment/image/1608708/thumbnail?d=1423642876)](/attachment/image/1608708?d=1423642876)   

  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: log.png
Size: 287 KB](/attachment/image/1608725/thumbnail?d=1423643952)](/attachment/image/1608725?d=1423643952)   

  
  
10 seconds later....  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: later.png
Size: 47 KB](/attachment/image/1608726/thumbnail?d=1423644014)](/attachment/image/1608726?d=1423644014)   

  
  
  
I can't upload here martingale.set saved. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#94](/thread/post/8060305#post8060305 "Post Permalink")

  * Feb 11, 2015 5:53pm  Feb 11, 2015 5:53pm 

  * [ Mariodrugs](mariodrugs)

  * | Membership Revoked  | Joined Dec 2014 | [379 Posts](/search?do=process&provider=Member&searchuser=394832)

20150211.txt is a .log file. Please change '.txt' into '.log' file and you can check. This is the only way how i Can upload that ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)  

Attached File(s)

![File Type: txt](https://assets.faireconomy.media/images/attach/txt.gif) [20150211.txt](/attachment/file/1608738?d=1423644782) 31 KB | 803 downloads 

  
  
martingale channel.txt change into martingale channel.set 

Attached File(s)

![File Type: txt](https://assets.faireconomy.media/images/attach/txt.gif) [martingale channel.txt](/attachment/file/1608739?d=1423644840) 1 KB | 403 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#95](/thread/post/8060419#post8060419 "Post Permalink")

  * Feb 11, 2015 6:32pm  Feb 11, 2015 6:32pm 

  * [ Mariodrugs](mariodrugs)

  * | Membership Revoked  | Joined Dec 2014 | [379 Posts](/search?do=process&provider=Member&searchuser=394832)

Again... buy positions closed at sl, and sell positiond didnt closed... but now in more scale.. its more dangerous for real account.... what is suddely chart EU will go up ? The account would be burn't ;O  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: wrong.png
Size: 86 KB](/attachment/image/1608772/thumbnail?d=1423647113)](/attachment/image/1608772?d=1423647113)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#96](/thread/post/8060476#post8060476 "Post Permalink")

  * Feb 11, 2015 6:47pm  Feb 11, 2015 6:47pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting Mariodrugs](/thread/post/8060419#post8060419 "View Quoted Post")
> 
> Disliked
> 
> Again... buy positions closed at sl, and sell positiond didnt closed... but now in more scale.. its more dangerous for real account.... what is suddely chart EU will go up ? The account would be burn't ;O {image}
> 
> Ignored

Let me analyze that.  
But bear in mind, don't use real account. I never recommend that as of now. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#97](/thread/post/8060495#post8060495 "Post Permalink")

  * Feb 11, 2015 6:53pm  Feb 11, 2015 6:53pm 

  * [ Mariodrugs](mariodrugs)

  * | Membership Revoked  | Joined Dec 2014 | [379 Posts](/search?do=process&provider=Member&searchuser=394832)

Is there a some way to turn off trail stops and stop looses?  
  
  
  
**I THINK I FOUND THE SOLUTION!![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1) If it works.. i will write it here!**

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#98](/thread/post/8060500#post8060500 "Post Permalink")

  * Feb 11, 2015 6:54pm  Feb 11, 2015 6:54pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

Mariodrugs,  
Sorry maan.... ![](https://resources.faireconomy.media/images/emojis/64/1f62b.png?v=15.1)I forgot to tell you. set Debugging Mode to true.  
then give me again the Expert tab logs. 

Attached Image

![](/attachment/image/1608784?d=1423648442)

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#99](/thread/post/8060503#post8060503 "Post Permalink")

  * Feb 11, 2015 6:55pm  Feb 11, 2015 6:55pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting Mariodrugs](/thread/post/8060495#post8060495 "View Quoted Post")
> 
> Disliked
> 
> Is there a some way to turn off trail stops and stop looses?
> 
> Ignored

What do you mean by trail stops? or stop losses? 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#100](/thread/post/8060518#post8060518 "Post Permalink")

  * Feb 11, 2015 7:00pm  Feb 11, 2015 7:00pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting aahmad29](/thread/post/8060136#post8060136 "View Quoted Post")
> 
> Disliked
> 
> {quote} My live account is 1:1000 but on Friday 2 hours before closing the market it is changed to 1:200 and then 2 hours after opening the market on Sunday, it changes back to 1:1000
> 
> Ignored

What broker are you using? 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Trapping System: Tunnel Martingale
  *   * [ **Reply to Thread** ](/thread/524198-trapping-system-tunnel-martingale/reply#reply)

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

[Martingale, Anti-martingale, and Compounding](/thread/571233-martingale-anti-martingale-and-compounding "Hi all traders, 
i started this thread to meet others people interested in money management. 
We all know that martingale strategies are...") 40 replies

[Martingale, Reverse Martingale, Modified Martingale, Maths](/thread/736165-martingale-reverse-martingale-modified-martingale-maths "Hi all, so Martingale has been a risky yet maybe non profitable system. While roulette has an edge of \(2.7%/5.4%\) 
  
Inspired by Adam...") 1 reply

[How to change this Martingale to Reverse Martingale ?](/thread/546755-how-to-change-this-martingale-to-reverse-martingale "How to change this Martingale to Reverse Martingale ?") 3 replies

[Trapping System: Way to Fully-Automated Trading System](/thread/509226-trapping-system-way-to-fully-automated-trading-system "Hi fellow Traders! 
This is my first time to write a new thread. Would like to share a trading method, which at least made me happy right...") 47 replies

[Martingale vs. Non Martingale (Simplified RoR vs Profit)](/thread/526308-martingale-vs-non-martingale-simplified-ror-vs-profit "Martingale: The gambler doubles his bet after every loss... 
  
Martingale vs. Non Martingale \(Simplified RoR vs Profit in 3 trade runs...") 1 reply

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/524198-trapping-system-tunnel-martingale/reply#reply)
  * Subscribe
  * [221](javascript:void\(0\);)

Attachments: Trapping System: Tunnel Martingale

Tags: Trapping System: Tunnel Martingale

#  [](/thread/524198-trapping-system-tunnel-martingale)Trapping System: Tunnel Martingale 

  * 

  * [#101](/thread/post/8060572#post8060572 "Post Permalink")

  * Feb 11, 2015 7:14pm  Feb 11, 2015 7:14pm 

  * [ Mariodrugs](mariodrugs)

  * | Membership Revoked  | Joined Dec 2014 | [379 Posts](/search?do=process&provider=Member&searchuser=394832)

I had at another chart putted another EA ! ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) That I think was the reason about trail stops and stop looses ! Now it started to looks good ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) If this happens again i will tell you but i think now it should be good!   
  
So what is that Debugging mode ? What is doing that? For what is that ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) ? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#102](/thread/post/8060615#post8060615 "Post Permalink")

  * Feb 11, 2015 7:25pm  Feb 11, 2015 7:25pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting Mariodrugs](/thread/post/8060572#post8060572 "View Quoted Post")
> 
> Disliked
> 
> I had at another chart putted another EA ! ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) That I think was the reason about trail stops and stop looses ! Now it started to looks good ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) If this happens again i will tell you but i think now it should be good! So what is that Debugging mode ? What is doing that? For what is that ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) ?
> 
> Ignored

No wonder.... ![](https://resources.faireconomy.media/images/emojis/64/1f62c.png?v=15.1)  
I think that is answering my question why the orders for the other part (say BUY section or SELL section) suddenly closing...  
In ur case, the 0.06 lot order was closed without closing the others, that's it was weird for me.  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot2.png
Size: 56 KB](/attachment/image/1608814/thumbnail?d=1423650244)](/attachment/image/1608814?d=1423650244)   

  
Because I have placed delete all orders in 1 function call, so if I would want to delete 1, I will delete all orders related to magic number you've set (default is 8080).  
  
When the order properly closed, it will have this line in your expert tab.  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot1.png
Size: 24 KB](/attachment/image/1608807/thumbnail?d=1423650024)](/attachment/image/1608807?d=1423650024)   

  
  
Debugging Mode generally will dump debugging text to Experts tab for my reference if any problem happened. It won't have any impact on your trades, probably little (very little) performance to the EA will be reduced, because writing to log frequently. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#103](/thread/post/8060699#post8060699 "Post Permalink")

  * Edited 8:28pm  Feb 11, 2015 7:47pm | Edited 8:28pm 

  * [ Mariodrugs](mariodrugs)

  * | Membership Revoked  | Joined Dec 2014 | [379 Posts](/search?do=process&provider=Member&searchuser=394832)

I came to the conclusion.. this strategy is good, but if you have 1.000.000$ on the account ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1) (but if I have one million, i wouldnt be risky that for 20$ for day ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)  
  
The situation like today on EurUsd is killing this strategy... 8 pips up, 8 pips down, open buy, open sell, open buy, open sell... it can kill accounts.. (of corse I test it on demo)  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Martingale faile.png
Size: 40 KB](/attachment/image/1608917/thumbnail?d=1423654092)](/attachment/image/1608917?d=1423654092)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#104](/thread/post/8060833#post8060833 "Post Permalink")

  * Feb 11, 2015 8:28pm  Feb 11, 2015 8:28pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting Mariodrugs](/thread/post/8060699#post8060699 "View Quoted Post")
> 
> Disliked
> 
> I came to the conclusion.. this strategy is good, but if you have 1.000.000$ on the account ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)
> 
> Ignored

Not necessary $1.000.000, if:

  1. You can find the best settings and options for this EA.  
few scenarios for example: 1 cycle with 1.00 starting lot after SNR reached (quite risky), unlimited cycles with 0.01 starting lot anytime.
  2. Avoid market holidays for respective currency.
  3. You happen to select a "good" broker, which has lower [spreads](/brokers/spreads "View Live Spreads on the Broker Guide").

That's why I said in 1st thread, your profit depends on your own strategy and scenario.  
  
I have another strategy actually, which will open 1 cycle of trades based on daily high (for BUY STOP) and daily low (for SELL STOP) with very small profit and high lots. That works fine and good, 90+% of the trade is profitable. The bad is, probably randomly every month there'll be 1 or 2 times the price is not moving as expected. So, I'm gonna mix this and daily high low to minimize the risk.  
  
So far my observation,  
My demo account (above this thread) was started at $5000, I was too optimistic with 0.5 starting lots and profit target at $0.5 each cycle. But then martingale reaches index 5, then my account got stucked. STOP order wasn't executed since I have no margin at all.  
I closed all orders and started again with $3100+, so far 1 week I got $400+. When NFP announced, I think that was the best day, but also the worst day. I got big profit for $200 that day, but martingale index reaches 10 before NFP announced.  
  
some settings from my testings:

  1. $3100+ starting
  2. Start AnyTime
  3. $0.20 Profit Target (No stop loss if you use Dynamic Money or Fixed Money)
  4. Starting Lot at 0.02
  5. Martingale Factor use standard 1, 2, 4, 8, 16, 32, 64, ....
  6. Max Martingale Factor 25
  7. Gap 40 pips (my broker's spread is 0.2 EURUSD, and 0.3 USDJPY)
  8. EURUSD and USDJPY

Some facts I observed:

  1. Max martingale reached so far is at index 10, which is 512 (which will creates you 10.24 lots if started from 0.02 lots).
  2. Index 10 was reached during: before NFP, around 15:00 Singapore time (sometimes only, not everyday), at sometime this Monday which is lazy day for EURUSD.
  3. There's no day without profit (at least in 1 week testing since started with $3100+). Minimum profit around $20, max around $200 (at NFP 4 Feb).
  4. Biggest profit in 1 cycle so far: $7.17 (EURUSD), and $14.53 (USDJPY).  
Not sure whether that is accurate, but it should be. Since I calculate it when I do Close for each order.
  5. I observed that Fixed Points scenario is not really good when your martingale index keeps growing. The best options would be either Dynamic Money or Fixed Money.  
The more martingale index used (especially when sideways), 1 points movement can be a big movement.

Probably next in v1.05 or v1.06, I will reveal another target type, which is the usage of trailing profit, this will maximize the profit per cycle as well.  
  
I will observe this for 2 or 3 more months, of course in demo. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#105](/thread/post/8060843#post8060843 "Post Permalink")

  * Feb 11, 2015 8:31pm  Feb 11, 2015 8:31pm 

  * [ aahmad29](aahmad29)

  * Joined Aug 2012 | Status: Love for all; Hatred for none | [3,557 Posts](/search?do=process&provider=Member&searchuser=286894)

> [Quoting radityo.ardi](/thread/post/8060518#post8060518 "View Quoted Post")
> 
> Disliked
> 
> {quote} What broker are you using?
> 
> Ignored

E.X.N.E.S.S 

Love for all; Hatred for none.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#106](/thread/post/8060860#post8060860 "Post Permalink")

  * Feb 11, 2015 8:36pm  Feb 11, 2015 8:36pm 

  * [ aahmad29](aahmad29)

  * Joined Aug 2012 | Status: Love for all; Hatred for none | [3,557 Posts](/search?do=process&provider=Member&searchuser=286894)

> [Quoting Mariodrugs](/thread/post/8060699#post8060699 "View Quoted Post")
> 
> Disliked
> 
> I came to the conclusion.. this strategy is good, but if you have 1.000.000$ on the account ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1) (but if I have one million, i wouldnt be risky that for 20$ for day ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1) The situation like today on EurUsd is killing this strategy... 8 pips up, 8 pips down, open buy, open sell, open buy, open sell... it can kill accounts.. (of corse I test it on demo) {image}
> 
> Ignored

There is suggestion, if you don't want to take any risk then take two trades daily. Both trades 5 minutes before London and NY open, keep profit minimum. 

Love for all; Hatred for none.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#107](/thread/post/8060866#post8060866 "Post Permalink")

  * Feb 11, 2015 8:38pm  Feb 11, 2015 8:38pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting aahmad29](/thread/post/8060860#post8060860 "View Quoted Post")
> 
> Disliked
> 
> {quote} There is suggestion, if you don't want to take any risk then take two trades daily. Both trades 5 minutes before London and NY open, keep profit minimum.
> 
> Ignored

That is also another scenario....![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)  
That's why you'll see so many settings on my EA.... ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#108](/thread/post/8060875#post8060875 "Post Permalink")

  * Feb 11, 2015 8:42pm  Feb 11, 2015 8:42pm 

  * [ Mariodrugs](mariodrugs)

  * | Membership Revoked  | Joined Dec 2014 | [379 Posts](/search?do=process&provider=Member&searchuser=394832)

> Quote
> 
> Disliked
> 
> radityo.ardi " 1.Max martingale reached so far is at index 10, which is 512 (which will creates you 10.24 lots if started from 0.02 lots)."

  
  
  
On that screen which i show you from today you can see index 12 ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1), which is 20.48 lots started from 0.01 microlots ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)  
  
Best wishes! Strategy not for me, but i will observe this thread! ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) Good luck! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#109](/thread/post/8061097#post8061097 "Post Permalink")

  * Feb 11, 2015 10:03pm  Feb 11, 2015 10:03pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting Mariodrugs](/thread/post/8060875#post8060875 "View Quoted Post")
> 
> Disliked
> 
> {quote} On that screen which i show you from today you can see index 12 ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1), which is 20.48 lots started from 0.01 microlots ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1) Best wishes! Strategy not for me, but i will observe this thread! ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) Good luck!
> 
> Ignored

No problem. Good luck to you as well! ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#110](/thread/post/8061936#post8061936 "Post Permalink")

  * Feb 12, 2015 3:06am  Feb 12, 2015 3:06am 

  * [ aahmad29](aahmad29)

  * Joined Aug 2012 | Status: Love for all; Hatred for none | [3,557 Posts](/search?do=process&provider=Member&searchuser=286894)

> [Quoting Mariodrugs](/thread/post/8060875#post8060875 "View Quoted Post")
> 
> Disliked
> 
> {quote} On that screen which i show you from today you can see index 12 ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1), which is 20.48 lots started from 0.01 microlots ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1) Best wishes! Strategy not for me, but i will observe this thread! ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) Good luck!
> 
> Ignored

20.48 lots, it is crazy thing. I never have this value but in any way wish you good luck with your trading. 

Love for all; Hatred for none.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#111](/thread/post/8061954#post8061954 "Post Permalink")

  * Feb 12, 2015 3:12am  Feb 12, 2015 3:12am 

  * [ aahmad29](aahmad29)

  * Joined Aug 2012 | Status: Love for all; Hatred for none | [3,557 Posts](/search?do=process&provider=Member&searchuser=286894)

> [Quoting radityo.ardi](/thread/post/8060866#post8060866 "View Quoted Post")
> 
> Disliked
> 
> {quote} That is also another scenario....![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1) That's why you'll see so many settings on my EA.... ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)
> 
> Ignored

Results so far for this week with initial lot 0.02 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Untitled.jpg
Size: 151 KB](/attachment/image/1609286/thumbnail?d=1423678321)](/attachment/image/1609286?d=1423678321)   

Love for all; Hatred for none.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#112](/thread/post/8063020#post8063020 "Post Permalink")

  * Feb 12, 2015 12:35pm  Feb 12, 2015 12:35pm 

  * [ addy5280](addy5280)

  * | Joined Nov 2010  | Status: Trader | [28 Posts](/search?do=process&provider=Member&searchuser=160534)

Attached Image (click to enlarge)

[![Click to Enlarge

Name: QQå›¾ç‰‡20150212112929.jpg
Size: 123 KB](/attachment/image/1609544/thumbnail?d=1423711977)](/attachment/image/1609544?d=1423711977)   

Attached Image (click to enlarge)

[![Click to Enlarge

Name: QQå›¾ç‰‡20150212112934.jpg
Size: 123 KB](/attachment/image/1609545/thumbnail?d=1423711982)](/attachment/image/1609545?d=1423711982)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#113](/thread/post/8063035#post8063035 "Post Permalink")

  * Feb 12, 2015 12:45pm  Feb 12, 2015 12:45pm 

  * [ addy5280](addy5280)

  * | Joined Nov 2010  | Status: Trader | [28 Posts](/search?do=process&provider=Member&searchuser=160534)

every order have different magic number 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#114](/thread/post/8063164#post8063164 "Post Permalink")

  * Feb 12, 2015 2:37pm  Feb 12, 2015 2:37pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting addy5280](/thread/post/8063035#post8063035 "View Quoted Post")
> 
> Disliked
> 
> every order have different magic number
> 
> Ignored

I'm just curious...  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot1.png
Size: 218 KB](/attachment/image/1609579/thumbnail?d=1423719211)](/attachment/image/1609579?d=1423719211)   

  
  
The one with red circle, was that coming from multiple charts, with multiple EA attached to it (of course 1 EA 1 chart), and all of them are the same pair???  
I see all of them GBPJPYm....  
  
In that case definitely some strange behaviour will exist, because I never tested that. And why would I need to test that scenario? Because once I set to 1 pair, probably I would want to open another chart for another pair then start with a different magic number.  
Am I right? 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#115](/thread/post/8063261#post8063261 "Post Permalink")

  * Feb 12, 2015 3:45pm  Feb 12, 2015 3:45pm 

  * [ addy5280](addy5280)

  * | Joined Nov 2010  | Status: Trader | [28 Posts](/search?do=process&provider=Member&searchuser=160534)

Attached Image (click to enlarge)

[![Click to Enlarge

Name: QQå›¾ç‰‡20150212144345.jpg
Size: 127 KB](/attachment/image/1609606/thumbnail?d=1423723537)](/attachment/image/1609606?d=1423723537)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#116](/thread/post/8064998#post8064998 "Post Permalink")

  * Feb 13, 2015 12:11am  Feb 13, 2015 12:11am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

I've never tested Support Resistance and Daily High Low thoroughly.  
Today just finished testing and fixed couple bugs.  
  
I will post EA updates tomorrow, v1.05.  
\- fixed Support Resistance scenario with limited max martingale count  
\- New added feature, Daily High and Low (instead of Support Resistance)  
\- Line colouring fixes  
\- Added time limiter to Support and resistance 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#117](/thread/post/8065358#post8065358 "Post Permalink")

  * Feb 13, 2015 2:02am  Feb 13, 2015 2:02am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

Sorry, I couldn't resist...![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)  
I've uploaded v1.06. Sorry, the version is jumping to 1.06.  
another new feature on top of it, the Trailing Target.  
Will explain it tomorrow (update the first thread). 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#118](/thread/post/8066306#post8066306 "Post Permalink")

  * Feb 13, 2015 11:10am  Feb 13, 2015 11:10am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar363134_3.gif) Eragon93](eragon93)

  * | Joined Feb 2014  | Status: Trader | [18 Posts](/search?do=process&provider=Member&searchuser=363134)

this strategy called Surefire hedge , i was using it on my real account Manuel best way to use it  
1- be4 news about 5 min becuz news moving the market  
2- when you see W or M pattern and i can find this pattern alot on renko chart Like the pic below  
by the way thank you for sharing the EA i will test it tomorrow 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot1.png
Size: 31 KB](/attachment/image/1610429/thumbnail?d=1423793341)](/attachment/image/1610429?d=1423793341)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#119](/thread/post/8066427#post8066427 "Post Permalink")

  * Feb 13, 2015 1:21pm  Feb 13, 2015 1:21pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar92149_1.gif) chamane](chamane)

  * Joined Jan 2009 | Status: Trader | [1,987 Posts](/search?do=process&provider=Member&searchuser=92149)

Here is [food](http://www.tradelikejarvis.com/how-implement-martingale-type-betting-strategy-trading-without-losing-money/) for thoughts. It allows more steps in the sequence, but you have to get two wins in a row to reset number of lots. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#120](/thread/post/8066433#post8066433 "Post Permalink")

  * Feb 13, 2015 1:26pm  Feb 13, 2015 1:26pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

I came to know that there is martingale series which less risky than 1, 2, 4.  
You can use 1, 2, 2, 2, 2, 2, 2, 2, 2....  
  
The only problem is if you set it to Money based target, the longer the martingale used, then the longer the target is. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Trapping System: Tunnel Martingale
  *   * [ **Reply to Thread** ](/thread/524198-trapping-system-tunnel-martingale/reply#reply)

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

[Martingale, Anti-martingale, and Compounding](/thread/571233-martingale-anti-martingale-and-compounding "Hi all traders, 
i started this thread to meet others people interested in money management. 
We all know that martingale strategies are...") 40 replies

[Martingale, Reverse Martingale, Modified Martingale, Maths](/thread/736165-martingale-reverse-martingale-modified-martingale-maths "Hi all, so Martingale has been a risky yet maybe non profitable system. While roulette has an edge of \(2.7%/5.4%\) 
  
Inspired by Adam...") 1 reply

[How to change this Martingale to Reverse Martingale ?](/thread/546755-how-to-change-this-martingale-to-reverse-martingale "How to change this Martingale to Reverse Martingale ?") 3 replies

[Trapping System: Way to Fully-Automated Trading System](/thread/509226-trapping-system-way-to-fully-automated-trading-system "Hi fellow Traders! 
This is my first time to write a new thread. Would like to share a trading method, which at least made me happy right...") 47 replies

[Martingale vs. Non Martingale (Simplified RoR vs Profit)](/thread/526308-martingale-vs-non-martingale-simplified-ror-vs-profit "Martingale: The gambler doubles his bet after every loss... 
  
Martingale vs. Non Martingale \(Simplified RoR vs Profit in 3 trade runs...") 1 reply

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/524198-trapping-system-tunnel-martingale/reply#reply)
  * Subscribe
  * [221](javascript:void\(0\);)

Attachments: Trapping System: Tunnel Martingale

Tags: Trapping System: Tunnel Martingale

#  [](/thread/524198-trapping-system-tunnel-martingale)Trapping System: Tunnel Martingale 

  * 

  * [#121](/thread/post/8066436#post8066436 "Post Permalink")

  * Feb 13, 2015 1:27pm  Feb 13, 2015 1:27pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting chamane](/thread/post/8066427#post8066427 "View Quoted Post")
> 
> Disliked
> 
> Here is [food](http://www.tradelikejarvis.com/how-implement-martingale-type-betting-strategy-trading-without-losing-money/) for thoughts. It allows more steps in the sequence, but you have to get two wins in a row to reset number of lots.
> 
> Ignored

That is riskier I think.  
But I might put that in configuration, and see whose account will blow.... ![](https://resources.faireconomy.media/images/emojis/64/1f608.png?v=15.1)

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#122](/thread/post/8066457#post8066457 "Post Permalink")

  * Feb 13, 2015 1:58pm  Feb 13, 2015 1:58pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar92149_1.gif) chamane](chamane)

  * Joined Jan 2009 | Status: Trader | [1,987 Posts](/search?do=process&provider=Member&searchuser=92149)

I would also suggest to trade pairs with high volatility on high timeframes (e.g. daily) and low volatility on low TF (e.g. 15min). USDCAD is offering such conditions rght now. Then chose a gap on thr 15min TF to avoid whipsaws. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#123](/thread/post/8066942#post8066942 "Post Permalink")

  * Feb 13, 2015 6:29pm  Feb 13, 2015 6:29pm 

  * [ pankwinto](pankwinto)

  * | Joined Sep 2011  | Status: Trader | [8 Posts](/search?do=process&provider=Member&searchuser=196831)

> [Quoting Mariodrugs](/thread/post/8060699#post8060699 "View Quoted Post")
> 
> Disliked
> 
> The situation like today on EurUsd is killing this strategy... 8 pips up, 8 pips down, open buy, open sell, open buy, open sell... it can kill accounts..{image}
> 
> Ignored

hi all, i think this will help avoid this situation :  
  
\- use dinamic gap size, and the gap in EA must rise 1-1.5 pp at low market volatility (ex. if the ATR(14) < 2-3 pp).  
\- or not open new cicle while ATR(14) < 2-3 pp.  
  
what you think, radityo.ardi ? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#124](/thread/post/8067337#post8067337 "Post Permalink")

  * Edited Feb 14, 2015 6:57pm  Feb 13, 2015 9:00pm | Edited Feb 14, 2015 6:57pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting pankwinto](/thread/post/8066942#post8066942 "View Quoted Post")
> 
> Disliked
> 
> {quote} hi all, i think this will help avoid this situation : - use dinamic gap size, and the gap in EA must rise 1-1.5 pp at low market volatility (ex. if the ATR(14) < 2-3 pp). - or not open new cicle while ATR(14) < 2-3 pp. what you think, radityo.ardi ?
> 
> Ignored

I'll take that up as suggestion,  
but dynamic gap means more settings, which is in my EA settings is too crowded already....  
Actually without me doing any changes, you can do dynamic gap size already. Open 2 charts, set ur EA at different time range (and also different magic number to avoid errors). That way you can actually solve it.  
  
  
Now, let's talk about interesting topic here.......................................... (I hope you'll be interested with these facts) ![](https://resources.faireconomy.media/images/emojis/64/1f918.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)  
I've just done a small simulation using MS Excel.  
As I said, there's way to minimize the risk, but also there's another risk linked to it.  
What we need to do:

  1. Use Start Anytime
  2. Set martingale factor to: 1, 2
  3. Set Martingale factor multiplier to 1.0. This way, will generate 1, 2, 2, 2, 2, 2......... until Max Martingale Factor is reached.
  4. Gaps is 30 points which means 3 pips for 5 digits broker (or more depends on your broker's [spreads](/brokers/spreads "View Live Spreads on the Broker Guide")).
  5. Let us set the profit to Fixed Money: $0.1 or $0.2
  6. Just start with fixed lots of 0.1

This way, actually will never get loss by minimizing the risk (again as I said, _practically_). Because if you use strict 1, 2, 4, once reaches 11 or 12 (with balance of $5K and starting lots 0.02), you are doomed. That point probably already 20.48 lots will be placed.  
  
**_Basically with above's scenario, martingale concept is never been purely used in this EA if you use Fixed Money_**. Because practically you never lost anything (because no order is closed in the cycle).  
  
Quoted from wikipedia:  

> Quote
> 
> Disliked
> 
> The simplest of these strategies was designed for a game in which the gambler wins his stake if a coin comes up heads and loses it if the coin comes up tails. The strategy had _the gambler double his bet after every loss_ so that _the first win would recover all previous losses plus win a profit equal to the original stake_.

  
So in my opinion, _Martingale should never be linked to the lots used, it should only be linked in the loss you've suffered_.  
_And if the order still open, you are not considered as loss_. Because you are choosing to deny that you are loss, and choose to close later when you are sure you get profit in total.  
  
Let us play with excel.  
Here I have as below with Gap 30 points. Buy 0.01 at 1.14550 and Sell 0.02 at 1.14520. While the price (Bid) moving to 1.14484, I got $0, no profit, no loss.  

Attached Image

![](/attachment/image/1610701?d=1423826938)

  
  
let us say the price goes back touching 1.14550, and buy touched and price goes down, sell 1.14520 touched as well and reaches 1.14418, I got $0, no profit, no loss.  

Attached Image

![](/attachment/image/1610709?d=1423827202)

  
  
The next $0 point is at 1.14352. So, I calculated, each $0 profit down, is actually 66 points.  

Attached Image

![](/attachment/image/1610711?d=1423827294)

  
  
Let us talk about the risk.  
Each and every $0 checkpoint, is 66 points. My broker is actually at 3 points spread (0.3 pips), and the gaps is 30 points. So I assume, this thing (together with martingale 1, 2, 2, 2....), resulted from = (Gaps x 2) + (spreads x 2).  
When I changed that to having a gaps 10 points, and spreads to 5 points (0.5 pips), here's the calculations.  

Attached Image

![](/attachment/image/1610719?d=1423828056)

  

Attached Image

![](/attachment/image/1610720?d=1423828145)

  
  
See that?? Exactly 30 points!  
Which is coming from this:  

> Quote
> 
> Disliked
> 
> Interval = (Gaps x 2) + (spreads x 2)

That is if the price goes down. The price goes up, it applies the same calculation!  
  
You can see the total of Lots used, 0.07, very less there...  
So, your profit will be "suspended" and must go through a longer road, if the price is going back to the tunnel and forwarding back to the same direction.  
  
So, with the settings above, I believe it is:

  1. **LESS RISKY**  
This is because of the martingale series. Less lots used = less risky.
  2. **Always profit**  
Wherever the price goes, you always get profit. Just the cycle will be closed a bit longer if another series is created.

This is the file I've used for calculation.  

Attached File(s)

![File Type: xlsx](https://assets.faireconomy.media/images/attach/xlsx.gif) [CounterPublic.xlsx](/attachment/file/1611010?d=1423851057) 14 KB | 601 downloads 

  
  
Or if you don't have excel, you can try it online on <http://1drv.ms/1AvaPh7>  
There's a testing site for this, which will be started by Monday 16 Feb 2014: <http://www.forexfactory.com/radityo.ardi/38>

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#125](/thread/post/8067570#post8067570 "Post Permalink")

  * Feb 13, 2015 10:49pm  Feb 13, 2015 10:49pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

Eh...why I get loss little by little...???  
There must be some bugs... 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#126](/thread/post/8067640#post8067640 "Post Permalink")

  * Feb 13, 2015 11:11pm  Feb 13, 2015 11:11pm 

  * [ GreenLot](greenlot)

  * | Joined Feb 2015  | Status: Trader | [2 Posts](/search?do=process&provider=Member&searchuser=400573)

Hello Radit  
  
thanks for sharing this system, i know this sistem and like it. but still not know how strenght this for trade coz depend balance and lot.  
Q : 1 is use this trade 24H or open only special time?  
2\. Can u share the EXL file for lot and margin calculate?  
  
Thanks Keep share Bro... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#127](/thread/post/8067811#post8067811 "Post Permalink")

  * Edited 1:11pm  Feb 14, 2015 12:08am | Edited 1:11pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting GreenLot](/thread/post/8067640#post8067640 "View Quoted Post")
> 
> Disliked
> 
> Hello Radit thanks for sharing this system, i know this sistem and like it. but still not know how strenght this for trade coz depend balance and lot. Q : 1 is use this trade 24H or open only special time? 2. Can u share the EXL file for lot and margin calculate? Thanks Keep share Bro...
> 
> Ignored

Thanks bro for the support.  
I know this system still got something to fix. I found the bug, will release it tomorrow again.  
  
Answering your Q,  
Basically no restriction on the timings. Even it can run 24H. But, as pointed by many bros around here, it will be good if you run at high volatility times, such as US open time, or EU open time.  
EXL file? What is that?  
  
UPDATED: [Sorry bro, I was confused, thought you mean ex4 file. See above, I've uploaded the excel file...](http://www.forexfactory.com/showthread.php?p=8067337#post8067337)

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#128](/thread/post/8068082#post8068082 "Post Permalink")

  * Feb 14, 2015 1:34am  Feb 14, 2015 1:34am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar157942_10.gif) fxindikator](fxindikator)

  * Joined Oct 2010 | Status: Trader | [167 Posts](/search?do=process&provider=Member&searchuser=157942)

hi Radit  
I've been observe your thread for a while, i seek of profitable grid system. and i believe yours are good one, some friend use similar system called cut and switch martingle, but use only during high impact news especially nfp release. based on your method i'ts use long order along with sell stop, and when sell activated it trigger buy stop order, and so on. and for such method, a spread are would higher as each order executed, and create a gap between both order ( buy and sell).  
how about using iexposure method, i;ve been use some grid system (got from ff too), and it's use iexposure calculation as exit plan.  
so far given good result, and I use similar martingle ratio as yours 1.2, as well traded at same platform.  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: ce.jpg
Size: 356 KB](/attachment/image/1610902/thumbnail?d=1423842183)](/attachment/image/1610902?d=1423842183)   

  
regarding order gap and your pending order, have you ever found any slippage happen ? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#129](/thread/post/8068269#post8068269 "Post Permalink")

  * Feb 14, 2015 3:20am  Feb 14, 2015 3:20am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting fxindikator](/thread/post/8068082#post8068082 "View Quoted Post")
> 
> Disliked
> 
> hi Radit I've been observe your thread for a while, i seek of profitable grid system. and i believe yours are good one, some friend use similar system called cut and switch martingle, but use only during high impact news especially nfp release. based on your method i'ts use long order along with sell stop, and when sell activated it trigger buy stop order, and so on. and for such method, a spread are would higher as each order executed, and create a gap between both order ( buy and sell). how about using iexposure method, i;ve been use some grid...
> 
> Ignored

Yes, and thanks for the support.  
I've been observing that Matrix Grid CE Edition as well. But, as an IT enthusiast and programmer myself, I feel is not really fair to try that EA, since it will always download data from some server for getting a trend. Just imagine if the server is not good enough (since it is CE, and free ![](https://resources.faireconomy.media/images/emojis/64/1f644.png?v=15.1)), and thousands, even hundred thousands of people connecting to that server at the same time, it may take the server down. Server down, no trend downloaded, may disrupt the EA. And we never know what is the code behind their server. So, I decided not to try that.  
Anyways....  
any slippage, I've never observe that. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#130](/thread/post/8068284#post8068284 "Post Permalink")

  * Feb 14, 2015 3:31am  Feb 14, 2015 3:31am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting radityo.ardi](/thread/post/8067570#post8067570 "View Quoted Post")
> 
> Disliked
> 
> Eh...why I get loss little by little...??? There must be some bugs...
> 
> Ignored

![](https://resources.faireconomy.media/images/emojis/64/1f62b.png?v=15.1) it wasn't a bug, just wrong configuration... damn...  
Default configuration was $-3.0 for Max Loss, no wonder why it got loss everytime cycle closes....  
Warning everyone! Max Loss, please set to highest number you can imagine...![](https://resources.faireconomy.media/images/emojis/64/1f923.png?v=15.1)  
i.e.: -9999999  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot1.png
Size: 39 KB](/attachment/image/1611015/thumbnail?d=1423852117)](/attachment/image/1611015?d=1423852117)   

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#131](/thread/post/8068784#post8068784 "Post Permalink")

  * Feb 14, 2015 1:10pm  Feb 14, 2015 1:10pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

I've uploaded the another new ex4 and mq4 to the first thread, still under same version v1.06.  
Added options to Enable Max Loss. And additionally, max loss is now set to -9999999 by default.  
  
Please check that out... thanks. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#132](/thread/post/8068993#post8068993 "Post Permalink")

  * Feb 14, 2015 9:32pm  Feb 14, 2015 9:32pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar145433_1.gif) princefred](princefred)

  * Joined Jun 2010 | Status: Trader | [449 Posts](/search?do=process&provider=Member&searchuser=145433)

Great job, thanks man i have been trying unsuccessfully to modify your ea to also have an option of entering trades using bollinger bands from a timeframe where the distance between the bands are less than x pips or for this to manage trades open manually. Can you do that ? 

Know News/time; WAIT for Edge Entries, MPLC Normalization, Exits & TP's..

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#133](/thread/post/8069563#post8069563 "Post Permalink")

  * Feb 15, 2015 5:34pm  Feb 15, 2015 5:34pm 

  * [ adepelummy](adepelummy)

  * | Joined Jul 2011  | Status: Trader | [4 Posts](/search?do=process&provider=Member&searchuser=187110)

The. Attached expert works on the same principle But has some problem. It can't trade more than a pair at a time and after profit it doesn't restart another trade. Can someone Please take a look and Try to fix it for us all. 

Attached File(s)

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [Super Hedging 1.73.mq4](/attachment/file/1611499?d=1423989257) 154 KB | 686 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#134](/thread/post/8069628#post8069628 "Post Permalink")

  * Feb 15, 2015 7:21pm  Feb 15, 2015 7:21pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting princefred](/thread/post/8068993#post8068993 "View Quoted Post")
> 
> Disliked
> 
> Great job, thanks man i have been trying unsuccessfully to modify your ea to also have an option of entering trades using bollinger bands from a timeframe where the distance between the bands are less than x pips or for this to manage trades open manually. Can you do that ?
> 
> Ignored

Hmmmm.......very sorry bro ![](https://resources.faireconomy.media/images/emojis/64/1f61f.png?v=15.1), I want to do it, but I can't. This EA's configuration is too long already, I don't want to put up too much things in it. Even the current start type, some of them still not developed / not stable enough.  
It's free anyway, plus source code.  
  
But the point is, I think it is fair enough if I only give you 4 common scenarios: from Support and Resistance, Daily High Low, Start Anytime, and X points from last price. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#135](/thread/post/8070624#post8070624 "Post Permalink")

  * Feb 16, 2015 11:55am  Feb 16, 2015 11:55am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar370635_1.gif) KanGKunG](kangkung)

  * Joined Apr 2014 | Status: Trader | [36 Posts](/search?do=process&provider=Member&searchuser=370635)

nice new idea from you radityo 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#136](/thread/post/8070681#post8070681 "Post Permalink")

  * Feb 16, 2015 1:04pm  Feb 16, 2015 1:04pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar378621_1.gif) Nico1359](nico1359)

  * Joined Jul 2014 | Status: Trader | [218 Posts](/search?do=process&provider=Member&searchuser=378621)

Thinking about trying this EA out on demo... A couple questions: Do this need to be traded on a specific timeframe (assume starting with $2,000 and trading .01 lots to start), also, would you consider this EA particularly broker-sensitive? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#137](/thread/post/8070694#post8070694 "Post Permalink")

  * Feb 16, 2015 1:16pm  Feb 16, 2015 1:16pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting Nico1359](/thread/post/8070681#post8070681 "View Quoted Post")
> 
> Disliked
> 
> Thinking about trying this EA out on demo... A couple questions: Do this need to be traded on a specific timeframe (assume starting with $2,000 and trading .01 lots to start), also, would you consider this EA particularly broker-sensitive?
> 
> Ignored

I cannot stress this more, but _you have to test this on demo first_. ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)  
Why?  
Because you need to find the best settings that is specific to your broker, your pair in your broker and the way you run this EA.  
  
Broker-sensitive? Hmmm... I would say that depends on what you want.  
  
Say you trade for EURUSD, in broker A and broker B, although both having the same low spreads, sometimes the movement is quite different. Low spreads broker is helping through faster closing of the cycle and setting up tighter gaps, but doesn't mean that higher spreads broker is not good.  
Even you can set the gap more than 50 pips based on your preference.  
  
Anyway, that is the main idea for this EA, very generic, no need indicator, no need TF specific, no need broker specific... 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#138](/thread/post/8073060#post8073060 "Post Permalink")

  * Feb 17, 2015 2:13pm  Feb 17, 2015 2:13pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

No wonder market didn't move yesterday, and martingale reaches index 12.  
It was President's day...  
  
Need to avoid that one. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#139](/thread/post/8073149#post8073149 "Post Permalink")

  * Feb 17, 2015 2:40pm  Feb 17, 2015 2:40pm 

  * [ GreenLot](greenlot)

  * | Joined Feb 2015  | Status: Trader | [2 Posts](/search?do=process&provider=Member&searchuser=400573)

Hi radit Thanks for support,  
  
but i still not understand the setting for the EA :  
my parameter is :  
1\. Only open London&USA hour  
2\. Only 3 Cycle  
3\. Use Fixed Lot  
4\. Use Fixed POINT for TP  
  
i try for backtesting the result is not what i needed.  
  
Can u help for the setting? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#140](/thread/post/8073200#post8073200 "Post Permalink")

  * Feb 17, 2015 3:28pm  Feb 17, 2015 3:28pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting GreenLot](/thread/post/8073149#post8073149 "View Quoted Post")
> 
> Disliked
> 
> Hi radit Thanks for support, but i still not understand the setting for the EA : my parameter is : 1. Only open London&USA hour 2. Only 3 Cycle 3. Use Fixed Lot 4. Use Fixed POINT for TP i try for backtesting the result is not what i needed. Can u help for the setting?
> 
> Ignored

That's my worry if there's too much configuration. But anyway, seems that you want to run to different time range, then you have to run 2 charts for the same pair.  
  
For example:  
  
_**For Chart 1**_  
StartType=1  
MagicNumber=8080  
StartAmountType=1  
StartFixedAmount=0.02  
MartingaleFactor=1,2,4  
MaxMartingaleFactor=25  
FactorMultiplier=2.0  
MartingaleGap=30  
MaxMartingaleCycle=3  
TargetType=2  
PointsTargetType=0  
PointsTarget=20  
PointsLoss=100  
StartFrom=0  
StartNextFrom=1  
DateTimeType=0  
DailyStartTime=15:00:00  
DailyStopTime=20:00:00  
SNRDirection=0  
DailyHighLowRecTime=14:00  
IsDebug=false  
IsDevelopment=false  
  
_**For Chart 2**_  
StartType=1  
MagicNumber=8181  
StartAmountType=1  
StartFixedAmount=0.02  
MartingaleFactor=1,2,4  
MaxMartingaleFactor=25  
FactorMultiplier=2.0  
MartingaleGap=30  
MaxMartingaleCycle=3  
TargetType=2  
PointsTargetType=0  
PointsTarget=20  
PointsLoss=100  
StartFrom=0  
StartNextFrom=1  
DateTimeType=0  
DailyStartTime=20:00:00  
DailyStopTime=02:00:00  
SNRDirection=0  
DailyHighLowRecTime=14:00  
IsDebug=false  
IsDevelopment=false  
  
  
Save the green text into notepad and save it as .set file, load it into the chart with EA.  
However, I don't think you can do backtest. I was trying, but didn't succeeded. That's why I decided to do forward testing.  
  
Note that there's value you can modify, such as Gap size (MartingaleGap), TP in points (PointsTarget), and SL in points (PointsLoss), Max cycle (MaxMartingaleCycle), DailyStartTime and DailyEndTime. Both Timing are assuming Local time to your PC / VPS. I set that for SGT, dunno which timeframe are you...  
The settings above is assuming you have 5 digits for EURUSD. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Trapping System: Tunnel Martingale
  *   * [ **Reply to Thread** ](/thread/524198-trapping-system-tunnel-martingale/reply#reply)

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

[Martingale, Anti-martingale, and Compounding](/thread/571233-martingale-anti-martingale-and-compounding "Hi all traders, 
i started this thread to meet others people interested in money management. 
We all know that martingale strategies are...") 40 replies

[Martingale, Reverse Martingale, Modified Martingale, Maths](/thread/736165-martingale-reverse-martingale-modified-martingale-maths "Hi all, so Martingale has been a risky yet maybe non profitable system. While roulette has an edge of \(2.7%/5.4%\) 
  
Inspired by Adam...") 1 reply

[How to change this Martingale to Reverse Martingale ?](/thread/546755-how-to-change-this-martingale-to-reverse-martingale "How to change this Martingale to Reverse Martingale ?") 3 replies

[Trapping System: Way to Fully-Automated Trading System](/thread/509226-trapping-system-way-to-fully-automated-trading-system "Hi fellow Traders! 
This is my first time to write a new thread. Would like to share a trading method, which at least made me happy right...") 47 replies

[Martingale vs. Non Martingale (Simplified RoR vs Profit)](/thread/526308-martingale-vs-non-martingale-simplified-ror-vs-profit "Martingale: The gambler doubles his bet after every loss... 
  
Martingale vs. Non Martingale \(Simplified RoR vs Profit in 3 trade runs...") 1 reply

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/524198-trapping-system-tunnel-martingale/reply#reply)
  * Subscribe
  * [221](javascript:void\(0\);)

Attachments: Trapping System: Tunnel Martingale

Tags: Trapping System: Tunnel Martingale

#  [](/thread/524198-trapping-system-tunnel-martingale)Trapping System: Tunnel Martingale 

  * 

  * [#141](/thread/post/8074927#post8074927 "Post Permalink")

  * Feb 18, 2015 12:39am  Feb 18, 2015 12:39am 

  * [ atena](atena)

  * | Joined Feb 2015  | Status: Trader | [1 Post](/search?do=process&provider=Member&searchuser=401001)

i read all the article and i found your idea about 1,2,2,2,2 fantastic for the reason of no danger for your money.  
but to my demo mt4 account start with buy order and not open sell order (invalid error).  
maybe my settings is wrong,can you give me your settings.  
  
radityo many thanks for your work!  
  
  
  
txt01=————————————————————— [COMMON]  
StartType=1  
ProfitLineColor=55295  
TextColor=55295  
UpperGapPriceColor=13382297  
LowerGapPriceColor=36095  
TextSize=8  
MagicNumber=8080  
LineStyle=0  
LineWidth=1  
LineHeight=13  
DailyStartTime=10:00:00  
DailyStopTime=00:00:00  
txt05=————————————————————— [SLIPPAGE]  
UseSlippage=false  
Slip=50  
txt02=————————————————————— [LOT(S)]  
StartAmountType=1  
StartDynamicAmount=0.000002  
StartFixedAmount=0.01  
txt03=————————————————————— [MARTINGALE]  
MartingaleFactor=1,2  
MaxMartingaleFactor=100  
FactorMultiplier=1.0  
MartingaleGap=10  
MaxMartingaleCycle=0  
txt04=————————————————————— [TARGET]  
TargetType=0  
TrailingTargetType=0  
ProfitTarget=0.1  
TrailingTarget=0.2  
UseProfitLoss=false  
ProfitLoss=-9999999.0  
ProfitTargetMultiplier=0.0001  
ProfitLossMultiplier=0.0001  
PointsTargetType=0  
PointsTarget=20  
PointsLoss=100  
PointsTargetColor=32768  
PointsLossColor=16711935  
txt06=————————————————————— [START ANYTIME]  
StartFrom=0  
StartNextFrom=1  
DateTimeType=0  
txt07=————————————————————— [START SUPPORT & RESISTANCE]  
PivotColor=8388736  
SNR1Color=65535  
SupResRecTime=09:00  
txt08=————————————————————— [START DAILY HIGH LOW]  
HighLowColor=13959039  
DailyHighLowRecTime=14:00  
txt09=————————————————————— [START SUPP & RES and DAILY HIGH LOW]  
OrderDirection=0  
txt99=————————————————————— [DEBUG]  
IsDebug=false  
IsDevelopment=false

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#142](/thread/post/8075107#post8075107 "Post Permalink")

  * Feb 18, 2015 1:32am  Feb 18, 2015 1:32am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar378621_1.gif) Nico1359](nico1359)

  * Joined Jul 2014 | Status: Trader | [218 Posts](/search?do=process&provider=Member&searchuser=378621)

Can "Max Martingale Factor" also be thought of as max trades opened at any time? In other words if I want to cap the trading at 1.28 lots, would that mean a Max Martingale Factor of 8?  
  
Thanks. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#143](/thread/post/8076125#post8076125 "Post Permalink")

  * Feb 18, 2015 11:39am  Feb 18, 2015 11:39am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting atena](/thread/post/8074927#post8074927 "View Quoted Post")
> 
> Disliked
> 
> i read all the article and i found your idea about 1,2,2,2,2 fantastic for the reason of no danger for your money. but to my demo mt4 account start with buy order and not open sell order (invalid error). maybe my settings is wrong,can you give me your settings. radityo many thanks for your work! txt01= [COMMON] StartType=1 ProfitLineColor=55295 TextColor=55295 UpperGapPriceColor=13382297 LowerGapPriceColor=36095 TextSize=8 MagicNumber=8080 LineStyle=0 LineWidth=1 LineHeight=13 DailyStartTime=10:00:00 DailyStopTime=00:00:00 txt05= [SLIPPAGE] UseSlippage=false...
> 
> Ignored

It can be done in this series as well,   
1, 2, 3, 4,5,6, the moment you want to minimize the risk, you can continue with the same last number, 6, 6, 6, 6, 6, .....  
So it'll form 1, 2,3, 4, 5, 6, 6, 6, 6, 6.... in general, this is the other way.  
  
Seems that the error because of your gap is too small. Buy created but sell stop not created, most of the time is because of gap is too low.  
Check your chart's prices, how many digits for the current pair's price. Mine in this X.XXXXX (5 digits), so if I would want a gap 10 pips, then I have to set MartingaleGap to 100. Different story for 4 digit, they have to keep set it as 10.  
  
This is not a bug, as I calculated based on the points, not pips.  
  

> [Quoting Nico1359](/thread/post/8075107#post8075107 "View Quoted Post")
> 
> Disliked
> 
> Can "Max Martingale Factor" also be thought of as max trades opened at any time? In other words if I want to cap the trading at 1.28 lots, would that mean a Max Martingale Factor of 8? Thanks.
> 
> Ignored

Max Martingale Factor is the max trades opened in 1 cycle itself. It was there since v1.03. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#144](/thread/post/8076148#post8076148 "Post Permalink")

  * Feb 18, 2015 11:55am  Feb 18, 2015 11:55am 

  * [ making_money](making_money)

  * | Joined Jan 2008  | Status: Trader | [13 Posts](/search?do=process&provider=Member&searchuser=57759)

hi radityo, it's nice to know that someone else also have the same idea of trading like me. skip that for now, i want to ask you how to set the EA to run on more than 1 pair in 1 metatrader. you said that by changing the magic number, can you give me example on it? sorry i'm not very familiar with setting an EA ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
  
second, is that possible for you to make 1 more additional parameter, that is SL for the 1st position? here is my thought, I know that the EA will make a pending order for the next position, but what if the trade is against the direction and the order failed to open due to price gap. eq: i use 60 point gap (5 digit broker), but then the price jump 100 point and continue, which make the next position order fail to open. If the EA can add a parameter where I can limit my loss for it, then it will be great. oh, I use fixed money setting.  
  
sorry for my confusing english 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#145](/thread/post/8076376#post8076376 "Post Permalink")

  * Feb 18, 2015 3:25pm  Feb 18, 2015 3:25pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting making_money](/thread/post/8076148#post8076148 "View Quoted Post")
> 
> Disliked
> 
> hi radityo, it's nice to know that someone else also have the same idea of trading like me. skip that for now, i want to ask you how to set the EA to run on more than 1 pair in 1 metatrader. you said that by changing the magic number, can you give me example on it? sorry i'm not very familiar with setting an EA ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) second, is that possible for you to make 1 more additional parameter, that is SL for the 1st position? here is my thought, I know that the EA will make a pending order for the next position, but what if the trade is against the direction...
> 
> Ignored

Hi bro.. it is already there, if you set to fixed TP and SL.  
  
btw magic number is ID that we cannot see, only EA can see. This ID is to segregate orders between each EA and/or your own order. So in 1 account, actually you can run multiple EAs, and do manual trade without disrupting each other. Now the problem is if one EA didn't use any magic number, then it will messed up any orders in it.  
  
Here's how: you open 2 charts (either same pair or different), attach the EA to both, but with _different Magic Number_.  
  

Attached Image

![](/attachment/image/1613540?d=1424238933)

  
So if you see the picture above, you can set:  
Target Type = Fixed Points  
Points Target Type = Fixed points for both SL and TP  
Points Target = this is the target in points (TP)  
Points Stop Loss = this is the stop loss in points (SL)  
  
If you use Fixed Points, the assumption is that it will be calculcated from the very first order.  
Please do test this on demo first and make sure it works as expected. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#146](/thread/post/8076415#post8076415 "Post Permalink")

  * Feb 18, 2015 3:51pm  Feb 18, 2015 3:51pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar389452_2.gif) SuperPip](superpip)

  * | Joined Nov 2014  | Status: Trader | [286 Posts](/search?do=process&provider=Member&searchuser=389452)

Hi guys!  
  
I don't understand how can work out the  
row 1,2,2,2,2,2...  
I know classical martingale 1,2,4..  
but are you increasing tp here?  
Can you explain that?  
  
rgds,  
SP 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#147](/thread/post/8076466#post8076466 "Post Permalink")

  * Feb 18, 2015 4:13pm  Feb 18, 2015 4:13pm 

  * [ making_money](making_money)

  * | Joined Jan 2008  | Status: Trader | [13 Posts](/search?do=process&provider=Member&searchuser=57759)

thanks for your fast reply bro, but if i use fix money setting, then it mean i cant use TP or SL? what i mean is that i can use TP and SL also for fix money setting  
  
and for magic number, it can be any number right? as long as it is different? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#148](/thread/post/8076544#post8076544 "Post Permalink")

  * Feb 18, 2015 5:01pm  Feb 18, 2015 5:01pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting making_money](/thread/post/8076466#post8076466 "View Quoted Post")
> 
> Disliked
> 
> thanks for your fast reply bro, but if i use fix money setting, then it mean i cant use TP or SL? what i mean is that i can use TP and SL also for fix money setting and for magic number, it can be any number right? as long as it is different?
> 
> Ignored

Because you are planning to set money-based target, therefore the settings for points will never be used.  
Otherwise, if you use fixed points, then the money based target settings will never be used.  
  

> [Quoting SuperPip](/thread/post/8076415#post8076415 "View Quoted Post")
> 
> Disliked
> 
> Hi guys! I don't understand how can work out the row 1,2,2,2,2,2... I know classical martingale 1,2,4.. but are you increasing tp here? Can you explain that? rgds, SP
> 
> Ignored

How can it work?  
See simple things here, if you got _lost of your money_ , you have to double your stake on the next bet, so you'll recover the previous lost, and you still get the profit of the first bet.  
See the underlined words above, technically (even though your open orders are minus), _your are NOT suffering any lost_.  
  
Just imagine this scenario:  
1\. BUY 1 LOT at 1.5000 and SELL STOP 2 LOT at 1.4950  
2\. If somehow the price goes down and 1.4950 touched, then your SELL STOP 2 LOT at 1.4950 is activated. EA will do BUY STOP 2 LOT at 1.5000.  
3\. Now if the price goes down, say 1.4800, your total BUY volume is 1 Lot, and total SELL volume is 2 Lots, you'll get profit in this case. 2 - 1 = 1 lots better when the price goes down, while the other 2 Lots is making neutral profit.  
4\. If somehow the price breaks 1.5000 and moves up say 1.5100, your total BUY volume is 3 Lots and total SELL volume is 2 Lots. You'll get profit in this case as well. 3 - 2 = 1 lots better when the price goes up, while the other 4 Lots is making neutral profit.  
  
The only problem with this approach is, the target price to make a profit will go further if there are too many martingales executed. But practically you'll get profit anyway, no doubt.  
Another way, is to increase the series by 1. Ex.: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16....  
So wherever the price goes, you'll get profit anyway, but in the same time, it will minimize the risk you have.  
Rather than having numbers like 1, 2, 4, 8, 16, 32, 64, 128, you'll end up in blowing your account during non-volatile times.  
  
You can "slow down" the martingale anyway, but it will increase your target length such as:  
1, 2, 3, _4, 4, 4, 4, 4, 4, 4, 4,_ 5, 6, 7, 8, 9..  
  
This is only the technical part and calculation. Basically, I've never done any settings as above (except for 1, 2, 2, 2, 2, 2 which I am testing now).  
As I said, you can do simulation with my excel file on my previous post. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#149](/thread/post/8076623#post8076623 "Post Permalink")

  * Feb 18, 2015 5:34pm  Feb 18, 2015 5:34pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar370635_1.gif) KanGKunG](kangkung)

  * Joined Apr 2014 | Status: Trader | [36 Posts](/search?do=process&provider=Member&searchuser=370635)

you have done a real gud job here radityo. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#150](/thread/post/8076679#post8076679 "Post Permalink")

  * Feb 18, 2015 6:01pm  Feb 18, 2015 6:01pm 

  * [ making_money](making_money)

  * | Joined Jan 2008  | Status: Trader | [13 Posts](/search?do=process&provider=Member&searchuser=57759)

hi, yes i get what you mean from the beginning. what i ask you is, is that possible for you to add also TP and SL setting in fix money setting?   
  
and i also notice that in fix money setting, there is "max loss" option. is there based on first position only or it is based on all position current P/L?  
  
thanks 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#151](/thread/post/8076685#post8076685 "Post Permalink")

  * Feb 18, 2015 6:05pm  Feb 18, 2015 6:05pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting making_money](/thread/post/8076679#post8076679 "View Quoted Post")
> 
> Disliked
> 
> hi, yes i get what you mean from the beginning. what i ask you is, is that possible for you to add also TP and SL setting in fix money setting? and i also notice that in fix money setting, there is "max loss" option. is there based on first position only or it is based on all position current P/L? thanks
> 
> Ignored

It was there, no?  
Max Loss is the SL for both Dynamic Money and Fixed Money target.  
  

> [Quoting KanGKunG](/thread/post/8076623#post8076623 "View Quoted Post")
> 
> Disliked
> 
> you have done a real gud job here radityo.
> 
> Ignored

Ya, man. Just need to proof it actually. I had started new EA for that case only. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#152](/thread/post/8076929#post8076929 "Post Permalink")

  * Feb 18, 2015 7:31pm  Feb 18, 2015 7:31pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar389452_2.gif) SuperPip](superpip)

  * | Joined Nov 2014  | Status: Trader | [286 Posts](/search?do=process&provider=Member&searchuser=389452)

Thank you for your answer!  
  

> [Quoting radityo.ardi](/thread/post/8076544#post8076544 "View Quoted Post")
> 
> Disliked
> 
> {quote} 1. BUY 1 LOT at 1.5000 and SELL STOP 2 LOT at 1.4950 2. If somehow the price goes down and 1.4950 touched, then your SELL STOP 2 LOT at 1.4950 is activated. EA will do BUY STOP 2 LOT at 1.5000. 3. Now if the price goes down, say 1.4800, your total BUY volume is 1 Lot, and total SELL volume is 2 Lots, you'll get profit in this case. 2 - 1 = 1 lots better when the price goes down, while the other 2 Lots is making neutral profit. 4. If soI've never done any settings as above (except for 1, 2, 2, 2, 2, 2 which I am testing now). As I said, you...
> 
> Ignored

Short example:  
  
1\. Sell 1 Lot at 1.500  
2\. Price goes up - Buy 2 Lots at 1.600  
3\. Price goes down - Sell 2 Lots at 1.500  
4\. Price goes up - Buy 2 Lots at 1.600  
5\. Price goes down - Sell at 1.500  
6\. Price goes up - Buy 2 Lots at 1.600  
7\. Price goes down - Sell 2 Lots at 1.500  
8\. Price goes up - Buy 2 Lots at 1.600  
9\. Price goes down - Sell 2 Lots at 1.500  
  
Price goes more down to 1.400  
  
Now you have 5 short positions from 1.500 with 9 lots and 4 long positions from 1.600 with 8 lots.  
Your balance will be negative 8 x -0.200 + 9 x 0.100 = - 1.6 + 0.9 = -0.5  
How you are generating a profit from here?  
  
SP 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#153](/thread/post/8077033#post8077033 "Post Permalink")

  * Edited 11:30pm  Feb 18, 2015 8:18pm | Edited 11:30pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting SuperPip](/thread/post/8076929#post8076929 "View Quoted Post")
> 
> Disliked
> 
> Thank you for your answer! {quote} Short example: 1. Sell 1 Lot at 1.500 2. Price goes up - Buy 2 Lots at 1.600 3. Price goes down - Sell 2 Lots at 1.500 4. Price goes up - Buy 2 Lots at 1.600 5. Price goes down - Sell at 1.500 6. Price goes up - Buy 2 Lots at 1.600 7. Price goes down - Sell 2 Lots at 1.500 8. Price goes up - Buy 2 Lots at 1.600 9. Price goes down - Sell 2 Lots at 1.500 Price goes more down to 1.400 Now you have 5 short positions from 1.500 with 9 lots and 4 long positions from 1.600 with 8 lots. Your balance will be negative 8...
> 
> Ignored

Don't expect 1.400 you'll get profit. I never said that. Everytime 2 series executed, that means the target has moved further, which is additional (2 x gaps) + (2 x spread size) in order to get total profit to $0. So you'll need to wait for sometime to get profit, because the target moved further. It doesn't mean that if 1.400 you'll get profit in any conditions.  
Based on my calculcation, with that positions, your gap is 10000 points, you'll get $0 profit at **0.69973**. Yes.... too far away to get only $0 profit...  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot2.png
Size: 50 KB](/attachment/image/1613756/thumbnail?d=1424257819)](/attachment/image/1613756?d=1424257819)   

  
  
But just imagine you have only 3 orders  
SELL 1 Lot at 1.500, BUY 2 lots 1.600, SELL 2 Lots at 1.500, you'll get $0 at **1.29991**. If it goes down, of course you'll get profit.  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot1.png
Size: 45 KB](/attachment/image/1613755/thumbnail?d=1424257763)](/attachment/image/1613755?d=1424257763)   

  
  
So, I never said there's no risk to get that "always" profit thing. Both are profitable, but we need to manage our money, am I right?  
  
The good thing for this series is just that less risk than 1, 2, 4 series. The bad is, everytime the martingale price gap range touched (which will activate you another pending orders), the $0 profit price will move further.  
  
Of course 1, 2, 4 there's a good thing as well, it will be closed anyway not far from the same price range as where the martingale starts, not too far. But the bad is, you have to manage big balance and of course your broker should allow big lots as well.  
  
  
Martingale with 1, 2, 4 is a quite great idea, but I think the implementation is wrong in the first place. _Shouldn't be applied in the lot size first of all, but in the Profit ($)_.  
If we apply it on the lot size, yes practically we are profit anyway, but to reach the profit is quite painful if the market is sideways.  
  
  
  
  
...........  
  
I think with my own statement, I GOT AN IDEA FOR ANOTHER EA!!!!![](https://resources.faireconomy.media/images/emojis/64/1f910.png?v=15.1)  
Thanks maaan... my explanation to you popping out an idea for me....   
  
  
I need to re-visit my HEAD-TAIL EA strategy....![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#154](/thread/post/8077482#post8077482 "Post Permalink")

  * Feb 18, 2015 11:20pm  Feb 18, 2015 11:20pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

I managed to check another series, which is  
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11..........  
  
High price: 1.14271  
Low price: 1.14241  
Bid: 1.13710  
Ask: 1.13713  
  

Attached Image

![](/attachment/image/1613913?d=1424269035)

  
Profit: $99  
  

Attached Image

![](/attachment/image/1613915?d=1424269091)

  
Profit: $257  
  
The more martingale index reached, the more the profit with the same current Bid and Ask price.  
At the same time it produces the same effect as 1, 2, 4, 8, 16, 32, 64....  
but with less risk.  
  
Let us try.... ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#155](/thread/post/8077580#post8077580 "Post Permalink")

  * Feb 18, 2015 11:53pm  Feb 18, 2015 11:53pm 

  * [ RHoudini](rhoudini)

  * | Joined Oct 2013  | Status: Trader | [29 Posts](/search?do=process&provider=Member&searchuser=353265)

Martingale goes well until it goes wrong.  
Simple backtesting of this kind of system shows that it will inevitably crash at some point, wiping out your whole account. Believe me, I've tested many...  
If you think that the market has a maximum of 9 Martingale steps in your "tunnel", you're in for a big surprise. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#156](/thread/post/8077635#post8077635 "Post Permalink")

  * Feb 19, 2015 12:09am  Feb 19, 2015 12:09am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting RHoudini](/thread/post/8077580#post8077580 "View Quoted Post")
> 
> Disliked
> 
> Martingale goes well until it goes wrong. Simple backtesting of this kind of system shows that it will inevitably crash at some point, wiping out your whole account. Believe me, I've tested many... If you think that the market has a maximum of 9 Martingale steps in your "tunnel", you're in for a big surprise.
> 
> Ignored

you are correct, somehow big surprises will be there. I was not also sure that martingale will stop at index 9, but finally reaches 11.  
Not only for martingale, of course. Remember what happened with CHF?  
No one thought that'll happen. some be rich in 1 night, some got big unexpected loss. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#157](/thread/post/8078403#post8078403 "Post Permalink")

  * Feb 19, 2015 4:32am  Feb 19, 2015 4:32am 

  * [ pankwinto](pankwinto)

  * | Joined Sep 2011  | Status: Trader | [8 Posts](/search?do=process&provider=Member&searchuser=196831)

> [Quoting RHoudini](/thread/post/8077580#post8077580 "View Quoted Post")
> 
> Disliked
> 
> If you think that the market has a maximum of 9 Martingale steps in your "tunnel", you're in for a big surprise.
> 
> Ignored

Today I have (opened during London session)  
25 steps by USDJPY, 118.797 - 118.757 ( 40 pp gap size).  
14 steps by EURJPY...  
  
Terrible! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#158](/thread/post/8078477#post8078477 "Post Permalink")

  * Feb 19, 2015 4:50am  Feb 19, 2015 4:50am 

  * [ aahmad29](aahmad29)

  * Joined Aug 2012 | Status: Love for all; Hatred for none | [3,557 Posts](/search?do=process&provider=Member&searchuser=286894)

> [Quoting radityo.ardi](/thread/post/8077635#post8077635 "View Quoted Post")
> 
> Disliked
> 
> {quote} you are correct, somehow big surprises will be there. I was not also sure that martingale will stop at index 9, but finally reaches 11. Not only for martingale, of course. Remember what happened with CHF? No one thought that'll happen. some be rich in 1 night, some got big unexpected loss.
> 
> Ignored

This trapping system only in loss when market is ranging. If you are experience enough to know when market is ranging then you can decrease your loss. For example, I trade on the news which are highlighted by Tony112 in his thread. I did trade FOMC and results are here.  
  
  
  
**EA can't do all work. Trader has to do some efforts in learning.**

Attached Image (click to enlarge)

[![Click to Enlarge

Name: 1.jpg
Size: 217 KB](/attachment/image/1614178/thumbnail?d=1424289035)](/attachment/image/1614178?d=1424289035)   

Love for all; Hatred for none.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#159](/thread/post/8080168#post8080168 "Post Permalink")

  * Feb 19, 2015 7:35pm  Feb 19, 2015 7:35pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting aahmad29](/thread/post/8078477#post8078477 "View Quoted Post")
> 
> Disliked
> 
> {quote} This trapping system only in loss when market is ranging. If you are experience enough to know when market is ranging then you can decrease your loss. For example, I trade on the news which are highlighted by Tony112 in his thread. I did trade FOMC and results are here. EA can't do all work. Trader has to do some efforts in learning.
> 
> Ignored

I couldn't agree more with you... ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#160](/thread/post/8081723#post8081723 "Post Permalink")

  * Feb 20, 2015 4:28am  Feb 20, 2015 4:28am 

  * [ chinedu](chinedu)

  * | Joined Feb 2009  | Status: Trader | [33 Posts](/search?do=process&provider=Member&searchuser=95312)

Please i want to know if any body has tried this system in a live account? i have been demo trading it for some days, the draw down down and the result i got is not too bad, to compare with other martingale trading system. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Trapping System: Tunnel Martingale
  *   * [ **Reply to Thread** ](/thread/524198-trapping-system-tunnel-martingale/reply#reply)

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

[Martingale, Anti-martingale, and Compounding](/thread/571233-martingale-anti-martingale-and-compounding "Hi all traders, 
i started this thread to meet others people interested in money management. 
We all know that martingale strategies are...") 40 replies

[Martingale, Reverse Martingale, Modified Martingale, Maths](/thread/736165-martingale-reverse-martingale-modified-martingale-maths "Hi all, so Martingale has been a risky yet maybe non profitable system. While roulette has an edge of \(2.7%/5.4%\) 
  
Inspired by Adam...") 1 reply

[How to change this Martingale to Reverse Martingale ?](/thread/546755-how-to-change-this-martingale-to-reverse-martingale "How to change this Martingale to Reverse Martingale ?") 3 replies

[Trapping System: Way to Fully-Automated Trading System](/thread/509226-trapping-system-way-to-fully-automated-trading-system "Hi fellow Traders! 
This is my first time to write a new thread. Would like to share a trading method, which at least made me happy right...") 47 replies

[Martingale vs. Non Martingale (Simplified RoR vs Profit)](/thread/526308-martingale-vs-non-martingale-simplified-ror-vs-profit "Martingale: The gambler doubles his bet after every loss... 
  
Martingale vs. Non Martingale \(Simplified RoR vs Profit in 3 trade runs...") 1 reply

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/524198-trapping-system-tunnel-martingale/reply#reply)
  * Subscribe
  * [221](javascript:void\(0\);)

Attachments: Trapping System: Tunnel Martingale

Tags: Trapping System: Tunnel Martingale

#  [](/thread/524198-trapping-system-tunnel-martingale)Trapping System: Tunnel Martingale 

  * 

  * [#161](/thread/post/8081758#post8081758 "Post Permalink")

  * Feb 20, 2015 4:45am  Feb 20, 2015 4:45am 

  * [ aahmad29](aahmad29)

  * Joined Aug 2012 | Status: Love for all; Hatred for none | [3,557 Posts](/search?do=process&provider=Member&searchuser=286894)

> [Quoting chinedu](/thread/post/8081723#post8081723 "View Quoted Post")
> 
> Disliked
> 
> Please i want to know if any body has tried this system in a live account? i have been demo trading it for some days, the draw down down and the result i got is not too bad, to compare with other martingale trading system.
> 
> Ignored

One suggestion from me, use this system 5 minutes before Red news in FF Calendar and trade only once. Once you get TP then no more trade and wait for next red news. You will start learning when you have to apply this system.  
  
It also depends what type of account you are using if it is ECN then use 10 pips gap and 10 Pips profit. 

Love for all; Hatred for none.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#162](/thread/post/8082914#post8082914 "Post Permalink")

  * Feb 20, 2015 7:01pm  Feb 20, 2015 7:01pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting chinedu](/thread/post/8081723#post8081723 "View Quoted Post")
> 
> Disliked
> 
> Please i want to know if any body has tried this system in a live account? i have been demo trading it for some days, the draw down down and the result i got is not too bad, to compare with other martingale trading system.
> 
> Ignored

Bro, this system is already there for long time ago. Of course some already tried with live account, which I don't know who else and how's the result. They may trade manually or using someother EA.  
  
But once you try this EA, please test it first on demo account, and recognize the behaviour.  
This EA is just a tool to help you trade with one of the martingale concept, not a money-maker machine.. ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)  
  
Your profit is really depends on you, and your settings to this EA. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#163](/thread/post/8082958#post8082958 "Post Permalink")

  * Feb 20, 2015 7:13pm  Feb 20, 2015 7:13pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

<http://www.forexfactory.com/radityo.ardi/38>  
  
See that?? It was using 1,2,2,2,2... series. Got reached martingale index 22, I had to close it because the target was too far. It was $4909 after that, down $ -91 from initial deposit of $5000.  
  
Now recovering with 1,2,3,4,5,6,7,8,9... series. Brave enough using starting lot dynamic 0.09.  
Let see what will happen next 2 weeks... 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#164](/thread/post/8084171#post8084171 "Post Permalink")

  * Feb 21, 2015 1:03am  Feb 21, 2015 1:03am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar157942_10.gif) fxindikator](fxindikator)

  * Joined Oct 2010 | Status: Trader | [167 Posts](/search?do=process&provider=Member&searchuser=157942)

> [Quoting radityo.ardi](/thread/post/8082958#post8082958 "View Quoted Post")
> 
> Disliked
> 
> <http://www.forexfactory.com/radityo.ardi/38> See that?? It was using 1,2,2,2,2... series. Got reached martingale index 22, I had to close it because the target was too far. It was $4909 after that, down $ -91 from initial deposit of $5000. Now recovering with 1,2,3,4,5,6,7,8,9... series. Brave enough using starting lot dynamic 0.09. Let see what will happen next 2 weeks...
> 
> Ignored

nice result, and such coincidence, the account age are 22 days. ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1).  
I did several test, and will start the test on the next trading day. placed the account at vps to maximize the result.  
is your current set file are exact the 1st page ?  
or there's another further improvement on setting.? just to make sure I use the right file.  
so far I do several test on high impact news only and put more 'bold' lot size ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1).  
do several attempt use different platform (even at local ID brokerage ![](https://resources.faireconomy.media/images/emojis/64/1f61c.png?v=15.1) ), bad news is these stop order are sometimes not filled correctly, I think not all price feed 'respect' news event volatility, seem you don't have any issue with your current forward tested trading account, so I test at same trading platform as yours. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#165](/thread/post/8086951#post8086951 "Post Permalink")

  * Feb 23, 2015 2:57am  Feb 23, 2015 2:57am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting fxindikator](/thread/post/8084171#post8084171 "View Quoted Post")
> 
> Disliked
> 
> {quote} nice result, and such coincidence, the account age are 22 days. ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1). I did several test, and will start the test on the next trading day. placed the account at vps to maximize the result. is your current set file are exact the 1st page ? or there's another further improvement on setting.? just to make sure I use the right file. so far I do several test on high impact news only and put more 'bold' lot size ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1). do several attempt use different platform (even at local ID brokerage ![](https://resources.faireconomy.media/images/emojis/64/1f61c.png?v=15.1) ), bad news is these stop order are sometimes not filled correctly,...
> 
> Ignored

u're from Indonesia?  
I did some observation at some specific time during high volatility and low volatility.  
My broker offers 0.3 pips [spreads](/brokers/spreads "View Live Spreads on the Broker Guide"). If I set gaps to 30 points (3 pips), it was fine at low volatility times. But at high (red) impact news, sometimes threw errors. So if I want to avoid that, I did set it to higher gaps, like 40 or 50.  
Being said as the lowest spreads broker doesn't mean 0.3 pips spreads all the time.. that's the fact. So errors is most likely because of gap is too low during high spread times. So EA can't handle the stop orders.  
  
I don't think there's limitations on which broker this EA will work. Always do an experiment to our broker first, so you know what is the best settings for the broker.  
  
Anyway, will extract the settings tomorrow for you... ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#166](/thread/post/8090640#post8090640 "Post Permalink")

  * Feb 24, 2015 12:22pm  Feb 24, 2015 12:22pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

Sorry, got no time to get the settings from VPS. But basically still the same config as in the first page. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#167](/thread/post/8091858#post8091858 "Post Permalink")

  * Feb 24, 2015 9:06pm  Feb 24, 2015 9:06pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

Hi All,  
I've uploaded v1.08.  
  
Version History:  
**v1.08**  
Added new functionality, Factor Operator. If Factor Operator is "Multiply", then the last martingale will be multiplied by Martingale Factor Modifier. If "Add" then last martingale will be added by Martingale Factor Modifier. Note that "Martingale Factor Modifier" was named as "Martingale Factor Multiplier".  
sample:  
With this settings below:  

Martingale Factor = 1,2

Martingale Factor Modifier = 2

Factor Operator = Add

will produce 1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20...  
If you change to Factor Operator = Multiply  
will produce 1, 2, 4, 8, 16, 32, ..... 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#168](/thread/post/8093016#post8093016 "Post Permalink")

  * Feb 25, 2015 2:27am  Feb 25, 2015 2:27am 

  * [ aahmad29](aahmad29)

  * Joined Aug 2012 | Status: Love for all; Hatred for none | [3,557 Posts](/search?do=process&provider=Member&searchuser=286894)

This is the way you use this system. you choose red reports and trade. Todays trades results are here  
  
Lot=0.02  
Gap=10 Pips  
Close on Profit=$1.6 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: 1.jpg
Size: 124 KB](/attachment/image/1618351/thumbnail?d=1424798820)](/attachment/image/1618351?d=1424798820)   
[![Click to Enlarge

Name: Untitled.jpg
Size: 181 KB](/attachment/image/1618352/thumbnail?d=1424798846)](/attachment/image/1618352?d=1424798846)   

Love for all; Hatred for none.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#169](/thread/post/8094113#post8094113 "Post Permalink")

  * Feb 25, 2015 12:05pm  Feb 25, 2015 12:05pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting aahmad29](/thread/post/8093016#post8093016 "View Quoted Post")
> 
> Disliked
> 
> This is the way you use this system. you choose red reports and trade. Todays trades results are here Lot=0.02 Gap=10 Pips Close on Profit=$1.6 {image} {image}
> 
> Ignored

Cool, man!  
did you use my EA for that result? 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#170](/thread/post/8094328#post8094328 "Post Permalink")

  * Feb 25, 2015 3:22pm  Feb 25, 2015 3:22pm 

  * [ aahmad29](aahmad29)

  * Joined Aug 2012 | Status: Love for all; Hatred for none | [3,557 Posts](/search?do=process&provider=Member&searchuser=286894)

> [Quoting radityo.ardi](/thread/post/8094113#post8094113 "View Quoted Post")
> 
> Disliked
> 
> {quote} Cool, man! did you use my EA for that result?
> 
> Ignored

No there are some errors, when I set your EA to close the all trades on Profit Dollar Amount. I have question and then I will set your EA for such events, Please can you tell me the settings as it is given below  
  
Gap=10 Pips  
Close all trades on Profit (net profit) =$1.6  
Initial lot=0.02  
Factor=1,2,4,8  
  
These are basic settings which my EA had it and I tried to use your EA but there was something wrong probably I did not understand settings of your EA. 

Love for all; Hatred for none.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#171](/thread/post/8094385#post8094385 "Post Permalink")

  * Feb 25, 2015 4:07pm  Feb 25, 2015 4:07pm 

  * [ aahmad29](aahmad29)

  * Joined Aug 2012 | Status: Love for all; Hatred for none | [3,557 Posts](/search?do=process&provider=Member&searchuser=286894)

> [Quoting radityo.ardi](/thread/post/8094113#post8094113 "View Quoted Post")
> 
> Disliked
> 
> {quote} Cool, man! did you use my EA for that result?
> 
> Ignored

I will set your EA 2 hours before NY open time. Pair will be EU. I will post results here and if there is any error then I will also explain it. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Image1.png
Size: 13 KB](/attachment/image/1618774/thumbnail?d=1424848031)](/attachment/image/1618774?d=1424848031)   

Love for all; Hatred for none.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#172](/thread/post/8094464#post8094464 "Post Permalink")

  * Edited 5:57pm  Feb 25, 2015 4:37pm | Edited 5:57pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting aahmad29](/thread/post/8094385#post8094385 "View Quoted Post")
> 
> Disliked
> 
> {quote} I will set your EA 2 hours before NY open time. Pair will be EU. I will post results here and if there is any error then I will also explain it. {image}
> 
> Ignored

If your gap 10 pips, and your EURUSD is 5 digits, gap settings to my EA is 100. My EA's base is not pip, since I cannot find the best way to work with pip. With points, it is easier since I can pinpoint it to digits.  
If yours is 4 digits, then you set 10.  
  
How to know whether 5 digits is to look at your marketwatch, how many numbers after decimal. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#173](/thread/post/8094510#post8094510 "Post Permalink")

  * Feb 25, 2015 4:52pm  Feb 25, 2015 4:52pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar157942_10.gif) fxindikator](fxindikator)

  * Joined Oct 2010 | Status: Trader | [167 Posts](/search?do=process&provider=Member&searchuser=157942)

> [Quoting radityo.ardi](/thread/post/8086951#post8086951 "View Quoted Post")
> 
> Disliked
> 
> {quote} u're from Indonesia? I did some observation at some specific time during high volatility and low volatility. My broker offers 0.3 pips spreads. If I set gaps to 30 points (3 pips), it was fine at low volatility times. But at high (red) impact news, sometimes threw errors. So if I want to avoid that, I did set it to higher gaps, like 40 or 50. Being said as the lowest spreads broker doesn't mean 0.3 pips spreads all the time.. that's the fact. So errors is most likely because of gap is too low during high spread times. So EA can't handle...
> 
> Ignored

yes, I am. doesnt bother about the setting if the setting are similar as listed at 1st page, will go with that. yeah spread are the key, to be honest i've been works on similar method past year ago, and the problem is the more bounces the more spreads need to be covered. I drop the research because there's no way to cover 3 spread pips + commision with bounce entry trade. and I think these method are works best during market 'rush' hour, the less sequence are the better, fast exit at profit are best for any strategies right ? ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#174](/thread/post/8094722#post8094722 "Post Permalink")

  * Feb 25, 2015 5:54pm  Feb 25, 2015 5:54pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting fxindikator](/thread/post/8094510#post8094510 "View Quoted Post")
> 
> Disliked
> 
> {quote} yes, I am. doesnt bother about the setting if the setting are similar as listed at 1st page, will go with that. yeah spread are the key, to be honest i've been works on similar method past year ago, and the problem is the more bounces the more spreads need to be covered. I drop the research because there's no way to cover 3 spread pips + commision with bounce entry trade. and I think these method are works best during market 'rush' hour, the less sequence are the better, fast exit at profit are best for any strategies right ? ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)
> 
> Ignored

I am the one that really having quite big question on how to recover if says martingale is reached the max based on our balance. This strategy is 50-50 to me, since we need to measure how big is your balance and how to overcome in such case the martingale is reached.  
But who knows, I got 35% more before reaching 30th day of the account. Let us see next 1 month then. I'm not playing this on my live account yet. Still got some doubt and trying to find the best settings from this strategy... hehehehe....  
  
Okie then, matursuwun... 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#175](/thread/post/8094959#post8094959 "Post Permalink")

  * Feb 25, 2015 6:59pm  Feb 25, 2015 6:59pm 

  * [ chirpydog](chirpydog)

  * | Joined Jan 2014  | Status: Trader | [50 Posts](/search?do=process&provider=Member&searchuser=361838)

Hello [_radityo.ardi_](http://www.forexfactory.com/radityo.ardi)  
  
I compiled the downloaded mq4 file and paste the ex4 file at the Experts directory but i received the following error upon loading the EA..  
  
2015.02.25 17:47:08.338 'TunnelMartingale' is not expert and cannot be executed  
  
Can you help ? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#176](/thread/post/8095205#post8095205 "Post Permalink")

  * Feb 25, 2015 8:17pm  Feb 25, 2015 8:17pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting chirpydog](/thread/post/8094959#post8094959 "View Quoted Post")
> 
> Disliked
> 
> Hello [radityo.ardi](http://www.forexfactory.com/radityo.ardi) I compiled the downloaded mq4 file and paste the ex4 file at the Experts directory but i received the following error upon loading the EA.. 2015.02.25 17:47:08.338 'TunnelMartingale' is not expert and cannot be executed Can you help ?
> 
> Ignored

try delete all TunnelMartingale.ex4 from Experts folder. Download the ex4 from this first thread page, then execute directly, rather than you compile it.  
  
I believe this issue is because build version of MetaEditor itself. But ex4 should work on all builds. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#177](/thread/post/8096344#post8096344 "Post Permalink")

  * Feb 26, 2015 3:31am  Feb 26, 2015 3:31am 

  * [ aahmad29](aahmad29)

  * Joined Aug 2012 | Status: Love for all; Hatred for none | [3,557 Posts](/search?do=process&provider=Member&searchuser=286894)

> [Quoting radityo.ardi](/thread/post/8094464#post8094464 "View Quoted Post")
> 
> Disliked
> 
> {quote} If your gap 10 pips, and your EURUSD is 5 digits, gap settings to my EA is 100. My EA's base is not pip, since I cannot find the best way to work with pip. With points, it is easier since I can pinpoint it to digits. If yours is 4 digits, then you set 10. How to know whether 5 digits is to look at your marketwatch, how many numbers after decimal.
> 
> Ignored

Gap=100 pints  
Profit target = $1  
Only one cycle  
  
I did activate EA a lot before news, red line is the right time to activate EA before news but at that time I was sleeping. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Untitled.jpg
Size: 164 KB](/attachment/image/1619323/thumbnail?d=1424889055)](/attachment/image/1619323?d=1424889055)   

Love for all; Hatred for none.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#178](/thread/post/8098038#post8098038 "Post Permalink")

  * Feb 26, 2015 7:47pm  Feb 26, 2015 7:47pm 

  * [ aahmad29](aahmad29)

  * Joined Aug 2012 | Status: Love for all; Hatred for none | [3,557 Posts](/search?do=process&provider=Member&searchuser=286894)

I have set your EA 3 hours before news on USDCAD pair with following settings because I am going to sleep but I will mention the position where new came in.  
  
Gap=100 Points (10 Pips)  
Profit target=$1  
Initial lot=0.01  
Other settings are default settings. 

Love for all; Hatred for none.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#179](/thread/post/8099460#post8099460 "Post Permalink")

  * Edited 3:40am  Feb 27, 2015 3:30am | Edited 3:40am 

  * [ aahmad29](aahmad29)

  * Joined Aug 2012 | Status: Love for all; Hatred for none | [3,557 Posts](/search?do=process&provider=Member&searchuser=286894)

> [Quoting radityo.ardi](/thread/post/8094464#post8094464 "View Quoted Post")
> 
> Disliked
> 
> {quote} If your gap 10 pips, and your EURUSD is 5 digits, gap settings to my EA is 100. My EA's base is not pip, since I cannot find the best way to work with pip. With points, it is easier since I can pinpoint it to digits. If yours is 4 digits, then you set 10. How to know whether 5 digits is to look at your marketwatch, how many numbers after decimal.
> 
> Ignored

Your EA gave even better results because it follows last profit direction. Here are results and all trades. If you want to do your own analysis then I want to mention that my broker time for NY open is 13:00. So you can see that how it goes after that and how many cycles are open.  
  
Those trades are taken in NY time 05:40 AM to 12:48 PM  
All order details are in Word Document.  
  
Pair = USDCAD (if EU then it will give better results)  
Gap=100 Points (10 Pips)  
Profit Trades are closed= $1  
Initial lot=0.01  
  
**Highest Active lot is 0.32**

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Untitled.jpg
Size: 205 KB](/attachment/image/1620172/thumbnail?d=1424973959)](/attachment/image/1620172?d=1424973959)   

Attached File(s)

![File Type: docx](https://assets.faireconomy.media/images/attach/docx.gif) [DetailedStatement.docx](/attachment/file/1620181?d=1424974360) 24 KB | 358 downloads 

Love for all; Hatred for none.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#180](/thread/post/8099753#post8099753 "Post Permalink")

  * Feb 27, 2015 6:32am  Feb 27, 2015 6:32am 

  * [ aahmad29](aahmad29)

  * Joined Aug 2012 | Status: Love for all; Hatred for none | [3,557 Posts](/search?do=process&provider=Member&searchuser=286894)

> [Quoting radityo.ardi](/thread/post/8094464#post8094464 "View Quoted Post")
> 
> Disliked
> 
> {quote} If your gap 10 pips, and your EURUSD is 5 digits, gap settings to my EA is 100. My EA's base is not pip, since I cannot find the best way to work with pip. With points, it is easier since I can pinpoint it to digits. If yours is 4 digits, then you set 10. How to know whether 5 digits is to look at your marketwatch, how many numbers after decimal.
> 
> Ignored

I have one question and one request.  
  
Question: Start and stop time is our PC time or broker time on our MT4 platform?  
  
Request: If you add one more option of Start and stop time then it would be easy to do forward testing on news. I take responsibility of doing forward testing the system during news. There are two main sessions when we have important news/reports are coming, one is LO and other is NYO. If we have option like this  
  
Start and stop time for First trade  
Start and stop time for second trade  
  
My plan is to take only one trade in one session if there is any Red news coming up. As soon as profit achieved and trade is closed then EA wait for second trade time. 

Love for all; Hatred for none.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Trapping System: Tunnel Martingale
  *   * [ **Reply to Thread** ](/thread/524198-trapping-system-tunnel-martingale/reply#reply)

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

[Martingale, Anti-martingale, and Compounding](/thread/571233-martingale-anti-martingale-and-compounding "Hi all traders, 
i started this thread to meet others people interested in money management. 
We all know that martingale strategies are...") 40 replies

[Martingale, Reverse Martingale, Modified Martingale, Maths](/thread/736165-martingale-reverse-martingale-modified-martingale-maths "Hi all, so Martingale has been a risky yet maybe non profitable system. While roulette has an edge of \(2.7%/5.4%\) 
  
Inspired by Adam...") 1 reply

[How to change this Martingale to Reverse Martingale ?](/thread/546755-how-to-change-this-martingale-to-reverse-martingale "How to change this Martingale to Reverse Martingale ?") 3 replies

[Trapping System: Way to Fully-Automated Trading System](/thread/509226-trapping-system-way-to-fully-automated-trading-system "Hi fellow Traders! 
This is my first time to write a new thread. Would like to share a trading method, which at least made me happy right...") 47 replies

[Martingale vs. Non Martingale (Simplified RoR vs Profit)](/thread/526308-martingale-vs-non-martingale-simplified-ror-vs-profit "Martingale: The gambler doubles his bet after every loss... 
  
Martingale vs. Non Martingale \(Simplified RoR vs Profit in 3 trade runs...") 1 reply

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/524198-trapping-system-tunnel-martingale/reply#reply)
  * Subscribe
  * [221](javascript:void\(0\);)

Attachments: Trapping System: Tunnel Martingale

Tags: Trapping System: Tunnel Martingale

#  [](/thread/524198-trapping-system-tunnel-martingale)Trapping System: Tunnel Martingale 

  * 

  * [#181](/thread/post/8099773#post8099773 "Post Permalink")

  * Feb 27, 2015 6:43am  Feb 27, 2015 6:43am 

  * [ ejikz](ejikz)

  * | Joined Jan 2010  | Status: Trader | [124 Posts](/search?do=process&provider=Member&searchuser=131860)

@ Radityo.ardi  
i really appreciate all your contribution to the development of the EA.  
Please look into this attached image and provide guide on how we can make the EA take the trade in such a pattern ..this will definitely help the huge draw down occassionally experience with the 1,2,4,8 .... or 1,2,3,4,5....  
Thanks 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: New strategy.jpg
Size: 30 KB](/attachment/image/1620273/thumbnail?d=1424987015)](/attachment/image/1620273?d=1424987015)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#182](/thread/post/8100377#post8100377 "Post Permalink")

  * Feb 27, 2015 2:19pm  Feb 27, 2015 2:19pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting aahmad29](/thread/post/8099753#post8099753 "View Quoted Post")
> 
> Disliked
> 
> {quote} I have one question and one request. Question: Start and stop time is our PC time or broker time on our MT4 platform? Request: If you add one more option of Start and stop time then it would be easy to do forward testing on news. I take responsibility of doing forward testing the system during news. There are two main sessions when we have important news/reports are coming, one is LO and other is NYO. If we have option like this Start and stop time for First trade Start and stop time for second trade My plan is to take only one trade in...
> 
> Ignored

@aahmad29,  
Actually I have thought of it before to add multiple series of date and time for start and stop time. But I won't give another parameter settings for that.  
My idea would be something like CSV file. So you put the entry line by line as below. To avoid such error readings, you need to put as date and time.  
  
27 Feb 2015 13:00:00, 27 Feb 2015 14:00:00  
27 Feb 2015 17:00:00, 27 Feb 2015 18:00:00  
  
This way, the EA will open orders at that timerange.  
Why should be like that format?  
The reason being is that you can just simply look at FF calendar for red news. Extract the date and time range for the whole month, or the whole 2 months. And let EA run under VPS. You'll get a better execution time without bothering opening and attach EA again. You'll just need to update CSV file every month.  
  
Please wait while I'm trying to make this happen ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)  
  
It is a very good feature to have.  
  

> [Quoting ejikz](/thread/post/8099773#post8099773 "View Quoted Post")
> 
> Disliked
> 
> @ Radityo.ardi i really appreciate all your contribution to the development of the EA. Please look into this attached image and provide guide on how we can make the EA take the trade in such a pattern ..this will definitely help the huge draw down occassionally experience with the 1,2,4,8 .... or 1,2,3,4,5.... Thanks {image}
> 
> Ignored

Hmm... such a different pattern.  
You can set fixed pattern like: 10, 14, 10, 14, 19, 25  
I don't know what's the next number after 25, but if you set to "Multiply" and factor as 2, then it will be 50, 100, 200.  
  
And together with that, set the starting lot to fixed: 0.01  
so it will produce 0.01 * 10 = 0.10, 0.01 * 14 = 0.14, etc  
  
Then set the target to Fixed Points, and points target type to Fixed TP and SL  
If you set Gaps to 100 points, then TP you set to 300 (you have to calculate it manually) 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#183](/thread/post/8101059#post8101059 "Post Permalink")

  * Feb 27, 2015 7:35pm  Feb 27, 2015 7:35pm 

  * [ aahmad29](aahmad29)

  * Joined Aug 2012 | Status: Love for all; Hatred for none | [3,557 Posts](/search?do=process&provider=Member&searchuser=286894)

> [Quoting radityo.ardi](/thread/post/8100377#post8100377 "View Quoted Post")
> 
> Disliked
> 
> {quote} @aahmad29, Actually I have thought of it before to add multiple series of date and time for start and stop time. But I won't give another parameter settings for that. My idea would be something like CSV file. So you put the entry line by line as below. To avoid such error readings, you need to put as date and time. 27 Feb 2015 13:00:00, 27 Feb 2015 14:00:00 27 Feb 2015 17:00:00, 27 Feb 2015 18:00:00 This way, the EA will open orders at that timerange. Why should be like that format? The reason being is that you can just simply look at FF...
> 
> Ignored

Thanks. Yes your idea is much better. I can set time ranges according to news. ![](https://resources.faireconomy.media/images/emojis/64/1f44f.png?v=15.1)

Love for all; Hatred for none.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#184](/thread/post/8102281#post8102281 "Post Permalink")

  * Feb 28, 2015 3:10am  Feb 28, 2015 3:10am 

  * [ aahmad29](aahmad29)

  * Joined Aug 2012 | Status: Love for all; Hatred for none | [3,557 Posts](/search?do=process&provider=Member&searchuser=286894)

> [Quoting radityo.ardi](/thread/post/8100377#post8100377 "View Quoted Post")
> 
> Disliked
> 
> {quote} @aahmad29, Actually I have thought of it before to add multiple series of date and time for start and stop time. But I won't give another parameter settings for that. My idea would be something like CSV file. So you put the entry line by line as below. To avoid such error readings, you need to put as date and time. 27 Feb 2015 13:00:00, 27 Feb 2015 14:00:00 27 Feb 2015 17:00:00, 27 Feb 2015 18:00:00 This way, the EA will open orders at that timerange. Why should be like that format? The reason being is that you can just simply look at FF...
> 
> Ignored

This time I set the time 5 minutes before news and first 2 trades had 0.02 max lot.  
  
Max lot used from 8:25 AM - 1:00 PM NY time was 0.08  
  
Detail attached.  
  
**Question: If I use Cycle=1 then it means that once Fixed money profit is achieved, EA will close the trade and wont take any other trade?**  
  
My plan is to take two trades a day, one in LO and other in NYO 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Untitled.jpg
Size: 156 KB](/attachment/image/1620949/thumbnail?d=1425060616)](/attachment/image/1620949?d=1425060616)   

Attached File(s)

![File Type: doc](https://assets.faireconomy.media/images/attach/doc.gif) [DetailedStatement.doc](/attachment/file/1620950?d=1425060632) 18 KB | 492 downloads 

Love for all; Hatred for none.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#185](/thread/post/8102289#post8102289 "Post Permalink")

  * Feb 28, 2015 3:18am  Feb 28, 2015 3:18am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting aahmad29](/thread/post/8102281#post8102281 "View Quoted Post")
> 
> Disliked
> 
> {quote} This time I set the time 5 minutes before news and first 2 trades had 0.02 max lot. Max lot used from 8:25 AM - 1:00 PM NY time was 0.08 Detail attached. Question: If I use Cycle=1 then it means that once Fixed money profit is achieved, EA will close the trade and wont take any other trade? My plan is to take two trades a day, one in LO and other in NYO {image} {file}
> 
> Ignored

Ya bro, you are correct. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#186](/thread/post/8104184#post8104184 "Post Permalink")

  * Mar 2, 2015 3:45am  Mar 2, 2015 3:45am 

  * [ aahmad29](aahmad29)

  * Joined Aug 2012 | Status: Love for all; Hatred for none | [3,557 Posts](/search?do=process&provider=Member&searchuser=286894)

> [Quoting radityo.ardi](/thread/post/8102289#post8102289 "View Quoted Post")
> 
> Disliked
> 
> {quote} Ya bro, you are correct.
> 
> Ignored

I will try to set EA for some of these reports.  
  
NY time 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Image1.png
Size: 18 KB](/attachment/image/1621607/thumbnail?d=1425235511)](/attachment/image/1621607?d=1425235511)   

Love for all; Hatred for none.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#187](/thread/post/8104438#post8104438 "Post Permalink")

  * Mar 2, 2015 7:17am  Mar 2, 2015 7:17am 

  * [ metta87](metta87)

  * | Joined Jul 2012  | Status: Trader | [1,170 Posts](/search?do=process&provider=Member&searchuser=271827)

> [Quoting ejikz](/thread/post/8099773#post8099773 "View Quoted Post")
> 
> Disliked
> 
> @ Radityo.ardi i really appreciate all your contribution to the development of the EA. Please look into this attached image and provide guide on how we can make the EA take the trade in such a pattern ..this will definitely help the huge draw down occassionally experience with the 1,2,4,8 .... or 1,2,3,4,5.... Thanks {image}
> 
> Ignored

You cant do anything when those type of range happen except wait and pray. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#188](/thread/post/8104903#post8104903 "Post Permalink")

  * Mar 2, 2015 3:00pm  Mar 2, 2015 3:00pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

A few notes during the weekend:  
  
It seems that still there was a bug in **Support and Resistance** and **Daily High and Low** scenario with fixed number of max cycle ( > 0).  
The bug will happen if you intend to run the EA 24/7 in VPS. But if you run ocassionally, it won't happen.  
  
My observation on Martingale with Less Risk:  
**Martingale with 1, 2, 2, 2, 2, 2...** series didn't close a cycle properly. It was simply because of the more martingale index, the target price will be more wide. So what happened is that martingale reaches somewhere in index of 40+, but never closed a cycle. I've pointed out this before actually.  
**Martingale with 1, 2, 3, 4, 5, 6...** series didn't work as well, but at least target price is more tight than 1, 2, 2, 2 series. Still martingale reaches index 30+ and it was "fine", some profit were made. But when market starts to lazy to move on, then the cycle closes longer than expected.  
**Martingale with 1, 3, 5, 7, 9, 11, 13...** again same story as above.  
  
I'll be honest with you, my conclusion is although it is less risk, you'll face these 2 problems:  
**Your cycle closes longer** , because you set it to a lowest measurement. Let us say, you've set martingale 1, 2, 2, 2, and your index reaches 50 with gap of 100 points for 5 digits pair. That means your target price is nearly impossible to reach.  
**Time does matter** , if you reached index 50, and target is reached, system will try to close all of it at the same time. While closing all orders takes time, the price sometimes changed 1 pip or 2, then the profit for the order that is still opened will change as well. So better to keep martingale index down to <15 to avoid this thing.  
  
Again, I'm testing with normal martingale starting from today, only thing is the settings is "Multiply", not with 2, but 1.5. So will produce 1, 2, 2, 3, 5, 8.... So let us see how it will be. Below is the URL for you to check.  
<http://www.forexfactory.com/radityo.ardi/61>  
  
For summary of the [normal martingale anytime](http://www.forexfactory.com/radityo.ardi/24):  
Actually this Martingale AnyTime is to find what would be the best settings to run this EA on a limited time range daily.  
It's been **28 days** since the start of this EA. The result is surprisingly a clean **40% PROFIT!**  
Below is the daily profit chart:  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot1.png
Size: 50 KB](/attachment/image/1621798/thumbnail?d=1425274670)](/attachment/image/1621798?d=1425274670)   

  
_For morning timeframe_ (08:00am SGT to 13:00pm SGT) was running at EUR/JPY for sometime, and changed to AUD/USD. But now I've removed the morning timeframe as of now. _For night timeframe_ (15:00pm SGT to 00:00am SGT) is always running at EUR/USD all along.  
  
Was quite worried, because it was reaching index 12 with volume size 40.96, but that never happened. Still 40% profit is not clean all the way.  

Attached Image

![](/attachment/image/1621802?d=1425275006)

  
See all those spikes? That was because index 12 was reached. If you look closely, there was downslope in the profit, which was because of coding mistakes for implementing Max Loss, it could've been 43% or 45% profit without this mistakes. See it on red circle in the below image.  

Attached Image

![](/attachment/image/1621805?d=1425275331)

  
  
For summary of [Martingale SNR (Support and Resistance)](http://www.forexfactory.com/radityo.ardi/81):  
Apparently the max cycle feature didn't work properly. So some days didn't get any executions. I think I have fixed it in v1.09 (not released yet). If this confirmed fixed, then I can release it.  
The profit? Quite good, **17% Profit** as of now, for the age of 32 days. There was spikes, but very less.  
There are 2 series of settings change in this SNR: Profit changed from Points to Money, and yesterday I change the series modifier to 1.5 instead of 2.0.  
  
Note:  
High risk are still there. Please put a hard note that for the same pair EURUSD, for each and every broker has different [spreads](/brokers/spreads "View Live Spreads on the Broker Guide"), movement behaviour, digits. So results can be different. I suggest you to test at least 1 or 2 months to make sure your settings is fine.  
Change in the one of the settings, change in broker, change in account type, change in spreads, or any affecting factor, that means you need to re-test again for 1 or 2 months again. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#189](/thread/post/8105804#post8105804 "Post Permalink")

  * Mar 2, 2015 10:24pm  Mar 2, 2015 10:24pm 

  * [ aahmad29](aahmad29)

  * Joined Aug 2012 | Status: Love for all; Hatred for none | [3,557 Posts](/search?do=process&provider=Member&searchuser=286894)

> [Quoting aahmad29](/thread/post/8104184#post8104184 "View Quoted Post")
> 
> Disliked
> 
> {quote} I will try to set EA for some of these reports. NY time {image}
> 
> Ignored

Here are two trades. Initial lot 0.01. Multiply factor 2  
  
I set time 4:25 to 5:25 for two red news. Cycle is 2. I will keep posting for other red news. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Untitled.jpg
Size: 217 KB](/attachment/image/1622044/thumbnail?d=1425302645)](/attachment/image/1622044?d=1425302645)   

Love for all; Hatred for none.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#190](/thread/post/8105839#post8105839 "Post Permalink")

  * Mar 2, 2015 10:44pm  Mar 2, 2015 10:44pm 

  * [ aahmad29](aahmad29)

  * Joined Aug 2012 | Status: Love for all; Hatred for none | [3,557 Posts](/search?do=process&provider=Member&searchuser=286894)

> [Quoting radityo.ardi](/thread/post/8102289#post8102289 "View Quoted Post")
> 
> Disliked
> 
> {quote} Ya bro, you are correct.
> 
> Ignored

Check your PM. 

Love for all; Hatred for none.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#191](/thread/post/8106385#post8106385 "Post Permalink")

  * Mar 3, 2015 2:12am  Mar 3, 2015 2:12am 

  * [ sorin24](sorin24)

  * | Joined Feb 2013  | Status: Trader | [16 Posts](/search?do=process&provider=Member&searchuser=325266)

I'm not sure what I did but something must be wrong... On testing, after changing many settings, it gave me around 125 000 transactions in 40 days.  
initial deposit - 500 usd. total net profit - 34 365 usd.  
I don't think that any broker will let me test this on a live account. ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

Attached Image (click to enlarge)

[![Click to Enlarge

Name: m1.JPG
Size: 94 KB](/attachment/image/1622213/thumbnail?d=1425316067)](/attachment/image/1622213?d=1425316067)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#192](/thread/post/8106456#post8106456 "Post Permalink")

  * Mar 3, 2015 2:52am  Mar 3, 2015 2:52am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar42265_1.gif) huatboyz](huatboyz)

  * Joined Jun 2007 | Status: Trader | [190 Posts](/search?do=process&provider=Member&searchuser=42265)

Hi Sorin,  
  
May I know what settings did u use please?  
  

> [Quoting sorin24](/thread/post/8106385#post8106385 "View Quoted Post")
> 
> Disliked
> 
> I'm not sure what I did but something must be wrong... On testing, after changing many settings, it gave me around 125 000 transactions in 40 days. initial deposit - 500 usd. total net profit - 34 365 usd. I don't think that any broker will let me test this on a live account. ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) {image}
> 
> Ignored

Pips Collector EA, No Martingale, No Grid

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#193](/thread/post/8106558#post8106558 "Post Permalink")

  * Mar 3, 2015 4:00am  Mar 3, 2015 4:00am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar325475_7.gif) mahdihasan](mahdihasan)

  * | Commercial User  | Joined Feb 2013 | [53 Posts](/search?do=process&provider=Member&searchuser=325475)

> [Quoting sorin24](/thread/post/8106385#post8106385 "View Quoted Post")
> 
> Disliked
> 
> I'm not sure what I did but something must be wrong... On testing, after changing many settings, it gave me around 125 000 transactions in 40 days. initial deposit - 500 usd. total net profit - 34 365 usd. I don't think that any broker will let me test this on a live account. ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) {image}
> 
> Ignored

Nice job dude, hope u will share your settings 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#194](/thread/post/8106678#post8106678 "Post Permalink")

  * Mar 3, 2015 5:23am  Mar 3, 2015 5:23am 

  * [ sorin24](sorin24)

  * | Joined Feb 2013  | Status: Trader | [16 Posts](/search?do=process&provider=Member&searchuser=325266)

maybe I got a virus in my PC...with 10k start money now it went to 287k. I really need to see what's wrong but beer doesn't help so far... 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: m2 10k start.JPG
Size: 100 KB](/attachment/image/1622290/thumbnail?d=1425327768)](/attachment/image/1622290?d=1425327768)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#195](/thread/post/8107371#post8107371 "Post Permalink")

  * Mar 3, 2015 2:25pm  Mar 3, 2015 2:25pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting sorin24](/thread/post/8106385#post8106385 "View Quoted Post")
> 
> Disliked
> 
> I'm not sure what I did but something must be wrong... On testing, after changing many settings, it gave me around 125 000 transactions in 40 days. initial deposit - 500 usd. total net profit - 34 365 usd. I don't think that any broker will let me test this on a live account. ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) {image}
> 
> Ignored

You gotta be kidding me?!!  
Share your settings then... I'm as the coder of this EA is also curious to know, since I always thought that kind of big profit can't be happened.  
  
Anyway, beer will help only if you got problem, not the otherwise... ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#196](/thread/post/8107854#post8107854 "Post Permalink")

  * Mar 3, 2015 6:23pm  Mar 3, 2015 6:23pm 

  * [ sorin24](sorin24)

  * | Joined Feb 2013  | Status: Trader | [16 Posts](/search?do=process&provider=Member&searchuser=325266)

something it's wrong with the platform from squared financial. On [fxcm](/brokers/fxcm "View FXCM Broker Profile") it doesn't work the same. However, I will keep testing on a demo account on live trading to see what's wrong. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#197](/thread/post/8107974#post8107974 "Post Permalink")

  * Mar 3, 2015 7:06pm  Mar 3, 2015 7:06pm 

  * [ pankwinto](pankwinto)

  * | Joined Sep 2011  | Status: Trader | [8 Posts](/search?do=process&provider=Member&searchuser=196831)

> [Quoting sorin24](/thread/post/8106385#post8106385 "View Quoted Post")
> 
> Disliked
> 
> I'm not sure what I did but something must be wrong... On testing, after changing many settings, it gave me around 125 000 transactions in 40 days. initial deposit - 500 usd. total net profit - 34 365 usd. I don't think that any broker will let me test this on a live account. ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) {image}
> 
> Ignored

Its just impossible. You must have about 2-3 transactions (closed orders) at every M1 bar (125000/40 days / 1440 ). 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#198](/thread/post/8111562#post8111562 "Post Permalink")

  * Mar 4, 2015 10:34pm  Mar 4, 2015 10:34pm 

  * [ Reamasesa](reamasesa)

  * Joined Jan 2015 | Status: Trader | [916 Posts](/search?do=process&provider=Member&searchuser=397375)

Hi,  
  
Thanks for this awesome EA.  
Can you add trade comment instead of the index, please?  
  
  
Thanks 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#199](/thread/post/8111710#post8111710 "Post Permalink")

  * Mar 4, 2015 11:12pm  Mar 4, 2015 11:12pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting Reamasesa](/thread/post/8111562#post8111562 "View Quoted Post")
> 
> Disliked
> 
> Hi, Thanks for this awesome EA. Can you add trade comment instead of the index, please? Thanks
> 
> Ignored

Don't change any index at the moment. The index is important for EA to recognize the trades.  
I'm in the middle of removing the index in the comment section, will release it this weekend once it is done. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#200](/thread/post/8111743#post8111743 "Post Permalink")

  * Mar 4, 2015 11:19pm  Mar 4, 2015 11:19pm 

  * [ Reamasesa](reamasesa)

  * Joined Jan 2015 | Status: Trader | [916 Posts](/search?do=process&provider=Member&searchuser=397375)

> [Quoting radityo.ardi](/thread/post/8111710#post8111710 "View Quoted Post")
> 
> Disliked
> 
> {quote} Don't change any index at the moment. The index is important for EA to recognize the trades. I'm in the middle of removing the index in the comment section, will release it this weekend once it is done.
> 
> Ignored

Thanks! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Trapping System: Tunnel Martingale
  *   * [ **Reply to Thread** ](/thread/524198-trapping-system-tunnel-martingale/reply#reply)

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

[Martingale, Anti-martingale, and Compounding](/thread/571233-martingale-anti-martingale-and-compounding "Hi all traders, 
i started this thread to meet others people interested in money management. 
We all know that martingale strategies are...") 40 replies

[Martingale, Reverse Martingale, Modified Martingale, Maths](/thread/736165-martingale-reverse-martingale-modified-martingale-maths "Hi all, so Martingale has been a risky yet maybe non profitable system. While roulette has an edge of \(2.7%/5.4%\) 
  
Inspired by Adam...") 1 reply

[How to change this Martingale to Reverse Martingale ?](/thread/546755-how-to-change-this-martingale-to-reverse-martingale "How to change this Martingale to Reverse Martingale ?") 3 replies

[Trapping System: Way to Fully-Automated Trading System](/thread/509226-trapping-system-way-to-fully-automated-trading-system "Hi fellow Traders! 
This is my first time to write a new thread. Would like to share a trading method, which at least made me happy right...") 47 replies

[Martingale vs. Non Martingale (Simplified RoR vs Profit)](/thread/526308-martingale-vs-non-martingale-simplified-ror-vs-profit "Martingale: The gambler doubles his bet after every loss... 
  
Martingale vs. Non Martingale \(Simplified RoR vs Profit in 3 trade runs...") 1 reply

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/524198-trapping-system-tunnel-martingale/reply#reply)
  * Subscribe
  * [221](javascript:void\(0\);)

Attachments: Trapping System: Tunnel Martingale

Tags: Trapping System: Tunnel Martingale

#  [](/thread/524198-trapping-system-tunnel-martingale)Trapping System: Tunnel Martingale 

  * 

  * [#201](/thread/post/8111751#post8111751 "Post Permalink")

  * Mar 4, 2015 11:23pm  Mar 4, 2015 11:23pm 

  * [ sorin24](sorin24)

  * | Joined Feb 2013  | Status: Trader | [16 Posts](/search?do=process&provider=Member&searchuser=325266)

somehow it doesn't close the trades on demo account. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: squared martingale2.JPG
Size: 78 KB](/attachment/image/1623811/thumbnail?d=1425479024)](/attachment/image/1623811?d=1425479024)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#202](/thread/post/8112762#post8112762 "Post Permalink")

  * Mar 5, 2015 6:12am  Mar 5, 2015 6:12am 

  * [ Reamasesa](reamasesa)

  * Joined Jan 2015 | Status: Trader | [916 Posts](/search?do=process&provider=Member&searchuser=397375)

> [Quoting sorin24](/thread/post/8111751#post8111751 "View Quoted Post")
> 
> Disliked
> 
> somehow it doesn't close the trades on demo account. {image}
> 
> Ignored

It closes on mine but very late or at the swap, which is a loss on mine.  
Didn't happen on my real account but I don't have the funds to further forward test it on it. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#203](/thread/post/8112799#post8112799 "Post Permalink")

  * Mar 5, 2015 6:37am  Mar 5, 2015 6:37am 

  * [ sorin24](sorin24)

  * | Joined Feb 2013  | Status: Trader | [16 Posts](/search?do=process&provider=Member&searchuser=325266)

I don't know what's wrong so far... And I hate that...because I would really like to use this on a real account. If it's working in a proper way it should give only gains or it should close at zero gain/loss. Are you using this on a real account? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#204](/thread/post/8113634#post8113634 "Post Permalink")

  * Mar 5, 2015 5:23pm  Mar 5, 2015 5:23pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting sorin24](/thread/post/8111751#post8111751 "View Quoted Post")
> 
> Disliked
> 
> somehow it doesn't close the trades on demo account. {image}
> 
> Ignored

This case is rarely happened at the settings which has lower gaps.  
What I observed and happened was (this happened very quickly):  
1\. Say you have opened 0.1 lot buy, and 0.2 sell stop.  
2\. The 0.2 sell stop is touched by the current price.  
3\. At the moment 0.2 sell stop is touched and changed to sell, EA will create 0.4 buy stop.  
4\. The moment 0.4 buy stop is still in process, the price quickly retracted back to the area near (or higher than) 0.1 buy price.  
5\. EA throws errors in alert window. 0.4 buy stop failed to create, but the price is already moving to higher level and never came back.  
6\. System keeps throwing errors since the buy stop price is not created.  
  
So this is how you got no stop order for your case, and opened orders never closes.  
  
To fix this, is actually to set the gap higher (3 or 5 pips higher). This case **never** happened on Martingale SNR (trade explorer above), since the gap for it is 100 points (10 pips), and my broker's spread is 0.2 pips (2 points).  
Please test it first on your demo acc, for at least 1 month. Try to pass everything, red news, yellow news, or NFP. See what's the best settings for you.  
  
I know still a lot of room to improve this EA better. But don't be rush with live account. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#205](/thread/post/8117349#post8117349 "Post Permalink")

  * Mar 6, 2015 8:46pm  Mar 6, 2015 8:46pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

This is what I called as risk... ![](https://resources.faireconomy.media/images/emojis/64/1f923.png?v=15.1)  
1, 2, 4 is a bad combination actually. Finally reached the limit (in a bad way), no margin left to open new order, was in the bad position.  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot1.png
Size: 119 KB](/attachment/image/1625448/thumbnail?d=1425642175)](/attachment/image/1625448?d=1425642175)   

  
  
But somehow the position returned back and closed at profit...  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot2.png
Size: 87 KB](/attachment/image/1625450/thumbnail?d=1425642267)](/attachment/image/1625450?d=1425642267)   

  
  
This is why I don't like to encourage people to use 1, 2, 4 series. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#206](/thread/post/8118013#post8118013 "Post Permalink")

  * Edited 11:35pm  Mar 6, 2015 11:12pm | Edited 11:35pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar399344_1.gif) Belmort](belmort)

  * | Joined Feb 2015  | Status: Trader | [13 Posts](/search?do=process&provider=Member&searchuser=399344)

Hai radityo. I test based on Fixed points target types but I think there's a problem.  
Why the trade close when it's not hit your TP point?  
I filled the the Point target 250 and Point stop loss 250 (5 Digits).  
The second one is max cycle. I filled the max cycle 1 but it keeps open trade. 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: tes.jpg
Size: 69 KB](/attachment/image/1625630/thumbnail?d=1425651111)](/attachment/image/1625630?d=1425651111)   
[![Click to Enlarge

Name: tes 2.jpg
Size: 137 KB](/attachment/image/1625660/thumbnail?d=1425652474)](/attachment/image/1625660?d=1425652474)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#207](/thread/post/8118615#post8118615 "Post Permalink")

  * Mar 7, 2015 2:00am  Mar 7, 2015 2:00am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting Belmort](/thread/post/8118013#post8118013 "View Quoted Post")
> 
> Disliked
> 
> Hai radityo. I test based on Fixed points target types but I think there's a problem. Why the trade close when it's not hit your TP point? I filled the the Point target 250 and Point stop loss 250 (5 Digits). The second one is max cycle. I filled the max cycle 1 but it keeps open trade. {image} {image}
> 
> Ignored

Let me check that out, bro. But I hope you didn't run any other EA / Indicators together with my EA.  
Because this same kind of thing was happened to a bro, and I was scratching my head. Turned out that this bro ran a different EA which does closing trade before time. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#208](/thread/post/8119070#post8119070 "Post Permalink")

  * Mar 7, 2015 5:40am  Mar 7, 2015 5:40am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar399344_1.gif) Belmort](belmort)

  * | Joined Feb 2015  | Status: Trader | [13 Posts](/search?do=process&provider=Member&searchuser=399344)

> [Quoting radityo.ardi](/thread/post/8118615#post8118615 "View Quoted Post")
> 
> Disliked
> 
> {quote} Let me check that out, bro. But I hope you didn't run any other EA / Indicators together with my EA. Because this same kind of thing was happened to a bro, and I was scratching my head. Turned out that this bro ran a different EA which does closing trade before time.
> 
> Ignored

No bro. Just single EA. Yours ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#209](/thread/post/8123574#post8123574 "Post Permalink")

  * Mar 10, 2015 10:18am  Mar 10, 2015 10:18am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar370635_1.gif) KanGKunG](kangkung)

  * Joined Apr 2014 | Status: Trader | [36 Posts](/search?do=process&provider=Member&searchuser=370635)

nice return so far.. tq radityo 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#210](/thread/post/8126386#post8126386 "Post Permalink")

  * Mar 11, 2015 6:13am  Mar 11, 2015 6:13am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar403827_1.gif) Jl29](jl29)

  * | Commercial User  | Joined Mar 2015 | [20 Posts](/search?do=process&provider=Member&searchuser=403827)

rad,  
  
Hey i keep getting error messages when I run the EA.  
  
Says..."Invalid Stops"  
  
Thanks,  
  
**Jl29**

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#211](/thread/post/8126402#post8126402 "Post Permalink")

  * Mar 11, 2015 6:20am  Mar 11, 2015 6:20am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar403827_1.gif) Jl29](jl29)

  * | Commercial User  | Joined Mar 2015 | [20 Posts](/search?do=process&provider=Member&searchuser=403827)

> [Quoting radityo.ardi](/thread/post/8117349#post8117349 "View Quoted Post")
> 
> Disliked
> 
> This is what I called as risk... ![](https://resources.faireconomy.media/images/emojis/64/1f923.png?v=15.1) 1, 2, 4 is a bad combination actually. Finally reached the limit (in a bad way), no margin left to open new order, was in the bad position. {image} But somehow the position returned back and closed at profit... {image} This is why I don't like to encourage people to use 1, 2, 4 series.
> 
> Ignored

  
what is the safest series to use? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#212](/thread/post/8126937#post8126937 "Post Permalink")

  * Mar 11, 2015 2:20pm  Mar 11, 2015 2:20pm 

  * [ aahmad29](aahmad29)

  * Joined Aug 2012 | Status: Love for all; Hatred for none | [3,557 Posts](/search?do=process&provider=Member&searchuser=286894)

> [Quoting radityo.ardi](/thread/post/8118615#post8118615 "View Quoted Post")
> 
> Disliked
> 
> {quote} Let me check that out, bro. But I hope you didn't run any other EA / Indicators together with my EA. Because this same kind of thing was happened to a bro, and I was scratching my head. Turned out that this bro ran a different EA which does closing trade before time.
> 
> Ignored

Hi radityo.ardi  
  
I know you have already given your valuable time to this thread but if you have any spare time please can you add one feature that EA must activate when price reaches on given price. Suppose I want EA to activate at price "e.g. 1.34**50".**  
  
Thanks 

Love for all; Hatred for none.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#213](/thread/post/8126948#post8126948 "Post Permalink")

  * Edited 3:04pm  Mar 11, 2015 2:39pm | Edited 3:04pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting aahmad29](/thread/post/8126937#post8126937 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi radityo.ardi I know you have already given your valuable time to this thread but if you have any spare time please can you add one feature that EA must activate when price reaches on given price. Suppose I want EA to activate at price "e.g. 1.3450". Thanks
> 
> Ignored

Noted. I haven't got much time lately last week and this week.  
Actually have planned to release v1.09, but got stucked up since I want the big change also included in that version.  
  
I'll take your idea up, will release it at v1.10+.  
  

> [Quoting Jl29](/thread/post/8126402#post8126402 "View Quoted Post")
> 
> Disliked
> 
> {quote} what is the safest series to use?
> 
> Ignored

Safest?  
Sequential number series is the safest: 1, 2, 3, 4, 5....  
This can be achieved by setting up operation to "Add" and Martingale: 1.  
But that comes with another risks, the cycle will be very hard to close if you stuck up on sideways / ranging market. The longer the martingale index is (count of opened order), the target will be very hard to achieve. But this still (logically) can be avoided by widening the gap (standard gap is normally 10 pips).  
  
If you see on top of this thread, see Martingale SNR there? That is using 1.5 modifier with operation of Multiply, (instead of standard modifier which is 2). So, this will produce 1, 2, 2, 3, 5, 8...  
The Martingale Anytime using Gaps of 30 points, while Martingale SNR using the standard gaps which is 100 points.  
  

> [Quoting Jl29](/thread/post/8126386#post8126386 "View Quoted Post")
> 
> Disliked
> 
> rad, Hey i keep getting error messages when I run the EA. Says..."Invalid Stops" Thanks, Jl29
> 
> Ignored

Common issue when you set the gap too low.  
You need to identify on which digits you are on. If on EURUSD you have price such as 1.08933, then that's 5 digits, and for 10 pips = 100 points. If your average spread is around 15 points, minimum gaps you can set is around 50 points.  
Having that configured as 50 points doesn't mean it will free of "invalid stops" error. Ocassionally will throw error, since your broker is having dynamic spread (check this with your broker).  
  
So as I said before, the safest gap is around 10 pips (100 points in 5 digits).  
\---------------------------------------------------------------------  
  
A PM that was sent to me, then I replied back. Worth to share...  
  
Q: 

> Quote
> 
> Disliked
> 
> Hi,  
>  have you looked into Semi Martingale method (<http://www.forexfactory.com/showthread.php?t=43221)?> thanks.

A: 

> Quote
> 
> Disliked
> 
> This settings will do. Martingale Index: 1, 1, 2, 3, 4, 6, 8, 11, 15, 20, 27, 36, 47, 62, 80, 102, 130, 165, 208, 263, 331, 416, 522, 655.  
>  Gap: 100 points (for 5 digits)  
>  Target: Fixed Points  
>  Target Mode: Fixed TP and SL  
>  TP: 400 points  
>  SL: 500 points (400 points + 100 gaps)

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#214](/thread/post/8126997#post8126997 "Post Permalink")

  * Mar 11, 2015 3:38pm  Mar 11, 2015 3:38pm 

  * [ happytrade38](happytrade38)

  * | Joined Sep 2014  | Status: Trader | [517 Posts](/search?do=process&provider=Member&searchuser=382480)

Hi ardi,  
Would you know the cause of this error? and how to fix this? 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: error.png
Size: 236 KB](/attachment/image/1628632/thumbnail?d=1426055841)](/attachment/image/1628632?d=1426055841)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#215](/thread/post/8127063#post8127063 "Post Permalink")

  * Mar 11, 2015 4:22pm  Mar 11, 2015 4:22pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting happytrade38](/thread/post/8126997#post8126997 "View Quoted Post")
> 
> Disliked
> 
> Hi ardi, Would you know the cause of this error? and how to fix this? {image}
> 
> Ignored

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot2.png
Size: 84 KB](/attachment/image/1628658/thumbnail?d=1426058453)](/attachment/image/1628658?d=1426058453)   

  
  
  
Be careful, your pair seems to be in 5 digits. So, 1 pip refer to 10 points. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#216](/thread/post/8127076#post8127076 "Post Permalink")

  * Mar 11, 2015 4:31pm  Mar 11, 2015 4:31pm 

  * [ happytrade38](happytrade38)

  * | Joined Sep 2014  | Status: Trader | [517 Posts](/search?do=process&provider=Member&searchuser=382480)

> [Quoting radityo.ardi](/thread/post/8127063#post8127063 "View Quoted Post")
> 
> Disliked
> 

> 
> Ignored

Hi Ardi,  
You are such a great person. it works now. thanks a lot. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#217](/thread/post/8127195#post8127195 "Post Permalink")

  * Mar 11, 2015 5:18pm  Mar 11, 2015 5:18pm 

  * [ happytrade38](happytrade38)

  * | Joined Sep 2014  | Status: Trader | [517 Posts](/search?do=process&provider=Member&searchuser=382480)

Hi Ardi,  
Another error. Could it be due to slippage turn off?  
Due to this error, it resulting few orders open due to unknown error.  
I observe one thing, after adding this EA into the chart and didn't turn on the auto-trading, error "Trade is not allowed in EA" keep pop-up. Are you exprienced it? 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: error.png
Size: 14 KB](/attachment/image/1628681/thumbnail?d=1426061684)](/attachment/image/1628681?d=1426061684)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#218](/thread/post/8127198#post8127198 "Post Permalink")

  * Mar 11, 2015 5:19pm  Mar 11, 2015 5:19pm 

  * [ aahmad29](aahmad29)

  * Joined Aug 2012 | Status: Love for all; Hatred for none | [3,557 Posts](/search?do=process&provider=Member&searchuser=286894)

> [Quoting radityo.ardi](/thread/post/8126948#post8126948 "View Quoted Post")
> 
> Disliked
> 
> {quote} Noted. I haven't got much time lately last week and this week. Actually have planned to release v1.09, but got stucked up since I want the big change also included in that version. I'll take your idea up, will release it at v1.10+. {quote} Safest? Sequential number series is the safest: 1, 2, 3, 4, 5.... This can be achieved by setting up operation to "Add" and Martingale: 1. But that comes with another risks, the cycle will be very hard to close if you stuck up on sideways / ranging market. The longer the martingale index is (count of opened...
> 
> Ignored

Thanks. 

Love for all; Hatred for none.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#219](/thread/post/8127236#post8127236 "Post Permalink")

  * Mar 11, 2015 5:27pm  Mar 11, 2015 5:27pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting happytrade38](/thread/post/8127195#post8127195 "View Quoted Post")
> 
> Disliked
> 
> Hi Ardi, Another error. Could it be due to slippage turn off? Due to this error, it resulting few orders open due to unknown error. I observe one thing, after adding this EA into the chart and didn't turn on the auto-trading, error "Trade is not allowed in EA" keep pop-up. Are you exprienced it? {image}
> 
> Ignored

hmm... your case seems new to me. But I think that's due to the closing price is not updated to the latest. So I think (probably) slippage would help that. Just try it out but honestly I have no answer for that.  
  
Yes, the error will always be shown until you turn on auto-trading. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#220](/thread/post/8127531#post8127531 "Post Permalink")

  * Mar 11, 2015 6:44pm  Mar 11, 2015 6:44pm 

  * [ happytrade38](happytrade38)

  * | Joined Sep 2014  | Status: Trader | [517 Posts](/search?do=process&provider=Member&searchuser=382480)

> [Quoting radityo.ardi](/thread/post/8127236#post8127236 "View Quoted Post")
> 
> Disliked
> 
> {quote} hmm... your case seems new to me. But I think that's due to the closing price is not updated to the latest. So I think (probably) slippage would help that. Just try it out but honestly I have no answer for that. Yes, the error will always be shown until you turn on auto-trading.
> 
> Ignored

Thanks. will try it out and update again. thanks. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Trapping System: Tunnel Martingale
  *   * [ **Reply to Thread** ](/thread/524198-trapping-system-tunnel-martingale/reply#reply)

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

[Martingale, Anti-martingale, and Compounding](/thread/571233-martingale-anti-martingale-and-compounding "Hi all traders, 
i started this thread to meet others people interested in money management. 
We all know that martingale strategies are...") 40 replies

[Martingale, Reverse Martingale, Modified Martingale, Maths](/thread/736165-martingale-reverse-martingale-modified-martingale-maths "Hi all, so Martingale has been a risky yet maybe non profitable system. While roulette has an edge of \(2.7%/5.4%\) 
  
Inspired by Adam...") 1 reply

[How to change this Martingale to Reverse Martingale ?](/thread/546755-how-to-change-this-martingale-to-reverse-martingale "How to change this Martingale to Reverse Martingale ?") 3 replies

[Trapping System: Way to Fully-Automated Trading System](/thread/509226-trapping-system-way-to-fully-automated-trading-system "Hi fellow Traders! 
This is my first time to write a new thread. Would like to share a trading method, which at least made me happy right...") 47 replies

[Martingale vs. Non Martingale (Simplified RoR vs Profit)](/thread/526308-martingale-vs-non-martingale-simplified-ror-vs-profit "Martingale: The gambler doubles his bet after every loss... 
  
Martingale vs. Non Martingale \(Simplified RoR vs Profit in 3 trade runs...") 1 reply

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/524198-trapping-system-tunnel-martingale/reply#reply)
  * Subscribe
  * [221](javascript:void\(0\);)

Attachments: Trapping System: Tunnel Martingale

Tags: Trapping System: Tunnel Martingale

#  [](/thread/524198-trapping-system-tunnel-martingale)Trapping System: Tunnel Martingale 

  * 

  * [#221](/thread/post/8128817#post8128817 "Post Permalink")

  * Edited 1:14am  Mar 12, 2015 12:55am | Edited 1:14am 

  * [ aahmad29](aahmad29)

  * Joined Aug 2012 | Status: Love for all; Hatred for none | [3,557 Posts](/search?do=process&provider=Member&searchuser=286894)

> [Quoting radityo.ardi](/thread/post/8126948#post8126948 "View Quoted Post")
> 
> Disliked
> 
> {quote} Noted. I haven't got much time lately last week and this week. Actually have planned to release v1.09, but got stucked up since I want the big change also included in that version. I'll take your idea up, will release it at v1.10+. {quote} Safest? Sequential number series is the safest: 1, 2, 3, 4, 5.... This can be achieved by setting up operation to "Add" and Martingale: 1. But that comes with another risks, the cycle will be very hard to close if you stuck up on sideways / ranging market. The longer the martingale index is (count of opened...
> 
> Ignored

Reason to ask about my request is that probably some people use 100 Pips (1000 Points) gap and my suggestion is that they activate the EA at half number and avoid whole number. In this case, traders wont have huge lots (most of time maximum number of orders will be 6) e.g 0.01, 0.02, 0.04, 0.08, 0.16, 0.32. Cycle should be 1. Once your EA close the order with given profit in dollars, Don't activate EA until price reaches again at half number.  
  
I am sure that no one tested the system like that. I do full time job so it is not possible for me to do manual test but still I will try my best to do manual test on my next off days.  
  
I will appreciate if any trader comes forward and test this scenario on EU pair. If initial lot is 0.01 then profit dollar must be $5. If initial lot is 0.1 then profit dollar must be $50. Once EA achieve the net profit dollar among all open positions, EA close the orders and wait for price to go back to 50 level. 

Love for all; Hatred for none.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#222](/thread/post/8129767#post8129767 "Post Permalink")

  * Mar 12, 2015 6:58am  Mar 12, 2015 6:58am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar403827_1.gif) Jl29](jl29)

  * | Commercial User  | Joined Mar 2015 | [20 Posts](/search?do=process&provider=Member&searchuser=403827)

rad,  
  
what are your take profit rules? and is there a way to customize my own take profit?   
  
Thanks again!  
  
Jl29 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#223](/thread/post/8130091#post8130091 "Post Permalink")

  * Mar 12, 2015 10:59am  Mar 12, 2015 10:59am 

  * [ happytrade38](happytrade38)

  * | Joined Sep 2014  | Status: Trader | [517 Posts](/search?do=process&provider=Member&searchuser=382480)

Hi [radityo.ardi](http://www.forexfactory.com/showthread.php?p=8126948#post8126948),  
  
I was setting the TP to 40pips (400 points), however, as per the highlighted order (EURUSD, the profit already in 42pips), but the order didn't close. Is it normal? 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: error.png
Size: 176 KB](/attachment/image/1629595/thumbnail?d=1426125374)](/attachment/image/1629595?d=1426125374)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#224](/thread/post/8130175#post8130175 "Post Permalink")

  * Mar 12, 2015 11:54am  Mar 12, 2015 11:54am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting happytrade38](/thread/post/8130091#post8130091 "View Quoted Post")
> 
> Disliked
> 
> Hi [radityo.ardi](http://www.forexfactory.com/showthread.php?p=8126948#post8126948), I was setting the TP to 40pips (400 points), however, as per the highlighted order (EURUSD, the profit already in 42pips), but the order didn't close. Is it normal? {image}
> 
> Ignored

OK.  
Your pair is 3 digits, so 400 points = 40 pips.  
High Gap: 121.541  
Low Gap: 121.441  
Current Price: 121.659  
  
  
So I suppose it is not yet reached to 400 points.  
Looking at the screenshot and based on your settings it should be closed when the price reaches 121.541 (SL) or 121.041 (TP). Hmm... I think there's a bug when you select _Next cycle start by follow last profit direction_ setting and case where SELL is created first.  
  
Before I confirm that is a bug, can you get me the dashboard screenshot?  
dashboard is the yellow printed text on the left top side of the chart, as in screenshot below. 

Attached Image

![](/attachment/image/1629641?d=1426129249)

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#225](/thread/post/8130207#post8130207 "Post Permalink")

  * Mar 12, 2015 12:13pm  Mar 12, 2015 12:13pm 

  * [ happytrade38](happytrade38)

  * | Joined Sep 2014  | Status: Trader | [517 Posts](/search?do=process&provider=Member&searchuser=382480)

> [Quoting radityo.ardi](/thread/post/8130175#post8130175 "View Quoted Post")
> 
> Disliked
> 
> {quote} OK. Your pair is 3 digits, so 400 points = 40 pips. High Gap: 121.541 Low Gap: 121.441 Current Price: 121.659 So I suppose it is not yet reached to 400 points. Looking at the screenshot and based on your settings it should be closed when the price reaches 121.541 (SL) or 121.041 (TP). Hmm... I think there's a bug when you select Next cycle start by follow last profit direction setting and case where SELL is created first. Before I confirm that is a bug, can you get me the dashboard screenshot? dashboard is the yellow printed text on the...
> 
> Ignored

  
Thanks for the prompt response.   
Here you go for the dashboard screenshot. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: error.png
Size: 98 KB](/attachment/image/1629646/thumbnail?d=1426130003)](/attachment/image/1629646?d=1426130003)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#226](/thread/post/8130223#post8130223 "Post Permalink")

  * Mar 12, 2015 12:24pm  Mar 12, 2015 12:24pm 

  * [ happytrade38](happytrade38)

  * | Joined Sep 2014  | Status: Trader | [517 Posts](/search?do=process&provider=Member&searchuser=382480)

> [Quoting radityo.ardi](/thread/post/8130175#post8130175 "View Quoted Post")
> 
> Disliked
> 
> {quote} OK. Your pair is 3 digits, so 400 points = 40 pips. High Gap: 121.541 Low Gap: 121.441 Current Price: 121.659 So I suppose it is not yet reached to 400 points. Looking at the screenshot and based on your settings it should be closed when the price reaches 121.541 (SL) or 121.041 (TP). Hmm... I think there's a bug when you select Next cycle start by follow last profit direction setting and case where SELL is created first. Before I confirm that is a bug, can you get me the dashboard screenshot? dashboard is the yellow printed text on the...
> 
> Ignored

Hi radityo.ardi,  
Something to add. Yes, guess USDJPY with 3 digits have the issue.  
However, the EURUSD with 5 digits shouldn't be an issue, as per the last screenshot, the pips is 423 and yet to be closed.  
For information, both charts are running on different magic number (EURUSD running on default 8080, USDJPY running on 8081). thanks. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#227](/thread/post/8130323#post8130323 "Post Permalink")

  * Edited 2:21pm  Mar 12, 2015 1:54pm | Edited 2:21pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting happytrade38](/thread/post/8130223#post8130223 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi radityo.ardi, Something to add. Yes, guess USDJPY with 3 digits have the issue. However, the EURUSD with 5 digits shouldn't be an issue, as per the last screenshot, the pips is 423 and yet to be closed. For information, both charts are running on different magic number (EURUSD running on default 8080, USDJPY running on 8081). thanks.
> 
> Ignored

Apparently I don't see any issue / bug in my testings a few minutes back.  
I want you to closely monitor the dashboard value, especially on "First Points" value.  
Your screenshot is also calculated correctly.  
42 points = 121.583 - 121.541  
It won't close until "First Points" >= TP or <= (SL * -1)  
  
So your order will close at 121.941 (TP) or 121.441 (SL), based on your settings TP = 400 and SL=100.  
Apparently I just identified a small bug, that if you set Enable Max Loss to false, it'll keep calculating the SL. I have fixed it, but haven't release it.  
  
Thanks for reporting the issues... that is very valuable for this EA.  
  
If you want to be fixed, please wait for the new v1.09 ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)  
  
  
UPDATE:  
another issue when updating EA's ex4 file in Support and Resistance, the condition not supposed to create new order after updating. But it was created. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#228](/thread/post/8130467#post8130467 "Post Permalink")

  * Mar 12, 2015 4:02pm  Mar 12, 2015 4:02pm 

  * [ happytrade38](happytrade38)

  * | Joined Sep 2014  | Status: Trader | [517 Posts](/search?do=process&provider=Member&searchuser=382480)

> [Quoting radityo.ardi](/thread/post/8130323#post8130323 "View Quoted Post")
> 
> Disliked
> 
> {quote} Apparently I don't see any issue / bug in my testings a few minutes back. I want you to closely monitor the dashboard value, especially on "First Points" value. Your screenshot is also calculated correctly. 42 points = 121.583 - 121.541 It won't close until "First Points" >= TP or <= (SL * -1) So your order will close at 121.941 (TP) or 121.441 (SL), based on your settings TP = 400 and SL=100. Apparently I just identified a small bug, that if you set Enable Max Loss to false, it'll keep calculating the SL. I have fixed it, but haven't release...
> 
> Ignored

  
Thanks for the update. Yes, will wait for the v1.09. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#229](/thread/post/8130554#post8130554 "Post Permalink")

  * Mar 12, 2015 4:30pm  Mar 12, 2015 4:30pm 

  * [ Ksth](ksth)

  * | Joined Jun 2012  | Status: Trader | [960 Posts](/search?do=process&provider=Member&searchuser=262880)

hi [_radityo.ardi_ ](http://www.forexfactory.com/radityo.ardi)   
is it possible to set 0.01 ? i did try it but EA buy @ 0.10 instead of 0.01 . 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#230](/thread/post/8130572#post8130572 "Post Permalink")

  * Mar 12, 2015 4:34pm  Mar 12, 2015 4:34pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting Ksth](/thread/post/8130554#post8130554 "View Quoted Post")
> 
> Disliked
> 
> hi [radityo.ardi ](http://www.forexfactory.com/radityo.ardi) is it possible to set 0.01 ? i did try it but EA buy @ 0.10 instead of 0.01 .
> 
> Ignored

Make sure your Starting Lots set to Fixed, and set to 0.01.  
Some cases, a broker may limit the lowest lot as 0.1, in this case, you have no choice to set 0.1. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#231](/thread/post/8131183#post8131183 "Post Permalink")

  * Mar 12, 2015 7:21pm  Mar 12, 2015 7:21pm 

  * [ happytrade38](happytrade38)

  * | Joined Sep 2014  | Status: Trader | [517 Posts](/search?do=process&provider=Member&searchuser=382480)

> [Quoting radityo.ardi](/thread/post/8104903#post8104903 "View Quoted Post")
> 
> Disliked
> 
> A few notes during the weekend: It seems that still there was a bug in Support and Resistance and Daily High and Low scenario with fixed number of max cycle ( > 0). The bug will happen if you intend to run the EA 24/7 in VPS. But if you run ocassionally, it won't happen. My observation on Martingale with Less Risk: Martingale with 1, 2, 2, 2, 2, 2... series didn't close a cycle properly. It was simply because of the more martingale index, the target price will be more wide. So what happened is that martingale reaches somewhere in index of 40+,...
> 
> Ignored

Hi radityo.ardi,I am quite surprise if the index reach 30 or 40. in normal martingale, the account already burst. Just want to understand further of yhr index, for example, the order close follow 1,2,2,2 consider as close in index of 4? Mind to share the TP of the martinagle less risk? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#232](/thread/post/8131358#post8131358 "Post Permalink")

  * Mar 12, 2015 8:17pm  Mar 12, 2015 8:17pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting happytrade38](/thread/post/8131183#post8131183 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi radityo.ardi,I am quite surprise if the index reach 30 or 40. in normal martingale, the account already burst. Just want to understand further of yhr index, for example, the order close follow 1,2,2,2 consider as close in index of 4? Mind to share the TP of the martinagle less risk?
> 
> Ignored

I always use the Money-based profit, never uses the points based. Because with points-based, your zero profit (break-even) price will move further even if you use 1, 2, 4. I think to make the break-even price stays there, you have to use 2.9 multiplier (I think) instead of 2. With multiplier 2 (1, 2, 4, 8...) it already too much risk put on the table, so I'm avoiding that.  
  
Right now the Less Risk is somewhat "okay", but you can see how much profit I got for 16 days (in percent). Still acceptable for me. Yes, index will be much longer than normal, but fair enough.  
  
Another interesting thing is the Martingale SNR (Support and Resistance), giving me a good profit as of now.  
  
Please bear in mind, that martingale series alone is not the only contributor to the length of the martingale index (order count), but also Gaps is playing an important role here.  
So, if the gaps says only 30 points, you are risking your EA (failing to open order or close all order) and also your strategy (you will get stuck into a lengthy cycle, you will put your account into a big risk as too many orders are created).  
  
So,  
My personal advice is:  
With $5K, starting lot Fixed at 0.1, Take profit (money based) at $40, martingale factor to "1" only (instead of "1, 2, 4"), Operation to Multiply, Modifier 1.5 (instead of standard 2), 100 points (or 10 pips) Gaps, max 3 cycles per day. I think is the best one and perfect. Additionally, you can set Trailing target to $10, which means it will drag your TP if $50 ($40 + $10) or more is reached. If the price moving more and your unrealized profit to $70, it will close the cycle if then the profit goes lower than $60, so on and so forth.  
  
For starting with $1K, then starting lot can be at 0.02 with TP at $8, or $500 then starting lot can be at 0.01 with TP at $4.  
  
If you guys have a better settings, I hope you can share it as well. 

Attached File(s)

![File Type: txt](https://assets.faireconomy.media/images/attach/txt.gif) [ANYTIMELESSRISK.set.txt](/attachment/file/1630005?d=1426159004) 1 KB | 418 downloads 

![File Type: txt](https://assets.faireconomy.media/images/attach/txt.gif) [SNREURUSD.set.txt](/attachment/file/1630006?d=1426159009) 1 KB | 356 downloads 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#233](/thread/post/8132268#post8132268 "Post Permalink")

  * Mar 13, 2015 12:27am  Mar 13, 2015 12:27am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

HA!!!  
Martingale AnyTime reaches 90% in 38 days  
Martingale SNR reaches 40% in 42 days  
  
Good result so far... 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#234](/thread/post/8134937#post8134937 "Post Permalink")

  * Mar 13, 2015 10:03pm  Mar 13, 2015 10:03pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

Hi All,  
I've released new version, v1.09.  
  
Below are the new features and fixes list:

  1. Cycle Count is not properly reset when re-attach again the same Support and Resistance. So EA thinks that still valid to create new order, although invalid.
  2. Draggable dashboard texts (by double clicking it).![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)
  3. Activating Trailing Targets and Dynamic Trailing Targets.
  4. Fixes for Trailing Target scenario.
  5. Slippage setting when Open order and Close order.
  6. Factor Operator (since v1.08), configurable between "Add" or "Multiply".
  7. Change Max Loss and Max Loss Multiplier to negative number. Value must be 0 or less. WARNING: there's no validation if you put positive numbers.![](https://resources.faireconomy.media/images/emojis/64/1f44e.png?v=15.1)
  8. Change Stop Loss to negative number. Value must be 0 or less. WARNING: there's no validation if you put positive numbers.
  9. Fixes for Enable Max Loss for Points based.
  10. Order Direction (since v1.07), applies for "High and Low" and "Support and Resistance". "Same direction" means if "Low" or "Resistance" is touched, then SELL order will be opened first. "Opposite direction", will do BUY order first.
  11. Fixes for removing index number from Comments. Now index is merged with MagicNumber. MagicNumber now set as the following format: [MagicNumber][4digitindex]. For example: 80800000 (for index 0), 80800001 (for index 1), 80800002 (for index 2), etc.
  12. Fixes for reset time and cycle reset.

I hope you guys all blessed with this EA update.  
I think SNR settings is the best settings I can get, with Multiplier 1.5. So, I set that as the default settings. Remember that the settings is based on $5K starting amount, and already set to Dynamic Lots, Dynamic Target Profit, and Dynamic Trailing Target. The minimum you can start (with 0.01) is around $500, with 10 pips (100 points) gaps. Still you don't need to worry with the settings, since set to dynamic against balance.  
  
I'm gonna test it out again for another month, then you know what will happen next if the result remains positive.  
  
**_But now, still I urge you to do it on DEMO first (at least 1 month) if_** :

  1. You just read this text, and knew this EA 10 minutes ago.
  2. Previously was in a good profit for 6 months more in live account, but now decided to move to another broker.
  3. Changing important settings (Gaps, profit, martingale numbers, factors, max martingale, etc).

Don't assume one is good, then you apply directly to live account without verifying with Demo account.  
Once it is good and acceptable, then you can start using live account, and then watch Jurassic World after that. Don't forget to RUN! ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)  
  
Have a nice weekend, GUYS! 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#235](/thread/post/8135922#post8135922 "Post Permalink")

  * Mar 14, 2015 1:45am  Mar 14, 2015 1:45am 

  * [ aahmad29](aahmad29)

  * Joined Aug 2012 | Status: Love for all; Hatred for none | [3,557 Posts](/search?do=process&provider=Member&searchuser=286894)

> [Quoting radityo.ardi](/thread/post/8134937#post8134937 "View Quoted Post")
> 
> Disliked
> 
> Hi All, I've released new version, v1.09. Below are the new features and fixes list: Cycle Count is not properly reset when re-attach again the same Support and Resistance. So EA thinks that still valid to create new order, although invalid. Draggable dashboard texts (by double clicking it).![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1) Activating Trailing Targets and Dynamic Trailing Targets. Fixes for Trailing Target scenario. Slippage setting when Open order and Close order. Factor Operator (since v1.08), configurable between "Add" or "Multiply". Change Max Loss and Max Loss Multiplier...
> 
> Ignored

![](https://resources.faireconomy.media/images/emojis/64/1f44f.png?v=15.1)

Love for all; Hatred for none.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#236](/thread/post/8137097#post8137097 "Post Permalink")

  * Mar 14, 2015 11:08pm  Mar 14, 2015 11:08pm 

  * [ Reamasesa](reamasesa)

  * Joined Jan 2015 | Status: Trader | [916 Posts](/search?do=process&provider=Member&searchuser=397375)

Thanks! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#237](/thread/post/8137258#post8137258 "Post Permalink")

  * Mar 15, 2015 2:18am  Mar 15, 2015 2:18am 

  * [ Reamasesa](reamasesa)

  * Joined Jan 2015 | Status: Trader | [916 Posts](/search?do=process&provider=Member&searchuser=397375)

Weird,  
I'm using Fixed Lots and it doesn't use the 0.01 fixed lot number I've put in settings, always 0.05  
Any ideas?  
  
  
  
Thanks 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#238](/thread/post/8138830#post8138830 "Post Permalink")

  * Mar 16, 2015 12:19pm  Mar 16, 2015 12:19pm 

  * [ happytrade38](happytrade38)

  * | Joined Sep 2014  | Status: Trader | [517 Posts](/search?do=process&provider=Member&searchuser=382480)

> [Quoting radityo.ardi](/thread/post/8134937#post8134937 "View Quoted Post")
> 
> Disliked
> 
> Hi All, I've released new version, v1.09. Below are the new features and fixes list: Cycle Count is not properly reset when re-attach again the same Support and Resistance. So EA thinks that still valid to create new order, although invalid. Draggable dashboard texts (by double clicking it).![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1) Activating Trailing Targets and Dynamic Trailing Targets. Fixes for Trailing Target scenario. Slippage setting when Open order and Close order. Factor Operator (since v1.08), configurable between "Add" or "Multiply". Change Max Loss and Max Loss Multiplier...
> 
> Ignored

Thanks, will try it. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#239](/thread/post/8138912#post8138912 "Post Permalink")

  * Mar 16, 2015 1:45pm  Mar 16, 2015 1:45pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting Reamasesa](/thread/post/8137258#post8137258 "View Quoted Post")
> 
> Disliked
> 
> Weird, I'm using Fixed Lots and it doesn't use the 0.01 fixed lot number I've put in settings, always 0.05 Any ideas? Thanks
> 
> Ignored

How much is your starting balance?  

> [Quoting radityo.ardi](/thread/post/8134937#post8134937 "View Quoted Post")
> 
> Disliked
> 
> Remember that the settings is based on $5K starting amount, and already set to Dynamic Lots, Dynamic Target Profit, and Dynamic Trailing Target. The minimum you can start (with 0.01) is around $500, with 10 pips (100 points) gaps. Still you don't need to worry with the settings, since set to dynamic against balance.
> 
> Ignored

Let me get it straight, I think I said it wrong.  
The minimum you can start (with 0.01) is around $250, with the same 10 pips.  
If you start with $250, and the Dynamic Lots set to 0.00005, then it will produce 0.01 lot (from $250 x 0.00005 = 0.0125 or 0.01, correct me if I'm wrong).  
  
As I said many times, please start with DEMO account first. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#240](/thread/post/8138961#post8138961 "Post Permalink")

  * Mar 16, 2015 2:46pm  Mar 16, 2015 2:46pm 

  * [ happytrade38](happytrade38)

  * | Joined Sep 2014  | Status: Trader | [517 Posts](/search?do=process&provider=Member&searchuser=382480)

> [Quoting radityo.ardi](/thread/post/8131358#post8131358 "View Quoted Post")
> 
> Disliked
> 
> {quote} I always use the Money-based profit, never uses the points based. Because with points-based, your zero profit (break-even) price will move further even if you use 1, 2, 4. I think to make the break-even price stays there, you have to use 2.9 multiplier (I think) instead of 2. With multiplier 2 (1, 2, 4, 8...) it already too much risk put on the table, so I'm avoiding that. Right now the Less Risk is somewhat "okay", but you can see how much profit I got for 16 days (in percent). Still acceptable for me. Yes, index will be much longer than...
> 
> Ignored

Hi Radityo.ardi,  
Your account is standard account? so when you mentioned take profit at $40, meaning is 4pip for 1 standard lot? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Trapping System: Tunnel Martingale
  *   * [ **Reply to Thread** ](/thread/524198-trapping-system-tunnel-martingale/reply#reply)

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

[Martingale, Anti-martingale, and Compounding](/thread/571233-martingale-anti-martingale-and-compounding "Hi all traders, 
i started this thread to meet others people interested in money management. 
We all know that martingale strategies are...") 40 replies

[Martingale, Reverse Martingale, Modified Martingale, Maths](/thread/736165-martingale-reverse-martingale-modified-martingale-maths "Hi all, so Martingale has been a risky yet maybe non profitable system. While roulette has an edge of \(2.7%/5.4%\) 
  
Inspired by Adam...") 1 reply

[How to change this Martingale to Reverse Martingale ?](/thread/546755-how-to-change-this-martingale-to-reverse-martingale "How to change this Martingale to Reverse Martingale ?") 3 replies

[Trapping System: Way to Fully-Automated Trading System](/thread/509226-trapping-system-way-to-fully-automated-trading-system "Hi fellow Traders! 
This is my first time to write a new thread. Would like to share a trading method, which at least made me happy right...") 47 replies

[Martingale vs. Non Martingale (Simplified RoR vs Profit)](/thread/526308-martingale-vs-non-martingale-simplified-ror-vs-profit "Martingale: The gambler doubles his bet after every loss... 
  
Martingale vs. Non Martingale \(Simplified RoR vs Profit in 3 trade runs...") 1 reply

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/524198-trapping-system-tunnel-martingale/reply#reply)
  * Subscribe
  * [221](javascript:void\(0\);)

Attachments: Trapping System: Tunnel Martingale

Tags: Trapping System: Tunnel Martingale

#  [](/thread/524198-trapping-system-tunnel-martingale)Trapping System: Tunnel Martingale 

  * 

  * [#241](/thread/post/8138976#post8138976 "Post Permalink")

  * Mar 16, 2015 3:02pm  Mar 16, 2015 3:02pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting happytrade38](/thread/post/8138961#post8138961 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi Radityo.ardi, Your account is standard account? so when you mentioned take profit at $40, meaning is 4pip for 1 standard lot?
> 
> Ignored

I'm using [Tickmill](/brokers/tickmill "View Tickmill Broker Profile") with Exchange account type. I never done any measurement. But if starting from $5K, expectation is $40 for 0.25 initial lots. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#242](/thread/post/8139145#post8139145 "Post Permalink")

  * Mar 16, 2015 4:48pm  Mar 16, 2015 4:48pm 

  * [ slianto](slianto)

  * | Joined Feb 2015  | Status: Trader | [180 Posts](/search?do=process&provider=Member&searchuser=399331)

hi radityo,  
i would like to know the setting in your 1st page if you dont mind, (sorry im a newbie)  
  
1\. the setting file ([Martingale Anytime EURUSD.set.txt](http://www.forexfactory.com/attachment.php?attachmentid=1610492&d=1423804968)) uses broker 4digits or 5digits?and what value that i need to change if it doesnt suit my broker (mine use 4digits).  
2\. about gaps, it is the differential points/pips between last closed candle and newly opened candle right?and how many point/pip do u suggest?  
3\. this works on which time frame?  
  
thank you. radityo. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#243](/thread/post/8139324#post8139324 "Post Permalink")

  * Mar 16, 2015 5:55pm  Mar 16, 2015 5:55pm 

  * [ leebsurag](leebsurag)

  * | Membership Revoked  | Joined Oct 2013 | [877 Posts](/search?do=process&provider=Member&searchuser=353350)

> [Quoting radityo.ardi](/thread/post/8138976#post8138976 "View Quoted Post")
> 
> Disliked
> 
> {quote} I'm using Tickmill with Exchange account type. I never done any measurement. But if starting from $5K, expectation is $40 for 0.25 initial lots.
> 
> Ignored

  
What is your trading time (sessions)? Any positive/negative slippage you get with them? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#244](/thread/post/8139357#post8139357 "Post Permalink")

  * Mar 16, 2015 6:11pm  Mar 16, 2015 6:11pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting slianto](/thread/post/8139145#post8139145 "View Quoted Post")
> 
> Disliked
> 
> hi radityo, i would like to know the setting in your 1st page if you dont mind, (sorry im a newbie) 1. the setting file ([Martingale Anytime EURUSD.set.txt](http://www.forexfactory.com/attachment.php?attachmentid=1610492&d=1423804968)) uses broker 4digits or 5digits?and what value that i need to change if it doesnt suit my broker (mine use 4digits). 2. about gaps, it is the differential points/pips between last closed candle and newly opened candle right?and how many point/pip do u suggest? 3. this works on which time frame? thank you....
> 
> Ignored

My suggestion is to take profit based on "money" rather than "points" (or pips). I've coded for that as well.  
The settings is applied for tickmill, 5 digits.  
No, gaps is the tunnel ceiling and floor distance (in points). Gaps, I suggest around 10 pips.  
As I never coded for specific timeframe, so no timeframe specific feature. It works on all.  
  

> [Quoting leebsurag](/thread/post/8139324#post8139324 "View Quoted Post")
> 
> Disliked
> 
> {quote} What is your trading time (sessions)? Any positive/negative slippage you get with them?
> 
> Ignored

Slippage, yes sometimes it does happen. I never set it anyway, that's why my trades, sometimes threw errors when it comes into high volatility times.  
Time to trade, I suggest 2 - 4 hours before US time and stop at 4 hours after US time for EUR/USD. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#245](/thread/post/8139392#post8139392 "Post Permalink")

  * Mar 16, 2015 6:30pm  Mar 16, 2015 6:30pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

![](https://resources.faireconomy.media/images/emojis/64/1f62b.png?v=15.1)found 1 bug again. Cycle Count not reset to zero, apparently it seems only happened on Monday morning SGT. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#246](/thread/post/8139470#post8139470 "Post Permalink")

  * Mar 16, 2015 7:03pm  Mar 16, 2015 7:03pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar360850_1.gif) Clipi](clipi)

  * | Joined Jan 2014  | Status: Trader | [482 Posts](/search?do=process&provider=Member&searchuser=360850)

good morning, I was testing your EA, appears a problem with the SL. I have 5 digit broker.  
GAP: 3  
SL: 100  
TP: 20  
to such a small gap can sometimes an order to buy or sell skips.  
thank you very much. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: MetaTrader 4 IC Markets.png
Size: 104 KB](/attachment/image/1632600/thumbnail?d=1426500022)](/attachment/image/1632600?d=1426500022)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#247](/thread/post/8139766#post8139766 "Post Permalink")

  * Edited Mar 17, 2015 9:22am  Mar 16, 2015 8:56pm | Edited Mar 17, 2015 9:22am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting Clipi](/thread/post/8139470#post8139470 "View Quoted Post")
> 
> Disliked
> 
> good morning, I was testing your EA, appears a problem with the SL. I have 5 digit broker. GAP: 3 SL: 100 TP: 20 to such a small gap can sometimes an order to buy or sell skips. thank you very much. {image}
> 
> Ignored

Gap = 3 means 0.3 pips, note that yours is 5 digits.  
Are you sure with that setting? Definitely it will throw errors. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#248](/thread/post/8140754#post8140754 "Post Permalink")

  * Mar 17, 2015 3:03am  Mar 17, 2015 3:03am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar403827_1.gif) Jl29](jl29)

  * | Commercial User  | Joined Mar 2015 | [20 Posts](/search?do=process&provider=Member&searchuser=403827)

rad,  
  
How can I change the Profit Target when I have it set with "fixed money" as the Target Price?  
  
I am trying to test different target prices.   
  
Right now, I am not sure how to change it from the default 10pip TP when using Fixed Money as my Target Price on the EA.  
  
Thanks,  
  
  
Jl29 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#249](/thread/post/8141020#post8141020 "Post Permalink")

  * Mar 17, 2015 4:59am  Mar 17, 2015 4:59am 

  * [ Hossein1](hossein1)

  * | Joined Sep 2011  | Status: Trader | [10 Posts](/search?do=process&provider=Member&searchuser=195709)

Hi  
Why can not I see the videos contained in the topic?  
Please help me 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#250](/thread/post/8141307#post8141307 "Post Permalink")

  * Mar 17, 2015 9:32am  Mar 17, 2015 9:32am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting Jl29](/thread/post/8140754#post8140754 "View Quoted Post")
> 
> Disliked
> 
> rad, How can I change the Profit Target when I have it set with "fixed money" as the Target Price? I am trying to test different target prices. Right now, I am not sure how to change it from the default 10pip TP when using Fixed Money as my Target Price on the EA. Thanks, Jl29
> 
> Ignored

Try calculate with excel file I"ve provided here:  
[http://www.forexfactory.com/showthre...37#post8067337](http://www.forexfactory.com/showthread.php?p=8067337#post8067337)  
You can do any kind of simulation there.  
  

> [Quoting Hossein1](/thread/post/8141020#post8141020 "View Quoted Post")
> 
> Disliked
> 
> Hi Why can not I see the videos contained in the topic? Please help me
> 
> Ignored

Your network maybe blocking it. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#251](/thread/post/8142389#post8142389 "Post Permalink")

  * Mar 17, 2015 7:50pm  Mar 17, 2015 7:50pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

Guys,  
Below is the proof that _not only Martingale series that can cause you a loss, but also the gap settings_.  
My Martingale Less Risk finally fell down touching the Stop Out 30% after margin call many times.  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot1.png
Size: 95 KB](/attachment/image/1633422/thumbnail?d=1426587756)](/attachment/image/1633422?d=1426587756)   

  
  
That Martingale uses gap 30 points, with "Multiply" modifier 1.5.  
Surprisingly,  
Martingale Support and Resistance with modifier 1.5 Gaps 100 points,  
Martingale Normal AnyTime with modifier 2.0 Gaps 30 points,  
and High Low with modifier 1.5 gaps 100 points,  
  
all still surviving.  

Attached Image

![](/attachment/image/1633446?d=1426588962)

  
  
And another one, private Martingale Anytime, modifier 1.5 Gaps 100 points,  

Attached Image

![](/attachment/image/1633448?d=1426589075)

  
  
  
In short (the conclusions):  
Whenever you change any of the important settings (Multiply, Modifier, Gaps, Martingale series, target, stop loss, etc), do a test first before running on live. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#252](/thread/post/8146211#post8146211 "Post Permalink")

  * Edited 7:19am  Mar 19, 2015 12:41am | Edited 7:19am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar403827_1.gif) Jl29](jl29)

  * | Commercial User  | Joined Mar 2015 | [20 Posts](/search?do=process&provider=Member&searchuser=403827)

Rad,  
  
I am in love with this type of trading!  
  
Tons of trades each day with small profits but I just can not seem to get the kind of results that you are showing in your Martingale Anytime Explorer.  
  
I want the EA to perform just like it does for you...200ish trades on busy days. As of now, I am getting way too many errors. I am running [FXPro](/brokers/fxpro "View FxPro Broker Profile").  
  
See attached...  
  
It's hedging. I have open buy and sell positions. Not sure how to fix this.  
  
My settings:  
Gap:30points and 2.0 modifier  
  
Thanks in advance,  
  
Jl29 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: error2.5.5.png
Size: 350 KB](/attachment/image/1635019/thumbnail?d=1426717156)](/attachment/image/1635019?d=1426717156)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#253](/thread/post/8148532#post8148532 "Post Permalink")

  * Mar 19, 2015 2:36pm  Mar 19, 2015 2:36pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting Jl29](/thread/post/8146211#post8146211 "View Quoted Post")
> 
> Disliked
> 
> Rad, I am in love with this type of trading! Tons of trades each day with small profits but I just can not seem to get the kind of results that you are showing in your Martingale Anytime Explorer. I want the EA to perform just like it does for you...200ish trades on busy days. As of now, I am getting way too many errors. I am running FXPro. See attached... It's hedging. I have open buy and sell positions. Not sure how to fix this. My settings: Gap:30points and 2.0 modifier Thanks in advance, Jl29 {image}
> 
> Ignored

Whow....  
You have 5 digits with 15 points spread. To me, 30 points gap is too optimistic, furthermore, it is considered too low.  
Yes, your [spreads](/brokers/spreads "View Live Spreads on the Broker Guide") is 15 points, compared to 30 points gap, but at high volatility times, the spread could expand higher, and EA couldn't work properly.  
  
Probably you may want to set your gap higher to 50 points. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#254](/thread/post/8149939#post8149939 "Post Permalink")

  * Edited Mar 20, 2015 12:42am  Mar 19, 2015 11:13pm | Edited Mar 20, 2015 12:42am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar403827_1.gif) Jl29](jl29)

  * | Commercial User  | Joined Mar 2015 | [20 Posts](/search?do=process&provider=Member&searchuser=403827)

> [Quoting radityo.ardi](/thread/post/8148532#post8148532 "View Quoted Post")
> 
> Disliked
> 
> {quote} Whow.... You have 5 digits with 15 points spread. To me, 30 points gap is too optimistic, furthermore, it is considered too low. Yes, your spreads is 15 points, compared to 30 points gap, but at high volatility times, the spread could expand higher, and EA couldn't work properly. Probably you may want to set your gap higher to 50 points.
> 
> Ignored

radityo.ardi,  
  
I will change gap to 50 points but will that stop both Long and Short positions to open at the same time (it hedges instead of exiting).  
  
What spread do you have on tickmill?  
-just checked out their site...impressive spreads. 0.4 on eur/usd  
  
thanks,  
  
Jl29 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#255](/thread/post/8150236#post8150236 "Post Permalink")

  * Mar 20, 2015 12:35am  Mar 20, 2015 12:35am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting Jl29](/thread/post/8149939#post8149939 "View Quoted Post")
> 
> Disliked
> 
> {quote} radityo.ardi, I will change gap to 50 points but will that stop both Long and Short positions to open at the same time (it hedges instead of exiting). What spread do you have on tickmill? thanks, Jl29
> 
> Ignored

When you change a setting, it will ask you whether to close all orders for the current cycle. Select Yes, then it will close all.  
I think 1 key point here is,  
When you want to change any settings, better do it when no order opened. If still there's order, you better wait until freeze time (out of start & stop time, for start type Anytime). Do this practice when even you are on demo, so you'll get the feel how this ea works, and on top of that will also safe your account from unecessary opening orders.  
Same when you (later) doing on live account, changing settings would need some test at least 1 or 2 months. We must be very discipline as this strategy having big risk.  
  
My tickmill having 0.2 pips spread with comissions. That's why I can set gaps to 30 pips. For you, the minimum is 60 actually. But just try it first on demo.  
I'm planning to activate AGEA demo with this EA tomorrow, since it has the same spreads like you (even a bit higher, @1.6 pips). Probably with small starting balance of 100 or 200 USD and see how it goes. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#256](/thread/post/8151033#post8151033 "Post Permalink")

  * Edited 8:02am  Mar 20, 2015 7:30am | Edited 8:02am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar403827_1.gif) Jl29](jl29)

  * | Commercial User  | Joined Mar 2015 | [20 Posts](/search?do=process&provider=Member&searchuser=403827)

Rad,  
  
Maybe this was somewhere in the thread and i missed it but...  
  
I noticed that you only trade the EU...why? is it bc of how volatile it has been combined with low spreads?  
  
The reason i ask is bc i was wondering why you wouldn't trade all pairs when red news is coming out.  
  
Say get in after 3 minutes of news release.  
  
Also, have you thought about entering first trade when stoch is at o/s or o/b on the 1M chart? Seems like that will boost the edge.   
...just a thought.  
  
Thanks again,  
  
Jl29 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#257](/thread/post/8151088#post8151088 "Post Permalink")

  * Mar 20, 2015 8:07am  Mar 20, 2015 8:07am 

  * [ sorin24](sorin24)

  * | Joined Feb 2013  | Status: Trader | [16 Posts](/search?do=process&provider=Member&searchuser=325266)

I think it's quite dangerous to trade even after 3 min... depending on broker the spread can go to 10 pips...yesterday it went from my usual 0.2 pips plus commission to 15 pips...it can give you plenty of errors and you can remain with the biggest position open on the wrong side...  
And Rad, if you want to try on live account with only 100-200 deposit I thing it's also dangerous...the margin levels will be hit and you will loose your account. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#258](/thread/post/8151291#post8151291 "Post Permalink")

  * Mar 20, 2015 11:25am  Mar 20, 2015 11:25am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting Jl29](/thread/post/8151033#post8151033 "View Quoted Post")
> 
> Disliked
> 
> Rad, Maybe this was somewhere in the thread and i missed it but... I noticed that you only trade the EU...why? is it bc of how volatile it has been combined with low spreads? The reason i ask is bc i was wondering why you wouldn't trade all pairs when red news is coming out. Say get in after 3 minutes of news release. Also, have you thought about entering first trade when stoch is at o/s or o/b on the 1M chart? Seems like that will boost the edge. ...just a thought. Thanks again, Jl29
> 
> Ignored

I tell you what.  
It doesn't matter to me whether EU or any pairs. I was testing USDJPY or AUDUSD sometime back, at 08:00 - 12:00 timeframe, but it was bad. Caught up with index 12 many times. But I observed, both will have a high volatility (which I'm expecting) on around US opening time. So this time I just play with EURUSD.  
Well, I want to keep my EA simple actually. Couple of people PM'd me to add some logic like some kind of chart at some timeframe, or based on fibo something... I said sorry to them, I can't do that. The settings now is already complicated, makes people cry. ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)  
  
3 mins after news is fine actually, well, at least to me. As long as you plan it out properly, such as gaps, lots, martingale series, etc.  
Why I said so? Bc news time is just news time. No actual relation with the chart, although news impacting the chart. Sometimes 8pm news (my time SGT), but market moves at 8:30pm, sometimes moves before news like 7:30 then 8pm is like freezing then move again at 9pm.  
  

> [Quoting sorin24](/thread/post/8151088#post8151088 "View Quoted Post")
> 
> Disliked
> 
> I think it's quite dangerous to trade even after 3 min... depending on broker the spread can go to 10 pips...yesterday it went from my usual 0.2 pips plus commission to 15 pips...it can give you plenty of errors and you can remain with the biggest position open on the wrong side... And Rad, if you want to try on live account with only 100-200 deposit I thing it's also dangerous...the margin levels will be hit and you will loose your account.
> 
> Ignored

Don't worry, bro. Let it be blown or die, since it is only demo.  
Sticking to the key points, never ever trade on live without testing it in demo for at least 1-2 months.  
  
I hope you guys following me. I haven't trade any live acc with this EA yet.  
I will tell you when is the time... 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#259](/thread/post/8151509#post8151509 "Post Permalink")

  * Mar 20, 2015 3:17pm  Mar 20, 2015 3:17pm 

  * [ leebsurag](leebsurag)

  * | Membership Revoked  | Joined Oct 2013 | [877 Posts](/search?do=process&provider=Member&searchuser=353350)

> [Quoting radityo.ardi](/thread/post/8150236#post8150236 "View Quoted Post")
> 
> Disliked
> 
> My tickmill having 0.2 pips spread with comissions. That's why I can set gaps to 30 pips. For you, the minimum is 60 actually. But just try it first on demo.
> 
> Ignored

How often you get such tight spreads on your orders? Only in flat market or it's in trending, slightly volatile one? What about spread widening, how often it occurs? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#260](/thread/post/8151569#post8151569 "Post Permalink")

  * Mar 20, 2015 4:14pm  Mar 20, 2015 4:14pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting leebsurag](/thread/post/8151509#post8151509 "View Quoted Post")
> 
> Disliked
> 
> {quote} How often you get such tight spreads on your orders? Only in flat market or it's in trending, slightly volatile one? What about spread widening, how often it occurs?
> 
> Ignored

Quite often.  
I would say "trending" can happen even on normal hours like now.  
  
But spread widening can occurs most of the time after a huge news released. You may notice I've posted some post saying that the cycle got stucked. That's when it happened, could be because of spread is high/wide at that time but could also because of the price moves and retract back before EA could finish open STOP order, so STOP order wasn't properly placed.  
How often, not too often, I got already 3 - 4 times in 45+ days running the EA, the same situation where STOP order can't be placed, and stuck. But I was never tried to alter the EA to work. I kept it running.  
  
When market is flat (or sleeping time, I would say), all orders executed properly, although I got my max martingale index touched many times due to the market is flat. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Trapping System: Tunnel Martingale
  *   * [ **Reply to Thread** ](/thread/524198-trapping-system-tunnel-martingale/reply#reply)

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

[Martingale, Anti-martingale, and Compounding](/thread/571233-martingale-anti-martingale-and-compounding "Hi all traders, 
i started this thread to meet others people interested in money management. 
We all know that martingale strategies are...") 40 replies

[Martingale, Reverse Martingale, Modified Martingale, Maths](/thread/736165-martingale-reverse-martingale-modified-martingale-maths "Hi all, so Martingale has been a risky yet maybe non profitable system. While roulette has an edge of \(2.7%/5.4%\) 
  
Inspired by Adam...") 1 reply

[How to change this Martingale to Reverse Martingale ?](/thread/546755-how-to-change-this-martingale-to-reverse-martingale "How to change this Martingale to Reverse Martingale ?") 3 replies

[Trapping System: Way to Fully-Automated Trading System](/thread/509226-trapping-system-way-to-fully-automated-trading-system "Hi fellow Traders! 
This is my first time to write a new thread. Would like to share a trading method, which at least made me happy right...") 47 replies

[Martingale vs. Non Martingale (Simplified RoR vs Profit)](/thread/526308-martingale-vs-non-martingale-simplified-ror-vs-profit "Martingale: The gambler doubles his bet after every loss... 
  
Martingale vs. Non Martingale \(Simplified RoR vs Profit in 3 trade runs...") 1 reply

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/524198-trapping-system-tunnel-martingale/reply#reply)
  * Subscribe
  * [221](javascript:void\(0\);)

Attachments: Trapping System: Tunnel Martingale

Tags: Trapping System: Tunnel Martingale

#  [](/thread/524198-trapping-system-tunnel-martingale)Trapping System: Tunnel Martingale 

  * 

  * [#261](/thread/post/8155020#post8155020 "Post Permalink")

  * Mar 22, 2015 9:29am  Mar 22, 2015 9:29am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar135523_1.gif) blamshakk](blamshakk)

  * Joined Mar 2010 | Status: Trader | [2,240 Posts](/search?do=process&provider=Member&searchuser=135523)

hey radityo ardi  
  
many thanks for sharing this system. can i ask what timeframe your martingaleanytime demo is?  
  
thanks 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#262](/thread/post/8155074#post8155074 "Post Permalink")

  * Mar 22, 2015 12:09pm  Mar 22, 2015 12:09pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting blamshakk](/thread/post/8155020#post8155020 "View Quoted Post")
> 
> Disliked
> 
> hey radityo ardi many thanks for sharing this system. can i ask what timeframe your martingaleanytime demo is? thanks
> 
> Ignored

No timeframe related. Any timeframe will do. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#263](/thread/post/8155143#post8155143 "Post Permalink")

  * Mar 22, 2015 3:47pm  Mar 22, 2015 3:47pm 

  * [ moncsicsi78](moncsicsi78)

  * | Joined Sep 2011  | Status: Trader | [160 Posts](/search?do=process&provider=Member&searchuser=196773)

Hi radityo.ardi,  
didn't you think to build in the EA pyramid function with trailing stop and "2sides" function? It would be interesting, and woud make more profit, I think. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#264](/thread/post/8155354#post8155354 "Post Permalink")

  * Mar 22, 2015 10:07pm  Mar 22, 2015 10:07pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar356628_2.gif) LITEchild](litechild)

  * Joined Nov 2013 | Status: Member of the 5% club | [1,259 Posts](/search?do=process&provider=Member&searchuser=356628)

Hello Rad. Been studying your work. Looks like a job very well done. Im curious if these features you mentioned at the beginning have been implemented yet? 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: TRAPPING SYSTEM.png
Size: 15 KB](/attachment/image/1637414/thumbnail?d=1427029635)](/attachment/image/1637414?d=1427029635)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#265](/thread/post/8155559#post8155559 "Post Permalink")

  * Mar 23, 2015 3:04am  Mar 23, 2015 3:04am 

  * [ aahmad29](aahmad29)

  * Joined Aug 2012 | Status: Love for all; Hatred for none | [3,557 Posts](/search?do=process&provider=Member&searchuser=286894)

> [Quoting radityo.ardi](/thread/post/8155074#post8155074 "View Quoted Post")
> 
> Disliked
> 
> {quote} No timeframe related. Any timeframe will do.
> 
> Ignored

  
Hi radityo.ardi  
  
I am going to start testing with little different settings and I am going to do manual trading. If you give permission I will keep posting the link of my trade explorer here in this thread.  
  
[http://www.forexfactory.com/showthre...53#post8155553](http://www.forexfactory.com/showthread.php?p=8155553#post8155553)

Love for all; Hatred for none.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#266](/thread/post/8155605#post8155605 "Post Permalink")

  * Mar 23, 2015 3:46am  Mar 23, 2015 3:46am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar135523_1.gif) blamshakk](blamshakk)

  * Joined Mar 2010 | Status: Trader | [2,240 Posts](/search?do=process&provider=Member&searchuser=135523)

thanks.... have loaded it on an m30 chart, lets see what the week brings  
  

> [Quoting radityo.ardi](/thread/post/8155074#post8155074 "View Quoted Post")
> 
> Disliked
> 
> {quote} No timeframe related. Any timeframe will do.
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#267](/thread/post/8156566#post8156566 "Post Permalink")

  * Mar 23, 2015 5:27pm  Mar 23, 2015 5:27pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting LITEchild](/thread/post/8155354#post8155354 "View Quoted Post")
> 
> Disliked
> 
> Hello Rad. Been studying your work. Looks like a job very well done. Im curious if these features you mentioned at the beginning have been implemented yet? {image}
> 
> Ignored

stay tuned, those 2 are still in progress. Would like to complete the logic after the current release.  
  

> [Quoting aahmad29](/thread/post/8155559#post8155559 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi radityo.ardi I am going to start testing with little different settings and I am going to do manual trading. If you give permission I will keep posting the link of my trade explorer here in this thread. [http://www.forexfactory.com/showthre...53#post8155553](http://www.forexfactory.com/showthread.php?p=8155553#post8155553)
> 
> Ignored

no problem bro. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#268](/thread/post/8156600#post8156600 "Post Permalink")

  * Mar 23, 2015 5:38pm  Mar 23, 2015 5:38pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar327198_1.gif) guguxpto](guguxpto)

  * Joined Feb 2013 | Status: EITHER IM RIGHT OR STOP LOSS | [737 Posts](/search?do=process&provider=Member&searchuser=327198)

very good y´m loking fot this for a very long time .  
first there are any bugs it is working ok for those o are testing .  
becouse i´m away from home y dont have the time to testet .  
10% or 5% is very good way to get some money from this or growin an acount . 

Scalping

[small stop loss ; )](guguxpto#04 "View Trade Explorer") All Time Return: 20.8%

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#269](/thread/post/8156859#post8156859 "Post Permalink")

  * Mar 23, 2015 7:03pm  Mar 23, 2015 7:03pm 

  * [ leebsurag](leebsurag)

  * | Membership Revoked  | Joined Oct 2013 | [877 Posts](/search?do=process&provider=Member&searchuser=353350)

> [Quoting radityo.ardi](/thread/post/8151569#post8151569 "View Quoted Post")
> 
> Disliked
> 
> {quote} Quite often. I would say "trending" can happen even on normal hours like now. But spread widening can occurs most of the time after a huge news released. You may notice I've posted some post saying that the cycle got stucked. That's when it happened, could be because of spread is high/wide at that time but could also because of the price moves and retract back before EA could finish open STOP order, so STOP order wasn't properly placed. How often, not too often, I got already 3 - 4 times in 45+ days running the EA, the same situation where...
> 
> Ignored

So an average transaction cost for standard lot is 6 USD, right? Quite cheap for you, as it appears you avoid news trading times. I'm mostly catching pips on news so it's a bit more expensive there. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#270](/thread/post/8160200#post8160200 "Post Permalink")

  * Mar 24, 2015 8:23pm  Mar 24, 2015 8:23pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar392900_1.gif) jollydragon](jollydragon)

  * | Joined Dec 2014  | Status: Trader | [122 Posts](/search?do=process&provider=Member&searchuser=392900)

Dear Radityo,  
  
It's really highly appreciated to get the open-source EA from you.  
I'm still studying it and not understand your precious code very well yet, but there is some problem during testing.   
I tested on M15 and no any orders can be open. Later found StartNow is always 'false' since Resistance1 and Support1 are '0' as if SetSNR() was never called.  
I'm still checking the root cause and hope get some idea from you in parallel. Thanks. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#271](/thread/post/8162233#post8162233 "Post Permalink")

  * Mar 25, 2015 11:51am  Mar 25, 2015 11:51am 

  * [ happytrade38](happytrade38)

  * | Joined Sep 2014  | Status: Trader | [517 Posts](/search?do=process&provider=Member&searchuser=382480)

Hi Radityo,  
I continue start to do the test for the new release.  
I see the default slippage is 50 point (my server is 5 digit, which equivalent to 5pips), what EA react if the real scenario where slippage more than 50 point? thanks a lot. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#272](/thread/post/8162422#post8162422 "Post Permalink")

  * Mar 25, 2015 3:46pm  Mar 25, 2015 3:46pm 

  * [ happytrade38](happytrade38)

  * | Joined Sep 2014  | Status: Trader | [517 Posts](/search?do=process&provider=Member&searchuser=382480)

Hi Radityo,  
I guess I cannot fully utilize the EA you have developed.  
My idea of the strategy is firstly I could buy or sell first, if it hit SL (10 pips), then it will close the position. At the same time open opposite position with 10 pips SL and 50 pips TP. I tested the EA, when it hit -10 pips, it opens another opposite position, but it didn't close the early -10pips position. Any chance to set it? thanks.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#273](/thread/post/8166282#post8166282 "Post Permalink")

  * Mar 26, 2015 8:31pm  Mar 26, 2015 8:31pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar392900_1.gif) jollydragon](jollydragon)

  * | Joined Dec 2014  | Status: Trader | [122 Posts](/search?do=process&provider=Member&searchuser=392900)

Dear Radityo, again highly appreciate your selfless and precious source codes.  
  
May I have some questions on the codes?  
  
1\. I understand a cycle is one round of Martingale from beginning to closed with a series of orders.  
. Why need to use "MaxMartingaleCycle" to limit the cycle loops?  
. Is it necessary to "ResetCycle()" and reset "CycleCount=0"?  
  
2\. Sorry to tell I can't understand the necessity of "if(i==0).." and "if(i==1).." in the example below.  
if(StringSubstr(mn,0,4)==IntegerToString(MagicNumber))  
{  
//Update the UpperGapPrice  
if(i==0) //first order  
{....}  
if(i==1)   
{....}  
  
3\. Within " else if(TrailingTargetType==TTTTrailingTarget) ..", why not to add "“TotalProfit>=TrailingTargetValue && TotalProfit<=TrailingTargetValue+TrailingTarget”" for the sentence " IsTimeToCloseAll=(TrailingTargetValue>0 && TotalProfit<=TrailingTargetValue);"? How can current sentence make profit? It's appreciated if you can kindly help clarify.  
4\. When calculate "FirstPoints" with the sentences "if(Direction==DBuy) { FirstPoints=...", what if the first order of current cycle hasn't been closed?  
5\. Within "SetSNR()", what if it's Holiday and market if off on last Friday?  
6\. Tested 1 year of 2013 and below is the balance wave.  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: backtest.png
Size: 15 KB](/attachment/image/1640841/thumbnail?d=1427369490)](/attachment/image/1640841?d=1427369490)   

  
  
  
​ 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#274](/thread/post/8167606#post8167606 "Post Permalink")

  * Mar 27, 2015 3:41am  Mar 27, 2015 3:41am 

  * [ aahmad29](aahmad29)

  * Joined Aug 2012 | Status: Love for all; Hatred for none | [3,557 Posts](/search?do=process&provider=Member&searchuser=286894)

> [Quoting radityo.ardi](/thread/post/8156566#post8156566 "View Quoted Post")
> 
> Disliked
> 
> {quote} stay tuned, those 2 are still in progress. Would like to complete the logic after the current release. {quote} no problem bro.
> 
> Ignored

First week is going good so far, lets see what happened for coming weeks. Sometimes I loose opportunity to close trade in profit because of my full time job but all of this is part of trading and I have to manage it manually.  
  
[http://www.forexfactory.com/showthre...22#post8166022](http://www.forexfactory.com/showthread.php?p=8166022#post8166022)

Love for all; Hatred for none.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#275](/thread/post/8169450#post8169450 "Post Permalink")

  * Edited 9:35pm  Mar 27, 2015 9:19pm | Edited 9:35pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

Sorry guys. I was out for a week, just to catch up some important job, so couldn't get time to reply you all.  
Shockingly, during my outage, the main martingale testing account is wiped out! ![](https://resources.faireconomy.media/images/emojis/64/1f923.png?v=15.1)  
I already know that Martingale Anytime on this testing is quite risky, knowing the fact that it reaches the max margin used many times.  
  
  

> [Quoting guguxpto](/thread/post/8156600#post8156600 "View Quoted Post")
> 
> Disliked
> 
> very good ym loking fot this for a very long time . first there are any bugs it is working ok for those o are testing . becouse im away from home y dont have the time to testet . 10% or 5% is very good way to get some money from this or growin an acount .
> 
> Ignored

Thanks man.  
  

> [Quoting leebsurag](/thread/post/8156859#post8156859 "View Quoted Post")
> 
> Disliked
> 
> {quote} So an average transaction cost for standard lot is 6 USD, right? Quite cheap for you, as it appears you avoid news trading times. I'm mostly catching pips on news so it's a bit more expensive there.
> 
> Ignored

hmmm... interesting... Ya, probably need to compare for each broker whether it is really gives advantage for us.  
  

> [Quoting jollydragon](/thread/post/8160200#post8160200 "View Quoted Post")
> 
> Disliked
> 
> Dear Radityo, It's really highly appreciated to get the open-source EA from you. I'm still studying it and not understand your precious code very well yet, but there is some problem during testing. I tested on M15 and no any orders can be open. Later found StartNow is always 'false' since Resistance1 and Support1 are '0' as if SetSNR() was never called. I'm still checking the root cause and hope get some idea from you in parallel. Thanks.
> 
> Ignored

I noticed as well. I need to work on the SNR case when the limit is set to zero, I think I have issues with this.  
  

> [Quoting happytrade38](/thread/post/8162233#post8162233 "View Quoted Post")
> 
> Disliked
> 
> Hi Radityo, I continue start to do the test for the new release. I see the default slippage is 50 point (my server is 5 digit, which equivalent to 5pips), what EA react if the real scenario where slippage more than 50 point? thanks a lot.
> 
> Ignored

I haven't tried the slippage scenario. But frankly, very interesting issue where I set slippage to false on some other broker, but the slippage is applied. I don't know whether the broker really accepting slippage = false. But it should throws you an error in case of slippage = false, or slippage = true and you set it to 0 (zero).  
  

> [Quoting happytrade38](/thread/post/8162422#post8162422 "View Quoted Post")
> 
> Disliked
> 
> Hi Radityo, I guess I cannot fully utilize the EA you have developed. My idea of the strategy is firstly I could buy or sell first, if it hit SL (10 pips), then it will close the position. At the same time open opposite position with 10 pips SL and 50 pips TP. I tested the EA, when it hit -10 pips, it opens another opposite position, but it didn't close the early -10pips position. Any chance to set it? thanks.
> 
> Ignored

aaah... .that is a different mechanism, yes, my EA won't fit with that condition ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)  
But good to explore that. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#276](/thread/post/8169753#post8169753 "Post Permalink")

  * Mar 27, 2015 10:54pm  Mar 27, 2015 10:54pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting jollydragon](/thread/post/8166282#post8166282 "View Quoted Post")
> 
> Disliked
> 
> Dear Radityo, again highly appreciate your selfless and precious source codes.​
> 
> Ignored

My pleasure...  
  

> [Quoting jollydragon](/thread/post/8166282#post8166282 "View Quoted Post")
> 
> Disliked
> 
> 1\. I understand a cycle is one round of Martingale from beginning to closed with a series of orders. . Why need to use "MaxMartingaleCycle" to limit the cycle loops? . Is it necessary to "ResetCycle()" and reset "CycleCount=0"?
> 
> Ignored

Max Martingale Cycle is to set how many maximum number of cycle by today. Normally this is set for people like me, where I want to limit my trade in a day max 2 or 3 cycles.  
Now for ResetCycle(), this one is to reset conditionally:  
if (((ArrOrderSize == 0 && !ForceReset) || ForceReset) && MaxMartingaleCycle > 0)  
which means this method is meant for MaxMartingaleCycle set to > 0\. If ForceReset(), it will set CycleCount to 0 if ForceReset = true or no open order and ForceReset = false.  
This condition is to cater a few scenarios:  
If the time of reset and record SNR is reached, but still there's order opened, then it won't reset.  
if there's no order, then it will reset.  
In case you restart / change timeframe and indicate Ues to close all orders.  
  

> [Quoting jollydragon](/thread/post/8166282#post8166282 "View Quoted Post")
> 
> Disliked
> 
> 2\. Sorry to tell I can't understand the necessity of "if(i==0).." and "if(i==1).." in the example below. if(StringSubstr(mn,0,4)==IntegerToString(MagicNumber)) { //Update the UpperGapPrice if(i==0) //first order {....} if(i==1) {....}​
> 
> Ignored

Sorry bro, I also can't remember what I wrote there... since I was off for 1 week. But let me try to explain my best...  
OK, this is just to find what is the Upper tunnel gap (ceiling) and Lower tunnel gap (floor). I use that logic only to record first and second. Since if you notice, that some users may want to reset or restarting (but this is very rare case) their MT4, the EA then can try to detect what is the ceiling and floor. So EA can continue in case restart happen.  
  

> [Quoting jollydragon](/thread/post/8166282#post8166282 "View Quoted Post")
> 
> Disliked
> 
> 3\. Within " else if(TrailingTargetType==TTTTrailingTarget) ..", why not to add "TotalProfit>=TrailingTargetValue && TotalProfit<=TrailingTargetValue+TrailingTarget" for the sentence " IsTimeToCloseAll=(TrailingTargetValue>0 && TotalProfit<=TrailingTargetValue);"? How can current sentence make profit? It's appreciated if you can kindly help clarify. ​
> 
> Ignored

Ok, TrailingTargetValue is the "planned" profit value, which is noted in the current currency of the account.  
There are 3 stages here in the trailing profit scenario.  
1\. when the price below ProfitTarget, of course, nothing happen. TrailingTargetValue will be zero all the time.  
2\. when the price above ProfitTarget AND below Trailing line, then update TrailingTargetValue = ProfitTarget, then cycle will be closed if profit reaches below TrailingTargetValue. See pic below.  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot1.png
Size: 12 KB](/attachment/image/1641903/thumbnail?d=1427461376)](/attachment/image/1641903?d=1427461376)   

  
3\. when the price above ProfitTarget AND above Trailing line, then update TrailingTargetValue = TotalProfit - TrailingTarget. If let us say, with the same condition, the profit going up and up (noted by the condition if ((TotalProfit - TrailingTarget) > TrailingTargetValue), I will keep updating TrailingTargetValue = TotalProfit - TrailingTarget. But if it is not, then I will keep silent, until the TotalProfit falls under TrailingTargetValue, then I close it all.  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot2.png
Size: 19 KB](/attachment/image/1641944/thumbnail?d=1427464515)](/attachment/image/1641944?d=1427464515)   

  
  

> [Quoting jollydragon](/thread/post/8166282#post8166282 "View Quoted Post")
> 
> Disliked
> 
> Dear Radityo, again highly appreciate your selfless and precious source codes. May I have some questions on the codes? 1. I understand a cycle is one round of Martingale from beginning to closed with a series of orders. . Why need to use "MaxMartingaleCycle" to limit the cycle loops? . Is it necessary to "ResetCycle()" and reset "CycleCount=0"? 2. Sorry to tell I can't understand the necessity of "if(i==0).." and "if(i==1).." in the example below. if(StringSubstr(mn,0,4)==IntegerToString(MagicNumber)) { //Update the UpperGapPrice if(i==0) //first...
> 
> Ignored

  

> [Quoting jollydragon](/thread/post/8166282#post8166282 "View Quoted Post")
> 
> Disliked
> 
> 4\. When calculate "FirstPoints" with the sentences "if(Direction==DBuy) { FirstPoints=...", what if the first order of current cycle hasn't been closed?
> 
> Ignored

Then it will get how many points for the first order.  
  

> [Quoting jollydragon](/thread/post/8166282#post8166282 "View Quoted Post")
> 
> Disliked
> 
> 5\. Within "SetSNR()", what if it's Holiday and market if off on last Friday? ​
> 
> Ignored

I still need 1 feature to avoid Holiday and market off day.  
  

> [Quoting jollydragon](/thread/post/8166282#post8166282 "View Quoted Post")
> 
> Disliked
> 
> 6\. Tested 1 year of 2013 and below is the balance wave. ​
> 
> Ignored

Seems good.  
  
  
I hope that answers your questions. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#277](/thread/post/8170075#post8170075 "Post Permalink")

  * Mar 28, 2015 1:03am  Mar 28, 2015 1:03am 

  * [ aahmad29](aahmad29)

  * Joined Aug 2012 | Status: Love for all; Hatred for none | [3,557 Posts](/search?do=process&provider=Member&searchuser=286894)

**The Rebel : Trade Explorer**  
  
Progress for this week. [http://www.forexfactory.com/showthre...64#post8168964](http://www.forexfactory.com/showthread.php?p=8168964#post8168964)

Love for all; Hatred for none.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#278](/thread/post/8170908#post8170908 "Post Permalink")

  * Mar 28, 2015 3:20pm  Mar 28, 2015 3:20pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

Hi all,  
v1.092 has been uploaded. This version is actually same as v1.09, with 1 fix:  
Dynamic Starting Lot is now updated everytime we want to start new cycle --> thanks to the one (I forgot the name) noting this bug down in this thread.  
  
  
Additionally, I've changed the license from MsPL to Tunnel Martingale License. Just same as MsPL with added terms such as charity.  
<https://sites.google.com/site/tunnelmartingalecla/>  
  
If in the future,  
you feel that this EA is USEFUL and GIVING PROFITS to yourself, you are ENCOURAGED to do DONATIONS (stated on the license above). This donations is not for me, but for other needy people, kids and children in your country or any other part of the world.  
  
I dedicated my time and efforts to build this EA freely to them, so let us share a good things we have with them. I'm sure you will agree with me. ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)  
But I will not force you under any circumstances, you have to donate yourself at your own good will. I've done my part and will keep doing this. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#279](/thread/post/8170930#post8170930 "Post Permalink")

  * Mar 28, 2015 4:55pm  Mar 28, 2015 4:55pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

I'll just put some notes on my observations during this weekend.  
  
Inspite of the losses suffered by Martingale AnyTime, it tried to cover the losses, and quite good performance for EU itself. So currently the EA trying to run "good" and covering the losses from $300-ish to now about $878. But still I think this won't last long, bumpy ride ahead.  
Nevertheless, I've never suggested Martingale AnyTime to be used in Live account. Since it is too much risky. The basic principle should consider the amount of cycles daily, the strategy taken, and plan your profit and losses.  
  
OK... continue to the next strategy, High and Low.  
This strategy is quite stable as of now. Not much martingale index consumed, small profit, but stable and smooth. So far reaches index 5, but it was very rare situation. I think I would recommend this strategy.  
To be honest, I've monitored this strategy for long time ago since last year in 2014, before start coding Tunnel Martingale. The profitable trades if you set 1 time trade daily, it will be like 90% profitable trades. But that time, the problem is when the market moves on opposite direction, there's no backup plan. Loss just loss, nothing to recover. Now you know why I add High and Low scenario there, since I know it was profitable with 90%. Because I can link High and Low strategy with this Tunnel Martingale. _So the idea is in case taking High and Low, but the market moves otherwise, I still can get the profit!_  
  
So let us take a look deeper into the forward testing result.  
So far been running this for 44 days, with all time profit for 25% or $1271 from starting balance of $5000. Not much, but quite good and stable. Win rate I think this strategy is higher, around 73%, compared to the other strategy like AnyTime or Support Resistance.  
I'm still thinking that we can somehow tune the settings up so we can get the profit higher, but that's another story I want to test.  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot1.png
Size: 69 KB](/attachment/image/1642351/thumbnail?d=1427528833)](/attachment/image/1642351?d=1427528833)   

  
  
Now you see the vertical line I drew?  
The left side was the old settings, I don't remember what it was, but some bugs was reflected there. Right side is the current settings unchanged till date.  
Now let us see the chart with dashboard.  

Attached Image

![](/attachment/image/1642352?d=1427528934)

  
  
During my observation, lowest margin never touch 50% of the balance! So, I'm still thought of tune the settings up to get more profits monthly.  
  
So, giving this facts, I'm still sure that this method is the most stable one so far. To look for this is quite simple.  
  

Attached Image

![](/attachment/image/1642353?d=1427529237)

  
spikes!  
Yikes! My comment is: need to see where it will fall. This is my Support and Resistance.  
  
And this...  

Attached Image

![](/attachment/image/1642354?d=1427529304)

  
smooth ride! Though I got 1 bumpy ride, but that was because of some bugs. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#280](/thread/post/8170984#post8170984 "Post Permalink")

  * Mar 28, 2015 7:00pm  Mar 28, 2015 7:00pm 

  * [ moncsicsi78](moncsicsi78)

  * | Joined Sep 2011  | Status: Trader | [160 Posts](/search?do=process&provider=Member&searchuser=196773)

It works well in trending periods and all trending pairs, all timeframe. (It is no matter.)  
But there is a disadvantage of it: ranging market.  
If there is a long ranging period or you put it on a ranging pair, the EA (the method) will kill your account.  
I thought about a lot of time how we can safer and/or profitable this method. (Not to be 100% safe, of course.)  
  
One important thing is: diversification. The more pairs you use on it on the same account, the more chance that there will be more pairs which go in profit, than which will remain in loss.  
  
The 2nd important thing is: use only on trending pairs! It is not so difficult to choose some trending pairs.  
  
And the 3rd importnat thing: some modifictaion on this strategy. I have 2 idea about it.  
  
My idea: not to use any indicator to indetify the trend/driection, because every of them can be false.  
Instead of it it would be better **to build pyramid** , every new level would be protect **with trailing stops**.  
With this method the EA would need much less trend movement to be able to close all of its positions.  
And can be able to collect much more profit, than without pyramid. To build pyramid: If an order is in profit, the EA would start to open another position in the same direction with an external adjustable distance (in pips) and an external adjustable lotmultiplier. Every new pyramid level can be protected by trailing stops. So the EA open new pyramid level in just that case when the previous levels are in profit and are protected with TS.  
In the picture attached below: there is a relative long shell position. 150 pips.  
Imagine how much pips you would be able to collect if this 150 pips distances were build by pyramid trades!  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: pyramid.PNG
Size: 39 KB](/attachment/image/1642372/thumbnail?d=1427536759)](/attachment/image/1642372?d=1427536759)   

  
And one more thing: you can make the EA **"2sides"** : we can collect even more profit.  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: 2 sides.PNG
Size: 52 KB](/attachment/image/1642373/thumbnail?d=1427536812)](/attachment/image/1642373?d=1427536812)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Trapping System: Tunnel Martingale
  *   * [ **Reply to Thread** ](/thread/524198-trapping-system-tunnel-martingale/reply#reply)

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

[Martingale, Anti-martingale, and Compounding](/thread/571233-martingale-anti-martingale-and-compounding "Hi all traders, 
i started this thread to meet others people interested in money management. 
We all know that martingale strategies are...") 40 replies

[Martingale, Reverse Martingale, Modified Martingale, Maths](/thread/736165-martingale-reverse-martingale-modified-martingale-maths "Hi all, so Martingale has been a risky yet maybe non profitable system. While roulette has an edge of \(2.7%/5.4%\) 
  
Inspired by Adam...") 1 reply

[How to change this Martingale to Reverse Martingale ?](/thread/546755-how-to-change-this-martingale-to-reverse-martingale "How to change this Martingale to Reverse Martingale ?") 3 replies

[Trapping System: Way to Fully-Automated Trading System](/thread/509226-trapping-system-way-to-fully-automated-trading-system "Hi fellow Traders! 
This is my first time to write a new thread. Would like to share a trading method, which at least made me happy right...") 47 replies

[Martingale vs. Non Martingale (Simplified RoR vs Profit)](/thread/526308-martingale-vs-non-martingale-simplified-ror-vs-profit "Martingale: The gambler doubles his bet after every loss... 
  
Martingale vs. Non Martingale \(Simplified RoR vs Profit in 3 trade runs...") 1 reply

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/524198-trapping-system-tunnel-martingale/reply#reply)
  * Subscribe
  * [221](javascript:void\(0\);)

Attachments: Trapping System: Tunnel Martingale

Tags: Trapping System: Tunnel Martingale

#  [](/thread/524198-trapping-system-tunnel-martingale)Trapping System: Tunnel Martingale 

  * 

  * [#281](/thread/post/8171392#post8171392 "Post Permalink")

  * Mar 29, 2015 5:46am  Mar 29, 2015 5:46am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar356628_2.gif) LITEchild](litechild)

  * Joined Nov 2013 | Status: Member of the 5% club | [1,259 Posts](/search?do=process&provider=Member&searchuser=356628)

> [Quoting radityo.ardi](/thread/post/8170908#post8170908 "View Quoted Post")
> 
> Disliked
> 
> Hi all, v1.092 has been uploaded. This version is actually same as v1.09, with 1 fix: Dynamic Starting Lot is now updated everytime we want to start new cycle --> thanks to the one (I forgot the name) noting this bug down in this thread. Additionally, I've changed the license from MsPL to Tunnel Martingale License. Just same as MsPL with added terms such as charity. <https://sites.google.com/site/tunnelmartingalecla/> If in the future, you feel that this EA is USEFUL and GIVING PROFITS to yourself, you are ENCOURAGED to do DONATIONS (stated...
> 
> Ignored

Thank you for such generous efforts in coding this EA for free, Rad. Your donations idea is certainly a good and morally sound idea. I have been following developments here quietly and the only issues still stopping me from testing out you EA is that Im waiting for the version with the ability to start at X points from current price, and Line color for TP (and hopefully SL). These options I believe will be critical to being profitable in the long term if used in a kind of semi auto mode. Hopefully you will find enough time to make this version available soon. Thanks. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#282](/thread/post/8172383#post8172383 "Post Permalink")

  * Mar 30, 2015 1:06pm  Mar 30, 2015 1:06pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting LITEchild](/thread/post/8171392#post8171392 "View Quoted Post")
> 
> Disliked
> 
> {quote} Thank you for such generous efforts in coding this EA for free, Rad. Your donations idea is certainly a good and morally sound idea. I have been following developments here quietly and the only issues still stopping me from testing out you EA is that Im waiting for the version with the ability to start at X points from current price, and Line color for TP (and hopefully SL). These options I believe will be critical to being profitable in the long term if used in a kind of semi auto mode. Hopefully you will find enough time to make this version...
> 
> Ignored

Thanks for the support man. That's why for the last release I won't give v1.10, because I'm planning to release 3 big features on v1.10.  
Start from X points, Avoiding Holiday, and Date Time series for AnyTime. Sorry for the delay. ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#283](/thread/post/8172483#post8172483 "Post Permalink")

  * Mar 30, 2015 3:04pm  Mar 30, 2015 3:04pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar370635_1.gif) KanGKunG](kangkung)

  * Joined Apr 2014 | Status: Trader | [36 Posts](/search?do=process&provider=Member&searchuser=370635)

relax bro.. just do what we wanna do.. we dont force them to use the EA... up to them to use it or not 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#284](/thread/post/8172807#post8172807 "Post Permalink")

  * Mar 30, 2015 6:08pm  Mar 30, 2015 6:08pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar356628_2.gif) LITEchild](litechild)

  * Joined Nov 2013 | Status: Member of the 5% club | [1,259 Posts](/search?do=process&provider=Member&searchuser=356628)

> [Quoting radityo.ardi](/thread/post/8172383#post8172383 "View Quoted Post")
> 
> Disliked
> 
> {quote} Thanks for the support man. That's why for the last release I won't give v1.10, because I'm planning to release 3 big features on v1.10. Start from X points, Avoiding Holiday, and Date Time series for AnyTime. Sorry for the delay. ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)
> 
> Ignored

![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#285](/thread/post/8174176#post8174176 "Post Permalink")

  * Mar 31, 2015 3:47am  Mar 31, 2015 3:47am 

  * [ Daat](daat)

  * | Joined Mar 2015  | Status: Trader | [2 Posts](/search?do=process&provider=Member&searchuser=406366)

@ radityo.ardi  
  
Congrats for an excellent thread.  
  
I have been forward testing exact same system on demo account for some 6 months now; though with out the benefit of an EA (as my platform is different). My settings are: gap 20 pips with TP and SL also 20 pips. I only trade .US30 at NYO for max one hour. I usually manage two cycles in this duration. An other variation is that I open a buy and a sell position simultaneously. By doing so, I get 20 pips on one position anyway with the first 20 pip movement up or down. The other position then follows the martingale series 1,2,4,8..... This gives me a total of 40 pips in each cycle. Only twice during my entire testing period, the martingale index went beyond 5.   
  
Since I cannot be very regular in my trading due to other commitments, I can only trade for about 12-14 days in a month. It has been generating minimum 10% monthly profit (demo :-)) consistently. There is great potential in this system and if the settings are right, it can be consistently profitable.  
  
What interests me most in your thread is the **DAILY HIGH - LOW strategy**. Can you please shed some more light on the strategy. I shall be highly grateful.  
  
Thanks once again for a very useful thread. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#286](/thread/post/8174786#post8174786 "Post Permalink")

  * Mar 31, 2015 1:31pm  Mar 31, 2015 1:31pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

Thanks @Daat!  
I never thought of using it in US30. Would you care to share what is your starting lot and starting balance? Would like to try it as well.  
  
Daily High Low basically, there's a settings where it will record the current today's high and low price. I noticed this behaviour on EUR/USD and XAU/USD (especially). For XAU/USD, normally I will set to 14:00 SGT (06:00 GMT) to record high and low. And most of the time (90%+) it always breaks either high or low. So, I coupled with this martingale tunnel, but I haven't retry it anyway in XAU/USD, only EUR/USD.  
  
So with Tunnel Martingale, there are 2 elements: the daily high and low recording time, max martingale cycle (based on the current logic, it will work when this value is set to > 0). The others just to follow the standard Tunnel Martingale settings. Once the cycle completes or max martingale reaches, then high low will be set to zero again, until the next day.  
  
Hope it helps. I'll try your strategy on US30, man! Probably gonna live up XAU/USD again in the game. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#287](/thread/post/8185935#post8185935 "Post Permalink")

  * Apr 5, 2015 9:50pm  Apr 5, 2015 9:50pm 

  * [ Daat](daat)

  * | Joined Mar 2015  | Status: Trader | [2 Posts](/search?do=process&provider=Member&searchuser=406366)

> [Quoting radityo.ardi](/thread/post/8174786#post8174786 "View Quoted Post")
> 
> Disliked
> 
> Thanks @Daat! I never thought of using it in US30. Would you care to share what is your starting lot and starting balance? Would like to try it as well. Daily High Low basically, there's a settings where it will record the current today's high and low price. I noticed this behaviour on EUR/USD and XAU/USD (especially). For XAU/USD, normally I will set to 14:00 SGT (06:00 GMT) to record high and low. And most of the time (90%+) it always breaks either high or low. So, I coupled with this martingale tunnel, but I haven't retry it anyway in XAU/USD,...
> 
> Ignored

  
Sorry for late reply.  
  
starting balance $10k  
Initial lot 0.1  
  
I will look forward to your input on this strategy to make it more consistent. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#288](/thread/post/8193124#post8193124 "Post Permalink")

  * Apr 9, 2015 3:55am  Apr 9, 2015 3:55am 

  * [ aahmad29](aahmad29)

  * Joined Aug 2012 | Status: Love for all; Hatred for none | [3,557 Posts](/search?do=process&provider=Member&searchuser=286894)

As I talked to you that I am changing process little bit. Once my trade hits index 2 then I set SL and TP. But both SL and TP are set to close that trade with break even or very small loss. I keep profit before it starts index 2. But I operate 3 cycles at a time sometimes.  
  
<http://www.forexfactory.com/aahmad29#82>  
  
[But](http://www.forexfactory.com/aahmad29#82) there is simple formula.  
  
Greater Risk = Greater Profit/Loss  
  
Less Risk = Less Profit/Loss 

Love for all; Hatred for none.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#289](/thread/post/8207362#post8207362 "Post Permalink")

  * Apr 16, 2015 12:14am  Apr 16, 2015 12:14am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar169138_2.gif) ycchai](ycchai)

  * | Joined Feb 2011  | Status: Trader | [58 Posts](/search?do=process&provider=Member&searchuser=169138)

Hi, thanks for the amazing EA, really a great work and a lot of afford.  
Can anyone modified something for me? I like to use this EA as semi-auto.  
It only start working after i put a trade manually, and stop after a cycle, it won't start again until i put a new order, buy or sell.  
the other function just fine, i can manage it to use. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#290](/thread/post/8207704#post8207704 "Post Permalink")

  * Apr 16, 2015 2:36am  Apr 16, 2015 2:36am 

  * [ aahmad29](aahmad29)

  * Joined Aug 2012 | Status: Love for all; Hatred for none | [3,557 Posts](/search?do=process&provider=Member&searchuser=286894)

> [Quoting ycchai](/thread/post/8207362#post8207362 "View Quoted Post")
> 
> Disliked
> 
> Hi, thanks for the amazing EA, really a great work and a lot of afford. Can anyone modified something for me? I like to use this EA as semi-auto. It only start working after i put a trade manually, and stop after a cycle, it won't start again until i put a new order, buy or sell. the other function just fine, i can manage it to use.
> 
> Ignored

I think you did not read the thread. When you want to place trade, you can use EA to place first trade by changing the settings for initial trade; you can set the settings and tell EA to place Buy or Sell trade. Activate the EA when you want to place trade. Then change the settings "Cycle=1". 

Love for all; Hatred for none.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#291](/thread/post/8208797#post8208797 "Post Permalink")

  * Apr 16, 2015 4:05pm  Apr 16, 2015 4:05pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar169138_2.gif) ycchai](ycchai)

  * | Joined Feb 2011  | Status: Trader | [58 Posts](/search?do=process&provider=Member&searchuser=169138)

> [Quoting aahmad29](/thread/post/8207704#post8207704 "View Quoted Post")
> 
> Disliked
> 
> {quote} I think you did not read the thread. When you want to place trade, you can use EA to place first trade by changing the settings for initial trade; you can set the settings and tell EA to place Buy or Sell trade. Activate the EA when you want to place trade. Then change the settings "Cycle=1".
> 
> Ignored

Oh...i see, thanks for the advise. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#292](/thread/post/8209767#post8209767 "Post Permalink")

  * Apr 16, 2015 9:59pm  Apr 16, 2015 9:59pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar169138_2.gif) ycchai](ycchai)

  * | Joined Feb 2011  | Status: Trader | [58 Posts](/search?do=process&provider=Member&searchuser=169138)

Hi,  
  
I change the setting "cycle=1", but it still open new trade after reach TP, i saw the text in chart "cycle count=2".  
  
One more problem that i face is, let say the start are buy 0.01, when the price reach the PO sell 0.02, it have open a new buy PO 0.04 but after that it close all trade, then open a new trade buy 0.01 at the PO sell 0.02(new cycle).  
  
I upload my setting, if someone could help me look where is wrong. 

Attached File(s)

![File Type: txt](https://assets.faireconomy.media/images/attach/txt.gif) [my.txt](/attachment/file/1655027?d=1429188285) 1 KB | 224 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#293](/thread/post/8212945#post8212945 "Post Permalink")

  * Apr 18, 2015 12:43am  Apr 18, 2015 12:43am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar169138_2.gif) ycchai](ycchai)

  * | Joined Feb 2011  | Status: Trader | [58 Posts](/search?do=process&provider=Member&searchuser=169138)

> [Quoting ycchai](/thread/post/8209767#post8209767 "View Quoted Post")
> 
> Disliked
> 
> Hi, I change the setting "cycle=1", but it still open new trade after reach TP, i saw the text in chart "cycle count=2". One more problem that i face is, let say the start are buy 0.01, when the price reach the PO sell 0.02, it have open a new buy PO 0.04 but after that it close all trade, then open a new trade buy 0.01 at the PO sell 0.02(new cycle). I upload my setting, if someone could help me look where is wrong. {file}
> 
> Ignored

i try few more time after that, it still open new order even i set "cycle=1". after the "longest index: 2" which i mention above, it still happen, i dont know why.  
and the EA open 2 position at the same time at pair EUR/JPY... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#294](/thread/post/8213248#post8213248 "Post Permalink")

  * Apr 18, 2015 3:38am  Apr 18, 2015 3:38am 

  * [ aahmad29](aahmad29)

  * Joined Aug 2012 | Status: Love for all; Hatred for none | [3,557 Posts](/search?do=process&provider=Member&searchuser=286894)

> [Quoting ycchai](/thread/post/8212945#post8212945 "View Quoted Post")
> 
> Disliked
> 
> {quote} i try few more time after that, it still open new order even i set "cycle=1". after the "longest index: 2" which i mention above, it still happen, i dont know why. and the EA open 2 position at the same time at pair EUR/JPY...
> 
> Ignored

Quote radityo.ardi, you will get your answer. 

Love for all; Hatred for none.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#295](/thread/post/8213252#post8213252 "Post Permalink")

  * Apr 18, 2015 3:40am  Apr 18, 2015 3:40am 

  * [ aahmad29](aahmad29)

  * Joined Aug 2012 | Status: Love for all; Hatred for none | [3,557 Posts](/search?do=process&provider=Member&searchuser=286894)

> [Quoting radityo.ardi](/thread/post/8174786#post8174786 "View Quoted Post")
> 
> Disliked
> 
> Thanks @Daat! I never thought of using it in US30. Would you care to share what is your starting lot and starting balance? Would like to try it as well. Daily High Low basically, there's a settings where it will record the current today's high and low price. I noticed this behaviour on EUR/USD and XAU/USD (especially). For XAU/USD, normally I will set to 14:00 SGT (06:00 GMT) to record high and low. And most of the time (90%+) it always breaks either high or low. So, I coupled with this martingale tunnel, but I haven't retry it anyway in XAU/USD,...
> 
> Ignored

Going good so far among all (NFP, ECB and others).  
  
Trade Explorer  
  
<http://www.forexfactory.com/aahmad29#82>

Love for all; Hatred for none.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#296](/thread/post/8213598#post8213598 "Post Permalink")

  * Apr 18, 2015 2:19pm  Apr 18, 2015 2:19pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting ycchai](/thread/post/8212945#post8212945 "View Quoted Post")
> 
> Disliked
> 
> {quote} i try few more time after that, it still open new order even i set "cycle=1". after the "longest index: 2" which i mention above, it still happen, i dont know why. and the EA open 2 position at the same time at pair EUR/JPY...
> 
> Ignored

I noticed this a few weeks ago. I have fixed it but haven't release any fixes. Will release only for this fix this Monday.  
Sorry for my inactivity these 3 weeks, due to some busy stuffs...![](https://resources.faireconomy.media/images/emojis/64/1f641.png?v=15.1)  
  

> [Quoting aahmad29](/thread/post/8213252#post8213252 "View Quoted Post")
> 
> Disliked
> 
> {quote} Going good so far among all (NFP, ECB and others). Trade Explorer <http://www.forexfactory.com/aahmad29#82>
> 
> Ignored

Good result there,man!  
Got no clue why my High Low strategy was blown off. I know that there's risk playing with martingale, and I don't think the other strategies have no risk as well. I guess at some point of time, 100 points gap also got risk. I want to try again with 200 points gap, 1 times a day, SNR or High Low. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#297](/thread/post/8213942#post8213942 "Post Permalink")

  * Apr 19, 2015 12:55am  Apr 19, 2015 12:55am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar169138_2.gif) ycchai](ycchai)

  * | Joined Feb 2011  | Status: Trader | [58 Posts](/search?do=process&provider=Member&searchuser=169138)

> [Quoting aahmad29](/thread/post/8213248#post8213248 "View Quoted Post")
> 
> Disliked
> 
> {quote} Quote radityo.ardi, you will get your answer.
> 
> Ignored

> [Quoting radityo.ardi](/thread/post/8213598#post8213598 "View Quoted Post")
> 
> Disliked
> 
> {quote} I noticed this a few weeks ago. I have fixed it but haven't release any fixes. Will release only for this fix this Monday. Sorry for my inactivity these 3 weeks, due to some busy stuffs...![](https://resources.faireconomy.media/images/emojis/64/1f641.png?v=15.1)
> 
> Ignored

Thanks you, both of you, I appreciate it. ![](https://resources.faireconomy.media/images/emojis/64/270c-fe0f.png?v=15.1)  
No worry, i'm new at this threat, feeling grateful found this EA, before this i do it manually...too tired to monitor the trade,  
ok then, i looking forward the new release ![](https://resources.faireconomy.media/images/emojis/64/1f918.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#298](/thread/post/8216673#post8216673 "Post Permalink")

  * Apr 20, 2015 11:21pm  Apr 20, 2015 11:21pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting ycchai](/thread/post/8213942#post8213942 "View Quoted Post")
> 
> Disliked
> 
> {quote} {quote} Thanks you, both of you, I appreciate it. ![](https://resources.faireconomy.media/images/emojis/64/270c-fe0f.png?v=15.1) No worry, i'm new at this threat, feeling grateful found this EA, before this i do it manually...too tired to monitor the trade, ok then, i looking forward the new release ![](https://resources.faireconomy.media/images/emojis/64/1f918.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)
> 
> Ignored

  
I've uploaded the fixes.  
v1.094  
\- Fix for Max Cycle Count 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#299](/thread/post/8217068#post8217068 "Post Permalink")

  * Apr 21, 2015 2:14am  Apr 21, 2015 2:14am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar169138_2.gif) ycchai](ycchai)

  * | Joined Feb 2011  | Status: Trader | [58 Posts](/search?do=process&provider=Member&searchuser=169138)

> [Quoting radityo.ardi](/thread/post/8216673#post8216673 "View Quoted Post")
> 
> Disliked
> 
> {quote} I've uploaded the fixes. v1.094 - Fix for Max Cycle Count
> 
> Ignored

Ok, thanks a million ![](https://resources.faireconomy.media/images/emojis/64/1f47c.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#300](/thread/post/8217227#post8217227 "Post Permalink")

  * Apr 21, 2015 3:44am  Apr 21, 2015 3:44am 

  * [ aahmad29](aahmad29)

  * Joined Aug 2012 | Status: Love for all; Hatred for none | [3,557 Posts](/search?do=process&provider=Member&searchuser=286894)

> [Quoting radityo.ardi](/thread/post/8213598#post8213598 "View Quoted Post")
> 
> Disliked
> 
> {quote} I noticed this a few weeks ago. I have fixed it but haven't release any fixes. Will release only for this fix this Monday. Sorry for my inactivity these 3 weeks, due to some busy stuffs...![](https://resources.faireconomy.media/images/emojis/64/1f641.png?v=15.1) {quote} Good result there,man! Got no clue why my High Low strategy was blown off. I know that there's risk playing with martingale, and I don't think the other strategies have no risk as well. I guess at some point of time, 100 points gap also got risk. I want to try again with 200 points gap, 1 times a day, SNR or High Low.
> 
> Ignored

  
I wanted to test it because I wanted that index don't go more than 5. Slow but steady profit is ok for me. If in one cycle you close the trade in index 5, then it is very good. I tested 200 point gap even before writing posts in this thread but at some point it didn't fail but it was risk and I wasn't comfortable with it. On the top of it I chose half level because if price hit half level then it means that price is not ranging and time to ready for big move.  
  
If you want to avoid higher index then there is another idea in my mind that when price hit half level then activate your system with 200 points. Once trade is closed then wait gain for PA to hit half level and activate EA again. 

Love for all; Hatred for none.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Trapping System: Tunnel Martingale
  *   * [ **Reply to Thread** ](/thread/524198-trapping-system-tunnel-martingale/reply#reply)

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

[Martingale, Anti-martingale, and Compounding](/thread/571233-martingale-anti-martingale-and-compounding "Hi all traders, 
i started this thread to meet others people interested in money management. 
We all know that martingale strategies are...") 40 replies

[Martingale, Reverse Martingale, Modified Martingale, Maths](/thread/736165-martingale-reverse-martingale-modified-martingale-maths "Hi all, so Martingale has been a risky yet maybe non profitable system. While roulette has an edge of \(2.7%/5.4%\) 
  
Inspired by Adam...") 1 reply

[How to change this Martingale to Reverse Martingale ?](/thread/546755-how-to-change-this-martingale-to-reverse-martingale "How to change this Martingale to Reverse Martingale ?") 3 replies

[Trapping System: Way to Fully-Automated Trading System](/thread/509226-trapping-system-way-to-fully-automated-trading-system "Hi fellow Traders! 
This is my first time to write a new thread. Would like to share a trading method, which at least made me happy right...") 47 replies

[Martingale vs. Non Martingale (Simplified RoR vs Profit)](/thread/526308-martingale-vs-non-martingale-simplified-ror-vs-profit "Martingale: The gambler doubles his bet after every loss... 
  
Martingale vs. Non Martingale \(Simplified RoR vs Profit in 3 trade runs...") 1 reply

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/524198-trapping-system-tunnel-martingale/reply#reply)
  * Subscribe
  * [221](javascript:void\(0\);)

Attachments: Trapping System: Tunnel Martingale

Tags: Trapping System: Tunnel Martingale

#  [](/thread/524198-trapping-system-tunnel-martingale)Trapping System: Tunnel Martingale 

  * 

  * [#301](/thread/post/8218204#post8218204 "Post Permalink")

  * Apr 21, 2015 5:26pm  Apr 21, 2015 5:26pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar169138_2.gif) ycchai](ycchai)

  * | Joined Feb 2011  | Status: Trader | [58 Posts](/search?do=process&provider=Member&searchuser=169138)

> [Quoting ycchai](/thread/post/8212945#post8212945 "View Quoted Post")
> 
> Disliked
> 
> {quote} i try few more time after that, it still open new order even i set "cycle=1". after the "longest index: 2" which i mention above, it still happen, i dont know why. and the EA open 2 position at the same time at pair EUR/JPY...
> 
> Ignored

so far, didn't see these problem.  
  
if attach at USD/CHF, it got a yellow line, Break Even line, it display the text of break even level at chart too...but the EA did nothing if price retrace, it just showing up. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#302](/thread/post/8218365#post8218365 "Post Permalink")

  * Apr 21, 2015 6:08pm  Apr 21, 2015 6:08pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting ycchai](/thread/post/8218204#post8218204 "View Quoted Post")
> 
> Disliked
> 
> {quote} so far, didn't see these problem. if attach at USD/CHF, it got a yellow line, Break Even line, it display the text of break even level at chart too...but the EA did nothing if price retrace, it just showing up.
> 
> Ignored

what does that mean by "EA did nothing"? need to understand the issue.  
let me know your broker, account type, and settings you've used. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#303](/thread/post/8219244#post8219244 "Post Permalink")

  * Apr 21, 2015 11:59pm  Apr 21, 2015 11:59pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar169138_2.gif) ycchai](ycchai)

  * | Joined Feb 2011  | Status: Trader | [58 Posts](/search?do=process&provider=Member&searchuser=169138)

> [Quoting radityo.ardi](/thread/post/8218365#post8218365 "View Quoted Post")
> 
> Disliked
> 
> {quote} what does that mean by "EA did nothing"? need to understand the issue. let me know your broker, account type, and settings you've used.
> 
> Ignored

i mean the break even line at USD/CHF, it just showing, but not really will "break even", i thought just UC got this, but now i saw on EU chart too, is there any setting for BE ![](https://resources.faireconomy.media/images/emojis/64/1f624.png?v=15.1). i use tickmill ecn demo acc.  
  
P/S can i modify this EA? for personal use only 

Attached File(s)

![File Type: txt](https://assets.faireconomy.media/images/attach/txt.gif) [my.set.txt](/attachment/file/1658455?d=1429628265) 1 KB | 258 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#304](/thread/post/8219532#post8219532 "Post Permalink")

  * Apr 22, 2015 1:52am  Apr 22, 2015 1:52am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting ycchai](/thread/post/8219244#post8219244 "View Quoted Post")
> 
> Disliked
> 
> {quote} i mean the break even line at USD/CHF, it just showing, but not really will "break even", i thought just UC got this, but now i saw on EU chart too, is there any setting for BE ![](https://resources.faireconomy.media/images/emojis/64/1f624.png?v=15.1). i use tickmill ecn demo acc. P/S can i modify this EA? for personal use only {file}
> 
> Ignored

break even is still experimental and need further testing. This has nothing to do with close all orders logic, I kept it separate. Break even does only calculation where you got $0 profit price. It doesn't mean it will close all orders.  
Hope that answers. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#305](/thread/post/8219568#post8219568 "Post Permalink")

  * Apr 22, 2015 2:13am  Apr 22, 2015 2:13am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar169138_2.gif) ycchai](ycchai)

  * | Joined Feb 2011  | Status: Trader | [58 Posts](/search?do=process&provider=Member&searchuser=169138)

> [Quoting radityo.ardi](/thread/post/8219532#post8219532 "View Quoted Post")
> 
> Disliked
> 
> {quote} break even is still experimental and need further testing. This has nothing to do with close all orders logic, I kept it separate. Break even does only calculation where you got $0 profit price. It doesn't mean it will close all orders. Hope that answers.
> 
> Ignored

i see, so i just have to ignore it then. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#306](/thread/post/8223823#post8223823 "Post Permalink")

  * Edited 9:05pm  Apr 23, 2015 7:08pm | Edited 9:05pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar169138_2.gif) ycchai](ycchai)

  * | Joined Feb 2011  | Status: Trader | [58 Posts](/search?do=process&provider=Member&searchuser=169138)

> [Quoting radityo.ardi](/thread/post/8216673#post8216673 "View Quoted Post")
> 
> Disliked
> 
> {quote} I've uploaded the fixes. v1.094 - Fix for Max Cycle Count
> 
> Ignored

Any idea why it close all at index 2? it happen again 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: stop at index 2.jpg
Size: 116 KB](/attachment/image/1660077/thumbnail?d=1429783671)](/attachment/image/1660077?d=1429783671)   
[![Click to Enlarge

Name: more.jpg
Size: 282 KB](/attachment/image/1660198/thumbnail?d=1429790726)](/attachment/image/1660198?d=1429790726)   

Attached File(s)

![File Type: txt](https://assets.faireconomy.media/images/attach/txt.gif) [my.set.txt](/attachment/file/1660078?d=1429783691) 1 KB | 299 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#307](/thread/post/8226348#post8226348 "Post Permalink")

  * Apr 24, 2015 6:27pm  Apr 24, 2015 6:27pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting ycchai](/thread/post/8223823#post8223823 "View Quoted Post")
> 
> Disliked
> 
> {quote} Any idea why it close all at index 2? it happen again {image} {file} {image}
> 
> Ignored

still seems to be fine based on the screenshot. but I don't have any idea why it was closing at index 2, where your settings is actually until index of 5 (if I'm not wrong).  
I was started this with [tickmill](/brokers/tickmill "View Tickmill Broker Profile"), and still using tickmill, nowhere it fails in some index. even I attach your settings, it also still running fine and never close at index 5.  
  
would you be able to check whether you attach any other indicator on your chart which does close the order?  
I thought it was because of stop loss, but your stop loss set to false, so it should not have any issue. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#308](/thread/post/8226602#post8226602 "Post Permalink")

  * Apr 24, 2015 7:50pm  Apr 24, 2015 7:50pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar169138_2.gif) ycchai](ycchai)

  * | Joined Feb 2011  | Status: Trader | [58 Posts](/search?do=process&provider=Member&searchuser=169138)

> [Quoting radityo.ardi](/thread/post/8226348#post8226348 "View Quoted Post")
> 
> Disliked
> 
> {quote} still seems to be fine based on the screenshot. but I don't have any idea why it was closing at index 2, where your settings is actually until index of 5 (if I'm not wrong). I was started this with tickmill, and still using tickmill, nowhere it fails in some index. even I attach your settings, it also still running fine and never close at index 5. would you be able to check whether you attach any other indicator on your chart which does close the order? I thought it was because of stop loss, but your stop loss set to false, so it should...
> 
> Ignored

![](https://resources.faireconomy.media/images/emojis/64/1f624.png?v=15.1)  
indicator shouldn't be a problem, it don't manage trade, i didn't use other EA, just 3 TM EA at different pair with different magic number. anyway i will try again with different setting, will inform if figure out where's wrong. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#309](/thread/post/8228527#post8228527 "Post Permalink")

  * Apr 26, 2015 11:10am  Apr 26, 2015 11:10am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting ycchai](/thread/post/8226602#post8226602 "View Quoted Post")
> 
> Disliked
> 
> {quote} ![](https://resources.faireconomy.media/images/emojis/64/1f624.png?v=15.1) indicator shouldn't be a problem, it don't manage trade, i didn't use other EA, just 3 TM EA at different pair with different magic number. anyway i will try again with different setting, will inform if figure out where's wrong.
> 
> Ignored

Just try with 1 new demo account, totally empty chart, no indicators, and run that EA alone. if no issues, that means some code (either in indicator or another EA) that is interrupting this EA. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#310](/thread/post/8228566#post8228566 "Post Permalink")

  * Apr 26, 2015 2:38pm  Apr 26, 2015 2:38pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar334546_1.gif) Pipomagic](pipomagic)

  * Joined May 2013 | Status: Coder, Trader & Optimist | [209 Posts](/search?do=process&provider=Member&searchuser=334546)

They say, " 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Martingale-Trading.png
Size: 506 KB](/attachment/image/1661815/thumbnail?d=1430026650)](/attachment/image/1661815?d=1430026650)   

DON'T TRADE THE DIRECTION, TRADE THE MOVE

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#311](/thread/post/8228609#post8228609 "Post Permalink")

  * Apr 26, 2015 5:07pm  Apr 26, 2015 5:07pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar297449_41.gif) broketrader](broketrader)

  * Joined Oct 2012 | Status: Trader | [1,696 Posts](/search?do=process&provider=Member&searchuser=297449)

Hi radityo,  
  
It's always interesting for me following people doing studies on martingales. I have done a lot of work myself on this subject and still working on it and if you allow me, I would like to share my findings, maybe they will be useful for you too.  
  
1\. Trading from London open to NY close is the right way to go at least for EUR/USD/GBP.  
2\. You should maybe consider not allowing new trades during NY news hours.  
3\. If I have understood, your EA makes symmetric trades eg. 20 pip TP, 20 pip SL You should consider making it asymmetric eg. 15 pips SL, 30 pip TP (or off course any values you want) this way one win recover 2 losses and your index increases slowly.  
4\. Consider integrating a trailing stop once that your target is reached instead of taking profits at that level.  
  
And finally and maybe my best advice, consider simplifying your EA, for me it seems far too complicated. In the past, I made an EA that worked not so bad until it imploded, it was quite complicated and had some points in common with yours, it cost me months of work to have finally several parameters that were just cancelling each other. when it imploded, I abandoned it and didn't trade for several months, then an idea came, coded it using the martingale approach and in two days I had the EA working, and the best part is that it's 2 pages of code and has 2 parameters only, imagine that, it just amazed me as I was thinking that it shouldn't work, like 99% of the EAs I write.  
  
That's not to say, that I'm better than you, no way! just emphasize that you should add a trading idea/system to your tunnel EA, maybe trade the daily breaks, high/low hour breaks, etc.. you see the point.  
  
That were just my 2 cents, anyway congratulations for your work and thanks for sharing with others.  
I will follow. 

Simplicity is the Ultimate Sophistication.

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#312](/thread/post/8228647#post8228647 "Post Permalink")

  * Apr 26, 2015 6:38pm  Apr 26, 2015 6:38pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar356628_2.gif) LITEchild](litechild)

  * Joined Nov 2013 | Status: Member of the 5% club | [1,259 Posts](/search?do=process&provider=Member&searchuser=356628)

> [Quoting broketrader](/thread/post/8228609#post8228609 "View Quoted Post")
> 
> Disliked
> 
> **you should add a trading idea/system to your tunnel EA, maybe trade the daily breaks, high/low hour breaks, etc.. you see the point.**
> 
> Ignored

![](https://resources.faireconomy.media/images/emojis/64/1f44f.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f44f.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f44f.png?v=15.1)....waiting for the version with the ability to start at X points from current price, and Line color for TP (and hopefully SL). These options I believe will be critical to being profitable in the long term if used in a kind of semi auto mode. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#313](/thread/post/8229718#post8229718 "Post Permalink")

  * Apr 27, 2015 5:46pm  Apr 27, 2015 5:46pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar157942_10.gif) fxindikator](fxindikator)

  * Joined Oct 2010 | Status: Trader | [167 Posts](/search?do=process&provider=Member&searchuser=157942)

> [Quoting radityo.ardi](/thread/post/8226348#post8226348 "View Quoted Post")
> 
> Disliked
> 
> {quote} still seems to be fine based on the screenshot. but I don't have any idea why it was closing at index 2, where your settings is actually until index of 5 (if I'm not wrong). I was started this with tickmill, and still using tickmill, nowhere it fails in some index. even I attach your settings, it also still running fine and never close at index 5. would you be able to check whether you attach any other indicator on your chart which does close the order? I thought it was because of stop loss, but your stop loss set to false, so it should...
> 
> Ignored

checking your trade explorer, quite a fans, all account with same broker feed. any personal inquiry about their live account ?, I think it's a good time to put real forward test with them, since they reintroduce the deposit bonus. been try my best to study most of your marty system lately, and had same view as broketrader said, it's way too complicated I think ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1). well, your result are still going, and it's been almost 3 months, right ? I'd love to use my own account and put some report upon these thread, but I do need more clear view upon the EA setting ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1). 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#314](/thread/post/8241593#post8241593 "Post Permalink")

  * May 4, 2015 2:09am  May 4, 2015 2:09am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting fxindikator](/thread/post/8229718#post8229718 "View Quoted Post")
> 
> Disliked
> 
> {quote} checking your trade explorer, quite a fans, all account with same broker feed. any personal inquiry about their live account ?, I think it's a good time to put real forward test with them, since they reintroduce the deposit bonus. been try my best to study most of your marty system lately, and had same view as broketrader said, it's way too complicated I think ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1). well, your result are still going, and it's been almost 3 months, right ? I'd love to use my own account and put some report upon these thread, but I do need more clear view upon...
> 
> Ignored

Careful, man. I do tempted to try it on live. but at least you must try first on demo.  
Keep in mind, just 1 cycle a day is more than enough, you can put the measure up, with support and resistance, or daily high low. But if you decided to run with anytime, you'd have to be careful.  
  
  
  
To all, I'm very sorry for my inactivity. My day job needs some attentions these days... But that doesn't mean I stop enhancing this EA, I'll keep doing it, infact I got another one, that is still tested. This something to do with grids, and the result is far better than Martingale Tunnel.  
  
My 'Another TM' got broke on Friday, I forgot to turn off during Labour Day...  
Stay calm and wait.... I'll try to keep up... 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#315](/thread/post/8242626#post8242626 "Post Permalink")

  * May 4, 2015 7:55pm  May 4, 2015 7:55pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar157942_10.gif) fxindikator](fxindikator)

  * Joined Oct 2010 | Status: Trader | [167 Posts](/search?do=process&provider=Member&searchuser=157942)

> [Quoting radityo.ardi](/thread/post/8241593#post8241593 "View Quoted Post")
> 
> Disliked
> 
> {quote} Careful, man. I do tempted to try it on live. but at least you must try first on demo. Keep in mind, just 1 cycle a day is more than enough, you can put the measure up, with support and resistance, or daily high low. But if you decided to run with anytime, you'd have to be careful. To all, I'm very sorry for my inactivity. My day job needs some attentions these days... But that doesn't mean I stop enhancing this EA, I'll keep doing it, infact I got another one, that is still tested. This something to do with grids, and the result is far...
> 
> Ignored

no worries, real problem comes only when we deny the risk with forex trading, especially when using martingale type. many traders may despite these method, but in real fact many people still got profit from it. which means lot increasement process do had real potential for small amount deposit, to burst our profit gain.  
if you had an skype id, would you mind to add me on your cycle ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1), my skype are exact same as FF id.  
had several trading method tested with most ecn account type, especially with tickmill account. the only thing remain with these tunnel it may news filter feature, linked with FF newscal indi perhaps. looking forward to see the new grid system, if only I had solid knowledge with coding would love to give a hand, but for a moment I may able to put minor contribution with suggestion and help with the forward testing process. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#316](/thread/post/8244801#post8244801 "Post Permalink")

  * May 5, 2015 7:53pm  May 5, 2015 7:53pm 

  * [ TickJob](tickjob)

  * | Joined Apr 2007  | Status: Trader | [166 Posts](/search?do=process&provider=Member&searchuser=37449)

> [Quoting broketrader](/thread/post/8228609#post8228609 "View Quoted Post")
> 
> Disliked
> 
> 3\. If I have understood, your EA makes symmetric trades eg. 20 pip TP, 20 pip SL You should consider making it asymmetric eg. 15 pips SL, 30 pip TP (or off course any values you want) this way one win recover 2 losses and your index increases slowly.  
>  4\. Consider integrating a trailing stop once that your target is reached instead of taking profits at that level.
> 
> Ignored

Hi radityo,  
Will it be possible to enchance your EA to include these two features?  
Sometimes we may fall into the range bound for long and we want to maximise our stay in the game by reducing the lot sizes. Once the price get out of the range usually should not be a problem to run 2xSL or higher. May I suggest to have the following type of lot size increament, or similar.  
  
The following table SL=10 is just example, it can be X pips or points user set. 

Attached Image

![](/attachment/image/1668128?d=1430823361)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#317](/thread/post/8245015#post8245015 "Post Permalink")

  * May 5, 2015 9:30pm  May 5, 2015 9:30pm 

  * [ TickJob](tickjob)

  * | Joined Apr 2007  | Status: Trader | [166 Posts](/search?do=process&provider=Member&searchuser=37449)

I got the table of lotsize from: <http://www.forexfactory.com/showthread.php?t=43221>

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#318](/thread/post/8246403#post8246403 "Post Permalink")

  * May 6, 2015 1:41pm  May 6, 2015 1:41pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

Hi All,  
I've been working on this EA separately, and would like to share to you (as promised) some small interesting information after few days testing.  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot1.png
Size: 39 KB](/attachment/image/1668763/thumbnail?d=1430886700)](/attachment/image/1668763?d=1430886700)   

  
  
Seems promising and better than Tunnel Martingale, well, in my opinion. I don't deny the risk behind (we all do trading, then we should accept the risk), but still less risk than Tunnel Martingale. I don't know what to give name to this EA, but as of now, named as GridTraps.  
  
Even I do on LIVE account for past 3 days. Too brave, huh??  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot2.png
Size: 51 KB](/attachment/image/1668766/thumbnail?d=1430887173)](/attachment/image/1668766?d=1430887173)   

  
  
I'm planning to create a separate thread. Do you think it is worth to try? 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#319](/thread/post/8246412#post8246412 "Post Permalink")

  * May 6, 2015 1:50pm  May 6, 2015 1:50pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar356628_2.gif) LITEchild](litechild)

  * Joined Nov 2013 | Status: Member of the 5% club | [1,259 Posts](/search?do=process&provider=Member&searchuser=356628)

> [Quoting radityo.ardi](/thread/post/8246403#post8246403 "View Quoted Post")
> 
> Disliked
> 
> Hi All, I've been working on this EA separately, and would like to share to you (as promised) some small interesting information after few days testing. {image} Seems promising and better than Tunnel Martingale, well, in my opinion. I don't deny the risk behind (we all do trading, then we should accept the risk), but still less risk than Tunnel Martingale. I don't know what to give name to this EA, but as of now, named as GridTraps. Even I do on LIVE account for past 3 days. Too brave, huh?? {image} I'm planning to create a separate thread. Do you...
> 
> Ignored

![](https://resources.faireconomy.media/images/emojis/64/1f914.png?v=15.1) Sounds interesting... should be worth exploring ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#320](/thread/post/8246481#post8246481 "Post Permalink")

  * May 6, 2015 2:49pm  May 6, 2015 2:49pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar169138_2.gif) ycchai](ycchai)

  * | Joined Feb 2011  | Status: Trader | [58 Posts](/search?do=process&provider=Member&searchuser=169138)

> [Quoting radityo.ardi](/thread/post/8246403#post8246403 "View Quoted Post")
> 
> Disliked
> 
> Hi All, I've been working on this EA separately, and would like to share to you (as promised) some small interesting information after few days testing. {image} Seems promising and better than Tunnel Martingale, well, in my opinion. I don't deny the risk behind (we all do trading, then we should accept the risk), but still less risk than Tunnel Martingale. I don't know what to give name to this EA, but as of now, named as GridTraps. Even I do on LIVE account for past 3 days. Too brave, huh?? {image} I'm planning to create a separate thread. Do you...
> 
> Ignored

Need more info ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Trapping System: Tunnel Martingale
  *   * [ **Reply to Thread** ](/thread/524198-trapping-system-tunnel-martingale/reply#reply)

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

[Martingale, Anti-martingale, and Compounding](/thread/571233-martingale-anti-martingale-and-compounding "Hi all traders, 
i started this thread to meet others people interested in money management. 
We all know that martingale strategies are...") 40 replies

[Martingale, Reverse Martingale, Modified Martingale, Maths](/thread/736165-martingale-reverse-martingale-modified-martingale-maths "Hi all, so Martingale has been a risky yet maybe non profitable system. While roulette has an edge of \(2.7%/5.4%\) 
  
Inspired by Adam...") 1 reply

[How to change this Martingale to Reverse Martingale ?](/thread/546755-how-to-change-this-martingale-to-reverse-martingale "How to change this Martingale to Reverse Martingale ?") 3 replies

[Trapping System: Way to Fully-Automated Trading System](/thread/509226-trapping-system-way-to-fully-automated-trading-system "Hi fellow Traders! 
This is my first time to write a new thread. Would like to share a trading method, which at least made me happy right...") 47 replies

[Martingale vs. Non Martingale (Simplified RoR vs Profit)](/thread/526308-martingale-vs-non-martingale-simplified-ror-vs-profit "Martingale: The gambler doubles his bet after every loss... 
  
Martingale vs. Non Martingale \(Simplified RoR vs Profit in 3 trade runs...") 1 reply

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/524198-trapping-system-tunnel-martingale/reply#reply)
  * Subscribe
  * [221](javascript:void\(0\);)

Attachments: Trapping System: Tunnel Martingale

Tags: Trapping System: Tunnel Martingale

#  [](/thread/524198-trapping-system-tunnel-martingale)Trapping System: Tunnel Martingale 

  * 

  * [#321](/thread/post/8246564#post8246564 "Post Permalink")

  * May 6, 2015 3:35pm  May 6, 2015 3:35pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar398921_25.gif) BillYon](billyon)

  * Joined Feb 2015 | Status: Trader | [924 Posts](/search?do=process&provider=Member&searchuser=398921)

> [Quoting radityo.ardi](/thread/post/8246403#post8246403 "View Quoted Post")
> 
> Disliked
> 
> Hi All, I've been working on this EA separately, and would like to share to you (as promised) some small interesting information after few days testing. {image} Seems promising and better than Tunnel Martingale, well, in my opinion. I don't deny the risk behind (we all do trading, then we should accept the risk), but still less risk than Tunnel Martingale. I don't know what to give name to this EA, but as of now, named as GridTraps. Even I do on LIVE account for past 3 days. Too brave, huh?? {image} I'm planning to create a separate thread. Do you...
> 
> Ignored

  
Yes .... 

Solutions ONLY!!!

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#322](/thread/post/8246705#post8246705 "Post Permalink")

  * May 6, 2015 4:33pm  May 6, 2015 4:33pm 

  * [ TickJob](tickjob)

  * | Joined Apr 2007  | Status: Trader | [166 Posts](/search?do=process&provider=Member&searchuser=37449)

> [Quoting radityo.ardi](/thread/post/8246403#post8246403 "View Quoted Post")
> 
> Disliked
> 
> Hi All, I've been working on this EA separately, and would like to share to you (as promised) some small interesting information after few days testing. {image} Seems promising and better than Tunnel Martingale, well, in my opinion. I don't deny the risk behind (we all do trading, then we should accept the risk), but still less risk than Tunnel Martingale. I don't know what to give name to this EA, but as of now, named as GridTraps. Even I do on LIVE account for past 3 days. Too brave, huh?? {image} I'm planning to create a separate thread. Do you...
> 
> Ignored

Are you talking about this type: [http://urbanforex.com/forum/topics/4...ource=activity](http://urbanforex.com/forum/topics/4-levels-martingale-grid-system?xg_source=activity)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#323](/thread/post/8246723#post8246723 "Post Permalink")

  * May 6, 2015 4:41pm  May 6, 2015 4:41pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar297449_41.gif) broketrader](broketrader)

  * Joined Oct 2012 | Status: Trader | [1,696 Posts](/search?do=process&provider=Member&searchuser=297449)

> [Quoting radityo.ardi](/thread/post/8246403#post8246403 "View Quoted Post")
> 
> Disliked
> 
> Hi All, I've been working on this EA separately, and would like to share to you (as promised) some small interesting information after few days testing. {image} Seems promising and better than Tunnel Martingale, well, in my opinion. I don't deny the risk behind (we all do trading, then we should accept the risk), but still less risk than Tunnel Martingale. I don't know what to give name to this EA, but as of now, named as GridTraps. Even I do on LIVE account for past 3 days. Too brave, huh?? {image} I'm planning to create a separate thread. Do you...
> 
> Ignored

Off course it's worth to try. Go go go ! 

Simplicity is the Ultimate Sophistication.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#324](/thread/post/8246806#post8246806 "Post Permalink")

  * May 6, 2015 5:12pm  May 6, 2015 5:12pm 

  * [ aahmad29](aahmad29)

  * Joined Aug 2012 | Status: Love for all; Hatred for none | [3,557 Posts](/search?do=process&provider=Member&searchuser=286894)

> [Quoting radityo.ardi](/thread/post/8246403#post8246403 "View Quoted Post")
> 
> Disliked
> 
> Hi All, I've been working on this EA separately, and would like to share to you (as promised) some small interesting information after few days testing. {image} Seems promising and better than Tunnel Martingale, well, in my opinion. I don't deny the risk behind (we all do trading, then we should accept the risk), but still less risk than Tunnel Martingale. I don't know what to give name to this EA, but as of now, named as GridTraps. Even I do on LIVE account for past 3 days. Too brave, huh?? {image} I'm planning to create a separate thread. Do you...
> 
> Ignored

I am always ready to test new ideas but please provide more info about the logic of this Grid method. I will do manual testing in worst scenarios. 

Love for all; Hatred for none.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#325](/thread/post/8246896#post8246896 "Post Permalink")

  * May 6, 2015 5:49pm  May 6, 2015 5:49pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar199316_1.gif) ellenbrook](ellenbrook)

  * Joined Oct 2011 | Status: Trader | [1,034 Posts](/search?do=process&provider=Member&searchuser=199316)

> [Quoting BillYon](/thread/post/8246564#post8246564 "View Quoted Post")
> 
> Disliked
> 
> {quote} Yes ....
> 
> Ignored

YES SURE GO FOR IT PLEASE![](https://resources.faireconomy.media/images/emojis/64/1f44f.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#326](/thread/post/8247670#post8247670 "Post Permalink")

  * May 6, 2015 10:43pm  May 6, 2015 10:43pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting TickJob](/thread/post/8244801#post8244801 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi radityo, Will it be possible to enchance your EA to include these two features? Sometimes we may fall into the range bound for long and we want to maximise our stay in the game by reducing the lot sizes. Once the price get out of the range usually should not be a problem to run 2xSL or higher. May I suggest to have the following type of lot size increament, or similar. The following table SL=10 is just example, it can be X pips or points user set. {image}
> 
> Ignored

Hi TickJob,  
I may not enhance the EA to another level. But your idea seems considerably ok. Not sure whether I can enhance more, since it is already "too much settings" words coming out from my mind... ![](https://resources.faireconomy.media/images/emojis/64/1f61f.png?v=15.1)

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#327](/thread/post/8247778#post8247778 "Post Permalink")

  * May 6, 2015 11:16pm  May 6, 2015 11:16pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting TickJob](/thread/post/8246705#post8246705 "View Quoted Post")
> 
> Disliked
> 
> {quote} Are you talking about this type: [http://urbanforex.com/forum/topics/4...ource=activity](http://urbanforex.com/forum/topics/4-levels-martingale-grid-system?xg_source=activity)
> 
> Ignored

No. I'm talking about standard grid, no martingale concept here...  
​  

> [Quoting LITEchild](/thread/post/8246412#post8246412 "View Quoted Post")
> 
> Disliked
> 
> {quote} ![](https://resources.faireconomy.media/images/emojis/64/1f914.png?v=15.1) Sounds interesting... should be worth exploring ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)
> 
> Ignored

> [Quoting ycchai](/thread/post/8246481#post8246481 "View Quoted Post")
> 
> Disliked
> 
> {quote} Need more info ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)
> 
> Ignored

> [Quoting BillYon](/thread/post/8246564#post8246564 "View Quoted Post")
> 
> Disliked
> 
> {quote} Yes ....
> 
> Ignored

> [Quoting broketrader](/thread/post/8246723#post8246723 "View Quoted Post")
> 
> Disliked
> 
> {quote} Off course it's worth to try. Go go go !
> 
> Ignored

> [Quoting aahmad29](/thread/post/8246806#post8246806 "View Quoted Post")
> 
> Disliked
> 
> {quote} I am always ready to test new ideas but please provide more info about the logic of this Grid method. I will do manual testing in worst scenarios.
> 
> Ignored

> [Quoting ellenbrook](/thread/post/8246896#post8246896 "View Quoted Post")
> 
> Disliked
> 
> {quote} YES SURE GO FOR IT PLEASE![](https://resources.faireconomy.media/images/emojis/64/1f44f.png?v=15.1)
> 
> Ignored

Thank you for the overwhelming responses.  
I'll make another thread for this EA (this weekend), and will get your help to test it out. I'll put the details on that new thread. For those who are wondering, actually this is an old grid method, which has been discussed and some created free EA (free at first) but then ......... everything changed when the fire nation attacked!  
  
Give me some time to wrap the EA up, so it will be more clean. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#328](/thread/post/8247826#post8247826 "Post Permalink")

  * May 6, 2015 11:28pm  May 6, 2015 11:28pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

Just for sharing, the reason why I'm choosing "that" broker over the others...  
  
The reason behind is because of slippage. Yes, that f**king slippage.  
When you do a test on demo account, performance seems good, and orders are properly executed at the requested price. Orders was executed faster, and all, and all....  
But when you start doing it on live account, performance is very bad, and orders got a quite big slippage. This BIG slippage is even applies for limit orders and stop orders, and even applies when you set slippage to zero or no slippage to the order. I'm a bit disappointed with the other brokers, and this slippage seems unacceptable.  
  
But so far, "that" broker seems ok even with live account. Performance is over the bar, and slippage is not too disappointing.  
  
My 50 cents: please be careful when you start trading with live account.Do recognize your broker, including slippage. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#329](/thread/post/8248192#post8248192 "Post Permalink")

  * May 7, 2015 1:12am  May 7, 2015 1:12am 

  * [ slianto](slianto)

  * | Joined Feb 2015  | Status: Trader | [180 Posts](/search?do=process&provider=Member&searchuser=399331)

Hi radityo!  
I would like to know about the set files configuration, your SNR setting is for 5digits broker right?  
I wanna try it on 4 digits broker, is there another variable do I need to change beside this?:  
  
MartingaleGap=100 -> change to 10  
PointsTarget=200 -> change to 20  
PointsLoss=200 -> change to 20  
  
I will play around with another variable later, just want to make sure i'm on the correct track to try this at 4 digits broker..  
  
  
and for your another EA, I'll support that. Hope together we will fix the bugs and build better EA.  
  
thanks! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#330](/thread/post/8249601#post8249601 "Post Permalink")

  * May 7, 2015 6:03pm  May 7, 2015 6:03pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting slianto](/thread/post/8248192#post8248192 "View Quoted Post")
> 
> Disliked
> 
> Hi radityo! I would like to know about the set files configuration, your SNR setting is for 5digits broker right? I wanna try it on 4 digits broker, is there another variable do I need to change beside this?: MartingaleGap=100 -> change to 10 PointsTarget=200 -> change to 20 PointsLoss=200 -> change to 20 I will play around with another variable later, just want to make sure i'm on the correct track to try this at 4 digits broker.. and for your another EA, I'll support that. Hope together we will fix the bugs and build better EA. thanks!
> 
> Ignored

Yes, you are correct. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#331](/thread/post/8251339#post8251339 "Post Permalink")

  * May 8, 2015 11:50am  May 8, 2015 11:50am 

  * [ slianto](slianto)

  * | Joined Feb 2015  | Status: Trader | [180 Posts](/search?do=process&provider=Member&searchuser=399331)

> [Quoting radityo.ardi](/thread/post/8249601#post8249601 "View Quoted Post")
> 
> Disliked
> 
> {quote} Yes, you are correct.
> 
> Ignored

thank you!  
and what happened to your trade explorer. SNR also lost.  
why in a sudden it place 33lots? and it took a big hit -6000 or so.. >.<

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#332](/thread/post/8251460#post8251460 "Post Permalink")

  * May 8, 2015 2:19pm  May 8, 2015 2:19pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting slianto](/thread/post/8251339#post8251339 "View Quoted Post")
> 
> Disliked
> 
> {quote} thank you! and what happened to your trade explorer. SNR also lost. why in a sudden it place 33lots? and it took a big hit -6000 or so.. >.<
> 
> Ignored

![](https://resources.faireconomy.media/images/emojis/64/1f937-200d-2642-fe0f.png?v=15.1)  
33 lots was because of the market didn't move much at that time. This is the main dangerous issue with martingale tunnel, and I do recognize that since the first loss of my demo account. It was not suppose to execute many cycles in a day. Though my SNR is for 4 cycles a day, maybe I should mark down the setting to 1 cycle a day. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#333](/thread/post/8254301#post8254301 "Post Permalink")

  * Edited 8:15am  May 11, 2015 7:13am | Edited 8:15am 

  * [ TickJob](tickjob)

  * | Joined Apr 2007  | Status: Trader | [166 Posts](/search?do=process&provider=Member&searchuser=37449)

> [Quoting radityo.ardi](/thread/post/8216673#post8216673 "View Quoted Post")
> 
> Disliked
> 
> {quote} I've uploaded the fixes. v1.094 - Fix for Max Cycle Count
> 
> Ignored

I downloaded from the first page it show 1.091(TunnelMartingale.mq4 ...28 Mar). Where can I download the latest version? 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: pic2.jpg
Size: 66 KB](/attachment/image/1671573/thumbnail?d=1431299706)](/attachment/image/1671573?d=1431299706)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#334](/thread/post/8254306#post8254306 "Post Permalink")

  * Edited 7:49am  May 11, 2015 7:24am | Edited 7:49am 

  * [ TickJob](tickjob)

  * | Joined Apr 2007  | Status: Trader | [166 Posts](/search?do=process&provider=Member&searchuser=37449)

> [Quoting radityo.ardi](/thread/post/8251460#post8251460 "View Quoted Post")
> 
> Disliked
> 
> {quote} ![](https://resources.faireconomy.media/images/emojis/64/1f937-200d-2642-fe0f.png?v=15.1) 33 lots was because of the market didn't move much at that time. This is the main dangerous issue with martingale tunnel, and I do recognize that since the first loss of my demo account. It was not suppose to execute many cycles in a day. Though my SNR is for 4 cycles a day, maybe I should mark down the setting to 1 cycle a day.
> 
> Ignored

Hi Bro,  
This EA should only be used by selecting the right entry point in which the market start to move away from ranging, never mind which direction, the bigger the move the better, even choppy also welcomed as long as it move more than 2-3 times your gap setting.  
  
NEVER NEVER NEVER let it run automatically blindly throughout any time period, unless the EA can automatically identify the big move and then start the cycles(we do NOT need to catch the very beginning of the move). For testing and exploring is OK to let it run automatically, BUT actually no point to test it this way, because we know that it sure fail at certain point when stay in ranging long enough. We should put our efford in improving our entry point, either manually or automatically.  
  
Your suggestion to start the cycle at X price in version 1.10 is the very suitable feature for this startegy. Looking forward to have this feature soon.  
  
Thank you. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#335](/thread/post/8254341#post8254341 "Post Permalink")

  * May 11, 2015 8:00am  May 11, 2015 8:00am 

  * [ TickJob](tickjob)

  * | Joined Apr 2007  | Status: Trader | [166 Posts](/search?do=process&provider=Member&searchuser=37449)

Please see attached screenshot below, how come I have these funny characters in the mq4 file? 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: pic1.jpg
Size: 88 KB](/attachment/image/1671564/thumbnail?d=1431298847)](/attachment/image/1671564?d=1431298847)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#336](/thread/post/8255199#post8255199 "Post Permalink")

  * May 11, 2015 8:17pm  May 11, 2015 8:17pm 

  * [ TickJob](tickjob)

  * | Joined Apr 2007  | Status: Trader | [166 Posts](/search?do=process&provider=Member&searchuser=37449)

Could someone advise how to modify the EA to add "Manual Mode" to start every cycle as shown the following screenshot. When EA running, it display BUY, SELL, STOP buttons.  
1\. press either BUY or SELL to start the cycle,  
2\. while the cycle is running(1,2,4...), we can press STOP button to close all position.  
3\. Repeat 1 after cycle automatically stop with profit or manually stop. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: pic1.jpg
Size: 161 KB](/attachment/image/1671856/thumbnail?d=1431342998)](/attachment/image/1671856?d=1431342998)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#337](/thread/post/8255454#post8255454 "Post Permalink")

  * May 11, 2015 10:05pm  May 11, 2015 10:05pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

I have started new thread for another Grid EA as promised. Please read through and comment there.  
  
<http://www.forexfactory.com/showthread.php?p=8255445>

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#338](/thread/post/8256480#post8256480 "Post Permalink")

  * Edited 2:22pm  May 12, 2015 12:06pm | Edited 2:22pm 

  * [ slianto](slianto)

  * | Joined Feb 2015  | Status: Trader | [180 Posts](/search?do=process&provider=Member&searchuser=399331)

> [Quoting TickJob](/thread/post/8254306#post8254306 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi Bro, This EA should only be used by selecting the right entry point in which the market start to move away from ranging, never mind which direction, the bigger the move the better, even choppy also welcomed as long as it move more than 2-3 times your gap setting. NEVER NEVER NEVER let it run automatically blindly throughout any time period, unless the EA can automatically identify the big move and then start the cycles(we do NOT need to catch the very beginning of the move). For testing and exploring is OK to let it run automatically,...
> 
> Ignored

Good idea, or we could try this:  
1\. Run this EA on the most volatile pairs ( could be the Beast GBP/NZD or the Dragon GBP/JPY or anything else )  
2\. Turn on this EA only during London Open till London Close 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#339](/thread/post/8256582#post8256582 "Post Permalink")

  * May 12, 2015 2:11pm  May 12, 2015 2:11pm 

  * [ TickJob](tickjob)

  * | Joined Apr 2007  | Status: Trader | [166 Posts](/search?do=process&provider=Member&searchuser=37449)

Today just start testing the "Start Any Time" version. First cycle go up to 32. Second cycle seem to have problem, it does not execute 0.08 lots Buy-Stop order. What is the problem? 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: buy1.jpg
Size: 267 KB](/attachment/image/1672348/thumbnail?d=1431407446)](/attachment/image/1672348?d=1431407446)   
[![Click to Enlarge

Name: buy2.jpg
Size: 134 KB](/attachment/image/1672349/thumbnail?d=1431407462)](/attachment/image/1672349?d=1431407462)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#340](/thread/post/8256597#post8256597 "Post Permalink")

  * May 12, 2015 2:23pm  May 12, 2015 2:23pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting TickJob](/thread/post/8256582#post8256582 "View Quoted Post")
> 
> Disliked
> 
> Today just start testing the "Start Any Time" version. First cycle go up to 32. Second cycle seem to have problem, it does not execute 0.08 lots Buy-Stop order. What is the problem? {image} {image}
> 
> Ignored

This is the old classic issue. When you set the Gaps too low, and the price like going up and down in less than 1 second within the gap, actually EA is trying to open BUY STOP order, but it was too late, the price already moving upwards.  
  
I'm hardly agree with the idea of button. but I don't have any reference how to do that. MQL4 is very limited if we want to implement a button. probably we can play with Global Variables? 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Trapping System: Tunnel Martingale
  *   * [ **Reply to Thread** ](/thread/524198-trapping-system-tunnel-martingale/reply#reply)

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

[Martingale, Anti-martingale, and Compounding](/thread/571233-martingale-anti-martingale-and-compounding "Hi all traders, 
i started this thread to meet others people interested in money management. 
We all know that martingale strategies are...") 40 replies

[Martingale, Reverse Martingale, Modified Martingale, Maths](/thread/736165-martingale-reverse-martingale-modified-martingale-maths "Hi all, so Martingale has been a risky yet maybe non profitable system. While roulette has an edge of \(2.7%/5.4%\) 
  
Inspired by Adam...") 1 reply

[How to change this Martingale to Reverse Martingale ?](/thread/546755-how-to-change-this-martingale-to-reverse-martingale "How to change this Martingale to Reverse Martingale ?") 3 replies

[Trapping System: Way to Fully-Automated Trading System](/thread/509226-trapping-system-way-to-fully-automated-trading-system "Hi fellow Traders! 
This is my first time to write a new thread. Would like to share a trading method, which at least made me happy right...") 47 replies

[Martingale vs. Non Martingale (Simplified RoR vs Profit)](/thread/526308-martingale-vs-non-martingale-simplified-ror-vs-profit "Martingale: The gambler doubles his bet after every loss... 
  
Martingale vs. Non Martingale \(Simplified RoR vs Profit in 3 trade runs...") 1 reply

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/524198-trapping-system-tunnel-martingale/reply#reply)
  * Subscribe
  * [221](javascript:void\(0\);)

Attachments: Trapping System: Tunnel Martingale

Tags: Trapping System: Tunnel Martingale

#  [](/thread/524198-trapping-system-tunnel-martingale)Trapping System: Tunnel Martingale 

  * 

  * [#341](/thread/post/8256694#post8256694 "Post Permalink")

  * Edited 4:08pm  May 12, 2015 3:26pm | Edited 4:08pm 

  * [ TickJob](tickjob)

  * | Joined Apr 2007  | Status: Trader | [166 Posts](/search?do=process&provider=Member&searchuser=37449)

Thank you for your answer.  
  
I try to SELL first(StartFrom=1) when EA start, it works!  
So actually I can have Buy.set and Sell.set file. and stop every 1 cycle, don't need button. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: pic292.jpg
Size: 257 KB](/attachment/image/1672427/thumbnail?d=1431414530)](/attachment/image/1672427?d=1431414530)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#342](/thread/post/8256864#post8256864 "Post Permalink")

  * Edited 5:20pm  May 12, 2015 4:51pm | Edited 5:20pm 

  * [ TickJob](tickjob)

  * | Joined Apr 2007  | Status: Trader | [166 Posts](/search?do=process&provider=Member&searchuser=37449)

Now I use Gap=100point(10pips), it also miss the 0.32 orders. Journal did not show the program execute 0.32 orders. Anyway to overcome it?  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: pic382.jpg
Size: 259 KB](/attachment/image/1672451/thumbnail?d=1431417078)](/attachment/image/1672451?d=1431417078)   

  
  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: pic10101.jpg
Size: 268 KB](/attachment/image/1672487/thumbnail?d=1431418756)](/attachment/image/1672487?d=1431418756)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#343](/thread/post/8256948#post8256948 "Post Permalink")

  * Edited 5:30pm  May 12, 2015 5:16pm | Edited 5:30pm 

  * [ TickJob](tickjob)

  * | Joined Apr 2007  | Status: Trader | [166 Posts](/search?do=process&provider=Member&searchuser=37449)

Another problem  
I set the Gap =100 points, ProfitTarget=2.00,  
The Breakeven at 1.12388, and Profit at 1.12438 seem incorrect?  
  
  
txt01=[COMMON]  
StartType=1  
ProfitLineColor=65535  
BreakEvenCheckIntv=5  
TextColor=55295  
UpperGapPriceColor=13382297  
LowerGapPriceColor=36095  
TextSize=8  
MagicNumber=8081  
LineStyle=0  
LineWidth=1  
LineHeight=13  
DateTimeType=0  
DailyStartTime=01:00:00  
DailyStopTime=00:00:00  
CommentInfo=TUNNELMARTINGALE  
txt05=[SLIPPAGE]  
UseSlippage=false  
ClosingSlippage=0  
OpeningSlippage=0  
txt02=[LOT(S)]  
StartAmountType=1  
StartDynamicAmount=0.000002  
StartFixedAmount=0.02  
txt03=[MARTINGALE]  
MartingaleFactor=1,2,4  
MaxMartingaleFactor=25  
FactorMultiplier=2.0  
FactorOperator=0  
MartingaleGap=100  
MaxMartingaleCycle=1  
txt04=[TARGET]  
TargetType=0  
TrailingTargetType=0  
ProfitTarget=2.00  
ProfitTargetMultiplier=0.0001  
TrailingTarget=10.0  
TrailingTargetMultiplier=0.002  
UseProfitLoss=false  
ProfitLoss=-9999999.0  
ProfitLossMultiplier=-9999999.0  
PointsTargetType=0  
PointsTarget=20  
PointsLoss=100  
PointsTargetColor=32768  
PointsLossColor=16711935  
txt06=[START ANYTIME]  
StartFrom=1  
StartNextFrom=0  
txt07=[START SUPPORT & RESISTANCE]  
PivotColor=8388736  
SNR1Color=65535  
SupResRecTime=09:00  
txt08=[START DAILY HIGH LOW & X-Points]  
HighLowColor=13959039  
DailyHighLowRecTime=14:00  
AnchorPrice=0  
XPointsTrigger=10  
txt09=[START SNR, HI-LO, XPoints]  
OrderDirection=0  
txt99=[DEBUG]  
IsDebug=false  
IsDevelopment=false  
TimeRange=30 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: pic733.jpg
Size: 137 KB](/attachment/image/1672482/thumbnail?d=1431418586)](/attachment/image/1672482?d=1431418586)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#344](/thread/post/8257337#post8257337 "Post Permalink")

  * May 12, 2015 7:19pm  May 12, 2015 7:19pm 

  * [ TickJob](tickjob)

  * | Joined Apr 2007  | Status: Trader | [166 Posts](/search?do=process&provider=Member&searchuser=37449)

I test it on another broker platform. Same problem, the 5th orders not submitting out. 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: pix238.jpg
Size: 288 KB](/attachment/image/1672632/thumbnail?d=1431425956)](/attachment/image/1672632?d=1431425956)   
[![Click to Enlarge

Name: pic923.jpg
Size: 271 KB](/attachment/image/1672633/thumbnail?d=1431425971)](/attachment/image/1672633?d=1431425971)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#345](/thread/post/8258731#post8258731 "Post Permalink")

  * May 13, 2015 10:41am  May 13, 2015 10:41am 

  * [ TickJob](tickjob)

  * | Joined Apr 2007  | Status: Trader | [166 Posts](/search?do=process&provider=Member&searchuser=37449)

found a bug  
Buy first (StartFrom=0) , it can go to 5th order.  
Sell first (StartFrom=1), it can NOT go to 5th order, EA hanged!

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: buy-first1.jpg
Size: 76 KB](/attachment/image/1673080/thumbnail?d=1431481230)](/attachment/image/1673080?d=1431481230)   
[![Click to Enlarge

Name: Sell-first1.jpg
Size: 49 KB](/attachment/image/1673081/thumbnail?d=1431481244)](/attachment/image/1673081?d=1431481244)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#346](/thread/post/8258884#post8258884 "Post Permalink")

  * May 13, 2015 2:43pm  May 13, 2015 2:43pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting TickJob](/thread/post/8258731#post8258731 "View Quoted Post")
> 
> Disliked
> 
> found a bug Buy first (StartFrom=0) , it can go to 5th order. Sell first (StartFrom=1), it can NOT go to 5th order, EA hanged! {image} {image}
> 
> Ignored

ok, will check it out sometime today. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#347](/thread/post/8259198#post8259198 "Post Permalink")

  * May 13, 2015 5:43pm  May 13, 2015 5:43pm 

  * [ TickJob](tickjob)

  * | Joined Apr 2007  | Status: Trader | [166 Posts](/search?do=process&provider=Member&searchuser=37449)

> [Quoting radityo.ardi](/thread/post/8258884#post8258884 "View Quoted Post")
> 
> Disliked
> 
> {quote} ok, will check it out sometime today.
> 
> Ignored

Thank you radityo.  
  
just another one happended, stop at 5th order, cannot submit 6th order, EA hanged also.  
this time cycle start buy first(StartFrom=0).  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: 16trya.jpg
Size: 278 KB](/attachment/image/1673262/thumbnail?d=1431506594)](/attachment/image/1673262?d=1431506594)   

  
  
txt01=[COMMON]  
StartType=1  
ProfitLineColor=65535  
BreakEvenCheckIntv=5  
TextColor=55295  
UpperGapPriceColor=13382297  
LowerGapPriceColor=36095  
TextSize=8  
MagicNumber=8080  
LineStyle=0  
LineWidth=1  
LineHeight=13  
DateTimeType=0  
DailyStartTime=01:00:00  
DailyStopTime=00:00:00  
CommentInfo=TUNNELMARTINGALE  
txt05=[SLIPPAGE]  
UseSlippage=false  
ClosingSlippage=0  
OpeningSlippage=0  
txt02=[LOT(S)]  
StartAmountType=1  
StartDynamicAmount=0.000002  
StartFixedAmount=0.01  
txt03=[MARTINGALE]  
MartingaleFactor=1,2,4  
MaxMartingaleFactor=25  
FactorMultiplier=2.0  
FactorOperator=0  
MartingaleGap=50  
MaxMartingaleCycle=0  
txt04=[TARGET]  
TargetType=0  
TrailingTargetType=0  
ProfitTarget=0.50  
ProfitTargetMultiplier=0.0001  
TrailingTarget=10.0  
TrailingTargetMultiplier=0.002  
UseProfitLoss=false  
ProfitLoss=-9999999.0  
ProfitLossMultiplier=-9999999.0  
PointsTargetType=0  
PointsTarget=20  
PointsLoss=100  
PointsTargetColor=32768  
PointsLossColor=16711935  
txt06=[START ANYTIME]  
StartFrom=0  
StartNextFrom=0  
txt07=[START SUPPORT & RESISTANCE]  
PivotColor=8388736  
SNR1Color=65535  
SupResRecTime=09:00  
txt08=[START DAILY HIGH LOW & X-Points]  
HighLowColor=13959039  
DailyHighLowRecTime=14:00  
AnchorPrice=0  
XPointsTrigger=10  
txt09=[START SNR, HI-LO, XPoints]  
OrderDirection=0  
txt99=[DEBUG]  
IsDebug=false  
IsDevelopment=false  
TimeRange=30 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#348](/thread/post/8259438#post8259438 "Post Permalink")

  * May 13, 2015 7:13pm  May 13, 2015 7:13pm 

  * [ TickJob](tickjob)

  * | Joined Apr 2007  | Status: Trader | [166 Posts](/search?do=process&provider=Member&searchuser=37449)

Another happening, stop at 6th order, 7th order hanged.  
I think the problem is not how many order. The main problem is EA hanged. May not due to the EA. Could it be my computer or network problem? Or maybe is the broker problem? but I tried two different brokers, [oanda](/brokers/oanda "View OANDA Broker Profile") and IC martket, both also encountered EA hanged often. So unlikely is brokers problem?

Attached Image (click to enlarge)

[![Click to Enlarge

Name: 32hanged.jpg
Size: 263 KB](/attachment/image/1673333/thumbnail?d=1431511940)](/attachment/image/1673333?d=1431511940)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#349](/thread/post/8259618#post8259618 "Post Permalink")

  * May 13, 2015 8:29pm  May 13, 2015 8:29pm 

  * [ TickJob](tickjob)

  * | Joined Apr 2007  | Status: Trader | [166 Posts](/search?do=process&provider=Member&searchuser=37449)

The test result is attached below.   
So far my problem is EA hanged.   
  
<http://www.fengshui-bank.com/Statement2.htm>

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#350](/thread/post/8259704#post8259704 "Post Permalink")

  * May 13, 2015 9:06pm  May 13, 2015 9:06pm 

  * [ TickJob](tickjob)

  * | Joined Apr 2007  | Status: Trader | [166 Posts](/search?do=process&provider=Member&searchuser=37449)

This time can go up to 64lots but the EA failed to take profit when reach/exceed target. My profit target is $0.5, and it already has $3.15 profit.  
Maybe hanged already.

Attached Image (click to enlarge)

[![Click to Enlarge

Name: 222222.jpg
Size: 280 KB](/attachment/image/1673412/thumbnail?d=1431518758)](/attachment/image/1673412?d=1431518758)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#351](/thread/post/8259719#post8259719 "Post Permalink")

  * May 13, 2015 9:14pm  May 13, 2015 9:14pm 

  * [ TickJob](tickjob)

  * | Joined Apr 2007  | Status: Trader | [166 Posts](/search?do=process&provider=Member&searchuser=37449)

I remove the EA, and it show blank window, by right EA will open a window to ask me to proceed to close all position or not. so confirm EA hanged already. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: 231231.jpg
Size: 146 KB](/attachment/image/1673417/thumbnail?d=1431519239)](/attachment/image/1673417?d=1431519239)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#352](/thread/post/8259770#post8259770 "Post Permalink")

  * May 13, 2015 9:33pm  May 13, 2015 9:33pm 

  * [ TickJob](tickjob)

  * | Joined Apr 2007  | Status: Trader | [166 Posts](/search?do=process&provider=Member&searchuser=37449)

Very interesting,   
spike also work!

Attached Image (click to enlarge)

[![Click to Enlarge

Name: asds.jpg
Size: 293 KB](/attachment/image/1673432/thumbnail?d=1431520411)](/attachment/image/1673432?d=1431520411)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#353](/thread/post/8260959#post8260959 "Post Permalink")

  * May 14, 2015 6:36am  May 14, 2015 6:36am 

  * [ TickJob](tickjob)

  * | Joined Apr 2007  | Status: Trader | [166 Posts](/search?do=process&provider=Member&searchuser=37449)

Let's it run over night, still running, did not hanged, max number of lots 0.08 (4th order).  
  
Hence, the problem now is to find out what cause it to hanged at higher order?  
  
Result as shown: <http://www.fengshui-bank.com/Statement3.htm>

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#354](/thread/post/8261153#post8261153 "Post Permalink")

  * May 14, 2015 10:28am  May 14, 2015 10:28am 

  * [ TickJob](tickjob)

  * | Joined Apr 2007  | Status: Trader | [166 Posts](/search?do=process&provider=Member&searchuser=37449)

hanged again at 5th order !  
Trade Records: <http://www.fengshui-bank.com/Statement5.htm>

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: xsssx.jpg
Size: 271 KB](/attachment/image/1673892/thumbnail?d=1431566879)](/attachment/image/1673892?d=1431566879)   
[![Click to Enlarge

Name: scdcd.jpg
Size: 228 KB](/attachment/image/1673894/thumbnail?d=1431567047)](/attachment/image/1673894?d=1431567047)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#355](/thread/post/8261466#post8261466 "Post Permalink")

  * May 14, 2015 3:01pm  May 14, 2015 3:01pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

ok. I think let me try on your other broker, same as you.  
I believe this issue is due to the many factors related to broker. I do experienced it with my old broker (AGEA). This tunnel martingale can't be attached to that broker, due to its high spread, and so many slippage applied. So this factor affecting the EA operation (I do experienced this, that is why I moved to [Tickmill](/brokers/tickmill "View Tickmill Broker Profile"), since it is more stable).  
  
Please test on your side with Tickmill, either Classic or Exchange account. Meanwhile, let me test overnight with your [IC Markets](/brokers/ic-markets "View IC Markets Broker Profile") and Oanda. I will test it on my VPS and see tomorrow. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#356](/thread/post/8262325#post8262325 "Post Permalink")

  * May 14, 2015 7:48pm  May 14, 2015 7:48pm 

  * [ TickJob](tickjob)

  * | Joined Apr 2007  | Status: Trader | [166 Posts](/search?do=process&provider=Member&searchuser=37449)

> [Quoting radityo.ardi](/thread/post/8261466#post8261466 "View Quoted Post")
> 
> Disliked
> 
> ok. I think let me try on your other broker, same as you. I believe this issue is due to the many factors related to broker. I do experienced it with my old broker (AGEA). This tunnel martingale can't be attached to that broker, due to its high spread, and so many slippage applied. So this factor affecting the EA operation (I do experienced this, that is why I moved to Tickmill, since it is more stable). Please test on your side with Tickmill, either Classic or Exchange account. Meanwhile, let me test overnight with your IC Markets and Oanda. I...
> 
> Ignored

Thanks Radityo.  
Just got Tickmill demo running. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: xccsS.jpg
Size: 288 KB](/attachment/image/1674240/thumbnail?d=1431600506)](/attachment/image/1674240?d=1431600506)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#357](/thread/post/8262387#post8262387 "Post Permalink")

  * May 14, 2015 8:12pm  May 14, 2015 8:12pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting TickJob](/thread/post/8262325#post8262325 "View Quoted Post")
> 
> Disliked
> 
> {quote} Thanks Radityo. Just got Tickmill demo running. {image}
> 
> Ignored

I'm testing your IC markets, with the same setting as [http://www.forexfactory.com/showthre...98#post8259198](http://www.forexfactory.com/showthread.php?p=8259198#post8259198)  
  
Only change from my side is:  
time: 00:00:00 to 23:59:59  
and Gaps I set to 100  
We'll see... 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#358](/thread/post/8262477#post8262477 "Post Permalink")

  * May 14, 2015 8:43pm  May 14, 2015 8:43pm 

  * [ TickJob](tickjob)

  * | Joined Apr 2007  | Status: Trader | [166 Posts](/search?do=process&provider=Member&searchuser=37449)

> [Quoting radityo.ardi](/thread/post/8261466#post8261466 "View Quoted Post")
> 
> Disliked
> 
> ok. I think let me try on your other broker, same as you. I believe this issue is due to the many factors related to broker. I do experienced it with my old broker (AGEA). This tunnel martingale can't be attached to that broker, due to its high spread, and so many slippage applied. So this factor affecting the EA operation (I do experienced this, that is why I moved to Tickmill, since it is more stable). Please test on your side with Tickmill, either Classic or Exchange account. Meanwhile, let me test overnight with your IC Markets and Oanda. I...
> 
> Ignored

Attached Image (click to enlarge)

[![Click to Enlarge

Name: saASDSF.jpg
Size: 292 KB](/attachment/image/1674286/thumbnail?d=1431603761)](/attachment/image/1674286?d=1431603761)   

  
  
I tried Tickmill a while only HANGED!  
My profit target $0.5, EA hanged, cannot take profit. I did manually take profit.  
  
trading record: <http://www.fengshui-bank.com/Statement7.htm>

Attached Image (click to enlarge)

[![Click to Enlarge

Name: SDVDFVDFV.jpg
Size: 246 KB](/attachment/image/1674287/thumbnail?d=1431603794)](/attachment/image/1674287?d=1431603794)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#359](/thread/post/8262612#post8262612 "Post Permalink")

  * May 14, 2015 9:34pm  May 14, 2015 9:34pm 

  * [ TickJob](tickjob)

  * | Joined Apr 2007  | Status: Trader | [166 Posts](/search?do=process&provider=Member&searchuser=37449)

Tickmill Hanged again!

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: sdvsvs.jpg
Size: 296 KB](/attachment/image/1674322/thumbnail?d=1431606862)](/attachment/image/1674322?d=1431606862)   
[![Click to Enlarge

Name: sascas.jpg
Size: 229 KB](/attachment/image/1674326/thumbnail?d=1431606952)](/attachment/image/1674326?d=1431606952)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#360](/thread/post/8262681#post8262681 "Post Permalink")

  * May 14, 2015 9:53pm  May 14, 2015 9:53pm 

  * [ TickJob](tickjob)

  * | Joined Apr 2007  | Status: Trader | [166 Posts](/search?do=process&provider=Member&searchuser=37449)

Tickmill another hanged  
4th order already hanged  
  
I do manually take profit, much more than target $0.5, haha  
  
will change back to ICMarkets to compare.

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: sascascasa.jpg
Size: 241 KB](/attachment/image/1674348/thumbnail?d=1431607931)](/attachment/image/1674348?d=1431607931)   
[![Click to Enlarge

Name: sdcsds.jpg
Size: 63 KB](/attachment/image/1674349/thumbnail?d=1431607977)](/attachment/image/1674349?d=1431607977)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Trapping System: Tunnel Martingale
  *   * [ **Reply to Thread** ](/thread/524198-trapping-system-tunnel-martingale/reply#reply)

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

[Martingale, Anti-martingale, and Compounding](/thread/571233-martingale-anti-martingale-and-compounding "Hi all traders, 
i started this thread to meet others people interested in money management. 
We all know that martingale strategies are...") 40 replies

[Martingale, Reverse Martingale, Modified Martingale, Maths](/thread/736165-martingale-reverse-martingale-modified-martingale-maths "Hi all, so Martingale has been a risky yet maybe non profitable system. While roulette has an edge of \(2.7%/5.4%\) 
  
Inspired by Adam...") 1 reply

[How to change this Martingale to Reverse Martingale ?](/thread/546755-how-to-change-this-martingale-to-reverse-martingale "How to change this Martingale to Reverse Martingale ?") 3 replies

[Trapping System: Way to Fully-Automated Trading System](/thread/509226-trapping-system-way-to-fully-automated-trading-system "Hi fellow Traders! 
This is my first time to write a new thread. Would like to share a trading method, which at least made me happy right...") 47 replies

[Martingale vs. Non Martingale (Simplified RoR vs Profit)](/thread/526308-martingale-vs-non-martingale-simplified-ror-vs-profit "Martingale: The gambler doubles his bet after every loss... 
  
Martingale vs. Non Martingale \(Simplified RoR vs Profit in 3 trade runs...") 1 reply

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/524198-trapping-system-tunnel-martingale/reply#reply)
  * Subscribe
  * [221](javascript:void\(0\);)

Attachments: Trapping System: Tunnel Martingale

Tags: Trapping System: Tunnel Martingale

#  [](/thread/524198-trapping-system-tunnel-martingale)Trapping System: Tunnel Martingale 

  * 

  * [#361](/thread/post/8262704#post8262704 "Post Permalink")

  * May 14, 2015 10:04pm  May 14, 2015 10:04pm 

  * [ TickJob](tickjob)

  * | Joined Apr 2007  | Status: Trader | [166 Posts](/search?do=process&provider=Member&searchuser=37449)

ICmarket also hanged at 4th order.  
Look like the hanged is related to market price changing very fast during opening?  
But then, why only this EA hanged, other EA do not hanged?  
Why EA on my computer hanged, Radityo computer does not hanged?

Attached Image (click to enlarge)

[![Click to Enlarge

Name: csdsdc.jpg
Size: 291 KB](/attachment/image/1674355/thumbnail?d=1431608649)](/attachment/image/1674355?d=1431608649)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#362](/thread/post/8263029#post8263029 "Post Permalink")

  * May 14, 2015 11:57pm  May 14, 2015 11:57pm 

  * [ TickJob](tickjob)

  * | Joined Apr 2007  | Status: Trader | [166 Posts](/search?do=process&provider=Member&searchuser=37449)

ICMarkets hanged again at 4th order.  
But why MT4 still working fine, I still can continue to add lots and take profit manually? It means everything (except the EA) is working fine?

Attached Image (click to enlarge)

[![Click to Enlarge

Name: kjhjkhkj.jpg
Size: 82 KB](/attachment/image/1674481/thumbnail?d=1431615391)](/attachment/image/1674481?d=1431615391)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#363](/thread/post/8264016#post8264016 "Post Permalink")

  * May 15, 2015 3:15pm  May 15, 2015 3:15pm 

  * [ TickJob](tickjob)

  * | Joined Apr 2007  | Status: Trader | [166 Posts](/search?do=process&provider=Member&searchuser=37449)

This morning I run the EA on 2 other computers so far have no problem. But my computer hanged. So can confirm now is my computer problem. Maybe too old already, coming to 10 years.

Attached Image

![](/attachment/image/1674780?d=1431670549)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#364](/thread/post/8264083#post8264083 "Post Permalink")

  * May 15, 2015 3:50pm  May 15, 2015 3:50pm 

  * [ TickJob](tickjob)

  * | Joined Apr 2007  | Status: Trader | [166 Posts](/search?do=process&provider=Member&searchuser=37449)

so far my highest = 13th.

Attached Image (click to enlarge)

[![Click to Enlarge

Name: 13th.jpg
Size: 311 KB](/attachment/image/1674796/thumbnail?d=1431672625)](/attachment/image/1674796?d=1431672625)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#365](/thread/post/8264338#post8264338 "Post Permalink")

  * May 15, 2015 5:33pm  May 15, 2015 5:33pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

I confirmed it stopped on my [IC Markets](/brokers/ic-markets "View IC Markets Broker Profile") even with VPS. Need to see why... but [tickmill](/brokers/tickmill "View Tickmill Broker Profile") so far I've never experienced one, except for the latency issue in internet connection. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#366](/thread/post/8264491#post8264491 "Post Permalink")

  * May 15, 2015 6:30pm  May 15, 2015 6:30pm 

  * [ TickJob](tickjob)

  * | Joined Apr 2007  | Status: Trader | [166 Posts](/search?do=process&provider=Member&searchuser=37449)

> [Quoting radityo.ardi](/thread/post/8264338#post8264338 "View Quoted Post")
> 
> Disliked
> 
> I confirmed it stopped on my IC Markets even with VPS. Need to see why... but tickmill so far I've never experienced one, except for the latency issue in internet connection.
> 
> Ignored

so now seem to have two issues: computer and brokers

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#367](/thread/post/8264681#post8264681 "Post Permalink")

  * Edited 9:08pm  May 15, 2015 7:44pm | Edited 9:08pm 

  * [ TickJob](tickjob)

  * | Joined Apr 2007  | Status: Trader | [166 Posts](/search?do=process&provider=Member&searchuser=37449)

Hi Radityo,  
  
I could not find the option of setting the following as shown in the screeenshot, how to do it?  
These few days I observed many many cases, start the next cycle in reversed direction is safer.  
For example, if up, buy-lots will take profit, then the next cycle should start Sell-First. Usually after running up(or down) some pips, it will stay in range for sometime, but don't know how long, that is more dangerous part. We are not worry if the price keep on up up up, this strategy will sure win some pips even the next cycle is in reversed direction at start.  
  
If we reversed the Buy-Sell direction ranging portion become profitable, no danger!

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: sasaas.jpg
Size: 122 KB](/attachment/image/1674954/thumbnail?d=1431686620)](/attachment/image/1674954?d=1431686620)   
[![Click to Enlarge

Name: ssss.jpg
Size: 114 KB](/attachment/image/1674979/thumbnail?d=1431687988)](/attachment/image/1674979?d=1431687988)   
[![Click to Enlarge

Name: csdcsdc.jpg
Size: 159 KB](/attachment/image/1674986/thumbnail?d=1431688333)](/attachment/image/1674986?d=1431688333)   
[![Click to Enlarge

Name: dfasas.jpg
Size: 159 KB](/attachment/image/1674995/thumbnail?d=1431689038)](/attachment/image/1674995?d=1431689038)   
[![Click to Enlarge

Name: dssdcd.jpg
Size: 167 KB](/attachment/image/1675003/thumbnail?d=1431690392)](/attachment/image/1675003?d=1431690392)   
[![Click to Enlarge

Name: scddsc.jpg
Size: 152 KB](/attachment/image/1675010/thumbnail?d=1431690870)](/attachment/image/1675010?d=1431690870)   
[![Click to Enlarge

Name: sdasdas.jpg
Size: 154 KB](/attachment/image/1675017/thumbnail?d=1431691214)](/attachment/image/1675017?d=1431691214)   
[![Click to Enlarge

Name: dsdcds.jpg
Size: 145 KB](/attachment/image/1675018/thumbnail?d=1431691244)](/attachment/image/1675018?d=1431691244)   
[![Click to Enlarge

Name: sdcsdcs.jpg
Size: 150 KB](/attachment/image/1675025/thumbnail?d=1431691729)](/attachment/image/1675025?d=1431691729)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#368](/thread/post/8264865#post8264865 "Post Permalink")

  * Edited 9:48pm  May 15, 2015 9:21pm | Edited 9:48pm 

  * [ TickJob](tickjob)

  * | Joined Apr 2007  | Status: Trader | [166 Posts](/search?do=process&provider=Member&searchuser=37449)

continiue.... 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: vdsdssdcds.jpg
Size: 201 KB](/attachment/image/1675034/thumbnail?d=1431692451)](/attachment/image/1675034?d=1431692451)   
[![Click to Enlarge

Name: vdsvsdvs.jpg
Size: 204 KB](/attachment/image/1675037/thumbnail?d=1431692630)](/attachment/image/1675037?d=1431692630)   
[![Click to Enlarge

Name: dsfdsfs.jpg
Size: 158 KB](/attachment/image/1675042/thumbnail?d=1431692782)](/attachment/image/1675042?d=1431692782)   
[![Click to Enlarge

Name: 34f3.jpg
Size: 177 KB](/attachment/image/1675046/thumbnail?d=1431693097)](/attachment/image/1675046?d=1431693097)   
[![Click to Enlarge

Name: 34r43.jpg
Size: 179 KB](/attachment/image/1675049/thumbnail?d=1431693229)](/attachment/image/1675049?d=1431693229)   
[![Click to Enlarge

Name: dsc3.jpg
Size: 183 KB](/attachment/image/1675053/thumbnail?d=1431693425)](/attachment/image/1675053?d=1431693425)   
[![Click to Enlarge

Name: dssa222.jpg
Size: 200 KB](/attachment/image/1675057/thumbnail?d=1431693673)](/attachment/image/1675057?d=1431693673)   
[![Click to Enlarge

Name: scdsd5.jpg
Size: 199 KB](/attachment/image/1675060/thumbnail?d=1431693803)](/attachment/image/1675060?d=1431693803)   
[![Click to Enlarge

Name: dvdfv65.jpg
Size: 209 KB](/attachment/image/1675063/thumbnail?d=1431693947)](/attachment/image/1675063?d=1431693947)   
[![Click to Enlarge

Name: dsd43.jpg
Size: 211 KB](/attachment/image/1675064/thumbnail?d=1431694084)](/attachment/image/1675064?d=1431694084)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#369](/thread/post/8264943#post8264943 "Post Permalink")

  * May 15, 2015 9:59pm  May 15, 2015 9:59pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting TickJob](/thread/post/8264681#post8264681 "View Quoted Post")
> 
> Disliked
> 
> Hi Radityo, I could not find the option of setting the following as shown in the screeenshot, how to do it? These few days I observed many many cases, start the next cycle in reversed direction is safer. For example, if up, buy-lots will take profit, then the next cycle should start Sell-First. Usually after running up(or down) some pips, it will stay in range for sometime, but don't know how long, that is more dangerous part. We are not worry if the price keep on up up up, this strategy will sure win some pips even the next cycle is in reversed...
> 
> Ignored

I have never tested this before, let me think to add this feature. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#370](/thread/post/8264956#post8264956 "Post Permalink")

  * Edited 10:31pm  May 15, 2015 10:05pm | Edited 10:31pm 

  * [ TickJob](tickjob)

  * | Joined Apr 2007  | Status: Trader | [166 Posts](/search?do=process&provider=Member&searchuser=37449)

> [Quoting radityo.ardi](/thread/post/8264943#post8264943 "View Quoted Post")
> 
> Disliked
> 
> {quote} I have never tested this before, let me think to add this feature.
> 
> Ignored

Thanks Radityo.  
  
Continue...  
the series of charts show that reversed after taking profit is working better. 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: cdg.jpg
Size: 206 KB](/attachment/image/1675072/thumbnail?d=1431695118)](/attachment/image/1675072?d=1431695118)   
[![Click to Enlarge

Name: ds.jpg
Size: 229 KB](/attachment/image/1675077/thumbnail?d=1431695581)](/attachment/image/1675077?d=1431695581)   
[![Click to Enlarge

Name: ce3.jpg
Size: 186 KB](/attachment/image/1675078/thumbnail?d=1431695723)](/attachment/image/1675078?d=1431695723)   
[![Click to Enlarge

Name: csd3.jpg
Size: 194 KB](/attachment/image/1675079/thumbnail?d=1431695816)](/attachment/image/1675079?d=1431695816)   
[![Click to Enlarge

Name: sdfc.jpg
Size: 157 KB](/attachment/image/1675086/thumbnail?d=1431696641)](/attachment/image/1675086?d=1431696641)   
[![Click to Enlarge

Name: xsa.jpg
Size: 185 KB](/attachment/image/1675087/thumbnail?d=1431696671)](/attachment/image/1675087?d=1431696671)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#371](/thread/post/8265146#post8265146 "Post Permalink")

  * May 15, 2015 11:17pm  May 15, 2015 11:17pm 

  * [ TickJob](tickjob)

  * | Joined Apr 2007  | Status: Trader | [166 Posts](/search?do=process&provider=Member&searchuser=37449)

in fast moving choppy time, after taking profit don't reverse seem very dangerous, it chop up down up down very fast the lot size reach 128.

Attached Image (click to enlarge)

[![Click to Enlarge

Name: juj4.jpg
Size: 210 KB](/attachment/image/1675122/thumbnail?d=1431699442)](/attachment/image/1675122?d=1431699442)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#372](/thread/post/8265945#post8265945 "Post Permalink")

  * Edited 7:44am  May 16, 2015 6:41am | Edited 7:44am 

  * [ TickJob](tickjob)

  * | Joined Apr 2007  | Status: Trader | [166 Posts](/search?do=process&provider=Member&searchuser=37449)

end of this week testing, brief summary:  
1\. [Oanda](/brokers/oanda "View OANDA Broker Profile"), ICMarkets seem to have problems, EA hanged at 4th or higher order.  
2\. my 10-year-old computer seem to have problem, EA hanged at 4h or higher order.  
3\. EA is working nonstop on my 6-year-old computer with Tickmill ECN-Pro Demo Acc.  
4\. Tickmill Classic Demo Acc hanged at 4th or higher order on my new 4-core computer.  
5\. need to have an option to reverse BUY-SELL after taking profit(see above series of charts)  
6\. need to have an option to manually increase and/or shift the gap up/down during progression.  
(actually it is a impossible to survive long with 5 pips gap, too small, spread widening to 5pips very likely and price choppy within 5pipis also often, safer is to dynamically adjusted automatically or by human)  
  
<http://www.fengshui-bank.com/Statement9.htm>

Attached Image (click to enlarge)

[![Click to Enlarge

Name: end2.jpg
Size: 293 KB](/attachment/image/1675339/thumbnail?d=1431726023)](/attachment/image/1675339?d=1431726023)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#373](/thread/post/8269498#post8269498 "Post Permalink")

  * May 19, 2015 8:21am  May 19, 2015 8:21am 

  * [ TickJob](tickjob)

  * | Joined Apr 2007  | Status: Trader | [166 Posts](/search?do=process&provider=Member&searchuser=37449)

I try new broker, Gainsy. It give me the following error message. What is the problem?  
I also notice that my gap size is 3 pip, but pending order become 5pips away.

Attached Image (click to enlarge)

[![Click to Enlarge

Name: gainsy-error1.jpg
Size: 289 KB](/attachment/image/1676574/thumbnail?d=1431991287)](/attachment/image/1676574?d=1431991287)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#374](/thread/post/8269518#post8269518 "Post Permalink")

  * May 19, 2015 8:42am  May 19, 2015 8:42am 

  * [ leancuisine](leancuisine)

  * | Joined Jul 2014  | Status: Trader | [38 Posts](/search?do=process&provider=Member&searchuser=376648)

> [Quoting TickJob](/thread/post/8269498#post8269498 "View Quoted Post")
> 
> Disliked
> 
> I try new broker, Gainsy. It give me the following error message. What is the problem? I also notice that my gap size is 3 pip, but pending order become 5pips away. {image}
> 
> Ignored

"Invalid Stops" might mean that there is a minimum pips distance that Gainsy requires the pending order to be away from, in this case 5 pips perhaps. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#375](/thread/post/8269734#post8269734 "Post Permalink")

  * May 19, 2015 1:45pm  May 19, 2015 1:45pm 

  * [ TickJob](tickjob)

  * | Joined Apr 2007  | Status: Trader | [166 Posts](/search?do=process&provider=Member&searchuser=37449)

> [Quoting leancuisine](/thread/post/8269518#post8269518 "View Quoted Post")
> 
> Disliked
> 
> {quote} "Invalid Stops" might mean that there is a minimum pips distance that Gainsy requires the pending order to be away from, in this case 5 pips perhaps.
> 
> Ignored

I see. Thank you for your information.  
Though there are error message but so far so good, EA still running, some orders still executed.  
5pips minimum distance on pending BUY-STOP SELL-STOP order may not be too much a problem.  
  
this is the result so far: <http://www.fengshui-bank.com/GainsyStatement1.htm>  
  
I just restart EA and set the GAP=55point, no erro. during starting.  
  
By the way, how is Gainsy, good broker? trusted?

Attached Image (click to enlarge)

[![Click to Enlarge

Name: gain3.jpg
Size: 260 KB](/attachment/image/1676658/thumbnail?d=1432011124)](/attachment/image/1676658?d=1432011124)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#376](/thread/post/8282260#post8282260 "Post Permalink")

  * May 25, 2015 7:44pm  May 25, 2015 7:44pm 

  * [ TickJob](tickjob)

  * | Joined Apr 2007  | Status: Trader | [166 Posts](/search?do=process&provider=Member&searchuser=37449)

I attached the EA to 30+ charts progressively, each with different magic number., it run for the few hours, then after my coffee break come back and see the following errors. Please advise what are these errors means. How do they affect my positions? 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: PM-Error Message.jpg
Size: 256 KB](/attachment/image/1680783/thumbnail?d=1432550635)](/attachment/image/1680783?d=1432550635)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#377](/thread/post/8282276#post8282276 "Post Permalink")

  * May 25, 2015 7:58pm  May 25, 2015 7:58pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar157942_10.gif) fxindikator](fxindikator)

  * Joined Oct 2010 | Status: Trader | [167 Posts](/search?do=process&provider=Member&searchuser=157942)

> [Quoting TickJob](/thread/post/8282260#post8282260 "View Quoted Post")
> 
> Disliked
> 
> I attached the EA to 30+ charts progressively, each with different magic number., it run for the few hours, then after my coffee break come back and see the following errors. Please advise what are these errors means. How do they affect my positions? {image}
> 
> Ignored

there's a good reason why raditya keep using tickmill platform on all his trade explorer. better check if your current brokers use has better pair specs. the reason why these error could be the minimum distance of any order executed/modify. it may never happen while we at manually trade, but when it's come to ea logic, freeze level are quite annoying. check your current pair **stop order/level** , if these level are any other than 0 pips means your current account are no better for any ea with tight execution as these rapid grid method. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#378](/thread/post/8282448#post8282448 "Post Permalink")

  * May 25, 2015 9:46pm  May 25, 2015 9:46pm 

  * [ TickJob](tickjob)

  * | Joined Apr 2007  | Status: Trader | [166 Posts](/search?do=process&provider=Member&searchuser=37449)

> [Quoting fxindikator](/thread/post/8282276#post8282276 "View Quoted Post")
> 
> Disliked
> 
> {quote} there's a good reason why raditya keep using tickmill platform on all his trade explorer. better check if your current brokers use has better pair specs. the reason why these error could be the minimum distance of any order executed/modify. it may never happen while we at manually trade, but when it's come to ea logic, freeze level are quite annoying. check your current pair stop order/level, if these level are any other than 0 pips means your current account are no better for any ea with tight execution as these rapid grid method.
> 
> Ignored

Thank you very much for your advice.  
I will try TickMill. By the way, whoelse is good?  
Some more errors come out when price go up fast, and many of my position taking profit. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: pm28-error.jpg
Size: 65 KB](/attachment/image/1680854/thumbnail?d=1432558014)](/attachment/image/1680854?d=1432558014)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#379](/thread/post/8282979#post8282979 "Post Permalink")

  * May 26, 2015 8:31am  May 26, 2015 8:31am 

  * [ TickJob](tickjob)

  * | Joined Apr 2007  | Status: Trader | [166 Posts](/search?do=process&provider=Member&searchuser=37449)

TickMill also has error.  
Don't know which broker to use now?

Attached Image (click to enlarge)

[![Click to Enlarge

Name: tickmill-error111.jpg
Size: 242 KB](/attachment/image/1681102/thumbnail?d=1432596775)](/attachment/image/1681102?d=1432596775)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#380](/thread/post/8283134#post8283134 "Post Permalink")

  * May 26, 2015 10:59am  May 26, 2015 10:59am 

  * [ TickJob](tickjob)

  * | Joined Apr 2007  | Status: Trader | [166 Posts](/search?do=process&provider=Member&searchuser=37449)

TickMill Hanged  
at least FxNext did not hang. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: tickmill-hanged1.jpg
Size: 116 KB](/attachment/image/1681166/thumbnail?d=1432605538)](/attachment/image/1681166?d=1432605538)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Trapping System: Tunnel Martingale
  *   * [ **Reply to Thread** ](/thread/524198-trapping-system-tunnel-martingale/reply#reply)

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

[Martingale, Anti-martingale, and Compounding](/thread/571233-martingale-anti-martingale-and-compounding "Hi all traders, 
i started this thread to meet others people interested in money management. 
We all know that martingale strategies are...") 40 replies

[Martingale, Reverse Martingale, Modified Martingale, Maths](/thread/736165-martingale-reverse-martingale-modified-martingale-maths "Hi all, so Martingale has been a risky yet maybe non profitable system. While roulette has an edge of \(2.7%/5.4%\) 
  
Inspired by Adam...") 1 reply

[How to change this Martingale to Reverse Martingale ?](/thread/546755-how-to-change-this-martingale-to-reverse-martingale "How to change this Martingale to Reverse Martingale ?") 3 replies

[Trapping System: Way to Fully-Automated Trading System](/thread/509226-trapping-system-way-to-fully-automated-trading-system "Hi fellow Traders! 
This is my first time to write a new thread. Would like to share a trading method, which at least made me happy right...") 47 replies

[Martingale vs. Non Martingale (Simplified RoR vs Profit)](/thread/526308-martingale-vs-non-martingale-simplified-ror-vs-profit "Martingale: The gambler doubles his bet after every loss... 
  
Martingale vs. Non Martingale \(Simplified RoR vs Profit in 3 trade runs...") 1 reply

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/524198-trapping-system-tunnel-martingale/reply#reply)
  * Subscribe
  * [221](javascript:void\(0\);)

Attachments: Trapping System: Tunnel Martingale

Tags: Trapping System: Tunnel Martingale

#  [](/thread/524198-trapping-system-tunnel-martingale)Trapping System: Tunnel Martingale 

  * 

  * [#381](/thread/post/8294283#post8294283 "Post Permalink")

  * Jun 1, 2015 1:33am  Jun 1, 2015 1:33am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar157942_10.gif) fxindikator](fxindikator)

  * Joined Oct 2010 | Status: Trader | [167 Posts](/search?do=process&provider=Member&searchuser=157942)

> [Quoting TickJob](/thread/post/8283134#post8283134 "View Quoted Post")
> 
> Disliked
> 
> TickMill Hanged at least FxNext did not hang. {image}
> 
> Ignored

is that a winxp OS ? perhaps it's related to memory used ? since the error are mostly context busy, means there's some lagging process. I barely found these problem, both when running the EA on my PC or VPS. radit should easily answer these matter, but seem he's too busy at another grid thread. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#382](/thread/post/8305267#post8305267 "Post Permalink")

  * Jun 4, 2015 9:47pm  Jun 4, 2015 9:47pm 

  * [ TickJob](tickjob)

  * | Joined Apr 2007  | Status: Trader | [166 Posts](/search?do=process&provider=Member&searchuser=37449)

> [Quoting fxindikator](/thread/post/8294283#post8294283 "View Quoted Post")
> 
> Disliked
> 
> {quote} is that a winxp OS ? perhaps it's related to memory used ? since the error are mostly context busy, means there's some lagging process. I barely found these problem, both when running the EA on my PC or VPS. radit should easily answer these matter, but seem he's too busy at another grid thread.
> 
> Ignored

today I run [TickMill](/brokers/tickmill "View Tickmill Broker Profile") 2 demo acc on 2 pc, each acc I run 10 instances of the same EA on 10 charts. It give the following error. Real trading account whether has this problem?

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: Tickmill-Invalid error1.jpg
Size: 158 KB](/attachment/image/1688774/thumbnail?d=1433422019)](/attachment/image/1688774?d=1433422019)   
[![Click to Enlarge

Name: TickMill-error2.jpg
Size: 162 KB](/attachment/image/1688779/thumbnail?d=1433422174)](/attachment/image/1688779?d=1433422174)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#383](/thread/post/8305279#post8305279 "Post Permalink")

  * Jun 4, 2015 9:51pm  Jun 4, 2015 9:51pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting TickJob](/thread/post/8305267#post8305267 "View Quoted Post")
> 
> Disliked
> 
> {quote} today I run TickMill 2 demo acc on 2 pc, each acc I run 10 instances of the same EA on 10 charts. It give the following error. Real trading account whether has this problem? {image}
> 
> Ignored

invalid stops is always the same issue as I described before. Due to the low gap, it actually tried to create order on the other side with requested price. The problem is the price moves too fast retract back to its previous position. Since the gap between the current price and the pending STOP order at the requested price is too low, broker throws this error. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#384](/thread/post/8305383#post8305383 "Post Permalink")

  * Jun 4, 2015 10:21pm  Jun 4, 2015 10:21pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar334546_1.gif) Pipomagic](pipomagic)

  * Joined May 2013 | Status: Coder, Trader & Optimist | [209 Posts](/search?do=process&provider=Member&searchuser=334546)

Only tunnel martingale at specific times of the day... example: 01:00 to 01:30 am GMT --- AUDUSD ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

DON'T TRADE THE DIRECTION, TRADE THE MOVE

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#385](/thread/post/8305640#post8305640 "Post Permalink")

  * Jun 4, 2015 11:30pm  Jun 4, 2015 11:30pm 

  * [ TickJob](tickjob)

  * | Joined Apr 2007  | Status: Trader | [166 Posts](/search?do=process&provider=Member&searchuser=37449)

> [Quoting radityo.ardi](/thread/post/8305279#post8305279 "View Quoted Post")
> 
> Disliked
> 
> {quote} invalid stops is always the same issue as I described before. Due to the low gap, it actually tried to create order on the other side with requested price. The problem is the price moves too fast retract back to its previous position. Since the gap between the current price and the pending STOP order at the requested price is too low, broker throws this error.
> 
> Ignored

  
Hi radityo,  
will the order be executed later on when price move back to valid order?  
  
I got busy error as follow, how does this affect the trade? 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: TickMill-Error2.jpg
Size: 202 KB](/attachment/image/1688926/thumbnail?d=1433428212)](/attachment/image/1688926?d=1433428212)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#386](/thread/post/8305667#post8305667 "Post Permalink")

  * Jun 4, 2015 11:42pm  Jun 4, 2015 11:42pm 

  * [ TickJob](tickjob)

  * | Joined Apr 2007  | Status: Trader | [166 Posts](/search?do=process&provider=Member&searchuser=37449)

another error, one instance of EA upper and lower lines missing, I don't know what's wrong but just remove this particular es from the chart. the other 9 instances of ea are still running ok. Could it be the possibility my computer loaded too many ea on the same account? 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: TickMill-Error3.jpg
Size: 50 KB](/attachment/image/1688934/thumbnail?d=1433428932)](/attachment/image/1688934?d=1433428932)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#387](/thread/post/8306444#post8306444 "Post Permalink")

  * Jun 5, 2015 6:23am  Jun 5, 2015 6:23am 

  * [ TickJob](tickjob)

  * | Joined Apr 2007  | Status: Trader | [166 Posts](/search?do=process&provider=Member&searchuser=37449)

Hi Radityo,  
  
I asked TickMill support, this is what they said:  
There is no limit to the number of close trade per second but please remember that if your EA will request order close, it should wait for confirmation from server.  
  
in your ea, how to add code to wait for confirmation from server? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#388](/thread/post/8306758#post8306758 "Post Permalink")

  * Jun 5, 2015 11:47am  Jun 5, 2015 11:47am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting TickJob](/thread/post/8306444#post8306444 "View Quoted Post")
> 
> Disliked
> 
> Hi Radityo, I asked TickMill support, this is what they said: There is no limit to the number of close trade per second but please remember that if your EA will request order close, it should wait for confirmation from server. in your ea, how to add code to wait for confirmation from server?
> 
> Ignored

simply to say, you can't close order simultaneously in 1 code. Once you call order close, it will wait until confirmed as closed, then it will move to the next opened order. So, no need to change on the code. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#389](/thread/post/8306759#post8306759 "Post Permalink")

  * Jun 5, 2015 11:49am  Jun 5, 2015 11:49am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting TickJob](/thread/post/8305640#post8305640 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi radityo, will the order be executed later on when price move back to valid order? I got busy error as follow, how does this affect the trade? {image}
> 
> Ignored

I'm not good at these error messages. But what I understand, this error is related to this.  
<https://www.mql5.com/en/articles/1412>  
More than 2 EAs are doing the trading. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#390](/thread/post/8307410#post8307410 "Post Permalink")

  * Jun 5, 2015 6:47pm  Jun 5, 2015 6:47pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar157942_10.gif) fxindikator](fxindikator)

  * Joined Oct 2010 | Status: Trader | [167 Posts](/search?do=process&provider=Member&searchuser=157942)

> [Quoting TickJob](/thread/post/8306444#post8306444 "View Quoted Post")
> 
> Disliked
> 
> Hi Radityo, I asked TickMill support, this is what they said: There is no limit to the number of close trade per second but please remember that if your EA will request order close, it should wait for confirmation from server. in your ea, how to add code to wait for confirmation from server?
> 
> Ignored

sure they will said that, since you put same ea at 10 chart at once. and yes they dont have minimum distance limit upon order modify or close. while related to multi order close it has to finish after one another, for example we had 100 order need to be close at the same time, the ea code see the closing price at 'x' price but as the price market keep changing, it need to 'reconfirm' or recalculate the close price order for the rest of order. I'm no expert with coding, but you can try these manually by putting lot of order and try to applied all order close script.  
best method probably by tuning the EA code to adapt ECN market price enviroment. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#391](/thread/post/8308095#post8308095 "Post Permalink")

  * Jun 5, 2015 9:57pm  Jun 5, 2015 9:57pm 

  * [ TickJob](tickjob)

  * | Joined Apr 2007  | Status: Trader | [166 Posts](/search?do=process&provider=Member&searchuser=37449)

Today EURUSD Gap throw out all my EA.   
How to overcome Gap problem?

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#392](/thread/post/8308271#post8308271 "Post Permalink")

  * Jun 5, 2015 10:25pm  Jun 5, 2015 10:25pm 

  * [ TickJob](tickjob)

  * | Joined Apr 2007  | Status: Trader | [166 Posts](/search?do=process&provider=Member&searchuser=37449)

Except this one still surviving through Gap. What so special about RVDMarkets?

Attached Image (click to enlarge)

[![Click to Enlarge

Name: GAP-Opening EA not working except this one1..jpg
Size: 177 KB](/attachment/image/1689815/thumbnail?d=1433510719)](/attachment/image/1689815?d=1433510719)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#393](/thread/post/8311953#post8311953 "Post Permalink")

  * Jun 8, 2015 6:52pm  Jun 8, 2015 6:52pm 

  * [ shadowbroker](shadowbroker)

  * | Joined Mar 2015  | Status: Trader | [15 Posts](/search?do=process&provider=Member&searchuser=402647)

i just started using this martingale ea, i thought about this idea a long time so its nice to find an ea for it.  
but i find it difficult to set it up. i am on a nano account demo. i want the cycle to be 20 pips for sl and 40 pips for tp (that way, the martingale factor needs to be 1.5, because the tp is double the sl). so i put in the ea settings Martingale Factor Modifier at 1.5 and i start with buy initial lot 0.25, but i see the next order, which is sell stop, is 0.50, and it should be 0.38 (0.25*1.5=0.375). can someone tell me what settings i need to put for this? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#394](/thread/post/8314990#post8314990 "Post Permalink")

  * Jun 9, 2015 10:09pm  Jun 9, 2015 10:09pm 

  * [ TickJob](tickjob)

  * | Joined Apr 2007  | Status: Trader | [166 Posts](/search?do=process&provider=Member&searchuser=37449)

> [Quoting radityo.ardi](/thread/post/8306759#post8306759 "View Quoted Post")
> 
> Disliked
> 
> {quote} I'm not good at these error messages. But what I understand, this error is related to this. <https://www.mql5.com/en/articles/1412> More than 2 EAs are doing the trading.
> 
> Ignored

Hi Radityo,  
THank you very much for the information.  
I copy the code and it works perfectly. Now I can run more than 10 EA in one platform also no problem. So far I tested the following 4 brokers no problem.  
TickMill  
RVDMarkets  
Darwinex  
Global Prime 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: many run1.jpg
Size: 413 KB](/attachment/image/1692218/thumbnail?d=1433855335)](/attachment/image/1692218?d=1433855335)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#395](/thread/post/8320231#post8320231 "Post Permalink")

  * Jun 11, 2015 8:26pm  Jun 11, 2015 8:26pm 

  * [ TickJob](tickjob)

  * | Joined Apr 2007  | Status: Trader | [166 Posts](/search?do=process&provider=Member&searchuser=37449)

Darwinex blocked my demo account.   
They said I sent over 10000 requests per day.   
How come other brokers do not block my account?  
  
another interesting thing, more than 10 EA running on Darwinex demo account hanged and I got huge profit.Maybe because the EA hanged then keep on sending out too many invalid requests.

Attached Image (click to enlarge)

[![Click to Enlarge

Name: darwinex.jpg
Size: 325 KB](/attachment/image/1694006/thumbnail?d=1434022161)](/attachment/image/1694006?d=1434022161)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#396](/thread/post/8321688#post8321688 "Post Permalink")

  * Jun 12, 2015 8:15am  Jun 12, 2015 8:15am 

  * [ AgeaRep](agearep)

  * | Joined Jun 2015  | Status: Trader | [1 Post](/search?do=process&provider=Member&searchuser=416019)

> [Quoting radityo.ardi](/thread/post/8261466#post8261466 "View Quoted Post")
> 
> Disliked
> 
> ok. I think let me try on your other broker, same as you. I believe this issue is due to the many factors related to broker. I do experienced it with my old broker (AGEA). This tunnel martingale can't be attached to that broker, due to its high spread, and so many slippage applied. So this factor affecting the EA operation (I do experienced this, that is why I moved to Tickmill, since it is more stable). Please test on your side with Tickmill, either Classic or Exchange account. Meanwhile, let me test overnight with your IC Markets and Oanda. I...
> 
> Ignored

We are sorry that you feel our order execution that way, what you mentioned about "slippage" was not true. When you place orders on MT4, you will see a dropbox named "Type", it shows "Market Execution", that means all your orders will be executed at market price (the price when server receives, in most cases, it is not the one you send / desire, in some cases, you will get better price than you desire), you may not like this execution, but it guarantees your order will be executed instead of receiving a message saying price changed you need to try again. If you want your orders to be executed at desired price, then you shall choose "Instant Execution", this execution type guarantees your order's execution price, but due to market changes all the time, your order may not be executed when price changes larger than your tolerance (you can set that tolerance when placing order), and your order will not execute. If you want this execution type, please contact us, we will exclusively setup your account for that. In one word, Market Execution: Order execution is guaranteed, but your price is not, and your order may be executed at better price than desired. Instant Execution: Your price is guaranteed, but order execution is not. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#397](/thread/post/8324529#post8324529 "Post Permalink")

  * Jun 13, 2015 5:16pm  Jun 13, 2015 5:16pm 

  * [ shadowbroker](shadowbroker)

  * | Joined Mar 2015  | Status: Trader | [15 Posts](/search?do=process&provider=Member&searchuser=402647)

> [Quoting shadowbroker](/thread/post/8311953#post8311953 "View Quoted Post")
> 
> Disliked
> 
> i just started using this martingale ea, i thought about this idea a long time so its nice to find an ea for it. but i find it difficult to set it up. i am on a nano account demo. i want the cycle to be 20 pips for sl and 40 pips for tp (that way, the martingale factor needs to be 1.5, because the tp is double the sl). so i put in the ea settings Martingale Factor Modifier at 1.5 and i start with buy initial lot 0.25, but i see the next order, which is sell stop, is 0.50, and it should be 0.38 (0.25*1.5=0.375). can someone tell me what settings...
> 
> Ignored

okay i figured out how to increase the lots correctly... but now i have other problem. the losing trades dont close at sl. the first trade is buy with 0.25 lots and i have sell stop 20 pips lower with 0.38 lots. when it reaches the sell stop it opens the sell trade, but it doesnt close the first buy trade! i set gap 20 pips , sl 20 pips and tp 40 pips. i tested on both nano account with 4 digits and normal account with 5 digits and it has the same problem. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#398](/thread/post/8336011#post8336011 "Post Permalink")

  * Jun 19, 2015 4:51pm  Jun 19, 2015 4:51pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar157942_10.gif) fxindikator](fxindikator)

  * Joined Oct 2010 | Status: Trader | [167 Posts](/search?do=process&provider=Member&searchuser=157942)

> [Quoting radityo.ardi](/thread/post/8306759#post8306759 "View Quoted Post")
> 
> Disliked
> 
> {quote} I'm not good at these error messages. But what I understand, this error is related to this. <https://www.mql5.com/en/articles/1412> More than 2 EAs are doing the trading.
> 
> Ignored

are you planning to release another revision then ? I've been thinking how bout putting all the order only during news released (high impact only for example).  
I just found similar ea who had news filter, and also using trapping order.  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: eaaa.jpg
Size: 205 KB](/attachment/image/1698957/thumbnail?d=1434700261)](/attachment/image/1698957?d=1434700261)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#399](/thread/post/8375128#post8375128 "Post Permalink")

  * Jul 10, 2015 10:51pm  Jul 10, 2015 10:51pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar378574_1.gif) McLovin](mclovin)

  * | Joined Jul 2014  | Status: Trader | [38 Posts](/search?do=process&provider=Member&searchuser=378574)

Hey Guys, and thanks a lot to **Radityo** for developing this interesting EA.  
  
I've been demo'ing this EA on a couple of Brokers and run into a couple of similar problems that TickJob seems to have run into. I've tested in Roboforex and [FXPro](/brokers/fxpro "View FxPro Broker Profile") both with differing results. On Roboforex loading the default Anytime EURUSD set on to my 1M EURUSD chart it seems to work fine apart from always stalling at the 4th order. It refuses to place the 5th Limit Order. I've set my Gap to either 60 or 100 (spread is about 15-20 points on 5 Digit brokers) and never get any of the Invalid Stops messages in the log. I do not have any other EA's loaded.  
  
On FXPro I stupidly placed it straight onto my Live account and it opened up 11x 0.02 trades as well as 11x pending 0.04 Limit orders before I hit the Autotrading button to disable it and then closed all the trades down manually. I then, more wisely repeated the set up but on an FXPro demo account and got similar behaviour. Sometimes the EA opens 2x 0.02 trades and 2x corresponding 0.04 Limit Orders (more often than not it's 2 sets), sometimes it opens 17! The number seems random. I've not managed it to open just the one set! I even just installed a clean MT4 just now and still get the same issues - loads of orders opened, every time.  
  
I've finally cracked this multiple order issue - The "Max Cycle" Setting needs to be set to **"1"** to only allow one set of orders at a time in FXPro. I do not have this issue in Roboforex using the "Max Cycle" setting of "0" (for Unlimited cycles).  
  
Another problem is that once a Profit Target is hit, the EA doesn't take the profit... It seems like it's stuck thinking that it wants to go in the opposite direction. The label "Direction" says "Sell" but the Buy orders are in significant Profit outstripping the corresponding Sells.  
  
I seem to run into Terminal issues on both brokers trying to close down a chart with this EA running or edit the EA Settings whilst it's running. I often get the Pop up prompt "You've decided to either stop your EA, or change....Do you want to close all pending orders ... etc" prompt but the terminal just hangs I have to restart it from Windows.  
  
I also managed some back testing which was interesting, but also, not without issues (See screenshot).  
  
Still - quite an interesting concept and I think it's worth taking further. I have traded a couple of Martingale systems that work well in ranging markets but fall over in trending ones and this Tunnel EA does the opposite though it does sometimes seem happy to flap around in a ranging market _**if**_ it gets on the right side of the market first! If we could somehow combine the 2 strategies... ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1) Here's an interesting article I read about adapting Martingale (or an "Inverse" Martingale) to a Trending market - <http://forexop.com/anti-martingale-trading-system/>  
  
I will keep testing this EA and look forward to contributing to this discussion. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: TunnelMartin.png
Size: 37 KB](/attachment/image/1711108/thumbnail?d=1436533712)](/attachment/image/1711108?d=1436533712)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#400](/thread/post/8412460#post8412460 "Post Permalink")

  * Edited Aug 2, 2015 12:28am  Aug 1, 2015 7:09am | Edited Aug 2, 2015 12:28am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar376032_1.gif) Carpathian](carpathian)

  * | Joined Jun 2014  | Status: Trader | [576 Posts](/search?do=process&provider=Member&searchuser=376032)

Hello Ardi and All,  
  
Tunnel/range exit combined with martingale... It is a nice concept one of my favorites as it looks simple and easy. You snap up a chart and price seems going somewhere anyways after some hesitation. Well sure it'll go away but how much will it cost you until it happens, and when it does how far does it go? How do you know if it will make up for your losses?  
  
I also created an EA for this concept, a bit different from yours I guess. Upon hitting the tunnel SL it closes the open position and immediately opens the reverse one with the set martingale factor size. So the EA has one position open at a time and it is monitoring the closed trades to keep track of the losses (ie. the cost of the tunnel) thus being able to calculate a BE for instance.  
Similarly while thinking about this, just as you, I came upon creating an excel file to model the possible outcomes of different martingale series and tunnel size factors. I did have the EA running on demos for a few months however never got back something I could trust in. It is either too big position size or the BE getting to far away or some technical problem.  
  
Nevertheless I think people on this thread may take use of this excel file (attached) by studying the mathematic nature of this concept and thus getting a better understanding.  
  
Keep up with the good work,  
Aron  

Attached File(s)

![File Type: xlsx](https://assets.faireconomy.media/images/attach/xlsx.gif) [Position.increase.xlsx](/attachment/file/1724351?d=1438380240) 30 KB | 566 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Trapping System: Tunnel Martingale
  *   * [ **Reply to Thread** ](/thread/524198-trapping-system-tunnel-martingale/reply#reply)

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

[Martingale, Anti-martingale, and Compounding](/thread/571233-martingale-anti-martingale-and-compounding "Hi all traders, 
i started this thread to meet others people interested in money management. 
We all know that martingale strategies are...") 40 replies

[Martingale, Reverse Martingale, Modified Martingale, Maths](/thread/736165-martingale-reverse-martingale-modified-martingale-maths "Hi all, so Martingale has been a risky yet maybe non profitable system. While roulette has an edge of \(2.7%/5.4%\) 
  
Inspired by Adam...") 1 reply

[How to change this Martingale to Reverse Martingale ?](/thread/546755-how-to-change-this-martingale-to-reverse-martingale "How to change this Martingale to Reverse Martingale ?") 3 replies

[Trapping System: Way to Fully-Automated Trading System](/thread/509226-trapping-system-way-to-fully-automated-trading-system "Hi fellow Traders! 
This is my first time to write a new thread. Would like to share a trading method, which at least made me happy right...") 47 replies

[Martingale vs. Non Martingale (Simplified RoR vs Profit)](/thread/526308-martingale-vs-non-martingale-simplified-ror-vs-profit "Martingale: The gambler doubles his bet after every loss... 
  
Martingale vs. Non Martingale \(Simplified RoR vs Profit in 3 trade runs...") 1 reply

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/524198-trapping-system-tunnel-martingale/reply#reply)
  * Subscribe
  * [221](javascript:void\(0\);)

Attachments: Trapping System: Tunnel Martingale

Tags: Trapping System: Tunnel Martingale

#  [](/thread/524198-trapping-system-tunnel-martingale)Trapping System: Tunnel Martingale 

  * 

  * [#401](/thread/post/8500119#post8500119 "Post Permalink")

  * Sep 21, 2015 11:56pm  Sep 21, 2015 11:56pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar406125_1.gif) Rolas](rolas)

  * | Joined Mar 2015  | Status: Trader | [15 Posts](/search?do=process&provider=Member&searchuser=406125)

Hello, everyone. When martingale 1.2.4 ,last order always 16,and EA stops.[ Image2.png ](http://www.forexfactory.com/attachment.php?attachmentid=1757964&stc=1&d=1442847018)Where is problem? Thankyou. My parameters[ Image3.png](http://www.forexfactory.com/attachment.php?attachmentid=1757966&stc=1&d=1442847338)

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: Image2.png
Size: 207 KB](/attachment/image/1757964/thumbnail?d=1442847016)](/attachment/image/1757964?d=1442847016)   
[![Click to Enlarge

Name: Image3.png
Size: 112 KB](/attachment/image/1757966/thumbnail?d=1442847337)](/attachment/image/1757966?d=1442847337)   

logitech

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#402](/thread/post/8501795#post8501795 "Post Permalink")

  * Edited Sep 23, 2015 12:08am  Sep 22, 2015 9:52pm | Edited Sep 23, 2015 12:08am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar345639_15.gif) SickOfScam](sickofscam)

  * | Membership Revoked  | Joined Aug 2013 | [589 Posts](/search?do=process&provider=Member&searchuser=345639)

Your MartingaleFactor= is 1, and MaxMartingaleFactor= is 25, which means you need set a MartingaleFactor for all 25 orders.  
For example: 0.01,0.02,0.04,0.06,0.09 ... you need specified as: 1,2,4,6,9 etc ....  
  
...you should try this EA on S. Tester too - and maybe then found some other new exciting conclusions !! :nerd:  
  
[quote=Rolas;8500119]Hello, everyone. When martingale 1.2.4 ,last order always 16,and EA stopsWhere is problem? Thank you. /quote]

perhaps my English is not perfect - but I know the Jungle

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#403](/thread/post/8502389#post8502389 "Post Permalink")

  * Sep 23, 2015 1:03am  Sep 23, 2015 1:03am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting Rolas](/thread/post/8500119#post8500119 "View Quoted Post")
> 
> Disliked
> 
> Hello, everyone. When martingale 1.2.4 ,last order always 16,and EA stops.[ Image2.png ](http://www.forexfactory.com/attachment.php?attachmentid=1757964&stc=1&d=1442847018)Where is problem? Thankyou. My parameters[ Image3.png](http://www.forexfactory.com/attachment.php?attachmentid=1757966&stc=1&d=1442847338) {image} {image}
> 
> Ignored

Hi,  
I'm very sorry, I'm no longer supporting this EA at the moment, as I'm focusing only 1 EA which I've built on another thread. But looking at the behaviour, you can check on the Experts tab to see whether any error arising.  
  
Usually this issue due to either you are not allowed to create order with the specified lot size at index 16, or maybe the price has slipped too far to create stop order. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#404](/thread/post/8538540#post8538540 "Post Permalink")

  * Oct 14, 2015 6:51am  Oct 14, 2015 6:51am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar406125_1.gif) Rolas](rolas)

  * | Joined Mar 2015  | Status: Trader | [15 Posts](/search?do=process&provider=Member&searchuser=406125)

> [Quoting radityo.ardi](/thread/post/8502389#post8502389 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi, I'm very sorry, I'm no longer supporting this EA at the moment, as I'm focusing only 1 EA which I've built on another thread. But looking at the behaviour, you can check on the Experts tab to see whether any error arising. Usually this issue due to either you are not allowed to create order with the specified lot size at index 16, or maybe the price has slipped too far to create stop order.
> 
> Ignored

Thank you Radityjo.ardi 

logitech

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#405](/thread/post/8653061#post8653061 "Post Permalink")

  * Dec 18, 2015 11:43pm  Dec 18, 2015 11:43pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar421160_9.gif) high321](high321)

  * Joined Jul 2015 | Status: 918528845436 | [229 Posts](/search?do=process&provider=Member&searchuser=421160)

if i put this system on two pair it gives second pair multiple order is any solution ? my gap is 30 to 50 point 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: EURUSDfM1k.png
Size: 37 KB](/attachment/image/1815572/thumbnail?d=1450449802)](/attachment/image/1815572?d=1450449802)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#406](/thread/post/8653352#post8653352 "Post Permalink")

  * Dec 19, 2015 1:48am  Dec 19, 2015 1:48am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar421160_9.gif) high321](high321)

  * Joined Jul 2015 | Status: 918528845436 | [229 Posts](/search?do=process&provider=Member&searchuser=421160)

It enabel max loss fuction did not working . Suppose i want only 6 lot opening like 1,2,4,8,16,32. So gap is 20 points then i have 1+4+16= 21 buy or sell and also 2+8+32 =42 buy or sell net lot is 42-21=21 lot . So i know every 100 point i loss 21 $ . If y any fuction all lot close on maxium loss like 21 and again start new circle. Pleace chek its enabel maxx loss fuction for dynamic lot 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#407](/thread/post/8654676#post8654676 "Post Permalink")

  * Dec 20, 2015 5:29pm  Dec 20, 2015 5:29pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar421160_9.gif) high321](high321)

  * Joined Jul 2015 | Status: 918528845436 | [229 Posts](/search?do=process&provider=Member&searchuser=421160)

i add stop losss but it can not restart on onec tp gain. that is the problem in ths ea . hope any one correct it 

Attached File(s)

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [tunnel martingle.mq4](/attachment/file/1816202?d=1450600143) 50 KB | 754 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#408](/thread/post/8655547#post8655547 "Post Permalink")

  * Dec 21, 2015 3:40pm  Dec 21, 2015 3:40pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

For those who has questions,  
Tunnel Martingale's development is currently discontinued. But I would like to recode it at sometime later. This recode activity will be started not faster than the next 3-5 months, depends on the support request on RdzGridTraps.  
  
I hope you understand. ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)  
  
Meanwhile, since it is a free open source code, you can ask another developer to "fork" it, and understand their legal standing before modifying it.  
I'll allow any modification from the latest source in the first page, as long as you don't change the base name (which is "Tunnel Martingale"), and you should not sell it for your own purpose.  
  
Apologies for that. Will see you in a few months later. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#409](/thread/post/8753738#post8753738 "Post Permalink")

  * Feb 15, 2016 3:12pm  Feb 15, 2016 3:12pm 

  * [ MFXN.rc](mfxn.rc)

  * | Joined Aug 2015  | Status: Trader | [1 Post](/search?do=process&provider=Member&searchuser=423865)

hello dear friends  
  
can any one add it this Feature:  
"start by manual order"  
  
its means a position open manual (pending or momentary), then the robot Based on settings and normal work manage and close it.  
and it can be run for Distinct charts in one mt4  
  
thank you 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#410](/thread/post/8768815#post8768815 "Post Permalink")

  * Feb 22, 2016 8:57pm  Feb 22, 2016 8:57pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar345639_15.gif) SickOfScam](sickofscam)

  * | Membership Revoked  | Joined Aug 2013 | [589 Posts](/search?do=process&provider=Member&searchuser=345639)

...tunnel of my mind... ![](https://resources.faireconomy.media/images/emojis/64/1f617.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f3b6.png?v=15.1)

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Tunnel.png
Size: 19 KB](/attachment/image/1862168/thumbnail?d=1456142185)](/attachment/image/1862168?d=1456142185)   

perhaps my English is not perfect - but I know the Jungle

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#411](/thread/post/8804346#post8804346 "Post Permalink")

  * Mar 10, 2016 9:48am  Mar 10, 2016 9:48am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar381991_7.gif) ForexSamsam](forexsamsam)

  * | Joined Sep 2014  | Status: Trader | [155 Posts](/search?do=process&provider=Member&searchuser=381991)

fail to all martingale ... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#412](/thread/post/8806459#post8806459 "Post Permalink")

  * Mar 11, 2016 1:02am  Mar 11, 2016 1:02am 

  * [ zigler](zigler)

  * | Joined Feb 2016  | Status: Trader | [166 Posts](/search?do=process&provider=Member&searchuser=447497)

Key is here to Place that on Trending pairs not on Range or you are dead. I see most using EURUSD, that could stick  
in range for Years! You need a TREND for such system, Or Fed Reserve Printer in your basement as other option ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#413](/thread/post/8936504#post8936504 "Post Permalink")

  * May 20, 2016 10:27am  May 20, 2016 10:27am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar416493_1.gif) esuerez](esuerez)

  * | Joined Jun 2015  | Status: Trader | [2 Posts](/search?do=process&provider=Member&searchuser=416493)

This is my Martingale Expert Advisor that I coded in 2008.  
  

Inserted Video

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#414](/thread/post/8938808#post8938808 "Post Permalink")

  * May 22, 2016 2:01am  May 22, 2016 2:01am 

  * [ masis](masis)

  * | Joined Jun 2015  | Status: Trader | [10 Posts](/search?do=process&provider=Member&searchuser=415054)

Hi, I had been using an EA very similar to yours on 5 different pairs. I did several backtests and I see here is a max 14 times in a row loss. For ex on Eurusd I was using 14 to 60 pips. It means, when i initiate the EA it places 14 pips above a buy stop and 14 pips below a sell stop. If buy stop is triggered the position is closed 60 pips above from the initial point. So the potential gain is 46 pips. İf the market retreats after the buy order execution then the sell stop triggers and %70 more lot is added to the initital lot size. In summary the distance between the buy and sell order is 28 pips. In every loss between buy and sell I add 70% to the last lot size so I keep my potential gain. The problem is, even I start with 0.01lot after 13 times loss in a row my lot size is increased as much as 10 lot as you can see the steps.(0,01-0,02-0,03-0,05-0,09-0,15-0,26-0,44-0,75-1,28-2,18-3,71-6,31- 10,73). Even this method is not guaranteed because there are weekend and news gap risk. You might miss the entry or reverse entry price, etc. After few moths of risky and stressful trading sessions, I realised that to trade the reverse of this method is better. My new trade idea is to bet against the market and increase my lot size in ranging market. Also most of the time the market is sideways. By this method in every trade my max loss will be my previous potential gain which was around 5usd(considering to start by 0,01lot). This week I will start to trade and Im so excited lets see whats gonna happen and will let you know the result. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#415](/thread/post/8938981#post8938981 "Post Permalink")

  * May 22, 2016 8:38am  May 22, 2016 8:38am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar397623_2.gif) Sajid](sajid)

  * Joined Jan 2015 | Status: ** NEWBIE ** | [601 Posts](/search?do=process&provider=Member&searchuser=397623)

> [Quoting zigler](/thread/post/8806459#post8806459 "View Quoted Post")
> 
> Disliked
> 
> Key is here to Place that on Trending pairs not on Range or you are dead. I see most using EURUSD, that could stick in range for Years! You need a TREND for such system, Or Fed Reserve Printer in your basement as other option ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)
> 
> Ignored

Dear, How you will know that when a pair to start ranging or trending? Forgive me brother, I still not discovered what the hell is a trend? Please don't ask me to go to babypips. I have chanted almost all. I have asked this question on many forums, but no universal definition i got. Some will be using the 200 EMA B.S, some will be using HH,LL but nobody knows that what a trend is at a particular time. Please forgive me, I can also figure out that what the trend was on past charts. As time goes on, My belief that there is nothing like trend. The only thing that can be considered as trend is "What the hell the big players are doing/arranging/planning at a particular time". Nobody can read there mind or the near future but you can almost 70% of the times, find out what possibly the bigger players will do.  
  
I hope, i have not disheartened anybody but this is what the harsh reality is. Take any system(EAs,Indicators), you will find yourself in situations that "If we add this thing,this thing, this thing, blah blah blah to system, it will become perfect but it will never happend while in the process, you will break your basic system.  
  
The key is to keep it simple as much as you can. Keep it generic. You will win market most of the times.  
  
  
Happy and Green pips to all. 

Forex; the game of movements not the game of candles.

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#416](/thread/post/8940192#post8940192 "Post Permalink")

  * May 23, 2016 3:29pm  May 23, 2016 3:29pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting Sajid](/thread/post/8938981#post8938981 "View Quoted Post")
> 
> Disliked
> 
> {quote} Dear, How you will know that when a pair to start ranging or trending? Forgive me brother, I still not discovered what the hell is a trend? Please don't ask me to go to babypips. I have chanted almost all. I have asked this question on many forums, but no universal definition i got. Some will be using the 200 EMA B.S, some will be using HH,LL but nobody knows that what a trend is at a particular time. Please forgive me, I can also figure out that what the trend was on past charts. As time goes on, My belief that there is nothing like trend....
> 
> Ignored

We have something in common. Sorry before, I actually not intend to reply on this thread, because I don't want to encourage martingale to people at the moment. But reading to your comments, it's interesting and I think we have something in common.  
  
I've read all of those resources, books, ebooks, everything about forex, how to determine all the trend and all. But none of them could absolutely predict the trend. The interesting thing is most of the time (or most of us) will read-learn-do and if starting to "work", we become what we call as "overconfident". And this is the one where people usually fall into the same pit.  
  
That is WHY:

  1. a lot of people selling forex strategy (in ebook, website, or some kind of signal)
  2. a lot of people selling EA
  3. a lot of people starting a company to be forex broker
  4. a lot of people starting a company to be an electronic wallet exchanger

No offense, but they are the actual money maker, sucking money from people who can't get up from their dream. Frankly speaking, I'm the one that is still dreaming... ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)  
  
Now go back to determining the trend and non-trend. No one could correctly predict the trend 100% without fail. But to me, the closest to 100% is to predict when the market are going to be in ranging time, which is inside the non-trading hours. So, I'm trying to catch profit from ranging market. Of course without playing with martingale. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#417](/thread/post/8940197#post8940197 "Post Permalink")

  * May 23, 2016 3:32pm  May 23, 2016 3:32pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting masis](/thread/post/8938808#post8938808 "View Quoted Post")
> 
> Disliked
> 
> Hi, I had been using an EA very similar to yours on 5 different pairs. I did several backtests and I see here is a max 14 times in a row loss. For ex on Eurusd I was using 14 to 60 pips. It means, when i initiate the EA it places 14 pips above a buy stop and 14 pips below a sell stop. If buy stop is triggered the position is closed 60 pips above from the initial point. So the potential gain is 46 pips. İf the market retreats after the buy order execution then the sell stop triggers and %70 more lot is added to the initital lot size. In summary...
> 
> Ignored

I introduce you to my EA: [RdzGridTraps](http://www.forexfactory.com/showthread.php?t=539304).  
It does exactly the same as what you've described. But I still don't recommend martingale (well, probably "soft" martingale still ok though). 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#418](/thread/post/8940518#post8940518 "Post Permalink")

  * May 23, 2016 6:17pm  May 23, 2016 6:17pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar397623_2.gif) Sajid](sajid)

  * Joined Jan 2015 | Status: ** NEWBIE ** | [601 Posts](/search?do=process&provider=Member&searchuser=397623)

> [Quoting radityo.ardi](/thread/post/8940192#post8940192 "View Quoted Post")
> 
> Disliked
> 
> {quote} We have something in common. Sorry before, I actually not intend to reply on this thread, because I don't want to encourage martingale to people at the moment. But reading to your comments, it's interesting and I think we have something in common. I've read all of those resources, books, ebooks, everything about forex, how to determine all the trend and all. But none of them could absolutely predict the trend. The interesting thing is most of the time (or most of us) will read-learn-do and if starting to "work", we become what we call as...
> 
> Ignored

  
200% agree with you regarding who are the real beneficiaries of the field. I have never been in martingale trading. And to be honest, I found myself very dumb in understanding martingale strategies. But i can't deny that martingale can be a possible way to make up a living from this B.S market. And also on the other side, some people dream that they will get/develop a martingale machine which will be earning for them while they are on the beach with their girlfriend. I think it's not like this. It's you and you to finally decide when to start running your ATM machine and when to stop it. Before engaging into any martingale , for me its more important to learn that  
1) when a pair most probably will fall into ranging. And i think it's not that much a difficult job.  
2) What pairs are suitable for a particular martingale?  
3) Timings? 

Forex; the game of movements not the game of candles.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#419](/thread/post/9671605#post9671605 "Post Permalink")

  * Mar 16, 2017 2:59pm  Mar 16, 2017 2:59pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar542878_3.gif) thangnd.1211](thangnd.1211)

  * | Joined Dec 2016  | Status: Trader | [244 Posts](/search?do=process&provider=Member&searchuser=542878)

i will test your EA, thank you ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#420](/thread/post/12606265#post12606265 "Post Permalink")

  * Nov 8, 2019 4:21pm  Nov 8, 2019 4:21pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

I'm not too sure... whether I have to revive this thread, or just keep it silent. Sorry, this post might've looked like a story to you.  
  
Tunnel Martingale is a stupid strategy. I've got an idea, rewrote the idea as EA in MetaTrader, backtest it, then failed. A lot of ideas... too many ideas. Martingale is a bad idea, it could suck your money instantly (generally speaking all strategy does, but this one does "better" to suck your money than others). If you follow this thread from start, basically Tunnel Martingale is just like any other martingale, if the market moves the opposite, open order 2 times of the volume from the previous order. It was awesome and gave an assurance that you will never lose (technically). Profit went through, but practically when it goes sideways, it will keep adding order 2 times of your last volume until your equity **runs dry**.  
  
I was having a feeling **TOO LAZY** to work on any EA from MetaTrader anymore. Just because of MetaTrader is such a d**k for keeping C++ as their MetaTrader's EA programming language. It is old as your grandma's pie recipe, which is nice btw, but not for such a programming language in this fast-moving world. Keeping arrays of objects with complex data, complex programming style, come on...!!! It took me weeks, just to deal with sorting alone, plus if I want a filter, sorting, all sort of stuff that people do when using arrays. Additionally, I need to decide which type of "string" variable I need to use, not to mention that I have to write **at least** 1 line of code to clear it in the memory. Ain't nobody got time for that!  
  
C++ isn't just the right programming language for writing EA to my opinion. While other businesses can move fast using a complicated-yet-easy-to-use code framework, writing C++ is just too slow. C++ is best suitable for programming the robot (the actual one, not EA), microprocessor, or devices, or anything you can think of that connects directly with hardware and stuff. It's because of the ability to "talk" to the hardware fluently without "conversion" of the language in the framework which typically can take longer to process. Easy, lightweight, and just so "direct". So, C++ ![](https://resources.faireconomy.media/images/emojis/64/2764-fe0f.png?v=15.1) devices/hardware, but not for trading tools like MetaTrader. I want something where just by snapping my finger, I can do many complex processes, especially dealing with arrays, heavy calculation and all. So, that's why .NET Framework was invented.  
  
  
Until **today** , I've got cTrader which is actually based on the .NET framework. But not many brokers used it up as their base platform, it's just like their sidekick. What do I get for using cTrader? I'm not in the position of promoting it, just that cTrader is the only one uses the NET framework (so far. Please CMIIW).

  1. Of course, using .NET Framework is much more efficient. Just by snapping finger, you can use all sort of complex process which C++ can do but can be 3x - 5x longer time to build the same logic. You don't even have to write any line just to clear your memory, all is done by the framework itself. I'm a 9-6 office worker, I don't have all my time to write these codes unless if I quit my job and do forex trading. But I'm not confident yet to do it since that requires a lot of money due to commitments with my personal errands (need to support my family, etc).
  2. When I was dealing with MetaTrader 4 (old one), I've got to deal with the synchronous process when opening order or opening at market price. Most of the time, opening 1 order can take 0.2 seconds - 1.5 seconds depending on the network connectivity. with cTrader, the infrastructure and the software itself is quite sustainable and reliable. You can take simultaneous asynchronous orders in no time! Maybe no one is there...? I don't know much about MetaTrader 5 and such, maybe now uses async but I won't budge if they still use C++.
  3. Brother, cTrader is using .NET Framework. That means you can use any libraries out there, be it the lib in Nuget, or whatever...!!! Now, what do you want? Want it to connect to SQL Server? Want it to connect to any server via network protocol? Want it to connect to the cloud? Process JSON, XML, anything easily?

  
Now, let's get back to the business, shall we?  
Recently, I've just finished rewriting Tunnel Martingale (TM) as a cBot (that's what they call for EA in cTrader). I did it in 1 day or less! Still, I need to tidy up anyway. But here's the idea. I've put additional logic to execute the TM's divided into sessions.  
I know that if I keep opening position and order, it always ends up bad! It sucks (literally) my money (virtual maybe)! But that's not what we're going to do. In summary, just execute 1 session, at the most-active timing for the chart. It's when a piece of news is about to release.  
  
You've got 3 news, it's 3 sessions. But the Tunnel Martingale concept still the same old sh*t. Just read at the FF calendar and put in the date and time, whether to start with Buy or Sell first. I backtested with the following simple concept:

  1. See FF calendar for past events.  
I would rather avoid Non-farm Payroll which happens every first Friday of the month, at 20:30 pm of my timezone. Since the movement is crazy and unpredictable, this could potentially end up having more than 10 open positions and suck your money dry.
  2. Tag the date and the exact time to the configuration.
  3. See "Forecast" and "Previous". Because by right, you can't see the "Actual" of future events. If it's "good for the first pair of the currency" then put Buy. If it's "good for the last pair of the currency", then put Sell.

Below a snip of the configuration...  

Attached Image

![](/attachment/image/3484782?d=1573197543)

  
  
and below is the backtest result for the past 1 month...  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot2.png
Size: 44 KB](/attachment/image/3484780/thumbnail?d=1573197472)](/attachment/image/3484780?d=1573197472)   

  
  
Now, this is what I like from writing code like this... more greens.  
  

> Quote
> 
> Disliked
> 
> It is not how you always win the trade, it is how you maximize the winning than losing. ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Trapping System: Tunnel Martingale
  *   * [ **Reply to Thread** ](/thread/524198-trapping-system-tunnel-martingale/reply#reply)

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

[Martingale, Anti-martingale, and Compounding](/thread/571233-martingale-anti-martingale-and-compounding "Hi all traders, 
i started this thread to meet others people interested in money management. 
We all know that martingale strategies are...") 40 replies

[Martingale, Reverse Martingale, Modified Martingale, Maths](/thread/736165-martingale-reverse-martingale-modified-martingale-maths "Hi all, so Martingale has been a risky yet maybe non profitable system. While roulette has an edge of \(2.7%/5.4%\) 
  
Inspired by Adam...") 1 reply

[How to change this Martingale to Reverse Martingale ?](/thread/546755-how-to-change-this-martingale-to-reverse-martingale "How to change this Martingale to Reverse Martingale ?") 3 replies

[Trapping System: Way to Fully-Automated Trading System](/thread/509226-trapping-system-way-to-fully-automated-trading-system "Hi fellow Traders! 
This is my first time to write a new thread. Would like to share a trading method, which at least made me happy right...") 47 replies

[Martingale vs. Non Martingale (Simplified RoR vs Profit)](/thread/526308-martingale-vs-non-martingale-simplified-ror-vs-profit "Martingale: The gambler doubles his bet after every loss... 
  
Martingale vs. Non Martingale \(Simplified RoR vs Profit in 3 trade runs...") 1 reply

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/524198-trapping-system-tunnel-martingale/reply#reply)
  * Subscribe
  * [221](javascript:void\(0\);)

Attachments: Trapping System: Tunnel Martingale

Tags: Trapping System: Tunnel Martingale

#  [](/thread/524198-trapping-system-tunnel-martingale)Trapping System: Tunnel Martingale 

  * 

  * [#421](/thread/post/12609199#post12609199 "Post Permalink")

  * Nov 11, 2019 8:58am  Nov 11, 2019 8:58am 

  * [ RevoTrader2](revotrader2)

  * | Joined Oct 2018  | Status: Trader | [7 Posts](/search?do=process&provider=Member&searchuser=721844)

Firstly, I am excited to see that the radityo.ardi is alive and posting in forex factory again. Hi there!  
  
Secondly, I agree with all your comments, especially regarding mg, however, I still use my own grid and mg ea, that is still, after 2.5 years, based on rdzgrid. This one: "Tunnel MG, in my opinion, just contains a lot of filters, and filters, imo, are every bit as bad as they are good; eg they filter out just as many of the best signals, as they do the bad. That is why I only tested TMG for few weeks before returning to testing of rdz. I have changed the first 2 trades from pending orders, to instant orders, AND also added options for different styles of trail stop/step, AND a sort of "average tp". My new ea contains only about 5% of your coding now, however, I still consider it as rdz evolved ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1).  
  
I did try to contact you via ff and google plus, and linked in, but only got a hello from you. I hope that you do resume coding of rdz or tunnel mg eas. I will eagerly follow your postings! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#422](/thread/post/12609713#post12609713 "Post Permalink")

  * Nov 11, 2019 5:47pm  Nov 11, 2019 5:47pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting RevoTrader2](/thread/post/12609199#post12609199 "View Quoted Post")
> 
> Disliked
> 
> Firstly, I am excited to see that the radityo.ardi is alive and posting in forex factory again. Hi there! Secondly, I agree with all your comments, especially regarding mg, however, I still use my own grid and mg ea, that is still, after 2.5 years, based on rdzgrid. This one: "Tunnel MG, in my opinion, just contains a lot of filters, and filters, imo, are every bit as bad as they are good; eg they filter out just as many of the best signals, as they do the bad. That is why I only tested TMG for few weeks before returning to testing of rdz. I have...
> 
> Ignored

Whoaaa.. I really didn't expect anyone from the past to reply, but I do really appreciate it!![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)  
Excited to see your reply too, buddy!  
Anyway, I'm just updating after a long hiatus. Got responsibilities, so held back whatever I left.  
  
I am still testing my cBot with the server's past data. It seems promising though, but honestly too good to be true.  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot2.png
Size: 151 KB](/attachment/image/3486378/thumbnail?d=1573458803)](/attachment/image/3486378?d=1573458803)   

  
  
I need more tests with more data as I got more. The rows on red touched 6 times of floor and ceiling of tunnel 6 times. But it is expected as it was Monday, the most "lazy" day in trading.  
  
So, in principle, this new Tunnel Martingale is nothing new, same as the last time. The only difference is just **purely money management**. I was thinking the same for other people with another strategy too, even manual "chart guy", or automated ones like myself. So for example:

  1. Last time we calculate lot size based on the money we have. Now, just tag to 0.01 always.
  2. Trade only once a day, avoid the same execution time, avoid the same pair. 2 trades max is also can, make sure the time is > 3 hrs apart.
  3. Avoid holidays.
  4. Avoid NFP.

So, the key here is don't be greedy. If you want to be greedy, put onto some other pairs. That screenshot is only for 1 pair, with 1,000 USD, generates around 11 USD on that timeframe, which is 1.1% growth. But you got a lot of pairs as well. Maybe we can push for 500 USD (then be 2.2% growth) starting money, or 250 USD. But that means risky margin level when it goes beyond 4x of touching floor + ceiling of the tunnel. To me, 10% growth per month is a decent profit.  
  
For Grid, I've got no idea how to improve it. I'm so exhausted with ideas. I can throw a lot of grid ideas, but none of them can anticipate the switch between sideways and trending. The fact is, grid requires the trade to be on always (because it's the nature of grid trading, you get profit from a lot of orders, sometimes it goes over a week). When you want it to generate profit during sideways, you'll be stuck when it's at a strong trend (and it happened). When you want it to generate profit during trending, the fact is it's not always trending all the time. So, I guess the Grid, whatever the strategy is, will be difficult and I don't see any future in it. I've seen a lot, like someone doing the "so-called" grid but not it. Hedge all the way till even months. But it's difficult to manage and practically stuck.  
  

> [Quoting RevoTrader2](/thread/post/12609199#post12609199 "View Quoted Post")
> 
> Disliked
> 
> I did try to contact you via ff and google plus, and linked in, but only got a hello from you. I hope that you do resume coding of rdz or tunnel mg eas. I will eagerly follow your postings!
> 
> Ignored

I am no longer coding with MetaTrader. The programming language is using C++ which is sucks. I am into cTrader now. Will post more if this TM does better. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#423](/thread/post/12610213#post12610213 "Post Permalink")

  * Nov 11, 2019 10:13pm  Nov 11, 2019 10:13pm 

  * [ RevoTrader2](revotrader2)

  * | Joined Oct 2018  | Status: Trader | [7 Posts](/search?do=process&provider=Member&searchuser=721844)

very cool; yes I read your previous...previous post regarding C++ and cTrader vs mql4 and MT4, and while i agree with your comments completely, Mt4 and mql4 is still the main platform used for the desktop, so while I will be very curious to follow your coding; I will have to try converting it to mql4 for my own use ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1) as cTrader, as good as the plusses it has over mt4, mt4 does not have any negatives that i am aware of that may have any effect or any negative effects on my current trading.  
  
i also agree with your grid comments regarding grid having to be kept in ON state. However the first reason i fell in love with rdzgridtraps was the on screen button and setting to stop trading after the current cycle has closed. I am not sure if that feature was in tunnel ea; been so much time and water under the bridge, I think I may get them mixed up haha. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#424](/thread/post/12610425#post12610425 "Post Permalink")

  * Nov 12, 2019 12:19am  Nov 12, 2019 12:19am 

  * [ Effax-square](effax-square)

  * | Joined Oct 2013  | Status: Trader | [34 Posts](/search?do=process&provider=Member&searchuser=352035)

> [Quoting radityo.ardi](/thread/post/12609713#post12609713 "View Quoted Post")
> 
> Disliked
> 
> {quote} Whoaaa.. I really didn't expect anyone from the past to reply, but I do really appreciate it!![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1) Excited to see your reply too, buddy! .
> 
> Ignored

welcome back my friend! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#425](/thread/post/12611294#post12611294 "Post Permalink")

  * Nov 12, 2019 1:16pm  Nov 12, 2019 1:16pm 

  * [ RevoTrader2](revotrader2)

  * | Joined Oct 2018  | Status: Trader | [7 Posts](/search?do=process&provider=Member&searchuser=721844)

> [Quoting radityo.ardi](/thread/post/12609713#post12609713 "View Quoted Post")
> 
> Disliked
> 
> {quote} For Grid, I've got no idea how to improve it. I'm so exhausted with ideas. I can throw a lot of grid ideas, but none of them can anticipate the switch between sideways and trending. The fact is, grid requires the trade to be on always (because it's the nature of grid trading, you get profit from a lot of orders, sometimes it goes over a week). When you want it to generate profit during sideways, you'll be stuck when it's at a strong trend (and it happened). When you want it to generate profit during trending, the fact is it's not always...
> 
> Ignored

I agree completely, which is why i added to your rdzgrid, i think i used base code 1.13?? The more recent ones used libraries, which constantly gave errors and didnt open trades when it should, so i went back to i am sure was 1.13.  
  
I added in abilities to limit the tradesizes, which eliminated the CreateOrder errors due to mgs getting out of hand ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1) , and also added a 1st and 2nd grid setting, so that the 1st grid trade opened at 150 point, and all other pendings open at 90 points Also... code to check that the open prices were accounting for stoplevels and such, whcih i dont need it anymore as i changed the first 2 trades to instant orders, so the stoplevel check is kinda redundant now, but anyways haha, also a setting to add the grid to the spread, which i dont use, but i have it there as an option that i might use on the higher spread pairs. I also check free margen and equity before attempting a new trade, and if freemargin is below XXX my lotsize for the new trade is limited to a teeny tiny size. This means that it will be a guaranteed loss, but a lot smaller loss than if i didnt open a new trade. And then on days when news events are occuring i always click the button on the chart that stops trading on close of the current cycle, eg rdz wont create a new cycle after the current trades all close. This forces me to check the market after end of the cycle and decide to open a new cycle or finish for the day. So i also have an indicator that opens an alert window when i have 0 trades open, so I know when i have to go back to computer to look at it. This is also setup so that the alert is pushed to my mobile mt4 on my phone. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#426](/thread/post/12612689#post12612689 "Post Permalink")

  * Nov 13, 2019 2:10am  Nov 13, 2019 2:10am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting RevoTrader2](/thread/post/12610213#post12610213 "View Quoted Post")
> 
> Disliked
> 
> very cool; yes I read your previous...previous post regarding C++ and cTrader vs mql4 and MT4, and while i agree with your comments completely, Mt4 and mql4 is still the main platform used for the desktop
> 
> Ignored

The reason is there is not many automated traders around. The demand for cTrader is way less than MT4. Not even MT5 can compare with MT4 in terms of number of users. That's where their money they can suck in.  
  

> [Quoting RevoTrader2](/thread/post/12610213#post12610213 "View Quoted Post")
> 
> Disliked
> 
> so while I will be very curious to follow your coding; I will have to try converting it to mql4 for my own use ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1) as cTrader
> 
> Ignored

Good luck, bro. I can't easily convert C# to mql, especially when someone is using LINQ for arrays. We can easily convert mql to C# but difficult otherwise. My new code uses LINQ as it's simple dealing with arrays. It's just requires too much of efforts. Anyway, the concept's the same. Just that I open orders based on preset date time from a JSON file, nothing special with the new TM.  
  

> [Quoting RevoTrader2](/thread/post/12610213#post12610213 "View Quoted Post")
> 
> Disliked
> 
> as good as the plusses it has over mt4, mt4 does not have any negatives that i am aware of that may have any effect or any negative effects on my current trading.
> 
> Ignored

No negative effects. Just the "terms & conditions" linked to the account only.  
  

> [Quoting RevoTrader2](/thread/post/12610213#post12610213 "View Quoted Post")
> 
> Disliked
> 
> However the first reason i fell in love with rdzgridtraps was the on screen button
> 
> Ignored

No button can be added in cTrader apparently. But it's not really needed, as I can write OnStop event to close 'em all. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#427](/thread/post/12612696#post12612696 "Post Permalink")

  * Nov 13, 2019 2:12am  Nov 13, 2019 2:12am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting RevoTrader2](/thread/post/12611294#post12611294 "View Quoted Post")
> 
> Disliked
> 
> {quote} I agree completely, which is why i added to your rdzgrid, i think i used base code 1.13?? The more recent ones used libraries, which constantly gave errors and didnt open trades when it should, so i went back to i am sure was 1.13. I added in abilities to limit the tradesizes, which eliminated the CreateOrder errors due to mgs getting out of hand ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1) , and also added a 1st and 2nd grid setting, so that the 1st grid trade opened at 150 point, and all other pendings open at 90 points Also... code to check that the open prices were accounting...
> 
> Ignored

Wooow..that's complex dude. I think the bottom line is grid is profitable, just don't put too much weight on it. That's a good concept, do a trade, call it a day and close it, try win some other time, profitable, then repeat.  
  
Are you still using it till today? 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#428](/thread/post/12612699#post12612699 "Post Permalink")

  * Nov 13, 2019 2:13am  Nov 13, 2019 2:13am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting Effax-square](/thread/post/12610425#post12610425 "View Quoted Post")
> 
> Disliked
> 
> {quote} welcome back my friend!
> 
> Ignored

Thanks brotha! 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#429](/thread/post/12613291#post12613291 "Post Permalink")

  * Nov 13, 2019 10:06am  Nov 13, 2019 10:06am 

  * [ RevoTrader2](revotrader2)

  * | Joined Oct 2018  | Status: Trader | [7 Posts](/search?do=process&provider=Member&searchuser=721844)

> [Quoting radityo.ardi](/thread/post/12612696#post12612696 "View Quoted Post")
> 
> Disliked
> 
> {quote} Wooow..that's complex dude. I think the bottom line is grid is profitable, just don't put too much weight on it. That's a good concept, do a trade, call it a day and close it, try win some other time, profitable, then repeat. Are you still using it till today?
> 
> Ignored

I was using it til June. And non trading life has picked up since then, otherwise I would be still using it on gbpusd right now. Grid being grid ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1), I found it did great so long as I was near the computer at almost all times to baby sit, which I was having too much fun with non trading life, so I have not used it since June, all manual stuff since then, albeit I do grid like manual trading anyways haha, you and rdzgrid has made a very big impression on me. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#430](/thread/post/12613449#post12613449 "Post Permalink")

  * Nov 13, 2019 12:40pm  Nov 13, 2019 12:40pm 

  * [ RevoTrader2](revotrader2)

  * | Joined Oct 2018  | Status: Trader | [7 Posts](/search?do=process&provider=Member&searchuser=721844)

> [Quoting radityo.ardi](/thread/post/12612689#post12612689 "View Quoted Post")
> 
> Disliked
> 
> {quote} Good luck, bro. I can't easily convert C# to mql, especially when someone is using LINQ for arrays. We can easily convert mql to C# but difficult otherwise. My new code uses LINQ as it's simple dealing with arrays. It's just requires too much of efforts. Anyway, the concept's the same. Just that I open orders based on preset date time from a JSON file, nothing special with the new TM. {quote} No negative effects. Just the "terms & conditions" linked to the account only. {quote} No button can be added in cTrader apparently. But it's not really...
> 
> Ignored

Maybe I can get or create a mt4 bridge. But am not concerned with that right now, and yeah, no real need for a button if you just have a setting in the ea or cBot setttings to stop after the X cycle has closed. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#431](/thread/post/12613618#post12613618 "Post Permalink")

  * Nov 13, 2019 3:37pm  Nov 13, 2019 3:37pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar184969_4.gif) cTrader](ctrader)

  * | Commercial User  | Joined Jul 2011 | [136 Posts](/search?do=process&provider=Member&searchuser=184969)

> [Quoting radityo.ardi](/thread/post/12612689#post12612689 "View Quoted Post")
> 
> Disliked
> 
> {quote} No button can be added in cTrader apparently. But it's not really needed, as I can write OnStop event to close 'em all.
> 
> Ignored

Hi radityo.ardi,  
  
You can add buttons in cTrader. Check the new features [added in 3.6](https://ctrader.com/forum/announcements/21629).  
  
Best Regards,  
cTrader Team 

cTrader & cAlgo - The New Standards in FX Trading

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#432](/thread/post/12614286#post12614286 "Post Permalink")

  * Nov 13, 2019 9:12pm  Nov 13, 2019 9:12pm 

  * [ RevoTrader2](revotrader2)

  * | Joined Oct 2018  | Status: Trader | [7 Posts](/search?do=process&provider=Member&searchuser=721844)

> [Quoting radityo.ardi](/thread/post/12612696#post12612696 "View Quoted Post")
> 
> Disliked
> 
> {quote} Wooow..that's complex dude.
> 
> Ignored

Well, that all happened over about 18 months, so it was a work in progress for all dat time. I am only disappointed that I wasnt able to share it with you before now and get your extra insights and advice on improving it before now. It isnt on my platforms now as the last couple mt4 updates screwwed wih it on the last live platform i had it on. When i am on hols next am going to test and fix the trouble. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#433](/thread/post/12615683#post12615683 "Post Permalink")

  * Nov 14, 2019 2:57pm  Nov 14, 2019 2:57pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting RevoTrader2](/thread/post/12613449#post12613449 "View Quoted Post")
> 
> Disliked
> 
> {quote} Maybe I can get or create a mt4 bridge. But am not concerned with that right now, and yeah, no real need for a button if you just have a setting in the ea or cBot settings to stop after the X cycle has closed.
> 
> Ignored

I did my research for mt4 bridge, not good in my opinion. Most of them paid (didn't get a chance to test it out), some other which is free, are mostly using network protocol to exchange information between MQL code and C#. The main problem is latency. While the bridge will take time to pick up the instruction from C# code (coz essentially it's using network protocol which will "listen" to instructions), the execution of the order inside MQL itself will also take time. Note: MetaTrader doesn't allow you open order asynchronously. One instruction to open an order must be finished before you can open another order. In cTrader, you can do simultaneously.  
I need that millisecond performance... 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#434](/thread/post/12615684#post12615684 "Post Permalink")

  * Nov 14, 2019 2:58pm  Nov 14, 2019 2:58pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting cTrader](/thread/post/12613618#post12613618 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi radityo.ardi, You can add buttons in cTrader. Check the new features [added in 3.6](https://ctrader.com/forum/announcements/21629). Best Regards, cTrader Team
> 
> Ignored

Didn't know that buttons natively supported. But hey, it's C#, we can pump up a button anywhere. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#435](/thread/post/12943672#post12943672 "Post Permalink")

  * Edited 3:45am  May 16, 2020 3:20am | Edited 3:45am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

Just a stupid idea, after multitude tests. I hope pictures can explain better.  

Attached Image

![](/attachment/image/3636842?d=1589566612)

  
  
Let it flow wherever it goes...  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot2.png
Size: 204 KB](/attachment/image/3636844/thumbnail?d=1589566749)](/attachment/image/3636844?d=1589566749)   

  
  
Then close wherever you want.  
  
The catch here is, you must run this only **once** at any particular time (usually when the high impact news is released)!  
  
Now, here is the deal. I've spent so much time on writing code playing around with all parameters and stuffs like that. It's like breadcrumb pieces, where I got the fact that:

  1. Price is always unpredictable (unless if you want to learn how to predict it, which makes your profitability higher).
  2. Price is always moving, especially when the market opens, some news released, or any high-impact stuff.
  3. Tunnel Martingale is now capable of setting Ceiling and Floor with Stop Orders (not executed, until the price is reached).

But I kept myself enclosed in a box that:

  1. I need to limit my profit and call it a day.
  2. I missed a huge movement.
  3. It's a martingale, you can't keep it running for so long.
  4. Your risk doubles as it progresses forward.

One key thing is, yes, your risk doubles, but your profit movement per pips also doubles.  
  
Just a brief info, backtesting is using:

  1. $1000 capital
  2. StartingLotSize 1.00
  3. Multiplier 2 (each lot size will be multiplied by 2)
  4. Tunnel height 200
  5. no stop loss

  
When I do that, I get $108 from perfect 4 trades (you see only one of them below).  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot2.png
Size: 251 KB](/attachment/image/3636858/thumbnail?d=1589567412)](/attachment/image/3636858?d=1589567412)   

  
So much movement missed.  
  
But when I took off the target, let it run...I get $919 from 2 trades.  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot3.png
Size: 275 KB](/attachment/image/3636863/thumbnail?d=1589567717)](/attachment/image/3636863?d=1589567717)   

  
  
For sure this is just backtesting. Interesting enough if I can put forwardtesting in the factor (maybe throw in some real $50 to the test). 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#436](/thread/post/12948720#post12948720 "Post Permalink")

  * May 19, 2020 1:07pm  May 19, 2020 1:07pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

Now,  
here is what I see that you don't see.  
  
A price for EURUSD always moves, from point A to point B, almost daily basis. Why is that?  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot1.png
Size: 208 KB](/attachment/image/3639293/thumbnail?d=1589860918)](/attachment/image/3639293?d=1589860918)   

  1. Because of a lot of people doing the bidding for EURUSD almost daily, on a regular basis, and at the same time.
  2. One may do trade during European time, one at US time.
  3. That's why you see the volume (in the chart above) getting more interesting at certain times.
  4. A few occasions it shoots up high, this is something we want to catch with martingale.
  5. Some just go up and down then back to the initial position, this is something we willing to take a loss and move on.

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#437](/thread/post/12949062#post12949062 "Post Permalink")

  * May 19, 2020 4:35pm  May 19, 2020 4:35pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

On that basis, here is the WRONG conception of Martingale:

  1. Doing the trade almost anytime, one to another, back to back.
  2. You think martingale is to double the risk of getting losses wider, just for a small piece of the profit.
  3. Doing the martingale trade in unlimited duration.
  4. Holy Grail is real.

And here is what I thought would be the best strategy for Martingale:

  1. Do the trade ONCE a day only.
  2. When you think the risk is doubled, don't forget that the profit potential is also doubled. Take the profit as much as you can if the price is in your favor, to cover the future losses.
  3. Don't start the trade first, put some trap. Do something like Price Action trader would do, the only difference is martingale is a little bit stupid. You don't calculate, you don't predict, you don't assume. Just put and let it run.
  4. Do in very limited duration, take profit/loss for the day then continue afresh for tomorrow. This is the mindset that most people forget, but it's in their minds already. Just like a very professional trader, they always stop trading, be it winning or losing, then continue tomorrow.
  5. Don't trade if one side (EUR or USD) is on a holiday (Bank Holiday, or any holidays).
  6. Holy Grail is not real, no trading strategy will give you win all the time. It's the risk management you can count on.

  
After years looking at the best method for martingale, I can confidently say I have found one, **but this is still far from perfect**. The risk is still there and needs a couple of tests in the long run.  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot1.png
Size: 37 KB](/attachment/image/3639462/thumbnail?d=1589873809)](/attachment/image/3639462?d=1589873809)   

  
Above backtested from 20th April to 8th May 2020, I am trying to run full test 1 year backward. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#438](/thread/post/12960499#post12960499 "Post Permalink")

  * May 25, 2020 1:14am  May 25, 2020 1:14am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

Just an update, I took notes during my backtesting, carefully looking at the FF calendar, filter out the currency I like (EURUSD), and tag the news type. Here is what I found interestingly can be attached to Tunnel Martingale.  
\- Unemployment Claims  
\- Flash Manufacturing PMI  
\- FED Announcement (Red one) - this also imposes better movement over other red high-impact news nearby the time  
\- ADP Non-Farm Employment Change (careful, sometimes sideways)  
\- Non-Farm Employment Change & Unemployment Rate (15 minutes before, 20:15pm)  
\- CPI m/m & Core CPI m/m  
\- Retail Sales m/m & Core Retail Sales m/m  
\- German ifo Business Climate? maybe?  
\- Spanish Unemployment Rate  
\- Advance GDP q/q & Advance GDP Price Index q/q  
\- ISM Manufacturing PMI  
\- German Constitutional Court Ruling  
\- President Trump Speaks about economic after 14:00 to 22:00, no other stuff  
\- Surprisingly, Building Permits gains some movement  
\- ECB Press Conference  
\- if a lot of EUR high-impact news on 16:00, set the timer to 14:00 instead  
  
And have settled through all the types of news backtested until the early week of March 2020. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#439](/thread/post/12965981#post12965981 "Post Permalink")

  * May 27, 2020 8:26pm  May 27, 2020 8:26pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

OK, just to settle in on what's going on with Tunnel Martingale from the last update.  
  
For those who don't follow, let's get a refresher. Tunnel Martingale basically consist of 2 main things: Ceiling, Floor. Both are the price line which guards if the price goes towards past Ceiling, it will put pending order on the Floor 2 times lot size of the previous (Ceiling). If this pending order gets executed, it will then again add pending order on the Ceiling 2 times lot size if the Floor. Until then it breaks out, (in example 0.16 of the lot size), it will take the profit and repeat from start all over again.  

Attached Image

![](/attachment/image/3647683?d=1590578742)

  
  
**Moving to cTrader**  
The reason for this is obviously the expanding logic of Tunnel Martingale can't be accommodated within Metatrader which the base programming language is C++. I mean, I am a full-time application developer obviously and there's a reason why I choose C# over C++ (it's an old programming language that's just like that, never got so much update). C# is an expanding universe, coding with it is so robust, quick, fast, it lets us focus on creative ideas more, rather than focusing on building unnecessary components to achieve the idea.  
Let me get a simple analogy, "you want to go to New York from Seattle". With C#, you've already got your components ready to be used like "cars", "motorcycle", "trains", "buses", "airplanes", just use it. Maybe in the future will get "teleport", in C# will get it. While with C++, no one is going to build for you, you need to build those transportation modes from scratch & handmade!  
  
**It's not your typical martingale, more enhanced**  
My last Tunnel Martingale in Metatrader 4, it's like running continuously non-stop. And this is the **ABSOLUTELY WRONG** method of doing it! The main reason is, the market is **unpredictable**. But, as I move forward from time to time to realize, the market is actually not that unpredictable. _You can't predict the unpredictable, but you must predict what's predictable_. The "**WHERE** it will move" (upward, downward, or sideways) is **unpredictable** , but the "**WHEN** it will move" is **predictable**.  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: 2020-05-27_15-42-00.png
Size: 130 KB](/attachment/image/3647685/thumbnail?d=1590578749)](/attachment/image/3647685?d=1590578749)   

  
  
Example: EURUSD will never make its move during the wee hours, it'll just sideways. But it will move commonly after high-impact news are released, or without news but just common opening time of a specific market (2-3 pm of my Singapore time, for EURUSD, see screenshot above). I don't care whether it will go up or down, as long as it moves toward one direction and not sideways.  
  
The problem I found with the previous version of Tunnel Martingale:

  1. it runs continuously, which is bad. Sometimes, the market just going sideways especially in the wee hours.
  2. Since it runs continuously, you will frequently face the sideways stuff. The more it gets into sideways, the larger the lot size you need, the bigger the risk, the more difficult you get out, the easier you get stuck and finally withdrawn so much blood!

  
As I get the rough idea to improve Tunnel Martingale, I had to play with an array of objects, a configuration that reads from a text file (presumably JSON file, since the idea is complex the configuration will be complex too). None of these is instantly available in Metatrader. I had to download/use external libraries, written by another folk that is also (probably) the code is not maintained for years/decades. While in cTrader, it's based on C#, the base .NET framework already fulfil my needs!  
  
**The questions that were rolling around my mind (these years)**

  1. How can I put Risk Management concept in this Tunnel Martingale? Does it just like the typical risk management where we put small lot size for a larger investment?
  2. Can I put 2 pending orders X pips above and below the current price? Then whichever pending orders executed (after it gets touched) will be the first tunnel line (either ceiling or floor)?
  3. Can I have this sliced as sessions in which I can tag each session to a certain date and time?
  4. Can I limit the session into X number of cycles (from 0.01 lot size to X.XX until it turns profit)?
  5. Can I close all the positions regardless of profit or not, in order to limit the exposure of risk generated by the martingale?
  6. If my first position is active (i.e. SELL) then the price against it until the second position is active (i.e. BUY), then it turns back to the first position's favor again, can I cancel the second position and compound the losses and consider it into the profit?
  7. If the session closed prematurely (due to the certain expiry date or similar concept), can I compound the losses into the next session, so that I am not in losses?

Now, here's the idea which currently has been incorporated into the new Tunnel Martingale (in cTrader) of course:

  1. Traps  
If you set TM running mode as Traps, it will NOT start the martingale immediately (no 2 below). It will set pending orders above + below the current price with the initial lot size. IF for example it goes up and the upper pending order is activated, then the pending order below will be canceled and replaced with 2 times of the lot size of the first position. Then from this point, the martingale starts (no 3 below).  

Attached Image

![](/attachment/image/3647684?d=1590578742)

  2. Session Dates  
Now, this is a new concept that has been thought for so long since **2 years past**! But I can't do it in Metatrader MQL as the programming language which is C++ is too vintage to accommodate my logic. I want to have an array of dates to which I want to _trade this Tunnel Martingale at a certain date and time and only once_.  
This means, I will have time once a month, defining the date + time I want to trade, based on FF calendar. Once set up for this month, then I will let it run through the month independently and host it in the Virtual Private Server. Why this Session Dates?  
  
Because a lot of occurrences happen when the market actually moves high pips after high-impact news is being released, even on standard open time for EURUSD that is 1400hrs on my local time. Who wouldn't want to catch that with this Tunnel Martingale? I do!  
You can take a look at historical data, any broker, on that specific date and time.
  3. Close Orders after a session finished  
Now, this idea just brought recently in the past few weeks. This is the risk management concept in this TM. So, if from each session date there is no profit or it's hanging (not closing) for profit, based on the specified "end time", it will close all the orders, regardless of whether it's profitable or not. Then tomorrow (or the next session date) can start afresh.  
For example, you can start to run a session today at 14:00 which will last for 3 hours, so 17:00 will be the end time. If within these 3 hours, it got reached the profit, it will close all of course, as per normal. If not, then it will wait until 17:00 to close all automatically.

I will tell you about SmartBucket and Compounding SmartBucket next time. I'm exhausted.... sorry. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#440](/thread/post/12966378#post12966378 "Post Permalink")

  * May 27, 2020 10:40pm  May 27, 2020 10:40pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar606368_2.gif) penyuperwira](penyuperwira)

  * Joined Aug 2017 | Status: Trader | [110 Posts](/search?do=process&provider=Member&searchuser=606368)

Wow... very detailed explanation... This is interesting  
Thanks for sharing this ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Trapping System: Tunnel Martingale
  *   * [ **Reply to Thread** ](/thread/524198-trapping-system-tunnel-martingale/reply#reply)

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

[Martingale, Anti-martingale, and Compounding](/thread/571233-martingale-anti-martingale-and-compounding "Hi all traders, 
i started this thread to meet others people interested in money management. 
We all know that martingale strategies are...") 40 replies

[Martingale, Reverse Martingale, Modified Martingale, Maths](/thread/736165-martingale-reverse-martingale-modified-martingale-maths "Hi all, so Martingale has been a risky yet maybe non profitable system. While roulette has an edge of \(2.7%/5.4%\) 
  
Inspired by Adam...") 1 reply

[How to change this Martingale to Reverse Martingale ?](/thread/546755-how-to-change-this-martingale-to-reverse-martingale "How to change this Martingale to Reverse Martingale ?") 3 replies

[Trapping System: Way to Fully-Automated Trading System](/thread/509226-trapping-system-way-to-fully-automated-trading-system "Hi fellow Traders! 
This is my first time to write a new thread. Would like to share a trading method, which at least made me happy right...") 47 replies

[Martingale vs. Non Martingale (Simplified RoR vs Profit)](/thread/526308-martingale-vs-non-martingale-simplified-ror-vs-profit "Martingale: The gambler doubles his bet after every loss... 
  
Martingale vs. Non Martingale \(Simplified RoR vs Profit in 3 trade runs...") 1 reply

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/524198-trapping-system-tunnel-martingale/reply#reply)
  * Subscribe
  * [221](javascript:void\(0\);)

Attachments: Trapping System: Tunnel Martingale

Tags: Trapping System: Tunnel Martingale

#  [](/thread/524198-trapping-system-tunnel-martingale)Trapping System: Tunnel Martingale 

  * 

  * [#441](/thread/post/12968459#post12968459 "Post Permalink")

  * May 28, 2020 8:44pm  May 28, 2020 8:44pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

Now, let's talk about Smart Bucket. This is getting interesting ![](https://resources.faireconomy.media/images/emojis/64/1f605.png?v=15.1)  
The idea is to compound in the piggy bank, the losses you suffer for the past trades, and then add it up to the next trade's target profit. This means if the previous/current trade is in the loss for $5 and closed due to a condition in the configuration, the losses will be added into the bucket. More loss for another $5, add again into the bucket which in total would be $10. If your target profit is $20, then for the next session/cycle, your target profit would be $30 ($20 from target profit, and $10 from the bucket).  
Practically saying, your previous losing trades will be "zero"-ed once the target is reached.  
  
There are 2 types of Smart Bucket: Normal Smart Bucket, and Martingale Smart Bucket (this one is experimental).  
So, these Smart Bucket essentially is only for mitigating the loss suffered. In a quick short word, take the loss now, convert into no loss on the next trade. If they still got the loss, accumulate again the loss and convert into no loss on the next trade, so on so forth.  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: TM-SmartBucket.png
Size: 51 KB](/attachment/image/3648886/thumbnail?d=1590666235)](/attachment/image/3648886?d=1590666235)   

  
Imagine the picture above (no 5). If the price moves and executes both 1st and 2nd order into positions, when the price move past the center (A), it will close the 0.02 position with loss and put the loss amount (in non-negative) into the bucket. And this bucket will be considered into the profit taking too (as described above).  
If price goes up till (B), it will not close the cycle and continue. Because essentially, it's not reached the needed take profit as there's addition from the bucket. But say if price goes to (C) with considering the bucket, it will close the cycle. At this point, the previous loss trade "converted" into no-loss or $0 trade. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#442](/thread/post/12968537#post12968537 "Post Permalink")

  * May 28, 2020 9:15pm  May 28, 2020 9:15pm 

  * [ Merka](merka)

  * Joined Jan 2016 | Status: Trader | [1,944 Posts](/search?do=process&provider=Member&searchuser=440568)

> [Quoting radityo.ardi](/thread/post/12965981#post12965981 "View Quoted Post")
> 
> Disliked
> 
> OK, just to settle in on what's going on with Tunnel Martingale from the last update. For those who don't follow, let's get a refresher. Tunnel Martingale basically consist of 2 main things: Ceiling, Floor. Both are the price line which guards if the price goes towards past Ceiling, it will put pending order on the Floor 2 times lot size of the previous (Ceiling). If this pending order gets executed, it will then again add pending order on the Ceiling 2 times lot size if the Floor. Until then it breaks out, (in example 0.16 of the lot size), it...
> 
> Ignored

I looked into this concept some years ago and never figured out how to reduce the risk.   
Maybe you will solve this issue 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#443](/thread/post/12974732#post12974732 "Post Permalink")

  * Jun 1, 2020 4:58pm  Jun 1, 2020 4:58pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar548123_2.gif) carddard](carddard)

  * Joined Jan 2017 | Status: Trader | [315 Posts](/search?do=process&provider=Member&searchuser=548123)

> [Quoting Merka](/thread/post/12968537#post12968537 "View Quoted Post")
> 
> Disliked
> 
> {quote} I looked into this concept some years ago and never figured out how to reduce the risk. Maybe you will solve this issue
> 
> Ignored

This is a treacherous path to go down indeed. It's something that I have spent a lot of time on (out of curiosity) on demo but never brought live, because of the fact that investors do not see this as viable investing. But or the hobby trader / gambler who has a higher risk profile, it is definitely fun to try out.  
  
There are ways to reduce your risk by cutting down on the number of open trades - but at the same time that exposes you to the current open leg (either buy or sell) and you need to constantly hedge the open order in hopes that there is enough volatility to bring you back on track.  
  
It also requires a certain amount of equity to trade more than a pair at any time in time. Another reason why I refused to bring this to live.  
  
But as a mental exercise, it is very fun to play around with. If anyone has enough guts to try it out on live, I'm willing to share! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#444](/thread/post/12976759#post12976759 "Post Permalink")

  * Jun 2, 2020 2:37pm  Jun 2, 2020 2:37pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting carddard](/thread/post/12974732#post12974732 "View Quoted Post")
> 
> Disliked
> 
> {quote} This is a treacherous path to go down indeed. It's something that I have spent a lot of time on (out of curiosity) on demo but never brought live, because of the fact that investors do not see this as viable investing. But or the hobby trader / gambler who has a higher risk profile, it is definitely fun to try out. There are ways to reduce your risk by cutting down on the number of open trades - but at the same time that exposes you to the current open leg (either buy or sell) and you need to constantly hedge the open order in hopes that...
> 
> Ignored

I do agree martingale has its risk. But isn't it the same concept with other trading systems as well?  
  
Just think of this, someone posted what claimed to be a winning strategy, then another too with another strategy, but all of these I found 1 thing in common. They have **entry requirements**. If not followed, then the strategy won't work. The funny part is that most of us ignore the fact that martingale does require entry requirements. Am I right?  
  
When I walk past MRT or public transport and sees the advertisement about investing in this, that, whatever, those always with one distinctive fine print: "**Investments are subject to investment risks. The risk of loss in leveraged trading can be substantial. You may sustain losses in excess of your initial funds.** " or anything along that line.  
  
Another example, when you trade EURUSD with technicals, say you use 2 EMA and 1 BB. Your signal tells you to buy, but then you would have another requirement that this strategy only works perfectly when you trade during EURUSD trading window. Other than that, it won't work nicely. Isn't it the same like when you apply martingale, but only at the time when a news has been released? Isn't it the same?  
Of course we could say, it's not the same. But what are the other similarities between those? What about something like can I set up the entry price for martingale the top and bottom? Of course if you set the top and bottom too tight, you would end up in bleeding your own account. But what if we can find the best distance between the top and bottom to work this out? Isn't this the same as we apply technicals where the EMA period parameters one is 14 and another is 50?  
I'm just saying it's not fair for people to say martingale is gambling and others are not.  
  
Then some other time, someone experienced (just an example to show you the idea, which I've also encountered in real life in the past) "okay, I'm using 2 EMA and 1 BB. Year 2015 until last year it was working perfectly. This year, it's in bad shape. this strategy doesn't work throughout the time". Well, then we all are in fact gambling our money out. We all do if you see the bold line which the advertisement forex company put on.  
  
  
We need to realize the fact that every single strategy (fundamentals, technicals, including martingale since it's considered algorithmic) in this world, pose a risk and each of them has their own requirements in order to make profits. These are facts we should not ignore.  
  
Now the question is, how do we reduce risks in martingale? 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#445](/thread/post/12976764#post12976764 "Post Permalink")

  * Jun 2, 2020 2:48pm  Jun 2, 2020 2:48pm 

  * [ goodways100](goodways100)

  * Joined Dec 2013 | Status: Trader | [615 Posts](/search?do=process&provider=Member&searchuser=358325)

I like to learn. But too busy trading. Will comment later. Thanks and  
Regards 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#446](/thread/post/12976783#post12976783 "Post Permalink")

  * Jun 2, 2020 3:07pm  Jun 2, 2020 3:07pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar548123_2.gif) carddard](carddard)

  * Joined Jan 2017 | Status: Trader | [315 Posts](/search?do=process&provider=Member&searchuser=548123)

> [Quoting radityo.ardi](/thread/post/12976759#post12976759 "View Quoted Post")
> 
> Disliked
> 
> {quote} I do agree martingale has its risk. But isn't it the same concept with other trading systems as well? Just think of this, someone posted what claimed to be a winning strategy, then another too with another strategy, but all of these I found 1 thing in common. They have entry requirements. If not followed, then the strategy won't work. The funny part is that most of us ignore the fact that martingale does require entry requirements. Am I right? When I walk past MRT or public transport and sees the advertisement about investing in this, that,...
> 
> Ignored

Don't get me wrong radityo.ardi, I completely agree that all strategies have inherent risk. No doubt the entry / exit requirements matter like in any strategy. I'm not challenging that. It's a personal preference of how much risk you want to undertake and in what form. My problem with this is that the absolute risk profile is not the only constraint that I am working within. The amount of **capital** and **margin requirements** matter as well.  
  
What I mean by this is, if I want to put my money between these 2 options:  
  
1) Open 1 trade of 0.01 lot each for 28 pairs  
2) (1) but with multiple entries with varying lots on 28 pairs  
  
I would almost always go for (1) because firstly I spread my exposure around different pairs and I know that in the worst case scenario, I always have only 1 trade (or 2, depending on whether you buy / sell at the same time). From an outsider point of view, it is also easier to attract investors because there is no overexposure in any particular instrument. That is also why I said that however, this is an interesting experiment to try out regardless of how attractive it is to investors, because it's an intellectually stimulating exercise and nothing is more exciting than an unorthodox method that proves the critics wrong.  
  
I have spent countless hours on trying to crack the martingale puzzle and quite literally have hundreds of algorithms just based on hedging / martingale but have not used any of them live because of the reasons stated above.  
  
With that said, I would still love to see how this progresses because I like to keep an open mind when it comes to retail trading. Never say never! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#447](/thread/post/12976785#post12976785 "Post Permalink")

  * Jun 2, 2020 3:08pm  Jun 2, 2020 3:08pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting Merka](/thread/post/12968537#post12968537 "View Quoted Post")
> 
> Disliked
> 
> {quote} I looked into this concept some years ago and never figured out how to reduce the risk. Maybe you will solve this issue
> 
> Ignored

because all of us think that martingale will solve all problems without us thinking through what's the entry requirement. It's a wrong mindset (me too in the past). So, we tend to think martingale has to be run all the time ignoring all the hurdles and quiet hours. We tend to think to take profit small, then do another round again next time.  
  
1 thing for sure, every news is released, the price always go to somewhere new and sit there for some time till another news is released. Sometimes mixed up, goes up there, then go down, but the range is not that something like sideways. Sometimes this can go like 100 pips - 400 pips. One day this year EURUSD reaches 1400 pips a day!  
Imagine that if you put martingale _at the right time_ let it move a bit (to execute another few pending orders) then shoot that 1400 pips without you closing the order. How much profit you will get? You can stop your martingale after that day and go to Bali.  
  
Martingale doubles your risk when it's not on your side, but once it shoots up and you let it go, your profit potential also doubles. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#448](/thread/post/12976791#post12976791 "Post Permalink")

  * Jun 2, 2020 3:15pm  Jun 2, 2020 3:15pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting goodways100](/thread/post/12976764#post12976764 "View Quoted Post")
> 
> Disliked
> 
> I like to learn. But too busy trading. Will comment later. Thanks and Regards
> 
> Ignored

  

> [Quoting carddard](/thread/post/12976783#post12976783 "View Quoted Post")
> 
> Disliked
> 
> {quote} Don't get me wrong radityo.ardi, I completely agree that all strategies have inherent risk. No doubt the entry / exit requirements matter like in any strategy. I'm not challenging that. It's a personal preference of how much risk you want to undertake and in what form. My problem with this is that the absolute risk profile is not the only constraint that I am working within. The amount of capital and margin requirements matter as well. What I mean by this is, if I want to put my money between these 2 options: 1) Open 1 trade of 0.01 lot...
> 
> Ignored

Yes, man. absolutely... ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
  
Anyway for both, I am doing this since no one is exploring much. So far the result is somewhat good, but I need more than what I'm seeing it currently. Gotta backtest it for at least the span of a year. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#449](/thread/post/12976795#post12976795 "Post Permalink")

  * Jun 2, 2020 3:18pm  Jun 2, 2020 3:18pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar548123_2.gif) carddard](carddard)

  * Joined Jan 2017 | Status: Trader | [315 Posts](/search?do=process&provider=Member&searchuser=548123)

> [Quoting radityo.ardi](/thread/post/12976791#post12976791 "View Quoted Post")
> 
> Disliked
> 
> {quote} {quote} Yes, man. absolutely... ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) Anyway for both, I am doing this since no one is exploring much. So far the result is somewhat good, but I need more than what I'm seeing it currently. Gotta backtest it for at least the span of a year.
> 
> Ignored

I have some old ideas that I have tested and abandoned, let me see if I can dig them out - Who knows, it might come in handy, but happy to contribute in the discussion! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#450](/thread/post/12976841#post12976841 "Post Permalink")

  * Jun 2, 2020 3:53pm  Jun 2, 2020 3:53pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar548123_2.gif) carddard](carddard)

  * Joined Jan 2017 | Status: Trader | [315 Posts](/search?do=process&provider=Member&searchuser=548123)

> [Quoting radityo.ardi](/thread/post/12965981#post12965981 "View Quoted Post")
> 
> Disliked
> 
> OK, just to settle in on what's going on with Tunnel Martingale from the last update. For those who don't follow, let's get a refresher. Tunnel Martingale basically consist of 2 main things: Ceiling, Floor. Both are the price line which guards if the price goes towards past Ceiling, it will put pending order on the Floor 2 times lot size of the previous (Ceiling). If this pending order gets executed, it will then again add pending order on the Ceiling 2 times lot size if the Floor. Until then it breaks out, (in example 0.16 of the lot size), it...
> 
> Ignored

One of the ideas that I played around with in the past is to adopt a dynamic "tunnel" - The ceiling and the floor is not fixed to any single point, but adjusts according to price momentum. The shortfall of this is that the positions have to be managed at an equilibrium at all times - Meaning to say the orders are placed according to where the current price momentum is going towards, and we don't try to predict that direction because we can't. But that means that I had to find ways to close out these positions actively to avoid the accumulation of a series of too many unfavourable trades.  
  
This is an example of a build up of too many trades while holding on stubbornly until a profit target is reached.  
It's all fun and games in demo but in live it's something to shit your pants over. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: 1.JPG
Size: 241 KB](/attachment/image/3652491/thumbnail?d=1591080804)](/attachment/image/3652491?d=1591080804)   

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#451](/thread/post/12976867#post12976867 "Post Permalink")

  * Jun 2, 2020 4:05pm  Jun 2, 2020 4:05pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting carddard](/thread/post/12976841#post12976841 "View Quoted Post")
> 
> Disliked
> 
> {quote} One of the ideas that I played around with in the past is to adopt a dynamic "tunnel" - The ceiling and the floor is not fixed to any single point, but adjusts according to price momentum. The shortfall of this is that the positions have to be managed at an equilibrium at all times - Meaning to say the orders are placed according to where the current price momentum is going towards, and we don't try to predict that direction because we can't. But that means that I had to find ways to close out these positions actively to avoid the accumulation...
> 
> Ignored

Does that execute all the time, back-to-back one to another?  
I gotta know, to confirm that my findings are correct.  
  

> [Quoting carddard](/thread/post/12976841#post12976841 "View Quoted Post")
> 
> Disliked
> 
> until a profit target is reached.
> 
> Ignored

That is the sentence I've always had in mind, but actually you can "release" that and let it shoot all the way. Just like trailing stop does. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#452](/thread/post/12976878#post12976878 "Post Permalink")

  * Jun 2, 2020 4:10pm  Jun 2, 2020 4:10pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar548123_2.gif) carddard](carddard)

  * Joined Jan 2017 | Status: Trader | [315 Posts](/search?do=process&provider=Member&searchuser=548123)

> [Quoting radityo.ardi](/thread/post/12976867#post12976867 "View Quoted Post")
> 
> Disliked
> 
> {quote} Does that execute all the time, back-to-back one to another? I gotta know, to confirm that my findings are correct. {quote} That is the sentence I've always had in mind, but actually you can "release" that and let it shoot all the way. Just like trailing stop does.
> 
> Ignored

It may or may not, depending on the settings. If you want to tap on the higher volatility sessions, you can do that. In the screenshot, I restricted hours to the London / NY session. But to be fair, trades are left open until the next trading day.  
  
Reg. profit target - Yes agreed. We should use a trailing stop that would come in handy if prices continue to move favorably away from your reference point. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#453](/thread/post/12976900#post12976900 "Post Permalink")

  * Jun 2, 2020 4:17pm  Jun 2, 2020 4:17pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar548123_2.gif) carddard](carddard)

  * Joined Jan 2017 | Status: Trader | [315 Posts](/search?do=process&provider=Member&searchuser=548123)

> [Quoting radityo.ardi](/thread/post/12976867#post12976867 "View Quoted Post")
> 
> Disliked
> 
> {quote} That is the sentence I've always had in mind, but actually you can "release" that and let it shoot all the way. Just like trailing stop does. {quote}
> 
> Ignored

By the way - With both buy and sell trades open at the same time, how is your approach in determining the "average price" for the sum of these orders, so that you can establish a reference point for the trailing stop. With just buy orders or just sell orders it's straightforward. But with both legs going on at the same time, do you have any ideas? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#454](/thread/post/12976913#post12976913 "Post Permalink")

  * Jun 2, 2020 4:25pm  Jun 2, 2020 4:25pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting carddard](/thread/post/12976878#post12976878 "View Quoted Post")
> 
> Disliked
> 
> {quote} It may or may not, depending on the settings. If you want to tap on the higher volatility sessions, you can do that. In the screenshot, I restricted hours to the London / NY session. But to be fair, trades are left open until the next trading day. Reg. profit target - Yes agreed. We should use a trailing stop that would come in handy if prices continue to move favorably away from your reference point.
> 
> Ignored

ok noted.  
In my mind, martingale can't be run back-to-back, even if you limit the trading hours. IMO must be one trade at a time, when something we know potentially could yield large pips. Other than that, sideways of different sizes may occur and potentially lead to sucking up the risk we have. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#455](/thread/post/12976943#post12976943 "Post Permalink")

  * Jun 2, 2020 4:35pm  Jun 2, 2020 4:35pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting carddard](/thread/post/12976900#post12976900 "View Quoted Post")
> 
> Disliked
> 
> {quote} By the way - With both buy and sell trades open at the same time, how is your approach in determining the "average price" for the sum of these orders, so that you can establish a reference point for the trailing stop. With just buy orders or just sell orders it's straightforward. But with both legs going on at the same time, do you have any ideas?
> 
> Ignored

Trailing can't be managed by normal order as usual. It has to be managed inside the EA itself but still uses the same concept.  
Usually, trailing stop is attached to an order with some number of pips to be the "distance".  
  
Now, the trailing stop must be attached to the whole chain of orders by trailing NOT the pips, but the profit $. This must be managed inside the EA.  
  
  
Apart from that, below is just a backtest about CPI m/m and Core CPI m/m from Jan 2019 till May 2020. This is what I'm talking about...  
The summary of this specific martingale strategy is only 1 chain of trades at a time, at one specific time, then force it close either on target or after some duration.  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot1.png
Size: 199 KB](/attachment/image/3652513/thumbnail?d=1591083073)](/attachment/image/3652513?d=1591083073)   

  
I'm about to test the other type of news.  
  
Just don't look at the capital, $, profit, etc. Focus on the strategy requirements.  
If you can see on the equity chart above, most of the trades closes with 1 open position only. Except the one I put mark, apparently touches the ceiling, then the floor. But that's it. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#456](/thread/post/12976987#post12976987 "Post Permalink")

  * Jun 2, 2020 4:50pm  Jun 2, 2020 4:50pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar548123_2.gif) carddard](carddard)

  * Joined Jan 2017 | Status: Trader | [315 Posts](/search?do=process&provider=Member&searchuser=548123)

> [Quoting radityo.ardi](/thread/post/12976943#post12976943 "View Quoted Post")
> 
> Disliked
> 
> {quote} Trailing can't be managed by normal order as usual. It has to be managed inside the EA itself but still uses the same concept. Usually, trailing stop is attached to an order with some number of pips to be the "distance". Now, the trailing stop must be attached to the whole chain of orders by trailing NOT the pips, but the profit $. This must be managed inside the EA. Apart from that, below is just a backtest about CPI m/m and Core CPI m/m from Jan 2019 till May 2020. This is what I'm talking about... The summary of this specific martingale...
> 
> Ignored

Yes, I understand your point about the trailing stop. I guess using $ value increments is 1 way to trail the entire group. I can visualize how using a pip step (with a directional bias) could work as well, as long as the net profit continues to ascend according to the pip step. I'll find time to test it out in code.  
  
Noted on your approach - It's very similar to one of the ways I've tested in the past - With the ideal scenario being just closing with 1 open position with a regular trailing stop. Only when price moves unfavorably do I kick in a "tunnel martingale". 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#457](/thread/post/12977512#post12977512 "Post Permalink")

  * Jun 2, 2020 8:17pm  Jun 2, 2020 8:17pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar548123_2.gif) carddard](carddard)

  * Joined Jan 2017 | Status: Trader | [315 Posts](/search?do=process&provider=Member&searchuser=548123)

> [Quoting carddard](/thread/post/12976841#post12976841 "View Quoted Post")
> 
> Disliked
> 
> {quote} One of the ideas that I played around with in the past is to adopt a dynamic "tunnel" - The ceiling and the floor is not fixed to any single point, but adjusts according to price momentum. The shortfall of this is that the positions have to be managed at an equilibrium at all times - Meaning to say the orders are placed according to where the current price momentum is going towards, and we don't try to predict that direction because we can't. But that means that I had to find ways to close out these positions actively to avoid the accumulation...
> 
> Ignored

As opposed to a fixed $ closure, I've added a group trailing stop and TP is relying solely on that.  
The equity profile looks something like this. You will notice the steeper incline during each group close.  
I think another viable way to do this is using the most recent swing high / low, instead of a fixed pip step. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: 1.JPG
Size: 257 KB](/attachment/image/3652750/thumbnail?d=1591096613)](/attachment/image/3652750?d=1591096613)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#458](/thread/post/12979239#post12979239 "Post Permalink")

  * Jun 3, 2020 1:28pm  Jun 3, 2020 1:28pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting carddard](/thread/post/12977512#post12977512 "View Quoted Post")
> 
> Disliked
> 
> {quote} As opposed to a fixed $ closure, I've added a group trailing stop and TP is relying solely on that. The equity profile looks something like this. You will notice the steeper incline during each group close. I think another viable way to do this is using the most recent swing high / low, instead of a fixed pip step. {image}
> 
> Ignored

Did you change any of the test parameters? I hope not.  
last time I see equity reaches down towards 2K which is not good. Now the risk is somewhat acceptable from my point of view. Congrats! 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#459](/thread/post/12979332#post12979332 "Post Permalink")

  * Jun 3, 2020 2:51pm  Jun 3, 2020 2:51pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar548123_2.gif) carddard](carddard)

  * Joined Jan 2017 | Status: Trader | [315 Posts](/search?do=process&provider=Member&searchuser=548123)

> [Quoting radityo.ardi](/thread/post/12979239#post12979239 "View Quoted Post")
> 
> Disliked
> 
> {quote} Did you change any of the test parameters? I hope not. last time I see equity reaches down towards 2K which is not good. Now the risk is somewhat acceptable from my point of view. Congrats!
> 
> Ignored

Nope, didn't change the parameters. Yeah I guess it helps to trail profit but the pre-requisite of having enough volatility and movement is important. Otherwise it would continue to bounce off the same region for a while and accumulate open lots. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#460](/thread/post/13431107#post13431107 "Post Permalink")

  * Mar 1, 2021 3:14am  Mar 1, 2021 3:14am 

  * [ MavecoDoido](mavecodoido)

  * | Joined Mar 2021  | Status: Trader | [1 Post](/search?do=process&provider=Member&searchuser=1072884)

> Quote
> 
> Disliked
> 
> As opposed to a fixed $ closure, I've added a group trailing stop and TP is relying solely on that.  
>  The equity profile looks something like this. You will notice the steeper incline during each group close.  
>  I think another viable way to do this is using the most recent swing high / low, instead of a fixed pip step.

  
carddard, could you send the parameters you are using to get to the BT shown above?  
Anyone with good and consistent results?  
  
Tks 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Trapping System: Tunnel Martingale
  *   * [ **Reply to Thread** ](/thread/524198-trapping-system-tunnel-martingale/reply#reply)

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

[Martingale, Anti-martingale, and Compounding](/thread/571233-martingale-anti-martingale-and-compounding "Hi all traders, 
i started this thread to meet others people interested in money management. 
We all know that martingale strategies are...") 40 replies

[Martingale, Reverse Martingale, Modified Martingale, Maths](/thread/736165-martingale-reverse-martingale-modified-martingale-maths "Hi all, so Martingale has been a risky yet maybe non profitable system. While roulette has an edge of \(2.7%/5.4%\) 
  
Inspired by Adam...") 1 reply

[How to change this Martingale to Reverse Martingale ?](/thread/546755-how-to-change-this-martingale-to-reverse-martingale "How to change this Martingale to Reverse Martingale ?") 3 replies

[Trapping System: Way to Fully-Automated Trading System](/thread/509226-trapping-system-way-to-fully-automated-trading-system "Hi fellow Traders! 
This is my first time to write a new thread. Would like to share a trading method, which at least made me happy right...") 47 replies

[Martingale vs. Non Martingale (Simplified RoR vs Profit)](/thread/526308-martingale-vs-non-martingale-simplified-ror-vs-profit "Martingale: The gambler doubles his bet after every loss... 
  
Martingale vs. Non Martingale \(Simplified RoR vs Profit in 3 trade runs...") 1 reply

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/524198-trapping-system-tunnel-martingale/reply#reply)
  * Subscribe
  * [221](javascript:void\(0\);)

Attachments: Trapping System: Tunnel Martingale

Tags: Trapping System: Tunnel Martingale

#  [](/thread/524198-trapping-system-tunnel-martingale)Trapping System: Tunnel Martingale 

  * 

  * [#461](/thread/post/13508501#post13508501 "Post Permalink")

  * Apr 23, 2021 8:21pm  Apr 23, 2021 8:21pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar433570_3.gif) simnz](simnz)

  * Joined Nov 2015 | Status: Trader | [2,525 Posts](/search?do=process&provider=Member&searchuser=433570)

> [Quoting broketrader](/thread/post/8228609#post8228609 "View Quoted Post")
> 
> Disliked
> 
> Hi radityo, It's always interesting for me following people doing studies on martingales. I have done a lot of work myself on this subject and still working on it and if you allow me, I would like to share my findings, maybe they will be useful for you too. 1. Trading from London open to NY close is the right way to go at least for EUR/USD/GBP. 2. You should maybe consider not allowing new trades during NY news hours. 3. If I have understood, your EA makes symmetric trades eg. 20 pip TP, 20 pip SL You should consider making it asymmetric eg. 15...
> 
> Ignored

Looking for your review of this EA. MQL is provided.  
[https://www.forexfactory.com/thread/...9#post13508389](https://www.forexfactory.com/thread/post/13508389#post13508389)

Practice makes a person perfect

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#462](/thread/post/13510733#post13510733 "Post Permalink")

  * Apr 26, 2021 2:24pm  Apr 26, 2021 2:24pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar548123_2.gif) carddard](carddard)

  * Joined Jan 2017 | Status: Trader | [315 Posts](/search?do=process&provider=Member&searchuser=548123)

> [Quoting MavecoDoido](/thread/post/13431107#post13431107 "View Quoted Post")
> 
> Disliked
> 
> {quote} carddard, could you send the parameters you are using to get to the BT shown above? Anyone with good and consistent results? Tks
> 
> Ignored

I'm not using OP's standard settings. But the crux of the idea remains the same - Using a pre-determined range and stubbornly holding on till it's in profit. And implement a group trailing stop concept to capitalize on price movements in favourable directions. There are ways to cut down on the risk but at the end of the day a martingale is still a martingale. I wouldn't recommend using this on live because of the high level of risk involved. But for the sake of discussion, assuming that you have the risk appetite and sufficient capital to withstand the drawdowns, it can be a thrilling experience. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: 2a5c99221ea5b4178cf27b3a750980a5.png
Size: 154 KB](/attachment/image/3923533/thumbnail?d=1619414627)](/attachment/image/3923533?d=1619414627)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#463](/thread/post/14000538#post14000538 "Post Permalink")

  * May 15, 2022 1:26am  May 15, 2022 1:26am 

  * [ newbi3](newbi3)

  * | Joined Apr 2019  | Status: Trader | [95 Posts](/search?do=process&provider=Member&searchuser=792958)

> [Quoting radityo.ardi](/thread/post/12965981#post12965981 "View Quoted Post")
> 
> Disliked
> 
> OK, just to settle in on what's going on with Tunnel Martingale from the last update. For those who don't follow, let's get a refresher. Tunnel Martingale basically consist of 2 main things: Ceiling, Floor. Both are the price line which guards if the price goes towards past Ceiling, it will put pending order on the Floor 2 times lot size of the previous (Ceiling). If this pending order gets executed, it will then again add pending order on the Ceiling 2 times lot size if the Floor. Until then it breaks out, (in example 0.16 of the lot size), it...
> 
> Ignored

i have used this EA and i always had big Dd and stress,im at the moment in big DD because i used this EA,the distance was too small that many trades open of the big lots and it can blow the account,i tried to fix it by myself and im in stress now ,check my situation now 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: 2022-05-14_18h13_55.png
Size: 16 KB](/attachment/image/4204099/thumbnail?d=1652545579)](/attachment/image/4204099?d=1652545579)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#464](/thread/post/14000731#post14000731 "Post Permalink")

  * May 15, 2022 6:32pm  May 15, 2022 6:32pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1193932_106.gif) eyefeelsix](eyefeelsix)

  * Joined Aug 2021 | Status: ᶠᶸᶜᵏᵧₒᵤ! | [1,814 Posts](/search?do=process&provider=Member&searchuser=1193932)

> [Quoting newbi3](/thread/post/14000538#post14000538 "View Quoted Post")
> 
> Disliked
> 
> {quote} i have used this EA and i always had big Dd and stress,im at the moment in big DD because i used this EA,the distance was too small that many trades open of the big lots and it can blow the account,i tried to fix it by myself and im in stress now ,check my situation now {image}
> 
> Ignored

looks like you will be tossed around for the next few months, make a decision from now It's not too late to closed one of these.  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: NZDJPYDaily.png
Size: 18 KB](/attachment/image/4204258/thumbnail?d=1652607220)](/attachment/image/4204258?d=1652607220)   

![](https://resources.faireconomy.media/images/emojis/64/1f409.png?v=15.1) Consistency beats intensity in the long run ~

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#465](/thread/post/14000785#post14000785 "Post Permalink")

  * May 15, 2022 9:55pm  May 15, 2022 9:55pm 

  * [ newbi3](newbi3)

  * | Joined Apr 2019  | Status: Trader | [95 Posts](/search?do=process&provider=Member&searchuser=792958)

> [Quoting eyefeelsix](/thread/post/14000731#post14000731 "View Quoted Post")
> 
> Disliked
> 
> {quote} looks like you will be tossed around for the next few months, make a decision from now It's not too late to closed one of these. {image}
> 
> Ignored

its a very difficult decision,sell DD is 40 and buy DD is 80,if i close sell and it goes down,i will lose the account,so i think using ict MTf strategy,i scalp with high lots and keep closing losing trades with profitable trades and save the account,what do u think? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#466](/thread/post/14000845#post14000845 "Post Permalink")

  * May 15, 2022 11:52pm  May 15, 2022 11:52pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1193932_106.gif) eyefeelsix](eyefeelsix)

  * Joined Aug 2021 | Status: ᶠᶸᶜᵏᵧₒᵤ! | [1,814 Posts](/search?do=process&provider=Member&searchuser=1193932)

> [Quoting newbi3](/thread/post/14000785#post14000785 "View Quoted Post")
> 
> Disliked
> 
> {quote} its a very difficult decision,sell DD is 40 and buy DD is 80,if i close sell and it goes down,i will lose the account,so i think using ict MTf strategy,i scalp with high lots and keep closing losing trades with profitable trades and save the account,what do u think?
> 
> Ignored

In my humble opinion..  
if so, the first thing you do is closed all your short positions, and let your long position last until 78.00, currently the bullish movement is still valid until that level has not been reached,  
However.. if you want back to go short for hedging, the bearish order block zone the red rectangle that I marked is a nice place to entrypoint ( opportunity to take profits when sideway occurs _potential wide range from peak of wave3 to wave4_ ) Good luck to you. 

![](https://resources.faireconomy.media/images/emojis/64/1f409.png?v=15.1) Consistency beats intensity in the long run ~

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#467](/thread/post/14000939#post14000939 "Post Permalink")

  * May 16, 2022 5:15am  May 16, 2022 5:15am 

  * [ newbi3](newbi3)

  * | Joined Apr 2019  | Status: Trader | [95 Posts](/search?do=process&provider=Member&searchuser=792958)

> [Quoting eyefeelsix](/thread/post/14000845#post14000845 "View Quoted Post")
> 
> Disliked
> 
> {quote} In my humble opinion.. if so, the first thing you do is closed all your short positions, and let your long position last until 78.00, currently the bullish movement is still valid until that level has not been reached, However.. if you want back to go short for hedging, the bearish order block zone the red rectangle that I marked is a nice place to entrypoint ( opportunity to take profits when sideway occurs potential wide range from peak of wave3 to wave4 ) Good luck to you.
> 
> Ignored

Thanks a lot so so much insight,yes i was thinking of clsoing some shorts,may be half short i will close,im afraid if i close and market goes down. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#468](/thread/post/14003021#post14003021 "Post Permalink")

  * May 17, 2022 11:00pm  May 17, 2022 11:00pm 

  * [ AjayShaga.io](ajayshaga.io)

  * | Joined May 2022  | Status: Trader | [1 Post](/search?do=process&provider=Member&searchuser=1456095)

> [Quoting radityo.ardi](/thread/post/8039710#post8039710 "View Quoted Post")
> 
> Disliked
> 
> I've uploaded v1.03. A few changes: Start by Support and Resistance is supported now. But in the middle of testing (Support and Resistance is never reached since Friday and today). Close by Fixed Points is supported as well. Moved the file hosting to Dropbox. I hope y'all able to download.
> 
> Ignored

Can anyone tell me how to setup this start time and end time to make it run 24 hours? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#469](/thread/post/14003259#post14003259 "Post Permalink")

  * May 18, 2022 3:14am  May 18, 2022 3:14am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar740000_1.gif) FunkyKoval](funkykoval)

  * Joined Nov 2018 | Status: Trader | [264 Posts](/search?do=process&provider=Member&searchuser=740000)

<https://www.mql5.com/en/articles/8390>

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#470](/thread/post/14007773#post14007773 "Post Permalink")

  * May 22, 2022 9:30am  May 22, 2022 9:30am 

  * [ newbi3](newbi3)

  * | Joined Apr 2019  | Status: Trader | [95 Posts](/search?do=process&provider=Member&searchuser=792958)

> [Quoting newbi3](/thread/post/14000939#post14000939 "View Quoted Post")
> 
> Disliked
> 
> {quote} Thanks a lot so so much insight,yes i was thinking of clsoing some shorts,may be half short i will close,im afraid if i close and market goes down.
> 
> Ignored

Please give me more insight of how this pair will mve for the next week,thanks 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#471](/thread/post/14009967#post14009967 "Post Permalink")

  * May 24, 2022 6:37pm  May 24, 2022 6:37pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar588299_3.gif) RiskFighter](riskfighter)

  * Joined Jun 2017 | Status: Trader | [1,566 Posts](/search?do=process&provider=Member&searchuser=588299)

> [Quoting radityo.ardi](/thread/post/12976759#post12976759 "View Quoted Post")
> 
> Disliked
> 
> {quote} I do agree martingale has its risk. But isn't it the same concept with other trading systems as well? Just think of this, someone posted what claimed to be a winning strategy, then another too with another strategy, but all of these I found 1 thing in common. They have entry requirements. If not followed, then the strategy won't work. The funny part is that most of us ignore the fact that martingale does require entry requirements. Am I right? When I walk past MRT or public transport and sees the advertisement about investing in this, that,...
> 
> Ignored

You are so right. People think about Martingale systems, that they can just take a trade and then the system send some profit. I se it the other way round. Take only winning trades and use Martingale if the trade turns into a looser.  
  
If you do your very best to find the perfect setup for the trade, then Martingale don't even have to be executed. You get the profit without fighting for it and without including the Martingale risk of very high losses. So use your best entry tactic or entry robot to take the trades. Martingale will then only be effectuated at the times where your trade goes into a loss. 

Read post #1 !! Then read it again 10 more times before you ask.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#472](/thread/post/14020753#post14020753 "Post Permalink")

  * Jun 3, 2022 9:56pm  Jun 3, 2022 9:56pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar608462_3.gif) T4Trade](t4trade)

  * Joined Sep 2017 | Status: Trend Following,Price Action,Grid | [2,484 Posts](/search?do=process&provider=Member&searchuser=608462)

> [Quoting eyefeelsix](/thread/post/14000731#post14000731 "View Quoted Post")
> 
> Disliked
> 
> {quote} looks like you will be tossed around for the next few months, make a decision from now It's not too late to closed one of these. {image}
> 
> Ignored

newbi3 is my another account,please check the price is at 70% retracement on daily chart, should i close buy trades now? 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: 2022-06-03_14h54_03.png
Size: 9 KB](/attachment/image/4217199/thumbnail?d=1654260988)](/attachment/image/4217199?d=1654260988)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#473](/thread/post/14021037#post14021037 "Post Permalink")

  * Jun 4, 2022 1:06am  Jun 4, 2022 1:06am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1193932_106.gif) eyefeelsix](eyefeelsix)

  * Joined Aug 2021 | Status: ᶠᶸᶜᵏᵧₒᵤ! | [1,814 Posts](/search?do=process&provider=Member&searchuser=1193932)

> [Quoting T4Trade](/thread/post/14020753#post14020753 "View Quoted Post")
> 
> Disliked
> 
> {quote} newbi3 is my another account,please check the price is at 70% retracement on daily chart, should i close buy trades now? {image}
> 
> Ignored

You're actually too late.. but yes, to open your locked positions ![](https://resources.faireconomy.media/images/emojis/64/1f513.png?v=15.1) first closed all buy to escape from the accident before, don't do anything after that ( to keep your margin still alive )  
  
if the price is getting higher, add more short with the same volume as on your short bottom at the level 88.6% ( RN 86.25 to 87.00 ) and that is your last chance to go short, and if the price managed to go down you can exit all out together on the 61.8% zone ( RN 82.50 ) because the price need some pullback to continue the bull trend.  
  
However, if this scenarios fails to work, you should be prepared to blow ![](https://resources.faireconomy.media/images/emojis/64/1f92f.png?v=15.1) your account.. the price will continues higher to break-out the previous 3rd wave  
  
Good luck friend ![](https://resources.faireconomy.media/images/emojis/64/270c-fe0f.png?v=15.1)

![](https://resources.faireconomy.media/images/emojis/64/1f409.png?v=15.1) Consistency beats intensity in the long run ~

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#474](/thread/post/14204663#post14204663 "Post Permalink")

  * Nov 1, 2022 11:09pm  Nov 1, 2022 11:09pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting RiskFighter](/thread/post/14009967#post14009967 "View Quoted Post")
> 
> Disliked
> 
> {quote} You are so right. People think about Martingale systems, that they can just take a trade and then the system send some profit. I se it the other way round. Take only winning trades and use Martingale if the trade turns into a looser. If you do your very best to find the perfect setup for the trade, then Martingale don't even have to be executed. You get the profit without fighting for it and without including the Martingale risk of very high losses. So use your best entry tactic or entry robot to take the trades. Martingale will then only...
> 
> Ignored

I've been taking a hiatus from trading, meanwhile also reading up on some new stuff like trading with Machine Learning - ML. You know...as we are too lazy to learn, I'm learning ML so the machine can do trading for me by predicting what's the next move and what's the confidence percentage. After 1 year of learning here and there, there's nothing much also that is very much definite that ML could help us with trading.  
  
About the martingale itself, it's true and mathematically correct that the system is 100% profitable. But, we're limited with our own capital. Just like if we want to travel to the nearest solar system other than us, it's mathematically possible to build a spaceship that can move faster than the speed of light. But, we're limited with our own resources and technology.  
  

> [Quoting RiskFighter](/thread/post/14009967#post14009967 "View Quoted Post")
> 
> Disliked
> 
> {quote} Take only winning trades and use Martingale if the trade turns into a looser. If you do your very best to find the perfect setup for the trade, then Martingale don't even have to be executed.
> 
> Ignored

Martingale is good if you execute manually if you can find longer-term trends. Moreover, it's not for continuous execution but just 1 or 2 trades. My problem is that I don't have time to look at the chart all the time. Best if the EA can also do a trailing stop (meaning it uses the stop losses line once it turns into open profit trades. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#475](/thread/post/14204949#post14204949 "Post Permalink")

  * Nov 2, 2022 1:00am  Nov 2, 2022 1:00am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar377334_6.gif) radityo.ardi](radityo.ardi)

  * Joined Jul 2014 | Status: BAGONG!!! | [1,142 Posts](/search?do=process&provider=Member&searchuser=377334)

> [Quoting newbi3](/thread/post/14000538#post14000538 "View Quoted Post")
> 
> Disliked
> 
> {quote} i have used this EA and i always had big Dd and stress,im at the moment in big DD because i used this EA,the distance was too small that many trades open of the big lots and it can blow the account,i tried to fix it by myself and im in stress now ,check my situation now {image}
> 
> Ignored

Sorry, mate. I still have not worked on Martingale again for so long. Maybe never will... or there might be a chance if I have time and some promising ideas. But for now, that's the risk of martingale. 

If you ask me to code/fix your EA... it's probably not for free...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#476](/thread/post/14228473#post14228473 "Post Permalink")

  * Nov 19, 2022 9:05pm  Nov 19, 2022 9:05pm 

  * [ Jippykaze](jippykaze)

  * | Joined Aug 2021  | Status: Trader | [13 Posts](/search?do=process&provider=Member&searchuser=1212380)

> [Quoting RiskFighter](/thread/post/14009967#post14009967 "View Quoted Post")
> 
> Disliked
> 
> {quote} You are so right. People think about Martingale systems, that they can just take a trade and then the system send some profit. I se it the other way round. Take only winning trades and use Martingale if the trade turns into a looser. If you do your very best to find the perfect setup for the trade, then Martingale don't even have to be executed. You get the profit without fighting for it and without including the Martingale risk of very high losses. So use your best entry tactic or entry robot to take the trades. Martingale will then only...
> 
> Ignored

  
Yes i also use this method, but still dangerous so sometimes still need to manually hedge or cut loss 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#477](/thread/post/14838051#post14838051 "Post Permalink")

  * Last Post: Apr 20, 2024 7:52am  Apr 20, 2024 7:52am 

  * [ ikpp](ikpp)

  * | Joined May 2016  | Status: Trader | [1 Post](/search?do=process&provider=Member&searchuser=464715)

Mr Radityo, do you have this EA for the MT5 version? . I just want this ea to work on the "anytime" option. The other options do not need to be used. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Trapping System: Tunnel Martingale
  *   * [ **Reply to Thread** ](/thread/524198-trapping-system-tunnel-martingale/reply#reply)

[](https://www.forexfactory.com "Homepage")

  * [Forums](forums)
  * [Trades](trades)
  * [Calendar](calendar)
  * [News](news)
  * [Market](market)
  * [Brokers](brokers)

****

[](https://www.faireconomy.com/)
