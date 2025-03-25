

  * 

[Spud's MTF FIB Breakout System](/thread/30109-spuds-mtf-fib-breakout-system "Spud's MTF FIB Breakout System 
-------------------------------- 
Ever since I learned about Fibonacci numbers they have interested my pure...") 375 replies

[H1Scalper System (MTF D1,H1,M5)](/thread/166646-h1scalper-system-mtf-d1h1m5 "Here are the indicators for a manual system. 
  
Explanations, rules and trading ideas are coming... 
. 
\(2009.05.13\) 
Attached are the...") 725 replies

[MTF Trix system](/thread/183801-mtf-trix-system "Hello everybody, 
 
This thread is for developing and discussing a multi-timeframe trading system that is based on one indicator - Trix -...") 3,697 replies

[MTF Stochastics into MTF Stoch Histogram](/thread/359918-mtf-stochastics-into-mtf-stoch-histogram "Hi, 
 
I have been trading with the help of MTF Stochastics for a few weeks now with relatively good results but would appreciate if...") 8 replies

[MTF Vajioo Scalping System](/thread/195912-mtf-vajioo-scalping-system "RUBBISH") 15 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/1319487-squeeze-n-go-mtf-system/reply#reply)
  * Subscribe
  * [216](javascript:void\(0\);)

Attachments: Squeeze n Go | MTF System

Tags: Squeeze n Go | MTF System

#  [](/thread/1319487-squeeze-n-go-mtf-system)Squeeze n Go | MTF System 

  * 

  * [#1](/thread/1319487-squeeze-n-go-mtf-system "Post Permalink")

  * First Post: Edited Dec 27, 2024 12:10am  Dec 21, 2024 3:57am | Edited Dec 27, 2024 12:10am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

_*****Changing the logic of the system to align with RickM's methodology. The previous system was based off an experienced coder form TradingView, however I find more merit in RickM's approach.*****_  
  
  
**This strategy focuses on trading the TTM Squeeze Pro indicator in combination with EMA trend ribbons to filter out fakeouts and align with the trend. It's designed for H1 or M5 timeframes while keeping the daily chart in mind for confirmation.**  
  
**Setup Requirements:**  
**EMA Trend Ribbon**  
EMA 21 (White) – The key trend indicator.  
EMA 34 (Yellow)  
EMA 55 (Orange)  
EMA 89 (Red)  
  
**The ribbon identifies trend direction:**  
Bullish trend: EMAs stacked upward (21 > 34 > 55 > 89).  
Bearish trend: EMAs stacked downward (21 < 34 < 55 < 89).  
  
**TTM Squeeze Pro (on TradingView)**  
Focus on the transition from red dots (Bollinger Bands inside Keltner Channels) to black dots.  
Look for momentum alignment with the squeeze breakout.  
  
**Entry & Exit Rules**  
**Entry:**  
Trade breakouts from red to black dots if the momentum histogram aligns with the trend.  
Only take trades in the direction of the EMA 21 and the ribbon.  
  
**Exit** :  
Close the trade when the momentum histogram shifts from red to yellow and begins reversing.  
  
**Multi-Timeframe Confirmation**  
Always confirm the trend on higher timeframes (Daily or Weekly).  
  
Check for squeeze setups across 15M, 30M, and higher timeframes for confluence.  
  
__**FOR REFERENCE FROM TTM SQUEEZE PRO INDICATOR - Beardy_Fred**__  
_> __John Carter creating the TTM Squeeze and TTM Squeeze Pro_  
_- > Lazybear's original interpretation of the TTM Squeeze: Squeeze Momentum Indicator_  
_- > Makit0's evolution of Lazybear's script to factor in the TTM Squeeze Pro upgrades - Squeeze PRO Arrows_  
  
_For those unfamiliar with the TTM Squeeze, it is simply a visual way of seeing how Bollinger Bands (standard deviations from a simple moving average ) relate to Keltner Channels (average true range bands) compared with the momentum of the price action. The concept is that as Bollinger Bands compress within Keltner Channels, price volatility decreases, giving way for a potential explosive price movement up or down._  
  
_Differences between the original TTM Squeeze and TTM Squeeze Pro:_  
_- > Both use a 2 standard deviation Bollinger Band ;_  
_- > The original squeeze only used a 1.5 ATR Keltner Channel; and_  
_- > The pro version uses 1.0, 1.5 and 2.0 ATR Keltner Channels ._  
_The pro version therefore helps differentiate between levels of squeeze (compression) as the Bollinger Bands moves through the Keltner Channels i.e. the greater the compression, the more potential for explosive moves - less compression means more squeezing._  
  
_The Histogram shows price momentum whereas the colored dots (along the zeroline) show where the Bollinger Bands are in relation to the Keltner Channels:_  
_- > Cyan Bars = positive, increasing momentum;_  
_- > Blue Bars = positive, decreasing momentum (indication of a reversal in price direction);_  
_- > Red Bars = negative, increasing momentum;_  
_- > Yellow Bars = negative, decreasing momentum (indication of a reversal in price direction);_  
_- > Orange Dots = High Compression / large squeeze (One or both of the Bollinger Bands is inside the 1st (1.0 ATR) Keltner Channel);_  
_- > Red Dots = Medium Squeeze (One or both of the Bollinger Bands is inside the 2nd (1.5 ATR) Keltner Channel);_  
_- > Black Dots = Low compression / wide squeeze (One or both of the Bollinger Bands is inside the 3rd (2.0 ATR) Keltner Channels );_  
_- > Green Dots = No Squeeze / Squeeze Fired (One or both of the Bollinger Bands is outside of the 3rd (2.0 ATR) Keltner Channel)._  
  
_Ideal Scenario:_  
_As the ticker enters the squeeze, black dots would warn of the beginning of a low compression squeeze. As the Bollinger bands continue to constrict within the Keltner Channels , red dots would highlight a medium compression. As the price action and momentum continues to compress an orange dot shows warning of high compression. As price action leaves the squeeze, the coloring would reverse e.g. orange to red to black to green. Any compression squeeze is considered fired at the first green dot that appears._  
  
_Note: This is an ideal progression of the different types of squeezes, however any type of squeeze (and color sequence) may appear at anytime, therefore the focus is primarily on the green dots after any type of compression._  
  
_Entry and Exit Guide:_  
_- > John Carter recommends entering a position after at least 5 black dots or wait for 1st green dot ; and_  
_- > Exit on second blue or yellow bar or, alternatively, remain in the position after confirming a continuing trend through a separate indicator._

  * [#2](/thread/post/15096786#post15096786 "Post Permalink")

  * Edited 4:54am  Dec 21, 2024 4:42am | Edited 4:54am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar272159_71.gif) driven18](driven18)

  * Joined Jul 2012 | Status: Trader | [1,385 Posts](/search?do=process&provider=Member&searchuser=272159)

> [Quoting MachineLearn](/thread/post/15096767#post15096767 "View Quoted Post")
> 
> Disliked
> 
> {image}
> 
> Ignored

Hey relentless Machine...System enthusiast? I like that and can relate to it ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
  
Can you post few charts, perhaps on the lower time frame(5M or 10M or 15M), have to be conscious of MM and SLs and point out where exactly you would of entered? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#3](/thread/post/15096807#post15096807 "Post Permalink")

  * Dec 21, 2024 5:20am  Dec 21, 2024 5:20am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

> [Quoting driven18](/thread/post/15096786#post15096786 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hey relentless Machine...System enthusiast? I like that and can relate to it ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) Can you post few charts, perhaps on the lower time frame(5M or 10M or 15M), have to be conscious of MM and SLs and point out where exactly you would of entered?
> 
> Ignored

Hello my friend   
  
Ofc, once I'm home I'll upload some more detailed charts. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#4](/thread/post/15096838#post15096838 "Post Permalink")

  * Dec 21, 2024 6:35am  Dec 21, 2024 6:35am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar272159_71.gif) driven18](driven18)

  * Joined Jul 2012 | Status: Trader | [1,385 Posts](/search?do=process&provider=Member&searchuser=272159)

> [Quoting MachineLearn](/thread/post/15096833#post15096833 "View Quoted Post")
> 
> Disliked
> 
> M1 Gold setup just finished. Stop was placed at the current outter BB with a 1:1 TP. {image}
> 
> Ignored

Very nice, simplicity is the key! I suggest Trailing Stop, every time PA gets to the top/bottom of BB. It will prevent from quick PA action hitting full Stop Loss. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 247 KB](/attachment/image/4865860/thumbnail?d=1734730526)](/attachment/image/4865860?d=1734730526)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#5](/thread/post/15096851#post15096851 "Post Permalink")

  * Dec 21, 2024 6:41am  Dec 21, 2024 6:41am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

> [Quoting driven18](/thread/post/15096838#post15096838 "View Quoted Post")
> 
> Disliked
> 
> {quote} Very nice, simplicity is the key! I suggest Trailing Stop, every time PA gets to the top/bottom of BB. It will prevent from quick PA action hitting full Stop Loss. {image}
> 
> Ignored

Lovely idea.  
  
Also I had Heikin Candles in those examples but setups were taking with normal candles. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#6](/thread/post/15096859#post15096859 "Post Permalink")

  * Dec 21, 2024 6:57am  Dec 21, 2024 6:57am 

  * [ Merka](merka)

  * Joined Jan 2016 | Status: Trader | [1,944 Posts](/search?do=process&provider=Member&searchuser=440568)

My KC (Blue) it's almost always inside the BB (black)  
Is that right? 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 63 KB](/attachment/image/4865874/thumbnail?d=1734731671)](/attachment/image/4865874?d=1734731671)   
[![Click to Enlarge

Name: screenshot.png
Size: 5 KB](/attachment/image/4865875/thumbnail?d=1734731731)](/attachment/image/4865875?d=1734731731)   
[![Click to Enlarge

Name: screenshot.png
Size: 6 KB](/attachment/image/4865876/thumbnail?d=1734731761)](/attachment/image/4865876?d=1734731761)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#7](/thread/post/15096862#post15096862 "Post Permalink")

  * Dec 21, 2024 7:01am  Dec 21, 2024 7:01am 

  * [ Merka](merka)

  * Joined Jan 2016 | Status: Trader | [1,944 Posts](/search?do=process&provider=Member&searchuser=440568)

> [Quoting MachineLearn](/thread/post/15096851#post15096851 "View Quoted Post")
> 
> Disliked
> 
> {quote} Lovely idea. Also I had Heikin Candles in those examples but setups were taking with normal candles.
> 
> Ignored

Are you waiting for Keltner Channel to move inside the Bollinger Bands or viceversa? 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#8](/thread/post/15096905#post15096905 "Post Permalink")

  * Dec 21, 2024 7:49am  Dec 21, 2024 7:49am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

> [Quoting Merka](/thread/post/15096862#post15096862 "View Quoted Post")
> 
> Disliked
> 
> {quote} Are you waiting for Keltner Channel to move inside the Bollinger Bands or viceversa?
> 
> Ignored

Sorry mixed it up ![](https://resources.faireconomy.media/images/emojis/64/1f605.png?v=15.1) . Never manually charted squeezes, always used indicator.  
  
Wait for BB to enter the KC  
  
Once SQUEEZE is located, wait for ST signal and validate with momentum 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#9](/thread/post/15096938#post15096938 "Post Permalink")

  * Dec 21, 2024 9:34am  Dec 21, 2024 9:34am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1967050_1.gif) Ju4ara](ju4ara)

  * | Joined Oct 2024  | Status: Trader | [105 Posts](/search?do=process&provider=Member&searchuser=1967050)

Looks promising, gonna give it a try 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#10](/thread/post/15096949#post15096949 "Post Permalink")

  * Dec 21, 2024 10:40am  Dec 21, 2024 10:40am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

> [Quoting Ju4ara](/thread/post/15096938#post15096938 "View Quoted Post")
> 
> Disliked
> 
> Looks promising, gonna give it a try
> 
> Ignored

Works quite well, but with every system you need to use common sense and some discretion. Don't take every setup. I've found more success when analyzing the current squeeze. If the indicators signal a squeeze remember it's based off the last 20 or so candles, so really try to understand and contextualize the squeeze before entering. Even blind I like my odds though 

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#11](/thread/post/15096959#post15096959 "Post Permalink")

  * Dec 21, 2024 11:30am  Dec 21, 2024 11:30am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar601035_2.gif) axecap](axecap)

  * Joined Aug 2017 | Status: Trader | [2,336 Posts](/search?do=process&provider=Member&searchuser=601035)

Hi Machine....I too have been using various squeeze breakout methods....mainly in lower time frames.  
What TF's have you been using this for?  
Thanks 

its all just one persons opinion....

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#12](/thread/post/15096963#post15096963 "Post Permalink")

  * Dec 21, 2024 11:48am  Dec 21, 2024 11:48am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

> [Quoting axecap](/thread/post/15096959#post15096959 "View Quoted Post")
> 
> Disliked
> 
> Hi Machine....I too have been using various squeeze breakout methods....mainly in lower time frames. What TF's have you been using this for? Thanks
> 
> Ignored

Any time frame 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#13](/thread/post/15096985#post15096985 "Post Permalink")

  * Dec 21, 2024 1:42pm  Dec 21, 2024 1:42pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1967050_1.gif) Ju4ara](ju4ara)

  * | Joined Oct 2024  | Status: Trader | [105 Posts](/search?do=process&provider=Member&searchuser=1967050)

> [Quoting MachineLearn](/thread/post/15096949#post15096949 "View Quoted Post")
> 
> Disliked
> 
> {quote} Works quite well, but with every system you need to use common sense and some discretion. Don't take every setup. I've found more success when analyzing the current squeeze. If the indicators signal a squeeze remember it's based off the last 20 or so candles, so really try to understand and contextualize the squeeze before entering. Even blind I like my odds though
> 
> Ignored

I see, there is no system which you can use blindly(if there is, you can build EA). What is traded the best with this system? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#14](/thread/post/15096988#post15096988 "Post Permalink")

  * Dec 21, 2024 2:14pm  Dec 21, 2024 2:14pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar2012074_12.gif) Th3W1z4rd](th3w1z4rd)

  * Joined Dec 2024 | Status: Trader | [121 Posts](/search?do=process&provider=Member&searchuser=2012074)

> [Quoting Ju4ara](/thread/post/15096985#post15096985 "View Quoted Post")
> 
> Disliked
> 
> {quote} I see, there is no system which you can use blindly(if there is, you can build EA). What is traded the best with this system?
> 
> Ignored

EAs on the platforms retail traders have access to, just can’t stay profitable long term if they’re 100% fully automated. I’ve tried this to the nth degree. They'll work for a few months, but they will eventually fail.  
  
Manual trading or semi-manual are the way to go. In other words, the trader needs to be involved and make some decisions because EAs can’t handle 100% of everything on their own, over the long run.  
  
That’s just my experience and opinion. Maybe someone out there has figured it out with MQL4 or MQL5, but I haven’t. 

Just my thoughts, not financial advice.

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#15](/thread/post/15096991#post15096991 "Post Permalink")

  * Dec 21, 2024 2:18pm  Dec 21, 2024 2:18pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

> [Quoting Ju4ara](/thread/post/15096985#post15096985 "View Quoted Post")
> 
> Disliked
> 
> {quote} I see, there is no system which you can use blindly(if there is, you can build EA). What is traded the best with this system?
> 
> Ignored

Any market can create a squeeze, it's just about finding and contextualizing them enough to feel confident in your trade. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#16](/thread/post/15096996#post15096996 "Post Permalink")

  * Dec 21, 2024 2:29pm  Dec 21, 2024 2:29pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

Some trades consider squeeze a to be valid if only one BB band enters inside the KC bands.  
  
I personally like to really see the bands contract nicely and tightly inside the KC 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#17](/thread/post/15096997#post15096997 "Post Permalink")

  * Dec 21, 2024 2:37pm  Dec 21, 2024 2:37pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

> [Quoting MachineLearn](/thread/post/15096996#post15096996 "View Quoted Post")
> 
> Disliked
> 
> Some trades consider squeeze a to be valid if only one BB band enters inside the KC bands. I personally like to really see the bands contract nicely and tightly inside the KC
> 
> Ignored

I like to see a pinch.  
  
Same setup just with ST Oscillator 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: Screenshot_20241221_003652_Photos.jpg
Size: 457 KB](/attachment/image/4865950/thumbnail?d=1734759441)](/attachment/image/4865950?d=1734759441)   
[![Click to Enlarge

Name: Screenshot_20241221_004223_Photos.jpg
Size: 413 KB](/attachment/image/4865952/thumbnail?d=1734759778)](/attachment/image/4865952?d=1734759778)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#18](/thread/post/15097014#post15097014 "Post Permalink")

  * Dec 21, 2024 3:26pm  Dec 21, 2024 3:26pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar601035_2.gif) axecap](axecap)

  * Joined Aug 2017 | Status: Trader | [2,336 Posts](/search?do=process&provider=Member&searchuser=601035)

BTCUSD M5 certainly showed the breakout.  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: cT_cs_8028942_BTCUSD_2024-12-21_19-20-59.jpg
Size: 447 KB](/attachment/image/4865959/thumbnail?d=1734762316)](/attachment/image/4865959?d=1734762316)   

its all just one persons opinion....

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#19](/thread/post/15097032#post15097032 "Post Permalink")

  * Dec 21, 2024 4:41pm  Dec 21, 2024 4:41pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1967050_1.gif) Ju4ara](ju4ara)

  * | Joined Oct 2024  | Status: Trader | [105 Posts](/search?do=process&provider=Member&searchuser=1967050)

> [Quoting MachineLearn](/thread/post/15096991#post15096991 "View Quoted Post")
> 
> Disliked
> 
> {quote} Any market can create a squeeze, it's just about finding and contextualizing them enough to feel confident in your trade.
> 
> Ignored

and what exactly is preferred to use to contextualise bb squeeze? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#20](/thread/post/15097113#post15097113 "Post Permalink")

  * Dec 22, 2024 12:02am  Dec 22, 2024 12:02am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

A nice scalping setup from yesterday afternoon 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot_20241221_094227_Photos.jpg
Size: 478 KB](/attachment/image/4866001/thumbnail?d=1734792176)](/attachment/image/4866001?d=1734792176)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Squeeze n Go | MTF System
  *   * [ **Reply to Thread** ](/thread/1319487-squeeze-n-go-mtf-system/reply#reply)

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

[Spud's MTF FIB Breakout System](/thread/30109-spuds-mtf-fib-breakout-system "Spud's MTF FIB Breakout System 
-------------------------------- 
Ever since I learned about Fibonacci numbers they have interested my pure...") 375 replies

[H1Scalper System (MTF D1,H1,M5)](/thread/166646-h1scalper-system-mtf-d1h1m5 "Here are the indicators for a manual system. 
  
Explanations, rules and trading ideas are coming... 
. 
\(2009.05.13\) 
Attached are the...") 725 replies

[MTF Trix system](/thread/183801-mtf-trix-system "Hello everybody, 
 
This thread is for developing and discussing a multi-timeframe trading system that is based on one indicator - Trix -...") 3,697 replies

[MTF Stochastics into MTF Stoch Histogram](/thread/359918-mtf-stochastics-into-mtf-stoch-histogram "Hi, 
 
I have been trading with the help of MTF Stochastics for a few weeks now with relatively good results but would appreciate if...") 8 replies

[MTF Vajioo Scalping System](/thread/195912-mtf-vajioo-scalping-system "RUBBISH") 15 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/1319487-squeeze-n-go-mtf-system/reply#reply)
  * Subscribe
  * [216](javascript:void\(0\);)

Attachments: Squeeze n Go | MTF System

Tags: Squeeze n Go | MTF System

#  [](/thread/1319487-squeeze-n-go-mtf-system)Squeeze n Go | MTF System 

  * 

  * [#21](/thread/post/15097119#post15097119 "Post Permalink")

  * Dec 22, 2024 12:21am  Dec 22, 2024 12:21am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

H1 AUDCAD currently in a setup. ST cross while in a squeeze, with momentum turning up.   
  
As well as a strong support area broken enticing short orders only for price to return higher shortly after. Could be a considerable amount of trapped traders. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot_20241221_101846_Photos.jpg
Size: 469 KB](/attachment/image/4866012/thumbnail?d=1734794513)](/attachment/image/4866012?d=1734794513)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#22](/thread/post/15097163#post15097163 "Post Permalink")

  * Dec 22, 2024 3:14am  Dec 22, 2024 3:14am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

BTC on M1, you can see we have a situation here where the bottom BB has contracted into the KC but not the upper band. Technically it's a squeeze, but does it imply any directional bias if only one band is in? Every other rule is valid, ST crossed down and momentum turned down. I'm observing and open to ideas. Maybe both BB bands do not need to pinched within, food for thought 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot_20241221_131240_Photos.jpg
Size: 479 KB](/attachment/image/4866044/thumbnail?d=1734804767)](/attachment/image/4866044?d=1734804767)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#23](/thread/post/15097168#post15097168 "Post Permalink")

  * Dec 22, 2024 3:43am  Dec 22, 2024 3:43am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar379731_1.gif) rockypoint](rockypoint)

  * Joined Aug 2014 | Status: Trader | [4,260 Posts](/search?do=process&provider=Member&searchuser=379731)

When I was trading this method years ago I only took trades where BB's on both sides where within the keltner channel. It's a good system if you are a patient trader. I consistently made money trading it. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#24](/thread/post/15097169#post15097169 "Post Permalink")

  * Dec 22, 2024 3:43am  Dec 22, 2024 3:43am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar379731_1.gif) rockypoint](rockypoint)

  * Joined Aug 2014 | Status: Trader | [4,260 Posts](/search?do=process&provider=Member&searchuser=379731)

Good luck with the thread![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f60e.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#25](/thread/post/15097173#post15097173 "Post Permalink")

  * Dec 22, 2024 3:57am  Dec 22, 2024 3:57am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

> [Quoting rockypoint](/thread/post/15097168#post15097168 "View Quoted Post")
> 
> Disliked
> 
> When I was trading this method years ago I only took trades where BB's on both sides where within the keltner channel. It's a good system if you are a patient trader. I consistently made money trading it.
> 
> Ignored

Thanks for the words on encouragement Rocky. I've experienced pretty nice results as well when waiting for both sides. Might not even be worth looking into a one side squeeze,but we shall see! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#26](/thread/post/15097175#post15097175 "Post Permalink")

  * Dec 22, 2024 4:01am  Dec 22, 2024 4:01am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

> [Quoting MachineLearn](/thread/post/15097163#post15097163 "View Quoted Post")
> 
> Disliked
> 
> BTC on M1, you can see we have a situation here where the bottom BB has contracted into the KC but not the upper band. Technically it's a squeeze, but does it imply any directional bias if only one band is in? Every other rule is valid, ST crossed down and momentum turned down. I'm observing and open to ideas. Maybe both BB bands do not need to pinched within, food for thought {image}
> 
> Ignored

The one side squeeze worked today, but maybe not tomorrow.. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot_20241221_140042_Photos.jpg
Size: 585 KB](/attachment/image/4866056/thumbnail?d=1734807668)](/attachment/image/4866056?d=1734807668)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#27](/thread/post/15097176#post15097176 "Post Permalink")

  * Dec 22, 2024 4:05am  Dec 22, 2024 4:05am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

Look at this setup on GBPNZD on the Daily.  
  
Beautiful setup however the bottom BB expanded outside of the KC right before our signal. Rules are important, but so is context. Would we avoid this trade because of one bar? Discretion is an important part of trading and I believe context should be added to any trade you make. However, over fitting a system and making exceptions to compensate for every market conditions is terrible. Still testing the limits of what the squeeze and types of squeezes can offer for opportunities 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot_20241221_140320_Photos.jpg
Size: 453 KB](/attachment/image/4866057/thumbnail?d=1734807922)](/attachment/image/4866057?d=1734807922)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#28](/thread/post/15097180#post15097180 "Post Permalink")

  * Edited 4:46am  Dec 22, 2024 4:35am | Edited 4:46am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

Do you deploy a concept that measures the intensity of the pinch? Not all squeezes are equal right?... Is a squeeze on a pair trending up with the BBs barely weaving in and out of the KC bands equal to a squeeze that's moving completely sideways and the BB has a nice pinch from both sides deep within the KC?  
  
There's a few things to keep in mind here as I forward test. What is price doing during the squeeze? What is the shape of the squeeze, or my personal favorite...where are the trapped traders and so forth.  
  
One thing I know for certain is price does react to the squeeze concept quite nicely. However picking the direction is God's work. Any slight advantage we can give ourselves is all we need to carve out an edge. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#29](/thread/post/15097221#post15097221 "Post Permalink")

  * Dec 22, 2024 8:34am  Dec 22, 2024 8:34am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar272159_71.gif) driven18](driven18)

  * Joined Jul 2012 | Status: Trader | [1,385 Posts](/search?do=process&provider=Member&searchuser=272159)

> [Quoting MachineLearn](/thread/post/15097176#post15097176 "View Quoted Post")
> 
> Disliked
> 
> Look at this setup on GBPNZD on the Daily. Beautiful setup however the bottom BB expanded outside of the KC right before our signal. Rules are important, but so is context. Would we avoid this trade because of one bar? Discretion is an important part of trading and I believe context should be added to any trade you make. However, over fitting a system and making exceptions to compensate for every market conditions is terrible. Still testing the limits of what the squeeze and types of squeezes can offer for opportunities {image}
> 
> Ignored

BB expanded outside on the Sell side but we are Buying..I would say that as long as Buy BB inside the KC when there is a Buy trade - it is counts as legit squeeze. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 120 KB](/attachment/image/4866076/thumbnail?d=1734824143)](/attachment/image/4866076?d=1734824143)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#30](/thread/post/15097225#post15097225 "Post Permalink")

  * Dec 22, 2024 8:57am  Dec 22, 2024 8:57am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

> [Quoting driven18](/thread/post/15097221#post15097221 "View Quoted Post")
> 
> Disliked
> 
> {quote} BB expanded outside on the Sell side but we are Buying..I would say that as long as Buy BB inside the KC when there is a Buy trade - it is counts as legit squeeze. {image}
> 
> Ignored

Interesting... as long as the band thats in the direction of the trade is in a squeeze, the trade stays validated. Will apply to future set ups and see how it pans out. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#31](/thread/post/15097242#post15097242 "Post Permalink")

  * Dec 22, 2024 9:58am  Dec 22, 2024 9:58am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar2012074_12.gif) Th3W1z4rd](th3w1z4rd)

  * Joined Dec 2024 | Status: Trader | [121 Posts](/search?do=process&provider=Member&searchuser=2012074)

I haven’t set up this template to check myself, but which pair has a trade for Monday using this system?  
  
That seems like a good way to figure out which signals or shapes of BB KC, are the most reliable by seeing if they match up with other systems. The most reliable signal is likely the one that comes from independent systems agreeing with each other. I think that's one of the ideas behind the prop firms. The companies buying the signals from the prop firms probably look for agreement across different systems.  
  
So, what is the next trade for Monday? That way, others can check their systems to see if they match this one. 

Just my thoughts, not financial advice.

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#32](/thread/post/15097248#post15097248 "Post Permalink")

  * Dec 22, 2024 10:24am  Dec 22, 2024 10:24am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

> [Quoting Th3W1z4rd](/thread/post/15097242#post15097242 "View Quoted Post")
> 
> Disliked
> 
> I haven’t set up this template to check myself, but which pair has a trade for Monday using this system? That seems like a good way to figure out which signals or shapes of BB KC, are the most reliable by seeing if they match up with other systems. The most reliable signal is likely the one that comes from independent systems agreeing with each other. I think that's one of the ideas behind the prop firms. The companies buying the signals from the prop firms probably look for agreement across different systems. So, what is the next trade for Monday?...
> 
> Ignored

I'll check now, but you should easily be able to recreate the Super Trend and Squeeze on your platform. The momentum indicator is only on TradingView however. Shouldn't be too hard to follow along. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#33](/thread/post/15097249#post15097249 "Post Permalink")

  * Dec 22, 2024 10:27am  Dec 22, 2024 10:27am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar2012074_12.gif) Th3W1z4rd](th3w1z4rd)

  * Joined Dec 2024 | Status: Trader | [121 Posts](/search?do=process&provider=Member&searchuser=2012074)

> [Quoting MachineLearn](/thread/post/15097248#post15097248 "View Quoted Post")
> 
> Disliked
> 
> {quote} I'll check now, but you should easily be able to recreate the Super Trend and Squeeze on your platform. The momentum indicator is only on TradingView however. Shouldn't be too hard to follow along.
> 
> Ignored

I tried to create a TradingView account to check out this system, but it looks like they ask for a subscription right after signing up. 

Just my thoughts, not financial advice.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#34](/thread/post/15097250#post15097250 "Post Permalink")

  * Dec 22, 2024 10:36am  Dec 22, 2024 10:36am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

> [Quoting Th3W1z4rd](/thread/post/15097249#post15097249 "View Quoted Post")
> 
> Disliked
> 
> {quote} I tried to create a TradingView account to check out this system, but it looks like they ask for a subscription right after signing up.
> 
> Ignored

It's free but you can only use two indicators. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#35](/thread/post/15097252#post15097252 "Post Permalink")

  * Dec 22, 2024 10:50am  Dec 22, 2024 10:50am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar2012074_12.gif) Th3W1z4rd](th3w1z4rd)

  * Joined Dec 2024 | Status: Trader | [121 Posts](/search?do=process&provider=Member&searchuser=2012074)

For example, candle patterns across different timeframes basically show weakness in JPY, so basically buying JPY pairs. Does this template show any buy signals for JPY pairs? 

Just my thoughts, not financial advice.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#36](/thread/post/15097257#post15097257 "Post Permalink")

  * Dec 22, 2024 11:48am  Dec 22, 2024 11:48am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

> [Quoting Th3W1z4rd](/thread/post/15097242#post15097242 "View Quoted Post")
> 
> Disliked
> 
> I haven’t set up this template to check myself, but which pair has a trade for Monday using this system? That seems like a good way to figure out which signals or shapes of BB KC, are the most reliable by seeing if they match up with other systems. The most reliable signal is likely the one that comes from independent systems agreeing with each other. I think that's one of the ideas behind the prop firms. The companies buying the signals from the prop firms probably look for agreement across different systems. So, what is the next trade for Monday?...
> 
> Ignored

AUDCAD on H1 is currently in a setup for long 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#37](/thread/post/15097263#post15097263 "Post Permalink")

  * Dec 22, 2024 12:04pm  Dec 22, 2024 12:04pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar2012074_12.gif) Th3W1z4rd](th3w1z4rd)

  * Joined Dec 2024 | Status: Trader | [121 Posts](/search?do=process&provider=Member&searchuser=2012074)

> [Quoting MachineLearn](/thread/post/15097257#post15097257 "View Quoted Post")
> 
> Disliked
> 
> {quote} AUDCAD on H1 is currently in a setup for long
> 
> Ignored

It’s not matching on my end. I don’t have a strong signal for AUDCAD, but if I had to make a call, I’d say sell based on the H3 candle pattern. This would likely only hold for the first three hours on Monday. There’s also a chance Monday could open with a gap down that will just offset or eat up that potential three hour move. 

Just my thoughts, not financial advice.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#38](/thread/post/15097268#post15097268 "Post Permalink")

  * Dec 22, 2024 12:41pm  Dec 22, 2024 12:41pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar2012074_12.gif) Th3W1z4rd](th3w1z4rd)

  * Joined Dec 2024 | Status: Trader | [121 Posts](/search?do=process&provider=Member&searchuser=2012074)

Speaking of TradingView and the alignment of signals, here are the Ideas pages for some forex brokers, listed alphabetically:  
  
Eightcap: <https://www.tradingview.com/broker/Eightcap/ideas/>  
[FOREX.com](/brokers/forexcom "View FOREX.com Broker Profile"): <https://www.tradingview.com/broker/FOREXcom/ideas/>  
Fusion Markets: <https://www.tradingview.com/broker/FusionMarkets/ideas/>  
[FXCM](/brokers/fxcm "View FXCM Broker Profile"): <https://www.tradingview.com/broker/FXCM/ideas/>  
[IC Markets](/brokers/ic-markets "View IC Markets Broker Profile"): <https://www.tradingview.com/broker/ICMarkets/ideas/>  
[OANDA](/brokers/oanda "View OANDA Broker Profile"): <https://www.tradingview.com/broker/OANDA/ideas/>  
[Pepperstone](/brokers/pepperstone "View Pepperstone Broker Profile"): <https://www.tradingview.com/broker/Pepperstone/ideas/>  
[Tickmill](/brokers/tickmill "View Tickmill Broker Profile"): <https://www.tradingview.com/broker/Tickmill/ideas/>

Just my thoughts, not financial advice.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#39](/thread/post/15097273#post15097273 "Post Permalink")

  * Dec 22, 2024 1:01pm  Dec 22, 2024 1:01pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

> [Quoting Th3W1z4rd](/thread/post/15097263#post15097263 "View Quoted Post")
> 
> Disliked
> 
> {quote} It’s not matching on my end. I don’t have a strong signal for AUDCAD, but if I had to make a call, I’d say sell based on the H3 candle pattern. This would likely only hold for the first three hours on Monday. There’s also a chance Monday could open with a gap down that will just offset or eat up that potential three hour move.
> 
> Ignored

Sounds like a different system, and I wouldn't say this current squeeze n go setup is strong, it's just a setup for reference.   
  
Could go either way for sure though, we are all just speculating ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#40](/thread/post/15097426#post15097426 "Post Permalink")

  * Dec 23, 2024 2:02am  Dec 23, 2024 2:02am 

  * [ arya.aryaee](arya.aryaee)

  * | Joined Oct 2012  | Status: Trader | [329 Posts](/search?do=process&provider=Member&searchuser=303027)

> [Quoting rockypoint](/thread/post/15097168#post15097168 "View Quoted Post")
> 
> Disliked
> 
> When I was trading this method years ago I only took trades where BB's on both sides where within the keltner channel. It's a good system if you are a patient trader. I consistently made money trading it.
> 
> Ignored

hello rockypoint! would you mind share your method and indicators if it was based on MT4 platform?  
Thanks 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Squeeze n Go | MTF System
  *   * [ **Reply to Thread** ](/thread/1319487-squeeze-n-go-mtf-system/reply#reply)

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

[Spud's MTF FIB Breakout System](/thread/30109-spuds-mtf-fib-breakout-system "Spud's MTF FIB Breakout System 
-------------------------------- 
Ever since I learned about Fibonacci numbers they have interested my pure...") 375 replies

[H1Scalper System (MTF D1,H1,M5)](/thread/166646-h1scalper-system-mtf-d1h1m5 "Here are the indicators for a manual system. 
  
Explanations, rules and trading ideas are coming... 
. 
\(2009.05.13\) 
Attached are the...") 725 replies

[MTF Trix system](/thread/183801-mtf-trix-system "Hello everybody, 
 
This thread is for developing and discussing a multi-timeframe trading system that is based on one indicator - Trix -...") 3,697 replies

[MTF Stochastics into MTF Stoch Histogram](/thread/359918-mtf-stochastics-into-mtf-stoch-histogram "Hi, 
 
I have been trading with the help of MTF Stochastics for a few weeks now with relatively good results but would appreciate if...") 8 replies

[MTF Vajioo Scalping System](/thread/195912-mtf-vajioo-scalping-system "RUBBISH") 15 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/1319487-squeeze-n-go-mtf-system/reply#reply)
  * Subscribe
  * [216](javascript:void\(0\);)

Attachments: Squeeze n Go | MTF System

Tags: Squeeze n Go | MTF System

#  [](/thread/1319487-squeeze-n-go-mtf-system)Squeeze n Go | MTF System 

  * 

  * [#41](/thread/post/15097494#post15097494 "Post Permalink")

  * Dec 23, 2024 6:03am  Dec 23, 2024 6:03am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

BTC M1  
Nice one band setup that went exactly as the system calculates. Price exploded out of the squeeze. 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: Screenshot_20241222_155436_Photos.jpg
Size: 529 KB](/attachment/image/4866311/thumbnail?d=1734901352)](/attachment/image/4866311?d=1734901352)   
[![Click to Enlarge

Name: Screenshot_20241222_155541_Photos.jpg
Size: 510 KB](/attachment/image/4866312/thumbnail?d=1734901378)](/attachment/image/4866312?d=1734901378)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#42](/thread/post/15097527#post15097527 "Post Permalink")

  * Dec 23, 2024 8:03am  Dec 23, 2024 8:03am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar272159_71.gif) driven18](driven18)

  * Joined Jul 2012 | Status: Trader | [1,385 Posts](/search?do=process&provider=Member&searchuser=272159)

> [Quoting MachineLearn](/thread/post/15097494#post15097494 "View Quoted Post")
> 
> Disliked
> 
> BTC M1 Nice one band setup that went exactly as the system calculates. Price exploded out of the squeeze. {image} {image}
> 
> Ignored

There you go, no reason to respect Sell side no squeeze. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#43](/thread/post/15097561#post15097561 "Post Permalink")

  * Edited 10:12am  Dec 23, 2024 9:35am | Edited 10:12am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar426855_1.gif) RickM](rickm)

  * Joined Sep 2015 | Status: Trader | [2,439 Posts](/search?do=process&provider=Member&searchuser=426855)

> [Quoting MachineLearn](/thread/post/15097494#post15097494 "View Quoted Post")
> 
> Disliked
> 
> BTC M1 Nice one band setup that went exactly as the system calculates. Price exploded out of the squeeze. {image} {image}
> 
> Ignored

Hi Machine  
  
I reckon you are using a Bollinger Band set on SMA instead of its better back tested settings of EMA. That way you get the both bands aligned correctly.  
I like both set to 21 MA as you can see with the chart below.  
  
Then I would focus on a break away of the white EMA during a Bollinger Band Squeeze.  
  
I think BTCUSD offers the best Squeeze setups I have ever seen, especially on the H1 time frame.  
It’s still a scalping strategy so I never used a trailing stop but just look to exit the position when the momentum stops. And that stoping is when price falls below the white 21 EMA line or if price hits massive resistance zone.  
  
Lastly I always look for trend or trend separation from its correct volume value pricing meaning that trade also had a reversal play on VWAP.  
So you had a combo of a nice a Squeeze/ VWAP setup which is a 88% sure winner always.  
  
Currently trading from a Japanese mountain resort north of Sapporo during the holiday break which is a period I love trading due to high volatility / low volume markets. I normally trade reversals mostly during these period's because trends can become a gamble.  
  
Cheers 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: IMG_2923.jpeg
Size: 768 KB](/attachment/image/4866362/thumbnail?d=1734914124)](/attachment/image/4866362?d=1734914124)   

Trading thin liquidity at the boundary of the charts

[0 ](javascript:void\(0\);) [4 ](javascript:void\(0\);)

  * [#44](/thread/post/15097571#post15097571 "Post Permalink")

  * Edited 10:07am  Dec 23, 2024 9:55am | Edited 10:07am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

> [Quoting RickM](/thread/post/15097561#post15097561 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi Machine I reckon you are using a Bollinger Band set on SMA instead of its better back tested settings of EMA. That way you get the both bands aligned correctly. I like both set to 21 MA as you can see with the chart below. Then I would focus on a break away of the white EMA during a Bollinger Band Squeeze. I think BTCUSD offers the best Squeeze setups I have ever seen, especially on the H1 time frame. It’s still a scalping strategy so I never used a trailing stop but just look to exit the position when the momentum stops. And that stoping...
> 
> Ignored

Beautiful, will adjust accordingly. Any other input please let us know!  
  
I'm also a fan of looking for reversal plays during the squeeze. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#45](/thread/post/15097650#post15097650 "Post Permalink")

  * Dec 23, 2024 1:22pm  Dec 23, 2024 1:22pm 

  * [ arya.aryaee](arya.aryaee)

  * | Joined Oct 2012  | Status: Trader | [329 Posts](/search?do=process&provider=Member&searchuser=303027)

> [Quoting RickM](/thread/post/15097561#post15097561 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi Machine I reckon you are using a Bollinger Band set on SMA instead of its better back tested settings of EMA. That way you get the both bands aligned correctly. I like both set to 21 MA as you can see with the chart below. Then I would focus on a break away of the white EMA during a Bollinger Band Squeeze. I think BTCUSD offers the best Squeeze setups I have ever seen, especially on the H1 time frame. It’s still a scalping strategy so I never used a trailing stop but just look to exit the position when the momentum stops. And that stoping...
> 
> Ignored

Hi RickM! kindky which setting are you using for keltner and bb? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#46](/thread/post/15097939#post15097939 "Post Permalink")

  * Edited 8:55pm  Dec 23, 2024 8:41pm | Edited 8:55pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1967050_1.gif) Ju4ara](ju4ara)

  * | Joined Oct 2024  | Status: Trader | [105 Posts](/search?do=process&provider=Member&searchuser=1967050)

Hi, I am exploring bb squeeze and how it works, so I can implement it in my system in the future(have spent whole weekend it). Also, it's not clearly exact system as squeeze n Go(not using super trend and momentum yet, but use VWAP instead), so sorry for that too, if ML thinks I shouldn't do that I will delete my post asap. Here is the possible trade I've found on BTC/USD, it is not totally set up yet. Price bounced off of VWAP(light-blue line) before the squee and broke over 21ema(white line),also change oh character on 1h tf. Is it a good idea to enter trade when bb leaves Keltner and price is still above VWAP and 21ema. Thanks in advance. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 116 KB](/attachment/image/4866635/thumbnail?d=1734953932)](/attachment/image/4866635?d=1734953932)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#47](/thread/post/15097947#post15097947 "Post Permalink")

  * Dec 23, 2024 8:47pm  Dec 23, 2024 8:47pm 

  * [ Merka](merka)

  * Joined Jan 2016 | Status: Trader | [1,944 Posts](/search?do=process&provider=Member&searchuser=440568)

> [Quoting RickM](/thread/post/15097561#post15097561 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi Machine I reckon you are using a Bollinger Band set on SMA instead of its better back tested settings of EMA. That way you get the both bands aligned correctly. I like both set to 21 MA as you can see with the chart below. Then I would focus on a break away of the white EMA during a Bollinger Band Squeeze. I think BTCUSD offers the best Squeeze setups I have ever seen, especially on the H1 time frame. It’s still a scalping strategy so I never used a trailing stop but just look to exit the position when the momentum stops. And that stoping...
> 
> Ignored

Can you please give an example on how you use the squeeze method with the VWAP.  
Didn't understood fully from your previous post  
Thanks 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#48](/thread/post/15097967#post15097967 "Post Permalink")

  * Dec 23, 2024 9:10pm  Dec 23, 2024 9:10pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar426855_1.gif) RickM](rickm)

  * Joined Sep 2015 | Status: Trader | [2,439 Posts](/search?do=process&provider=Member&searchuser=426855)

> [Quoting arya.aryaee](/thread/post/15097650#post15097650 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi RickM! kindky which setting are you using for keltner and bb?
> 
> Ignored

Hi arya  
  
Bollinger Bands 21 EMA with bands at 2  
Keltner Channel 21 EMA with bands at 1.5  
  
I use 21 instead of 20 because it's at Fibonacial Number. It backtests better on price action setups..  
As for stop loss, either place it under opposite band or use 2 ATR as a good safety stop.   
  
I would demo trade any settings unchanged for at least 100 setups - then judge the results it produces. As a normal guide, it's not usual for me to get 10-12 winners in a row before running into a 4-5 losing trade block. 

Trading thin liquidity at the boundary of the charts

[0 ](javascript:void\(0\);) [6 ](javascript:void\(0\);)

  * [#49](/thread/post/15097970#post15097970 "Post Permalink")

  * Dec 23, 2024 9:18pm  Dec 23, 2024 9:18pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar588299_3.gif) RiskFighter](riskfighter)

  * Joined Jun 2017 | Status: Trader | [1,566 Posts](/search?do=process&provider=Member&searchuser=588299) | Online Now 

I once saw a tool on Trading view that I liked. Could not find something like it at MT4, so I coded it. Identifying those squeezes and widenings can be a bit tricky for my old eyes. So I made it with bars.  
  
Set the MM_Length to the same value as the BB. Set the other parameters to true.

  1. Darkred - bands are widening, but are still inside the average of the x bars back.
  2. DarkGreen - bands are widening, and are now outside the average of the x bars back.
  3. LightGreen - bands are squeezing but are still wider than the average of the x bars back.
  4. LightRed - bands are narrower than the average of the x bars back.
  5. When bars are green, they are larger than the yellow line. It means that the bands are wider than the average of the last x bars.

It is an indicator by the way.  
  
You guys might thinks this is overkill and unnessesary, then don't use it.  
  
Merry Christmas 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 27 KB](/attachment/image/4866665/thumbnail?d=1734956452)](/attachment/image/4866665?d=1734956452)   

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [BollingerMomentum_6.ex4](/attachment/file/4866660?d=1734956327) 10 KB | 234 downloads 

Read post #1 !! Then read it again 10 more times before you ask.

[0 ](javascript:void\(0\);) [4 ](javascript:void\(0\);)

  * [#50](/thread/post/15097987#post15097987 "Post Permalink")

  * Dec 23, 2024 9:40pm  Dec 23, 2024 9:40pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

> [Quoting Ju4ara](/thread/post/15097939#post15097939 "View Quoted Post")
> 
> Disliked
> 
> Hi, I am exploring bb squeeze and how it works, so I can implement it in my system in the future(have spent whole weekend it). Also, it's not clearly exact system as squeeze n Go(not using super trend and momentum yet, but use VWAP instead), so sorry for that too, if ML thinks I shouldn't do that I will delete my post asap. Here is the possible trade I've found on BTC/USD, it is not totally set up yet. Price bounced off of VWAP(light-blue line) before the squee and broke over 21ema(white line),also change oh character on 1h tf. Is it a good idea...
> 
> Ignored

Any variation and customization is absolutely fine, we're all here to experiment. The initial system was just a concept from a coder on TradingView, I'm not married to it. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#51](/thread/post/15097993#post15097993 "Post Permalink")

  * Dec 23, 2024 9:56pm  Dec 23, 2024 9:56pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1967050_1.gif) Ju4ara](ju4ara)

  * | Joined Oct 2024  | Status: Trader | [105 Posts](/search?do=process&provider=Member&searchuser=1967050)

> [Quoting MachineLearn](/thread/post/15097987#post15097987 "View Quoted Post")
> 
> Disliked
> 
> {quote} Any variation and customization is absolutely fine, we're all here to experiment. The initial system was just a concept from a coder on TradingView, I'm not married to it.
> 
> Ignored

I just don't understand yet how to use bb squeeze, I am still guessing about where and when to enter 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#52](/thread/post/15098019#post15098019 "Post Permalink")

  * Dec 23, 2024 10:22pm  Dec 23, 2024 10:22pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar426855_1.gif) RickM](rickm)

  * Joined Sep 2015 | Status: Trader | [2,439 Posts](/search?do=process&provider=Member&searchuser=426855)

> [Quoting Merka](/thread/post/15097947#post15097947 "View Quoted Post")
> 
> Disliked
> 
> {quote} Can you please give an example on how you use the squeeze method with the VWAP. Didn't understood fully from your previous post Thanks
> 
> Ignored

Hi Merka  
  
I use VWAP if I am looking for Squeeze setups when trading on smaller timeframes with markets that do provide Level 2 data.  
  
No wise trader should go long if the VWAP value line is above a strong bearish move, unless it has moved out at least 2 deviations.  
  
Almost every single prop firm trader, hedge fund manager and banker these days is now trained to only BUY stock / Future contracts if price is over the daily VWAP line or SELL stock / Future contracts if price is under daily VWAP line.. A public confirmation of this trend was made public by Ken Griffin who runs Citadel LLC, which turns over around 30-40% of total volume on the US Stock Markets. He openly discussed how if he plans to buy 100,000 stock of any company, his traders using Algorithms will attack the order book with 100 size trades for days or weeks till he gets his fill - but only if the orders average close to the Daily VWAP line.  
  
The whole world has turned VWAP crazy it seems..  
  
Therefore I don't want to fight against the tide, but rather surf in on the next wave. That BITCOIN trade above had moved out about 2 deviations so was likely to reverse back to the volume average. Therefore a Squeeze setup & a VWAP setup.  
  
Unfortunately its no use for Forex Markets and I don't need to tell anyone why. 

Trading thin liquidity at the boundary of the charts

[0 ](javascript:void\(0\);) [4 ](javascript:void\(0\);)

  * [#53](/thread/post/15098025#post15098025 "Post Permalink")

  * Dec 23, 2024 10:29pm  Dec 23, 2024 10:29pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar426855_1.gif) RickM](rickm)

  * Joined Sep 2015 | Status: Trader | [2,439 Posts](/search?do=process&provider=Member&searchuser=426855)

> [Quoting Ju4ara](/thread/post/15097993#post15097993 "View Quoted Post")
> 
> Disliked
> 
> {quote} I just don't understand yet how to use bb squeeze, I am still guessing about where and when to enter
> 
> Ignored

Hi Ju4ara  
  
  
The original idea is you go long if price is above the 21 EMA once the Bollinger Bands move back outside the Keltner Channel.  
  
That's the design of this system, but we all may see something else that suits them.  
Personally, a strong break of the 21 EMA after a Bollinger Band pinch is often enough for me to enter. 

Trading thin liquidity at the boundary of the charts

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#54](/thread/post/15098046#post15098046 "Post Permalink")

  * Dec 23, 2024 10:45pm  Dec 23, 2024 10:45pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar272159_71.gif) driven18](driven18)

  * Joined Jul 2012 | Status: Trader | [1,385 Posts](/search?do=process&provider=Member&searchuser=272159)

> [Quoting RickM](/thread/post/15098019#post15098019 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi Merka I use VWAP if I am looking for Squeeze setups when trading on smaller timeframes with markets that do provide Level 2 data. No wise trader should go long if the VWAP value line is above a strong bearish move, unless it has moved out at least 2 deviations. Almost every single prop firm trader, hedge fund manager and banker these days is now trained to only BUY stock / Future contracts if price is over the daily VWAP line or SELL stock / Future contracts if price is under daily VWAP line.. A public confirmation of this trend was made...
> 
> Ignored

Sapporo is a beer I drink when going to sushi restaurants in US. It is very famous Japanese beer. Have fun ![](https://resources.faireconomy.media/images/emojis/64/1f600.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f37a.png?v=15.1)

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#55](/thread/post/15098085#post15098085 "Post Permalink")

  * Dec 23, 2024 11:20pm  Dec 23, 2024 11:20pm 

  * [ averied](averied)

  * | Joined Aug 2013  | Status: Trader | [32 Posts](/search?do=process&provider=Member&searchuser=347416)

> [Quoting MachineLearn](/thread/post/15096762#post15096762 "View Quoted Post")
> 
> Disliked
> 
> The guidelines provided here are just a starting point to help you build your own rules. It’s also worth mentioning that I personally avoid relying on Expert Advisors (EAs) or fully automated systems. For experienced traders, discretion is a critical element in decision-making. The market is dynamic, and no rigid rule set can capture all its nuances.
> 
> Ignored

IMO, this is just a way of fooling yourself. Unless you backtest this for a considerable amount of time, you have no way of knowing if you are wasting your time trading this. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#56](/thread/post/15098116#post15098116 "Post Permalink")

  * Dec 23, 2024 11:47pm  Dec 23, 2024 11:47pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

> [Quoting averied](/thread/post/15098085#post15098085 "View Quoted Post")
> 
> Disliked
> 
> {quote} IMO, this is just a way of fooling yourself. Unless you backtest this for a considerable amount of time, you have no way of knowing if you are wasting your time trading this.
> 
> Ignored

I respect your opinion and use to think this way when I first started. You want back testing results that tell you that the system works x% of the time. Fundamentally, I don't agree with rigid rule sets and binary operations.  
  
IMO, the best trading is done when you can combine the discretional decision making and analysis of a experienced trader with the emotions of a robot. Some here are experienced and some are not. The ones who aren't are usually the ones begging and whining for EAs because the think they plug and play a magical robot and become profitable over night. If you're experienced however, you don't need back test results to understand if a system works for you or not. You need forward testing results to compare to your real life trading experience. The true key is controlling your emotions at the end of the day.  
  
Since we disagree fundamentally this thread is probably not for you my brother. 

[0 ](javascript:void\(0\);) [3 ](javascript:void\(0\);)

  * [#57](/thread/post/15098193#post15098193 "Post Permalink")

  * Dec 24, 2024 12:43am  Dec 24, 2024 12:43am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar588299_3.gif) RiskFighter](riskfighter)

  * Joined Jun 2017 | Status: Trader | [1,566 Posts](/search?do=process&provider=Member&searchuser=588299) | Online Now 

> [Quoting RickM](/thread/post/15098019#post15098019 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi Merka I use VWAP if I am looking for Squeeze setups when trading on smaller timeframes with markets that do provide Level 2 data. No wise trader should go long if the VWAP value line is above a strong bearish move, unless it has moved out at least 2 deviations. Almost every single prop firm trader, hedge fund manager and banker these days is now trained to only BUY stock / Future contracts if price is over the daily VWAP line or SELL stock / Future contracts if price is under daily VWAP line.. A public confirmation of this trend was made...
> 
> Ignored

Very interesting information. Thank you. 

Read post #1 !! Then read it again 10 more times before you ask.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#58](/thread/post/15098232#post15098232 "Post Permalink")

  * Dec 24, 2024 1:31am  Dec 24, 2024 1:31am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

NQ Pre Market (Gray dots at top represent squeeze). I removed the components of the actual squeeze(BB and KC) on the screen for clarity   
  
This was a one band (top) squeeze  
  
Also Momentum bars are hard to see but they're pushing bullish as well 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot_20241223_113041_Photos.jpg
Size: 451 KB](/attachment/image/4866820/thumbnail?d=1734971464)](/attachment/image/4866820?d=1734971464)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#59](/thread/post/15098235#post15098235 "Post Permalink")

  * Dec 24, 2024 1:33am  Dec 24, 2024 1:33am 

  * [ arya.aryaee](arya.aryaee)

  * | Joined Oct 2012  | Status: Trader | [329 Posts](/search?do=process&provider=Member&searchuser=303027)

> [Quoting RickM](/thread/post/15097967#post15097967 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi arya Bollinger Bands 21 EMA with bands at 2 Keltner Channel 21 EMA with bands at 1.5 I use 21 instead of 20 because it's at Fibonacial Number. It backtests better on price action setups.. As for stop loss, either place it under opposite band or use 2 ATR as a good safety stop. I would demo trade any settings unchanged for at least 100 setups - then judge the results it produces. As a normal guide, it's not usual for me to get 10-12 winners in a row before running into a 4-5 losing trade block.
> 
> Ignored

Thankyou Rick due to your prompt reply!nice of you 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#60](/thread/post/15098286#post15098286 "Post Permalink")

  * Dec 24, 2024 2:17am  Dec 24, 2024 2:17am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

SL at BB  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot_20241223_121722_Photos.jpg
Size: 388 KB](/attachment/image/4866863/thumbnail?d=1734974258)](/attachment/image/4866863?d=1734974258)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Squeeze n Go | MTF System
  *   * [ **Reply to Thread** ](/thread/1319487-squeeze-n-go-mtf-system/reply#reply)

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

[Spud's MTF FIB Breakout System](/thread/30109-spuds-mtf-fib-breakout-system "Spud's MTF FIB Breakout System 
-------------------------------- 
Ever since I learned about Fibonacci numbers they have interested my pure...") 375 replies

[H1Scalper System (MTF D1,H1,M5)](/thread/166646-h1scalper-system-mtf-d1h1m5 "Here are the indicators for a manual system. 
  
Explanations, rules and trading ideas are coming... 
. 
\(2009.05.13\) 
Attached are the...") 725 replies

[MTF Trix system](/thread/183801-mtf-trix-system "Hello everybody, 
 
This thread is for developing and discussing a multi-timeframe trading system that is based on one indicator - Trix -...") 3,697 replies

[MTF Stochastics into MTF Stoch Histogram](/thread/359918-mtf-stochastics-into-mtf-stoch-histogram "Hi, 
 
I have been trading with the help of MTF Stochastics for a few weeks now with relatively good results but would appreciate if...") 8 replies

[MTF Vajioo Scalping System](/thread/195912-mtf-vajioo-scalping-system "RUBBISH") 15 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/1319487-squeeze-n-go-mtf-system/reply#reply)
  * Subscribe
  * [216](javascript:void\(0\);)

Attachments: Squeeze n Go | MTF System

Tags: Squeeze n Go | MTF System

#  [](/thread/1319487-squeeze-n-go-mtf-system)Squeeze n Go | MTF System 

  * 

  * [#61](/thread/post/15098440#post15098440 "Post Permalink")

  * Dec 24, 2024 9:02am  Dec 24, 2024 9:02am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar426855_1.gif) RickM](rickm)

  * Joined Sep 2015 | Status: Trader | [2,439 Posts](/search?do=process&provider=Member&searchuser=426855)

FOREX TRADERS  
  
When I trade the Squeeze on Forex Markets, I find this setup the best.  
  
Generally Forex Markets produce many fake outs so I find it best to trade with a EMA Trend Ribbon (EMA 21 - 34 -55 -89).  
Most trades I take are on H1 or M5 but I always see what the Daily chart is doing.  
  
Using the TTM Squeeze Pro (Tradingview), trade the breakout of RED DOTS (BB inside Keltner Channel) to black dots if the momentum indicator agrees.  
  
  
Below is EURJPY on H1. Here we are only looking for Bearish signals and the take profit signal is when the Momentum Histogram turns from Red to Yellow and moving backwards. Also on the multi - time frame view, there is Squeeze setups on 15M / 30M / W / M  
  
If in doubt, the WHITE EMA which is 21 is KING.  
  
Cheers 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: EEEJ.png
Size: 155 KB](/attachment/image/4866974/thumbnail?d=1734999109)](/attachment/image/4866974?d=1734999109)   

Trading thin liquidity at the boundary of the charts

[0 ](javascript:void\(0\);) [6 ](javascript:void\(0\);)

  * [#62](/thread/post/15098448#post15098448 "Post Permalink")

  * Dec 24, 2024 9:18am  Dec 24, 2024 9:18am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

> [Quoting RickM](/thread/post/15098440#post15098440 "View Quoted Post")
> 
> Disliked
> 
> FOREX TRADERS When I trade the Squeeze on Forex Markets, I find this setup the best. Generally Forex Markets produce many fake outs so I find it best to trade with a EMA Trend Ribbon (EMA 21 - 34 -55 -89). Most trades I take are on H1 or M5 but I always see what the Daily chart is doing. Using the TTM Squeeze Pro (Tradingview), trade the breakout of RED DOTS (BB inside Keltner Channel) to black dots if the momentum indicator agrees. Below is EURJPY on H1. Here we are only looking for Bearish signals and the take profit signal is when the Momentum...
> 
> Ignored

Sounds good. Updating the system to align with your methodology as we move forward. First post has been updated. Let's master this approach. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#63](/thread/post/15098452#post15098452 "Post Permalink")

  * Dec 24, 2024 9:25am  Dec 24, 2024 9:25am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

> [Quoting RickM](/thread/post/15098440#post15098440 "View Quoted Post")
> 
> Disliked
> 
> FOREX TRADERS When I trade the Squeeze on Forex Markets, I find this setup the best. Generally Forex Markets produce many fake outs so I find it best to trade with a EMA Trend Ribbon (EMA 21 - 34 -55 -89). Most trades I take are on H1 or M5 but I always see what the Daily chart is doing. Using the TTM Squeeze Pro (Tradingview), trade the breakout of RED DOTS (BB inside Keltner Channel) to black dots if the momentum indicator agrees. Below is EURJPY on H1. Here we are only looking for Bearish signals and the take profit signal is when the Momentum...
> 
> Ignored

For clairty, we should trade the breakout of the black dots to the red dots you mean? The black dots represent the squeeze and when the squeeze releases it will change to red dots right. Then use momentum for confluence. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#64](/thread/post/15098459#post15098459 "Post Permalink")

  * Dec 24, 2024 9:37am  Dec 24, 2024 9:37am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar426855_1.gif) RickM](rickm)

  * Joined Sep 2015 | Status: Trader | [2,439 Posts](/search?do=process&provider=Member&searchuser=426855)

Attached Image (click to enlarge)

[![Click to Enlarge

Name: FBI2.png
Size: 169 KB](/attachment/image/4866989/thumbnail?d=1735000972)](/attachment/image/4866989?d=1735000972)   

Trading thin liquidity at the boundary of the charts

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#65](/thread/post/15098464#post15098464 "Post Permalink")

  * Dec 24, 2024 9:45am  Dec 24, 2024 9:45am 

  * [ sln](sln)

  * | Joined Jun 2014  | Status: Trader | [46 Posts](/search?do=process&provider=Member&searchuser=376125)

Hi RickM,  
is there anyway you could share the indicators and template please?TIA  
the mtf indicator of the mom and squeeze looks interesting 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#66](/thread/post/15098475#post15098475 "Post Permalink")

  * Dec 24, 2024 10:10am  Dec 24, 2024 10:10am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar426855_1.gif) RickM](rickm)

  * Joined Sep 2015 | Status: Trader | [2,439 Posts](/search?do=process&provider=Member&searchuser=426855)

Then we need to learn to evaluate setups into 3 groups - A+ Setups. - B Setups - C Setups  
  
We only want to trade A+ Setups at Full size and B Setups at half size. C Setups avoid because the result is small profit for much mental energy.  
  
The final step is to practice trading A+ setups with additional trades to obtain BIG Positions.  
  
Trade safety guys 

Trading thin liquidity at the boundary of the charts

[0 ](javascript:void\(0\);) [3 ](javascript:void\(0\);)

  * [#67](/thread/post/15098485#post15098485 "Post Permalink")

  * Dec 24, 2024 10:29am  Dec 24, 2024 10:29am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

**M1 Gold 2 hours ago**

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot_20241223_202625_Photos.jpg
Size: 535 KB](/attachment/image/4867000/thumbnail?d=1735003599)](/attachment/image/4867000?d=1735003599)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#68](/thread/post/15098526#post15098526 "Post Permalink")

  * Dec 24, 2024 12:33pm  Dec 24, 2024 12:33pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

Trade still active as histo hasn't changed or momentum 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot_20241223_223258_Photos.jpg
Size: 465 KB](/attachment/image/4867027/thumbnail?d=1735011199)](/attachment/image/4867027?d=1735011199)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#69](/thread/post/15098774#post15098774 "Post Permalink")

  * Dec 24, 2024 8:01pm  Dec 24, 2024 8:01pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar426855_1.gif) RickM](rickm)

  * Joined Sep 2015 | Status: Trader | [2,439 Posts](/search?do=process&provider=Member&searchuser=426855)

> [Quoting sln](/thread/post/15098464#post15098464 "View Quoted Post")
> 
> Disliked
> 
> Hi RickM, is there anyway you could share the indicators and template please?TIA the mtf indicator of the mom and squeeze looks interesting
> 
> Ignored

Hi sin  
  
On Tradingview Platform  
  
MTF Squeeze Pro  
TTM Squeeze Pro  
EMA Ribbon   
  
Cheers 

Trading thin liquidity at the boundary of the charts

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#70](/thread/post/15098827#post15098827 "Post Permalink")

  * Dec 24, 2024 10:02pm  Dec 24, 2024 10:02pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1967050_1.gif) Ju4ara](ju4ara)

  * | Joined Oct 2024  | Status: Trader | [105 Posts](/search?do=process&provider=Member&searchuser=1967050)

> [Quoting RickM](/thread/post/15098475#post15098475 "View Quoted Post")
> 
> Disliked
> 
> Then we need to learn to evaluate setups into 3 groups - A+ Setups. - B Setups - C Setups We only want to trade A+ Setups at Full size and B Setups at half size. C Setups avoid because the result is small profit for much mental energy. The final step is to practice trading A+ setups with additional trades to obtain BIG Positions. Trade safety guys
> 
> Ignored

Hi, what is considered A+ setup? Thanks. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#71](/thread/post/15098895#post15098895 "Post Permalink")

  * Edited Dec 25, 2024 12:31am  Dec 24, 2024 11:57pm | Edited Dec 25, 2024 12:31am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar272159_71.gif) driven18](driven18)

  * Joined Jul 2012 | Status: Trader | [1,385 Posts](/search?do=process&provider=Member&searchuser=272159)

Direction just changed to Bullish, all EMA's pointing up and below the yellow **King 21 EMA**(per RickM from Japan ![](https://resources.faireconomy.media/images/emojis/64/1f1ef-1f1f5.png?v=15.1) ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)), I am simplifying a bit for the sake of this thread, but this **first meaningful** squeeze I would be taking on Dow Futures 5 Min TF 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 16 KB](/attachment/image/4867266/thumbnail?d=1735053142)](/attachment/image/4867266?d=1735053142)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#72](/thread/post/15098918#post15098918 "Post Permalink")

  * Dec 25, 2024 12:59am  Dec 25, 2024 12:59am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar272159_71.gif) driven18](driven18)

  * Joined Jul 2012 | Status: Trader | [1,385 Posts](/search?do=process&provider=Member&searchuser=272159)

Just now - 1 Min Dow futures 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 11 KB](/attachment/image/4867282/thumbnail?d=1735055983)](/attachment/image/4867282?d=1735055983)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#73](/thread/post/15098923#post15098923 "Post Permalink")

  * Dec 25, 2024 1:11am  Dec 25, 2024 1:11am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

> [Quoting driven18](/thread/post/15098918#post15098918 "View Quoted Post")
> 
> Disliked
> 
> Just now - 1 Min Dow futures {image}
> 
> Ignored

Nice one, seems to be squeezing again. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#74](/thread/post/15098933#post15098933 "Post Permalink")

  * Edited 2:09am  Dec 25, 2024 1:48am | Edited 2:09am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar272159_71.gif) driven18](driven18)

  * Joined Jul 2012 | Status: Trader | [1,385 Posts](/search?do=process&provider=Member&searchuser=272159)

> [Quoting MachineLearn](/thread/post/15098923#post15098923 "View Quoted Post")
> 
> Disliked
> 
> {quote} Nice one, seems to be squeezing again.
> 
> Ignored

I like first squeeze after trend change, after that, I do not like squeezes that did not retrace properly...I would rather load up on the 1st squeeze and manage it with MM 'till the obliiiiivion or 'till I see red histogram.  
  
The 3rd squeeze has potential as yellow EMA retraced nicely into the Blue EMA. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 17 KB](/attachment/image/4867289/thumbnail?d=1735058936)](/attachment/image/4867289?d=1735058936)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#75](/thread/post/15098942#post15098942 "Post Permalink")

  * Dec 25, 2024 2:10am  Dec 25, 2024 2:10am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

> [Quoting driven18](/thread/post/15098933#post15098933 "View Quoted Post")
> 
> Disliked
> 
> {quote} I like first squeeze after trend change, after that, I do not like squeezes that did not retrace properly...I would rather load up on the 1st squeeze and manage it with MM 'till the obliiiiivion or 'till I see red histogram. The 3rd squeeze has potential as yellow EMA retraced nicely into the Blue EMA. {image}
> 
> Ignored

Agreed. Third one took off haha 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#76](/thread/post/15099039#post15099039 "Post Permalink")

  * Dec 25, 2024 9:03am  Dec 25, 2024 9:03am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar426855_1.gif) RickM](rickm)

  * Joined Sep 2015 | Status: Trader | [2,439 Posts](/search?do=process&provider=Member&searchuser=426855)

> [Quoting Ju4ara](/thread/post/15098827#post15098827 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi, what is considered A+ setup? Thanks.
> 
> Ignored

Hi Ju4ara  
  
A+ Setups are always on Trend with price leaving the 21 EMA with Momentum.  
  
The original indicator for momentum is using a indicator found on every single trading platform.  
That's "Momentum " set to 12 with a line through either the 00 or 100.  
  
If yo use the TTM Squeeze Indicator - the design was to enter a Long on lite blue and exit after 2 bars of dark blue.  
Personally I just exit when price crosses back over the 21 EMA  
  
  
Happy Holidays 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: DOW 2.png
Size: 179 KB](/attachment/image/4867375/thumbnail?d=1735085244)](/attachment/image/4867375?d=1735085244)   

Trading thin liquidity at the boundary of the charts

[0 ](javascript:void\(0\);) [5 ](javascript:void\(0\);)

  * [#77](/thread/post/15099090#post15099090 "Post Permalink")

  * Edited 4:58pm  Dec 25, 2024 3:52pm | Edited 4:58pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar588299_3.gif) RiskFighter](riskfighter)

  * Joined Jun 2017 | Status: Trader | [1,566 Posts](/search?do=process&provider=Member&searchuser=588299) | Online Now 

> [Quoting RickM](/thread/post/15099039#post15099039 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi Ju4ara A+ Setups are always on Trend with price leaving the 21 EMA with Momentum. The original indicator for momentum is using a indicator found on every single trading platform. That's "Momentum " set to 12 with a line through either the 00 or 100. If yo use the TTM Squeeze Indicator - the design was to enter a Long on lite blue and exit after 2 bars of dark blue. Personally I just exit when price crosses back over the 21 EMA Happy Holidays {image}
> 
> Ignored

MT4 traders can use Bill Williams Awesome Oscillator.  
  
Here you have both the Momentum set to 12 and the Williams.  
  
Won't work in ranging - hence the Squeeze strategy. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 29 KB](/attachment/image/4867426/thumbnail?d=1735113491)](/attachment/image/4867426?d=1735113491)   

Read post #1 !! Then read it again 10 more times before you ask.

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#78](/thread/post/15099107#post15099107 "Post Permalink")

  * Dec 25, 2024 5:55pm  Dec 25, 2024 5:55pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1967050_1.gif) Ju4ara](ju4ara)

  * | Joined Oct 2024  | Status: Trader | [105 Posts](/search?do=process&provider=Member&searchuser=1967050)

> [Quoting RickM](/thread/post/15099039#post15099039 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi Ju4ara A+ Setups are always on Trend with price leaving the 21 EMA with Momentum. The original indicator for momentum is using an indicator found on every single trading platform. That's "Momentum " set to 12 with a line through either the 00 or 100. If yo use the TTM Squeeze Indicator - the design was to enter a Long on lite blue and exit after 2 bars of dark blue. Personally I just exit when price crosses back over the 21 EMA Happy Holidays {image}
> 
> Ignored

Thanks for making it clear. What timeframe would you recommend to trade indices with bb squeeze? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#79](/thread/post/15099115#post15099115 "Post Permalink")

  * Dec 25, 2024 6:42pm  Dec 25, 2024 6:42pm 

  * [ HazHazHaz](hazhazhaz)

  * | Joined Feb 2023  | Status: Trader | [188 Posts](/search?do=process&provider=Member&searchuser=1593215)

Hi MachineLearn and RickM,  
  
Roughly which session and which pairs are do setups appear and are good usually? How many pips do you usually target? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#80](/thread/post/15099128#post15099128 "Post Permalink")

  * Dec 25, 2024 7:47pm  Dec 25, 2024 7:47pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar426855_1.gif) RickM](rickm)

  * Joined Sep 2015 | Status: Trader | [2,439 Posts](/search?do=process&provider=Member&searchuser=426855)

> [Quoting Ju4ara](/thread/post/15099107#post15099107 "View Quoted Post")
> 
> Disliked
> 
> {quote} Thanks for making it clear. What timeframe would you recommend to trade indices with bb squeeze?
> 
> Ignored

Hi. JU4ara  
  
Check out Rocky's thread, he only trades ES (US500) on the 1 minute chart and wins every day (Williams%R, SAR X-over 15 minute candles).  
  
Personally I like the Two Minute chart for Squueze's but both of us are intraday traders.  
Otherwise, look at M5 or H1 for the best setups.  
  
Cheers 

Trading thin liquidity at the boundary of the charts

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Squeeze n Go | MTF System
  *   * [ **Reply to Thread** ](/thread/1319487-squeeze-n-go-mtf-system/reply#reply)

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

[Spud's MTF FIB Breakout System](/thread/30109-spuds-mtf-fib-breakout-system "Spud's MTF FIB Breakout System 
-------------------------------- 
Ever since I learned about Fibonacci numbers they have interested my pure...") 375 replies

[H1Scalper System (MTF D1,H1,M5)](/thread/166646-h1scalper-system-mtf-d1h1m5 "Here are the indicators for a manual system. 
  
Explanations, rules and trading ideas are coming... 
. 
\(2009.05.13\) 
Attached are the...") 725 replies

[MTF Trix system](/thread/183801-mtf-trix-system "Hello everybody, 
 
This thread is for developing and discussing a multi-timeframe trading system that is based on one indicator - Trix -...") 3,697 replies

[MTF Stochastics into MTF Stoch Histogram](/thread/359918-mtf-stochastics-into-mtf-stoch-histogram "Hi, 
 
I have been trading with the help of MTF Stochastics for a few weeks now with relatively good results but would appreciate if...") 8 replies

[MTF Vajioo Scalping System](/thread/195912-mtf-vajioo-scalping-system "RUBBISH") 15 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/1319487-squeeze-n-go-mtf-system/reply#reply)
  * Subscribe
  * [216](javascript:void\(0\);)

Attachments: Squeeze n Go | MTF System

Tags: Squeeze n Go | MTF System

#  [](/thread/1319487-squeeze-n-go-mtf-system)Squeeze n Go | MTF System 

  * 

  * [#81](/thread/post/15099129#post15099129 "Post Permalink")

  * Dec 25, 2024 8:00pm  Dec 25, 2024 8:00pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar426855_1.gif) RickM](rickm)

  * Joined Sep 2015 | Status: Trader | [2,439 Posts](/search?do=process&provider=Member&searchuser=426855)

> [Quoting HazHazHaz](/thread/post/15099115#post15099115 "View Quoted Post")
> 
> Disliked
> 
> Hi MachineLearn and RickM, Roughly which session and which pairs are do setups appear and are good usually? How many pips do you usually target?
> 
> Ignored

Hi Haz  
  
Without doubt, the best session to trade is from US Open. If you can trade then, the best in order is US500 / DOW /. Nasdaq / US2000.  
I am based out of Australia so that time period is hard for me to trade often (US Open starts at 12.30am for me) so I normally trade 3 primary markets during the London session instead. I favour ES / Gold / Oil Futures but also watch EU & Bitcoin.  
  
Bitcoin on the One Hour Chart offers perhaps the BEST SQUEEZE'S Setups I have ever seen - always watch it.  
  
As for Targets, I don't have any. Just trade the setup till momentum fails (or cross of the 21EMA).   
On Forex, H1 works best.  
  
Cheers 

Trading thin liquidity at the boundary of the charts

[0 ](javascript:void\(0\);) [4 ](javascript:void\(0\);)

  * [#82](/thread/post/15099136#post15099136 "Post Permalink")

  * Dec 25, 2024 8:17pm  Dec 25, 2024 8:17pm 

  * [ HazHazHaz](hazhazhaz)

  * | Joined Feb 2023  | Status: Trader | [188 Posts](/search?do=process&provider=Member&searchuser=1593215)

> [Quoting RickM](/thread/post/15099129#post15099129 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi Haz Without doubt, the best session to trade is from US Open. If you can trade then, the best in order is US500 / DOW /. Nasdaq / US2000. I am based out of Australia so that time period is hard for me to trade often (US Open starts at 12.30am for me) so I normally trade 3 primary markets during the London session instead. I favour ES / Gold / Oil Futures but also watch EU & Bitcoin. Bitcoin on the One Hour Chart offers perhaps the BEST SQUEEZE'S Setups I have ever seen - always watch it. As for Targets, I don't have any. Just trade the...
> 
> Ignored

Thanks for the reply. What about Forex pairs, any favourites? I'm trying to stay away from indices and crypto.  
I shall follow this thread to learn more first. Appreciate more examples and guidance from you and MachineLearn when you can share! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#83](/thread/post/15099157#post15099157 "Post Permalink")

  * Dec 25, 2024 10:51pm  Dec 25, 2024 10:51pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1967050_1.gif) Ju4ara](ju4ara)

  * | Joined Oct 2024  | Status: Trader | [105 Posts](/search?do=process&provider=Member&searchuser=1967050)

> [Quoting RickM](/thread/post/15099039#post15099039 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi Ju4ara A+ Setups are always on Trend with price leaving the 21 EMA with Momentum. The original indicator for momentum is using a indicator found on every single trading platform. That's "Momentum " set to 12 with a line through either the 00 or 100. If yo use the TTM Squeeze Indicator - the design was to enter a Long on lite blue and exit after 2 bars of dark blue. Personally I just exit when price crosses back over the 21 EMA Happy Holidays {image}
> 
> Ignored

Which one is recommended to use, HA or candlestick? Because you use both and results of squeeze are different if you use HA. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#84](/thread/post/15099264#post15099264 "Post Permalink")

  * Edited 8:06am  Dec 26, 2024 7:52am | Edited 8:06am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

BTC H1 in a squeeze. Orange dots indicate it was extreme at one point during the squeeze which is good. On the lower time frame there was a small breakout from a squeeze but price mildly pulled back. We'll observe what happens when the squeeze ends and what momentum looks like. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot_20241225_175140_Photos.jpg
Size: 323 KB](/attachment/image/4867542/thumbnail?d=1735167151)](/attachment/image/4867542?d=1735167151)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#85](/thread/post/15099265#post15099265 "Post Permalink")

  * Dec 26, 2024 7:54am  Dec 26, 2024 7:54am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar426855_1.gif) RickM](rickm)

  * Joined Sep 2015 | Status: Trader | [2,439 Posts](/search?do=process&provider=Member&searchuser=426855)

> [Quoting Ju4ara](/thread/post/15099157#post15099157 "View Quoted Post")
> 
> Disliked
> 
> {quote} Which one is recommended to use, HA or candlestick? Because you use both and results of squeeze are different if you use HA.
> 
> Ignored

Correct, I sometimes show HA candles BUT its for illustrations reasons only.  
  
Candles & HA focus too much on the CLOSE, we should be studying the range.  
  
I trade using BARS, its best to see the range.  
If you use HA Candles, you need to change the Keltner Band spec's. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Bars.png
Size: 120 KB](/attachment/image/4867543/thumbnail?d=1735167274)](/attachment/image/4867543?d=1735167274)   

Trading thin liquidity at the boundary of the charts

[0 ](javascript:void\(0\);) [3 ](javascript:void\(0\);)

  * [#86](/thread/post/15099515#post15099515 "Post Permalink")

  * Dec 26, 2024 3:56pm  Dec 26, 2024 3:56pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar588299_3.gif) RiskFighter](riskfighter)

  * Joined Jun 2017 | Status: Trader | [1,566 Posts](/search?do=process&provider=Member&searchuser=588299) | Online Now 

I am a lousy manual trader. Weak stummock you know. But I think I will have a go with this strategy. It will make life easier if I have a mtf. indicator that sends an alarm when a possible setup occurs. Does anybody else have an interest in that? I can make it if I get help to use the right parameters.  
  
Will it be better if I do not pollude this thread with an indicator Machin?? 

Read post #1 !! Then read it again 10 more times before you ask.

[0 ](javascript:void\(0\);) [3 ](javascript:void\(0\);)

  * [#87](/thread/post/15099572#post15099572 "Post Permalink")

  * Edited 6:22pm  Dec 26, 2024 6:12pm | Edited 6:22pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1967050_1.gif) Ju4ara](ju4ara)

  * | Joined Oct 2024  | Status: Trader | [105 Posts](/search?do=process&provider=Member&searchuser=1967050)

> [Quoting RickM](/thread/post/15099039#post15099039 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi Ju4ara A+ Setups are always on Trend with price leaving the 21 EMA with Momentum. The original indicator for momentum is using a indicator found on every single trading platform. That's "Momentum " set to 12 with a line through either the 00 or 100. If yo use the TTM Squeeze Indicator - the design was to enter a Long on lite blue and exit after 2 bars of dark blue. Personally I just exit when price crosses back over the 21 EMA Happy Holidays {image}
> 
> Ignored

RickM,  
I am trying to make A+ setup entries clear. What if we are in an uptrend, red dots appear before pullback to 21ema and have yellow momentum, then pullback appears, also momentum switches to light blue and dots are still remaining red, is this A+ setup and should I enter right away on red dot or wait for black dot on the next candles with rising momentum? Scenario two is the same case is after pullback momentum also switches to light-blue but dot switched to black, how to enter in this case? And the third scenario is previous 2 scenarios, but red dot then black dot/ red dot then red dot appeared already on pullback. Thanks for patience and Happy holidays. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#88](/thread/post/15099593#post15099593 "Post Permalink")

  * Dec 26, 2024 6:54pm  Dec 26, 2024 6:54pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1967050_1.gif) Ju4ara](ju4ara)

  * | Joined Oct 2024  | Status: Trader | [105 Posts](/search?do=process&provider=Member&searchuser=1967050)

> [Quoting Ju4ara](/thread/post/15099572#post15099572 "View Quoted Post")
> 
> Disliked
> 
> {quote} RickM, I am trying to make A+ setup entries clear. What if we are in an uptrend, red dots appear before pullback to 21ema and have yellow momentum, then pullback appears, also momentum switches to light blue and dots are still remaining red, is this A+ setup and should I enter right away on red dot or wait for black dot on the next candles with rising momentum? Scenario two is the same case is after pullback momentum also switches to light-blue but dot switched to black, how to enter in this case? And the third scenario is previous 2 scenarios,...
> 
> Ignored

let's pretend there is no range and it is a trend, is this a+ setup or A+ setups are the ones which pulled back from ema with red dot, and red dot appeared on increasing momentum 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 74 KB](/attachment/image/4867661/thumbnail?d=1735206884)](/attachment/image/4867661?d=1735206884)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#89](/thread/post/15099624#post15099624 "Post Permalink")

  * Edited 8:47pm  Dec 26, 2024 8:07pm | Edited 8:47pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar426855_1.gif) RickM](rickm)

  * Joined Sep 2015 | Status: Trader | [2,439 Posts](/search?do=process&provider=Member&searchuser=426855)

> [Quoting Ju4ara](/thread/post/15099593#post15099593 "View Quoted Post")
> 
> Disliked
> 
> {quote} let's pretend there is no range and it is a trend, is this a+ setup or A+ setups are the ones which pulled back from ema with red dot, and red dot appeared on increasing momentum {image}
> 
> Ignored

Take the trade on the Black Dot if price is moving away from the 21 EMA with momentum. Risk is low because you can place your stop on the other side of the EMA and hope momentum continues for a while.  
  
AVERAGE MOVE FOR A SQUEEZE SETUP =. 6 to 8 Bars then if gifts some more

Trading thin liquidity at the boundary of the charts

[0 ](javascript:void\(0\);) [3 ](javascript:void\(0\);)

  * [#90](/thread/post/15099658#post15099658 "Post Permalink")

  * Edited 9:22pm  Dec 26, 2024 9:11pm | Edited 9:22pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar426855_1.gif) RickM](rickm)

  * Joined Sep 2015 | Status: Trader | [2,439 Posts](/search?do=process&provider=Member&searchuser=426855)

Hokkaido Gokoku - jinja Shrine  
  
About 4pm, I found a quiet spot on a bench, near that big tree and began trading. I get my inspiration from those special places in the world that raise my emotional senses - and this 120 year Shrine in the top of Japan was one of those gems. It was just me and the Bitcoin Market without a single other sole anywhere to be seen.  
  
I saw a H1 Squeeze setup and took a Long from the 21 EMA - it ran beautifully for 20 minutes but my profits were short lived because it sharply reversed back down to my STOP for a small loss.  
  
Bugger, I let a nice gain slip away. Its snowing just a bit more which relaxes me some.  
  
I read a news story about BlackRocks EFT being hit my strong withdraws from investors - $100K is too much for some. It hits me hard then that I should only be looking for Shorts so I move down to M5 Chart and look for some Squeeze Setups there.  
  
Snow is getting harder, I move uncover near some sort of Lion statue that looks grumpy that I am.  
  
Then I see another Squeeze on M5 that is following a Trend, looks like a A+ Setup.  
Range breakout - Trend - Good Momentum - Leaving the 21 EMA - CHECK. CHECK. CHECK. CHECK  
  
I'm in  
  
Wind swirls the snow some more and the sun has now set so it's getting dark. I see some worker sweeping away the snow from the entrance but no one else.  
  
Trades looking good  
  
Here comes the momentum WHAM down it goes  
  
Then it drifts, no some fanny car stuff but its still moving down some more so I stay in position.  
About now this worker starts waving his hands around - to be it means get the hell out of here.  
  
I exit this position for a 2.3% gain to my Equity, and shuttle out of the Shrine before this guy with no hair actually slams the door closed as I passed  
which made me slip down the stairs and fall in a heap at the snow covered pathway below.  
  
Laptop in good condition lucky.  
However a bruised backside to show for my efforts - BUT WHAT A GREAT PLACE TO TRADE  
  
That bald head guy was laughing, I am sure of that 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: Shrine HGJS.png
Size: 611 KB](/attachment/image/4867706/thumbnail?d=1735215121)](/attachment/image/4867706?d=1735215121)   
[![Click to Enlarge

Name: Bitcoin Box2.png
Size: 244 KB](/attachment/image/4867709/thumbnail?d=1735215765)](/attachment/image/4867709?d=1735215765)   

Trading thin liquidity at the boundary of the charts

[0 ](javascript:void\(0\);) [4 ](javascript:void\(0\);)

  * [#91](/thread/post/15099673#post15099673 "Post Permalink")

  * Dec 26, 2024 9:30pm  Dec 26, 2024 9:30pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

> [Quoting MachineLearn](/thread/post/15099264#post15099264 "View Quoted Post")
> 
> Disliked
> 
> BTC H1 in a squeeze. Orange dots indicate it was extreme at one point during the squeeze which is good. On the lower time frame there was a small breakout from a squeeze but price mildly pulled back. We'll observe what happens when the squeeze ends and what momentum looks like. {image}
> 
> Ignored

Beautiful really 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot_20241226_072911_Photos.jpg
Size: 394 KB](/attachment/image/4867722/thumbnail?d=1735216173)](/attachment/image/4867722?d=1735216173)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#92](/thread/post/15099674#post15099674 "Post Permalink")

  * Dec 26, 2024 9:31pm  Dec 26, 2024 9:31pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

> [Quoting RiskFighter](/thread/post/15099515#post15099515 "View Quoted Post")
> 
> Disliked
> 
> I am a lousy manual trader. Weak stummock you know. But I think I will have a go with this strategy. It will make life easier if I have a mtf. indicator that sends an alarm when a possible setup occurs. Does anybody else have an interest in that? I can make it if I get help to use the right parameters. Will it be better if I do not pollude this thread with an indicator Machin??
> 
> Ignored

No worries, fire away 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#93](/thread/post/15099696#post15099696 "Post Permalink")

  * Dec 26, 2024 10:02pm  Dec 26, 2024 10:02pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar272159_71.gif) driven18](driven18)

  * Joined Jul 2012 | Status: Trader | [1,385 Posts](/search?do=process&provider=Member&searchuser=272159)

> [Quoting RiskFighter](/thread/post/15099515#post15099515 "View Quoted Post")
> 
> Disliked
> 
> I am a lousy manual trader. Weak stummock you know. But I think I will have a go with this strategy. It will make life easier if I have a mtf. indicator that sends an alarm when a possible setup occurs. Does anybody else have an interest in that? I can make it if I get help to use the right parameters. Will it be better if I do not pollude this thread with an indicator Machin??
> 
> Ignored

RiskFighter, it would be great if you can code MTF squeeze dashboard in MT5, similar to this from TradingView. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 5 KB](/attachment/image/4867747/thumbnail?d=1735218476)](/attachment/image/4867747?d=1735218476)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#94](/thread/post/15099713#post15099713 "Post Permalink")

  * Dec 26, 2024 10:15pm  Dec 26, 2024 10:15pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar272159_71.gif) driven18](driven18)

  * Joined Jul 2012 | Status: Trader | [1,385 Posts](/search?do=process&provider=Member&searchuser=272159)

> [Quoting RickM](/thread/post/15099658#post15099658 "View Quoted Post")
> 
> Disliked
> 
> Hokkaido Gokoku - jinja Shrine About 4pm, I found a quiet spot on a bench, near that big tree and began trading. I get my inspiration from those special places in the world that raise my emotional senses - and this 120 year Shrine in the top of Japan was one of those gems. It was just me and the Bitcoin Market without a single other sole anywhere to be seen. I saw a H1 Squeeze setup and took a Long from the 21 EMA - it ran beautifully for 20 minutes but my profits were short lived because it sharply reversed back down to my STOP for a small loss....
> 
> Ignored

Damn boyyy, that story almost borders on Romanticism ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#95](/thread/post/15099719#post15099719 "Post Permalink")

  * Dec 26, 2024 10:25pm  Dec 26, 2024 10:25pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar588299_3.gif) RiskFighter](riskfighter)

  * Joined Jun 2017 | Status: Trader | [1,566 Posts](/search?do=process&provider=Member&searchuser=588299) | Online Now 

> [Quoting driven18](/thread/post/15099696#post15099696 "View Quoted Post")
> 
> Disliked
> 
> {quote} RiskFighter, it would be great if you can code MTF squeeze dashboard in MT5, similar to this from TradingView. {image}
> 
> Ignored

Sorry, I do not have MT5. 

Read post #1 !! Then read it again 10 more times before you ask.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#96](/thread/post/15099721#post15099721 "Post Permalink")

  * Dec 26, 2024 10:28pm  Dec 26, 2024 10:28pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar272159_71.gif) driven18](driven18)

  * Joined Jul 2012 | Status: Trader | [1,385 Posts](/search?do=process&provider=Member&searchuser=272159)

If you are **an MT5 coder(experienced)** and know how to code this dashboard indicator, identically to below TV indicator and later to code ea with few simple rules, you may want to DM me or post it here.  
  
I been trading through my personal ea for the last 3 years and know that robot is an excellent way to test, optimize and and trade markets forward.  
  
In a few weeks if no one comes up with it, I may coded it through my MT5 developers. I will then create ea out of it and put this technique through my vigorous and scientific backtesting and optimization. I studied **John Ehlers methods** and it is a real science to properly backtest and optimize. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 5 KB](/attachment/image/4867754/thumbnail?d=1735219804)](/attachment/image/4867754?d=1735219804)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#97](/thread/post/15099727#post15099727 "Post Permalink")

  * Dec 26, 2024 10:33pm  Dec 26, 2024 10:33pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar272159_71.gif) driven18](driven18)

  * Joined Jul 2012 | Status: Trader | [1,385 Posts](/search?do=process&provider=Member&searchuser=272159)

Dow Futures 2 Min TF.  
Blue dots - squeeeeeeeze.   
1\. Win  
2\. Yellow EMA went above Blue - No Trade. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 19 KB](/attachment/image/4867755/thumbnail?d=1735219993)](/attachment/image/4867755?d=1735219993)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#98](/thread/post/15099790#post15099790 "Post Permalink")

  * Dec 26, 2024 11:54pm  Dec 26, 2024 11:54pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

-> John Carter recommends entering a position after at least 5 black dots or wait for 1st green dot ; and  
-> Exit on second blue or yellow bar or, alternatively, remain in the position after confirming a continuing trend through a separate indicator. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#99](/thread/post/15099797#post15099797 "Post Permalink")

  * Dec 27, 2024 12:00am  Dec 27, 2024 12:00am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

Recent setup...  
  
Orange to red to black to green on the entry Also, stayed in a high compression squeeze for a considerable period of time.   
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot_20241226_100017_Photos.jpg
Size: 540 KB](/attachment/image/4867798/thumbnail?d=1735225232)](/attachment/image/4867798?d=1735225232)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#100](/thread/post/15099821#post15099821 "Post Permalink")

  * Dec 27, 2024 12:12am  Dec 27, 2024 12:12am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

Updated first post to include the description of the TTM Squeeze Pro indicator by the author himself.   
  
Can add context to the system and also answer any questions about the different colors and dots. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Squeeze n Go | MTF System
  *   * [ **Reply to Thread** ](/thread/1319487-squeeze-n-go-mtf-system/reply#reply)

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

[Spud's MTF FIB Breakout System](/thread/30109-spuds-mtf-fib-breakout-system "Spud's MTF FIB Breakout System 
-------------------------------- 
Ever since I learned about Fibonacci numbers they have interested my pure...") 375 replies

[H1Scalper System (MTF D1,H1,M5)](/thread/166646-h1scalper-system-mtf-d1h1m5 "Here are the indicators for a manual system. 
  
Explanations, rules and trading ideas are coming... 
. 
\(2009.05.13\) 
Attached are the...") 725 replies

[MTF Trix system](/thread/183801-mtf-trix-system "Hello everybody, 
 
This thread is for developing and discussing a multi-timeframe trading system that is based on one indicator - Trix -...") 3,697 replies

[MTF Stochastics into MTF Stoch Histogram](/thread/359918-mtf-stochastics-into-mtf-stoch-histogram "Hi, 
 
I have been trading with the help of MTF Stochastics for a few weeks now with relatively good results but would appreciate if...") 8 replies

[MTF Vajioo Scalping System](/thread/195912-mtf-vajioo-scalping-system "RUBBISH") 15 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/1319487-squeeze-n-go-mtf-system/reply#reply)
  * Subscribe
  * [216](javascript:void\(0\);)

Attachments: Squeeze n Go | MTF System

Tags: Squeeze n Go | MTF System

#  [](/thread/1319487-squeeze-n-go-mtf-system)Squeeze n Go | MTF System 

  * 

  * [#101](/thread/post/15099844#post15099844 "Post Permalink")

  * Edited 1:13am  Dec 27, 2024 12:31am | Edited 1:13am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar272159_71.gif) driven18](driven18)

  * Joined Jul 2012 | Status: Trader | [1,385 Posts](/search?do=process&provider=Member&searchuser=272159)

Nobody knows what the future will bring but it never hurts to protect yourself with trailing Sl.  
  
In a real trading I would of been going to BE or exiting already - do not like this PA(2nd chart)  
  
Reentry(3rd Chart)  
  
[https://www.forexfactory.com/thread/...7#post15099727](https://www.forexfactory.com/thread/post/15099727#post15099727)

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 17 KB](/attachment/image/4867822/thumbnail?d=1735227102)](/attachment/image/4867822?d=1735227102)   
[![Click to Enlarge

Name: screenshot.png
Size: 15 KB](/attachment/image/4867825/thumbnail?d=1735227454)](/attachment/image/4867825?d=1735227454)   
[![Click to Enlarge

Name: screenshot.png
Size: 29 KB](/attachment/image/4867841/thumbnail?d=1735229526)](/attachment/image/4867841?d=1735229526)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#102](/thread/post/15099883#post15099883 "Post Permalink")

  * Dec 27, 2024 1:36am  Dec 27, 2024 1:36am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar272159_71.gif) driven18](driven18)

  * Joined Jul 2012 | Status: Trader | [1,385 Posts](/search?do=process&provider=Member&searchuser=272159)

This is demo trading but would of been done for the day +150. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 26 KB](/attachment/image/4867861/thumbnail?d=1735230997)](/attachment/image/4867861?d=1735230997)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#103](/thread/post/15099886#post15099886 "Post Permalink")

  * Dec 27, 2024 1:39am  Dec 27, 2024 1:39am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1967050_1.gif) Ju4ara](ju4ara)

  * | Joined Oct 2024  | Status: Trader | [105 Posts](/search?do=process&provider=Member&searchuser=1967050)

Guys I've spent a bit more than a week to learn how to use bb squeeze(from rockypoint's thread initially) because I saw potential in this strategy. Today, even with stupid mistakes I've made 9RRR with this strategy on us30 and us500, I am not greedy and don't have balls to hold the trade as RickM does, So when I enter, my additional criteria is setting up tp to 5R. Thanks, RickM for sharing your wisdom, still have lots of questions, but will ask after holidays. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#104](/thread/post/15099905#post15099905 "Post Permalink")

  * Edited 6:39am  Dec 27, 2024 2:09am | Edited 6:39am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar588299_3.gif) RiskFighter](riskfighter)

  * Joined Jun 2017 | Status: Trader | [1,566 Posts](/search?do=process&provider=Member&searchuser=588299) | Online Now 

Here is my first shot for a Squeeze indicator. I am normally a robot programmer so this is out of my comfort zone and it takes time. So today you get an indicator that fills the areas where Keltner lies outside the Bollinger Bands.  
  
Don't put the Bollinger and Keltner indicators on your chart, MY indicator prints the Bollinger Bands and the Keltner Channel.  
  
You can change nessesary parameters as well as colors to your likings.  
  
With this indicator you can have - say 4 different charts on your screen and get notified when there is a setup on one of them.  
  
Tomorrow I will add the alarm function - it is not in there yet. The MTF function will come later. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 35 KB](/attachment/image/4867870/thumbnail?d=1735232715)](/attachment/image/4867870?d=1735232715)   

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [SqueezeBBK_3.ex4](/attachment/file/4867871?d=1735232939) 13 KB | 180 downloads 

Read post #1 !! Then read it again 10 more times before you ask.

[0 ](javascript:void\(0\);) [7 ](javascript:void\(0\);)

  * [#105](/thread/post/15099921#post15099921 "Post Permalink")

  * Dec 27, 2024 2:53am  Dec 27, 2024 2:53am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

+1R on Gold  
  
Did not enter on two red bars, instead entered on decreasing bullish momentum and on the 5th black dot, after a medium squeeze in the overall direction of the major trend after a small pullback. Not A+ but worked.  
  
Can probably hold and move SL. Squeeze ending and bearish momentum kicking in. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot_20241226_125303_Photos.jpg
Size: 714 KB](/attachment/image/4867879/thumbnail?d=1735235599)](/attachment/image/4867879?d=1735235599)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#106](/thread/post/15100051#post15100051 "Post Permalink")

  * Dec 27, 2024 6:30am  Dec 27, 2024 6:30am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

Observing - Highly Compressed and Bullish Momentum is decreasing in a bearish market, with a bounce off my EMA anchor.  
  
Also to note is the length of the squeeze  
  
Do we enter on red momentum bars or black dots, not even the slowest of all green dots... hmm  
  
This would surely dictate your position sizing?   
  
RR stays the same in every setup? Things I'm pondering. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot_20241226_163007_Photos.jpg
Size: 573 KB](/attachment/image/4867933/thumbnail?d=1735248637)](/attachment/image/4867933?d=1735248637)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#107](/thread/post/15100064#post15100064 "Post Permalink")

  * Dec 27, 2024 6:59am  Dec 27, 2024 6:59am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar426855_1.gif) RickM](rickm)

  * Joined Sep 2015 | Status: Trader | [2,439 Posts](/search?do=process&provider=Member&searchuser=426855)

> [Quoting driven18](/thread/post/15099713#post15099713 "View Quoted Post")
> 
> Disliked
> 
> {quote} Damn boyyy, that story almost borders on Romanticism ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)
> 
> Ignored

Just a post to lighten up this place a bit, and prove you can trade from any where if you have a edge. 

Trading thin liquidity at the boundary of the charts

[0 ](javascript:void\(0\);) [5 ](javascript:void\(0\);)

  * [#108](/thread/post/15100067#post15100067 "Post Permalink")

  * Dec 27, 2024 7:03am  Dec 27, 2024 7:03am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar272159_71.gif) driven18](driven18)

  * Joined Jul 2012 | Status: Trader | [1,385 Posts](/search?do=process&provider=Member&searchuser=272159)

> [Quoting RickM](/thread/post/15100064#post15100064 "View Quoted Post")
> 
> Disliked
> 
> {quote} Just a post to lighten up this place a bit, and prove you can trade from any where if you have a edge.
> 
> Ignored

I agree, just came back from Cabo San Lucas, paid off 4 nights 5 Stars exclusive resort with 2 days trading, while sipping Anejo tequilas. ![](https://resources.faireconomy.media/images/emojis/64/1f60e.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f37a.png?v=15.1)  
  
Wife was not excited about me trading a bit, but then was very happy with results ![](https://resources.faireconomy.media/images/emojis/64/1f600.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f600.png?v=15.1) O well, you know how the saying go's and I coined it .."I can live without trading, but why?" 

[0 ](javascript:void\(0\);) [3 ](javascript:void\(0\);)

  * [#109](/thread/post/15100073#post15100073 "Post Permalink")

  * Dec 27, 2024 7:07am  Dec 27, 2024 7:07am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

> [Quoting driven18](/thread/post/15100067#post15100067 "View Quoted Post")
> 
> Disliked
> 
> {quote} I agree, just came back from Cabo San Lucas, paid off 4 nights 5 Stars exclusive resort with 2 days trading, while sipping Anejo tequilas. ![](https://resources.faireconomy.media/images/emojis/64/1f60e.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f37a.png?v=15.1) Wife was not excited about me trading a bit, but then was very happy with results ![](https://resources.faireconomy.media/images/emojis/64/1f600.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f600.png?v=15.1)
> 
> Ignored

I could take some notes from you guys, it's all business over here 

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#110](/thread/post/15100080#post15100080 "Post Permalink")

  * Dec 27, 2024 7:25am  Dec 27, 2024 7:25am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar426855_1.gif) RickM](rickm)

  * Joined Sep 2015 | Status: Trader | [2,439 Posts](/search?do=process&provider=Member&searchuser=426855)

> [Quoting MachineLearn](/thread/post/15100051#post15100051 "View Quoted Post")
> 
> Disliked
> 
> Observing - Highly Compressed and Bullish Momentum is decreasing in a bearish market, with a bounce off my EMA anchor. Also to note is the length of the squeeze Do we enter on red momentum bars or black dots, not even the slowest of all green dots... hmm This would surely dictate your position sizing? RR stays the same in every setup? Things I'm pondering. {image}
> 
> Ignored

This is the biggest question mark, which colour dot to trade from?.  
After a few years trading with this strategy (one of a few I trade), I found the best risk reward results come from focusing on price leaving the 21 EMA with momentum on a trending market.  
  
I believe we should follow the PA signals more than which colour dot it’s presently at.  
  
This enables me to have a very very tight stop / it either works immediately or I am out for a small loss. If you trade with dots, the loss can be far larger 

Trading thin liquidity at the boundary of the charts

[0 ](javascript:void\(0\);) [9 ](javascript:void\(0\);)

  * [#111](/thread/post/15100085#post15100085 "Post Permalink")

  * Dec 27, 2024 7:32am  Dec 27, 2024 7:32am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

> [Quoting RickM](/thread/post/15100080#post15100080 "View Quoted Post")
> 
> Disliked
> 
> {quote} This is the biggest question mark, which colour dot to trade from?. After a few years trading with this strategy (one of a few I trade), I found the best risk reward results come from focusing on price leaving the 21 EMA with momentum on a trending market. I believe we should follow the PA signals more than which colour dot it’s presently at. This enables me to have a very very tight stop / it either works immediately or I am out for a small loss. If you trade with dots, the loss can be far larger
> 
> Ignored

Well said love it. This is exactly why I enjoy asking questions out loud. Really let's us hone in on what's important. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#112](/thread/post/15100087#post15100087 "Post Permalink")

  * Dec 27, 2024 7:48am  Dec 27, 2024 7:48am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar272159_71.gif) driven18](driven18)

  * Joined Jul 2012 | Status: Trader | [1,385 Posts](/search?do=process&provider=Member&searchuser=272159)

> [Quoting RickM](/thread/post/15100064#post15100064 "View Quoted Post")
> 
> Disliked
> 
> {quote} Just a post to lighten up this place a bit, and prove you can trade from any where if you have a edge.
> 
> Ignored

I just remembered I took few pics from the hotel balcony in the evening, when I traded in Cabo San Lucas...romanticism is my "middle" name ![](https://resources.faireconomy.media/images/emojis/64/1f600.png?v=15.1)

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 340 KB](/attachment/image/4867947/thumbnail?d=1735253309)](/attachment/image/4867947?d=1735253309)   
[![Click to Enlarge

Name: screenshot.png
Size: 328 KB](/attachment/image/4867948/thumbnail?d=1735253454)](/attachment/image/4867948?d=1735253454)   

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#113](/thread/post/15100088#post15100088 "Post Permalink")

  * Dec 27, 2024 7:50am  Dec 27, 2024 7:50am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar426855_1.gif) RickM](rickm)

  * Joined Sep 2015 | Status: Trader | [2,439 Posts](/search?do=process&provider=Member&searchuser=426855)

Why does the Squeeze setup work?  
  
John Carter talks about pressure being trapped inside a Squeeze with will soon act like a spring, exploding price outwards on release.  
But he is wrong here on this basic explanation.  
  
What happens is during a Squeeze period, limit orders are placed either side of compression area in high numbers by impatient traders. Generally it’s 2 to 1 selling limit orders on a bullish trend.  
Therefore the Squeeze breakout is just a liquidity run towards high imbalance of bids and asks.  
  
A bullish trend is therefore the destruction of Sellers Equity. When we add stops, we get a trend continuation of this move called stop runs which is free money if we can stay in for a period. 

Trading thin liquidity at the boundary of the charts

[0 ](javascript:void\(0\);) [3 ](javascript:void\(0\);)

  * [#114](/thread/post/15100090#post15100090 "Post Permalink")

  * Dec 27, 2024 7:52am  Dec 27, 2024 7:52am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar426855_1.gif) RickM](rickm)

  * Joined Sep 2015 | Status: Trader | [2,439 Posts](/search?do=process&provider=Member&searchuser=426855)

> [Quoting driven18](/thread/post/15100087#post15100087 "View Quoted Post")
> 
> Disliked
> 
> {quote} I just remembered I took few pics of the hotel balcony when I traded in Cabo San Lucas...romanticism is my "middle" name ![](https://resources.faireconomy.media/images/emojis/64/1f600.png?v=15.1) {image} {image}
> 
> Ignored

Nice shot, never been there yet but I will add it to my travel list 

Trading thin liquidity at the boundary of the charts

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#115](/thread/post/15100142#post15100142 "Post Permalink")

  * Edited 12:29pm  Dec 27, 2024 9:47am | Edited 12:29pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar601035_2.gif) axecap](axecap)

  * Joined Aug 2017 | Status: Trader | [2,336 Posts](/search?do=process&provider=Member&searchuser=601035)

> [Quoting RickM](/thread/post/15099129#post15099129 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi Haz Without doubt, the best session to trade is from US Open. If you can trade then, the best in order is US500 / DOW /. Nasdaq / US2000. I am based out of Australia so that time period is hard for me to trade often (US Open starts at 12.30am for me) so I normally trade 3 primary markets during the London session instead. I favour ES / Gold / Oil Futures but also watch EU & Bitcoin. Bitcoin on the One Hour Chart offers perhaps the BEST
> 
> Ignored

Hi Rick, thanks for your contribuition here. Given that you trade London session due to your location Im curious as to your thoughts on the FTSE? wouldnt that be a good option to replace US500 ?  
thanks 

its all just one persons opinion....

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#116](/thread/post/15100160#post15100160 "Post Permalink")

  * Dec 27, 2024 10:36am  Dec 27, 2024 10:36am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1781092_20.gif) LucasFX7](lucasfx7)

  * | Joined Jan 2024  | Status: Trader | [29 Posts](/search?do=process&provider=Member&searchuser=1781092) | Online Now 

Thank you everyone for all your knowledge and experiences. Here is my template and indicator for MT4. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 15 KB](/attachment/image/4867983/thumbnail?d=1735263396)](/attachment/image/4867983?d=1735263396)   

Attached File(s)

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [SQZMOM_LB_100.mq4](/attachment/file/4867984?d=1735263411) 6 KB | 261 downloads 

![File Type: tpl](https://assets.faireconomy.media/images/attach/tpl.gif) [Default.tpl](/attachment/file/4867985?d=1735263412) 2 KB | 140 downloads 

[0 ](javascript:void\(0\);) [6 ](javascript:void\(0\);)

  * [#117](/thread/post/15100162#post15100162 "Post Permalink")

  * Dec 27, 2024 10:46am  Dec 27, 2024 10:46am 

  * [ oochiwaawaa](oochiwaawaa)

  * | Membership Revoked  | Joined Dec 2023 | [796 Posts](/search?do=process&provider=Member&searchuser=1769620)

> [Quoting LucasFX7](/thread/post/15100160#post15100160 "View Quoted Post")
> 
> Disliked
> 
> Thank you everyone for all your knowledge and experiences. Here is my template and indicator for MT4. {image} {file} {file}
> 
> Ignored

  
soooo ... what now?  
  
should i take it 4 a walk ??? oooorr ??? feed it? oooorr ????  
  
am i suppose to send u money ??? or what?? 

protein for breakfast !

[1 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#118](/thread/post/15100163#post15100163 "Post Permalink")

  * Dec 27, 2024 10:47am  Dec 27, 2024 10:47am 

  * [ oochiwaawaa](oochiwaawaa)

  * | Membership Revoked  | Joined Dec 2023 | [796 Posts](/search?do=process&provider=Member&searchuser=1769620)

congratulations u have a template 

protein for breakfast !

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#119](/thread/post/15100164#post15100164 "Post Permalink")

  * Dec 27, 2024 10:48am  Dec 27, 2024 10:48am 

  * [ oochiwaawaa](oochiwaawaa)

  * | Membership Revoked  | Joined Dec 2023 | [796 Posts](/search?do=process&provider=Member&searchuser=1769620)

> [Quoting RickM](/thread/post/15100088#post15100088 "View Quoted Post")
> 
> Disliked
> 
> Why does the Squeeze setup work? John Carter talks about pressure being trapped inside a Squeeze with will soon act like a spring, exploding price outwards on release. But he is wrong here on this basic explanation. What happens is during a Squeeze period, limit orders are placed either side of compression area in high numbers by impatient traders. Generally it’s 2 to 1 selling limit orders on a bullish trend. Therefore the Squeeze breakout is just a liquidity run towards high imbalance of bids and asks. A bullish trend is therefore the destruction...
> 
> Ignored

  
prove it. i know different to u soooo .... prove it please 

protein for breakfast !

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#120](/thread/post/15100196#post15100196 "Post Permalink")

  * Dec 27, 2024 12:09pm  Dec 27, 2024 12:09pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar272159_71.gif) driven18](driven18)

  * Joined Jul 2012 | Status: Trader | [1,385 Posts](/search?do=process&provider=Member&searchuser=272159)

> [Quoting oochiwaawaa](/thread/post/15100162#post15100162 "View Quoted Post")
> 
> Disliked
> 
> {quote} soooo ... what now? should i take it 4 a walk ??? oooorr ??? feed it? oooorr ???? am i suppose to send u money ??? or what??
> 
> Ignored

**You are an IDIOT!** Get to Fuck out of here! 

[1 ](javascript:void\(0\);) [7 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Squeeze n Go | MTF System
  *   * [ **Reply to Thread** ](/thread/1319487-squeeze-n-go-mtf-system/reply#reply)

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

[Spud's MTF FIB Breakout System](/thread/30109-spuds-mtf-fib-breakout-system "Spud's MTF FIB Breakout System 
-------------------------------- 
Ever since I learned about Fibonacci numbers they have interested my pure...") 375 replies

[H1Scalper System (MTF D1,H1,M5)](/thread/166646-h1scalper-system-mtf-d1h1m5 "Here are the indicators for a manual system. 
  
Explanations, rules and trading ideas are coming... 
. 
\(2009.05.13\) 
Attached are the...") 725 replies

[MTF Trix system](/thread/183801-mtf-trix-system "Hello everybody, 
 
This thread is for developing and discussing a multi-timeframe trading system that is based on one indicator - Trix -...") 3,697 replies

[MTF Stochastics into MTF Stoch Histogram](/thread/359918-mtf-stochastics-into-mtf-stoch-histogram "Hi, 
 
I have been trading with the help of MTF Stochastics for a few weeks now with relatively good results but would appreciate if...") 8 replies

[MTF Vajioo Scalping System](/thread/195912-mtf-vajioo-scalping-system "RUBBISH") 15 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/1319487-squeeze-n-go-mtf-system/reply#reply)
  * Subscribe
  * [216](javascript:void\(0\);)

Attachments: Squeeze n Go | MTF System

Tags: Squeeze n Go | MTF System

#  [](/thread/1319487-squeeze-n-go-mtf-system)Squeeze n Go | MTF System 

  * 

  * [#121](/thread/post/15100203#post15100203 "Post Permalink")

  * Dec 27, 2024 12:23pm  Dec 27, 2024 12:23pm 

  * [ oochiwaawaa](oochiwaawaa)

  * | Membership Revoked  | Joined Dec 2023 | [796 Posts](/search?do=process&provider=Member&searchuser=1769620)

> [Quoting driven18](/thread/post/15100196#post15100196 "View Quoted Post")
> 
> Disliked
> 
> {quote} You are an IDIOT! Get to Fuck out of here!
> 
> Ignored

well well well  
  
gotta luv interneters  
  
and internet cronies  
  
whats da matter pal ?   
  
once u ppl start talkin bout anythin WORTH talkin bout THEN Ill start too ..... Ok  
  
gotta luv da internet ==== dont need any common snese BUT theres buckets o crud to be had 

protein for breakfast !

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#122](/thread/post/15100205#post15100205 "Post Permalink")

  * Dec 27, 2024 12:28pm  Dec 27, 2024 12:28pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar601035_2.gif) axecap](axecap)

  * Joined Aug 2017 | Status: Trader | [2,336 Posts](/search?do=process&provider=Member&searchuser=601035)

> [Quoting driven18](/thread/post/15100196#post15100196 "View Quoted Post")
> 
> Disliked
> 
> {quote} You are an IDIOT! Get to Fuck out of here!
> 
> Ignored

Peter Caleb.... the drunken australian.... membership revoked....keeps reappearing.  
OP needs to block him 

its all just one persons opinion....

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#123](/thread/post/15100211#post15100211 "Post Permalink")

  * Dec 27, 2024 12:36pm  Dec 27, 2024 12:36pm 

  * [ oochiwaawaa](oochiwaawaa)

  * | Membership Revoked  | Joined Dec 2023 | [796 Posts](/search?do=process&provider=Member&searchuser=1769620)

> [Quoting axecap](/thread/post/15100205#post15100205 "View Quoted Post")
> 
> Disliked
> 
> {quote} Peter Caleb.... the drunken australian.... membership revoked....keeps reappearing. OP needs to block him
> 
> Ignored

  
ooooo  
  
so sorry to interrupt your virtual reality experience  
  
do u want fries with that?  
  
or maybe a labotomy ?  
  
ya know ..... just to help ya get more comfy ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f60e.png?v=15.1)

protein for breakfast !

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#124](/thread/post/15100223#post15100223 "Post Permalink")

  * Dec 27, 2024 12:50pm  Dec 27, 2024 12:50pm 

  * [ oochiwaawaa](oochiwaawaa)

  * | Membership Revoked  | Joined Dec 2023 | [796 Posts](/search?do=process&provider=Member&searchuser=1769620)

weeeeell ya gotta admit ==== what im talkin bout is way more entertaining!!!!   
  
da stuff u ppl talk bout is soooooooooooooooooooooooo borin !! so uneventful, sooooooo last century !!! so redundant, so outta synch with reality.  
  
and DEFINITELY less funny ![](https://resources.faireconomy.media/images/emojis/64/1f605.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f605.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f605.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f605.png?v=15.1)

protein for breakfast !

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#125](/thread/post/15100235#post15100235 "Post Permalink")

  * Dec 27, 2024 1:21pm  Dec 27, 2024 1:21pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

annnnd he's gone.. 

[0 ](javascript:void\(0\);) [6 ](javascript:void\(0\);)

  * [#126](/thread/post/15100248#post15100248 "Post Permalink")

  * Dec 27, 2024 1:41pm  Dec 27, 2024 1:41pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar588299_3.gif) RiskFighter](riskfighter)

  * Joined Jun 2017 | Status: Trader | [1,566 Posts](/search?do=process&provider=Member&searchuser=588299) | Online Now 

This is my Watchlist template:  
When a trade is entered, I change to template II. 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 64 KB](/attachment/image/4868036/thumbnail?d=1735274451)](/attachment/image/4868036?d=1735274451)   
[![Click to Enlarge

Name: screenshot.png
Size: 26 KB](/attachment/image/4868038/thumbnail?d=1735274513)](/attachment/image/4868038?d=1735274513)   

Read post #1 !! Then read it again 10 more times before you ask.

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#127](/thread/post/15100447#post15100447 "Post Permalink")

  * Dec 27, 2024 5:33pm  Dec 27, 2024 5:33pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar426855_1.gif) RickM](rickm)

  * Joined Sep 2015 | Status: Trader | [2,439 Posts](/search?do=process&provider=Member&searchuser=426855)

> [Quoting axecap](/thread/post/15100142#post15100142 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi Rick, thanks for your contribuition here. Given that you trade London session due to your location Im curious as to your thoughts on the FTSE? wouldnt that be a good option to replace US500 ? thanks
> 
> Ignored

I do trade the DAX at times and I find it better.   
However the US indices do offer nice trends from around Frankfurt open for around 4 hours which I trade every day.  
I double the size (or add when in profit soon up) knowing there’s often just one good setup during the London session. The secret is to get out regardless after 5 hours (yes there can be nice long trends but just slow) because your’e get cut up till the New York session starts.  
Therefore I would trade ES or NQ as my primary London Session markets while keeping away from the DOW during this time as it’s liquidity is terrible.   
I have 3 primary markets I trade which I map on higher time frames - ES. Gold, Oil  
On another screen watch screen A I list the DOW, Bitcoin, Russel DAX, EURUSD Futures.   
Forex markets watch screen B I list the 5 US pairs, EURJPY, GBPJPY and a few commodities.  
  
Still it’s better to be a master of a few that try and trade the latest hot market 

Trading thin liquidity at the boundary of the charts

[0 ](javascript:void\(0\);) [7 ](javascript:void\(0\);)

  * [#128](/thread/post/15100459#post15100459 "Post Permalink")

  * Dec 27, 2024 5:45pm  Dec 27, 2024 5:45pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar601035_2.gif) axecap](axecap)

  * Joined Aug 2017 | Status: Trader | [2,336 Posts](/search?do=process&provider=Member&searchuser=601035)

> [Quoting RickM](/thread/post/15100447#post15100447 "View Quoted Post")
> 
> Disliked
> 
> {quote} I do trade the DAX at times and I find it better.
> 
> Ignored

Thanks for the detailed response. Much appreciated 

its all just one persons opinion....

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#129](/thread/post/15100539#post15100539 "Post Permalink")

  * Dec 27, 2024 7:51pm  Dec 27, 2024 7:51pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar588299_3.gif) RiskFighter](riskfighter)

  * Joined Jun 2017 | Status: Trader | [1,566 Posts](/search?do=process&provider=Member&searchuser=588299) | Online Now 

Watching on M15. Those small periodes of ranging occurs, but seems to short to really give a valid setup. Then try th siotuation on a shorter TF. In this example it was a fine setup on M5 which I missed because M15 seemed to light. 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 31 KB](/attachment/image/4868175/thumbnail?d=1735296650)](/attachment/image/4868175?d=1735296650)   
[![Click to Enlarge

Name: screenshot.png
Size: 30 KB](/attachment/image/4868177/thumbnail?d=1735296690)](/attachment/image/4868177?d=1735296690)   

Read post #1 !! Then read it again 10 more times before you ask.

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#130](/thread/post/15100553#post15100553 "Post Permalink")

  * Dec 27, 2024 8:05pm  Dec 27, 2024 8:05pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar426855_1.gif) RickM](rickm)

  * Joined Sep 2015 | Status: Trader | [2,439 Posts](/search?do=process&provider=Member&searchuser=426855)

“Most traders take a good system and destroy it by trying to make it into a perfect system.” - Robert Prechter  
  
I'll put my hand up and claim I've done that too many times.

Trading thin liquidity at the boundary of the charts

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#131](/thread/post/15100577#post15100577 "Post Permalink")

  * Dec 27, 2024 8:53pm  Dec 27, 2024 8:53pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1897355_6.gif) vmd108](vmd108)

  * | Joined Jun 2024  | Status: Trader | [39 Posts](/search?do=process&provider=Member&searchuser=1897355)

Hi Machine Learn!  
  
You first got me interested in the squeeze when you mentioned it in another thread I follow. Good that you started your own thread on that.  
  
I'm curious about your experience with **Squeeze Momentum Indicator** by **LazyBear**  
([https://www.tradingview.com/script/n...ator-LazyBear/](https://www.tradingview.com/script/nqQ1DT5a-Squeeze-Momentum-Indicator-LazyBear/))  
  
It's currently the most popular indicator on TradingView (90,000+ likes).  
  
I've never been able to figure out how to actually use it.  
  
What is your, or anyone else's, opinion on this and why BB and KC works better in your method? 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#132](/thread/post/15100743#post15100743 "Post Permalink")

  * Dec 27, 2024 11:21pm  Dec 27, 2024 11:21pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar272159_71.gif) driven18](driven18)

  * Joined Jul 2012 | Status: Trader | [1,385 Posts](/search?do=process&provider=Member&searchuser=272159)

2 Min Dow Futures now, Blue Dots - squeeze. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 15 KB](/attachment/image/4868277/thumbnail?d=1735309271)](/attachment/image/4868277?d=1735309271)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#133](/thread/post/15100799#post15100799 "Post Permalink")

  * Dec 28, 2024 12:03am  Dec 28, 2024 12:03am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

> [Quoting vmd108](/thread/post/15100577#post15100577 "View Quoted Post")
> 
> Disliked
> 
> Hi Machine Learn! You first got me interested in the squeeze when you mentioned it in another thread I follow. Good that you started your own thread on that. I'm curious about your experience with Squeeze Momentum Indicator by LazyBear ([https://www.tradingview.com/script/n...ator-LazyBear/](https://www.tradingview.com/script/nqQ1DT5a-Squeeze-Momentum-Indicator-LazyBear/)) It's currently the most popular indicator on TradingView (90,000+ likes). I've never been able to figure out how to actually use it. What is your, or anyone else's, opinion on this and why BB and KC works better in your method?...
> 
> Ignored

What's up vmd...It's basically the exact same thing. I would recommend loading up the one from the first page just to avoid confusion for yourself 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#134](/thread/post/15100805#post15100805 "Post Permalink")

  * Edited 12:59am  Dec 28, 2024 12:09am | Edited 12:59am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar272159_71.gif) driven18](driven18)

  * Joined Jul 2012 | Status: Trader | [1,385 Posts](/search?do=process&provider=Member&searchuser=272159)

> [Quoting axecap](/thread/post/15100205#post15100205 "View Quoted Post")
> 
> Disliked
> 
> {quote} Peter Caleb.... the drunken australian.... membership revoked....keeps reappearing. OP needs to block him
> 
> Ignored

I think his Mindfulness finally went to MindFuck..a bit sad for that person, but trading is definitely for **strongminded** humans. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 38 KB](/attachment/image/4868316/thumbnail?d=1735312149)](/attachment/image/4868316?d=1735312149)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#135](/thread/post/15100855#post15100855 "Post Permalink")

  * Dec 28, 2024 1:05am  Dec 28, 2024 1:05am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar588299_3.gif) RiskFighter](riskfighter)

  * Joined Jun 2017 | Status: Trader | [1,566 Posts](/search?do=process&provider=Member&searchuser=588299) | Online Now 

he he . what can I say? We were told that best trading time is NY session. I was sleeping.  
  
Maybe one should not watch US30, US100 and US500 at the same time - eh! 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 41 KB](/attachment/image/4868341/thumbnail?d=1735315511)](/attachment/image/4868341?d=1735315511)   

Read post #1 !! Then read it again 10 more times before you ask.

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#136](/thread/post/15101162#post15101162 "Post Permalink")

  * Dec 28, 2024 8:47pm  Dec 28, 2024 8:47pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar588299_3.gif) RiskFighter](riskfighter)

  * Joined Jun 2017 | Status: Trader | [1,566 Posts](/search?do=process&provider=Member&searchuser=588299) | Online Now 

I promissed to make an alarm to the MT4 Squeeze indicator. Well, it's done. But as it is Saturday I cannot test it.   
  
I will test it Monday and release if it works as intended. 

Read post #1 !! Then read it again 10 more times before you ask.

[0 ](javascript:void\(0\);) [3 ](javascript:void\(0\);)

  * [#137](/thread/post/15101369#post15101369 "Post Permalink")

  * Dec 29, 2024 1:45pm  Dec 29, 2024 1:45pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1172533_7.gif) FocusWinReal](focuswinreal)

  * | Joined Jul 2021  | Status: Trader | [676 Posts](/search?do=process&provider=Member&searchuser=1172533)

> [Quoting RickM](/thread/post/15098440#post15098440 "View Quoted Post")
> 
> Disliked
> 
> FOREX TRADERS When I trade the Squeeze on Forex Markets, I find this setup the best. Generally Forex Markets produce many fake outs so I find it best to trade with a EMA Trend Ribbon (EMA 21 - 34 -55 -89). Most trades I take are on H1 or M5 but I always see what the Daily chart is doing. Using the TTM Squeeze Pro (Tradingview), trade the breakout of RED DOTS (BB inside Keltner Channel) to black dots if the momentum indicator agrees. Below is EURJPY on H1. Here we are only looking for Bearish signals and the take profit signal is when the Momentum...
> 
> Ignored

Hi Rick, could you elaborate on what you see as the main benefit of using the trend ribbon in addition to the 21 ema? I find the more ema's the more my mind goes walkabout. But, 1 ema and it's like focus without distraction.  
  
Thanks for the recent input on the threads.   
Cheers... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#138](/thread/post/15101436#post15101436 "Post Permalink")

  * Dec 29, 2024 7:42pm  Dec 29, 2024 7:42pm 

  * [ roanfox](roanfox)

  * | Joined Dec 2022  | Status: Trader | [96 Posts](/search?do=process&provider=Member&searchuser=1562325)

> [Quoting RiskFighter](/thread/post/15101162#post15101162 "View Quoted Post")
> 
> Disliked
> 
> I promissed to make an alarm to the MT4 Squeeze indicator. Well, it's done. But as it is Saturday I cannot test it. I will test it Monday and release if it works as intended.
> 
> Ignored

Hey Risk, thanks a lot for the Squeeze indicator, the alarm will be a nice addition. Sorry to impose on you like this, but is there any way of adding a button to hide/show the indicator? If its too much to ask dont worry about it 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#139](/thread/post/15101444#post15101444 "Post Permalink")

  * Dec 29, 2024 8:07pm  Dec 29, 2024 8:07pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar588299_3.gif) RiskFighter](riskfighter)

  * Joined Jun 2017 | Status: Trader | [1,566 Posts](/search?do=process&provider=Member&searchuser=588299) | Online Now 

> [Quoting roanfox](/thread/post/15101436#post15101436 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hey Risk, thanks a lot for the Squeeze indicator, the alarm will be a nice addition. Sorry to impose on you like this, but is there any way of adding a button to hide/show the indicator? If its too much to ask dont worry about it
> 
> Ignored

I am working on such a button.  
  
And I am working another smart thing for you guys. Might be released on Monday too. 

Read post #1 !! Then read it again 10 more times before you ask.

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#140](/thread/post/15101445#post15101445 "Post Permalink")

  * Dec 29, 2024 8:10pm  Dec 29, 2024 8:10pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar588299_3.gif) RiskFighter](riskfighter)

  * Joined Jun 2017 | Status: Trader | [1,566 Posts](/search?do=process&provider=Member&searchuser=588299) | Online Now 

> [Quoting FocusWinReal](/thread/post/15101369#post15101369 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi Rick, could you elaborate on what you see as the main benefit of using the trend ribbon in addition to the 21 ema? I find the more ema's the more my mind goes walkabout. But, 1 ema and it's like focus without distraction. Thanks for the recent input on the threads. Cheers...
> 
> Ignored

My take is 2 things. 1 - At least one more EA makes it easier to see in a glance if the chart is trending. 2 - You can use two of the other EMA's to serve as exit/Bounce areas. 

Read post #1 !! Then read it again 10 more times before you ask.

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Squeeze n Go | MTF System
  *   * [ **Reply to Thread** ](/thread/1319487-squeeze-n-go-mtf-system/reply#reply)

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

[Spud's MTF FIB Breakout System](/thread/30109-spuds-mtf-fib-breakout-system "Spud's MTF FIB Breakout System 
-------------------------------- 
Ever since I learned about Fibonacci numbers they have interested my pure...") 375 replies

[H1Scalper System (MTF D1,H1,M5)](/thread/166646-h1scalper-system-mtf-d1h1m5 "Here are the indicators for a manual system. 
  
Explanations, rules and trading ideas are coming... 
. 
\(2009.05.13\) 
Attached are the...") 725 replies

[MTF Trix system](/thread/183801-mtf-trix-system "Hello everybody, 
 
This thread is for developing and discussing a multi-timeframe trading system that is based on one indicator - Trix -...") 3,697 replies

[MTF Stochastics into MTF Stoch Histogram](/thread/359918-mtf-stochastics-into-mtf-stoch-histogram "Hi, 
 
I have been trading with the help of MTF Stochastics for a few weeks now with relatively good results but would appreciate if...") 8 replies

[MTF Vajioo Scalping System](/thread/195912-mtf-vajioo-scalping-system "RUBBISH") 15 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/1319487-squeeze-n-go-mtf-system/reply#reply)
  * Subscribe
  * [216](javascript:void\(0\);)

Attachments: Squeeze n Go | MTF System

Tags: Squeeze n Go | MTF System

#  [](/thread/1319487-squeeze-n-go-mtf-system)Squeeze n Go | MTF System 

  * 

  * [#141](/thread/post/15101449#post15101449 "Post Permalink")

  * Dec 29, 2024 8:18pm  Dec 29, 2024 8:18pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar426855_1.gif) RickM](rickm)

  * Joined Sep 2015 | Status: Trader | [2,439 Posts](/search?do=process&provider=Member&searchuser=426855)

> [Quoting RiskFighter](/thread/post/15101444#post15101444 "View Quoted Post")
> 
> Disliked
> 
> {quote} I am working on such a button. And I am working another smart thing for you guys. Might be released on Monday too.
> 
> Ignored

Nice work Risky, good to have a Coder on board. 

Trading thin liquidity at the boundary of the charts

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#142](/thread/post/15101455#post15101455 "Post Permalink")

  * Dec 29, 2024 8:30pm  Dec 29, 2024 8:30pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar588299_3.gif) RiskFighter](riskfighter)

  * Joined Jun 2017 | Status: Trader | [1,566 Posts](/search?do=process&provider=Member&searchuser=588299) | Online Now 

> [Quoting RickM](/thread/post/15101449#post15101449 "View Quoted Post")
> 
> Disliked
> 
> {quote} Nice work Risky, good to have a Coder on board.
> 
> Ignored

Thank you. It is nice to know if you are welcome. Sometime coders are not. 

Read post #1 !! Then read it again 10 more times before you ask.

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#143](/thread/post/15101457#post15101457 "Post Permalink")

  * Dec 29, 2024 8:48pm  Dec 29, 2024 8:48pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar426855_1.gif) RickM](rickm)

  * Joined Sep 2015 | Status: Trader | [2,439 Posts](/search?do=process&provider=Member&searchuser=426855)

> [Quoting FocusWinReal](/thread/post/15101369#post15101369 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi Rick, could you elaborate on what you see as the main benefit of using the trend ribbon in addition to the 21 ema? I find the more ema's the more my mind goes walkabout. But, 1 ema and it's like focus without distraction. Thanks for the recent input on the threads. Cheers...
> 
> Ignored

Hi Focus  
  
You could use the 89EMA as your Bias and the 21EMA as a signal to trade provided there is momentum away from the EMA.  
Forex Markets produce a lot of false breakouts so having a Bias helps for these markets.  
  
Then you need to develop a rating for every Squeeze setup you see - A+. B. C  
Don't trade C setups, just trade A+ & B group Squeeze setups to obtain consistently.  
  
Facts are with any Strategy, there is a 48% chance you could lose 7 trades in a row, therefore cut the losers quick and risk letting the winners run & run  
If I run into a sequence of 3 or more losing trades in a row, I will only trade A+ setups till I get back in the swing. 

Trading thin liquidity at the boundary of the charts

[0 ](javascript:void\(0\);) [8 ](javascript:void\(0\);)

  * [#144](/thread/post/15101569#post15101569 "Post Permalink")

  * Dec 30, 2024 2:30am  Dec 30, 2024 2:30am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1172533_7.gif) FocusWinReal](focuswinreal)

  * | Joined Jul 2021  | Status: Trader | [676 Posts](/search?do=process&provider=Member&searchuser=1172533)

> [Quoting RickM](/thread/post/15101457#post15101457 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi Focus You could use the 89EMA as your Bias and the 21EMA as a signal to trade provided there is momentum away from the EMA. Forex Markets produce a lot of false breakouts so having a Bias helps for these markets. Then you need to develop a rating for every Squeeze setup you see - A+. B. C Don't trade C setups, just trade A+ & B group Squeeze setups to obtain consistently. Facts are with any Strategy, there is a 48% chance you could lose 7 trades in a row, therefore cut the losers quick and risk letting the winners run & run If I run into...
> 
> Ignored

Thanks Rick, that makes sense.   
  
@RiskFighter, thanks also.  
It's late I'll comment further later.  
  
Cheers... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#145](/thread/post/15101582#post15101582 "Post Permalink")

  * Dec 30, 2024 3:48am  Dec 30, 2024 3:48am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

![](https://resources.faireconomy.media/images/emojis/64/1f9d0.png?v=15.1)   

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot_20241229_134817_Photos.jpg
Size: 367 KB](/attachment/image/4868825/thumbnail?d=1735498113)](/attachment/image/4868825?d=1735498113)   

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#146](/thread/post/15101610#post15101610 "Post Permalink")

  * Dec 30, 2024 5:19am  Dec 30, 2024 5:19am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar601035_2.gif) axecap](axecap)

  * Joined Aug 2017 | Status: Trader | [2,336 Posts](/search?do=process&provider=Member&searchuser=601035)

> [Quoting MachineLearn](/thread/post/15101582#post15101582 "View Quoted Post")
> 
> Disliked
> 
> ![](https://resources.faireconomy.media/images/emojis/64/1f9d0.png?v=15.1) {image}
> 
> Ignored

hi Machine, any particular reason you trade BTC tether rather than BTCUSD. Thanks 

its all just one persons opinion....

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#147](/thread/post/15101616#post15101616 "Post Permalink")

  * Edited 6:54am  Dec 30, 2024 6:00am | Edited 6:54am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar272159_71.gif) driven18](driven18)

  * Joined Jul 2012 | Status: Trader | [1,385 Posts](/search?do=process&provider=Member&searchuser=272159)

Here is demo equity line trading 1 Min Dow Futures for this week, no trading on December 24th and 25th, using squeeze strategy at 50% of the rules and my personal flavors of Money Management.  
  
Point is, we all trade differently, for me, I see the relevance to investigate it **further.**

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 16 KB](/attachment/image/4868860/thumbnail?d=1735506000)](/attachment/image/4868860?d=1735506000)   

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#148](/thread/post/15101644#post15101644 "Post Permalink")

  * Dec 30, 2024 7:38am  Dec 30, 2024 7:38am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar426855_1.gif) RickM](rickm)

  * Joined Sep 2015 | Status: Trader | [2,439 Posts](/search?do=process&provider=Member&searchuser=426855)

> [Quoting driven18](/thread/post/15101616#post15101616 "View Quoted Post")
> 
> Disliked
> 
> Here is demo equity line trading 1 Min Dow Futures for this week, no trading on December 24th and 25th, using squeeze strategy at 50% of the rules and my personal flavors of Money Management. Point is, we all trade differently, for me, I see the relevance to investigate it further. {image}
> 
> Ignored

Hi Driven  
  
What I see happen in real usage of this system is you get a week full of multiple wins in a row creating great growth curve followed by a few days of negative equity decline pretty much as your graph showed.  
The reason for the negative growth is normally a trading pair has moved into consolidation on the Daily chart resulting in the trader getting chopped up.  
Therefore it’s a good idea to check the Daily and Weekly charts and avoid pairs that are range bound.  
That why trading with a EMA ribbon can also help because your taking the second breakout of consolidation period which increase the chance of a profitable trade. 

Trading thin liquidity at the boundary of the charts

[0 ](javascript:void\(0\);) [6 ](javascript:void\(0\);)

  * [#149](/thread/post/15101653#post15101653 "Post Permalink")

  * Edited 9:32am  Dec 30, 2024 7:57am | Edited 9:32am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar272159_71.gif) driven18](driven18)

  * Joined Jul 2012 | Status: Trader | [1,385 Posts](/search?do=process&provider=Member&searchuser=272159)

"That why trading with a EMA ribbon can also help because your taking the second breakout of consolidation period which increase the chance of a profitable trade"  
  
I agree with above statement from RickM.  
  
Yes, it is ranging/chopping and then trending. It happened to be a good trending week at the end...the main point is to keep losses at a minimum when ranging and that is a science on its own.  
  
When understanding Money Management correctly, there is no need to look at any other timeframes, then the current one, as none of us has a clue what the next trade will do, regardless of higher timeframes. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#150](/thread/post/15101681#post15101681 "Post Permalink")

  * Edited 11:17am  Dec 30, 2024 9:46am | Edited 11:17am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar426855_1.gif) RickM](rickm)

  * Joined Sep 2015 | Status: Trader | [2,439 Posts](/search?do=process&provider=Member&searchuser=426855)

Hi Driven  
  
I agree with most of the stuff you write, however feel multi time frame analyst is still important.  
  
Looking at EURUSD on the Daily chart, we can see price is caught within a range set by a candle on Wednesday 18th. This was a high volume day as well so I wouldn't be trading any low timeframe Squeeze's till that range is broken.  
  
What is a A++ setup ?  
  
Breakout Squeeze on the Daily, H1 & M5 at the same time = $$$$$$$$$$$ 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: EU trap.png
Size: 168 KB](/attachment/image/4868905/thumbnail?d=1735519563)](/attachment/image/4868905?d=1735519563)   
[![Click to Enlarge

Name: eu day day.png
Size: 174 KB](/attachment/image/4868927/thumbnail?d=1735525045)](/attachment/image/4868927?d=1735525045)   

Trading thin liquidity at the boundary of the charts

[0 ](javascript:void\(0\);) [7 ](javascript:void\(0\);)

  * [#151](/thread/post/15101684#post15101684 "Post Permalink")

  * Edited 4:30pm  Dec 30, 2024 10:02am | Edited 4:30pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar588299_3.gif) RiskFighter](riskfighter)

  * Joined Jun 2017 | Status: Trader | [1,566 Posts](/search?do=process&provider=Member&searchuser=588299) | Online Now 

This is next version of the Squeeze indicator. It now can give an alarm on screen and on your phone.  
  
The robot test if the Keltner channels move outside of the Bollinger Channels. This is always a sign of a squeeze. At the moment when both K-channels again are inside the BB-Channels, then the indicator sends the alarm. The robot works on bar close only. Remember to put the 21EMA on the chart. The robot does not print that.  
  
NOTE: This is not a sign to enter a trade. There are rules of this strategy to follow. And not all squeezes leads to a setup.  
NOTE: There are many fine squeezes where K does not get inside BB. So if you lay all your eggs in this indicator, then you will miss some setups.  
  
We have been talking about a button that should hide the indicator. Problem is, that the indicator not only works on the BB and K indicator. I have coded it to actually draw theese indicators also. This to be sure that the indi works on the right set of settings on BB and K. SO - if I hide the indicator, then the screen will be all empty.  
  
I am handling it like this. When I want the indi to find me some nice squeezes, then I have a template for that. If I don't then I have another template containing the strategy setup including the EMA ribbon. 

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [SqueezeBBK_4.ex4](/attachment/file/4868930?d=1735525429) 14 KB | 703 downloads 

Read post #1 !! Then read it again 10 more times before you ask.

[0 ](javascript:void\(0\);) [7 ](javascript:void\(0\);)

  * [#152](/thread/post/15101691#post15101691 "Post Permalink")

  * Edited Dec 31, 2024 7:24am  Dec 30, 2024 10:13am | Edited Dec 31, 2024 7:24am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar588299_3.gif) RiskFighter](riskfighter)

  * Joined Jun 2017 | Status: Trader | [1,566 Posts](/search?do=process&provider=Member&searchuser=588299) | Online Now 

I made a little christmas present for you guys.  
  
I am often in a situation where I have time to follow the screen and start a trade. But I do not have the ability to stay at the screen to follow it. So I thought it would be nice with a stand in. So I made an exit robot.  
  
You can use a SuperTrend exit or an EMA exit after your choice. Could be one of the EMA's in the ribbon.  
  
I use to colour the chart background if I have a trade on that instrument. This way I have a nice overview if I trade say 8 FF pairs. This is why there are some colour settings. If you don't want this function, then you must set all the colours to your chosen background colour.  
  
Note you are using it at your own responsibility. If it does not exit as it should, it is your problem. And always use it on demo.  
Note that you might not always be satisfied with the exit. The bar maybe crossed the Exit EMA and then went back on track.  
Note that it works on bar close only. Meaning a spike does not trigger an exit.  
  
Will I make a trade robot, that can enter trades. No, don't ask. This is a manual strategy. A trading robot will not work.  
  
**EDIT: This robot works correct only when you trade ONE portion of an instrument. If you add on so that you pocess more than one trade of the instrument, then the exit robot will close only one portion at the end of a bar. There are technical reasons for this.**

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [ExitRobot_1.ex4](/attachment/file/4868909?d=1735521109) 12 KB | 95 downloads 

Read post #1 !! Then read it again 10 more times before you ask.

[0 ](javascript:void\(0\);) [4 ](javascript:void\(0\);)

  * [#153](/thread/post/15101714#post15101714 "Post Permalink")

  * Dec 30, 2024 11:21am  Dec 30, 2024 11:21am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar272159_71.gif) driven18](driven18)

  * Joined Jul 2012 | Status: Trader | [1,385 Posts](/search?do=process&provider=Member&searchuser=272159)

> [Quoting RiskFighter](/thread/post/15101691#post15101691 "View Quoted Post")
> 
> Disliked
> 
> I made a little christmas present for you guys. I am often in a situation where I have time to follow the screen and start a trade. But I do not have the ability to stay at the screen to follow it. So I thought it would be nice with a stand in. So I made an exit robot. You can use a SuperTrend exit or an EMA exit after your choice. Could be one of the EMA's in the ribbon. I use to colour the chart background if I have a trade on that instrument. This way I have a nice overview if I trade say 8 FF pairs. This is why there are some colour settings....
> 
> Ignored

Thanks for doing this for people....too bad you do not code in MT5.  
  
MT5 is ment for creating robust ea's/robots. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#154](/thread/post/15101723#post15101723 "Post Permalink")

  * Edited Dec 31, 2024 12:28am  Dec 30, 2024 11:32am | Edited Dec 31, 2024 12:28am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar272159_71.gif) driven18](driven18)

  * Joined Jul 2012 | Status: Trader | [1,385 Posts](/search?do=process&provider=Member&searchuser=272159)

> [Quoting RickM](/thread/post/15101681#post15101681 "View Quoted Post")
> 
> Disliked
> 
> Hi Driven I agree with most of the stuff you write, however feel multi time frame analyst is still important. Looking at EURUSD on the Daily chart, we can see price is caught within a range set by a candle on Wednesday 18th. This was a **high volume day** as well so I wouldn't be trading any **low timeframe Squeeze's till that range is broken.** What is a A++ setup ? Breakout Squeeze on the**Daily, H1 & M5 at the same time = **$$$$$$$$$$$ {image} {image}
> 
> Ignored

TMI (in bold) and distraction(for me), but  
  
RickM, as we say in Australia, mate ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1): 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 17 KB](/attachment/image/4868936/thumbnail?d=1735525974)](/attachment/image/4868936?d=1735525974)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#155](/thread/post/15101826#post15101826 "Post Permalink")

  * Dec 30, 2024 2:33pm  Dec 30, 2024 2:33pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1172533_7.gif) FocusWinReal](focuswinreal)

  * | Joined Jul 2021  | Status: Trader | [676 Posts](/search?do=process&provider=Member&searchuser=1172533)

> [Quoting RickM](/thread/post/15101681#post15101681 "View Quoted Post")
> 
> Disliked
> 
> Hi Driven I agree with most of the stuff you write, however feel multi time frame analyst is still important. Looking at EURUSD on the Daily chart, we can see price is caught within a range set by a candle on Wednesday 18th. This was a high volume day as well so I wouldn't be trading any low timeframe Squeeze's till that range is broken. What is a A++ setup ? Breakout Squeeze on the Daily, H1 & M5 at the same time = $$$$$$$$$$$ {image} {image}
> 
> Ignored

I agree Rick, the daily at least should be out of a range for any A setups to appear. I guess for me to not use a ribbon is to only wait for the much bigger timeframes to be in movement so as to only have a lower timeframe bias and trigger ema. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#156](/thread/post/15102138#post15102138 "Post Permalink")

  * Edited 9:54pm  Dec 30, 2024 9:38pm | Edited 9:54pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar272159_71.gif) driven18](driven18)

  * Joined Jul 2012 | Status: Trader | [1,385 Posts](/search?do=process&provider=Member&searchuser=272159)

Here is my first live trade with the squeeze(not shown as I use different inputs) on 1 Min Dow Futures under the 21 EMA(yellow) ribbon  
  
2nd image - closed that trade for + 91 points. 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 3 KB](/attachment/image/4869226/thumbnail?d=1735562348)](/attachment/image/4869226?d=1735562348)   
[![Click to Enlarge

Name: screenshot.png
Size: 4 KB](/attachment/image/4869229/thumbnail?d=1735562533)](/attachment/image/4869229?d=1735562533)   

[0 ](javascript:void\(0\);) [6 ](javascript:void\(0\);)

  * [#157](/thread/post/15102264#post15102264 "Post Permalink")

  * Dec 30, 2024 11:33pm  Dec 30, 2024 11:33pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot_20241230_093333_Photos.jpg
Size: 471 KB](/attachment/image/4869317/thumbnail?d=1735569234)](/attachment/image/4869317?d=1735569234)   

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#158](/thread/post/15102321#post15102321 "Post Permalink")

  * Dec 31, 2024 12:08am  Dec 31, 2024 12:08am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

> [Quoting MachineLearn](/thread/post/15102264#post15102264 "View Quoted Post")
> 
> Disliked
> 
> {image}
> 
> Ignored

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot_20241230_100803_Photos.jpg
Size: 494 KB](/attachment/image/4869354/thumbnail?d=1735571304)](/attachment/image/4869354?d=1735571304)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#159](/thread/post/15102430#post15102430 "Post Permalink")

  * Dec 31, 2024 1:52am  Dec 31, 2024 1:52am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar272159_71.gif) driven18](driven18)

  * Joined Jul 2012 | Status: Trader | [1,385 Posts](/search?do=process&provider=Member&searchuser=272159)

My latest live trades, notice how 2 trades, with direction of 21 EMA worked out to full TP.  
  
I am done for 2024 and wish everyone a Happy and Healthy and Lucky New Year! Cheers to everyone around the world(including the playa haters),  
I am outta here ![](https://resources.faireconomy.media/images/emojis/64/1f600.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f37a.png?v=15.1)

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 17 KB](/attachment/image/4869440/thumbnail?d=1735577661)](/attachment/image/4869440?d=1735577661)   

[0 ](javascript:void\(0\);) [8 ](javascript:void\(0\);)

  * [#160](/thread/post/15102443#post15102443 "Post Permalink")

  * Dec 31, 2024 2:00am  Dec 31, 2024 2:00am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

> [Quoting driven18](/thread/post/15102430#post15102430 "View Quoted Post")
> 
> Disliked
> 
> My latest live trades, notice how 2 trades, with direction of 21 EMA worked out to full TP. I am done for 2024 and wish everyone a Happy and Healthy and Lucky New Year! Cheers to everyone around the world(including the playa haters), I am outta here ![](https://resources.faireconomy.media/images/emojis/64/1f600.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f37a.png?v=15.1) {image}
> 
> Ignored

Beautiful! ![](https://resources.faireconomy.media/images/emojis/64/1f942.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Squeeze n Go | MTF System
  *   * [ **Reply to Thread** ](/thread/1319487-squeeze-n-go-mtf-system/reply#reply)

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

[Spud's MTF FIB Breakout System](/thread/30109-spuds-mtf-fib-breakout-system "Spud's MTF FIB Breakout System 
-------------------------------- 
Ever since I learned about Fibonacci numbers they have interested my pure...") 375 replies

[H1Scalper System (MTF D1,H1,M5)](/thread/166646-h1scalper-system-mtf-d1h1m5 "Here are the indicators for a manual system. 
  
Explanations, rules and trading ideas are coming... 
. 
\(2009.05.13\) 
Attached are the...") 725 replies

[MTF Trix system](/thread/183801-mtf-trix-system "Hello everybody, 
 
This thread is for developing and discussing a multi-timeframe trading system that is based on one indicator - Trix -...") 3,697 replies

[MTF Stochastics into MTF Stoch Histogram](/thread/359918-mtf-stochastics-into-mtf-stoch-histogram "Hi, 
 
I have been trading with the help of MTF Stochastics for a few weeks now with relatively good results but would appreciate if...") 8 replies

[MTF Vajioo Scalping System](/thread/195912-mtf-vajioo-scalping-system "RUBBISH") 15 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/1319487-squeeze-n-go-mtf-system/reply#reply)
  * Subscribe
  * [216](javascript:void\(0\);)

Attachments: Squeeze n Go | MTF System

Tags: Squeeze n Go | MTF System

#  [](/thread/1319487-squeeze-n-go-mtf-system)Squeeze n Go | MTF System 

  * 

  * [#161](/thread/post/15102517#post15102517 "Post Permalink")

  * Dec 31, 2024 3:55am  Dec 31, 2024 3:55am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

**GBPCHF**  
  
CHF pairs are in a lengthy high compression squeeze on H1 while respecting the 21, keep an eye out  
  
Looking for a breakout from the 21 with good momentum on the TTSP indicator 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot_20241230_135503_Photos.jpg
Size: 375 KB](/attachment/image/4869487/thumbnail?d=1735584938)](/attachment/image/4869487?d=1735584938)   

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#162](/thread/post/15102642#post15102642 "Post Permalink")

  * Dec 31, 2024 8:53am  Dec 31, 2024 8:53am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar426855_1.gif) RickM](rickm)

  * Joined Sep 2015 | Status: Trader | [2,439 Posts](/search?do=process&provider=Member&searchuser=426855)

> [Quoting driven18](/thread/post/15102430#post15102430 "View Quoted Post")
> 
> Disliked
> 
> My latest live trades, notice how 2 trades, with direction of 21 EMA worked out to full TP. I am done for 2024 and wish everyone a Happy and Healthy and Lucky New Year! Cheers to everyone around the world(including the playa haters), I am outta here ![](https://resources.faireconomy.media/images/emojis/64/1f600.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f37a.png?v=15.1) {image}
> 
> Ignored

Nice trade Driven  
  
The 21EMA is the prefect entry and exit tool for most setups. 

Trading thin liquidity at the boundary of the charts

[0 ](javascript:void\(0\);) [5 ](javascript:void\(0\);)

  * [#163](/thread/post/15102760#post15102760 "Post Permalink")

  * Dec 31, 2024 2:02pm  Dec 31, 2024 2:02pm 

  * [ ChelseaR](chelsear)

  * | Joined Dec 2024  | Status: Trader | [64 Posts](/search?do=process&provider=Member&searchuser=2001129)

> [Quoting FocusWinReal](/thread/post/15101826#post15101826 "View Quoted Post")
> 
> Disliked
> 
> {quote} I agree Rick, the daily at least should be out of a range for any A setups to appear. I guess for me to not use a ribbon is to only wait for the much bigger timeframes to be in movement so as to only have a lower timeframe bias and trigger ema.
> 
> Ignored

Do you find that using the lower timeframe bias with the trigger EMA improves your entry accuracy, or do you sometimes miss opportunities by waiting too long? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#164](/thread/post/15102994#post15102994 "Post Permalink")

  * Dec 31, 2024 8:34pm  Dec 31, 2024 8:34pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar426855_1.gif) RickM](rickm)

  * Joined Sep 2015 | Status: Trader | [2,439 Posts](/search?do=process&provider=Member&searchuser=426855)

> [Quoting RiskFighter](/thread/post/15101684#post15101684 "View Quoted Post")
> 
> Disliked
> 
> This is next version of the Squeeze indicator. It now can give an alarm on screen and on your phone. The robot test if the Keltner channels move outside of the Bollinger Channels. This is always a sign of a squeeze. At the moment when both K-channels again are inside the BB-Channels, then the indicator sends the alarm. The robot works on bar close only. Remember to put the 21EMA on the chart. The robot does not print that. NOTE: This is not a sign to enter a trade. There are rules of this strategy to follow. And not all squeezes leads to a setup....
> 
> Ignored

Hi Risk  
  
I am looking forward to running some tests with your EA’s soon. As an ex - coder, I know how many hours it can take (time wasted away from family and friends) to get a decent final product finished even to a workable version. I can’t run them on an Apple Laptop but will test them when back at my trading den in a few weeks time. Cracking work. 

Trading thin liquidity at the boundary of the charts

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#165](/thread/post/15103015#post15103015 "Post Permalink")

  * Dec 31, 2024 9:16pm  Dec 31, 2024 9:16pm 

  * [ TableTop](tabletop)

  * | Joined Apr 2021  | Status: Trader | [95 Posts](/search?do=process&provider=Member&searchuser=1086359)

> [Quoting RiskFighter](/thread/post/15100539#post15100539 "View Quoted Post")
> 
> Disliked
> 
> Watching on M15. Those small periodes of ranging occurs, but seems to short to really give a valid setup. Then try th siotuation on a shorter TF. In this example it was a fine setup on M5 which I missed because M15 seemed to light.
> 
> Ignored

Great indicator. Here is an example with just showing the squeeze bars for Gold on M1. This highlights the timing of a squeeze on lower timeframes.  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 22 KB](/attachment/image/4869872/thumbnail?d=1735647122)](/attachment/image/4869872?d=1735647122)   

  
  
We can see the 50 pip box form prior to the NY session, with a 15 minute squeeze at the previous week high, and breakout at 1530 (0830 NY). The day high is put in on another 15 minute rotation, giving a 150 pip move to trade.   
  
It's a nice clean indicator. 

[0 ](javascript:void\(0\);) [3 ](javascript:void\(0\);)

  * [#166](/thread/post/15103134#post15103134 "Post Permalink")

  * Dec 31, 2024 11:41pm  Dec 31, 2024 11:41pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar588299_3.gif) RiskFighter](riskfighter)

  * Joined Jun 2017 | Status: Trader | [1,566 Posts](/search?do=process&provider=Member&searchuser=588299) | Online Now 

Thanks guys for kind words.  
  
We must also remember that the strategy is from Machine and Rick. Thank you for sharing.  
  
And a happy New Year to all. 

Read post #1 !! Then read it again 10 more times before you ask.

[0 ](javascript:void\(0\);) [3 ](javascript:void\(0\);)

  * [#167](/thread/post/15103496#post15103496 "Post Permalink")

  * Jan 1, 2025 12:40pm  Jan 1, 2025 12:40pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1172533_7.gif) FocusWinReal](focuswinreal)

  * | Joined Jul 2021  | Status: Trader | [676 Posts](/search?do=process&provider=Member&searchuser=1172533)

> [Quoting ChelseaR](/thread/post/15102760#post15102760 "View Quoted Post")
> 
> Disliked
> 
> {quote} Do you find that using the lower timeframe bias with the trigger EMA improves your entry accuracy, or do you sometimes miss opportunities by waiting too long?
> 
> Ignored

My experience of trading (not so much this method because I stumbled on it recently after reading a few of RickM's posts) is that we are always too late or too early for entering trades. Point is: there is never a perfect entry (perhaps the odd one) and in hindsight what might appear to be late is not and what might appear to be early is also not. And then there are the bad entries that go against you. For this method I like what the OP and the participants are posting.   
  
Cheers... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#168](/thread/post/15103603#post15103603 "Post Permalink")

  * Jan 1, 2025 11:22pm  Jan 1, 2025 11:22pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar175961_3.gif) heispark](heispark)

  * Joined Apr 2011 | Status: Hoc Etiam Transibit.... | [5,429 Posts](/search?do=process&provider=Member&searchuser=175961)

> [Quoting RickM](/thread/post/15102994#post15102994 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi Risk I am looking forward to running some tests with your EA’s soon. As an ex - coder, I know how many hours it can take (time wasted away from family and friends) to get a decent final product finished even to a workable version. I can’t run them on an Apple Laptop but will test them when back at my trading den in a few weeks time. Cracking work.
> 
> Ignored

Hi, Rick  
Just curious, why do you want to spend your time seeking and playing other systems or strategies if you already have a profitable strategy? To find stronger one?  
Have Happy New Year anyway.  
![](https://resources.faireconomy.media/images/emojis/64/263a-fe0f.png?v=15.1)

Simplicity is the ultimate sophistication - Leonardo da Vinci

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#169](/thread/post/15103605#post15103605 "Post Permalink")

  * Jan 1, 2025 11:35pm  Jan 1, 2025 11:35pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar175961_3.gif) heispark](heispark)

  * Joined Apr 2011 | Status: Hoc Etiam Transibit.... | [5,429 Posts](/search?do=process&provider=Member&searchuser=175961)

It will gonna be brutally chopped up during choppy conditions like other breakout strategies I believe......... Nothing new. 

Simplicity is the ultimate sophistication - Leonardo da Vinci

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#170](/thread/post/15103607#post15103607 "Post Permalink")

  * Jan 1, 2025 11:50pm  Jan 1, 2025 11:50pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar115754_4.gif) rover99x](rover99x)

  * | Joined Sep 2009  | Status: Trader | [542 Posts](/search?do=process&provider=Member&searchuser=115754)

Oh John Carter's Squeeze method:-  
I used to use this some years ago, and I never managed to get it to work in any meaningful way, it just uses a contraction in prices waiting for the inevitable explosion of price in one direction, or so what John Carter would have you believe. The difficulty is you get many fake-outs, which make this method no better than say, a Bollinger Band or Kelter Channel. John Carter is a well versed personality who makes a fortune from teaching people how to trade, just don't bother.....  
  
It's just easier to trade what you think the direction of travail will be. Simples 

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#171](/thread/post/15103669#post15103669 "Post Permalink")

  * Jan 2, 2025 3:38am  Jan 2, 2025 3:38am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar588299_3.gif) RiskFighter](riskfighter)

  * Joined Jun 2017 | Status: Trader | [1,566 Posts](/search?do=process&provider=Member&searchuser=588299) | Online Now 

> [Quoting heispark](/thread/post/15103603#post15103603 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi, Rick Just curious, why do you want to spend your time seeking and playing other systems or strategies if you already have a profitable strategy? To find stronger one? Have Happy New Year anyway. ![](https://resources.faireconomy.media/images/emojis/64/263a-fe0f.png?v=15.1)
> 
> Ignored

This IS his strategy. Or part of it. BB inside the Keltner shows a Squeeze, and that is what Rick is trading (One of his tools of cause). So this is not another system. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 110 KB](/attachment/image/4870346/thumbnail?d=1735756651)](/attachment/image/4870346?d=1735756651)   

Read post #1 !! Then read it again 10 more times before you ask.

[0 ](javascript:void\(0\);) [3 ](javascript:void\(0\);)

  * [#172](/thread/post/15103682#post15103682 "Post Permalink")

  * Jan 2, 2025 4:40am  Jan 2, 2025 4:40am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar379731_1.gif) rockypoint](rockypoint)

  * Joined Aug 2014 | Status: Trader | [4,260 Posts](/search?do=process&provider=Member&searchuser=379731)

> [Quoting heispark](/thread/post/15103605#post15103605 "View Quoted Post")
> 
> Disliked
> 
> It will gonna be brutally chopped up during choppy conditions like other breakout strategies I believe......... Nothing new.
> 
> Ignored

You just change the way you trade it, ranging choppy markets you look for smaller wins and get the hell out if it starts to turn against you. Or if PA is super bad you just don't trade. I've used this off an on over the years always made money with it, trade a variation of it now. Except I just use BB's you can pretty much tell when there's a squeeze and when PA ranges just use BB expansions to look for trades. 

[0 ](javascript:void\(0\);) [5 ](javascript:void\(0\);)

  * [#173](/thread/post/15103708#post15103708 "Post Permalink")

  * Jan 2, 2025 6:51am  Jan 2, 2025 6:51am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar272159_71.gif) driven18](driven18)

  * Joined Jul 2012 | Status: Trader | [1,385 Posts](/search?do=process&provider=Member&searchuser=272159)

> [Quoting heispark](/thread/post/15103605#post15103605 "View Quoted Post")
> 
> Disliked
> 
> It will gonna be brutally chopped up during choppy conditions like other breakout strategies I believe......... Nothing new.
> 
> Ignored

No one has any clue, if it will be a chop or trending market, next second from now.  
  
**5% of the people who are successful and trade real live money understand this, that one must take every trade based on the trading plan regardless chop or not in the present trade.**  
  
Skill lies in the Money Management, not to lose more than planned during chop and to take next trade, hoping for the better, "trending" condition.  
  
Money Management trumps over any unplanned losses(speaking on this subject). 

[0 ](javascript:void\(0\);) [4 ](javascript:void\(0\);)

  * [#174](/thread/post/15103713#post15103713 "Post Permalink")

  * Jan 2, 2025 7:04am  Jan 2, 2025 7:04am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar175961_3.gif) heispark](heispark)

  * Joined Apr 2011 | Status: Hoc Etiam Transibit.... | [5,429 Posts](/search?do=process&provider=Member&searchuser=175961)

> [Quoting RiskFighter](/thread/post/15103669#post15103669 "View Quoted Post")
> 
> Disliked
> 
> {quote} This IS his strategy. Or part of it. BB inside the Keltner shows a Squeeze, and that is what Rick is trading (One of his tools of cause). So this is not another system. {image}
> 
> Ignored

I don't think so. Last time I heard he was using volume delta and some other volume related stuff....... 

Simplicity is the ultimate sophistication - Leonardo da Vinci

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#175](/thread/post/15103730#post15103730 "Post Permalink")

  * Jan 2, 2025 8:09am  Jan 2, 2025 8:09am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar379731_1.gif) rockypoint](rockypoint)

  * Joined Aug 2014 | Status: Trader | [4,260 Posts](/search?do=process&provider=Member&searchuser=379731)

> [Quoting heispark](/thread/post/15103713#post15103713 "View Quoted Post")
> 
> Disliked
> 
> {quote} I don't think so. Last time I heard he was using volume delta and some other volume related stuff.......
> 
> Ignored

He uses a few different systems including this one. See post 150. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#176](/thread/post/15103743#post15103743 "Post Permalink")

  * Jan 2, 2025 8:52am  Jan 2, 2025 8:52am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar426855_1.gif) RickM](rickm)

  * Joined Sep 2015 | Status: Trader | [2,439 Posts](/search?do=process&provider=Member&searchuser=426855)

> [Quoting rover99x](/thread/post/15103607#post15103607 "View Quoted Post")
> 
> Disliked
> 
> Oh John Carter's Squeeze method:- I used to use this some years ago, and I never managed to get it to work in any meaningful way, it just uses a contraction in prices waiting for the inevitable explosion of price in one direction, or so what John Carter would have you believe. The difficulty is you get many fake-outs, which make this method no better than say, a Bollinger Band or Kelter Channel. John Carter is a well versed personality who makes a fortune from teaching people how to trade, just don't bother..... It's just easier to trade what you...
> 
> Ignored

Hi Rover99  
  
I am in agreement with you if you focus on just trading the breakout when the Bollinger Bands expands back outside the Keltner Channel, you will get cut up all day.  
To make this "idea work", do what most successful traders of this system do which is focus on breakouts from the 21 EMA once a trend has been established or looks likely. This way if the breakout fails, you are either still in profit or occur a tiny loss.  
The real way to profit from this strategy is to take trades mainly shortly after Frankfurt or New York open as these are the squeezes that work best.  
  
Cheers 

Trading thin liquidity at the boundary of the charts

[0 ](javascript:void\(0\);) [4 ](javascript:void\(0\);)

  * [#177](/thread/post/15103758#post15103758 "Post Permalink")

  * Jan 2, 2025 9:19am  Jan 2, 2025 9:19am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar426855_1.gif) RickM](rickm)

  * Joined Sep 2015 | Status: Trader | [2,439 Posts](/search?do=process&provider=Member&searchuser=426855)

> [Quoting heispark](/thread/post/15103713#post15103713 "View Quoted Post")
> 
> Disliked
> 
> {quote} I don't think so. Last time I heard he was using volume delta and some other volume related stuff.......
> 
> Ignored

Hi Heispark  
  
I still use volume strategy's which is why the Squeeze set up works best on Stocks & Futures.  
What is a true breakout?  
  
That is when we see a Bid/ Ask imbalance of 3 to 1 that's supported by strong bursts of volume as seen on a DOM. Typically this occurs over a 2-3 minute period in 15-30 second bursts. Without this activity, its a fake move generally but you can get those unexplainable moves during low volume periods.  
  
Therefore I trade the squeeze mostly on Futures (ES/NQ/Gold/Oil) on the 2 minute chart with aid of a DOM. Been doing that for Futures for a few years now and more on Stocks. Because this forum is more Forex based, I keep the Volume Jargon out of the discussion as its still profitable without it.  
  
I don't trade the way John Carter does nor have any association with him or his education company, never even visited his site.  
  
  
PS. I show the standard charts I use on here when I trade Forex Markets often, my Futures Setup is different. 

Trading thin liquidity at the boundary of the charts

[0 ](javascript:void\(0\);) [5 ](javascript:void\(0\);)

  * [#178](/thread/post/15104768#post15104768 "Post Permalink")

  * Jan 3, 2025 9:40am  Jan 3, 2025 9:40am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar426855_1.gif) RickM](rickm)

  * Joined Sep 2015 | Status: Trader | [2,439 Posts](/search?do=process&provider=Member&searchuser=426855)

First trade of the year for me on Gold  
  
Trading the Range breakout of the Aussie Open on Gold with Squeeze setup 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Gold A.png
Size: 137 KB](/attachment/image/4871109/thumbnail?d=1735864839)](/attachment/image/4871109?d=1735864839)   

Trading thin liquidity at the boundary of the charts

[0 ](javascript:void\(0\);) [9 ](javascript:void\(0\);)

  * [#179](/thread/post/15105440#post15105440 "Post Permalink")

  * Edited 11:44pm  Jan 3, 2025 11:29pm | Edited 11:44pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar272159_71.gif) driven18](driven18)

  * Joined Jul 2012 | Status: Trader | [1,385 Posts](/search?do=process&provider=Member&searchuser=272159)

Dow Futures 1 Min TF, Real Live Trade(open charts for better visuals)..will be taking profits soon..  
  
And here you go(second image) **+125 - Done for the Day** ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f37a.png?v=15.1)

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 24 KB](/attachment/image/4871490/thumbnail?d=1735914549)](/attachment/image/4871490?d=1735914549)   
[![Click to Enlarge

Name: screenshot.png
Size: 20 KB](/attachment/image/4871496/thumbnail?d=1735914808)](/attachment/image/4871496?d=1735914808)   

[0 ](javascript:void\(0\);) [3 ](javascript:void\(0\);)

  * [#180](/thread/post/15105450#post15105450 "Post Permalink")

  * Edited Jan 4, 2025 7:38pm  Jan 3, 2025 11:36pm | Edited Jan 4, 2025 7:38pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar588299_3.gif) RiskFighter](riskfighter)

  * Joined Jun 2017 | Status: Trader | [1,566 Posts](/search?do=process&provider=Member&searchuser=588299) | Online Now 

Here is my latest tool. It shows the Keltner Squeeze status at timeframes M1 to D. It is the blue tool at the top of the chart.  
  
It updates every minute. But it shows the status at the latest close of bar at the different timeframes. So the M1 can change often and the D might have a squeeze for days.  
  
I am normaly a robot coder and making a new robot is done very fast. Making an indicator is hard and I have worked days on this. And I am not satisfied. I would like the blue boxes to be able to place at any spot at the chart. I know it can be done, but that must be later.  
  
Otherwise I think it is working and it will be a nice tool to have.  
  
On the chart I have both my Squeeze tools.  
  
Again - this is Keltner squeezes, there will be squeeze setups that are not catched by this Keltner tool.  
  
Enjoy. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 38 KB](/attachment/image/4871489/thumbnail?d=1735914453)](/attachment/image/4871489?d=1735914453)   

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [SqueezeBBK_4.ex4](/attachment/file/4871506?d=1735914985) 14 KB | 179 downloads 

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [SqueezeBBK_mtf_1.ex4](/attachment/file/4871858?d=1735987097) 14 KB | 155 downloads 

Read post #1 !! Then read it again 10 more times before you ask.

[0 ](javascript:void\(0\);) [4 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Squeeze n Go | MTF System
  *   * [ **Reply to Thread** ](/thread/1319487-squeeze-n-go-mtf-system/reply#reply)

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

[Spud's MTF FIB Breakout System](/thread/30109-spuds-mtf-fib-breakout-system "Spud's MTF FIB Breakout System 
-------------------------------- 
Ever since I learned about Fibonacci numbers they have interested my pure...") 375 replies

[H1Scalper System (MTF D1,H1,M5)](/thread/166646-h1scalper-system-mtf-d1h1m5 "Here are the indicators for a manual system. 
  
Explanations, rules and trading ideas are coming... 
. 
\(2009.05.13\) 
Attached are the...") 725 replies

[MTF Trix system](/thread/183801-mtf-trix-system "Hello everybody, 
 
This thread is for developing and discussing a multi-timeframe trading system that is based on one indicator - Trix -...") 3,697 replies

[MTF Stochastics into MTF Stoch Histogram](/thread/359918-mtf-stochastics-into-mtf-stoch-histogram "Hi, 
 
I have been trading with the help of MTF Stochastics for a few weeks now with relatively good results but would appreciate if...") 8 replies

[MTF Vajioo Scalping System](/thread/195912-mtf-vajioo-scalping-system "RUBBISH") 15 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/1319487-squeeze-n-go-mtf-system/reply#reply)
  * Subscribe
  * [216](javascript:void\(0\);)

Attachments: Squeeze n Go | MTF System

Tags: Squeeze n Go | MTF System

#  [](/thread/1319487-squeeze-n-go-mtf-system)Squeeze n Go | MTF System 

  * 

  * [#181](/thread/post/15105459#post15105459 "Post Permalink")

  * Edited Jan 4, 2025 12:05am  Jan 3, 2025 11:42pm | Edited Jan 4, 2025 12:05am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar272159_71.gif) driven18](driven18)

  * Joined Jul 2012 | Status: Trader | [1,385 Posts](/search?do=process&provider=Member&searchuser=272159)

Hard work and nice tools RiskFighter, now one can see what timeframe Squeeze occurring.  
  
However, I do not recommend looking at other Squeeze time frames to trade on current timeframe. Squeeze on current time frame, whatever time frame you trade is more powerful and much less TMI when it comes to Money Management and MindFuck(Fear and Greed). Simple is the best. 1+1=2. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#182](/thread/post/15105566#post15105566 "Post Permalink")

  * Jan 4, 2025 12:34am  Jan 4, 2025 12:34am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot_20250103_103322_Photos.jpg
Size: 332 KB](/attachment/image/4871576/thumbnail?d=1735918419)](/attachment/image/4871576?d=1735918419)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#183](/thread/post/15105574#post15105574 "Post Permalink")

  * Jan 4, 2025 12:38am  Jan 4, 2025 12:38am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar588299_3.gif) RiskFighter](riskfighter)

  * Joined Jun 2017 | Status: Trader | [1,566 Posts](/search?do=process&provider=Member&searchuser=588299) | Online Now 

> [Quoting driven18](/thread/post/15105459#post15105459 "View Quoted Post")
> 
> Disliked
> 
> Hard work and nice tools RiskFighter, now one can see what timeframe Squeeze occurring. However, I do not recommend looking at other Squeeze time frames to trade on current timeframe. Squeeze on current time frame, whatever time frame you trade is more powerful and much less TMI when it comes to Money Management and MindFuck(Fear and Greed). Simple is the best. 1+1=2.
> 
> Ignored

The idea is that you may not trade lover TF if you have a Squeeze at higher TF. Because the squeeze on higher TF indicates ranging conditions.  
  
On the other hand, if the squeeze at HTF turns into a nice breakout, then you have nice conditions on lower TF. This is what Rick calls an A+ setup. Until I get aquainted with this strategy, I will search the A+ setups 

Read post #1 !! Then read it again 10 more times before you ask.

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#184](/thread/post/15105586#post15105586 "Post Permalink")

  * Edited 1:00am  Jan 4, 2025 12:46am | Edited 1:00am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar588299_3.gif) RiskFighter](riskfighter)

  * Joined Jun 2017 | Status: Trader | [1,566 Posts](/search?do=process&provider=Member&searchuser=588299) | Online Now 

It is a mantra of mine, that it is important to know when charts are ranging. It can be hard to identify. My mtf Squeeze tool can be helpful. So this can be important when playing the Squeeze strategy from Machin / RickM, but it can in general help to identify ranging markets.  
  
Watch this EURJPY. Squeeze on four timeframes. Don't touch it. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 33 KB](/attachment/image/4871583/thumbnail?d=1735919206)](/attachment/image/4871583?d=1735919206)   

Read post #1 !! Then read it again 10 more times before you ask.

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#185](/thread/post/15105600#post15105600 "Post Permalink")

  * Edited 1:31am  Jan 4, 2025 12:55am | Edited 1:31am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar272159_71.gif) driven18](driven18)

  * Joined Jul 2012 | Status: Trader | [1,385 Posts](/search?do=process&provider=Member&searchuser=272159)

A little bit of the rant below(giving back to Machine and to FF community), but Mr. Market welcomed me nicely into 2025 ![](https://resources.faireconomy.media/images/emojis/64/1f600.png?v=15.1)  
  
I do not really care for A+ or B+ or whatever the grade set up is. Entry mostly is irrelevant and I pay **only 10% of my attention** to it.  
  
Fact, that PA is above/below 21 EMA and breaking out after squeeze on present TF is enough.  
  
**Money Management (40%) and controlling your MindFuck(Fear and Greed) (50%) is where it's at.**  
  
95% of traders look for perfect entries, 5% of successful traders pay attention to other 90%.  
  
Here are 2 trades over 2 days for 275 points that were taken with the technique similar to this one...2nd trade is in this thread on the images above.  
  
[https://www.forexfactory.com/thread/...0#post15105440](https://www.forexfactory.com/thread/post/15105440#post15105440)  
  
I am showing how they looked on Hourly TFs to display 2 days..did not care for grading the setups. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 9 KB](/attachment/image/4871590/thumbnail?d=1735920017)](/attachment/image/4871590?d=1735920017)   

[0 ](javascript:void\(0\);) [6 ](javascript:void\(0\);)

  * [#186](/thread/post/15105649#post15105649 "Post Permalink")

  * Jan 4, 2025 1:37am  Jan 4, 2025 1:37am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

> [Quoting driven18](/thread/post/15105600#post15105600 "View Quoted Post")
> 
> Disliked
> 
> A little bit of the rant below(giving back to Machine and to FF community), but Mr. Market welcomed me nicely into 2025 ![](https://resources.faireconomy.media/images/emojis/64/1f600.png?v=15.1) I do not really care for A+ or B+ or whatever the grade set up is. Entry mostly is irrelevant and I pay only 10% of my attention to it. Fact, that PA is above/below 21 EMA and breaking out after squeeze on present TF is enough. Money Management (40%) and controlling your MindFuck(Fear and Greed) (50%) is where it's at. 95% of traders look for perfect entries, 5% of successful traders pay attention to other 90%. Here...
> 
> Ignored

Fear and greed are two of the most powerful emotions that influence decision-making in trading, and understanding how they affect behavior is critical for long-term success. Here's why they play such an important role:   
  
Fear often arises when a trader experiences losses or perceives risk in the market. It can lead to hesitation, premature exits, or avoiding trades altogether, even when opportunities align with their strategy. Fear of missing out (FOMO) can also push traders into impulsive decisions.  
Greed manifests as the desire to maximize profits. It can cause traders to hold positions too long, ignore their exit strategy, or over-leverage, leading to significant losses when the market reverses.  
  
Risk Management  
Both fear and greed interfere with disciplined risk management:  
\- Greed may push traders to risk more than they should, violating stop-loss limits or increasing position sizes beyond their plan. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#187](/thread/post/15105804#post15105804 "Post Permalink")

  * Jan 4, 2025 6:52am  Jan 4, 2025 6:52am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar601035_2.gif) axecap](axecap)

  * Joined Aug 2017 | Status: Trader | [2,336 Posts](/search?do=process&provider=Member&searchuser=601035)

BTCUSD M30.  
  
Moving away from EMA21 at the right time after the squeeze.  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 22 KB](/attachment/image/4871727/thumbnail?d=1735941119)](/attachment/image/4871727?d=1735941119)   

its all just one persons opinion....

[0 ](javascript:void\(0\);) [3 ](javascript:void\(0\);)

  * [#188](/thread/post/15105841#post15105841 "Post Permalink")

  * Jan 4, 2025 9:45am  Jan 4, 2025 9:45am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar426855_1.gif) RickM](rickm)

  * Joined Sep 2015 | Status: Trader | [2,439 Posts](/search?do=process&provider=Member&searchuser=426855)

> [Quoting axecap](/thread/post/15105804#post15105804 "View Quoted Post")
> 
> Disliked
> 
> BTCUSD M30. Moving away from EMA21 at the right time after the squeeze. {image}
> 
> Ignored

Hi axecap  
  
That's the best setup I believe.  
Trends Bullish, take the bullish breakout from the 21EMA when there is nice momentum.  
  
A winning Strategy because its simple. 

Trading thin liquidity at the boundary of the charts

[0 ](javascript:void\(0\);) [5 ](javascript:void\(0\);)

  * [#189](/thread/post/15106884#post15106884 "Post Permalink")

  * Jan 6, 2025 7:26pm  Jan 6, 2025 7:26pm 

  * [ roanfox](roanfox)

  * | Joined Dec 2022  | Status: Trader | [96 Posts](/search?do=process&provider=Member&searchuser=1562325)

Easy enough bounce off the 21 in the 1 min (entry was on the yellow circle, sorry for not showing precise entry but I do my trading on Ctrader and use MT4 mostly for charting as sometimes it gets too slow and fucks up some of my trades), price was already coming out of a squeeze, and in higher timeframes price has bullish momentum, closed after 15 min candle closed (overlay is 15 min candle) 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 17 KB](/attachment/image/4872537/thumbnail?d=1736159081)](/attachment/image/4872537?d=1736159081)   

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#190](/thread/post/15107150#post15107150 "Post Permalink")

  * Jan 6, 2025 10:17pm  Jan 6, 2025 10:17pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar588299_3.gif) RiskFighter](riskfighter)

  * Joined Jun 2017 | Status: Trader | [1,566 Posts](/search?do=process&provider=Member&searchuser=588299) | Online Now 

Today we had a mtf squeeze on USDJPY. WOW! This is M15. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 45 KB](/attachment/image/4872699/thumbnail?d=1736169406)](/attachment/image/4872699?d=1736169406)   

Read post #1 !! Then read it again 10 more times before you ask.

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#191](/thread/post/15107626#post15107626 "Post Permalink")

  * Jan 7, 2025 6:40am  Jan 7, 2025 6:40am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1967050_1.gif) Ju4ara](ju4ara)

  * | Joined Oct 2024  | Status: Trader | [105 Posts](/search?do=process&provider=Member&searchuser=1967050)

Hi, would you recommend to enter after squeeze in such situation, and if yes, then which candle would be better to enter?  
Thanks. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: IMG_1698.png
Size: 109 KB](/attachment/image/4872981/thumbnail?d=1736199588)](/attachment/image/4872981?d=1736199588)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#192](/thread/post/15108029#post15108029 "Post Permalink")

  * Jan 7, 2025 5:28pm  Jan 7, 2025 5:28pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar426855_1.gif) RickM](rickm)

  * Joined Sep 2015 | Status: Trader | [2,439 Posts](/search?do=process&provider=Member&searchuser=426855)

> [Quoting Ju4ara](/thread/post/15107626#post15107626 "View Quoted Post")
> 
> Disliked
> 
> Hi, would you recommend to enter after squeeze in such situation, and if yes, then which candle would be better to enter? Thanks. {image}
> 
> Ignored

Hi Ju4ara  
  
In my experience of trading this system, the best signal is obtained from trading a breakout from the 21EMA WHILE the Squeeze is still showing Red circles. Otherwise, if we wait for the green circles to show as our signal - the main move may already be over.   
Therefore I would have taken that bigger bearish candle just before the black circle appeared.   
I would want price to stay on the bearish side of the 21EMA or I would exit immediately for a very small loss.   
The idea is we are looking for a setup that gives us some big runners ideally, not a hand full of small pip winners. 

Trading thin liquidity at the boundary of the charts

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#193](/thread/post/15108247#post15108247 "Post Permalink")

  * Jan 7, 2025 9:11pm  Jan 7, 2025 9:11pm 

  * [ Merka](merka)

  * Joined Jan 2016 | Status: Trader | [1,944 Posts](/search?do=process&provider=Member&searchuser=440568)

> [Quoting RickM](/thread/post/15108029#post15108029 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi Ju4ara In my experience of trading this system, the best signal is obtained from trading a breakout from the 21EMA WHILE the Squeeze is still showing Red circles. Otherwise, if we wait for the green circles to show as our signal - the main move may already be over. Therefore I would have taken that bigger bearish candle just before the black circle appeared. I would want price to stay on the bearish side of the 21EMA or I would exit immediately for a very small loss. The idea is we are looking for a setup that gives us some big runners...
> 
> Ignored

@RickM  
What do you do if price retrace back to 21 EMA? You exit the trade. ok  
what happens, after above, if the trade resumes to the bearish side again?  
Do you re-enter again?  
or only the first signal is worth taking?  
  
cheers 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#194](/thread/post/15108373#post15108373 "Post Permalink")

  * Jan 7, 2025 10:37pm  Jan 7, 2025 10:37pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar426855_1.gif) RickM](rickm)

  * Joined Sep 2015 | Status: Trader | [2,439 Posts](/search?do=process&provider=Member&searchuser=426855)

> [Quoting Merka](/thread/post/15108247#post15108247 "View Quoted Post")
> 
> Disliked
> 
> {quote} @RickM What do you do if price retrace back to 21 EMA? You exit the trade. ok what happens, after above, if the trade resumes to the bearish side again? Do you re-enter again? or only the first signal is worth taking? cheers
> 
> Ignored

Hi Merka  
  
Most good A+ setups just keep trending so if price retraces, I'll consider exiting if it breaks the 21EMA.   
I want the trade to work perfectly on entry without delay generally or it's probably not ready to move yet. I am happy to cut it quickly and try again soon after if the setup appears again. Nothing wrong with taking 3 attempts to get on a trend provide the losses are tiny and you let the breakout run some distance when it does move hard.   
I took 4 failed long trades in a row on BTC in November before I nailed the real move from 77K up to 89K.   
  
Cheers 

Trading thin liquidity at the boundary of the charts

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#195](/thread/post/15108420#post15108420 "Post Permalink")

  * Jan 7, 2025 11:04pm  Jan 7, 2025 11:04pm 

  * [ Merka](merka)

  * Joined Jan 2016 | Status: Trader | [1,944 Posts](/search?do=process&provider=Member&searchuser=440568)

> [Quoting RickM](/thread/post/15108373#post15108373 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi Merka Most good A+ setups just keep trending so if price retraces, I'll consider exiting if it breaks the 21EMA. I want the trade to work perfectly on entry without delay generally or it's probably not ready to move yet. I am happy to cut it quickly and try again soon after if the setup appears again. Nothing wrong with taking 3 attempts to get on a trend provide the losses are tiny and you let the breakout run some distance when it does move hard. I took 4 failed long trades in a row on BTC in November before I nailed the real move from...
> 
> Ignored

Thanks for clarifying.  
Sometimes I find, when price retrace back to EMA21, the squeeze is over and need to wait for the next squeeze setup.  
  
Would be nice if you could share the timing on chart for those 4 attempts for study purpose.  
Guess will benefit the community on how to apply this strategy  
  
Thanks 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#196](/thread/post/15108429#post15108429 "Post Permalink")

  * Edited 11:53pm  Jan 7, 2025 11:11pm | Edited 11:53pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar272159_71.gif) driven18](driven18)

  * Joined Jul 2012 | Status: Trader | [1,385 Posts](/search?do=process&provider=Member&searchuser=272159)

> [Quoting RickM](/thread/post/15108373#post15108373 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi Merka Most good A+ setups just keep trending so if price retraces, I'll consider exiting if it breaks the 21EMA. I want the trade to work perfectly on entry without delay generally or it's probably not ready to move yet. I am happy to cut it quickly and try again soon after if the setup appears again. **Nothing wrong with taking 3 attempts to get on a trend provide** the losses are tiny and you let the breakout run some distance when it does move hard. I took 4 failed long trades in a row on BTC in November before I nailed the real...
> 
> Ignored

I agree, in fact one of my buddies(Cryptosurf), one of the very few(RickM included) that I respect on FF, probes multiple times before following up with trending position.  
  
I, on the other hand, maybe a bit late into the entry and do not probe, but then keep with position and trail it, as it moves my way or use predetermined Stop Loss to exit. 

[0 ](javascript:void\(0\);) [5 ](javascript:void\(0\);)

  * [#197](/thread/post/15108498#post15108498 "Post Permalink")

  * Jan 7, 2025 11:54pm  Jan 7, 2025 11:54pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar272159_71.gif) driven18](driven18)

  * Joined Jul 2012 | Status: Trader | [1,385 Posts](/search?do=process&provider=Member&searchuser=272159)

> [Quoting driven18](/thread/post/15108429#post15108429 "View Quoted Post")
> 
> Disliked
> 
> {quote} I agree, in fact one of my buddies(Cryptosurf), one of the very few(RickM included) that I respect on FF, probes multiple times before following up with trending position. I, on the other hand, maybe a bit late into the entry and do not probe, but then keep with position and trail it, as it moves my way or use predetermined Stop Loss to exit.
> 
> Ignored

I also at times, to get a better entry, get on at limit Buy/Sell, after signs that trend started. 

[0 ](javascript:void\(0\);) [4 ](javascript:void\(0\);)

  * [#198](/thread/post/15108925#post15108925 "Post Permalink")

  * Jan 8, 2025 6:26am  Jan 8, 2025 6:26am 

  * [ pakeha](pakeha)

  * | Joined Sep 2011  | Status: Trader | [435 Posts](/search?do=process&provider=Member&searchuser=193174)

First post on this thread  
  
I am looking at an approach using RSI (15) as confirmation. The example here is BTC on the daily chart.   
  
Trend: All EMAs pointing up for long trades and down for short trades.   
Entry: shown as a green vertical line... usually on the red or black dots while the Squeeze is still on + noticeable price movement away from the EMA 21 + RSI(15) confirmation breaks above 60, or below 40  
Exit: this is the challenging part... John Carter mentions that the average move is 6 candles regardless of timeframe, so this is what I have used in this example.... the exit is shown as a blue vertical line. This works really well for quick moves, but not as well for longer up/down moves, as with BTC in November 2024.   
  
Comments welcome 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 167 KB](/attachment/image/4873778/thumbnail?d=1736285080)](/attachment/image/4873778?d=1736285080)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#199](/thread/post/15109013#post15109013 "Post Permalink")

  * Jan 8, 2025 9:16am  Jan 8, 2025 9:16am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar426855_1.gif) RickM](rickm)

  * Joined Sep 2015 | Status: Trader | [2,439 Posts](/search?do=process&provider=Member&searchuser=426855)

> [Quoting pakeha](/thread/post/15108925#post15108925 "View Quoted Post")
> 
> Disliked
> 
> First post on this thread I am looking at an approach using RSI (15) as confirmation. The example here is BTC on the daily chart. Trend: All EMAs pointing up for long trades and down for short trades. Entry: shown as a green vertical line... usually on the red or black dots while the Squeeze is still on + noticeable price movement away from the EMA 21 + RSI(15) confirmation breaks above 60, or below 40 Exit: this is the challenging part... John Carter mentions that the average move is 6 candles regardless of timeframe, so this is what I have used...
> 
> Ignored

Hi pakeha  
  
That was a great post so thanks for sharing.  
I believe the EXIT is the hardest part of this strategy and one I struggled with for quite a while when I first started trading the Squeeze.  
Also I believe Exit strategy's differ from one market to another, for instance I use a set stop distance when trading shares with the Squeeze and use the 21 EMA as my Exit for Forex and Future Market setups.  
  
But even using the 21EMA as an Exit strategy is debatable by many traders because price has stalled and collapsing back to a loss when you Exit instead of taking the profits as momentum stalls earlier. I found taking small profits all the time ensures you miss out on those big runners that COME ALONG OCCASIONALLY.  
Without those BIG WINNERS, you never truly break away from being a AVERAGE TRADER with average profits.  
I will try and ADD ANOTHER POSITION at the 21EMA instead of getting out if I think there's a chance price is only in a pullback situation. Using this idea to ADD ANOTHER POSITION at the 21 EMA has enabled me to win 3 trades last year in excess of $100K each.  
  
They were all traded in the Australian Stock Market.  
  
That is why High Win Rates don't work with the Squeeze Setups, you need to be accepting a few small losses while WAITING PATIENTLY for those runners to come along and then ADD additional trades around the 21EMA.  
  
Your'e got it now, go get 'em tiger 

Trading thin liquidity at the boundary of the charts

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#200](/thread/post/15109032#post15109032 "Post Permalink")

  * Jan 8, 2025 9:47am  Jan 8, 2025 9:47am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar272159_71.gif) driven18](driven18)

  * Joined Jul 2012 | Status: Trader | [1,385 Posts](/search?do=process&provider=Member&searchuser=272159)

> [Quoting pakeha](/thread/post/15108925#post15108925 "View Quoted Post")
> 
> Disliked
> 
> First post on this thread I am looking at an approach using RSI (15) as confirmation. The example here is BTC on the daily chart. Trend: All EMAs pointing up for long trades and down for short trades. Entry: shown as a green vertical line... usually on the red or black dots while the Squeeze is still on + noticeable price movement away from the EMA 21 + RSI(15) confirmation breaks above 60, or below 40 Exit: this is the challenging part... John Carter mentions that the average move is 6 candles regardless of timeframe, so this is what I have used...
> 
> Ignored

I never look for quicker profits/exits. In trading, expression "you can not go wrong taking profits" is **very wrong.** **You will go broke taking quick profits.**  
  
I take full position, no add ons(do not like too much screen time and statistically it works better for me) and mark the furthest point that I believe PA can get to on whatever TF I am trading.  
  
And then Money Manage it without Fear and Greed. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Squeeze n Go | MTF System
  *   * [ **Reply to Thread** ](/thread/1319487-squeeze-n-go-mtf-system/reply#reply)

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

[Spud's MTF FIB Breakout System](/thread/30109-spuds-mtf-fib-breakout-system "Spud's MTF FIB Breakout System 
-------------------------------- 
Ever since I learned about Fibonacci numbers they have interested my pure...") 375 replies

[H1Scalper System (MTF D1,H1,M5)](/thread/166646-h1scalper-system-mtf-d1h1m5 "Here are the indicators for a manual system. 
  
Explanations, rules and trading ideas are coming... 
. 
\(2009.05.13\) 
Attached are the...") 725 replies

[MTF Trix system](/thread/183801-mtf-trix-system "Hello everybody, 
 
This thread is for developing and discussing a multi-timeframe trading system that is based on one indicator - Trix -...") 3,697 replies

[MTF Stochastics into MTF Stoch Histogram](/thread/359918-mtf-stochastics-into-mtf-stoch-histogram "Hi, 
 
I have been trading with the help of MTF Stochastics for a few weeks now with relatively good results but would appreciate if...") 8 replies

[MTF Vajioo Scalping System](/thread/195912-mtf-vajioo-scalping-system "RUBBISH") 15 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/1319487-squeeze-n-go-mtf-system/reply#reply)
  * Subscribe
  * [216](javascript:void\(0\);)

Attachments: Squeeze n Go | MTF System

Tags: Squeeze n Go | MTF System

#  [](/thread/1319487-squeeze-n-go-mtf-system)Squeeze n Go | MTF System 

  * 

  * [#201](/thread/post/15109034#post15109034 "Post Permalink")

  * Edited 10:00am  Jan 8, 2025 9:49am | Edited 10:00am 

  * [ pakeha](pakeha)

  * | Joined Sep 2011  | Status: Trader | [435 Posts](/search?do=process&provider=Member&searchuser=193174)

> [Quoting RickM](/thread/post/15109013#post15109013 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi pakeha That was a great post so thanks for sharing. I believe the EXIT is the hardest part of this strategy and one I struggled with for quite a while when I first started trading the Squeeze. Also I believe Exit strategy's differ from one market to another, for instance I use a set stop distance when trading shares with the Squeeze and use the 21 EMA as my Exit for Forex and Future Market setups. But even using the 21EMA as an Exit strategy is debatable by many traders because price has stalled and collapsing back to a loss when you...
> 
> Ignored

The other option I am back-testing is when the RSI is above 75 after 6 candles (see green line on RSI on the chart below, or 25 if shorts), is to hold the trade until the blue Squeeze histogram bar displays... this way you can get more of the extended up moves... almost double the return in this example. Trying to find a way to get both the small and bigger moves. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 175 KB](/attachment/image/4873846/thumbnail?d=1736297296)](/attachment/image/4873846?d=1736297296)   

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#202](/thread/post/15109047#post15109047 "Post Permalink")

  * Jan 8, 2025 10:16am  Jan 8, 2025 10:16am 

  * [ pakeha](pakeha)

  * | Joined Sep 2011  | Status: Trader | [435 Posts](/search?do=process&provider=Member&searchuser=193174)

Another example of two "hold longer" trades from earlier in 2024 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 157 KB](/attachment/image/4873854/thumbnail?d=1736298936)](/attachment/image/4873854?d=1736298936)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#203](/thread/post/15109234#post15109234 "Post Permalink")

  * Jan 8, 2025 3:41pm  Jan 8, 2025 3:41pm 

  * [ meta.e](meta.e)

  * | Joined Jul 2024  | Status: Trader | [3 Posts](/search?do=process&provider=Member&searchuser=1908132)

> [Quoting RickM](/thread/post/15098019#post15098019 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi Merka I use VWAP if I am looking for Squeeze setups when trading on smaller timeframes with markets that do provide Level 2 data. No wise trader should go long if the VWAP value line is above a strong bearish move, unless it has moved out at least 2 deviations. Almost every single prop firm trader, hedge fund manager and banker these days is now trained to only BUY stock / Future contracts if price is over the daily VWAP line or SELL stock / Future contracts if price is under daily VWAP line.. A public confirmation of this trend was made...
> 
> Ignored

Important information  
I used BB-Keltner Squeeze-FVBO-2.0\EMA\ on tradingview  
And then add what you said about vwap, a very useful weapon. Thank you. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#204](/thread/post/15109603#post15109603 "Post Permalink")

  * Jan 8, 2025 9:01pm  Jan 8, 2025 9:01pm 

  * [ Merka](merka)

  * Joined Jan 2016 | Status: Trader | [1,944 Posts](/search?do=process&provider=Member&searchuser=440568)

> [Quoting driven18](/thread/post/15109032#post15109032 "View Quoted Post")
> 
> Disliked
> 
> {quote} I never look for quicker profits/exits. In trading, expression "you can not go wrong taking profits" is very wrong. You will go broke taking quick profits. I take full position, no add ons(do not like too much screen time and statistically it works better for me) and mark the furthest point that I believe PA can get to on whatever TF I am trading. And then Money Manage it without Fear and Greed.
> 
> Ignored

If no fear involved means your edge is the "money managemen" and not the entry setup because no matter what price can go either directions hitting your TP/SL.  
Isn't it?  
It's clear you found your own nish edge over the market. Good on you.  
Cheers 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#205](/thread/post/15111576#post15111576 "Post Permalink")

  * Jan 10, 2025 9:00am  Jan 10, 2025 9:00am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1967050_1.gif) Ju4ara](ju4ara)

  * | Joined Oct 2024  | Status: Trader | [105 Posts](/search?do=process&provider=Member&searchuser=1967050)

Hi, these are losing trades where I have lost full position, are they executed the right way?  
Thanks. 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 100 KB](/attachment/image/4875285/thumbnail?d=1736466667)](/attachment/image/4875285?d=1736466667)   
[![Click to Enlarge

Name: screenshot.png
Size: 91 KB](/attachment/image/4875289/thumbnail?d=1736466943)](/attachment/image/4875289?d=1736466943)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#206](/thread/post/15111583#post15111583 "Post Permalink")

  * Edited 10:40am  Jan 10, 2025 9:06am | Edited 10:40am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

My current position  
  
Edit - Closed at BE 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot_20250109_190632_Photos.jpg
Size: 330 KB](/attachment/image/4875297/thumbnail?d=1736467613)](/attachment/image/4875297?d=1736467613)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#207](/thread/post/15112421#post15112421 "Post Permalink")

  * Jan 10, 2025 11:15pm  Jan 10, 2025 11:15pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar426855_1.gif) RickM](rickm)

  * Joined Sep 2015 | Status: Trader | [2,439 Posts](/search?do=process&provider=Member&searchuser=426855)

> [Quoting Ju4ara](/thread/post/15111576#post15111576 "View Quoted Post")
> 
> Disliked
> 
> Hi, these are losing trades where I have lost full position, are they executed the right way? Thanks. {image} {image}
> 
> Ignored

Hi Ju4ara  
  
My opinion is that was a C grade setup because the Squeeze Setup was occurring on a M1 chart and it was around the cross over of the London / New York Sessions.  
I would forget trading Squeeze's on M1 because the Risk / Reward isn't great. I will trade M2 for A+ Setups or trade good setups on M5.  
  
Lets see how it would have gone on M5 - if you had traded earlier, it would of been a great trade.  
  
HINT - When trading Gold, forget taking any Squeeze sets Mid Session of London, they need to appear within 3 hours of London Open or DO NOT TRADE Them.  
Look elsewhere.  
  
Edit - M1 only works well on US500 after New York Open, Check out Rocky's thread. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: gold m5 ff.png
Size: 103 KB](/attachment/image/4875803/thumbnail?d=1736518505)](/attachment/image/4875803?d=1736518505)   

Trading thin liquidity at the boundary of the charts

[0 ](javascript:void\(0\);) [6 ](javascript:void\(0\);)

  * [#208](/thread/post/15112649#post15112649 "Post Permalink")

  * Jan 11, 2025 1:25am  Jan 11, 2025 1:25am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1967050_1.gif) Ju4ara](ju4ara)

  * | Joined Oct 2024  | Status: Trader | [105 Posts](/search?do=process&provider=Member&searchuser=1967050)

> [Quoting RickM](/thread/post/15112421#post15112421 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi Ju4ara My opinion is that was a C grade setup because the Squeeze Setup was occurring on a M1 chart and it was around the cross over of the London / New York Sessions. I would forget trading Squeeze's on M1 because the Risk / Reward isn't great. I will trade M2 for A+ Setups or trade good setups on M5. Lets see how it would have gone on M5 - if you had traded earlier, it would of been a great trade. HINT - When trading Gold, forget taking any Squeeze sets Mid Session of London, they need to appear within 3 hours of London Open or DO NOT...
> 
> Ignored

Hi RickM,  
thanks a lot for sharing your wisdom. Where would you locate your sl then, because there after a few candles there is a candle with big wick which would take stoploss if was located just under signal candle’s 21 ema, these long-wicked candles often take me out of position, so what is your opinion on that? Also, would you share some more knowledge for timing and timeframes recommended to use in those time periods? I usually trade gold, us500 and us30 in london session, what would be your advise for these pairs(when to trade and in what timeframe for london session)? Thanks a lot. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#209](/thread/post/15113216#post15113216 "Post Permalink")

  * Jan 11, 2025 11:39pm  Jan 11, 2025 11:39pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar426855_1.gif) RickM](rickm)

  * Joined Sep 2015 | Status: Trader | [2,439 Posts](/search?do=process&provider=Member&searchuser=426855)

> [Quoting Ju4ara](/thread/post/15112649#post15112649 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi RickM, thanks a lot for sharing your wisdom. Where would you locate your sl then, because there after a few candles there is a candle with big wick which would take stoploss if was located just under signal candle’s 21 ema, these long-wicked candles often take me out of position, so what is your opinion on that? Also, would you share some more knowledge for timing and timeframes recommended to use in those time periods? I usually trade gold, us500 and us30 in london session, what would be your advise for these pairs(when to trade and...
> 
> Ignored

Hi Ju4ara  
  
I always wait for the candle to close before I worry about the 21EMA been taken out, those long wicks are just liquidity runs which I ignore.  
In the above case, No exit was needed because the close was above the 21EMA on M5.  
If you are going to trade M1, rather than use the 21EMA, try using the Keltner Channel set to 1.5 as your exit instead.   
On M2 or higher, the 21EMA is good to use - therefore skip M1 unless you trade US500 30 minutes after New York open.  
  
So I mostly trade ES / NQ / Gold / Oil Future's during the London session and if I can stay up to 3am, the start of the New York session.  
I may trade BITCOIN & EU Future's if something exciting is happening there.   
I normally trade on M2 (but keep an eye on M5) where I am looking for Squeeze setups on those pairs based around price leaving the 21EMA.  
I also look for Volatility Contraction Patterns inside a Squeeze Setup PLUS trade another Strategy I'm keeping under wraps till I create a THREAD on it sometime this year. - TRADING SNOW MONKEYS -  
  
Houston we have a problem.  
  
The chart on Future's M5 Gold directly from COMEX is very different from the CFD Gold chart (Chart 2 posts back) and if you had traded off that CFD chart - YOU WERE TRADING BLIND. The breakout candle on Gold Future's chart was 12 times higher in volume than any other candle on the chart and this information  
WAS VERY IMPORTANT.  
To develop this into a setup that offered A+++ - you needed to know which candle it was first, then secondary how to apply this knowledge into creating this fantastic trade entry that A+++ which was about 20 minutes earlier than your traded (Trading Snow Monkeys Strategy).  
  
It was on Gold M5 Futures Chart, not Gold M5 CFD Chart -   
  
Cheers 

Trading thin liquidity at the boundary of the charts

[0 ](javascript:void\(0\);) [4 ](javascript:void\(0\);)

  * [#210](/thread/post/15113289#post15113289 "Post Permalink")

  * Jan 12, 2025 4:05am  Jan 12, 2025 4:05am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1967050_1.gif) Ju4ara](ju4ara)

  * | Joined Oct 2024  | Status: Trader | [105 Posts](/search?do=process&provider=Member&searchuser=1967050)

Hi RickM,  
thanks for info, waiting for your new thread, would like to gain knowledge from you. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#211](/thread/post/15113371#post15113371 "Post Permalink")

  * Jan 12, 2025 9:25am  Jan 12, 2025 9:25am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar426855_1.gif) RickM](rickm)

  * Joined Sep 2015 | Status: Trader | [2,439 Posts](/search?do=process&provider=Member&searchuser=426855)

What is a VCP Pattern 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: VCP.png
Size: 74 KB](/attachment/image/4876492/thumbnail?d=1736641494)](/attachment/image/4876492?d=1736641494)   

Trading thin liquidity at the boundary of the charts

[0 ](javascript:void\(0\);) [3 ](javascript:void\(0\);)

  * [#212](/thread/post/15113402#post15113402 "Post Permalink")

  * Jan 12, 2025 12:41pm  Jan 12, 2025 12:41pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

> [Quoting RickM](/thread/post/15113371#post15113371 "View Quoted Post")
> 
> Disliked
> 
> What is a VCP Pattern {image}
> 
> Ignored

Great model there. I started exploring this concept a bit more and stumbled upon something.  
  
Lovely script on TradingView that actually was awarded Editors Picks called _**Revolution Volatility Bands With Range Contraction Signal VII**_.  
  
As stated by its author it's essentially volatility bands with a technical analysis pattern, the triangle/wedge, which he has called "contraction signal".  
  
Put simply: When price is written in blue, volatility overall is falling. When the outer bands start to fatten up in blue, a contraction signal is forming. Works with any length of your choosing.  
  
I've tested and this indicator produces squeezes that accurately align with TTM Squeeze Pro. Combined with the 21 EMA, it's another powerful tool to add to the arsenal.  
  
Wait for price and bands to be blue then follow typical squeeze and go methodology. Works quite nicely. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot_20250111_224647_Photos.jpg
Size: 374 KB](/attachment/image/4876521/thumbnail?d=1736653624)](/attachment/image/4876521?d=1736653624)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#213](/thread/post/15113411#post15113411 "Post Permalink")

  * Jan 12, 2025 2:13pm  Jan 12, 2025 2:13pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1967050_1.gif) Ju4ara](ju4ara)

  * | Joined Oct 2024  | Status: Trader | [105 Posts](/search?do=process&provider=Member&searchuser=1967050)

> [Quoting RickM](/thread/post/15113371#post15113371 "View Quoted Post")
> 
> Disliked
> 
> What is a VCP Pattern {image}
> 
> Ignored

aren’t we supposed to enter on break of range? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#214](/thread/post/15113436#post15113436 "Post Permalink")

  * Jan 12, 2025 4:14pm  Jan 12, 2025 4:14pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar601035_2.gif) axecap](axecap)

  * Joined Aug 2017 | Status: Trader | [2,336 Posts](/search?do=process&provider=Member&searchuser=601035)

BTCUSD M10  
  
Squeezy confluence.  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 47 KB](/attachment/image/4876546/thumbnail?d=1736666042)](/attachment/image/4876546?d=1736666042)   

its all just one persons opinion....

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#215](/thread/post/15113498#post15113498 "Post Permalink")

  * Jan 12, 2025 9:26pm  Jan 12, 2025 9:26pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar426855_1.gif) RickM](rickm)

  * Joined Sep 2015 | Status: Trader | [2,439 Posts](/search?do=process&provider=Member&searchuser=426855)

> [Quoting Ju4ara](/thread/post/15113411#post15113411 "View Quoted Post")
> 
> Disliked
> 
> {quote} aren’t we supposed to enter on break of range?
> 
> Ignored

Yes if its a normal Squeeze.  
If its a Squeeze + VCP Setup, get in early. 

Trading thin liquidity at the boundary of the charts

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#216](/thread/post/15113500#post15113500 "Post Permalink")

  * Jan 12, 2025 9:33pm  Jan 12, 2025 9:33pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar175961_3.gif) heispark](heispark)

  * Joined Apr 2011 | Status: Hoc Etiam Transibit.... | [5,429 Posts](/search?do=process&provider=Member&searchuser=175961)

> [Quoting RickM](/thread/post/15113371#post15113371 "View Quoted Post")
> 
> Disliked
> 
> What is a VCP Pattern {image}
> 
> Ignored

Looks similar to Patrick Wieland's flag patterns........ ![](https://resources.faireconomy.media/images/emojis/64/1f914.png?v=15.1)

Simplicity is the ultimate sophistication - Leonardo da Vinci

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#217](/thread/post/15113513#post15113513 "Post Permalink")

  * Edited 10:53pm  Jan 12, 2025 10:42pm | Edited 10:53pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar272159_71.gif) driven18](driven18)

  * Joined Jul 2012 | Status: Trader | [1,385 Posts](/search?do=process&provider=Member&searchuser=272159)

My observation and experience. I do not probe and do not split positions.  
  
It is at most importance for this technique to come in full force on the very first retracement to EMA 21 and then burst away from 21.  
  
Expression: ""The early bird gets the worm". This way you come in for a better Entry and better Stop loss.  
  
If there was a squeeze before that first burst, that would make that set up A+, but if there is a strong push away from 21, squeeze is not that relevant.   
  
Second, Third. etc. push is not as favorable statistically. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 41 KB](/attachment/image/4876612/thumbnail?d=1736689383)](/attachment/image/4876612?d=1736689383)   

[0 ](javascript:void\(0\);) [3 ](javascript:void\(0\);)

  * [#218](/thread/post/15113698#post15113698 "Post Permalink")

  * Jan 13, 2025 7:13am  Jan 13, 2025 7:13am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar588299_3.gif) RiskFighter](riskfighter)

  * Joined Jun 2017 | Status: Trader | [1,566 Posts](/search?do=process&provider=Member&searchuser=588299) | Online Now 

I have uploaded a couple of tools for this strategy. In this moment there have been 550 downloads. So there are many people that find an interest in this strategy. I think you guys should make a post saying hello to everybody and tell that you are following the thread. It is much more satisfying for OP and and other wise people if they know that there is an interest. 

Read post #1 !! Then read it again 10 more times before you ask.

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#219](/thread/post/15113758#post15113758 "Post Permalink")

  * Edited 9:48am  Jan 13, 2025 9:20am | Edited 9:48am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar426855_1.gif) RickM](rickm)

  * Joined Sep 2015 | Status: Trader | [2,439 Posts](/search?do=process&provider=Member&searchuser=426855)

> [Quoting heispark](/thread/post/15113500#post15113500 "View Quoted Post")
> 
> Disliked
> 
> {quote} Looks similar to Patrick Wieland's flag patterns........ ![](https://resources.faireconomy.media/images/emojis/64/1f914.png?v=15.1)
> 
> Ignored

Hi Heispark  
  
I think you can draw parallels between many pattern shapes but the VCP Pattern was made popular by a Market Wizard who had the best yearly returns of any trader inviewed by Jack Schwager. Mark Minervini used it to twice win the US Investment Championship as an amateur and went on to run his own Hedge fund producing eye popping returns.  
  
Minervini emphasizes that specific entry points are needed before you can enter a trade - this way you can be in profit almost straight away rather than suffer long periods of drawdown that destroys traders mindsets. My biggest trade size (Future's or Forex) I ever take is 10 contracts on ES (US500) which is about $120 per tick. A single candle can throw you into the Red $1,000 in under 10 seconds. Hell NO I want accurate entry if I trade that large otherwise the mental pain is very very painful.  
  
The Volatility Contraction Pattern works because it creates an IMBALANCE of ASK'S on a Bullish Trend or an IMBALANCE of BID's on a Bearish Trend which creates an breakout.at the expense of reversal traders equity. 

Trading thin liquidity at the boundary of the charts

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#220](/thread/post/15113878#post15113878 "Post Permalink")

  * Jan 13, 2025 12:32pm  Jan 13, 2025 12:32pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1967050_1.gif) Ju4ara](ju4ara)

  * | Joined Oct 2024  | Status: Trader | [105 Posts](/search?do=process&provider=Member&searchuser=1967050)

> [Quoting RickM](/thread/post/15112421#post15112421 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi Ju4ara My opinion is that was a C grade setup because the Squeeze Setup was occurring on a M1 chart and it was around the cross over of the London / New York Sessions. I would forget trading Squeeze's on M1 because the Risk / Reward isn't great. I will trade M2 for A+ Setups or trade good setups on M5. Let's see how it would have gone on M5 - if you had traded earlier, it would have been a great trade. HINT - When trading Gold, forget taking any Squeeze sets Mid Session of London, they need to appear within 3 hours of London Open or DO...
> 
> Ignored

So, is this basically a vcp pattern? And you enter right before a breakout when the squeeze appears and put your stop loss right below the 21ema, which makes your position more efficient, is that right? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Squeeze n Go | MTF System
  *   * [ **Reply to Thread** ](/thread/1319487-squeeze-n-go-mtf-system/reply#reply)

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

[Spud's MTF FIB Breakout System](/thread/30109-spuds-mtf-fib-breakout-system "Spud's MTF FIB Breakout System 
-------------------------------- 
Ever since I learned about Fibonacci numbers they have interested my pure...") 375 replies

[H1Scalper System (MTF D1,H1,M5)](/thread/166646-h1scalper-system-mtf-d1h1m5 "Here are the indicators for a manual system. 
  
Explanations, rules and trading ideas are coming... 
. 
\(2009.05.13\) 
Attached are the...") 725 replies

[MTF Trix system](/thread/183801-mtf-trix-system "Hello everybody, 
 
This thread is for developing and discussing a multi-timeframe trading system that is based on one indicator - Trix -...") 3,697 replies

[MTF Stochastics into MTF Stoch Histogram](/thread/359918-mtf-stochastics-into-mtf-stoch-histogram "Hi, 
 
I have been trading with the help of MTF Stochastics for a few weeks now with relatively good results but would appreciate if...") 8 replies

[MTF Vajioo Scalping System](/thread/195912-mtf-vajioo-scalping-system "RUBBISH") 15 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/1319487-squeeze-n-go-mtf-system/reply#reply)
  * Subscribe
  * [216](javascript:void\(0\);)

Attachments: Squeeze n Go | MTF System

Tags: Squeeze n Go | MTF System

#  [](/thread/1319487-squeeze-n-go-mtf-system)Squeeze n Go | MTF System 

  * 

  * [#221](/thread/post/15114078#post15114078 "Post Permalink")

  * Jan 13, 2025 5:30pm  Jan 13, 2025 5:30pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar175961_3.gif) heispark](heispark)

  * Joined Apr 2011 | Status: Hoc Etiam Transibit.... | [5,429 Posts](/search?do=process&provider=Member&searchuser=175961)

> [Quoting RickM](/thread/post/15113758#post15113758 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi Heispark I think you can draw parallels between many pattern shapes but the VCP Pattern was made popular by a Market Wizard who had the best yearly returns of any trader inviewed by Jack Schwager. Mark Minervini used it to twice win the US Investment Championship as an amateur and went on to run his own Hedge fund producing eye popping returns. Minervini emphasizes that specific entry points are needed before you can enter a trade - this way you can be in profit almost straight away rather than suffer long periods of drawdown that destroys...
> 
> Ignored

Rick, if your SL is taken, are you going to reverse your position immediately? As you know, market makers are not fool and they make fake breakouts time to time, occasionally multiple time in either side to kill breakout traders. 

Simplicity is the ultimate sophistication - Leonardo da Vinci

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#222](/thread/post/15114704#post15114704 "Post Permalink")

  * Edited 1:05am  Jan 14, 2025 12:51am | Edited 1:05am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar588299_3.gif) RiskFighter](riskfighter)

  * Joined Jun 2017 | Status: Trader | [1,566 Posts](/search?do=process&provider=Member&searchuser=588299) | Online Now 

> [Quoting RickM](/thread/post/15113758#post15113758 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi Heispark I think you can draw parallels between many pattern shapes but the VCP Pattern was made popular by a Market Wizard who had the best yearly returns of any trader inviewed by Jack Schwager. Mark Minervini used it to twice win the US Investment Championship as an amateur and went on to run his own Hedge fund producing eye popping returns. Minervini emphasizes that specific entry points are needed before you can enter a trade - this way you can be in profit almost straight away rather than suffer long periods of drawdown that destroys...
> 
> Ignored

This VCP is utmost interesting. Are you making a thread by this Rick? Or can you point in a direction of further reading. I of cause found something, but it is mostly stock related and a bit to short in the explaining.  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 46 KB](/attachment/image/4877336/thumbnail?d=1736784347)](/attachment/image/4877336?d=1736784347)   

Read post #1 !! Then read it again 10 more times before you ask.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#223](/thread/post/15114773#post15114773 "Post Permalink")

  * Jan 14, 2025 2:05am  Jan 14, 2025 2:05am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar588299_3.gif) RiskFighter](riskfighter)

  * Joined Jun 2017 | Status: Trader | [1,566 Posts](/search?do=process&provider=Member&searchuser=588299) | Online Now 

I found the books:  
  
•[Think & Trade Like a Champion: The Secrets, Rules & Blunt Truths of a Stock Market Wizard eBook : ](https://www.amazon.in/Think-Trade-Like-Champion-Secrets-ebook/dp/B0755Y5LCZ?crid=AO1SR0AZNAEI&keywords=mark+minervini+books&qid=1673070075&sprefix=mark+mine,aps,259&sr=8-1&linkCode=sl1&tag=learntotrad09-21&linkId=32b48528bc92d82e74464cf0f05ede15&language=en_IN&ref_=as_li_ss_tl)[Minervini](https://www.amazon.in/Think-Trade-Like-Champion-Secrets-ebook/dp/B0755Y5LCZ?crid=AO1SR0AZNAEI&keywords=mark+minervini+books&qid=1673070075&sprefix=mark+mine,aps,259&sr=8-1&linkCode=sl1&tag=learntotrad09-21&linkId=32b48528bc92d82e74464cf0f05ede15&language=en_IN&ref_=as_li_ss_tl)[, Mark: Amazon.in: Kindle Store](https://www.amazon.in/Think-Trade-Like-Champion-Secrets-ebook/dp/B0755Y5LCZ?crid=AO1SR0AZNAEI&keywords=mark+minervini+books&qid=1673070075&sprefix=mark+mine,aps,259&sr=8-1&linkCode=sl1&tag=learntotrad09-21&linkId=32b48528bc92d82e74464cf0f05ede15&language=en_IN&ref_=as_li_ss_tl)  
•[Trade Like a Stock Market Wizard: How to Achieve Super Performance in Stocks in Any Market: Speak Your Mind and Get the Results You Want : ](https://www.amazon.in/Trade-Like-Stock-Market-Wizard/dp/0071807225?crid=AO1SR0AZNAEI&keywords=mark+minervini+books&qid=1673070075&sprefix=mark+mine,aps,259&sr=8-2&linkCode=sl1&tag=learntotrad09-21&linkId=a582450d1960c26d3cafa0eb277fcf8c&language=en_IN&ref_=as_li_ss_tl)[Minervini](https://www.amazon.in/Trade-Like-Stock-Market-Wizard/dp/0071807225?crid=AO1SR0AZNAEI&keywords=mark+minervini+books&qid=1673070075&sprefix=mark+mine,aps,259&sr=8-2&linkCode=sl1&tag=learntotrad09-21&linkId=a582450d1960c26d3cafa0eb277fcf8c&language=en_IN&ref_=as_li_ss_tl)[, Mark: Amazon.in: Books](https://www.amazon.in/Trade-Like-Stock-Market-Wizard/dp/0071807225?crid=AO1SR0AZNAEI&keywords=mark+minervini+books&qid=1673070075&sprefix=mark+mine,aps,259&sr=8-2&linkCode=sl1&tag=learntotrad09-21&linkId=a582450d1960c26d3cafa0eb277fcf8c&language=en_IN&ref_=as_li_ss_tl)

Read post #1 !! Then read it again 10 more times before you ask.

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#224](/thread/post/15115069#post15115069 "Post Permalink")

  * Jan 14, 2025 10:03am  Jan 14, 2025 10:03am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar426855_1.gif) RickM](rickm)

  * Joined Sep 2015 | Status: Trader | [2,439 Posts](/search?do=process&provider=Member&searchuser=426855)

> [Quoting Ju4ara](/thread/post/15113878#post15113878 "View Quoted Post")
> 
> Disliked
> 
> {quote} So, is this basically a vcp pattern? And you enter right before a breakout when the squeeze appears and put your stop loss right below the 21ema, which makes your position more efficient, is that right?
> 
> Ignored

Yes, I’m getting in early because it’s a great VCP setup where’s on a standard Squeeze setup I am waiting for a breakout of range.  
However I prefer taking trades that are leaving the 21EMA so if the breakout candle is too separated from the 21, it’s a No trade for me. 

Trading thin liquidity at the boundary of the charts

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#225](/thread/post/15115118#post15115118 "Post Permalink")

  * Jan 14, 2025 11:39am  Jan 14, 2025 11:39am 

  * [ binnie](binnie)

  * | Joined Dec 2010  | Status: invisible | [987 Posts](/search?do=process&provider=Member&searchuser=163246)

> [Quoting RiskFighter](/thread/post/15114773#post15114773 "View Quoted Post")
> 
> Disliked
> 
> I found the books: •[Think & Trade Like a Champion: The Secrets, Rules & Blunt Truths of a Stock Market Wizard eBook : ](https://www.amazon.in/Think-Trade-Like-Champion-Secrets-ebook/dp/B0755Y5LCZ?crid=AO1SR0AZNAEI&keywords=mark+minervini+books&qid=1673070075&sprefix=mark+mine,aps,259&sr=8-1&linkCode=sl1&tag=learntotrad09-21&linkId=32b48528bc92d82e74464cf0f05ede15&language=en_IN&ref_=as_li_ss_tl)[Minervini](https://www.amazon.in/Think-Trade-Like-Champion-Secrets-ebook/dp/B0755Y5LCZ?crid=AO1SR0AZNAEI&keywords=mark+minervini+books&qid=1673070075&sprefix=mark+mine,aps,259&sr=8-1&linkCode=sl1&tag=learntotrad09-21&linkId=32b48528bc92d82e74464cf0f05ede15&language=en_IN&ref_=as_li_ss_tl)[,](https://www.amazon.in/Think-Trade-Like-Champion-Secrets-ebook/dp/B0755Y5LCZ?crid=AO1SR0AZNAEI&keywords=mark+minervini+books&qid=1673070075&sprefix=mark+mine,aps,259&sr=8-1&linkCode=sl1&tag=learntotrad09-21&linkId=32b48528bc92d82e74464cf0f05ede15&language=en_IN&ref_=as_li_ss_tl)...
> 
> Ignored

Cheers Risk. Appreciate your efforts & general info. Trade well buddy. 

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#226](/thread/post/15115160#post15115160 "Post Permalink")

  * Jan 14, 2025 1:09pm  Jan 14, 2025 1:09pm 

  * [ prestige09](prestige09)

  * | Joined Nov 2022  | Status: Trader | [14 Posts](/search?do=process&provider=Member&searchuser=1536799)

> [Quoting RickM](/thread/post/15113371#post15113371 "View Quoted Post")
> 
> Disliked
> 
> What is a VCP Pattern {image}
> 
> Ignored

Hello, Rick. I use the VCP (Volatility Contraction Pattern) strategy when trading stocks, and it has consistently delivered excellent results for me. Over time, I’ve developed a preference for Point & Figure (P&F) charts to identify VCP patterns, as they provide a cleaner and more straightforward representation of price action without the noise often present in traditional charts.  
To refine my approach, I use larger box values and longer timeframes on P&F charts for identifying the overall pattern and structure. For entries, I switch to smaller box values and shorter timeframes to pinpoint precise breakout levels with better accuracy.  
Here’s an example of my most recent trade using this method. Take a look at the P&F chart for pattern identification and the OHLC chart also 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: Screenshot_44.jpg
Size: 175 KB](/attachment/image/4877592/thumbnail?d=1736827452)](/attachment/image/4877592?d=1736827452)   
[![Click to Enlarge

Name: Screenshot_45.jpg
Size: 35 KB](/attachment/image/4877593/thumbnail?d=1736827454)](/attachment/image/4877593?d=1736827454)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#227](/thread/post/15115741#post15115741 "Post Permalink")

  * Jan 14, 2025 11:03pm  Jan 14, 2025 11:03pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar426855_1.gif) RickM](rickm)

  * Joined Sep 2015 | Status: Trader | [2,439 Posts](/search?do=process&provider=Member&searchuser=426855)

> [Quoting prestige09](/thread/post/15115160#post15115160 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hello, Rick. I use the VCP (Volatility Contraction Pattern) strategy when trading stocks, and it has consistently delivered excellent results for me. Over time, I’ve developed a preference for Point & Figure (P&F) charts to identify VCP patterns, as they provide a cleaner and more straightforward representation of price action without the noise often present in traditional charts. To refine my approach, I use larger box values and longer timeframes on P&F charts for identifying the overall pattern and structure. For entries, I switch to...
> 
> Ignored

Hi prestige  
  
That's a very interesting post, thanks for sharing. I think I need to study your P&F charts for a while to get my head around the story they are telling.  
I use the VCP Pattern a lot on Stocks and Future's as well and I agree it's such a great trade setup.  
Can I ask if you have used much it on trading Forex or Future's Markets and if so please share some of your experience's using this unique Pattern formation.  
  
Cheers 

Trading thin liquidity at the boundary of the charts

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#228](/thread/post/15115794#post15115794 "Post Permalink")

  * Edited 11:43pm  Jan 14, 2025 11:29pm | Edited 11:43pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar272159_71.gif) driven18](driven18)

  * Joined Jul 2012 | Status: Trader | [1,385 Posts](/search?do=process&provider=Member&searchuser=272159)

DOW Futures 2 Min TF, real live trades.  
  
As previously stated, the moment EMA 21 cleared, I entered, Profit +150 pips(points), 3 trades (one earlier in London session), **done for the day.![](https://resources.faireconomy.media/images/emojis/64/1f37a.png?v=15.1)**

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 22 KB](/attachment/image/4878040/thumbnail?d=1736864934)](/attachment/image/4878040?d=1736864934)   

[0 ](javascript:void\(0\);) [4 ](javascript:void\(0\);)

  * [#229](/thread/post/15115800#post15115800 "Post Permalink")

  * Edited 11:55pm  Jan 14, 2025 11:34pm | Edited 11:55pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar426855_1.gif) RickM](rickm)

  * Joined Sep 2015 | Status: Trader | [2,439 Posts](/search?do=process&provider=Member&searchuser=426855)

> [Quoting RiskFighter](/thread/post/15114704#post15114704 "View Quoted Post")
> 
> Disliked
> 
> {quote} This VCP is utmost interesting. Are you making a thread by this Rick? Or can you point in a direction of further reading. I of cause found something, but it is mostly stock related and a bit to short in the explaining. There is something about stage 1 and 2 relation. As it happens I just yesterday made a tool identifying instruments with 3 EMA's pointing in same direction - aligning well and growing. That could be part of a helping tool to identify those nice setups. [Finding](https://www.forexfactory.com/thread/post/15113704#post15113704)...
> 
> Ignored

Hi Risk  
  
More strategy's on how to trade the VCP Patterns within Squeeze Setups but more importantly how to trap BIG PLAYERS that are trading like Snow Monkeys.  
More about that later. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: SNOW.png
Size: 123 KB](/attachment/image/4878057/thumbnail?d=1736866501)](/attachment/image/4878057?d=1736866501)   

Trading thin liquidity at the boundary of the charts

[0 ](javascript:void\(0\);) [5 ](javascript:void\(0\);)

  * [#230](/thread/post/15115829#post15115829 "Post Permalink")

  * Jan 14, 2025 11:55pm  Jan 14, 2025 11:55pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar272159_71.gif) driven18](driven18)

  * Joined Jul 2012 | Status: Trader | [1,385 Posts](/search?do=process&provider=Member&searchuser=272159)

**RickM** , I have to **give a compliment** , after sooo many years knowing each other, I think I finally grabbed something from you that am trying to incorporate into my scalp trading, 21 (Fib) EMA. The more I look at it, the more I like the Fib and Ema relationship. Be safe as you coming down the mountain skiing.![](https://resources.faireconomy.media/images/emojis/64/26f7-fe0f.png?v=15.1)  
  
We are in Budapest taking the hot thermal baths. ![](https://resources.faireconomy.media/images/emojis/64/1f60e.png?v=15.1)

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 6 KB](/attachment/image/4878056/thumbnail?d=1736866493)](/attachment/image/4878056?d=1736866493)   

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#231](/thread/post/15115834#post15115834 "Post Permalink")

  * Jan 14, 2025 11:59pm  Jan 14, 2025 11:59pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar426855_1.gif) RickM](rickm)

  * Joined Sep 2015 | Status: Trader | [2,439 Posts](/search?do=process&provider=Member&searchuser=426855)

> [Quoting driven18](/thread/post/15115829#post15115829 "View Quoted Post")
> 
> Disliked
> 
> RickM, I have to give a compliment, after sooo many years knowing each other, I think I finally grabbed something from you that am trying to incorporate into my scalp trading, 21 (Fib) EMA. The more I look at it, the more I like the Fib and Ema relationship. Be safe as you coming down the mountain skiing.![](https://resources.faireconomy.media/images/emojis/64/26f7-fe0f.png?v=15.1) We are in Budapest taking the hot thermal baths. ![](https://resources.faireconomy.media/images/emojis/64/1f60e.png?v=15.1) {image}
> 
> Ignored

Hi driven  
  
That's why I use the 89 EMA as my BIAS TREND  
  
Cheers 

Trading thin liquidity at the boundary of the charts

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#232](/thread/post/15116616#post15116616 "Post Permalink")

  * Jan 15, 2025 6:17pm  Jan 15, 2025 6:17pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1967050_1.gif) Ju4ara](ju4ara)

  * | Joined Oct 2024  | Status: Trader | [105 Posts](/search?do=process&provider=Member&searchuser=1967050)

Hi, is this considered a vcp pattern, and if yes, then what timeframe should I use for entry(m5 or m2)? On my own research I found that m2 has too many fakes while m5 is more stable, but gives worse RRR. 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 97 KB](/attachment/image/4878616/thumbnail?d=1736932593)](/attachment/image/4878616?d=1736932593)   
[![Click to Enlarge

Name: screenshot.png
Size: 101 KB](/attachment/image/4878617/thumbnail?d=1736932626)](/attachment/image/4878617?d=1736932626)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#233](/thread/post/15116817#post15116817 "Post Permalink")

  * Jan 15, 2025 9:34pm  Jan 15, 2025 9:34pm 

  * [ prestige09](prestige09)

  * | Joined Nov 2022  | Status: Trader | [14 Posts](/search?do=process&provider=Member&searchuser=1536799)

> [Quoting RickM](/thread/post/15115741#post15115741 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi prestige That's a very interesting post, thanks for sharing. I think I need to study your P&F charts for a while to get my head around the story they are telling. I use the VCP Pattern a lot on Stocks and Future's as well and I agree it's such a great trade setup. Can I ask if you have used much it on trading Forex or Future's Markets and if so please share some of your experience's using this unique Pattern formation. Cheers
> 
> Ignored

Thank you for your kind words, Rick! I’m glad you found my post interesting. P&F charts are indeed a fantastic tool for visualizing patterns like VCP, and once you get familiar with them, the clarity they offer can be quite eye-opening.  
It’s great to hear that you also use the VCP pattern on stocks and futures—I completely agree that it’s a highly effective setup when applied with discipline and the right tools.  
To answer your question, yes, I have experimented with the VCP pattern in the Forex and Futures markets. In Forex, I primarily apply VCP and other patterns to gold (XAU/USD), and it has given me good results. P&F charts are especially helpful in filtering out noise in such a volatile market, making contractions and breakout points more apparent.  
However, I don’t use TradingView for P&F or Renko charts, as I’ve found their calculations and formulas for these chart types to be unreliable. Instead, I rely on an Indian market software that provides accurate formulas and calculations for P&F and Renko charts. While this software primarily supports Indian market data (e.g., MCX: GOLD FUTURE instead of XAU/USD), the movements and behavior of both charts are essentially the same. If I spot a long or short setup on MCX GOLD FUTURE, I trade the same setup on XAU/USD.  
There is a way to integrate live data for Forex, crypto, and other global markets into this software—one of my friends has set it up—but since I focus on stock markets and only trade XAU/USD in Forex, I haven’t added other market data.  
My approach is consistent across all markets: I start with larger box values and timeframes to identify the broader structure, then shift to smaller box values and timeframes to refine my entry and exit points. It’s a systematic process, and the results have been worth the effort.  
If you’d like, I can share an example of a Forex or Futures trade where I applied the VCP pattern using P&F charts. Feel free to DM me.  
here's one example of VCP and Turtle breakout system. 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: Screenshot_46.jpg
Size: 193 KB](/attachment/image/4878781/thumbnail?d=1736944423)](/attachment/image/4878781?d=1736944423)   
[![Click to Enlarge

Name: Screenshot_47.jpg
Size: 163 KB](/attachment/image/4878782/thumbnail?d=1736944424)](/attachment/image/4878782?d=1736944424)   

[0 ](javascript:void\(0\);) [4 ](javascript:void\(0\);)

  * [#234](/thread/post/15116923#post15116923 "Post Permalink")

  * Jan 15, 2025 10:35pm  Jan 15, 2025 10:35pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar426855_1.gif) RickM](rickm)

  * Joined Sep 2015 | Status: Trader | [2,439 Posts](/search?do=process&provider=Member&searchuser=426855)

A couple of trades I took tonight was on Oil, a nice Break of the 21EMA during a Squeeze and one without the Squeeze and really just an continuation trade.  
Both on M2 with a decent trade size.  
The best trades always appear when traders get trapped within a range and have to COVER their positions.   
Looking at the trades now, I failed to just stay in a LONG position and ADD when price pulled back to the 21EMA.  
Nice profit but only a B grade for me. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Oil 1.png
Size: 118 KB](/attachment/image/4878823/thumbnail?d=1736948153)](/attachment/image/4878823?d=1736948153)   

Trading thin liquidity at the boundary of the charts

[0 ](javascript:void\(0\);) [5 ](javascript:void\(0\);)

  * [#235](/thread/post/15116954#post15116954 "Post Permalink")

  * Jan 15, 2025 10:43pm  Jan 15, 2025 10:43pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar426855_1.gif) RickM](rickm)

  * Joined Sep 2015 | Status: Trader | [2,439 Posts](/search?do=process&provider=Member&searchuser=426855)

> [Quoting prestige09](/thread/post/15116817#post15116817 "View Quoted Post")
> 
> Disliked
> 
> {quote} Thank you for your kind words, Rick! I’m glad you found my post interesting. P&F charts are indeed a fantastic tool for visualizing patterns like VCP, and once you get familiar with them, the clarity they offer can be quite eye-opening. It’s great to hear that you also use the VCP pattern on stocks and futures—I completely agree that it’s a highly effective setup when applied with discipline and the right tools. To answer your question, yes, I have experimented with the VCP pattern in the Forex and Futures markets. In Forex, I primarily...
> 
> Ignored

Hi prestige  
  
I'll PM you, I have a few questions about your setups.  
  
I suppose I better ask about your Turtle Breakout Strategy, how does it add value to your trading?.  
  
Cheers 

Trading thin liquidity at the boundary of the charts

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#236](/thread/post/15116987#post15116987 "Post Permalink")

  * Jan 15, 2025 10:54pm  Jan 15, 2025 10:54pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar426855_1.gif) RickM](rickm)

  * Joined Sep 2015 | Status: Trader | [2,439 Posts](/search?do=process&provider=Member&searchuser=426855)

> [Quoting Ju4ara](/thread/post/15116616#post15116616 "View Quoted Post")
> 
> Disliked
> 
> Hi, is this considered a vcp pattern, and if yes, then what timeframe should I use for entry(m5 or m2)? On my own research I found that m2 has too many fakes while m5 is more stable, but gives worse RRR. {image} {image}
> 
> Ignored

Hi Ju4ara  
  
I would be happy to call that setup a VCP Pattern, very few are prefect.  
We do need that first downwards move to be a strong rejection and then get higher lows while disregarding wicks.  
M5 is a good all around timeframe from which we can scalp with good results, I fine personally that M2 works better on Future's because the candle highs and lows are different from CFD charts often meaning the setups are often more available.  
  
Cheers 

Trading thin liquidity at the boundary of the charts

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#237](/thread/post/15117009#post15117009 "Post Permalink")

  * Jan 15, 2025 11:01pm  Jan 15, 2025 11:01pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar272159_71.gif) driven18](driven18)

  * Joined Jul 2012 | Status: Trader | [1,385 Posts](/search?do=process&provider=Member&searchuser=272159)

> [Quoting prestige09](/thread/post/15116817#post15116817 "View Quoted Post")
> 
> Disliked
> 
> {quote} Thank you for your kind words, Rick! I’m glad you found my post interesting. P&F charts are indeed a fantastic tool for visualizing patterns like VCP, and once you get familiar with them, the clarity they offer can be quite eye-opening. It’s great to hear that you also use the VCP pattern on stocks and futures—I completely agree that it’s a highly effective setup when applied with discipline and the right tools. To answer your question, yes, I have experimented with the VCP pattern in the Forex and Futures markets. In Forex, I primarily...
> 
> Ignored

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#238](/thread/post/15117026#post15117026 "Post Permalink")

  * Edited 11:21pm  Jan 15, 2025 11:08pm | Edited 11:21pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar272159_71.gif) driven18](driven18)

  * Joined Jul 2012 | Status: Trader | [1,385 Posts](/search?do=process&provider=Member&searchuser=272159)

This is more for Machine and other subs here..  
  
Rick, I am going to use your chart(last time ![](https://resources.faireconomy.media/images/emojis/64/1f60e.png?v=15.1))..I will repost my below.  
  
50% of my trading is happening on Limit Buy/Sell orders...your chart is perfect for this demonstration.  
  
Let the burst away from EMA 21 happen and then wait for retracement to value area(my name for it).  
  
I would recommend for more aggressive traders to come in on Full Position on Limit orders, no add ons, first trade on Limit Sell and second trade on Limit Buy.  
  
Second chart is my chart from yesterday - Blue circles would of been Limit Buy and Limit Sell. 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 50 KB](/attachment/image/4878883/thumbnail?d=1736950129)](/attachment/image/4878883?d=1736950129)   
[![Click to Enlarge

Name: screenshot.png
Size: 59 KB](/attachment/image/4878903/thumbnail?d=1736950580)](/attachment/image/4878903?d=1736950580)   

[0 ](javascript:void\(0\);) [5 ](javascript:void\(0\);)

  * [#239](/thread/post/15117289#post15117289 "Post Permalink")

  * Jan 16, 2025 1:09am  Jan 16, 2025 1:09am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

> [Quoting prestige09](/thread/post/15116817#post15116817 "View Quoted Post")
> 
> Disliked
> 
> {quote} Thank you for your kind words, Rick! I’m glad you found my post interesting. P&F charts are indeed a fantastic tool for visualizing patterns like VCP, and once you get familiar with them, the clarity they offer can be quite eye-opening. It’s great to hear that you also use the VCP pattern on stocks and futures—I completely agree that it’s a highly effective setup when applied with discipline and the right tools. To answer your question, yes, I have experimented with the VCP pattern in the Forex and Futures markets. In Forex, I primarily...
> 
> Ignored

Feel free to post whatever you please here my friend. We are all always expanding our outlook and ideologies on the market. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#240](/thread/post/15117294#post15117294 "Post Permalink")

  * Jan 16, 2025 1:11am  Jan 16, 2025 1:11am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

> [Quoting driven18](/thread/post/15117026#post15117026 "View Quoted Post")
> 
> Disliked
> 
> This is more for Machine and other subs here.. Rick, I am going to use your chart(last time ![](https://resources.faireconomy.media/images/emojis/64/1f60e.png?v=15.1))..I will repost my below. 50% of my trading is happening on Limit Buy/Sell orders...your chart is perfect for this demonstration. Let the burst away from EMA 21 happen and then wait for retracement to value area(my name for it). I would recommend for more aggressive traders to come in on Full Position on Limit orders, no add ons, first trade on Limit Sell and second trade on Limit Buy. Second chart is my chart from yesterday - Blue circles would...
> 
> Ignored

Makes too much sense ![](https://resources.faireconomy.media/images/emojis/64/1f602.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Squeeze n Go | MTF System
  *   * [ **Reply to Thread** ](/thread/1319487-squeeze-n-go-mtf-system/reply#reply)

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

[Spud's MTF FIB Breakout System](/thread/30109-spuds-mtf-fib-breakout-system "Spud's MTF FIB Breakout System 
-------------------------------- 
Ever since I learned about Fibonacci numbers they have interested my pure...") 375 replies

[H1Scalper System (MTF D1,H1,M5)](/thread/166646-h1scalper-system-mtf-d1h1m5 "Here are the indicators for a manual system. 
  
Explanations, rules and trading ideas are coming... 
. 
\(2009.05.13\) 
Attached are the...") 725 replies

[MTF Trix system](/thread/183801-mtf-trix-system "Hello everybody, 
 
This thread is for developing and discussing a multi-timeframe trading system that is based on one indicator - Trix -...") 3,697 replies

[MTF Stochastics into MTF Stoch Histogram](/thread/359918-mtf-stochastics-into-mtf-stoch-histogram "Hi, 
 
I have been trading with the help of MTF Stochastics for a few weeks now with relatively good results but would appreciate if...") 8 replies

[MTF Vajioo Scalping System](/thread/195912-mtf-vajioo-scalping-system "RUBBISH") 15 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/1319487-squeeze-n-go-mtf-system/reply#reply)
  * Subscribe
  * [216](javascript:void\(0\);)

Attachments: Squeeze n Go | MTF System

Tags: Squeeze n Go | MTF System

#  [](/thread/1319487-squeeze-n-go-mtf-system)Squeeze n Go | MTF System 

  * 

  * [#241](/thread/post/15117305#post15117305 "Post Permalink")

  * Jan 16, 2025 1:16am  Jan 16, 2025 1:16am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

> [Quoting driven18](/thread/post/15117026#post15117026 "View Quoted Post")
> 
> Disliked
> 
> This is more for Machine and other subs here.. Rick, I am going to use your chart(last time ![](https://resources.faireconomy.media/images/emojis/64/1f60e.png?v=15.1))..I will repost my below. 50% of my trading is happening on Limit Buy/Sell orders...your chart is perfect for this demonstration. Let the burst away from EMA 21 happen and then wait for retracement to value area(my name for it). I would recommend for more aggressive traders to come in on Full Position on Limit orders, no add ons, first trade on Limit Sell and second trade on Limit Buy. Second chart is my chart from yesterday - Blue circles would...
> 
> Ignored

Quick scan and I found a beautiful setup from a couple days ago.  
  
I've coded a simple indicator that can detect a break and retest of the value area as you would call it. (congrestion of green arrows) Then, per usual, couple that with a heavy squeeze and breakout w/ momentum. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot_20250115_111503_Photos.jpg
Size: 401 KB](/attachment/image/4879036/thumbnail?d=1736957734)](/attachment/image/4879036?d=1736957734)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#242](/thread/post/15117434#post15117434 "Post Permalink")

  * Jan 16, 2025 3:16am  Jan 16, 2025 3:16am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

Squeeze, 21 Break, Retest, Momentum  
  
Got in a little late however 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: Screenshot_20250115_131457_Photos.jpg
Size: 381 KB](/attachment/image/4879098/thumbnail?d=1736964917)](/attachment/image/4879098?d=1736964917)   
[![Click to Enlarge

Name: Screenshot_20250115_131959_Photos.jpg
Size: 428 KB](/attachment/image/4879099/thumbnail?d=1736965212)](/attachment/image/4879099?d=1736965212)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#243](/thread/post/15117531#post15117531 "Post Permalink")

  * Jan 16, 2025 4:58am  Jan 16, 2025 4:58am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

UJ M5 in a nice squeeze. Overall down trend, price pulled back up and then fell down through 21 and found resistance around the 21 again when attempting to pull back up. Thoughts.. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot_20250115_145845_Photos.jpg
Size: 448 KB](/attachment/image/4879144/thumbnail?d=1736971136)](/attachment/image/4879144?d=1736971136)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#244](/thread/post/15117545#post15117545 "Post Permalink")

  * Jan 16, 2025 5:20am  Jan 16, 2025 5:20am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar272159_71.gif) driven18](driven18)

  * Joined Jul 2012 | Status: Trader | [1,385 Posts](/search?do=process&provider=Member&searchuser=272159)

I would not trade that with this technique...C- - - set up, high risk, because too large of the retracement up (in black) from short to make sense of it and consider it. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 128 KB](/attachment/image/4879153/thumbnail?d=1736972362)](/attachment/image/4879153?d=1736972362)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#245](/thread/post/15117549#post15117549 "Post Permalink")

  * Edited 6:11am  Jan 16, 2025 5:22am | Edited 6:11am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar272159_71.gif) driven18](driven18)

  * Joined Jul 2012 | Status: Trader | [1,385 Posts](/search?do=process&provider=Member&searchuser=272159)

What a stock market today in general...Portfolios of people(incl. me) who work with stocks and crypto's rejoiced and rejuvenated.  
  
Hard work to research for weeks and months to bring "your best" to portfolios, but I am grateful, of course that hard work pays off ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1).  
  
Later today or tomorrow may bring a different market, but the point is, if the portfolio is solid and was at the high, you know it will get there again.  
  
Love USA markets! ![](https://resources.faireconomy.media/images/emojis/64/1f1fa-1f1f8.png?v=15.1)  
  
P.S. One of the reason I also trade Index Futures. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#246](/thread/post/15117601#post15117601 "Post Permalink")

  * Jan 16, 2025 7:46am  Jan 16, 2025 7:46am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

> [Quoting driven18](/thread/post/15117545#post15117545 "View Quoted Post")
> 
> Disliked
> 
> I would not trade that with this technique...C- - - set up, high risk, because too large of the retracement up (in black) from short to make sense of it and consider it. {image}
> 
> Ignored

Worked today, I'll consider it luck 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot_20250115_174623_Photos.jpg
Size: 423 KB](/attachment/image/4879185/thumbnail?d=1736981194)](/attachment/image/4879185?d=1736981194)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#247](/thread/post/15117603#post15117603 "Post Permalink")

  * Jan 16, 2025 7:50am  Jan 16, 2025 7:50am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

> [Quoting driven18](/thread/post/15117545#post15117545 "View Quoted Post")
> 
> Disliked
> 
> I would not trade that with this technique...C- - - set up, high risk, because too large of the retracement up (in black) from short to make sense of it and consider it. {image}
> 
> Ignored

Could look at it like, the bigger the retracement the more bullish suckers trapped and the more momentum coming out of the squeeze. The lower high taken out and a trend line break, just for price to plummet on them.   
  
Agreed too risky, but I love captializing on trapped retail traders ![](https://resources.faireconomy.media/images/emojis/64/1f602.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#248](/thread/post/15117726#post15117726 "Post Permalink")

  * Jan 16, 2025 12:00pm  Jan 16, 2025 12:00pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar272159_71.gif) driven18](driven18)

  * Joined Jul 2012 | Status: Trader | [1,385 Posts](/search?do=process&provider=Member&searchuser=272159)

> [Quoting MachineLearn](/thread/post/15117603#post15117603 "View Quoted Post")
> 
> Disliked
> 
> {quote} Could look at it like, the bigger the retracement the more bullish suckers trapped and the more momentum coming out of the squeeze. The lower high taken out and a trend line break, just for price to plummet on them. Agreed too risky, but I love captializing on trapped retail traders ![](https://resources.faireconomy.media/images/emojis/64/1f602.png?v=15.1)
> 
> Ignored

Could but Would Not.![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#249](/thread/post/15117774#post15117774 "Post Permalink")

  * Jan 16, 2025 1:19pm  Jan 16, 2025 1:19pm 

  * [ prestige09](prestige09)

  * | Joined Nov 2022  | Status: Trader | [14 Posts](/search?do=process&provider=Member&searchuser=1536799)

> [Quoting RickM](/thread/post/15116954#post15116954 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi prestige I'll PM you, I have a few questions about your setups. I suppose I better ask about your Turtle Breakout Strategy, how does it add value to your trading?. Cheers
> 
> Ignored

Back then i wasn't abele to much trading because of my job, so i trade only breakout strategy so i can set alert on breakout price, i start with trendline breakout but i don't use normal trendline i use 45 degree trendline it give me good result as well i got 8-10 entry in month, then i spent more time on chart and start using turtle breakout as well in intraday in commodity and in stock for positional trade, then one of my friend told me about VCP, i fiend some similarity's in both setup and start doing both and make some scanners and it's made my life easy, now hours of chart reading can be done by 1-2 min. i dont like spending too much time on charts, so this breakout strategy and scanner made my work to easy, we can discuss on this setup and how i select my stock on google meet. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#250](/thread/post/15117777#post15117777 "Post Permalink")

  * Jan 16, 2025 1:25pm  Jan 16, 2025 1:25pm 

  * [ prestige09](prestige09)

  * | Joined Nov 2022  | Status: Trader | [14 Posts](/search?do=process&provider=Member&searchuser=1536799)

> [Quoting driven18](/thread/post/15117009#post15117009 "View Quoted Post")
> 
> Disliked
> 

> 
> Ignored

i start trading in early 2022, using candlestick, then i discover P&F i trade in Indian stock market and forex. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#251](/thread/post/15117795#post15117795 "Post Permalink")

  * Jan 16, 2025 1:53pm  Jan 16, 2025 1:53pm 

  * [ prestige09](prestige09)

  * | Joined Nov 2022  | Status: Trader | [14 Posts](/search?do=process&provider=Member&searchuser=1536799)

Yesterdays silver trade using Turtle breakout on P&F chart, I think its very similar to Squeeze n Go. 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: Screenshot_48.jpg
Size: 216 KB](/attachment/image/4879297/thumbnail?d=1737003184)](/attachment/image/4879297?d=1737003184)   
[![Click to Enlarge

Name: Screenshot_49.jpg
Size: 230 KB](/attachment/image/4879298/thumbnail?d=1737003186)](/attachment/image/4879298?d=1737003186)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#252](/thread/post/15118118#post15118118 "Post Permalink")

  * Edited 8:02pm  Jan 16, 2025 7:51pm | Edited 8:02pm 

  * [ Merka](merka)

  * Joined Jan 2016 | Status: Trader | [1,944 Posts](/search?do=process&provider=Member&searchuser=440568)

> [Quoting prestige09](/thread/post/15117795#post15117795 "View Quoted Post")
> 
> Disliked
> 
> Yesterdays silver trade using Turtle breakout on P&F chart, I think its very similar to Squeeze n Go. {image} {image}
> 
> Ignored

Do you find P&F charts useful in FX?  
Thanks 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#253](/thread/post/15120016#post15120016 "Post Permalink")

  * Edited 11:12am  Jan 18, 2025 11:01am | Edited 11:12am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar272159_71.gif) driven18](driven18)

  * Joined Jul 2012 | Status: Trader | [1,385 Posts](/search?do=process&provider=Member&searchuser=272159)

Dow Futures 5 Min TF.  
  
Sometimes you get stuck for the looooong(in America)weekend..traveling, just looked at my laptop...O, well..in profit +78 points, not too bad ![](https://resources.faireconomy.media/images/emojis/64/1f600.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f37a.png?v=15.1).  
  
Relevance: Under EMA 21 and intuition that people will be taking profits going into the long weekend, but under EMA 21, nevertheless. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 12 KB](/attachment/image/4880650/thumbnail?d=1737165723)](/attachment/image/4880650?d=1737165723)   

[0 ](javascript:void\(0\);) [3 ](javascript:void\(0\);)

  * [#254](/thread/post/15120270#post15120270 "Post Permalink")

  * Edited 6:35am  Jan 19, 2025 6:24am | Edited 6:35am 

  * [ CashBox](cashbox)

  * Joined Jun 2007 | Status: Trader | [933 Posts](/search?do=process&provider=Member&searchuser=41428)

> [Quoting driven18](/thread/post/15117026#post15117026 "View Quoted Post")
> 
> Disliked
> 
> This is more for Machine and other subs here.. Rick, I am going to use your chart(last time ![](https://resources.faireconomy.media/images/emojis/64/1f60e.png?v=15.1))..I will repost my below. 50% of my trading is happening on Limit Buy/Sell orders...your chart is perfect for this demonstration. Let the burst away from EMA 21 happen and then wait for retracement to value area(my name for it). I would recommend for more aggressive traders to come in on Full Position on Limit orders, no add ons, first trade on Limit Sell and second trade on Limit Buy. Second chart is my chart from yesterday - Blue circles would...
> 
> Ignored

Nice use of limit orders!!!  
I've been enjoying this thread.  
This is also a measured move set up.

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Measured Move off of the 20ma.JPG
Size: 96 KB](/attachment/image/4880855/thumbnail?d=1737235477)](/attachment/image/4880855?d=1737235477)   

[0 ](javascript:void\(0\);) [3 ](javascript:void\(0\);)

  * [#255](/thread/post/15120457#post15120457 "Post Permalink")

  * Jan 19, 2025 8:14pm  Jan 19, 2025 8:14pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1967050_1.gif) Ju4ara](ju4ara)

  * | Joined Oct 2024  | Status: Trader | [105 Posts](/search?do=process&provider=Member&searchuser=1967050)

Hi, I would like to show squeeze entry on btc/usdt 1H after vcp pattern the day before Trump inauguration which will cause bull run(imo). Is it good, or should it be drown as in second screenshot? 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 105 KB](/attachment/image/4880955/thumbnail?d=1737285038)](/attachment/image/4880955?d=1737285038)   
[![Click to Enlarge

Name: screenshot.png
Size: 104 KB](/attachment/image/4880957/thumbnail?d=1737285638)](/attachment/image/4880957?d=1737285638)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#256](/thread/post/15120466#post15120466 "Post Permalink")

  * Jan 19, 2025 9:06pm  Jan 19, 2025 9:06pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar426855_1.gif) RickM](rickm)

  * Joined Sep 2015 | Status: Trader | [2,439 Posts](/search?do=process&provider=Member&searchuser=426855)

> [Quoting Ju4ara](/thread/post/15120457#post15120457 "View Quoted Post")
> 
> Disliked
> 
> Hi, I would like to show squeeze entry on btc/usdt 1H after vcp pattern the day before Trump inauguration which will cause bull run(imo). Is it good, or should it be drown as in second screenshot? {image} {image}
> 
> Ignored

Hi Ju4ara  
  
Here is actually how I would trade this move (if I was trading).  
  
VCP Pattern + Squeeze on BTCUSD  
  
Skip the trend lines, 95% of retail traders use them and they lose.  
  
RULE 1.. There must be a Base low that shows strong rejection.  
RULE 2.. There must be a higher low (ignore wicks)  
RULE 3.. There must be a 3rd higher low that's sitting around the 21 EMA  
  
Entry is when this 3rd higher low moves away from the 21 EMA ..... just enter with your stop (If BTC / Stocks) below the Wick of the Base Low.  
  
  
So we are getting in early because we want to be in position to take advantage of any POP at breakout area.  
Breakout traders generally lose these days due to the high amount of Professional traders attacking breakout positions, at least if your in early you will still PROFIT.  
  
The idea here is this - WHO'S IN CONTROL, BUYERS or SELLERS.  
At my entry, I have enough evidence that Buyers are in control now.  
  
PS. Not a trade recommendation here only because its a SUNDAY and most professionals are not yet trading.  
PSPS. I have no evidence VOLUME is of much help on this setup, its a pure Price Action Pattern Only. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: BTC.png
Size: 139 KB](/attachment/image/4880967/thumbnail?d=1737288370)](/attachment/image/4880967?d=1737288370)   

Trading thin liquidity at the boundary of the charts

[0 ](javascript:void\(0\);) [3 ](javascript:void\(0\);)

  * [#257](/thread/post/15120475#post15120475 "Post Permalink")

  * Jan 19, 2025 9:31pm  Jan 19, 2025 9:31pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar426855_1.gif) RickM](rickm)

  * Joined Sep 2015 | Status: Trader | [2,439 Posts](/search?do=process&provider=Member&searchuser=426855)

> [Quoting CashBox](/thread/post/15120270#post15120270 "View Quoted Post")
> 
> Disliked
> 
> {quote} Nice use of limit orders!!! I've been enjoying this thread. This is also a measured move set up.{image}
> 
> Ignored

Hi CashBox  
  
Love your Art Work, and some nice points.  
Having Targets is something many traders like to use, and profit very well from them indeed.   
I use them for BTC and Stocks myself and do very well, but not fond of them on Futures or Forex.  
It’s just me.  
  
Cheers 

Trading thin liquidity at the boundary of the charts

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#258](/thread/post/15120482#post15120482 "Post Permalink")

  * Jan 19, 2025 9:50pm  Jan 19, 2025 9:50pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1967050_1.gif) Ju4ara](ju4ara)

  * | Joined Oct 2024  | Status: Trader | [105 Posts](/search?do=process&provider=Member&searchuser=1967050)

> [Quoting RickM](/thread/post/15120466#post15120466 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi Ju4ara Here is actually how I would trade this move (if I was trading). VCP Pattern + Squeeze on BTCUSD Skip the trend lines, 95% of retail traders use them and they lose. RULE 1.. There must be a Base low that shows strong rejection. RULE 2.. There must be a higher low (ignore wicks) RULE 3.. There must be a 3rd higher low that's sitting around the 21 EMA Entry is when this 3rd higher low moves away from the 21 EMA ..... just enter with your stop (If BTC / Stocks) below the Wick of the Base Low. So we are getting in early because we...
> 
> Ignored

Hi RickM, so would entry be like this? 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 103 KB](/attachment/image/4880974/thumbnail?d=1737291001)](/attachment/image/4880974?d=1737291001)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#259](/thread/post/15120841#post15120841 "Post Permalink")

  * Jan 20, 2025 1:24pm  Jan 20, 2025 1:24pm 

  * [ prestige09](prestige09)

  * | Joined Nov 2022  | Status: Trader | [14 Posts](/search?do=process&provider=Member&searchuser=1536799)

> [Quoting Merka](/thread/post/15118118#post15118118 "View Quoted Post")
> 
> Disliked
> 
> {quote} Do you find P&F charts useful in FX? Thanks
> 
> Ignored

Yes, P&F charts are incredibly versatile and can be used effectively in every market. They work well for both intraday and positional trading.  
**Why Do I Choose P &F Over Candlesticks?**

  1. **Less Noise:**  
In candlestick charts, there are two dimensions—**time** and **price**. During sideways markets, this dual-dimension setup can become very noisy and confusing. It’s challenging to read the market in such conditions, and I’ve found myself overtrading at times because of it, which leads to higher impact costs.  
With P&F charts, there’s only one dimension—**price**. A new box or column is created only when the price moves a specific amount. This means in sideways markets, you’ll see fewer setups, which helps to avoid overtrading.
  2. **Objective Patterns with Simplicity:**  
P&F charts offer very few patterns, and all of them are highly objective. This makes it easier to identify and trade them without confusion. Unlike some candlestick systems where multiple interpretations can lead to uncertainty, P&F patterns are straightforward and reliable.

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#260](/thread/post/15120931#post15120931 "Post Permalink")

  * Jan 20, 2025 3:39pm  Jan 20, 2025 3:39pm 

  * [ CashBox](cashbox)

  * Joined Jun 2007 | Status: Trader | [933 Posts](/search?do=process&provider=Member&searchuser=41428)

Here's a good walk through explaining the TTM squeeze indicator set ups:  

Inserted Video

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Squeeze n Go | MTF System
  *   * [ **Reply to Thread** ](/thread/1319487-squeeze-n-go-mtf-system/reply#reply)

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

[Spud's MTF FIB Breakout System](/thread/30109-spuds-mtf-fib-breakout-system "Spud's MTF FIB Breakout System 
-------------------------------- 
Ever since I learned about Fibonacci numbers they have interested my pure...") 375 replies

[H1Scalper System (MTF D1,H1,M5)](/thread/166646-h1scalper-system-mtf-d1h1m5 "Here are the indicators for a manual system. 
  
Explanations, rules and trading ideas are coming... 
. 
\(2009.05.13\) 
Attached are the...") 725 replies

[MTF Trix system](/thread/183801-mtf-trix-system "Hello everybody, 
 
This thread is for developing and discussing a multi-timeframe trading system that is based on one indicator - Trix -...") 3,697 replies

[MTF Stochastics into MTF Stoch Histogram](/thread/359918-mtf-stochastics-into-mtf-stoch-histogram "Hi, 
 
I have been trading with the help of MTF Stochastics for a few weeks now with relatively good results but would appreciate if...") 8 replies

[MTF Vajioo Scalping System](/thread/195912-mtf-vajioo-scalping-system "RUBBISH") 15 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/1319487-squeeze-n-go-mtf-system/reply#reply)
  * Subscribe
  * [216](javascript:void\(0\);)

Attachments: Squeeze n Go | MTF System

Tags: Squeeze n Go | MTF System

#  [](/thread/1319487-squeeze-n-go-mtf-system)Squeeze n Go | MTF System 

  * 

  * [#261](/thread/post/15120943#post15120943 "Post Permalink")

  * Jan 20, 2025 3:51pm  Jan 20, 2025 3:51pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar426855_1.gif) RickM](rickm)

  * Joined Sep 2015 | Status: Trader | [2,439 Posts](/search?do=process&provider=Member&searchuser=426855)

> [Quoting Ju4ara](/thread/post/15120482#post15120482 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi RickM, so would entry be like this? {image}
> 
> Ignored

Yes, around 103,800 and it when up to 106,420 before it got hit hard by Bearish Delta.   
  
I am not keen on trading BTC in the weekends because most pro's aren't there and anything can happen.  
It seems a better fix to go long in the 90's and go short over 100 at present. 

Trading thin liquidity at the boundary of the charts

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#262](/thread/post/15121447#post15121447 "Post Permalink")

  * Edited Jan 21, 2025 12:09am  Jan 20, 2025 11:36pm | Edited Jan 21, 2025 12:09am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1967050_1.gif) Ju4ara](ju4ara)

  * | Joined Oct 2024  | Status: Trader | [105 Posts](/search?do=process&provider=Member&searchuser=1967050)

> [Quoting RickM](/thread/post/15120943#post15120943 "View Quoted Post")
> 
> Disliked
> 
> {quote} Yes, around 103,800 and it when up to 106,420 before it got hit hard by Bearish Delta. I am not keen on trading BTC in the weekends because most pro's aren't there and anything can happen. It seems a better fix to go long in the 90's and go short over 100 at present.
> 
> Ignored

Hi RickM,  
Is this also a vcp pattern? Just want to learn the nature of it, I like how it works. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: IMG_1723.jpeg
Size: 585 KB](/attachment/image/4881625/thumbnail?d=1737385768)](/attachment/image/4881625?d=1737385768)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#263](/thread/post/15121522#post15121522 "Post Permalink")

  * Jan 21, 2025 12:16am  Jan 21, 2025 12:16am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar272159_71.gif) driven18](driven18)

  * Joined Jul 2012 | Status: Trader | [1,385 Posts](/search?do=process&provider=Member&searchuser=272159)

> [Quoting driven18](/thread/post/15120016#post15120016 "View Quoted Post")
> 
> Disliked
> 
> Dow Futures 5 Min TF. Sometimes you get stuck for the looooong(in America)weekend..traveling, just looked at my laptop...O, well..in profit +78 points, not too bad ![](https://resources.faireconomy.media/images/emojis/64/1f600.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f37a.png?v=15.1). Relevance: Under EMA 21 and intuition that people will be taking profits going into the long weekend, but under EMA 21, nevertheless. {image}
> 
> Ignored

To finish up on above trade, +82 points.   
  
O Well, Thank you Mr. Market! 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 15 KB](/attachment/image/4881630/thumbnail?d=1737386213)](/attachment/image/4881630?d=1737386213)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#264](/thread/post/15121526#post15121526 "Post Permalink")

  * Jan 21, 2025 12:22am  Jan 21, 2025 12:22am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar272159_71.gif) driven18](driven18)

  * Joined Jul 2012 | Status: Trader | [1,385 Posts](/search?do=process&provider=Member&searchuser=272159)

> [Quoting Ju4ara](/thread/post/15121447#post15121447 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi RickM, Is this also a vcp pattern? Just want to learn the nature of it, I like how it works. {image}
> 
> Ignored

While you wait for the answer from RickM, I say it as I see it: "What a horrible PA on this chart". You can pay me, I would never take that trade. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#265](/thread/post/15121575#post15121575 "Post Permalink")

  * Jan 21, 2025 1:02am  Jan 21, 2025 1:02am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1967050_1.gif) Ju4ara](ju4ara)

  * | Joined Oct 2024  | Status: Trader | [105 Posts](/search?do=process&provider=Member&searchuser=1967050)

> [Quoting driven18](/thread/post/15121526#post15121526 "View Quoted Post")
> 
> Disliked
> 
> {quote} While you wait for the answer from RickM, I say it as I see it: "What a horrible PA on this chart". You can pay me, I would never take that trade.
> 
> Ignored

Hi, that's why I said "just want to learn the nature of it". I wasn't going to take it, the point of question was getting advise about vcp pattern overall, but thanks for your comment, appreciate it. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#266](/thread/post/15122093#post15122093 "Post Permalink")

  * Jan 21, 2025 11:42am  Jan 21, 2025 11:42am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar426855_1.gif) RickM](rickm)

  * Joined Sep 2015 | Status: Trader | [2,439 Posts](/search?do=process&provider=Member&searchuser=426855)

> [Quoting Ju4ara](/thread/post/15121447#post15121447 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi RickM, Is this also a vcp pattern? Just want to learn the nature of it, I like how it works. {image}
> 
> Ignored

Hi Ju4ara  
  
A VCP pattern is only formed within a tight range - here we use a Bollinger Band Squeeze for this rule.  
  
Therefore start looking for areas of low volatility before we can find VCP patterns  
  
Cheers 

Trading thin liquidity at the boundary of the charts

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#267](/thread/post/15123048#post15123048 "Post Permalink")

  * Jan 22, 2025 12:55am  Jan 22, 2025 12:55am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar272159_71.gif) driven18](driven18)

  * Joined Jul 2012 | Status: Trader | [1,385 Posts](/search?do=process&provider=Member&searchuser=272159)

First 2 trades under my favorite President, respecting EMA 21.(under/over)  
  
She(Dow) did not know which way she wanted to go but we got her at the end.  
  
Relevance, I am helping to keep thread going, EMA 21 and a New USA President. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 20 KB](/attachment/image/4882501/thumbnail?d=1737474923)](/attachment/image/4882501?d=1737474923)   

[0 ](javascript:void\(0\);) [4 ](javascript:void\(0\);)

  * [#268](/thread/post/15123056#post15123056 "Post Permalink")

  * Jan 22, 2025 12:57am  Jan 22, 2025 12:57am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1967050_1.gif) Ju4ara](ju4ara)

  * | Joined Oct 2024  | Status: Trader | [105 Posts](/search?do=process&provider=Member&searchuser=1967050)

Hi, I guess this is a vcp pattern, but so choppy, would it be good entry? 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 107 KB](/attachment/image/4882507/thumbnail?d=1737475047)](/attachment/image/4882507?d=1737475047)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#269](/thread/post/15123062#post15123062 "Post Permalink")

  * Jan 22, 2025 1:00am  Jan 22, 2025 1:00am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar272159_71.gif) driven18](driven18)

  * Joined Jul 2012 | Status: Trader | [1,385 Posts](/search?do=process&provider=Member&searchuser=272159)

> [Quoting Ju4ara](/thread/post/15123056#post15123056 "View Quoted Post")
> 
> Disliked
> 
> Hi, I guess this is a vcp pattern, but so choppy, would it be good entry? {image}
> 
> Ignored

Not bad, as far the subject of the thread...I would be bullish here, but come in on Limit Buy. 

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#270](/thread/post/15123099#post15123099 "Post Permalink")

  * Jan 22, 2025 1:25am  Jan 22, 2025 1:25am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1967050_1.gif) Ju4ara](ju4ara)

  * | Joined Oct 2024  | Status: Trader | [105 Posts](/search?do=process&provider=Member&searchuser=1967050)

> [Quoting driven18](/thread/post/15123062#post15123062 "View Quoted Post")
> 
> Disliked
> 
> {quote} Not bad, as far the subject of the thread...I would be bullish here, but come in on Limit Buy.
> 
> Ignored

I took the trade, in profit now. I either wait for 5R profit or close the trade after price crosses 21EMA(I do take profit at 5R for not getting harmed psychologically). 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#271](/thread/post/15124279#post15124279 "Post Permalink")

  * Jan 22, 2025 11:03pm  Jan 22, 2025 11:03pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1967050_1.gif) Ju4ara](ju4ara)

  * | Joined Oct 2024  | Status: Trader | [105 Posts](/search?do=process&provider=Member&searchuser=1967050)

Another vcp pattern with squeeze entry, correct me if I'm wrong.  
EDIT: Lost full position on this one. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 103 KB](/attachment/image/4883308/thumbnail?d=1737554578)](/attachment/image/4883308?d=1737554578)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#272](/thread/post/15124549#post15124549 "Post Permalink")

  * Jan 23, 2025 1:40am  Jan 23, 2025 1:40am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1967050_1.gif) Ju4ara](ju4ara)

  * | Joined Oct 2024  | Status: Trader | [105 Posts](/search?do=process&provider=Member&searchuser=1967050)

Went to smoke and skipped this nice trade ;( 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 100 KB](/attachment/image/4883449/thumbnail?d=1737563998)](/attachment/image/4883449?d=1737563998)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#273](/thread/post/15124820#post15124820 "Post Permalink")

  * Jan 23, 2025 6:30am  Jan 23, 2025 6:30am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar588299_3.gif) RiskFighter](riskfighter)

  * Joined Jun 2017 | Status: Trader | [1,566 Posts](/search?do=process&provider=Member&searchuser=588299) | Online Now 

Yes smoking is expensive. 

Read post #1 !! Then read it again 10 more times before you ask.

[0 ](javascript:void\(0\);) [4 ](javascript:void\(0\);)

  * [#274](/thread/post/15125252#post15125252 "Post Permalink")

  * Jan 23, 2025 6:34pm  Jan 23, 2025 6:34pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1967050_1.gif) Ju4ara](ju4ara)

  * | Joined Oct 2024  | Status: Trader | [105 Posts](/search?do=process&provider=Member&searchuser=1967050)

lost in London session 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 101 KB](/attachment/image/4883849/thumbnail?d=1737624871)](/attachment/image/4883849?d=1737624871)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#275](/thread/post/15125405#post15125405 "Post Permalink")

  * Jan 23, 2025 8:23pm  Jan 23, 2025 8:23pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar426855_1.gif) RickM](rickm)

  * Joined Sep 2015 | Status: Trader | [2,439 Posts](/search?do=process&provider=Member&searchuser=426855)

> [Quoting Ju4ara](/thread/post/15125252#post15125252 "View Quoted Post")
> 
> Disliked
> 
> lost in London session {image}
> 
> Ignored

Hi Ju4ara  
  
I'm actually trading that Market presently (ES not CFD), can I give you my view.  
AND of course its a historical chart so its easy for me to an expert after the fact -  
  
The Squeeze occurred 18 bars earlier.  
When I saw a Squeeze of a 4-5 bars, I go back and look for a rejection move.  
1 - Rejection  
2- Retest with a lower low (not prefect but good enough)  
3- Now I want to trade this Third move down from the EMA 21.  
  
I also want 1 - 2 - 3 to be close together which they were.  
What do you think of this setup, I don't see a setup in your Trade because NO SQUEEZE (at least a few bars min).  
  
I always place a BE Stop once it leaves and only use the EMA 21 once its move a reasonable distance.  
I only starting trading around the time you took the trade so miss my setup. On ES, Profit would be around 15 Ticks.  
Nothing great but still a nice start to the day. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: vvv.png
Size: 110 KB](/attachment/image/4883935/thumbnail?d=1737631372)](/attachment/image/4883935?d=1737631372)   

Trading thin liquidity at the boundary of the charts

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#276](/thread/post/15125607#post15125607 "Post Permalink")

  * Jan 23, 2025 11:04pm  Jan 23, 2025 11:04pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1967050_1.gif) Ju4ara](ju4ara)

  * | Joined Oct 2024  | Status: Trader | [105 Posts](/search?do=process&provider=Member&searchuser=1967050)

> [Quoting RickM](/thread/post/15125405#post15125405 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi Ju4ara I'm actually trading that Market presently (ES not CFD), can I give you my view. AND of course its a historical chart so its easy for me to an expert after the fact - The Squeeze occurred 18 bars earlier. When I saw a Squeeze of a 4-5 bars, I go back and look for a rejection move. 1 - Rejection 2- Retest with a lower low (not prefect but good enough) 3- Now I want to trade this Third move down from the EMA 21. I also want 1 - 2 - 3 to be close together which they were. What do you think of this setup, I don't see a setup in your...
> 
> Ignored

Hi RickM  
Glad to see your reply, it's the only way I learn something new about squeezes. Could you, please, explain why you looked for rejection before squeeze, waited for retest with lower low and only then entered. Also, there was squeeze on my screenshot with 3 candle duration, isn't that enough?  
  
P.S. you said about BE SL, how many candles or distance you wait before placing that stop?  
Thanks in advance. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#277](/thread/post/15125942#post15125942 "Post Permalink")

  * Jan 24, 2025 2:21am  Jan 24, 2025 2:21am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

What about this setup from earlier this month? Maybe not A+ because price pulled back a little further than ideal on the third leg, but you can see price exploded shortly after the setup. High compression squeeze started nice and early and released with Momentum. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot_20250123_121725_Photos.jpg
Size: 355 KB](/attachment/image/4884259/thumbnail?d=1737652653)](/attachment/image/4884259?d=1737652653)   

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#278](/thread/post/15125981#post15125981 "Post Permalink")

  * Jan 24, 2025 2:50am  Jan 24, 2025 2:50am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1967050_1.gif) Ju4ara](ju4ara)

  * | Joined Oct 2024  | Status: Trader | [105 Posts](/search?do=process&provider=Member&searchuser=1967050)

One more setup occurred on dow 2M, I don’t trade this time tho. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: IMG_1731.png
Size: 93 KB](/attachment/image/4884285/thumbnail?d=1737654652)](/attachment/image/4884285?d=1737654652)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#279](/thread/post/15125989#post15125989 "Post Permalink")

  * Jan 24, 2025 3:00am  Jan 24, 2025 3:00am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1967050_1.gif) Ju4ara](ju4ara)

  * | Joined Oct 2024  | Status: Trader | [105 Posts](/search?do=process&provider=Member&searchuser=1967050)

> [Quoting MachineLearn](/thread/post/15125942#post15125942 "View Quoted Post")
> 
> Disliked
> 
> What about this setup from earlier this month? Maybe not A+ because price pulled back a little further than ideal on the third leg, but you can see price exploded shortly after the setup. High compression squeeze started nice and early and released with Momentum. {image}
> 
> Ignored

Seems nice to me, but there was no signal to enter before break of resistance, then it would be A+ I guess. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#280](/thread/post/15126180#post15126180 "Post Permalink")

  * Jan 24, 2025 6:50am  Jan 24, 2025 6:50am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

I like thus setup. Multiple bounces off a strong resistance area. Diamonds signaling retests. Buyers absorbed? Then price starts to enter a high compression squeeze , after squeezing for a bit. VCP pattern appearing now as well and I would expect an explosive move soon.  
  
I like to wait for a release personally.  
  
You can see a couple strong support zones below that we could use at TP, which we would create a great RR assuming price breaks to the downside. 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: Screenshot_20250123_165129_Photos.jpg
Size: 258 KB](/attachment/image/4884379/thumbnail?d=1737669099)](/attachment/image/4884379?d=1737669099)   
[![Click to Enlarge

Name: Screenshot_20250123_165257_Photos.jpg
Size: 264 KB](/attachment/image/4884380/thumbnail?d=1737669188)](/attachment/image/4884380?d=1737669188)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Squeeze n Go | MTF System
  *   * [ **Reply to Thread** ](/thread/1319487-squeeze-n-go-mtf-system/reply#reply)

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

[Spud's MTF FIB Breakout System](/thread/30109-spuds-mtf-fib-breakout-system "Spud's MTF FIB Breakout System 
-------------------------------- 
Ever since I learned about Fibonacci numbers they have interested my pure...") 375 replies

[H1Scalper System (MTF D1,H1,M5)](/thread/166646-h1scalper-system-mtf-d1h1m5 "Here are the indicators for a manual system. 
  
Explanations, rules and trading ideas are coming... 
. 
\(2009.05.13\) 
Attached are the...") 725 replies

[MTF Trix system](/thread/183801-mtf-trix-system "Hello everybody, 
 
This thread is for developing and discussing a multi-timeframe trading system that is based on one indicator - Trix -...") 3,697 replies

[MTF Stochastics into MTF Stoch Histogram](/thread/359918-mtf-stochastics-into-mtf-stoch-histogram "Hi, 
 
I have been trading with the help of MTF Stochastics for a few weeks now with relatively good results but would appreciate if...") 8 replies

[MTF Vajioo Scalping System](/thread/195912-mtf-vajioo-scalping-system "RUBBISH") 15 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/1319487-squeeze-n-go-mtf-system/reply#reply)
  * Subscribe
  * [216](javascript:void\(0\);)

Attachments: Squeeze n Go | MTF System

Tags: Squeeze n Go | MTF System

#  [](/thread/1319487-squeeze-n-go-mtf-system)Squeeze n Go | MTF System 

  * 

  * [#281](/thread/post/15126190#post15126190 "Post Permalink")

  * Jan 24, 2025 7:03am  Jan 24, 2025 7:03am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

Almost like I can see the future ![](https://resources.faireconomy.media/images/emojis/64/1f602.png?v=15.1), moments later we get an aggressive more to the downside. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot_20250123_170209_Photos.jpg
Size: 298 KB](/attachment/image/4884381/thumbnail?d=1737669743)](/attachment/image/4884381?d=1737669743)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#282](/thread/post/15126200#post15126200 "Post Permalink")

  * Jan 24, 2025 7:11am  Jan 24, 2025 7:11am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

> [Quoting MachineLearn](/thread/post/15126190#post15126190 "View Quoted Post")
> 
> Disliked
> 
> Almost like I can see the future ![](https://resources.faireconomy.media/images/emojis/64/1f602.png?v=15.1), moments later we get an aggressive more to the downside. {image}
> 
> Ignored

Followed by another one ![](https://resources.faireconomy.media/images/emojis/64/1f633.png?v=15.1)  
  
Even elif we entered after the first explosive move there is still pips to gain from the second one.  
  
Now here's where it gets tough...do we assume that there's enough momentum to break to new lows or do you take your money and run. I would say from observing the squeeze we had to the left which was relatively substantial with tons of buying absorbed, this might be worth sticking around for better RR with a SL moved to BE? 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot_20250123_170735_Photos.jpg
Size: 317 KB](/attachment/image/4884386/thumbnail?d=1737670071)](/attachment/image/4884386?d=1737670071)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#283](/thread/post/15126252#post15126252 "Post Permalink")

  * Jan 24, 2025 8:47am  Jan 24, 2025 8:47am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar272159_71.gif) driven18](driven18)

  * Joined Jul 2012 | Status: Trader | [1,385 Posts](/search?do=process&provider=Member&searchuser=272159)

> [Quoting MachineLearn](/thread/post/15126200#post15126200 "View Quoted Post")
> 
> Disliked
> 
> {quote} Followed by another one ![](https://resources.faireconomy.media/images/emojis/64/1f633.png?v=15.1) Even elif we entered after the first explosive move there is still pips to gain from the second one. Now here's where it gets tough...**do we assume that there's enough momentum to break to new lows or do you take your money and run.** I would say from observing the squeeze we had to the left which was relatively substantial with tons of buying absorbed, this might be worth sticking around for better RR with a SL moved to BE? {image}
> 
> Ignored

There is nothing to assume, every trade is different, you know my mantra - Entries are just 10% of the whole business.  
  
At times if I am "wrong"(I do not believe in this word when it comes to trading.), I can still make money properly managing a trade.  
  
**Start moving towards the other 90% of the business, Money Management(40%), Controlling MindFuck(Fear and Greed)(50%)**

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#284](/thread/post/15126316#post15126316 "Post Permalink")

  * Edited 11:20am  Jan 24, 2025 10:53am | Edited 11:20am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

This is ready to go, but which way. PA isn't the best.  
  
More sellers absorbed, more touches, maybe a pop to the upside.  
  
I'm considering a LIMIT in the breakout zone 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot_20250123_205241_Photos.jpg
Size: 311 KB](/attachment/image/4884474/thumbnail?d=1737683574)](/attachment/image/4884474?d=1737683574)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#285](/thread/post/15126332#post15126332 "Post Permalink")

  * Jan 24, 2025 11:16am  Jan 24, 2025 11:16am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

> [Quoting MachineLearn](/thread/post/15126316#post15126316 "View Quoted Post")
> 
> Disliked
> 
> This is ready to go, but which way. PA isn't the best. More sellers absorbed, more touches, maybe a pop to the upside. I'm considering a LIMIT in the breakout zone {image}
> 
> Ignored

WOAH, I can see the future now ![](https://resources.faireconomy.media/images/emojis/64/1f61c.png?v=15.1)  
  
There's no doubt the squeeze is powerful. Place a limit above or below the breakout zone with a tight stop and you'll make money  
  
Was ready for this one this time 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: Screenshot_20250123_211622_Photos.jpg
Size: 219 KB](/attachment/image/4884481/thumbnail?d=1737685009)](/attachment/image/4884481?d=1737685009)   
[![Click to Enlarge

Name: Screenshot_20250123_211746_TradingView.jpg
Size: 51 KB](/attachment/image/4884483/thumbnail?d=1737685077)](/attachment/image/4884483?d=1737685077)   

[0 ](javascript:void\(0\);) [4 ](javascript:void\(0\);)

  * [#286](/thread/post/15126398#post15126398 "Post Permalink")

  * Jan 24, 2025 12:39pm  Jan 24, 2025 12:39pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar588299_3.gif) RiskFighter](riskfighter)

  * Joined Jun 2017 | Status: Trader | [1,566 Posts](/search?do=process&provider=Member&searchuser=588299) | Online Now 

> [Quoting driven18](/thread/post/15126252#post15126252 "View Quoted Post")
> 
> Disliked
> 
> {quote} There is nothing to assume, every trade is different, you know my mantra - Entries are just 10% of the whole business. At times if I am "wrong"(I do not believe in this word when it comes to trading.), I can still make money properly managing a trade. Start moving towards the other 90% of the business, Money Management(40%), Controlling MindFuck(Fear and Greed)(50%)
> 
> Ignored

How do you make money if you are wrong? Are you using a very low reward compared to risk? Or a very quick break even? Or ???? 

Read post #1 !! Then read it again 10 more times before you ask.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#287](/thread/post/15126423#post15126423 "Post Permalink")

  * Jan 24, 2025 1:16pm  Jan 24, 2025 1:16pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar272159_71.gif) driven18](driven18)

  * Joined Jul 2012 | Status: Trader | [1,385 Posts](/search?do=process&provider=Member&searchuser=272159)

> [Quoting RiskFighter](/thread/post/15126398#post15126398 "View Quoted Post")
> 
> Disliked
> 
> {quote} How do you make money if you are wrong? Are you using a very low reward compared to risk? Or a very quick break even? Or ????
> 
> Ignored

Money Management is not taught skill, after years of monitoring your personal behaviors and feelings, it is up to individual trader to decide how much pressure he/she can handle when "wrong" trade does not go traders direction or how much guts trader has to stay in the trade all the way to TP. 

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#288](/thread/post/15126426#post15126426 "Post Permalink")

  * Jan 24, 2025 1:17pm  Jan 24, 2025 1:17pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

Could be a good bet here 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot_20250123_231652_Photos.jpg
Size: 270 KB](/attachment/image/4884553/thumbnail?d=1737692249)](/attachment/image/4884553?d=1737692249)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#289](/thread/post/15126900#post15126900 "Post Permalink")

  * Jan 24, 2025 8:52pm  Jan 24, 2025 8:52pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1967050_1.gif) Ju4ara](ju4ara)

  * | Joined Oct 2024  | Status: Trader | [105 Posts](/search?do=process&provider=Member&searchuser=1967050)

hi guys,  
I have an issue, soon I will move and will only be able to trade during London session only, but last 3 days I watch and there are no great entry opportunities in first 3 hours of london open. I trade us30, us500 and gold. I understand that these markets work best on new york open, but could you give me an advice on what should I do? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#290](/thread/post/15126913#post15126913 "Post Permalink")

  * Jan 24, 2025 9:04pm  Jan 24, 2025 9:04pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar426855_1.gif) RickM](rickm)

  * Joined Sep 2015 | Status: Trader | [2,439 Posts](/search?do=process&provider=Member&searchuser=426855)

> [Quoting Ju4ara](/thread/post/15125607#post15125607 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi RickM Glad to see your reply, it's the only way I learn something new about squeezes. Could you, please, explain why you looked for rejection before squeeze, waited for retest with lower low and only then entered. Also, there was squeeze on my screenshot with 3 candle duration, isn't that enough? P.S. you said about BE SL, how many candles or distance you wait before placing that stop? Thanks in advance.
> 
> Ignored

Hi Ju4ara  
  
The Squeeze Indicator works when the Bollinger Bands slip inside the Keltner Channel as you know. But as they are lagging indicators, the Squeeze had actually started a few bars earlier if you look at the chart. Therefore I looked LEFT to see if there was any Rejection Candle already in a tight range - and saw the setup.  
  
The problem with John Carters Setup is it's late to the party at both ends. Meaning the PA is already in Consolidation before the RED dots appear and the signal to trade is often a few bars too late AFTER BREAKOUT has occurred. Therefore many traders like myself feel the 21EMA is a better SIGNAL to trade than waiting for the dots to turn Black or Green. The VCP Pattern over rides the Squeeze signals for me where I am looking for a 1 - 2 - 3 pullback then enter as long as price starts from a consolidation area.  
  
Its how I do it - but the basic's of the SQUEEZE setup is still good and valid so find your own edge hat works for you.  
For a Stop, I really want 10 Ticks or more on ES (US 500) so I use a BE Stop until I feel I will get at least that amount.  
10 Ticks on ES is worth about $115 Profit on 1 Contract.   
  
Cheers 

Trading thin liquidity at the boundary of the charts

[0 ](javascript:void\(0\);) [3 ](javascript:void\(0\);)

  * [#291](/thread/post/15126924#post15126924 "Post Permalink")

  * Jan 24, 2025 9:14pm  Jan 24, 2025 9:14pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1967050_1.gif) Ju4ara](ju4ara)

  * | Joined Oct 2024  | Status: Trader | [105 Posts](/search?do=process&provider=Member&searchuser=1967050)

Oh, so that also was a vcp pattern there, it was barely seen, that’s why I missed that point, now I understand why you looked for rejection few bars before. So you wait for at least 10ticks in profit before setting sl to BE? 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#292](/thread/post/15126971#post15126971 "Post Permalink")

  * Jan 24, 2025 9:53pm  Jan 24, 2025 9:53pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

> [Quoting MachineLearn](/thread/post/15126426#post15126426 "View Quoted Post")
> 
> Disliked
> 
> Could be a good bet here {image}
> 
> Ignored

That's 3 in a row, with the limit setup I can catch these impulsive moves. The accuracy and volatility is A1 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: Screenshot_20250124_075221_Photos.jpg
Size: 225 KB](/attachment/image/4884854/thumbnail?d=1737723212)](/attachment/image/4884854?d=1737723212)   
[![Click to Enlarge

Name: Screenshot_20250124_075254_TradingView.jpg
Size: 51 KB](/attachment/image/4884855/thumbnail?d=1737723212)](/attachment/image/4884855?d=1737723212)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#293](/thread/post/15127196#post15127196 "Post Permalink")

  * Jan 24, 2025 11:58pm  Jan 24, 2025 11:58pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

Had this level marked before the spike down, definitely an area of interest. Waiting before setting limit, want to see some more absorbtion, or see the squeeze become highly compressed.  
  
If I did set limit I wouldn't target very far  
  
Edit - squeeze is currently bouncing between highly compressed and normal compression, still waiting 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot_20250124_095610_Photos.jpg
Size: 349 KB](/attachment/image/4884976/thumbnail?d=1737730614)](/attachment/image/4884976?d=1737730614)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#294](/thread/post/15127236#post15127236 "Post Permalink")

  * Jan 25, 2025 12:20am  Jan 25, 2025 12:20am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

> [Quoting MachineLearn](/thread/post/15127196#post15127196 "View Quoted Post")
> 
> Disliked
> 
> Had this level marked before the spike down, definitely an area of interest. Waiting before setting limit, want to see some more absorbtion, or see the squeeze become highly compressed. If I did set limit I wouldn't target very far Edit - squeeze is currently bouncing between highly compressed and normal compression, still waiting {image}
> 
> Ignored

Annnnd there's the drop, 4/4 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot_20250124_102025_Photos.jpg
Size: 551 KB](/attachment/image/4884991/thumbnail?d=1737732046)](/attachment/image/4884991?d=1737732046)   

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#295](/thread/post/15127250#post15127250 "Post Permalink")

  * Jan 25, 2025 12:30am  Jan 25, 2025 12:30am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

Watching  
  
EDIT - Took a small position 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot_20250124_102950_Photos.jpg
Size: 278 KB](/attachment/image/4885008/thumbnail?d=1737732601)](/attachment/image/4885008?d=1737732601)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#296](/thread/post/15127265#post15127265 "Post Permalink")

  * Jan 25, 2025 12:37am  Jan 25, 2025 12:37am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

> [Quoting MachineLearn](/thread/post/15127250#post15127250 "View Quoted Post")
> 
> Disliked
> 
> Watching EDIT - Took a small position {image}
> 
> Ignored

Very small position but right again. Price pushed right down to our target area 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot_20250124_103705_Photos.jpg
Size: 396 KB](/attachment/image/4885013/thumbnail?d=1737733040)](/attachment/image/4885013?d=1737733040)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#297](/thread/post/15127295#post15127295 "Post Permalink")

  * Edited 1:13am  Jan 25, 2025 12:57am | Edited 1:13am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot_20250124_111344_Photos.jpg
Size: 291 KB](/attachment/image/4885051/thumbnail?d=1737735236)](/attachment/image/4885051?d=1737735236)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#298](/thread/post/15127365#post15127365 "Post Permalink")

  * Jan 25, 2025 1:55am  Jan 25, 2025 1:55am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

> [Quoting driven18](/thread/post/15126423#post15126423 "View Quoted Post")
> 
> Disliked
> 
> {quote} Money Management is not taught skill, after years of monitoring your personal behaviors and feelings, it is up to individual trader to decide how much pressure he/she can handle when "wrong" trade does not go traders direction or how much guts trader has to stay in the trade all the way to TP.
> 
> Ignored

From a verified instutional trading desk employee   
  
What "edge" or model gives retail the best chance?  
  
While I can't give you a prescriptive answer here, I will suggest what my past response is: identify different market regimes... once you identify a regime (ex. Trump bull run, pandemic black swan event, rising inflation, MBS imbalance, yield inversions, etc) find or create a trading strategy that can be profitable.  
  
I will openly share how I approach trading here I break it down like this:  
\- 10% Signal Generation (this is the strategy used, in the case of retail the 50 EMA Crossover, or whatever the signal is)  
  
-30% Risk Management (determining where to enter, stop out, add to a winner, or peel off a position)  
  
-60% Psychology (some professionals call this a sham and I understand where they are coming from, but the idea is... most retail come into trading from nothing. This aspect is one of the reasons I love the industry, because it allows you to meritoriously earn based on your capacity. However, the harsh reality I have seen: I have given my signals/RNN output to many retail traders and even though the system generates perfect to the tick entries and exits, they will still fail. They allow scarcity mindset, greed, FOMO, whatever emotion you want to take over. This is one of the largest reasons I recommend retail try their best to code their strategies to make execution as rule based, as possible. Why do you think institutions do it? 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#299](/thread/post/15127366#post15127366 "Post Permalink")

  * Jan 25, 2025 1:56am  Jan 25, 2025 1:56am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

"I am sure you have heard the cliche, "the market will always be there tomorrow". When was the last time you understood: the market tomorrow is not the market today, and the market the day after is not the market tomorrow?  
**Unfortunately, the largest issue I see with retail that manage to escape from the consistent grind to _finding the Holy Grail_** (those that chase guru to guru, or strategy to strategy) only remain profitable in certain regimes. They are never able to create multiple strategies, that work in multiple market regimes, and *most importantly* efficiently deploy the correct strategy in the correct regime. This requires time and experience."  
  
![](https://resources.faireconomy.media/images/emojis/64/1f974.png?v=15.1)

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#300](/thread/post/15127373#post15127373 "Post Permalink")

  * Jan 25, 2025 2:03am  Jan 25, 2025 2:03am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar272159_71.gif) driven18](driven18)

  * Joined Jul 2012 | Status: Trader | [1,385 Posts](/search?do=process&provider=Member&searchuser=272159)

> [Quoting MachineLearn](/thread/post/15127365#post15127365 "View Quoted Post")
> 
> Disliked
> 
> {quote} From a verified instutional trading desk employee What "edge" or model gives retail the best chance? While I can't give you a prescriptive answer here, I will suggest what my past response is: identify different market regimes... once you identify a regime (ex. Trump bull run, pandemic black swan event, rising inflation, MBS imbalance, yield inversions, etc) find or create a trading strategy that can be profitable. I will openly share how I approach trading here I break it down like this: - 10% Signal Generation (this is the strategy used,...
> 
> Ignored

**Exactly what I been telling you. Read my posts one more time.**  
  
I am up **+15% for the month** and will not be trading this month anymore.  
  

  

  
During last year, I believe I "paid back" to certain individuals with my knowledge and experience.   
  
Good Luck with ALL to ALL! ![](https://resources.faireconomy.media/images/emojis/64/1f4b0.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f604.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f37a.png?v=15.1)

[0 ](javascript:void\(0\);) [4 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Squeeze n Go | MTF System
  *   * [ **Reply to Thread** ](/thread/1319487-squeeze-n-go-mtf-system/reply#reply)

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

[Spud's MTF FIB Breakout System](/thread/30109-spuds-mtf-fib-breakout-system "Spud's MTF FIB Breakout System 
-------------------------------- 
Ever since I learned about Fibonacci numbers they have interested my pure...") 375 replies

[H1Scalper System (MTF D1,H1,M5)](/thread/166646-h1scalper-system-mtf-d1h1m5 "Here are the indicators for a manual system. 
  
Explanations, rules and trading ideas are coming... 
. 
\(2009.05.13\) 
Attached are the...") 725 replies

[MTF Trix system](/thread/183801-mtf-trix-system "Hello everybody, 
 
This thread is for developing and discussing a multi-timeframe trading system that is based on one indicator - Trix -...") 3,697 replies

[MTF Stochastics into MTF Stoch Histogram](/thread/359918-mtf-stochastics-into-mtf-stoch-histogram "Hi, 
 
I have been trading with the help of MTF Stochastics for a few weeks now with relatively good results but would appreciate if...") 8 replies

[MTF Vajioo Scalping System](/thread/195912-mtf-vajioo-scalping-system "RUBBISH") 15 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/1319487-squeeze-n-go-mtf-system/reply#reply)
  * Subscribe
  * [216](javascript:void\(0\);)

Attachments: Squeeze n Go | MTF System

Tags: Squeeze n Go | MTF System

#  [](/thread/1319487-squeeze-n-go-mtf-system)Squeeze n Go | MTF System 

  * 

  * [#301](/thread/post/15127392#post15127392 "Post Permalink")

  * Jan 25, 2025 2:29am  Jan 25, 2025 2:29am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

Is set for lift off 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot_20250124_122420_Photos.jpg
Size: 275 KB](/attachment/image/4885087/thumbnail?d=1737739771)](/attachment/image/4885087?d=1737739771)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#302](/thread/post/15127538#post15127538 "Post Permalink")

  * Jan 25, 2025 6:27am  Jan 25, 2025 6:27am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1967050_1.gif) Ju4ara](ju4ara)

  * | Joined Oct 2024  | Status: Trader | [105 Posts](/search?do=process&provider=Member&searchuser=1967050)

> [Quoting MachineLearn](/thread/post/15127365#post15127365 "View Quoted Post")
> 
> Disliked
> 
> {quote} From a verified instutional trading desk employee What "edge" or model gives retail the best chance? While I can't give you a prescriptive answer here, I will suggest what my past response is: identify different market regimes... once you identify a regime (ex. Trump bull run, pandemic black swan event, rising inflation, MBS imbalance, yield inversions, etc) find or create a trading strategy that can be profitable. I will openly share how I approach trading here I break it down like this: - 10% Signal Generation (this is the strategy used,...
> 
> Ignored

Still have problem with self control(psychology), that’s why I’m still not in profit, don’t know how to fix it. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#303](/thread/post/15127543#post15127543 "Post Permalink")

  * Jan 25, 2025 6:37am  Jan 25, 2025 6:37am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

> [Quoting Ju4ara](/thread/post/15127538#post15127538 "View Quoted Post")
> 
> Disliked
> 
> {quote} Still have problem with self control(psychology), that’s why I’m still not in profit, don’t know how to fix it.
> 
> Ignored

Once your trade parameters are set I would recommend walking away and letting your SL and TP do what you set them to do.   
  
It also helps to have good RR, because psychologically it's much easier to stomach a loss when you know your wins are 3X more profit. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#304](/thread/post/15127555#post15127555 "Post Permalink")

  * Jan 25, 2025 7:00am  Jan 25, 2025 7:00am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1967050_1.gif) Ju4ara](ju4ara)

  * | Joined Oct 2024  | Status: Trader | [105 Posts](/search?do=process&provider=Member&searchuser=1967050)

> [Quoting MachineLearn](/thread/post/15127543#post15127543 "View Quoted Post")
> 
> Disliked
> 
> {quote} Once your trade parameters are set I would recommend walking away and letting your SL and TP do what you set them to do. It also helps to have good RR, because psychologically it's much easier to stomach a loss when you know your wins are 3X more profit.
> 
> Ignored

That’s why I trade this strategy for 5R. Still working on myself because sometimes I do something I shouldn’t do. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#305](/thread/post/15127564#post15127564 "Post Permalink")

  * Jan 25, 2025 7:21am  Jan 25, 2025 7:21am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

> [Quoting MachineLearn](/thread/post/15127392#post15127392 "View Quoted Post")
> 
> Disliked
> 
> Is set for lift off {image}
> 
> Ignored

Called it again, been waiting for this all day. 5/5?  
  
Limit set below trend break for easy trade 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot_20250124_172107_Photos.jpg
Size: 333 KB](/attachment/image/4885179/thumbnail?d=1737757287)](/attachment/image/4885179?d=1737757287)   

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#306](/thread/post/15127569#post15127569 "Post Permalink")

  * Edited 7:51am  Jan 25, 2025 7:37am | Edited 7:51am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

No limit set , but curious too see what kind squeeze appears here and if more buyers are absorbed.  
  
Conversely seems like a bullish vcp is simulataneously setting up too (kind of)  
  
Check back on market open 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: Screenshot_20250124_173531_Photos.jpg
Size: 349 KB](/attachment/image/4885180/thumbnail?d=1737758178)](/attachment/image/4885180?d=1737758178)   
[![Click to Enlarge

Name: Screenshot_20250124_173753_Photos.jpg
Size: 295 KB](/attachment/image/4885183/thumbnail?d=1737758305)](/attachment/image/4885183?d=1737758305)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#307](/thread/post/15127624#post15127624 "Post Permalink")

  * Jan 25, 2025 11:26am  Jan 25, 2025 11:26am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar426855_1.gif) RickM](rickm)

  * Joined Sep 2015 | Status: Trader | [2,439 Posts](/search?do=process&provider=Member&searchuser=426855)

> [Quoting driven18](/thread/post/15127373#post15127373 "View Quoted Post")
> 
> Disliked
> 

> 
> Ignored

Hi Driven  
  

When I came back last time, I set myself a limit of only creating a post if it can be done under 10 minutes.  
  
I would say there's many setups I have missed because I was reading FF and NOT CONCENTRATING.   
Personally I need to scale back my time here sometime soon. 

Trading thin liquidity at the boundary of the charts

[0 ](javascript:void\(0\);) [4 ](javascript:void\(0\);)

  * [#308](/thread/post/15127639#post15127639 "Post Permalink")

  * Jan 25, 2025 12:31pm  Jan 25, 2025 12:31pm 

  * [ CashBox](cashbox)

  * Joined Jun 2007 | Status: Trader | [933 Posts](/search?do=process&provider=Member&searchuser=41428)

Yes, RickM, we keep coming back. I try to only be here on weekends/holidays and skip months at a time unless I find an interesting thread to check in on. 

[0 ](javascript:void\(0\);) [3 ](javascript:void\(0\);)

  * [#309](/thread/post/15127640#post15127640 "Post Permalink")

  * Jan 25, 2025 12:41pm  Jan 25, 2025 12:41pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

IMO you guys aren't on forex factory enough ![](https://resources.faireconomy.media/images/emojis/64/1f602.png?v=15.1)   
  
No seriously, between FF and Trading, your life can get consumed.  
  
Stay healthy friends. 

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#310](/thread/post/15127778#post15127778 "Post Permalink")

  * Jan 25, 2025 9:16pm  Jan 25, 2025 9:16pm 

  * [ pray4pips](pray4pips)

  * | Joined Nov 2024  | Status: Trader | [16 Posts](/search?do=process&provider=Member&searchuser=1996382)

> [Quoting RickM](/thread/post/15126913#post15126913 "View Quoted Post")
> 
> Disliked
> 
> {quote} The VCP Pattern over rides the Squeeze signals for me
> 
> Ignored

What does VCP stand for? Thanks 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#311](/thread/post/15127811#post15127811 "Post Permalink")

  * Edited 11:13pm  Jan 25, 2025 10:42pm | Edited 11:13pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar272159_71.gif) driven18](driven18)

  * Joined Jul 2012 | Status: Trader | [1,385 Posts](/search?do=process&provider=Member&searchuser=272159)

> [Quoting RickM](/thread/post/15127624#post15127624 "View Quoted Post")
> 
> Disliked
> 

> 
> Ignored

O My! I am glad I posted "may decide". So it is a "mindfuck" of its own. Thanks for heads up RickM.![](https://resources.faireconomy.media/images/emojis/64/1f600.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f600.png?v=15.1)

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#312](/thread/post/15127851#post15127851 "Post Permalink")

  * Jan 26, 2025 1:10am  Jan 26, 2025 1:10am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

BTC entered a high compression squeeze and heavy resistance around Christmas, then exploded down and never looked back.  
  
Then a few days later, did it again 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot_20250125_111118_Photos.jpg
Size: 314 KB](/attachment/image/4885397/thumbnail?d=1737821505)](/attachment/image/4885397?d=1737821505)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#313](/thread/post/15128086#post15128086 "Post Permalink")

  * Jan 26, 2025 3:30pm  Jan 26, 2025 3:30pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar426855_1.gif) RickM](rickm)

  * Joined Sep 2015 | Status: Trader | [2,439 Posts](/search?do=process&provider=Member&searchuser=426855)

> [Quoting Ju4ara](/thread/post/15126900#post15126900 "View Quoted Post")
> 
> Disliked
> 
> hi guys, I have an issue, soon I will move and will only be able to trade during London session only, but last 3 days I watch and there are no great entry opportunities in first 3 hours of london open. I trade us30, us500 and gold. I understand that these markets work best on new york open, but could you give me an advice on what should I do?
> 
> Ignored

Hi Ju  
  
I mostly trade London where I focus on ES / NQ / Gold & Oil Futures so I am in the same situation as yourself.  
The solution is quite obvious if you only want to trade those markets during London, trade two strategy's.  
  
I trade the the VCP Pattern (inside Squeeze's) on a 2 minute Chart during London Open where possible, otherwise 70% of my time is focussed on my primary strategy. On Friday there was very little to trade during the London Session, I quit for the week.  
  
If I only want to trade Squeeze Setups during London, I also look at EURUSD - GBPUSD - USDJPY - EURJPY - GBPJPY & BTC on M5 or H1. 

Trading thin liquidity at the boundary of the charts

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#314](/thread/post/15128140#post15128140 "Post Permalink")

  * Jan 26, 2025 7:34pm  Jan 26, 2025 7:34pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1967050_1.gif) Ju4ara](ju4ara)

  * | Joined Oct 2024  | Status: Trader | [105 Posts](/search?do=process&provider=Member&searchuser=1967050)

> [Quoting RickM](/thread/post/15128086#post15128086 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi Ju I mostly trade London where I focus on ES / NQ / Gold & Oil Futures so I am in the same situation as yourself. The solution is quite obvious if you only want to trade those markets during London, trade two strategy's. I trade the the VCP Pattern (inside Squeeze's) on a 2 minute Chart during London Open where possible, otherwise 70% of my time is focussed on my primary strategy. On Friday there was very little to trade during the London Session, I quit for the week. If I only want to trade Squeeze Setups during London, I also look at...
> 
> Ignored

Hi RickM,  
Thanks for advice. So do you trade mostly vcp pattern or only vcp pattern on indices and gold? Also, I remember you said that btc and forex works best on H1, do you recommend M5 too? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#315](/thread/post/15128216#post15128216 "Post Permalink")

  * Jan 27, 2025 12:18am  Jan 27, 2025 12:18am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot_20250126_101847_Photos.jpg
Size: 386 KB](/attachment/image/4885656/thumbnail?d=1737904735)](/attachment/image/4885656?d=1737904735)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#316](/thread/post/15128377#post15128377 "Post Permalink")

  * Jan 27, 2025 7:46am  Jan 27, 2025 7:46am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot_20250126_174539_Photos.jpg
Size: 281 KB](/attachment/image/4885751/thumbnail?d=1737931582)](/attachment/image/4885751?d=1737931582)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#317](/thread/post/15128378#post15128378 "Post Permalink")

  * Jan 27, 2025 7:48am  Jan 27, 2025 7:48am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

> [Quoting MachineLearn](/thread/post/15127569#post15127569 "View Quoted Post")
> 
> Disliked
> 
> No limit set , but curious too see what kind squeeze appears here and if more buyers are absorbed. Conversely seems like a bullish vcp is simulataneously setting up too (kind of) Check back on market open {image} {image}
> 
> Ignored

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot_20250126_174826_Photos.jpg
Size: 301 KB](/attachment/image/4885752/thumbnail?d=1737931718)](/attachment/image/4885752?d=1737931718)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#318](/thread/post/15128384#post15128384 "Post Permalink")

  * Edited 8:32am  Jan 27, 2025 7:52am | Edited 8:32am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

Next setup I'll be waiting for  
Update   
Trendline tested again  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot_20250126_183125_Photos.jpg
Size: 252 KB](/attachment/image/4885763/thumbnail?d=1737934320)](/attachment/image/4885763?d=1737934320)   

  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot_20250126_175211_Photos.jpg
Size: 308 KB](/attachment/image/4885753/thumbnail?d=1737931944)](/attachment/image/4885753?d=1737931944)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#319](/thread/post/15128489#post15128489 "Post Permalink")

  * Jan 27, 2025 11:12am  Jan 27, 2025 11:12am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot_20250126_211234_Photos.jpg
Size: 303 KB](/attachment/image/4885850/thumbnail?d=1737943968)](/attachment/image/4885850?d=1737943968)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#320](/thread/post/15128511#post15128511 "Post Permalink")

  * Jan 27, 2025 11:42am  Jan 27, 2025 11:42am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

Loading up 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot_20250126_214145_Photos.jpg
Size: 269 KB](/attachment/image/4885867/thumbnail?d=1737945722)](/attachment/image/4885867?d=1737945722)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Squeeze n Go | MTF System
  *   * [ **Reply to Thread** ](/thread/1319487-squeeze-n-go-mtf-system/reply#reply)

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

[Spud's MTF FIB Breakout System](/thread/30109-spuds-mtf-fib-breakout-system "Spud's MTF FIB Breakout System 
-------------------------------- 
Ever since I learned about Fibonacci numbers they have interested my pure...") 375 replies

[H1Scalper System (MTF D1,H1,M5)](/thread/166646-h1scalper-system-mtf-d1h1m5 "Here are the indicators for a manual system. 
  
Explanations, rules and trading ideas are coming... 
. 
\(2009.05.13\) 
Attached are the...") 725 replies

[MTF Trix system](/thread/183801-mtf-trix-system "Hello everybody, 
 
This thread is for developing and discussing a multi-timeframe trading system that is based on one indicator - Trix -...") 3,697 replies

[MTF Stochastics into MTF Stoch Histogram](/thread/359918-mtf-stochastics-into-mtf-stoch-histogram "Hi, 
 
I have been trading with the help of MTF Stochastics for a few weeks now with relatively good results but would appreciate if...") 8 replies

[MTF Vajioo Scalping System](/thread/195912-mtf-vajioo-scalping-system "RUBBISH") 15 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/1319487-squeeze-n-go-mtf-system/reply#reply)
  * Subscribe
  * [216](javascript:void\(0\);)

Attachments: Squeeze n Go | MTF System

Tags: Squeeze n Go | MTF System

#  [](/thread/1319487-squeeze-n-go-mtf-system)Squeeze n Go | MTF System 

  * 

  * [#321](/thread/post/15128953#post15128953 "Post Permalink")

  * Jan 27, 2025 7:48pm  Jan 27, 2025 7:48pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar426855_1.gif) RickM](rickm)

  * Joined Sep 2015 | Status: Trader | [2,439 Posts](/search?do=process&provider=Member&searchuser=426855)

> [Quoting Ju4ara](/thread/post/15128140#post15128140 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi RickM, Thanks for advice. So do you trade mostly vcp pattern or only vcp pattern on indices and gold? Also, I remember you said that btc and forex works best on H1, do you recommend M5 too?
> 
> Ignored

Hi Ju  
  
M5 if you want to intraday trade Forex, H1 as a second option. 

Trading thin liquidity at the boundary of the charts

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#322](/thread/post/15129064#post15129064 "Post Permalink")

  * Jan 27, 2025 9:07pm  Jan 27, 2025 9:07pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1967050_1.gif) Ju4ara](ju4ara)

  * | Joined Oct 2024  | Status: Trader | [105 Posts](/search?do=process&provider=Member&searchuser=1967050)

> [Quoting RickM](/thread/post/15128953#post15128953 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi Ju M5 if you want to intraday trade Forex, H1 as a second option.
> 
> Ignored

Hi RickM, would it be enough to add only one pair to my stack e.g. E/U only, or should I add all pairs mentioned in your previous message?  
Thanks in advance. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#323](/thread/post/15129076#post15129076 "Post Permalink")

  * Jan 27, 2025 9:16pm  Jan 27, 2025 9:16pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1967050_1.gif) Ju4ara](ju4ara)

  * | Joined Oct 2024  | Status: Trader | [105 Posts](/search?do=process&provider=Member&searchuser=1967050)

hi guys, which candle here would be recommended to enter position? 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 109 KB](/attachment/image/4886190/thumbnail?d=1737980137)](/attachment/image/4886190?d=1737980137)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#324](/thread/post/15129202#post15129202 "Post Permalink")

  * Jan 27, 2025 10:21pm  Jan 27, 2025 10:21pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar272159_71.gif) driven18](driven18)

  * Joined Jul 2012 | Status: Trader | [1,385 Posts](/search?do=process&provider=Member&searchuser=272159)

> [Quoting Ju4ara](/thread/post/15129076#post15129076 "View Quoted Post")
> 
> Disliked
> 
> hi guys, which candle here would be recommended to enter position? {image}
> 
> Ignored

Here would be my entry point, beautiful "rejection" and "early bird gets the worm". 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 81 KB](/attachment/image/4886260/thumbnail?d=1737984056)](/attachment/image/4886260?d=1737984056)   

[0 ](javascript:void\(0\);) [5 ](javascript:void\(0\);)

  * [#325](/thread/post/15129209#post15129209 "Post Permalink")

  * Jan 27, 2025 10:25pm  Jan 27, 2025 10:25pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar272159_71.gif) driven18](driven18)

  * Joined Jul 2012 | Status: Trader | [1,385 Posts](/search?do=process&provider=Member&searchuser=272159)

Here is "Deep Seek" short trade for +250. Got a signal on Sunday night here, could not resist. Sometimes done for the day, before the day started.  
  
5 Min TF, Dow Futures,**Under 21 EMA.**

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 9 KB](/attachment/image/4886268/thumbnail?d=1737984322)](/attachment/image/4886268?d=1737984322)   

[0 ](javascript:void\(0\);) [6 ](javascript:void\(0\);)

  * [#326](/thread/post/15129236#post15129236 "Post Permalink")

  * Jan 27, 2025 10:36pm  Jan 27, 2025 10:36pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar426855_1.gif) RickM](rickm)

  * Joined Sep 2015 | Status: Trader | [2,439 Posts](/search?do=process&provider=Member&searchuser=426855)

> [Quoting Ju4ara](/thread/post/15129076#post15129076 "View Quoted Post")
> 
> Disliked
> 
> hi guys, which candle here would be recommended to enter position? {image}
> 
> Ignored

Driven NAILED it  
  
  
  
Your entry isn't a VCP Pattern but its a B Grade Squeeze Setup - worth a shot 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: ddd.png
Size: 297 KB](/attachment/image/4886289/thumbnail?d=1737984989)](/attachment/image/4886289?d=1737984989)   

Trading thin liquidity at the boundary of the charts

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#327](/thread/post/15129314#post15129314 "Post Permalink")

  * Jan 27, 2025 11:12pm  Jan 27, 2025 11:12pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

> [Quoting MachineLearn](/thread/post/15128384#post15128384 "View Quoted Post")
> 
> Disliked
> 
> Next setup I'll be waiting for Update Trendline tested again {image} {image}
> 
> Ignored

POP goes the weasel..  
  
Not going to find better RR in many other systems 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot_20250127_091059_Photos.jpg
Size: 225 KB](/attachment/image/4886355/thumbnail?d=1737987137)](/attachment/image/4886355?d=1737987137)   

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#328](/thread/post/15129320#post15129320 "Post Permalink")

  * Jan 27, 2025 11:16pm  Jan 27, 2025 11:16pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar426855_1.gif) RickM](rickm)

  * Joined Sep 2015 | Status: Trader | [2,439 Posts](/search?do=process&provider=Member&searchuser=426855)

> [Quoting Ju4ara](/thread/post/15129064#post15129064 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi RickM, would it be enough to add only one pair to my stack e.g. E/U only, or should I add all pairs mentioned in your previous message? Thanks in advance.
> 
> Ignored

Have them up on one screen and pick the best setup.  
Only trade 1 US pair or Yen Pair at a time 

Trading thin liquidity at the boundary of the charts

[0 ](javascript:void\(0\);) [4 ](javascript:void\(0\);)

  * [#329](/thread/post/15129533#post15129533 "Post Permalink")

  * Jan 28, 2025 1:28am  Jan 28, 2025 1:28am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1967050_1.gif) Ju4ara](ju4ara)

  * | Joined Oct 2024  | Status: Trader | [105 Posts](/search?do=process&provider=Member&searchuser=1967050)

VCP pattern appeared on a graph, but I was waiting for momentum so entered on 4th pullback.  
EDIT: Lost 2R in this trade, feeling frustrated. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 107 KB](/attachment/image/4886496/thumbnail?d=1737995265)](/attachment/image/4886496?d=1737995265)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#330](/thread/post/15129566#post15129566 "Post Permalink")

  * Jan 28, 2025 1:52am  Jan 28, 2025 1:52am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1967050_1.gif) Ju4ara](ju4ara)

  * | Joined Oct 2024  | Status: Trader | [105 Posts](/search?do=process&provider=Member&searchuser=1967050)

New structure showed instead of that one, still a vcp pattern, I've waited for momentum and entered. I just don't understand how would I know there is going to be a new structure in a first place. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 102 KB](/attachment/image/4886516/thumbnail?d=1737996740)](/attachment/image/4886516?d=1737996740)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#331](/thread/post/15129588#post15129588 "Post Permalink")

  * Jan 28, 2025 2:09am  Jan 28, 2025 2:09am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar272159_71.gif) driven18](driven18)

  * Joined Jul 2012 | Status: Trader | [1,385 Posts](/search?do=process&provider=Member&searchuser=272159)

> [Quoting driven18](/thread/post/15129202#post15129202 "View Quoted Post")
> 
> Disliked
> 
> {quote} Here would be my entry point, beautiful "rejection" and "early bird gets the worm". {image}
> 
> Ignored

I am reposting this again, as **THIS IS** **an A+++++++ setup**.  
  
Give me this set up and I will take it all day long and **I can guarantee** with proper Money Management and Control of MindFuck, I will be profitable at the end of the month, every month. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 61 KB](/attachment/image/4886526/thumbnail?d=1737997741)](/attachment/image/4886526?d=1737997741)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#332](/thread/post/15129713#post15129713 "Post Permalink")

  * Jan 28, 2025 3:51am  Jan 28, 2025 3:51am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

Could pop either way ofc 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot_20250127_135122_Photos.jpg
Size: 233 KB](/attachment/image/4886610/thumbnail?d=1738003899)](/attachment/image/4886610?d=1738003899)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#333](/thread/post/15129764#post15129764 "Post Permalink")

  * Jan 28, 2025 5:03am  Jan 28, 2025 5:03am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar272159_71.gif) driven18](driven18)

  * Joined Jul 2012 | Status: Trader | [1,385 Posts](/search?do=process&provider=Member&searchuser=272159)

> [Quoting MachineLearn](/thread/post/15129713#post15129713 "View Quoted Post")
> 
> Disliked
> 
> Could pop either way ofc {image}
> 
> Ignored

I think you are taking a pop as an all in all technical analysis....Are you forgetting direction of the markets, perhaps at least on the higher timeframe?  
  
Pop happens after a squeeze, but can be continue to be a **broadening squeeze instead of pop** , so you lose both ways. I would highly recommends to wait for the trades as the one been discussed today....it looks good and feels good, even if Stop out occurs, trader should feel good taking that trade. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#334](/thread/post/15129781#post15129781 "Post Permalink")

  * Jan 28, 2025 5:42am  Jan 28, 2025 5:42am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

> [Quoting driven18](/thread/post/15129764#post15129764 "View Quoted Post")
> 
> Disliked
> 
> {quote} I think you are taking a pop as an all in all technical analysis....Are you forgetting direction of the markets, perhaps at least on the higher timeframe? Pop happens after a squeeze, but can be continue to be a broadening squeeze instead of pop, so you lose both ways. I would highly recommends to wait for the trades as the one been discussed today....it looks good and feels good, even if Stop out occurs, trader should feel good taking that trade.
> 
> Ignored

I have a directional bias that I favor. I proceed with entry conditions based off of these biases which will directly impact my money management and trade setup.  
  
For example in this trade that just triggered, my bias is bullish. So when I do get a pop to the upside I have a tighter SL, and more psychological confidence to hold my position.  
  
HTF just like any other indicator can sometimes be a fallacy. I typically like to trade the candles im looking at, but I do take it into consideration 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot_20250127_154426_Photos.jpg
Size: 329 KB](/attachment/image/4886653/thumbnail?d=1738010678)](/attachment/image/4886653?d=1738010678)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#335](/thread/post/15129792#post15129792 "Post Permalink")

  * Jan 28, 2025 6:09am  Jan 28, 2025 6:09am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

> [Quoting MachineLearn](/thread/post/15129781#post15129781 "View Quoted Post")
> 
> Disliked
> 
> {quote} I have a directional bias that I favor. I proceed with entry conditions based off of these biases which will directly impact my money management and trade setup. For example in this trade that just triggered, my bias is bullish. So when I do get a pop to the upside I have a tighter SL, and more psychological confidence to hold my position. HTF just like any other indicator can sometimes be a fallacy. I typically like to trade the candles im looking at, but I do take it into consideration {image}
> 
> Ignored

POP goes the weasel ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)  
  
TP HIT 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot_20250127_160841_TradingView.jpg
Size: 342 KB](/attachment/image/4886663/thumbnail?d=1738012139)](/attachment/image/4886663?d=1738012139)   

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#336](/thread/post/15129795#post15129795 "Post Permalink")

  * Jan 28, 2025 6:16am  Jan 28, 2025 6:16am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar272159_71.gif) driven18](driven18)

  * Joined Jul 2012 | Status: Trader | [1,385 Posts](/search?do=process&provider=Member&searchuser=272159)

> [Quoting MachineLearn](/thread/post/15129792#post15129792 "View Quoted Post")
> 
> Disliked
> 
> {quote} POP goes the weasel ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1) TP HIT {image}
> 
> Ignored

The weasel, the weasel, just went POP. ![](https://resources.faireconomy.media/images/emojis/64/1f44a.png?v=15.1)  
  
To counter the "deepseek", I started my position in NVIDIA! USA, USA ![](https://resources.faireconomy.media/images/emojis/64/1f1fa-1f1f8.png?v=15.1). 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#337](/thread/post/15129799#post15129799 "Post Permalink")

  * Jan 28, 2025 6:19am  Jan 28, 2025 6:19am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

> [Quoting driven18](/thread/post/15129795#post15129795 "View Quoted Post")
> 
> Disliked
> 
> {quote} The weasel, the weasel, just went POP. ![](https://resources.faireconomy.media/images/emojis/64/1f44a.png?v=15.1) To counter the "deepseek", I started my position in NVIDIA! USA, USA ![](https://resources.faireconomy.media/images/emojis/64/1f1fa-1f1f8.png?v=15.1).
> 
> Ignored

![](https://resources.faireconomy.media/images/emojis/64/1f602.png?v=15.1) ![](https://resources.faireconomy.media/images/emojis/64/1f602.png?v=15.1)

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#338](/thread/post/15129880#post15129880 "Post Permalink")

  * Jan 28, 2025 8:25am  Jan 28, 2025 8:25am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot_20250127_182417_TradingView.jpg
Size: 46 KB](/attachment/image/4886715/thumbnail?d=1738020333)](/attachment/image/4886715?d=1738020333)   

  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot_20250127_182352_Photos.jpg
Size: 272 KB](/attachment/image/4886716/thumbnail?d=1738020334)](/attachment/image/4886716?d=1738020334)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#339](/thread/post/15129930#post15129930 "Post Permalink")

  * Jan 28, 2025 9:27am  Jan 28, 2025 9:27am 

  * [ aud](aud)

  * | Joined Apr 2008  | Status: Trader | [1,013 Posts](/search?do=process&provider=Member&searchuser=67749)

> [Quoting driven18](/thread/post/15129209#post15129209 "View Quoted Post")
> 
> Disliked
> 
> ~~ 5 Min TF, Dow Futures, Under 21 EMA.
> 
> Ignored

Staying in the trade when it crossed back above the 21 ema is the trick! 

Good Trading

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#340](/thread/post/15129942#post15129942 "Post Permalink")

  * Jan 28, 2025 9:52am  Jan 28, 2025 9:52am 

  * [ aud](aud)

  * | Joined Apr 2008  | Status: Trader | [1,013 Posts](/search?do=process&provider=Member&searchuser=67749)

> [Quoting Ju4ara](/thread/post/15129076#post15129076 "View Quoted Post")
> 
> Disliked
> 
> hi guys, which candle here would be recommended to enter position? {image}
> 
> Ignored

If you rephrase the question to "where to add a 2nd trade after moving the S/L to at least BE" ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) My humble opinion would be the 3rd arrow (the righter most). It's the only one that is a momentum candle that also clears the cluster.   
  
Given all the MAs on your chart, the first trade is easy to see if you watch for the first pull back after the MAs cross over. The entry (which has been pointed out) just happens to be a momentum candle that also clears the cluster. 

Good Trading

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Squeeze n Go | MTF System
  *   * [ **Reply to Thread** ](/thread/1319487-squeeze-n-go-mtf-system/reply#reply)

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

[Spud's MTF FIB Breakout System](/thread/30109-spuds-mtf-fib-breakout-system "Spud's MTF FIB Breakout System 
-------------------------------- 
Ever since I learned about Fibonacci numbers they have interested my pure...") 375 replies

[H1Scalper System (MTF D1,H1,M5)](/thread/166646-h1scalper-system-mtf-d1h1m5 "Here are the indicators for a manual system. 
  
Explanations, rules and trading ideas are coming... 
. 
\(2009.05.13\) 
Attached are the...") 725 replies

[MTF Trix system](/thread/183801-mtf-trix-system "Hello everybody, 
 
This thread is for developing and discussing a multi-timeframe trading system that is based on one indicator - Trix -...") 3,697 replies

[MTF Stochastics into MTF Stoch Histogram](/thread/359918-mtf-stochastics-into-mtf-stoch-histogram "Hi, 
 
I have been trading with the help of MTF Stochastics for a few weeks now with relatively good results but would appreciate if...") 8 replies

[MTF Vajioo Scalping System](/thread/195912-mtf-vajioo-scalping-system "RUBBISH") 15 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/1319487-squeeze-n-go-mtf-system/reply#reply)
  * Subscribe
  * [216](javascript:void\(0\);)

Attachments: Squeeze n Go | MTF System

Tags: Squeeze n Go | MTF System

#  [](/thread/1319487-squeeze-n-go-mtf-system)Squeeze n Go | MTF System 

  * 

  * [#341](/thread/post/15129946#post15129946 "Post Permalink")

  * Edited 11:41pm  Jan 28, 2025 10:00am | Edited 11:41pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

H1 setup, will take much longer...but I like the odds. Last time a setup appeared like this is took off. Good RR. Could target much more but that's first TP  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot_20250127_195912_Photos.jpg
Size: 312 KB](/attachment/image/4886751/thumbnail?d=1738026004)](/attachment/image/4886751?d=1738026004)   

  
*  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot_20250128_094003_TradingView.jpg
Size: 312 KB](/attachment/image/4887269/thumbnail?d=1738075272)](/attachment/image/4887269?d=1738075272)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#342](/thread/post/15130009#post15130009 "Post Permalink")

  * Edited 11:56am  Jan 28, 2025 11:39am | Edited 11:56am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar272159_71.gif) driven18](driven18)

  * Joined Jul 2012 | Status: Trader | [1,385 Posts](/search?do=process&provider=Member&searchuser=272159)

> [Quoting aud](/thread/post/15129930#post15129930 "View Quoted Post")
> 
> Disliked
> 
> {quote} Staying in the trade when it crossed back above the 21 ema **is the trick!**
> 
> Ignored

Tricky is what it is. No Mindfuck here..stay the course and get to that promised land we call TP. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#343](/thread/post/15130246#post15130246 "Post Permalink")

  * Jan 28, 2025 5:49pm  Jan 28, 2025 5:49pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar426855_1.gif) RickM](rickm)

  * Joined Sep 2015 | Status: Trader | [2,439 Posts](/search?do=process&provider=Member&searchuser=426855)

> [Quoting driven18](/thread/post/15129795#post15129795 "View Quoted Post")
> 
> Disliked
> 
> {quote} The weasel, the weasel, just went POP. ![](https://resources.faireconomy.media/images/emojis/64/1f44a.png?v=15.1) To counter the "deepseek", I started my position in NVIDIA! USA, USA ![](https://resources.faireconomy.media/images/emojis/64/1f1fa-1f1f8.png?v=15.1).
> 
> Ignored

I just hope NVIDIA keeps providing big volume moves on US Indice's like yesterday.  
  
On ES, Volume was 12 times above normal London values - not hard to just trade with the Trend on these days.  
If we go back to Friday's London Session, Volume was 1/4 normal values - not hard to skip trading the session on those days. 

Trading thin liquidity at the boundary of the charts

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#344](/thread/post/15130310#post15130310 "Post Permalink")

  * Jan 28, 2025 6:36pm  Jan 28, 2025 6:36pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1967050_1.gif) Ju4ara](ju4ara)

  * | Joined Oct 2024  | Status: Trader | [105 Posts](/search?do=process&provider=Member&searchuser=1967050)

> [Quoting aud](/thread/post/15129942#post15129942 "View Quoted Post")
> 
> Disliked
> 
> {quote} If you rephrase the question to "where to add a 2nd trade after moving the S/L to at least BE" ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) My humble opinion would be the 3rd arrow (the righter most). It's the only one that is a momentum candle that also clears the cluster. Given all the MAs on your chart, the first trade is easy to see if you watch for the first pull back after the MAs cross over. The entry (which has been pointed out) just happens to be a momentum candle that also clears the cluster.
> 
> Ignored

That’s what I meant to be honest, thanks. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#345](/thread/post/15130799#post15130799 "Post Permalink")

  * Jan 29, 2025 12:37am  Jan 29, 2025 12:37am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1967050_1.gif) Ju4ara](ju4ara)

  * | Joined Oct 2024  | Status: Trader | [105 Posts](/search?do=process&provider=Member&searchuser=1967050)

Hi, would you recommend to take this trade? Red dots on Choc + retest of both 21ema and support on black dot with nice rejection 30 mins after London open. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 113 KB](/attachment/image/4887322/thumbnail?d=1738078652)](/attachment/image/4887322?d=1738078652)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#346](/thread/post/15130808#post15130808 "Post Permalink")

  * Jan 29, 2025 12:43am  Jan 29, 2025 12:43am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar272159_71.gif) driven18](driven18)

  * Joined Jul 2012 | Status: Trader | [1,385 Posts](/search?do=process&provider=Member&searchuser=272159)

> [Quoting Ju4ara](/thread/post/15130799#post15130799 "View Quoted Post")
> 
> Disliked
> 
> Hi, would you recommend to take this trade? Red dots on Choc + retest of both 21ema and support on black dot with nice rejection 30 mins after London open. {image}
> 
> Ignored

![](https://resources.faireconomy.media/images/emojis/64/1f4af.png?v=15.1) \- Yes  
  
Get rid of Nova Volume - no use whatsoever. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#347](/thread/post/15131059#post15131059 "Post Permalink")

  * Jan 29, 2025 5:19am  Jan 29, 2025 5:19am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot_20250128_151927_Photos.jpg
Size: 303 KB](/attachment/image/4887508/thumbnail?d=1738095582)](/attachment/image/4887508?d=1738095582)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#348](/thread/post/15131258#post15131258 "Post Permalink")

  * Jan 29, 2025 1:56pm  Jan 29, 2025 1:56pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot_20250128_235623_Photos.jpg
Size: 285 KB](/attachment/image/4887681/thumbnail?d=1738126607)](/attachment/image/4887681?d=1738126607)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#349](/thread/post/15131279#post15131279 "Post Permalink")

  * Jan 29, 2025 2:57pm  Jan 29, 2025 2:57pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot_20250129_005736_Photos.jpg
Size: 308 KB](/attachment/image/4887695/thumbnail?d=1738130275)](/attachment/image/4887695?d=1738130275)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#350](/thread/post/15132891#post15132891 "Post Permalink")

  * Edited 11:02pm  Jan 30, 2025 10:12pm | Edited 11:02pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar272159_71.gif) driven18](driven18)

  * Joined Jul 2012 | Status: Trader | [1,385 Posts](/search?do=process&provider=Member&searchuser=272159)

In a trade 5 Min TF Dow Futures, managing as I post this and no MindFuck.  
  
Relevance, under EMA 21 and to continue supporting Machine thread.  
  
Done, **+102** ![](https://resources.faireconomy.media/images/emojis/64/1f600.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f37a.png?v=15.1)

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 10 KB](/attachment/image/4888900/thumbnail?d=1738242697)](/attachment/image/4888900?d=1738242697)   
[![Click to Enlarge

Name: screenshot.png
Size: 15 KB](/attachment/image/4888920/thumbnail?d=1738243965)](/attachment/image/4888920?d=1738243965)   

[0 ](javascript:void\(0\);) [5 ](javascript:void\(0\);)

  * [#351](/thread/post/15132917#post15132917 "Post Permalink")

  * Jan 30, 2025 10:31pm  Jan 30, 2025 10:31pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1967050_1.gif) Ju4ara](ju4ara)

  * | Joined Oct 2024  | Status: Trader | [105 Posts](/search?do=process&provider=Member&searchuser=1967050)

Found this trade today in london session, on uptrend after pullback from 21ema with small rejection and momentum was not great, but I would still take it because of strong move from 21ema on squeeze. Would rate it as B+. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: IMG_1743.png
Size: 121 KB](/attachment/image/4888915/thumbnail?d=1738243749)](/attachment/image/4888915?d=1738243749)   

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#352](/thread/post/15133622#post15133622 "Post Permalink")

  * Jan 31, 2025 11:39am  Jan 31, 2025 11:39am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar426855_1.gif) RickM](rickm)

  * Joined Sep 2015 | Status: Trader | [2,439 Posts](/search?do=process&provider=Member&searchuser=426855)

> [Quoting Ju4ara](/thread/post/15132917#post15132917 "View Quoted Post")
> 
> Disliked
> 
> Found this trade today in london session, on uptrend after pullback from 21ema with small rejection and momentum was not great, but I would still take it because of strong move from 21ema on squeeze. Would rate it as B+. {image}
> 
> Ignored

Hi Ju4ara  
  
Yes, B+ but it was really an A++++++  
There was something more important happening there that as a trader we should have seen.  
  
I saw it and added a trade from the first setup on the previous Squeeze. So when price came down to the 21 EMA, it was either a take profit and be happy or look to add an additional trade on Gold.  
  
I took this trade on GCJ5 and now I had 2 long positions.  
I stayed in the trade for a bit longer and took profit higher up.   
  
My exit was terrible but the profit was worth in an excess of 2K for entering on single contracts.  
  
I really need to talk about the “missing X” soon which is a game changer if you are not already using it.   
Did you know there was a prefect Squeeze + X on Monday with ES(Us500) that if I was at my trading desk on Monday instead of drinking at a bar - I may have earned 11k on a Setup.   
  
I am pissed off I wasn’t trading that night, I missed the prefect trade.  
I got what I deserved.  
  
Driven talks about “Mindfuck” or something similar.  
If you really want to trade with mindfuck  
  
You need “missing x”  
  
  
Cheers 

Trading thin liquidity at the boundary of the charts

[0 ](javascript:void\(0\);) [3 ](javascript:void\(0\);)

  * [#353](/thread/post/15133631#post15133631 "Post Permalink")

  * Jan 31, 2025 11:46am  Jan 31, 2025 11:46am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar272159_71.gif) driven18](driven18)

  * Joined Jul 2012 | Status: Trader | [1,385 Posts](/search?do=process&provider=Member&searchuser=272159)

> [Quoting RickM](/thread/post/15133622#post15133622 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi Ju4ara Yes, B+ but it was really an A++++++ There was something more important happening there that as a trader we should have seen. I saw it and added a trade from the first setup on the previous Squeeze. So when price came down to the 21 EMA, it was either a take profit and be happy or look to add an additional trade on Gold. I took this trade on GCJ5 and now I had 2 long positions. I stayed in the trade for a bit longer and took profit higher up. My exit was terrible but the profit was worth in an excess of 2K for entering on single...
> 
> Ignored

RickM, the post above sounds like you still under effect of that drink at the bar. Come on mate, I thought Australians can handle their liquor ![](https://resources.faireconomy.media/images/emojis/64/1f607.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f37a.png?v=15.1).  
  
"missing X" What the bloody hell you talking about? (I am saying it with an Australian accent) ![](https://resources.faireconomy.media/images/emojis/64/1f44a.png?v=15.1)

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#354](/thread/post/15133673#post15133673 "Post Permalink")

  * Jan 31, 2025 1:19pm  Jan 31, 2025 1:19pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar426855_1.gif) RickM](rickm)

  * Joined Sep 2015 | Status: Trader | [2,439 Posts](/search?do=process&provider=Member&searchuser=426855)

> [Quoting driven18](/thread/post/15133631#post15133631 "View Quoted Post")
> 
> Disliked
> 
> {quote} RickM, the post above sounds like you still under effect of that drink at the bar. Come on mate, I thought Australians can handle their liquor ![](https://resources.faireconomy.media/images/emojis/64/1f607.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f37a.png?v=15.1). "missing X" What the bloody hell you talking about? (I am saying it with an Australian accent) ![](https://resources.faireconomy.media/images/emojis/64/1f44a.png?v=15.1)
> 
> Ignored

Hi Driven  
  
I reckon if you traded with “ missing x, you could double your Mindfuck trades with ease.  
It’s best I show you guys a chart of the prefect Gold trade from last night that was taken by myself and probably a few thousand professional traders as well.  
Its a Squeeze entry then managed by “missing X”.  
For most professional traders, it was just “missing X”  
  
Thats when I get back to the trading den for London Open later and find some spare time.  

  
PS. I loved the Monday trade setup so much, I have re traded it 5 times on Replay Mode this week already. Got to love platforms that allow traders to retrade setups to nail trade execution. 

Trading thin liquidity at the boundary of the charts

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#355](/thread/post/15133981#post15133981 "Post Permalink")

  * Jan 31, 2025 6:51pm  Jan 31, 2025 6:51pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar2023811_1.gif) CogAlpha](cogalpha)

  * Joined Jan 2025 | Status: Trader | [231 Posts](/search?do=process&provider=Member&searchuser=2023811)

Playing around coding a Script, based on whats written in here..   
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 41 KB](/attachment/image/4889530/thumbnail?d=1738316990)](/attachment/image/4889530?d=1738316990)   

  
  
Not finished just yet.. but already looks promising.   
As RickM wrote several times... there may be more optimal Entries, by using experience.   
Experience cant be put into code. But once its finished, it may still be useful for some. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#356](/thread/post/15134023#post15134023 "Post Permalink")

  * Jan 31, 2025 7:36pm  Jan 31, 2025 7:36pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar426855_1.gif) RickM](rickm)

  * Joined Sep 2015 | Status: Trader | [2,439 Posts](/search?do=process&provider=Member&searchuser=426855)

> [Quoting CogAlpha](/thread/post/15133981#post15133981 "View Quoted Post")
> 
> Disliked
> 
> Playing around coding a Script, based on whats written in here.. {image} Not finished just yet.. but already looks promising. As RickM wrote several times... there may be more optimal Entries, by using experience. Experience cant be put into code. But once its finished, it may still be useful for some.
> 
> Ignored

Looks good Cog, please let us know how it works out. 

Trading thin liquidity at the boundary of the charts

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#357](/thread/post/15134030#post15134030 "Post Permalink")

  * Jan 31, 2025 7:44pm  Jan 31, 2025 7:44pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar2023811_1.gif) CogAlpha](cogalpha)

  * Joined Jan 2025 | Status: Trader | [231 Posts](/search?do=process&provider=Member&searchuser=2023811)

> [Quoting RickM](/thread/post/15134023#post15134023 "View Quoted Post")
> 
> Disliked
> 
> {quote} Looks good Cog, please let us know how it works out.
> 
> Ignored

Here is an overview which I made in preperation for Publishing it on FF... (Need that stuff for Tradingview guidelines)  
  
The Entries arent filtered out properly as of now. EMA order.. etc are missing.  
Once I am happy with that, I will post it here.  
  
Adaptive Squeeze Intensity Indicator  
  
Main Settings

  1. **Base Length** (default: 20)

    1. Controls the primary calculation period
    2. Minimum value: 10
    3. Adjusts sensitivity of core calculations

  

  2. **BB Multiplier** (default: 2.0)

    1. Bollinger Bands standard deviation multiplier
    2. Range: 1.0 to 4.0
    3. Impacts Bollinger Bands width calculation

  

  3. **Keltner Channel Multipliers**

    1. Three separate multipliers for different channel intensities

      1. Keltner Channel #1 (default: 1.0)
      2. Keltner Channel #2 (default: 1.5)
      3. Keltner Channel #3 (default: 2.0)

  

  
Volume Settings

  1. **Include Volume Analysis** (default: true)

    1. Toggles volume consideration in squeeze intensity calculation

  

  2. **Volume MA Length** (default: 14)

    1. Moving average length for volume calculations

  

  3. **Volume Threshold** (default: 1.5)

    1. Determines volume intensity significance

  

Visualization

  1. **Show Numeric Score** (default: true)

    1. Displays numeric squeeze intensity score

  

  2. **Show Intensity Zones** (default: true)

    1. Renders background zones representing squeeze intensity

  

  3. **Color Customization**

    1. Bullish and Bearish color selections for visual representation

  

Calculation Methodology  
Scoring System (0-100 points)  
The indicator generates a comprehensive squeeze intensity score through four key components:

  1. **Band Convergence Score** (0-40 points)

    1. Measures the compression between Bollinger Bands and Keltner Channels
    2. Higher convergence indicates stronger potential for breakout

  

  2. **Price Position Score** (0-20 points)

    1. Evaluates price's position relative to the Keltner Channels
    2. Assesses how centrally or extremely price is positioned

  

  3. **Volume Intensity Score** (0-20 points)

    1. Optional volume analysis
    2. Rewards increased volume activity above a specified threshold

  

  4. **Momentum Score** (0-20 points)

    1. Calculates price momentum using linear regression
    2. Measures price movement's strength and direction

  

Squeeze States

  1. **No Squeeze** (Green): Significant market expansion
  2. **Low Compression** (Black): Minimal market compression
  3. **Mid Compression** (Red): Moderate market tightening
  4. **High Compression** (Orange): Significant market compression

Visualizations

  1. Colored column plot representing squeeze intensity
  2. Gradient coloration from transparent to solid based on intensity
  3. Optional background zones for visual squeeze intensity levels
  4. Optional numeric score label on the last bar

Signals  
Entry Signals

  1. 🢁 Arrow indicating potential long entry
  2. Triggered during squeeze release
  3. Optional background highlight on entry

Alert Conditions

  1. **Extreme Squeeze Alert**

    1. Triggered when squeeze score crosses above 80

  

  2. **Squeeze Release Alert**

    1. Signaled on initial squeeze release, indicating potential breakout

  

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#358](/thread/post/15134039#post15134039 "Post Permalink")

  * Jan 31, 2025 7:58pm  Jan 31, 2025 7:58pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar426855_1.gif) RickM](rickm)

  * Joined Sep 2015 | Status: Trader | [2,439 Posts](/search?do=process&provider=Member&searchuser=426855)

> [Quoting driven18](/thread/post/15133631#post15133631 "View Quoted Post")
> 
> Disliked
> 
> {quote} RickM, the post above sounds like you still under effect of that drink at the bar. Come on mate, I thought Australians can handle their liquor ![](https://resources.faireconomy.media/images/emojis/64/1f607.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f37a.png?v=15.1). "missing X" What the bloody hell you talking about? (I am saying it with an Australian accent) ![](https://resources.faireconomy.media/images/emojis/64/1f44a.png?v=15.1)
> 
> Ignored

Here was the Gold Chart from yesterday.  
  
The "missing X" is the Mindfuck we should use because its how many professionals trade markets.  
  
Step 1 ...... Trade 1 was a Squeeze setup where I took trade 1.  
  
Missing X is .............. Anchored Volume Weighted Average Price  
  
Step 2 ......... Place a Anchored VWAP indicator on the breakout candle and let the trade run.  
  
Step 3 ......... If Price returns to AVWAP, don't exit but rather looked to add an additional trade. Trade 2  
  
Price returns to AVWAP - means Mindfuck  
  
Step 4 ......... Add another trade at AVWAP again. If price doesn't bounce long - EXIT whole position.  
  
The reason AWAP or VWAP works so well on Stock & Future's charts is because many Hedge Fund / Bank Traders who are building positions are told only to Buy at VWAP or below - NEVER ABOVE. Therefore we have hidden Support or hidden resistance at these spots from Professional traders.  
  
If you took this 2 hour trade trade one Gold Future's contract - result would be around $3K profit. The risk would only be around 12 Ticks.  
  
There was also a fantastic Squeeze / AVWAP on ES Mini on Monday that was worth $11,000 trading just single contracts at a time (Perhaps I should not of been at a bar). I have traded this one again 5 times on Re-play mode on Motivewave to practice my execution skills.  
That's Mindfuck  
  
Happy Squeeze's next week guys 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: AVWAP dd.png
Size: 132 KB](/attachment/image/4889573/thumbnail?d=1738321126)](/attachment/image/4889573?d=1738321126)   

Trading thin liquidity at the boundary of the charts

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#359](/thread/post/15134044#post15134044 "Post Permalink")

  * Edited 8:33pm  Jan 31, 2025 8:06pm | Edited 8:33pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar2023811_1.gif) CogAlpha](cogalpha)

  * Joined Jan 2025 | Status: Trader | [231 Posts](/search?do=process&provider=Member&searchuser=2023811)

> [Quoting RickM](/thread/post/15134039#post15134039 "View Quoted Post")
> 
> Disliked
> 
> {quote} Here was the Gold Chart from yesterday. The "missing X" is the Mindfuck we should use because its how many professionals trade markets. Step 1 ...... Trade 1 was a Squeeze setup where I took trade 1. Missing X is .............. Anchored Volume Weighted Average Price Step 2 ......... Place a Anchored VWAP indicator on the breakout candle and let the trade run. Step 3 ......... If Price returns to AVWAP, don't exit but rather looked to add an additional trade. Trade 2 Price returns to AVWAP - means Mindfuck Step 4 ......... Add another trade...
> 
> Ignored

If I may ask.  
  
I have been Trading for a long time, finding the "right" Exit has been always a tough one for me when I am adding into a Position.  
I ended up defaulting for 1 Trade, no scaling in, going for a 1:2RR the math... maths out for me to be profitable, but I do know that scaling is a very powerful way not to only increase your profits, but even decrease your risk.  
  
So my question... when do you exit a Trade?  
And... if your answer is based on Delta/Volume, do you have another method?  
Edit: I assume there are different methods you use based on different Entry styles. So I suspect the Answer isnt easy to give.  
  
2nd Question:  
  
You said the big bois use the VWAP. Is this limited to short term timeframes, or also used in long term Timeframes?  
  
Cheers 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#360](/thread/post/15134068#post15134068 "Post Permalink")

  * Jan 31, 2025 8:48pm  Jan 31, 2025 8:48pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar426855_1.gif) RickM](rickm)

  * Joined Sep 2015 | Status: Trader | [2,439 Posts](/search?do=process&provider=Member&searchuser=426855)

> [Quoting CogAlpha](/thread/post/15134044#post15134044 "View Quoted Post")
> 
> Disliked
> 
> {quote} If I may ask. I have been Trading for a long time, finding the "right" Exit has been always a tough one for me when I am adding into a Position. I ended up defaulting for 1 Trade, no scaling in, going for a 1:2RR the math... maths out for me to be profitable, but I do know that scaling is a very powerful way not to only increase your profits, but even decrease your risk. So my question... when do you exit a Trade? And... if your answer is based on Delta/Volume, do you have another method? 2nd Question: You said the big bois use the VWAP....
> 
> Ignored

Hi Cog  
  
I am a Delta imbalance trader by default so for years I used to hunt 4-12 ticks per trade and exit. On a normal day I used to take 50-80 trade setups per session and used to be totally knacked after 4 hours trading. Profitability was dependent on Market Volatility so on a good day I would kill it and on a low Volatility I would end in RED due to trading costs.  
  
What a stupid idea right?  
  
I backtested many exit strategy's and always came up with two sure winners.  
Either  
1.. I EXIT a single entry trade as price collapses back over the 21EMA  
2.. I place a AVWAP indicator on a breakout candle and keep adding at every bounce until it fails. THIS IS THE BEST STRATEGY I HAVE FOUND IN 30 YEARS TRADING  
At each further breakout on STRONG VOLUME, we need a new AVWAP on intraday charts.  
  
Intraday Charts work best using AVWAP as an Exit  
Daily Charts work best using Weekly VWAP as an Exit  
  
That's my opinion and some may disagree.  
Cheers 

Trading thin liquidity at the boundary of the charts

[0 ](javascript:void\(0\);) [5 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Squeeze n Go | MTF System
  *   * [ **Reply to Thread** ](/thread/1319487-squeeze-n-go-mtf-system/reply#reply)

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

[Spud's MTF FIB Breakout System](/thread/30109-spuds-mtf-fib-breakout-system "Spud's MTF FIB Breakout System 
-------------------------------- 
Ever since I learned about Fibonacci numbers they have interested my pure...") 375 replies

[H1Scalper System (MTF D1,H1,M5)](/thread/166646-h1scalper-system-mtf-d1h1m5 "Here are the indicators for a manual system. 
  
Explanations, rules and trading ideas are coming... 
. 
\(2009.05.13\) 
Attached are the...") 725 replies

[MTF Trix system](/thread/183801-mtf-trix-system "Hello everybody, 
 
This thread is for developing and discussing a multi-timeframe trading system that is based on one indicator - Trix -...") 3,697 replies

[MTF Stochastics into MTF Stoch Histogram](/thread/359918-mtf-stochastics-into-mtf-stoch-histogram "Hi, 
 
I have been trading with the help of MTF Stochastics for a few weeks now with relatively good results but would appreciate if...") 8 replies

[MTF Vajioo Scalping System](/thread/195912-mtf-vajioo-scalping-system "RUBBISH") 15 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/1319487-squeeze-n-go-mtf-system/reply#reply)
  * Subscribe
  * [216](javascript:void\(0\);)

Attachments: Squeeze n Go | MTF System

Tags: Squeeze n Go | MTF System

#  [](/thread/1319487-squeeze-n-go-mtf-system)Squeeze n Go | MTF System 

  * 

  * [#361](/thread/post/15134105#post15134105 "Post Permalink")

  * Edited 10:00pm  Jan 31, 2025 9:28pm | Edited 10:00pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar272159_71.gif) driven18](driven18)

  * Joined Jul 2012 | Status: Trader | [1,385 Posts](/search?do=process&provider=Member&searchuser=272159)

RickM, good stuff, but you know that we always disagree(on professional level) with these 2 points.  
  
My point for newer and/or loosing traders:  
  
1\. Anything to do with volume is totally meaningless, including VWAP and all of it incarnations.  
  
2\. It is statistically more beneficial to go in with full position from the start and use **Money Management** trailing the full position, rather then add on positions to get to full position.  
  
**MindFuck** is what 60% of the business is, controlling Fear and Greed, every new position is a Mindfuck on its own and with **full position I am diminishing it.**..not sure if "missing X' is the same thing, most likely not.  
  
Chart below is 2Min.TF Gold entry(in hindsight) circled and managing **full position** , as an example. Arrow ends when full position exits.  
  
I do not trade gold but here is a live trade with full position I took on January 27 Dow Futures. [https://www.forexfactory.com/thread/...9#post15129209](https://www.forexfactory.com/thread/post/15129209#post15129209)

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 21 KB](/attachment/image/4889625/thumbnail?d=1738326961)](/attachment/image/4889625?d=1738326961)   

[0 ](javascript:void\(0\);) [4 ](javascript:void\(0\);)

  * [#362](/thread/post/15134421#post15134421 "Post Permalink")

  * Edited 12:59am  Feb 1, 2025 12:41am | Edited 12:59am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar272159_71.gif) driven18](driven18)

  * Joined Jul 2012 | Status: Trader | [1,385 Posts](/search?do=process&provider=Member&searchuser=272159)

Dow Futures 5 Min TF, **MindFuck - can you handle it?** Of course Yes and of course I do have feelings ![](https://resources.faireconomy.media/images/emojis/64/1f600.png?v=15.1)  
  
Will be moving stops momentarily...  
  
And out, **+140,** Real Live trading, no hindsight here. 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 17 KB](/attachment/image/4889801/thumbnail?d=1738338245)](/attachment/image/4889801?d=1738338245)   
[![Click to Enlarge

Name: screenshot.png
Size: 16 KB](/attachment/image/4889804/thumbnail?d=1738338394)](/attachment/image/4889804?d=1738338394)   

[0 ](javascript:void\(0\);) [3 ](javascript:void\(0\);)

  * [#363](/thread/post/15134434#post15134434 "Post Permalink")

  * Feb 1, 2025 12:49am  Feb 1, 2025 12:49am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar272159_71.gif) driven18](driven18)

  * Joined Jul 2012 | Status: Trader | [1,385 Posts](/search?do=process&provider=Member&searchuser=272159)

  

Inserted Video

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#364](/thread/post/15134911#post15134911 "Post Permalink")

  * Feb 1, 2025 7:17am  Feb 1, 2025 7:17am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

Nice one from earlier 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot_20250131_171701_Photos.jpg
Size: 319 KB](/attachment/image/4890046/thumbnail?d=1738361866)](/attachment/image/4890046?d=1738361866)   

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#365](/thread/post/15134997#post15134997 "Post Permalink")

  * Feb 1, 2025 11:02am  Feb 1, 2025 11:02am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar426855_1.gif) RickM](rickm)

  * Joined Sep 2015 | Status: Trader | [2,439 Posts](/search?do=process&provider=Member&searchuser=426855)

> [Quoting MachineLearn](/thread/post/15134911#post15134911 "View Quoted Post")
> 
> Disliked
> 
> Nice one from earlier {image}
> 
> Ignored

Nice trade Machine, I can also see a VCP Pattern to strengthen the push upwards 

Trading thin liquidity at the boundary of the charts

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#366](/thread/post/15135003#post15135003 "Post Permalink")

  * Feb 1, 2025 11:16am  Feb 1, 2025 11:16am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar426855_1.gif) RickM](rickm)

  * Joined Sep 2015 | Status: Trader | [2,439 Posts](/search?do=process&provider=Member&searchuser=426855)

I have traded with Driven a few years back and we love to disagree on one subject - VOLUME  
  
There is no chance in hell he will ever consider Volume data is of much value in trading, so no point wasting time here debating with him this subject matter.  
  
But, perhaps there is one other trader reading this post that can see something in this chart below that may just change their opinion slightly.  
  
Volume Data is best used by applying VWAP to intraday charts to show us where the professionals are Buying or Selling. Its next best used for watching the tape (DOM) on Future's and Stock Chart to gain a small advantage here.  
  
1.. When price starts to reverse Bullish, we will see two things. Price up to this moment will hit the Bids and mainly rest against the bids (Buyers).  
2.. At the turn, we start to see Bid tick rejection where price hits the Bid and instantly jumps up and hits the Ask's. So now we see every move now being rejected against the Bids and price now just starts to sit more at the Ask's (Sellers). ITS A SHIFT, very small but it can be seen.  
  
Many of the most famous traders we all read about swear by the TAPE  
  
Now I'll go back in my hole before Driven gives me a hard time 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: DD bid ask.png
Size: 179 KB](/attachment/image/4890109/thumbnail?d=1738376127)](/attachment/image/4890109?d=1738376127)   

Trading thin liquidity at the boundary of the charts

[0 ](javascript:void\(0\);) [9 ](javascript:void\(0\);)

  * [#367](/thread/post/15135004#post15135004 "Post Permalink")

  * Feb 1, 2025 11:23am  Feb 1, 2025 11:23am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar272159_71.gif) driven18](driven18)

  * Joined Jul 2012 | Status: Trader | [1,385 Posts](/search?do=process&provider=Member&searchuser=272159)

> [Quoting RickM](/thread/post/15135003#post15135003 "View Quoted Post")
> 
> Disliked
> 
> I have traded with Driven a few years back and we love to disagree on one subject - VOLUME There is no chance in hell he will ever consider Volume data is of much value in trading, so no point wasting time here debating with him this subject matter. But, perhaps there is one other trader reading this post that can see something in this chart below that may just change their opinion slightly. Volume Data is best used by applying VWAP to intraday charts to show us where the professionals are Buying or Selling. Its next best used for watching the tape...
> 
> Ignored

![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f37a.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f44a.png?v=15.1)

[0 ](javascript:void\(0\);) [3 ](javascript:void\(0\);)

  * [#368](/thread/post/15135017#post15135017 "Post Permalink")

  * Edited 12:50pm  Feb 1, 2025 12:16pm | Edited 12:50pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar272159_71.gif) driven18](driven18)

  * Joined Jul 2012 | Status: Trader | [1,385 Posts](/search?do=process&provider=Member&searchuser=272159)

That was a hell of the month. I was very active on this thread and decided to post an equity line for the month of January, just to show traders that there are always losing days(circled), profitable days, etc..business is not easy especially during drawdowns, but if you have an edge, overall stats are great, so  
  
46 trades, 10% Relative DD and **+16%** profit overall.  
  
It may bring more haters, but I do not give a crap.  
  
Anyway, hello March and projecting good things to come. GL to All!.![](https://resources.faireconomy.media/images/emojis/64/1f37a.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f44a.png?v=15.1)  
  
P.S. @MachneLearn I promise not to hog the thread in March.![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 21 KB](/attachment/image/4890124/thumbnail?d=1738379525)](/attachment/image/4890124?d=1738379525)   

[0 ](javascript:void\(0\);) [13 ](javascript:void\(0\);)

  * [#369](/thread/post/15135365#post15135365 "Post Permalink")

  * Feb 2, 2025 6:17am  Feb 2, 2025 6:17am 

  * [ CashBox](cashbox)

  * Joined Jun 2007 | Status: Trader | [933 Posts](/search?do=process&provider=Member&searchuser=41428)

> [Quoting RickM](/thread/post/15135003#post15135003 "View Quoted Post")
> 
> Disliked
> 
> I have traded with Driven a few years back and we love to disagree on one subject - VOLUME There is no chance in hell he will ever consider Volume data is of much value in trading, so no point wasting time here debating with him this subject matter. But, perhaps there is one other trader reading this post that can see something in this chart below that may just change their opinion slightly. Volume Data is best used by applying VWAP to intraday charts to show us where the professionals are Buying or Selling. Its next best used for watching the tape...
> 
> Ignored

SMB, an actual prop firm (up to $25,000,000 in capital per trader, not the pay to play fx/cfd places), shows statistics that their best traders are tape readers. 

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#370](/thread/post/15135429#post15135429 "Post Permalink")

  * Feb 2, 2025 10:13am  Feb 2, 2025 10:13am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar426855_1.gif) RickM](rickm)

  * Joined Sep 2015 | Status: Trader | [2,439 Posts](/search?do=process&provider=Member&searchuser=426855)

> [Quoting CashBox](/thread/post/15135365#post15135365 "View Quoted Post")
> 
> Disliked
> 
> {quote} SMB, an actual prop firm (up to $25,000,000 in capital per trader, not the pay to play fx/cfd places), shows statistics that their best traders are tape readers.
> 
> Ignored

Hi Cashbox  
  
Exactly, we can also include other great traders like Paul Tudor Jones, Jessie Livermore and Richard Wickoff to name a few.  
  
The big point here is THIS is where you see those Algorithm's actually trading against smaller players. The DOM lets us know whether the Buying or Selling pressure is real or fake which can help deciding on whether we should be trading now.  
  
On my chart above, I use the AVWAP to show hidden resistance - then look for down Ticks on the 500 Tick chart (ES) and actually enter on an ASK when price is pressuring the BIDS.   
  
That's one good trade. 

Trading thin liquidity at the boundary of the charts

[0 ](javascript:void\(0\);) [3 ](javascript:void\(0\);)

  * [#371](/thread/post/15135472#post15135472 "Post Permalink")

  * Feb 2, 2025 12:59pm  Feb 2, 2025 12:59pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot_20250201_225911_Photos.jpg
Size: 297 KB](/attachment/image/4890413/thumbnail?d=1738468764)](/attachment/image/4890413?d=1738468764)   

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#372](/thread/post/15135473#post15135473 "Post Permalink")

  * Feb 2, 2025 1:00pm  Feb 2, 2025 1:00pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

> [Quoting driven18](/thread/post/15135017#post15135017 "View Quoted Post")
> 
> Disliked
> 
> That was a hell of the month. I was very active on this thread and decided to post an equity line for the month of January, just to show traders that there are always losing days(circled), profitable days, etc..business is not easy especially during drawdowns, but if you have an edge, overall stats are great, so 46 trades, 10% Relative DD and +16% profit overall. It may bring more haters, but I do not give a crap. Anyway, hello March and projecting good things to come. GL to All!.![](https://resources.faireconomy.media/images/emojis/64/1f37a.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f44a.png?v=15.1) P.S. @MachneLearn I promise not to hog the thread...
> 
> Ignored

This is is all of our thread brother, hogging can't exist.  
  
Look forward to more posts, don't slow down! 

[0 ](javascript:void\(0\);) [4 ](javascript:void\(0\);)

  * [#373](/thread/post/15135502#post15135502 "Post Permalink")

  * Feb 2, 2025 2:47pm  Feb 2, 2025 2:47pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar35901_4.gif) pipcruiser](pipcruiser)

  * Joined Mar 2007 | Status: One life - live it... | [601 Posts](/search?do=process&provider=Member&searchuser=35901)

> [Quoting MachineLearn](/thread/post/15126180#post15126180 "View Quoted Post")
> 
> Disliked
> 
> I like thus setup. Multiple bounces off a strong resistance area. Diamonds signaling retests. Buyers absorbed? Then price starts to enter a high compression squeeze , after squeezing for a bit. VCP pattern appearing now as well and I would expect an explosive move soon. I like to wait for a release personally. You can see a couple strong support zones below that we could use at TP, which we would create a great RR assuming price breaks to the downside. {image} {image}
> 
> Ignored

Hi ML, Could you give the name of the TV "diamond indicator" - thanks in advance buddy.  
  
PC 

Less is more...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#374](/thread/post/15135785#post15135785 "Post Permalink")

  * Feb 3, 2025 2:22am  Feb 3, 2025 2:22am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

> [Quoting pipcruiser](/thread/post/15135502#post15135502 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi ML, Could you give the name of the TV "diamond indicator" - thanks in advance buddy. PC
> 
> Ignored

[https://www.tradingview.com/script/U...es-ChartPrime/](https://www.tradingview.com/script/Uz2AJ0i4-Support-and-Resistance-High-Volume-Boxes-ChartPrime/)

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot_20250202_122254_TradingView.jpg
Size: 258 KB](/attachment/image/4890552/thumbnail?d=1738516983)](/attachment/image/4890552?d=1738516983)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#375](/thread/post/15135787#post15135787 "Post Permalink")

  * Feb 3, 2025 2:25am  Feb 3, 2025 2:25am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

> [Quoting pipcruiser](/thread/post/15135502#post15135502 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi ML, Could you give the name of the TV "diamond indicator" - thanks in advance buddy. PC
> 
> Ignored

I wait for multiple bounces (diamonds) and then look for squeezes that have seen high compression and wait for a breakout. Use VCP and EMAS in confluence.  
  
Every timeframe works different for number of retests, types of squeezes and breakouts that work best together 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#376](/thread/post/15135890#post15135890 "Post Permalink")

  * Feb 3, 2025 5:05am  Feb 3, 2025 5:05am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot_20250202_150449_Photos.jpg
Size: 333 KB](/attachment/image/4890606/thumbnail?d=1738526704)](/attachment/image/4890606?d=1738526704)   

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#377](/thread/post/15136193#post15136193 "Post Permalink")

  * Feb 3, 2025 10:05am  Feb 3, 2025 10:05am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot_20250202_200433_Photos.jpg
Size: 313 KB](/attachment/image/4890755/thumbnail?d=1738544700)](/attachment/image/4890755?d=1738544700)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#378](/thread/post/15136293#post15136293 "Post Permalink")

  * Feb 3, 2025 12:09pm  Feb 3, 2025 12:09pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

> [Quoting MachineLearn](/thread/post/15136193#post15136193 "View Quoted Post")
> 
> Disliked
> 
> {image}
> 
> Ignored

Continued to fall 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot_20250202_220923_Photos.jpg
Size: 291 KB](/attachment/image/4890829/thumbnail?d=1738552176)](/attachment/image/4890829?d=1738552176)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#379](/thread/post/15136646#post15136646 "Post Permalink")

  * Feb 3, 2025 7:27pm  Feb 3, 2025 7:27pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar35901_4.gif) pipcruiser](pipcruiser)

  * Joined Mar 2007 | Status: One life - live it... | [601 Posts](/search?do=process&provider=Member&searchuser=35901)

> [Quoting MachineLearn](/thread/post/15135787#post15135787 "View Quoted Post")
> 
> Disliked
> 
> {quote} I wait for multiple bounces (diamonds) and then look for squeezes that have seen high compression and wait for a breakout. Use VCP and EMAS in confluence. Every timeframe works different for number of retests, types of squeezes and breakouts that work best together
> 
> Ignored

Thanks a lot!  
  
PC 

Less is more...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#380](/thread/post/15136907#post15136907 "Post Permalink")

  * Edited 11:32pm  Feb 3, 2025 11:10pm | Edited 11:32pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1967050_1.gif) Ju4ara](ju4ara)

  * | Joined Oct 2024  | Status: Trader | [105 Posts](/search?do=process&provider=Member&searchuser=1967050)

took this trade on gold, great vcp pattern, A++  
  
EDIT: I didn't like pa around my tp so took 4.5R instead of 5R  
EDIT 2: Got to wait a bit more and would take full tp, but still great result 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 104 KB](/attachment/image/4891226/thumbnail?d=1738591858)](/attachment/image/4891226?d=1738591858)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Squeeze n Go | MTF System
  *   * [ **Reply to Thread** ](/thread/1319487-squeeze-n-go-mtf-system/reply#reply)

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

[Spud's MTF FIB Breakout System](/thread/30109-spuds-mtf-fib-breakout-system "Spud's MTF FIB Breakout System 
-------------------------------- 
Ever since I learned about Fibonacci numbers they have interested my pure...") 375 replies

[H1Scalper System (MTF D1,H1,M5)](/thread/166646-h1scalper-system-mtf-d1h1m5 "Here are the indicators for a manual system. 
  
Explanations, rules and trading ideas are coming... 
. 
\(2009.05.13\) 
Attached are the...") 725 replies

[MTF Trix system](/thread/183801-mtf-trix-system "Hello everybody, 
 
This thread is for developing and discussing a multi-timeframe trading system that is based on one indicator - Trix -...") 3,697 replies

[MTF Stochastics into MTF Stoch Histogram](/thread/359918-mtf-stochastics-into-mtf-stoch-histogram "Hi, 
 
I have been trading with the help of MTF Stochastics for a few weeks now with relatively good results but would appreciate if...") 8 replies

[MTF Vajioo Scalping System](/thread/195912-mtf-vajioo-scalping-system "RUBBISH") 15 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/1319487-squeeze-n-go-mtf-system/reply#reply)
  * Subscribe
  * [216](javascript:void\(0\);)

Attachments: Squeeze n Go | MTF System

Tags: Squeeze n Go | MTF System

#  [](/thread/1319487-squeeze-n-go-mtf-system)Squeeze n Go | MTF System 

  * 

  * [#381](/thread/post/15137001#post15137001 "Post Permalink")

  * Feb 3, 2025 11:56pm  Feb 3, 2025 11:56pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

> [Quoting MachineLearn](/thread/post/15136293#post15136293 "View Quoted Post")
> 
> Disliked
> 
> {quote} Continued to fall {image}
> 
> Ignored

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot_20250203_095620_Photos.jpg
Size: 293 KB](/attachment/image/4891282/thumbnail?d=1738594594)](/attachment/image/4891282?d=1738594594)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#382](/thread/post/15138954#post15138954 "Post Permalink")

  * Feb 5, 2025 4:01am  Feb 5, 2025 4:01am 

  * [ yeezey](yeezey)

  * | Joined Oct 2024  | Status: Trader | [1 Post](/search?do=process&provider=Member&searchuser=1969239)

> [Quoting RickM](/thread/post/15135003#post15135003 "View Quoted Post")
> 
> Disliked
> 
> I have traded with Driven a few years back and we love to disagree on one subject - VOLUME There is no chance in hell he will ever consider Volume data is of much value in trading, so no point wasting time here debating with him this subject matter. But, perhaps there is one other trader reading this post that can see something in this chart below that may just change their opinion slightly. Volume Data is best used by applying VWAP to intraday charts to show us where the professionals are Buying or Selling. Its next best used for watching the tape...
> 
> Ignored

where did you guys learned to read the tape and trade? im 4 years persuing to be a trader, but not seeing much improvement, appreciate it 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#383](/thread/post/15139110#post15139110 "Post Permalink")

  * Feb 5, 2025 7:06am  Feb 5, 2025 7:06am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot_20250204_170639_Photos.jpg
Size: 250 KB](/attachment/image/4892398/thumbnail?d=1738706815)](/attachment/image/4892398?d=1738706815)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#384](/thread/post/15139139#post15139139 "Post Permalink")

  * Feb 5, 2025 7:55am  Feb 5, 2025 7:55am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar426855_1.gif) RickM](rickm)

  * Joined Sep 2015 | Status: Trader | [2,439 Posts](/search?do=process&provider=Member&searchuser=426855)

> [Quoting yeezey](/thread/post/15138954#post15138954 "View Quoted Post")
> 
> Disliked
> 
> {quote} where did you guys learned to read the tape and trade? im 4 years persuing to be a trader, but not seeing much improvement, appreciate it
> 
> Ignored

Hi yeezey  
  
First of all you need to trade Future’s or Stocks to even see a tape (DOM or Time & Sales) so that is where you start.  
I learned basic tape reading skills years ago trading Australian Equities but it wasn’t till I started trading Future’s on Jigsaw that I was able to get a better feel for it.  
For 1 year, I traded ES (US500 Futures) only with just a DOM, volume profile and a 5 second tick chart where I would watch every tick for over 4 hours. Here I was learning to trade Tick rejections, sweeps, incomplete auctions, liquidity claims, spoofing, HFT manipulation etc to gain a trading edge over other market participants.  
  
The idea is we are attempting to identify whether a move is being created due to order manipulation or actual big player intent.  
  
These days I study closely on ES, Oil, Gold, EU Future’s to see whether the order size that is hitting the DOM is being accepted and moving price or is it being rejected in the form of a back tick.  
  
So I trade my setups like Sqeeze breakouts, VCP Patterns, Liquidity Claims, pullback Patterns then look to trade with the aid of a DOM to see when a move has volume intend from many other trading participants or if it’s from Algo HFT programs.  
  
If you are interest in DOM trading, check out Fat Cat on YouTube.  
  
Cheers 

Trading thin liquidity at the boundary of the charts

[0 ](javascript:void\(0\);) [5 ](javascript:void\(0\);)

  * [#385](/thread/post/15141589#post15141589 "Post Permalink")

  * Edited 12:47am  Feb 7, 2025 12:22am | Edited 12:47am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar272159_71.gif) driven18](driven18)

  * Joined Jul 2012 | Status: Trader | [1,385 Posts](/search?do=process&provider=Member&searchuser=272159)

This NASDAQ trade is dedicated **to RickM** for bringing me back to trade ENQ futures.  
  
Although there is **no Volume involved whatsoever and no Liquidity Claims![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)** , this dedication is True and Valid. ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f37a.png?v=15.1)  
  
Above EMA 21, 5 Min Nasdaq Futures, Will be TP(ing) very very soon....and out **\+ 2%**. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 15 KB](/attachment/image/4893813/thumbnail?d=1738855271)](/attachment/image/4893813?d=1738855271)   

[0 ](javascript:void\(0\);) [4 ](javascript:void\(0\);)

  * [#386](/thread/post/15141627#post15141627 "Post Permalink")

  * Edited 9:26am  Feb 7, 2025 12:41am | Edited 9:26am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar272159_71.gif) driven18](driven18)

  * Joined Jul 2012 | Status: Trader | [1,385 Posts](/search?do=process&provider=Member&searchuser=272159)

I would like to expand a bit on how I traded this PA and my thought process as it relates to this thread.  
  
1\. PA moved above EMA 21  
2\. Retracement during the squeeze (and white dots prior)  
3\. Strong push up  
4\. Most of the traders who place their stop loss under the Swing were taken out of this trade. Do not do this, leave some room for PA to breeze(hint - use proper position size). 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 61 KB](/attachment/image/4893833/thumbnail?d=1738856647)](/attachment/image/4893833?d=1738856647)   

[0 ](javascript:void\(0\);) [6 ](javascript:void\(0\);)

  * [#387](/thread/post/15142106#post15142106 "Post Permalink")

  * Feb 7, 2025 12:57pm  Feb 7, 2025 12:57pm 

  * [ kalimac1](kalimac1)

  * | Joined Jul 2024  | Status: Trader | [13 Posts](/search?do=process&provider=Member&searchuser=1905061)

Can I take a long position here? 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 23 KB](/attachment/image/4894151/thumbnail?d=1738901073)](/attachment/image/4894151?d=1738901073)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#388](/thread/post/15142518#post15142518 "Post Permalink")

  * Feb 7, 2025 9:33pm  Feb 7, 2025 9:33pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar2023811_1.gif) CogAlpha](cogalpha)

  * Joined Jan 2025 | Status: Trader | [231 Posts](/search?do=process&provider=Member&searchuser=2023811)

Hey guys... here is the Script I have build based on what was written in this Thread.   
Let me know if there are things you think are wrong.   
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 31 KB](/attachment/image/4894424/thumbnail?d=1738931543)](/attachment/image/4894424?d=1738931543)   

  
[https://www.tradingview.com/script/z...eze-Intensity/](https://www.tradingview.com/script/zsIFK9N3-COG-Adaptive-Squeeze-Intensity/)  
  
  
![](https://resources.faireconomy.media/images/emojis/64/2b50.png?v=15.1) Key Features

  1. ![](https://resources.faireconomy.media/images/emojis/64/1f4c8.png?v=15.1) Comprehensive squeeze intensity scoring system (0-100)
  2. ![](https://resources.faireconomy.media/images/emojis/64/1f4cf.png?v=15.1) Multiple Keltner Channel compression zones
  3. ![](https://resources.faireconomy.media/images/emojis/64/1f4ca.png?v=15.1) Volume analysis integration
  4. ![](https://resources.faireconomy.media/images/emojis/64/1f3af.png?v=15.1) EMA-based trend confirmation
  5. ![](https://resources.faireconomy.media/images/emojis/64/1f3a8.png?v=15.1) Proximity-based entry validation
  6. ![](https://resources.faireconomy.media/images/emojis/64/1f4f1.png?v=15.1) Visual status monitoring
  7. ![](https://resources.faireconomy.media/images/emojis/64/1f3a8.png?v=15.1) Customizable color schemes
  8. ![](https://resources.faireconomy.media/images/emojis/64/26a1.png?v=15.1) Clear entry signals with directional indicators

![](https://resources.faireconomy.media/images/emojis/64/1f527.png?v=15.1) Components  
1\. ![](https://resources.faireconomy.media/images/emojis/64/1f4d0.png?v=15.1) Squeeze Intensity Score (0-100)  
The indicator calculates a total squeeze intensity score based on four components:

  1. ![](https://resources.faireconomy.media/images/emojis/64/1f4ca.png?v=15.1) Band Convergence (0-40 points): Measures the relationship between Bollinger Bands and Keltner Channels
  2. ![](https://resources.faireconomy.media/images/emojis/64/1f4cd.png?v=15.1) Price Position (0-20 points): Evaluates price location relative to the base channels
  3. ![](https://resources.faireconomy.media/images/emojis/64/1f4c8.png?v=15.1) Volume Intensity (0-20 points): Analyzes volume patterns and thresholds
  4. ![](https://resources.faireconomy.media/images/emojis/64/26a1.png?v=15.1) Momentum (0-20 points): Assesses price momentum and direction

2\. ![](https://resources.faireconomy.media/images/emojis/64/1f3a8.png?v=15.1) Compression Zones  
Visual representation of squeeze intensity levels:

  1. ![](https://resources.faireconomy.media/images/emojis/64/1f534.png?v=15.1) Extreme Squeeze (80-100): Red zone
  2. ![](https://resources.faireconomy.media/images/emojis/64/1f7e0.png?v=15.1) Strong Squeeze (60-80): Orange zone
  3. ![](https://resources.faireconomy.media/images/emojis/64/1f7e1.png?v=15.1) Moderate Squeeze (40-60): Yellow zone
  4. ![](https://resources.faireconomy.media/images/emojis/64/1f7e2.png?v=15.1) Light Squeeze (20-40): Green zone
  5. ![](https://resources.faireconomy.media/images/emojis/64/26aa.png?v=15.1) No Squeeze (0-20): Base zone

3\. ![](https://resources.faireconomy.media/images/emojis/64/1f3af.png?v=15.1) Entry Signals  
The indicator generates entry signals based on:

  1. ![](https://resources.faireconomy.media/images/emojis/64/2728.png?v=15.1) Squeeze release confirmation
  2. ![](https://resources.faireconomy.media/images/emojis/64/27a1-fe0f.png?v=15.1) Momentum direction
  3. ![](https://resources.faireconomy.media/images/emojis/64/1f4ca.png?v=15.1) Candlestick pattern confirmation
  4. ![](https://resources.faireconomy.media/images/emojis/64/1f4c8.png?v=15.1) Optional EMA trend alignment
  5. ![](https://resources.faireconomy.media/images/emojis/64/1f3af.png?v=15.1) Customizable EMA proximity validation

[0 ](javascript:void\(0\);) [5 ](javascript:void\(0\);)

  * [#389](/thread/post/15142582#post15142582 "Post Permalink")

  * Feb 7, 2025 10:23pm  Feb 7, 2025 10:23pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1746342_1.gif) MachineLearn](machinelearn)

  * Joined Nov 2023 | Status: Trader | [1,286 Posts](/search?do=process&provider=Member&searchuser=1746342)

> [Quoting CogAlpha](/thread/post/15142518#post15142518 "View Quoted Post")
> 
> Disliked
> 
> Hey guys... here is the Script I have build based on what was written in this Thread. Let me know if there are things you think are wrong. {image} [https://www.tradingview.com/script/z...eze-Intensity/](https://www.tradingview.com/script/zsIFK9N3-COG-Adaptive-Squeeze-Intensity/) ![](https://resources.faireconomy.media/images/emojis/64/2b50.png?v=15.1) Key Features ![](https://resources.faireconomy.media/images/emojis/64/1f4c8.png?v=15.1) Comprehensive squeeze intensity scoring system (0-100) ![](https://resources.faireconomy.media/images/emojis/64/1f4cf.png?v=15.1) Multiple Keltner Channel compression zones ![](https://resources.faireconomy.media/images/emojis/64/1f4ca.png?v=15.1) Volume analysis integration ![](https://resources.faireconomy.media/images/emojis/64/1f3af.png?v=15.1) EMA-based trend confirmation ![](https://resources.faireconomy.media/images/emojis/64/1f3a8.png?v=15.1) Proximity-based entry validation ![](https://resources.faireconomy.media/images/emojis/64/1f4f1.png?v=15.1) Visual status monitoring ![](https://resources.faireconomy.media/images/emojis/64/1f3a8.png?v=15.1)...
> 
> Ignored

Wow you put in a lot of work. Thank you.   
  
Looks good from a quick glance! 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#390](/thread/post/15142629#post15142629 "Post Permalink")

  * Feb 7, 2025 10:41pm  Feb 7, 2025 10:41pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar2023811_1.gif) CogAlpha](cogalpha)

  * Joined Jan 2025 | Status: Trader | [231 Posts](/search?do=process&provider=Member&searchuser=2023811)

> [Quoting MachineLearn](/thread/post/15142582#post15142582 "View Quoted Post")
> 
> Disliked
> 
> {quote} Wow you put in a lot of work. Thank you. Looks good from a quick glance!
> 
> Ignored

Thank you! hope its helpful for some.   
  
big Love ![](https://resources.faireconomy.media/images/emojis/64/2764-fe0f.png?v=15.1)

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#391](/thread/post/15143415#post15143415 "Post Permalink")

  * Feb 8, 2025 4:17pm  Feb 8, 2025 4:17pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar426855_1.gif) RickM](rickm)

  * Joined Sep 2015 | Status: Trader | [2,439 Posts](/search?do=process&provider=Member&searchuser=426855)

> [Quoting kalimac1](/thread/post/15142106#post15142106 "View Quoted Post")
> 
> Disliked
> 
> Can I take a long position here? {image}
> 
> Ignored

Hi Kalimac  
  
I wouldn't now mainly because price action shows 3 failed bullish moves.  
Now we would have to wait for a break of the last major high - so wait to see if this occurs.  
My guess is these candles are forming during a low liquidity period so there is no Bullish intent.  
  
Cheers 

Trading thin liquidity at the boundary of the charts

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#392](/thread/post/15143486#post15143486 "Post Permalink")

  * Feb 8, 2025 9:04pm  Feb 8, 2025 9:04pm 

  * [ MarcoSx](marcosx)

  * | Joined Jan 2025  | Status: Trader | [8 Posts](/search?do=process&provider=Member&searchuser=2038487)

> [Quoting CogAlpha](/thread/post/15142518#post15142518 "View Quoted Post")
> 
> Disliked
> 
> Hey guys... here is the Script I have build based on what was written in this Thread. Let me know if there are things you think are wrong. {image} [https://www.tradingview.com/script/z...eze-Intensity/](https://www.tradingview.com/script/zsIFK9N3-COG-Adaptive-Squeeze-Intensity/) ![](https://resources.faireconomy.media/images/emojis/64/2b50.png?v=15.1) Key Features ![](https://resources.faireconomy.media/images/emojis/64/1f4c8.png?v=15.1) Comprehensive squeeze intensity scoring system (0-100) ![](https://resources.faireconomy.media/images/emojis/64/1f4cf.png?v=15.1) Multiple Keltner Channel compression zones ![](https://resources.faireconomy.media/images/emojis/64/1f4ca.png?v=15.1) Volume analysis integration ![](https://resources.faireconomy.media/images/emojis/64/1f3af.png?v=15.1) EMA-based trend confirmation ![](https://resources.faireconomy.media/images/emojis/64/1f3a8.png?v=15.1) Proximity-based entry validation ![](https://resources.faireconomy.media/images/emojis/64/1f4f1.png?v=15.1) Visual status monitoring ![](https://resources.faireconomy.media/images/emojis/64/1f3a8.png?v=15.1)...
> 
> Ignored

I won't discourage your effort, as I've coded couple of scripts around the squeeze myself, which is not an easy task. If you wait for all the confirmations for the signal, then you are likely late to the party all the time, consequently your are shorting the bottom or buying the top. The current version would be more useful to confirm where to exit the position.  
  
Just a hint where you should focus more of your time, try to code/test rules where the entry is the most convenient to catch the move. Simple question with a hard answer, how can you define the situation where the impulsive move begins? 

[0 ](javascript:void\(0\);) [4 ](javascript:void\(0\);)

  * [#393](/thread/post/15143560#post15143560 "Post Permalink")

  * Feb 9, 2025 12:22am  Feb 9, 2025 12:22am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar588299_3.gif) RiskFighter](riskfighter)

  * Joined Jun 2017 | Status: Trader | [1,566 Posts](/search?do=process&provider=Member&searchuser=588299) | Online Now 

> [Quoting MarcoSx](/thread/post/15143486#post15143486 "View Quoted Post")
> 
> Disliked
> 
> {quote} I won't discourage your effort, as I've coded couple of scripts around the squeeze myself, which is not an easy task. If you wait for all the confirmations for the signal, then you are likely late to the party all the time, consequently your are shorting the bottom or buying the top. The current version would be more useful to confirm where to exit the position. Just a hint where you should focus more of your time, try to code/test rules where the entry is the most convenient to catch the move. Simple question with a hard answer, how can...
> 
> Ignored

Read his post again. Cog has made a script based on things discussed in this thread. If you think focus is not correct, then talk to Machine and Rick. Just a hint. 

Read post #1 !! Then read it again 10 more times before you ask.

[0 ](javascript:void\(0\);) [3 ](javascript:void\(0\);)

  * [#394](/thread/post/15143583#post15143583 "Post Permalink")

  * Feb 9, 2025 1:01am  Feb 9, 2025 1:01am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar2023811_1.gif) CogAlpha](cogalpha)

  * Joined Jan 2025 | Status: Trader | [231 Posts](/search?do=process&provider=Member&searchuser=2023811)

> [Quoting MarcoSx](/thread/post/15143486#post15143486 "View Quoted Post")
> 
> Disliked
> 
> {quote} I won't discourage your effort, as I've coded couple of scripts around the squeeze myself, which is not an easy task. If you wait for all the confirmations for the signal, then you are likely late to the party all the time, consequently your are shorting the bottom or buying the top. The current version would be more useful to confirm where to exit the position. Just a hint where you should focus more of your time, try to code/test rules where the entry is the most convenient to catch the move. Simple question with a hard answer, how can...
> 
> Ignored

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 39 KB](/attachment/image/4895040/thumbnail?d=1739030485)](/attachment/image/4895040?d=1739030485)   

  
play with the settings... hint... increase the BB multiplier... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#395](/thread/post/15143586#post15143586 "Post Permalink")

  * Feb 9, 2025 1:09am  Feb 9, 2025 1:09am 

  * [ MarcoSx](marcosx)

  * | Joined Jan 2025  | Status: Trader | [8 Posts](/search?do=process&provider=Member&searchuser=2038487)

If I wasn't familiar with the thread, Rick's ideas, I wouldn't bother to add an opinion related to my experience. I tried to help you and other members also, instead got replies with irony. Nevermind. Enjoy your weekend. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#396](/thread/post/15143740#post15143740 "Post Permalink")

  * Edited 9:42am  Feb 9, 2025 9:24am | Edited 9:42am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar426855_1.gif) RickM](rickm)

  * Joined Sep 2015 | Status: Trader | [2,439 Posts](/search?do=process&provider=Member&searchuser=426855)

> [Quoting abuislam](/thread/post/15143438#post15143438 "View Quoted Post")
> 
> Disliked
> 
> Great breakdown! The integration of TTM Squeeze Pro with EMA trend ribbons makes sense for filtering fakeouts. Have you tested this strategy on different market conditions, like ranging vs. trending markets? Would love to hear your insights!
> 
> Ignored

Hi abuisiam  
  
The idea here is we are looking for markets that are in ranging conditions, then hope to time our trades when the market breaks actually out into trending conditions soon after. The A+ trade is the breakout that occurs on a lower time frame market that has a bias that follows the higher time frame trend.  
  
This was one of my best trades from last year. Price was trending on the BTC Day chart and I waited for the breakout on the BTC 1 hour time frame to trade.  
With Forex Markets, I look for trending Day charts first and hunt for breakouts on the 1 hour chart thereafter.  
  
I have learned successful traders Buy when the market is very strong with support under price and Sell when the market is very weak with support above price.  
Most traders want to do the opposite by Selling high or Buying low and that is why many of them lose (They may win 4 in a row but the 5th trade destroys them).  
The Squeeze indicator alerts us to nice setups if we aren't paying attention. It's our job to establish whether its a A+. B or C setup.  
  
Cheers 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: btc nov.png
Size: 160 KB](/attachment/image/4895116/thumbnail?d=1739060687)](/attachment/image/4895116?d=1739060687)   

Trading thin liquidity at the boundary of the charts

[0 ](javascript:void\(0\);) [7 ](javascript:void\(0\);)

  * [#397](/thread/post/15143854#post15143854 "Post Permalink")

  * Feb 9, 2025 6:24pm  Feb 9, 2025 6:24pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar2023811_1.gif) CogAlpha](cogalpha)

  * Joined Jan 2025 | Status: Trader | [231 Posts](/search?do=process&provider=Member&searchuser=2023811)

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 64 KB](/attachment/image/4895197/thumbnail?d=1739093079)](/attachment/image/4895197?d=1739093079)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#398](/thread/post/15143858#post15143858 "Post Permalink")

  * Feb 9, 2025 6:53pm  Feb 9, 2025 6:53pm 

  * [ kalimac1](kalimac1)

  * | Joined Jul 2024  | Status: Trader | [13 Posts](/search?do=process&provider=Member&searchuser=1905061)

> [Quoting RickM](/thread/post/15143415#post15143415 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi Kalimac I wouldn't now mainly because price action shows 3 failed bullish moves. Now we would have to wait for a break of the last major high - so wait to see if this occurs. My guess is these candles are forming during a low liquidity period so there is no Bullish intent. Cheers
> 
> Ignored

thanks for your advice, PA still stuck under top 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 19 KB](/attachment/image/4895200/thumbnail?d=1739094796)](/attachment/image/4895200?d=1739094796)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#399](/thread/post/15144259#post15144259 "Post Permalink")

  * Edited 12:20pm  Feb 10, 2025 11:39am | Edited 12:20pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar588299_3.gif) RiskFighter](riskfighter)

  * Joined Jun 2017 | Status: Trader | [1,566 Posts](/search?do=process&provider=Member&searchuser=588299) | Online Now 

> [Quoting RickM](/thread/post/15143740#post15143740 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi abuisiam The idea here is we are looking for markets that are in ranging conditions, then hope to time our trades when the market breaks actually out into trending conditions soon after. The A+ trade is the breakout that occurs on a lower time frame market that has a bias that follows the higher time frame trend. This was one of my best trades from last year. Price was trending on the BTC Day chart and I waited for the breakout on the BTC 1 hour time frame to trade. With Forex Markets, I look for trending Day charts first and hunt for...
> 
> Ignored

From Rick's post: "_The A+ trade is the breakout that occurs on a lower time frame market that has a bias that follows the higher time frame trend_."  
  
So you need to know the trend.  
  
I don't know if this has a value for some of the MT4 traders, but let me share it. I made my own **Multi Timeframe MT4 Ribbon indicator**. You can define the EMA's you want. Only three though and Machine define four in post #1.  
  
So using this indicator you can watch if the EMA's are aligned nicely in higher timeframes.  
  
You can define three colours.  
AColour: The arrow get this colour if the MA is trending AND the very last data is still trending.  
BColour: The arrow get this colour if the MA is trending BUT the last closed bar goes in the other direction than the trend.  
NoColour: The EMA's are cluttered - no aligment - not tradeable.  
  
Standard colours are White, Yellow and Red. (Changeable).  
  
The red colour is used in case of the cluttered picture. In this case there will be a dot in stead of an arrow.  
  
Please understand that this is a quickie. You cannot move the indicator to other locations in this version.and there might be other smart features it does not have.  
  
**Never** trade based only on the indicator. You MUST make your own top/down analysis. It is ment as a help, not a trading signal.  
  
Let me know if you find errors.  
  
Attached an example of the situation on timeframe M5, where the situation is cluttered and the indicator shows a dot.  
  

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: < 1 KB](/attachment/image/4895464/thumbnail?d=1739155364)](/attachment/image/4895464?d=1739155364)   
[![Click to Enlarge

Name: screenshot.png
Size: 28 KB](/attachment/image/4895465/thumbnail?d=1739155582)](/attachment/image/4895465?d=1739155582)   
[![Click to Enlarge

Name: screenshot.png
Size: 23 KB](/attachment/image/4895466/thumbnail?d=1739155655)](/attachment/image/4895466?d=1739155655)   

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [TribleRibbon_1.ex4](/attachment/file/4895460?d=1739155148) 11 KB | 52 downloads 

Read post #1 !! Then read it again 10 more times before you ask.

[0 ](javascript:void\(0\);) [4 ](javascript:void\(0\);)

  * [#400](/thread/post/15144340#post15144340 "Post Permalink")

  * Feb 10, 2025 2:21pm  Feb 10, 2025 2:21pm 

  * [ kalimac1](kalimac1)

  * | Joined Jul 2024  | Status: Trader | [13 Posts](/search?do=process&provider=Member&searchuser=1905061)

> [Quoting RickM](/thread/post/15143740#post15143740 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi abuisiam The idea here is we are looking for markets that are in ranging conditions, then hope to time our trades when the market breaks actually out into trending conditions soon after. The A+ trade is the breakout that occurs on a lower time frame market that has a bias that follows the higher time frame trend. This was one of my best trades from last year. Price was trending on the BTC Day chart and I waited for the breakout on the BTC 1 hour time frame to trade. With Forex Markets, I look for trending Day charts first and hunt for...
> 
> Ignored

> Quote
> 
> Disliked
> 
> **Selling high or Buying low**

Hi RickM  
As I understand it this means: find top and bottom of the market  

> Quote
> 
> Disliked
> 
> **Buy when the market is very strong with support under price and Sell when the market is very weak with support above price**

I don't understand this clearly.  
Can you please give me some examples of this. Thanks a lot 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Squeeze n Go | MTF System
  *   * [ **Reply to Thread** ](/thread/1319487-squeeze-n-go-mtf-system/reply#reply)

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

[Spud's MTF FIB Breakout System](/thread/30109-spuds-mtf-fib-breakout-system "Spud's MTF FIB Breakout System 
-------------------------------- 
Ever since I learned about Fibonacci numbers they have interested my pure...") 375 replies

[H1Scalper System (MTF D1,H1,M5)](/thread/166646-h1scalper-system-mtf-d1h1m5 "Here are the indicators for a manual system. 
  
Explanations, rules and trading ideas are coming... 
. 
\(2009.05.13\) 
Attached are the...") 725 replies

[MTF Trix system](/thread/183801-mtf-trix-system "Hello everybody, 
 
This thread is for developing and discussing a multi-timeframe trading system that is based on one indicator - Trix -...") 3,697 replies

[MTF Stochastics into MTF Stoch Histogram](/thread/359918-mtf-stochastics-into-mtf-stoch-histogram "Hi, 
 
I have been trading with the help of MTF Stochastics for a few weeks now with relatively good results but would appreciate if...") 8 replies

[MTF Vajioo Scalping System](/thread/195912-mtf-vajioo-scalping-system "RUBBISH") 15 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/1319487-squeeze-n-go-mtf-system/reply#reply)
  * Subscribe
  * [216](javascript:void\(0\);)

Attachments: Squeeze n Go | MTF System

Tags: Squeeze n Go | MTF System

#  [](/thread/1319487-squeeze-n-go-mtf-system)Squeeze n Go | MTF System 

  * 

  * [#401](/thread/post/15144518#post15144518 "Post Permalink")

  * Feb 10, 2025 6:19pm  Feb 10, 2025 6:19pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar588299_3.gif) RiskFighter](riskfighter)

  * Joined Jun 2017 | Status: Trader | [1,566 Posts](/search?do=process&provider=Member&searchuser=588299) | Online Now 

> [Quoting CogAlpha](/thread/post/15142518#post15142518 "View Quoted Post")
> 
> Disliked
> 
> Hey guys... here is the Script I have build based on what was written in this Thread. Let me know if there are things you think are wrong. {image} [https://www.tradingview.com/script/z...eze-Intensity/](https://www.tradingview.com/script/zsIFK9N3-COG-Adaptive-Squeeze-Intensity/) ![](https://resources.faireconomy.media/images/emojis/64/2b50.png?v=15.1) Key Features ![](https://resources.faireconomy.media/images/emojis/64/1f4c8.png?v=15.1) Comprehensive squeeze intensity scoring system (0-100) ![](https://resources.faireconomy.media/images/emojis/64/1f4cf.png?v=15.1) Multiple Keltner Channel compression zones ![](https://resources.faireconomy.media/images/emojis/64/1f4ca.png?v=15.1) Volume analysis integration ![](https://resources.faireconomy.media/images/emojis/64/1f3af.png?v=15.1) EMA-based trend confirmation ![](https://resources.faireconomy.media/images/emojis/64/1f3a8.png?v=15.1) Proximity-based entry validation ![](https://resources.faireconomy.media/images/emojis/64/1f4f1.png?v=15.1) Visual status monitoring ![](https://resources.faireconomy.media/images/emojis/64/1f3a8.png?v=15.1)...
> 
> Ignored

Hi Cog

  1. ![](https://resources.faireconomy.media/images/emojis/64/1f4c8.png?v=15.1) Comprehensive squeeze intensity scoring system (0-100)

This is interesting. How do you make that measure?? 

Read post #1 !! Then read it again 10 more times before you ask.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#402](/thread/post/15144636#post15144636 "Post Permalink")

  * Feb 10, 2025 7:58pm  Feb 10, 2025 7:58pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar2023811_1.gif) CogAlpha](cogalpha)

  * Joined Jan 2025 | Status: Trader | [231 Posts](/search?do=process&provider=Member&searchuser=2023811)

> [Quoting RiskFighter](/thread/post/15144518#post15144518 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi Cog ![](https://resources.faireconomy.media/images/emojis/64/1f4c8.png?v=15.1) Comprehensive squeeze intensity scoring system (0-100) This is interesting. How do you make that measure??
> 
> Ignored

Hey RiskFighter, I know you are a coder.   
My Script is open source, I believe the code can explain it better than I could put into written words.  
  
But let me know if there are things unclear (or even mistakes in my logic, I am just a hobby coder) 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#403](/thread/post/15144659#post15144659 "Post Permalink")

  * Feb 10, 2025 8:06pm  Feb 10, 2025 8:06pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar588299_3.gif) RiskFighter](riskfighter)

  * Joined Jun 2017 | Status: Trader | [1,566 Posts](/search?do=process&provider=Member&searchuser=588299) | Online Now 

> [Quoting CogAlpha](/thread/post/15144636#post15144636 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hey RiskFighter, I know you are a coder. My Script is open source, I believe the code can explain it better than I could put into written words. But let me know if there are things unclear (or even mistakes in my logic, I am just a hobby coder)
> 
> Ignored

Damned - my lazy gene are hurt ;-) OK, I will take a look.  
  
Thanks for responding. 

Read post #1 !! Then read it again 10 more times before you ask.

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#404](/thread/post/15144677#post15144677 "Post Permalink")

  * Feb 10, 2025 8:20pm  Feb 10, 2025 8:20pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar426855_1.gif) RickM](rickm)

  * Joined Sep 2015 | Status: Trader | [2,439 Posts](/search?do=process&provider=Member&searchuser=426855)

> [Quoting kalimac1](/thread/post/15144340#post15144340 "View Quoted Post")
> 
> Disliked
> 
> {quote} {quote} Hi RickM As I understand it this means: find top and bottom of the market {quote} I don't understand this clearly. Can you please give me some examples of this. Thanks a lot
> 
> Ignored

Hi Kalimac  
  
I mean we should be Buying at Highs or Selling at new lows provided price has bounced off Resistance - see my chart below.  
( Algo's help because they spoof the market on new highs & lows which supports breakouts ie. I want to see spoofing)  
  
Here's an example of my trading NQ today during the London Session today. Generally it's slow on Monday which is a nice way to start the week.  
My goal is to earn a wage every single night just doing this on ES / NQ or Gold. So generally I am targeting around $500-$700 profit to cover my daily expenses trading these 3 setups.  
  
Here is three plays from my playbook. All three setups rely on being able to read the tape.  
  
1\. Fade Resistance (yellow)  
2\. Breakout of Resistance on solid Ask/Bid imbalance (Green)  
3\. Ask & Bid Flipping on aggressive liquidity runs. (Purple)  
  
The secret of trading in my eyes is to trade off Resistance levels. So in a breakout, I want price to bounce of Resistance area and the I want to see the Tape support direction.  
When price makes NEW HIGHS, we should be only looking for Buys and we should take trades above Resistance.  
  
SKILL  
  
This is what real trading skill is about, fearless entry's using supply & demand to TAKE THE CORRECT TRADES.  
Practise - Practise - Practise  
  
  
THEN  
  
If during the process of earning a days pay with these 3 plays, I also see a Squeeze Setup, a VCP Pattern or a AVWAP play then I will take it.  
  
Otherwise I just trade my 3 plays and read the bloody tape.  
  
PS. I lost one trade here, can't remember which one  
PS. Hint - To trade the NQ Tape, Read MNQ Tape instead. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Tape Read 2.png
Size: 257 KB](/attachment/image/4895722/thumbnail?d=1739186413)](/attachment/image/4895722?d=1739186413)   

Trading thin liquidity at the boundary of the charts

[0 ](javascript:void\(0\);) [3 ](javascript:void\(0\);)

  * [#405](/thread/post/15144686#post15144686 "Post Permalink")

  * Edited 10:15pm  Feb 10, 2025 8:27pm | Edited 10:15pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar588299_3.gif) RiskFighter](riskfighter)

  * Joined Jun 2017 | Status: Trader | [1,566 Posts](/search?do=process&provider=Member&searchuser=588299) | Online Now 

TW has now implemented an ADBlocker check. As I am not paying and use an ADBlocker, I am not allowed to use TW. I find that absolutely fair.  
As I don't want to use TW, then I will not pay for it and it is now closed area for me.  
  
But I think I am covered in the matter of squeeze intencity, because my indicator (uploaded here) only call it a squeeze if the Keltner gets outside the Bollinger. Then it is serious bussiness.  
  
However I notice sometimes, that a squeeze only last for 1 or 2 bars. I might make a meassure that set some minimum number of squeezed bars in order to call it a squeeze. 

Read post #1 !! Then read it again 10 more times before you ask.

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#406](/thread/post/15144743#post15144743 "Post Permalink")

  * Edited 9:38pm  Feb 10, 2025 9:23pm | Edited 9:38pm 

  * [ MarcoSx](marcosx)

  * | Joined Jan 2025  | Status: Trader | [8 Posts](/search?do=process&provider=Member&searchuser=2038487)

> [Quoting RiskFighter](/thread/post/15144686#post15144686 "View Quoted Post")
> 
> Disliked
> 
> TW has now implemented an ADBlocker check. As I am not paying and use an ADBlocker, I am not allowed to use TW. I find that absolutely fair. As I don't want to use TW, then I will not pay for it and it is now closed area for me. But I think I am covered in the matter of squeeze intencity, because my indicator (uploaded here) only call it a squeeze if the Keltner gets outside the Bollinger. Then it is serious bussiness. However I notice sometimes, that a squeeze only last for 1 or 2 bars. I might make a meassure that set some minimum number of squeezed...
> 
> Ignored

Best squeezes happen FAST and if you want to partecipate in the move you have to pay the premium price since there is no pullback. By fast I mean the squeeze duration iseltf is around 2-6 bars, price and volume speed are also moving fast. Usually the move lasts only for several more bars, but the amount % in price change is large.  
  
On the other side you have SLOW/LONG squeezes which have duration of 30+ to infinite bars. This is where most people lose as there are many fakeouts. When the proper breakout happens, supported by volume it usually offers a retracement, the first pullback is the best entry. After a long squeeze, the move is steady and supported for longer time.  
  
Personally I am using a normalized bollinger band width, which I find more appropriate and sensitive to the extremes (on both sides) and when the volatility starts to rise, compared to the TTM squeeze. Basically it compares the width to prior compressions/extensions instead of local atr bands (keltner channel) as TTM. 

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#407](/thread/post/15144810#post15144810 "Post Permalink")

  * Feb 10, 2025 10:20pm  Feb 10, 2025 10:20pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar588299_3.gif) RiskFighter](riskfighter)

  * Joined Jun 2017 | Status: Trader | [1,566 Posts](/search?do=process&provider=Member&searchuser=588299) | Online Now 

> [Quoting MarcoSx](/thread/post/15144743#post15144743 "View Quoted Post")
> 
> Disliked
> 
> {quote} Best squeezes happen FAST and if you want to partecipate in the move you have to pay the premium price since there is no pullback. By fast I mean the squeeze duration iseltf is around 2-6 bars, price and volume speed are also moving fast. Usually the move lasts only for several more bars, but the amount % in price change is large. On the other side you have SLOW/LONG squeezes which have duration of 30+ to infinite bars. This is where most people lose as there are many fakeouts. When the proper breakout happens, supported by volume it usually...
> 
> Ignored

Thank you. That is valuable info.  
  
I will not use TW though. Am very happy with MT4 and I can make whatever tool I like there. 

Read post #1 !! Then read it again 10 more times before you ask.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#408](/thread/post/15147105#post15147105 "Post Permalink")

  * Feb 12, 2025 5:17pm  Feb 12, 2025 5:17pm 

  * [ kalimac1](kalimac1)

  * | Joined Jul 2024  | Status: Trader | [13 Posts](/search?do=process&provider=Member&searchuser=1905061)

Is there a good entry? 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 12 KB](/attachment/image/4897229/thumbnail?d=1739348232)](/attachment/image/4897229?d=1739348232)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#409](/thread/post/15155003#post15155003 "Post Permalink")

  * Last Post: Feb 19, 2025 3:59pm  Feb 19, 2025 3:59pm 

  * [ kalimac1](kalimac1)

  * | Joined Jul 2024  | Status: Trader | [13 Posts](/search?do=process&provider=Member&searchuser=1905061)

> [Quoting RickM](/thread/post/15144677#post15144677 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi Kalimac I mean we should be Buying at Highs or Selling at new lows provided price has bounced off Resistance - see my chart below. ( Algo's help because they spoof the market on new highs & lows which supports breakouts ie. I want to see spoofing) Here's an example of my trading NQ today during the London Session today. Generally it's slow on Monday which is a nice way to start the week. My goal is to earn a wage every single night just doing this on ES / NQ or Gold. So generally I am targeting around $500-$700 profit to cover my daily...
> 
> Ignored

thanks for sharing  
I have another question  
What will you do when this happen? 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 22 KB](/attachment/image/4901660/thumbnail?d=1739948343)](/attachment/image/4901660?d=1739948343)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Squeeze n Go | MTF System
  *   * [ **Reply to Thread** ](/thread/1319487-squeeze-n-go-mtf-system/reply#reply)

[](https://www.forexfactory.com "Homepage")

  * [Forums](forums)
  * [Trades](trades)
  * [Calendar](calendar)
  * [News](news)
  * [Market](market)
  * [Brokers](brokers)

****

[](https://www.faireconomy.com/)
