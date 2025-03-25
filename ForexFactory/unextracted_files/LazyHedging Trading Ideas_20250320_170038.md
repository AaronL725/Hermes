

  * 

[EurCad Analysis and Trading Ideas](/thread/360980-eurcad-analysis-and-trading-ideas "Hello my friends. 
 
As of lately I have had remarkable success in trading EurCad and after hearing other traders ideas I decided that we...") 594 replies

[FSP Trading Journal and Trend Ideas](/thread/427493-fsp-trading-journal-and-trend-ideas "hello  
I am trying to post some of my trade Ideas here. 
there will be trend following and counter trend trades. 
I will post image rather...") 16 replies

[Forex trading platform that doesn't take your ideas](/thread/311080-forex-trading-platform-that-doesnt-take-your-ideas "Ninja trader, Metatrader, Tradestation all can copy the EA and indicators straight out of your PC. 
 
How do we go about developing a...") 11 replies

[Program Your Trading Ideas without being a programmer](/thread/225629-program-your-trading-ideas-without-being-a-programmer "I have to admit, I have a lot of trading ideas, but no programming skills. I hate paying a programmer to take 3 days to write an EA for me,...") 4 replies

[Exchanging trading ideas](/thread/136764-exchanging-trading-ideas "I'm opening this thread as a substitute for live chat like msn etc to exchange trading ideas and to filter of some posts at Igrok's thread,...") 37 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/1058948-lazyhedging-trading-ideas/reply#reply)
  * Subscribe
  * [271](javascript:void\(0\);)

Attachments: LazyHedging Trading Ideas

Tags: LazyHedging Trading Ideas

#  [](/thread/1058948-lazyhedging-trading-ideas)LazyHedging Trading Ideas 

  * 

  * [#1](/thread/1058948-lazyhedging-trading-ideas "Post Permalink")

  * First Post: Edited Jan 23, 2022 2:49pm  Feb 7, 2021 7:40am | Edited Jan 23, 2022 2:49pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

**Starting with [Post #151](http://\[/COLOR), the idea of trading with the BodySwitch indicator is described and commented on.**  
**No new thread has been started yet, so please continue reading from this post.**  
  
**One should try to understand Note #4 below, because that is the idea of the Sliding Hedge. If one uses it, an optimal money management is automatically ensured.**  
**In[ Post #33 ](https://www.forexfactory.com/thread/post/13407947#post13407947) one can find an Excel sheet with a comparison of martingale levels. Those who can and want to should try to understand the calculations...**  
  
**############################################################################**  
  
In his thread "**Jake Bernstein 10 SMA high 8 SMA low trading system** " [https://www.forexfactory.com/thread/...high-8-sma-low](https://www.forexfactory.com/thread/1006033-jake-bernstein-10-sma-high-8-sma-low), _@Toto69_ presented his personal trading variant with some discretionary trading options. I used to read a couple of books by Jake and here I am posting some comments and indicators for the 10/8 trading idea.  
Here I only post a small indicator, and when I have time I will continue to post more things and an EA, but everyone can test their ideas and apply other trend following or counter trend variants.  
If any errors are found, I will update the indicators.  
  
**Note #1** \- The trend is determined when the body of a candle is above/below the HiLo MAs, and that is a little earlier than the rule with the 2-3 highs/lows outside the channel rule.  
  
**Note #2** \- The same indicator can be used for the trend of the upper time frame.  
One sees quite simply that in a trend zone (D1 e.g.) the number of green bars is greater than the red bars for the long direction e.g.  
For this reason, one should only take long trends on H1, for example, because the sections in the long direction can cause less losses.  
  
**Note #3** \- The indicator shows possible entries when the trend changes (the short horizontal lines above/below the thicker line = Open_CurrentBar or HiLo_PreviousBar).  
The first line corresponds to the entry, and the second to the take profit.  
The distances are calculated from the width of the channel. I recommend that you compare them to the ATR and one will find that my calculation is a little better.  
  
**Note #4** \- The first idea for trading is to set after entry a trailing stop identical to the calculated distance between the lines.  
At loss when the exit level is reached, one should trade in the opposite direction (a small hedge trade) with the same trailing stop.  
Anyone who examines this rule will find that the use of a martingale can be very beneficial (I'm curious if someone will do that ...).  
The number of lots can be calculated with a percentage of the capital, one can limit the number of simultaneous orders, etc.  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: EURUSD.rH1.png
Size: 87 KB](/attachment/image/3856751/thumbnail?d=1612650751)](/attachment/image/3856751?d=1612650751)   

  
\---------------  
  
There are many ways to trade Jake's channel and I can only post a few comments about my variant. The potential is great if one analyzes and tests a little longer...  
  

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [smLazyHedging ChannelOsc_v1.3.ex4](/attachment/file/3856752?d=1612650752) 16 KB | 2,042 downloads 

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [smLazyHedging TrendOsc_v1.1.ex4](/attachment/file/3856754?d=1612650755) 15 KB | 2,107 downloads 

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [smLazyHedging TrendChannel_v1.5.1.ex4](/attachment/file/3865237?d=1613507759) 60 KB | 1,564 downloads | Uploaded Feb 17, 2021 5:35am 

  
A useful indicator:  

Attached File(s)

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [smShow HistoryOrders.mq4](/attachment/file/4020561?d=1629808817) 7 KB | 954 downloads | Uploaded Aug 24, 2021 9:40pm 

  * [#2](/thread/post/13400118#post13400118 "Post Permalink")

  * Feb 9, 2021 4:31am  Feb 9, 2021 4:31am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar563839_1.gif) maxus182](maxus182)

  * | Joined Mar 2017  | Status: Trader | [17 Posts](/search?do=process&provider=Member&searchuser=563839)

Hello mr. SwingMan,  
  
I really like your indicator **smLazyHedging TrendOsc_v1.1**. It suits my style of trading very well. Is it possible to add a sound alert for the color change? I'm using it for scalping, so the sound would be perfect. Thank you for all of your great work! 

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#3](/thread/post/13400135#post13400135 "Post Permalink")

  * Feb 9, 2021 4:55am  Feb 9, 2021 4:55am 

  * [ dr.butze](dr.butze)

  * | Joined Jun 2020  | Status: Trader | [165 Posts](/search?do=process&provider=Member&searchuser=965218)

Dear swingman, thank you very much for your generosity. i am still very new here in the forum. and i always see how much work you provide to everyone here for free. thank you very much for that.  
please excuse me if i ask very stupid questions. can you maybe explain again the three yellow lines. there is one thicker one and two thinner ones. The thicker one is the entry and the two thinner ones? I saw your explanations above. But to be honest, I haven't quite understood them yet.  
Thank you for your understanding.  
  
Many greetings from Meenz to FfM 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#4](/thread/post/13400161#post13400161 "Post Permalink")

  * Feb 9, 2021 5:30am  Feb 9, 2021 5:30am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar472073_2.gif) ordosgoitia](ordosgoitia)

  * Joined Jun 2016 | Status: Trader | [268 Posts](/search?do=process&provider=Member&searchuser=472073)

Hi Swingman  
  
Thanks for your work, this fits my trading style, now i can see the trend is a easy way.  
  
Juan 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#5](/thread/post/13400241#post13400241 "Post Permalink")

  * Feb 9, 2021 7:12am  Feb 9, 2021 7:12am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting maxus182](/thread/post/13400118#post13400118 "View Quoted Post")
> 
> Disliked
> 
> Hello mr. SwingMan, I really like your indicator smLazyHedging TrendOsc_v1.1. It suits my style of trading very well. Is it possible to add a sound alert for the color change? I'm using it for scalping, so the sound would be perfect. Thank you for all of your great work!
> 
> Ignored

Maybe later... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#6](/thread/post/13400249#post13400249 "Post Permalink")

  * Feb 9, 2021 7:27am  Feb 9, 2021 7:27am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting dr.butze](/thread/post/13400135#post13400135 "View Quoted Post")
> 
> Disliked
> 
> ...can you maybe explain again the three yellow lines. there is one thicker one and two thinner ones. The thicker one is the entry and the two thinner ones?
> 
> Ignored

Meenz Helau!  
  
The thick line is a reference line, the first thin line is the entry and the second is the take profit.  
  
Test the two options for the reference line (Open_CurrentBar and HiLo_PreviousBar), and you can decide which is better for you.  
If one tests the indicator for a while, one will realize the magnetic properties of the lines ... 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#7](/thread/post/13400802#post13400802 "Post Permalink")

  * Feb 9, 2021 5:30pm  Feb 9, 2021 5:30pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar330952_1.gif) derekw](derekw)

  * Joined Mar 2013 | Status: Trader | [1,581 Posts](/search?do=process&provider=Member&searchuser=330952)

Lovely indicators, as usual... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#8](/thread/post/13400844#post13400844 "Post Permalink")

  * Feb 9, 2021 5:56pm  Feb 9, 2021 5:56pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar622649_2.gif) Degolep](degolep)

  * Joined Oct 2017 | Status: Trader | [995 Posts](/search?do=process&provider=Member&searchuser=622649)

Generous SwingMan as always, thank you. 

Anything above the line is an uptrend, below the line is a downtrend.

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#9](/thread/post/13400863#post13400863 "Post Permalink")

  * Feb 9, 2021 6:05pm  Feb 9, 2021 6:05pm 

  * [ dr.butze](dr.butze)

  * | Joined Jun 2020  | Status: Trader | [165 Posts](/search?do=process&provider=Member&searchuser=965218)

[quote = SwingMan; 13400249] {quote} Meenz Helau! Die dicke Linie ist eine Referenzlinie, die erste dünne Linie ist der Eintrag und die zweite ist der Take Profit. Testen Sie die beiden Optionen für die Referenzlinie (Open_CurrentBar und HiLo_PreviousBar), und Sie können entscheiden, welche für Sie besser ist. Wenn man den Indikator eine Weile testet, erkennt man die magnetischen Eigenschaften der Linien ... [/ quote]  
  
![](https://resources.faireconomy.media/images/emojis/64/1f973.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/270c-fe0f.png?v=15.1)  
Dear Swingman,  
thank you very much. Now I have understood it. I will watch the indicators closely ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)  
Many greetings ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#10](/thread/post/13401176#post13401176 "Post Permalink")

  * Feb 9, 2021 9:08pm  Feb 9, 2021 9:08pm 

  * [ gerval](gerval)

  * | Joined May 2020  | Status: Trader | [243 Posts](/search?do=process&provider=Member&searchuser=958353)

Hello Swingman Simple idea but it seems efficient, I like it.   
I'm going to test it on various pairs and timeframes.  
The one of several later entries with martingale or simple, does not seem a bad idea limiting the number of later entries.  
Try it with EA in backtesting or better yet, demo account ... would be the best.  
Thank you very much for your ideas. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#11](/thread/post/13401371#post13401371 "Post Permalink")

  * Feb 9, 2021 11:18pm  Feb 9, 2021 11:18pm 

  * [ gerval](gerval)

  * | Joined May 2020  | Status: Trader | [243 Posts](/search?do=process&provider=Member&searchuser=958353)

Forgive my ignorance.  
  
What I observe in the lines indicator is that I do not know what type of filter it uses to prevent those lines from reappearing on the contrary when the price turns around after a short time.  
  
And another question is why sometimes it opens a few candles of the anterors and, at other times, many candles pass without the lines appearing?.  
  
I like how the indicator works, congratulations on it. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#12](/thread/post/13401420#post13401420 "Post Permalink")

  * Feb 9, 2021 11:35pm  Feb 9, 2021 11:35pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting gerval](/thread/post/13401371#post13401371 "View Quoted Post")
> 
> Disliked
> 
> Forgive my ignorance.
> 
> Ignored

I'm sorry but I can't do this ...  
  
  
If one has an unknown indicator, one has to study the parameters with options and watch what happens:  
  
Trading_Direction = Main_Trend / Both_Directions  
  
Enable_UpperTrendFilter = true / false  
  
Entry_Value = Open_CurrentBar / HiLo_PreviousBar  
  
Range_Calculation = Channel_Range / ATR_Range 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#13](/thread/post/13401459#post13401459 "Post Permalink")

  * Feb 9, 2021 11:49pm  Feb 9, 2021 11:49pm 

  * [ gerval](gerval)

  * | Joined May 2020  | Status: Trader | [243 Posts](/search?do=process&provider=Member&searchuser=958353)

I understand, go testing parameters.  
It was in case there was a general answer with some basic parameter.  
Thanks, I am testing it with the original configuration 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#14](/thread/post/13402415#post13402415 "Post Permalink")

  * Feb 10, 2021 12:44pm  Feb 10, 2021 12:44pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar218703_1.gif) forexgrh](forexgrh)

  * | Joined Jan 2012  | Status: Trader | [36 Posts](/search?do=process&provider=Member&searchuser=218703)

Interesting, looks like it can be used for scalping at a shorter timeframe to [ SwingMan](https://www.forexfactory.com/swingman)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#15](/thread/post/13404321#post13404321 "Post Permalink")

  * Feb 11, 2021 1:54pm  Feb 11, 2021 1:54pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar218703_1.gif) forexgrh](forexgrh)

  * | Joined Jan 2012  | Status: Trader | [36 Posts](/search?do=process&provider=Member&searchuser=218703)

3 trades in Demo simply following the colour, hence short trend Vs long trend.  
  
Waited till 2nd greenbar / blue bar to confirm and used last swing low as SL then locked in profit and trailed stop till stopped out...... All done in 1min but also looking at 5 min so confirming trend 4 times... Need to work out TP..... maybe 1:1.5 or 1:2  
  
(Missed 1 trade due to coffee break) 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: a6eda5265bb901e7f961dc02f6ab0f28.png
Size: 66 KB](/attachment/image/3860522/thumbnail?d=1613019132)](/attachment/image/3860522?d=1613019132)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#16](/thread/post/13404539#post13404539 "Post Permalink")

  * Feb 11, 2021 5:42pm  Feb 11, 2021 5:42pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting forexgrh](/thread/post/13404321#post13404321 "View Quoted Post")
> 
> Disliked
> 
> 3 trades in Demo simply following the colour, hence short trend Vs long trend. Waited till 2nd greenbar / blue bar to confirm and used last swing low as SL then locked in profit and trailed stop till stopped out...... All done in 1min but also looking at 5 min so confirming trend 4 times... Need to work out TP..... maybe 1:1.5 or 1:2 (Missed 1 trade due to coffee break) {image}
> 
> Ignored

Yes, an interesting scalping!  
On M5 you have catch exactly the trend reverse from the quarter level! 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: GBPUSD.rM5.png
Size: 29 KB](/attachment/image/3860654/thumbnail?d=1613032934)](/attachment/image/3860654?d=1613032934)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#17](/thread/post/13404543#post13404543 "Post Permalink")

  * Feb 11, 2021 5:46pm  Feb 11, 2021 5:46pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

Here the next reverse?! 

Attached Image

![](/attachment/image/3860656?d=1613033170)

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#18](/thread/post/13404550#post13404550 "Post Permalink")

  * Feb 11, 2021 5:54pm  Feb 11, 2021 5:54pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar218703_1.gif) forexgrh](forexgrh)

  * | Joined Jan 2012  | Status: Trader | [36 Posts](/search?do=process&provider=Member&searchuser=218703)

Swingman could you share the Octaves lines please, I can only find v1? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#19](/thread/post/13404560#post13404560 "Post Permalink")

  * Feb 11, 2021 6:01pm  Feb 11, 2021 6:01pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting forexgrh](/thread/post/13404550#post13404550 "View Quoted Post")
> 
> Disliked
> 
> Swingman could you share the Octaves lines please, I can only find v1?
> 
> Ignored

Here the last version: 

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [smOctaves Lines_v2.ex4](/attachment/file/3860666?d=1613034066) 16 KB | 1,092 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#20](/thread/post/13404567#post13404567 "Post Permalink")

  * Feb 11, 2021 6:04pm  Feb 11, 2021 6:04pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar218703_1.gif) forexgrh](forexgrh)

  * | Joined Jan 2012  | Status: Trader | [36 Posts](/search?do=process&provider=Member&searchuser=218703)

Thanks SM 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * LazyHedging Trading Ideas
  *   * [ **Reply to Thread** ](/thread/1058948-lazyhedging-trading-ideas/reply#reply)

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

[EurCad Analysis and Trading Ideas](/thread/360980-eurcad-analysis-and-trading-ideas "Hello my friends. 
 
As of lately I have had remarkable success in trading EurCad and after hearing other traders ideas I decided that we...") 594 replies

[FSP Trading Journal and Trend Ideas](/thread/427493-fsp-trading-journal-and-trend-ideas "hello  
I am trying to post some of my trade Ideas here. 
there will be trend following and counter trend trades. 
I will post image rather...") 16 replies

[Forex trading platform that doesn't take your ideas](/thread/311080-forex-trading-platform-that-doesnt-take-your-ideas "Ninja trader, Metatrader, Tradestation all can copy the EA and indicators straight out of your PC. 
 
How do we go about developing a...") 11 replies

[Program Your Trading Ideas without being a programmer](/thread/225629-program-your-trading-ideas-without-being-a-programmer "I have to admit, I have a lot of trading ideas, but no programming skills. I hate paying a programmer to take 3 days to write an EA for me,...") 4 replies

[Exchanging trading ideas](/thread/136764-exchanging-trading-ideas "I'm opening this thread as a substitute for live chat like msn etc to exchange trading ideas and to filter of some posts at Igrok's thread,...") 37 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/1058948-lazyhedging-trading-ideas/reply#reply)
  * Subscribe
  * [271](javascript:void\(0\);)

Attachments: LazyHedging Trading Ideas

Tags: LazyHedging Trading Ideas

#  [](/thread/1058948-lazyhedging-trading-ideas)LazyHedging Trading Ideas 

  * 

  * [#21](/thread/post/13405335#post13405335 "Post Permalink")

  * Feb 12, 2021 1:39am  Feb 12, 2021 1:39am 

  * [ pareshshah](pareshshah)

  * | Joined Jan 2019  | Status: Trader | [41 Posts](/search?do=process&provider=Member&searchuser=755695)

> [Quoting SwingMan](/thread/post/13404560#post13404560 "View Quoted Post")
> 
> Disliked
> 
> {quote} Here the last version: {file}
> 
> Ignored

Hi, SwingMan,  
  
thanks for wonderful trading system. would it be possible to remove comment section from indicator.   
  
happy trading  
  
Paresh shah 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#22](/thread/post/13405495#post13405495 "Post Permalink")

  * Feb 12, 2021 2:48am  Feb 12, 2021 2:48am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting pareshshah](/thread/post/13405335#post13405335 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi, SwingMan, thanks for wonderful trading system. would it be possible to remove comment section from indicator. happy trading Paresh shah
> 
> Ignored

Please write from which indicator ... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#23](/thread/post/13405525#post13405525 "Post Permalink")

  * Feb 12, 2021 3:08am  Feb 12, 2021 3:08am 

  * [ pareshshah](pareshshah)

  * | Joined Jan 2019  | Status: Trader | [41 Posts](/search?do=process&provider=Member&searchuser=755695)

> [Quoting SwingMan](/thread/post/13405495#post13405495 "View Quoted Post")
> 
> Disliked
> 
> {quote} Please write from which indicator ...
> 
> Ignored

  
Dear Swingman,  
  
Its hedging Trend channel v 1.4  
  
  
thanks n regards always.  
  
Paresh shah. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#24](/thread/post/13405575#post13405575 "Post Permalink")

  * Feb 12, 2021 3:46am  Feb 12, 2021 3:46am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting pareshshah](/thread/post/13405335#post13405335 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi, SwingMan, thanks for wonderful trading system. would it be possible to remove comment section from indicator. happy trading Paresh shah
> 
> Ignored

**New version "smLazyHedging TrendChannel_v1.5"**  
  
OK, we have now two parameters for Comments if you do without my automatic calculation of the lots:  

Inserted Code
    
    
    Show_IndicatorName =true;
    Show_Comment       =false;

  
Just one comment, because I see that many want to use the indicators for their own systems, that's okay.  
But, that also means that nobody understood what kind of system was explained here, and I will also give further explanations only if someone tries to think about it. 

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [smLazyHedging TrendChannel_v1.5.ex4](/attachment/file/3861193?d=1613069209) 59 KB | 766 downloads 

[0 ](javascript:void\(0\);) [3 ](javascript:void\(0\);)

  * [#25](/thread/post/13405584#post13405584 "Post Permalink")

  * Feb 12, 2021 3:51am  Feb 12, 2021 3:51am 

  * [ Takisd](takisd)

  * Joined Dec 2005 | Status: Com Member = Scammer | [5,092 Posts](/search?do=process&provider=Member&searchuser=4969)

Interesting thread. Congrats on the indicators and input. Subscribing and will take a closer look at strategies around these indicators 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#26](/thread/post/13406045#post13406045 "Post Permalink")

  * Feb 12, 2021 1:07pm  Feb 12, 2021 1:07pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1037532_1.gif) Tdate](tdate)

  * | Joined Dec 2020  | Status: Trader | [9 Posts](/search?do=process&provider=Member&searchuser=1037532)

Hello swingman ,  
  
the title of the thread states lazy hedging, i understand the use of indicator and trading with regards to higher time-frame ...i would like to know how you implement your style of hedging into this system...looking forward to learn 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#27](/thread/post/13406085#post13406085 "Post Permalink")

  * Feb 12, 2021 2:11pm  Feb 12, 2021 2:11pm 

  * [ pareshshah](pareshshah)

  * | Joined Jan 2019  | Status: Trader | [41 Posts](/search?do=process&provider=Member&searchuser=755695)

> [Quoting SwingMan](/thread/post/13405575#post13405575 "View Quoted Post")
> 
> Disliked
> 
> {quote} New version "smLazyHedging TrendChannel_v1.5" OK, we have now two parameters for Comments if you do without my automatic calculation of the lots: Show_IndicatorName =true; Show_Comment =false; Just one comment, because I see that many want to use the indicators for their own systems, that's okay. But, that also means that nobody understood what kind of system was explained here, and I will also give further explanations only if someone tries to think about it. {file}
> 
> Ignored

  
Thanks a lot for modification you have done on indicator. Simple trade system. follow rules as stated will do wonder.   
  
god bless you.  
  
Happy trading and innovation as always...  
  
Paresh 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#28](/thread/post/13407479#post13407479 "Post Permalink")

  * Feb 13, 2021 4:32am  Feb 13, 2021 4:32am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar608462_3.gif) T4Trade](t4trade)

  * Joined Sep 2017 | Status: Trend Following,Price Action,Grid | [2,484 Posts](/search?do=process&provider=Member&searchuser=608462)

what does this D1/H1 shows? please explain more about this,what this calculation is depend on? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#29](/thread/post/13407598#post13407598 "Post Permalink")

  * Feb 13, 2021 6:47am  Feb 13, 2021 6:47am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting T4Trade](/thread/post/13407479#post13407479 "View Quoted Post")
> 
> Disliked
> 
> what does this D1/H1 shows? please explain more about this,what this calculation is depend on?
> 
> Ignored

\- Please quote correctly: H1/D1 and not the other way around.  
  
\- H1 is the current timeframe and D1 the upper timeframe, and the trend directions of the two timeframes can/must match.  
Why I suggest this is explained in Note #2, and if someone has time should do a little statistic.  
  
\- Nothing is calculated (except for the spacing between trading levels and lots number for x% risk).  
  
If one takes his time, one will find that this has no direct connection with price trending.  
For me, as a lazy trader, it would take too much energy to analyze the trends. I don't care about the trend as such, it is only important to trade in the current TF the right bars in the upper TF.  
If there is a strong reversal in D1, one detects this on H4 or H1 and one trades M15, M5 or M1 so that contrary trades can also take place. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#30](/thread/post/13407910#post13407910 "Post Permalink")

  * Feb 13, 2021 7:49pm  Feb 13, 2021 7:49pm 

  * [ gerval](gerval)

  * | Joined May 2020  | Status: Trader | [243 Posts](/search?do=process&provider=Member&searchuser=958353)

Hi all.  
I have been testing the indicator in a basic way and without taking into account other things, in EURUSD and some other in D1 and H4. changing the TP and SL with the lines and the one that gave me the best result has been as in the image, letting the price decide which line to break at the immediate entry (thick line). Poniedo Breakeven when price is 2 pips short of TP1.  
  
In pairs with a higher volatility range, I have changed the two final parameters of the indicator (Factor_L1 to 1.5 and Factor _2 to 3.0) to separate the lines from the original configuration by 50% more. The backtest is not very extensive but it has not worked badly, about 2 years in H4. If you take into account trends in higher TF you can improve.  
  
In this period of time, he has made 4 negative operations in a row, in case you want to try entering later using martingale ...  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: aebc06fe7bb94d99268a614b595b8857.png
Size: 86 KB](/attachment/image/3862722/thumbnail?d=1613213370)](/attachment/image/3862722?d=1613213370)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#31](/thread/post/13407931#post13407931 "Post Permalink")

  * Feb 13, 2021 8:37pm  Feb 13, 2021 8:37pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting gerval](/thread/post/13407910#post13407910 "View Quoted Post")
> 
> Disliked
> 
> Hi all. I have been testing the indicator in a basic way and without taking into account other things, in EURUSD and some other in D1 and H4. changing the TP and SL with the lines and the one that gave me the best result has been as in the image, letting the price decide which line to break at the immediate entry (thick line). Poniedo Breakeven when price is 2 pips short of TP1. In pairs with a higher volatility range, I have changed the two final parameters of the indicator (Factor_L1 to 1.5 and Factor _2 to 3.0) to separate the lines from the...
> 
> Ignored

I didn't quite understand how you tested it, but it is good if you are satisfied!  
On many days, if one only trades M5, M15, M30 and H1, one has a positive result at the end of the day.  
  
Because you mentioned the martingale: usually one can trade the martingale with doubling up to level 7-8. With the procedure in my Note #4, one can go much higher to about 14... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#32](/thread/post/13407940#post13407940 "Post Permalink")

  * Feb 13, 2021 8:59pm  Feb 13, 2021 8:59pm 

  * [ gerval](gerval)

  * | Joined May 2020  | Status: Trader | [243 Posts](/search?do=process&provider=Member&searchuser=958353)

About the martingale I mean making independent entries at another time, accumulating the losses and increasing the lot, in the backtest I have received up to 4 consecutive negatives, although the backtest is not very broad. Can the indicator period be extended?  
  
Regarding what it says about the trailing stop, I understand that an entry is made and another order is immediately weighted at the stop point? Or at the point where it is closed with the trailing stop, if the profit is not what is expected?  
  
To be able to do 14 is it because when closing with a trailing stop and having some profit, in the next order can the lot price be lowered a little by the previous profit?.  
Thanks 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#33](/thread/post/13407947#post13407947 "Post Permalink")

  * Feb 13, 2021 9:22pm  Feb 13, 2021 9:22pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting gerval](/thread/post/13407940#post13407940 "View Quoted Post")
> 
> Disliked
> 
> About the martingale I mean making independent entries at another time, accumulating the losses and increasing the lot, in the backtest I have received up to 4 consecutive negatives, although the backtest is not very broad. Can the indicator period be extended? Regarding what it says about the trailing stop, I understand that an entry is made and another order is immediately weighted at the stop point? Or at the point where it is closed with the trailing stop, if the profit is not what is expected? To be able to do 14 is it because when closing...
> 
> Ignored

Nice that you are wondering, you analyzed correctly.  
It's almost like you noticed, but every time you start trailing there is a loss.  
The new lot is this loss +1 as in the martingale and in normal martingale you always lose your bet.  
  
In my simulation (if that's correct) you only lose on average half your bet. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Hedging Martingale.PNG
Size: 29 KB](/attachment/image/3862733/thumbnail?d=1613218947)](/attachment/image/3862733?d=1613218947)   

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#34](/thread/post/13407976#post13407976 "Post Permalink")

  * Feb 13, 2021 9:54pm  Feb 13, 2021 9:54pm 

  * [ gerval](gerval)

  * | Joined May 2020  | Status: Trader | [243 Posts](/search?do=process&provider=Member&searchuser=958353)

It makes perfect sense to use the martingale like this.  
  
Assuming that half is lost in each operation, if I see your table correct, being able to drag many more operations in martingale.  
  
Another point in favor of this assumed risk is compensated in the case that in an operation with a high number of martingale, if the trailing stop works, it would take us far with a high lot.  
  
Mathematically on some occasion it will not work, but if you know how to dose the benefit and the loss when it arrives, that is fine.  
  
If each operation we have 50% of losing (although following trends can be reduced theoretically) by a maximum of 14 martingales = 0.5 / 14 = 0.035% of the time we would lose.  
  
I use the translator, sorry for my English  
  
I will try to test it in demo, but it is difficult manually in small TF 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#35](/thread/post/13407985#post13407985 "Post Permalink")

  * Feb 13, 2021 10:13pm  Feb 13, 2021 10:13pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting gerval](/thread/post/13407976#post13407976 "View Quoted Post")
> 
> Disliked
> 
> It makes perfect sense to use the martingale like this. Assuming that half is lost in each operation, if I see your table correct, being able to drag many more operations in martingale. Another point in favor of this assumed risk is compensated in the case that in an operation with a high number of martingale, if the trailing stop works, it would take us far with a high lot. Mathematically on some occasion it will not work, but if you know how to dose the benefit and the loss when it arrives, that is fine. If each operation we have 50% of losing...
> 
> Ignored

I honestly wonder that someone in the forum understood what it was about ...  
  
The only disadvantage with this method is that you can only trade with one EA if you want to trade multiple pairs and TFs. Now I don't have the time to do that, but I follow the TFs to H1 every day to get a feeling. I also only noticed a maximum of 4 levels of loss.  
  
In my table, one should take risk percentages instead of lots. Then one sees that one has rather small DDs with 0.10% or 0.20% risk, and one can trade 5-10 pairs or TFs at the same time. 

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#36](/thread/post/13408019#post13408019 "Post Permalink")

  * Feb 13, 2021 11:25pm  Feb 13, 2021 11:25pm 

  * [ gerval](gerval)

  * | Joined May 2020  | Status: Trader | [243 Posts](/search?do=process&provider=Member&searchuser=958353)

In case of operating multipairs, I think the risk grows significantly. In case we use a multilevel martingale in several pairs, the margin would decrease faster and we could not reach the possible 12 or 14 martingale as in just one. By cons, the account goes up before  
  
I will test it manually and tell you, an alarm could be included in the indicator?  
  
How long have you been testing it?  
  
Thanks for your knowledge and material. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#37](/thread/post/13408051#post13408051 "Post Permalink")

  * Feb 14, 2021 12:09am  Feb 14, 2021 12:09am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting gerval](/thread/post/13408019#post13408019 "View Quoted Post")
> 
> Disliked
> 
> In case of operating multipairs, I think the risk grows significantly. In case we use a multilevel martingale in several pairs, the margin would decrease faster and we could not reach the possible 12 or 14 martingale as in just one. By cons, the account goes up before I will test it manually and tell you, an alarm could be included in the indicator? How long have you been testing it? Thanks for your knowledge and material.
> 
> Ignored

I tested the idea in different versions and stayed with the current form about two months ago.  
Every day I analyze the signaled trades for 12 forex pairs and the TFs from M5 to H1, sometimes also H4 and D1.  
It works well for indexes too, and maybe not as well for futures and bitcoins.  
  
The idea seems to me to be good to trade intraday the TFs M5 to H1 with a single martingale level, and for a day of loss to set a new basis the next day. The average loss is not 2 per trade as with normal martingales, but around 1.5 or less.  
I also wrote beforehand that my calculation of the trading distances is surprisingly good compared to ATR (but one should also test from others ...).  
Manual testing would be difficult for me during the day. For an EA I didn't want to invest time and post here in forum, and one reason is that many download such EAs and do not follow any analyzes. But when I see that there is actually interest and some contributions like yours, I can do that.  
  
What alarm did you mean? 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#38](/thread/post/13408111#post13408111 "Post Permalink")

  * Feb 14, 2021 2:53am  Feb 14, 2021 2:53am 

  * [ gerval](gerval)

  * | Joined May 2020  | Status: Trader | [243 Posts](/search?do=process&provider=Member&searchuser=958353)

In summary, I understand that you wait for the indicator to appear, use the first line for entry with stop on the thick line, with take profit on the next thin line to the entry, at the same time with a trailing stop on the thick line (at the same distance between stop and entry). In case of not reaching the tp, it is re-entered once, increasing 1 unit to the loss. And in case of losing it, the martinagala is not increased.  
  
Looking for a trend in high time frame and entering the same direction? The problem that by doing just one more re-entry we would go against the possible trend, perhaps 2 levels of martingale, would place us in the direction of the trend.  
  
The alarm was referring to an alert, especially to warn in small tf when the indicator is drawn.  
  
The EA is interesting since the becktesting would be much faster, but as it says and for the system to work (as always), you must know its operation perfectly before using an EA. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#39](/thread/post/13408149#post13408149 "Post Permalink")

  * Feb 14, 2021 4:07am  Feb 14, 2021 4:07am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

You described everything very well.  
  
I mentioned a variant with only one bet level for intraday trading, only for M5 and M15 e.g.  
Sure, someone has to test it, but my impression is that there are enough gains per day to compensate for the losses. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#40](/thread/post/13408539#post13408539 "Post Permalink")

  * Feb 15, 2021 12:08am  Feb 15, 2021 12:08am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar439469_22.gif) MoneyZilla](moneyzilla)

  * Joined Dec 2015 | Status: Suuka Maadik | [3,630 Posts](/search?do=process&provider=Member&searchuser=439469)

Just want to share something, I think it can be valuable for you.  
  
Me is working on over 500 MT4s. When I have a bad strategy, something that crashes an account, I keep the chart and the settings forever. Until I find time to break down the cause of the crash. This usually happens within a year or two.  
  
Here is the important part. Was passing by few of these in Jan'21, and just added a condition for _time_. Something like _a metronome_? A repeatable trading condition, if the last signal direction was a buy, specific buy of the bottoms, for example. Same for the sells. Run a specific sell on the tops. Just a trading condition that repeats X times every day. The smaller the repeat, the better, me thinks.  
  
Suddenly. Out of the blue. These account destroyers have turn into a massive success. Just because I have added _time_ , in the form of a trading condition. And it works on a simple strategies, like breakout, for example, or candles. Imagine, candle-based?!? What could be more simple than that?!? No special filtering and complicated setups. Just anything + _time_ (in the form of a repeatable trading condition of the last signal direction, and you do similar with the next signal direction, ext., ext.).  
  
Just mentioning this, if you can use it? As it did solved all my hedging issues. Now, when lazy hedging, i do not use a SL or never close a trade. Just don't have to. The only limitation is the max account trades...  
  
If you can't find a use of the _time_ , _sorry for the long post_. Won't bother you anymore.

Maadik Hugiis. IQ 69.

[0 ](javascript:void\(0\);) [4 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * LazyHedging Trading Ideas
  *   * [ **Reply to Thread** ](/thread/1058948-lazyhedging-trading-ideas/reply#reply)

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

[EurCad Analysis and Trading Ideas](/thread/360980-eurcad-analysis-and-trading-ideas "Hello my friends. 
 
As of lately I have had remarkable success in trading EurCad and after hearing other traders ideas I decided that we...") 594 replies

[FSP Trading Journal and Trend Ideas](/thread/427493-fsp-trading-journal-and-trend-ideas "hello  
I am trying to post some of my trade Ideas here. 
there will be trend following and counter trend trades. 
I will post image rather...") 16 replies

[Forex trading platform that doesn't take your ideas](/thread/311080-forex-trading-platform-that-doesnt-take-your-ideas "Ninja trader, Metatrader, Tradestation all can copy the EA and indicators straight out of your PC. 
 
How do we go about developing a...") 11 replies

[Program Your Trading Ideas without being a programmer](/thread/225629-program-your-trading-ideas-without-being-a-programmer "I have to admit, I have a lot of trading ideas, but no programming skills. I hate paying a programmer to take 3 days to write an EA for me,...") 4 replies

[Exchanging trading ideas](/thread/136764-exchanging-trading-ideas "I'm opening this thread as a substitute for live chat like msn etc to exchange trading ideas and to filter of some posts at Igrok's thread,...") 37 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/1058948-lazyhedging-trading-ideas/reply#reply)
  * Subscribe
  * [271](javascript:void\(0\);)

Attachments: LazyHedging Trading Ideas

Tags: LazyHedging Trading Ideas

#  [](/thread/1058948-lazyhedging-trading-ideas)LazyHedging Trading Ideas 

  * 

  * [#41](/thread/post/13408828#post13408828 "Post Permalink")

  * Feb 15, 2021 7:47am  Feb 15, 2021 7:47am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting MoneyZilla](/thread/post/13408539#post13408539 "View Quoted Post")
> 
> Disliked
> 
> ...Imagine, candle-based?!? What could be more simple than that?!? No special filtering and complicated setups. Just anything + time (in the form of a repeatable trading condition of the last signal direction, and you do similar with the next signal direction, ext., ext.). Just mentioning this, if you can use it? As it did solved all my hedging issues.
> 
> Ignored

Thanks for the hint.  
  
A whole world uses PA (Price Action) and you use TA (Time Action). Congratulations for the results! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#42](/thread/post/13408999#post13408999 "Post Permalink")

  * Feb 15, 2021 1:14pm  Feb 15, 2021 1:14pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar218703_1.gif) forexgrh](forexgrh)

  * | Joined Jan 2012  | Status: Trader | [36 Posts](/search?do=process&provider=Member&searchuser=218703)

I understand time action, but how best do we display that as a picture hmmm ? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#43](/thread/post/13410141#post13410141 "Post Permalink")

  * Feb 16, 2021 3:34am  Feb 16, 2021 3:34am 

  * [ gerval](gerval)

  * | Joined May 2020  | Status: Trader | [243 Posts](/search?do=process&provider=Member&searchuser=958353)

Hello Swingman.  
  
Today I have been testing the system, although not as I would have liked because the trailing stop EA did not work well for this system (it moves with the price in positive), I have looked for another that seems to work from the beginning.  
  
I have traded in M-15 because in a lower time frame, having to place the orders manually and the spread ...  
  
Generally well, I have had up to 4 entries (pair with little movement and spread too wide), in addition to respecting the levels millimetrically just in the entries and sl of the levels, so the trailing stop did not move.  
  
How do you manage in range zones where the trailing stop does not move? takes losses and enters another point on the chart? or keep tickets?  
  
Thanks 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#44](/thread/post/13410154#post13410154 "Post Permalink")

  * Feb 16, 2021 3:43am  Feb 16, 2021 3:43am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar680490_1.gif) forex1x8](forex1x8)

  * Joined May 2018 | Status: Trader | [315 Posts](/search?do=process&provider=Member&searchuser=680490)

Congratulations Swingman I would like to leave a collaboration here.  
This system can be fantastic with or active US30.  
TF M15  
A hug to everyone and green pips. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#45](/thread/post/13410214#post13410214 "Post Permalink")

  * Feb 16, 2021 5:06am  Feb 16, 2021 5:06am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting gerval](/thread/post/13410141#post13410141 "View Quoted Post")
> 
> Disliked
> 
> ... **the trailing stop** EA did not work well for this system (it**moves with the price in positive**), ... Generally well, I have had up to 4 entries (pair with little movement **and spread too wide**), in addition to respecting the levels millimetrically just in the entries and sl of the levels, so the trailing stop did not move. How do you manage in range zones where the trailing stop does not move? **takes losses** and **enters another point on the chart**? or keep tickets? Thanks
> 
> Ignored

\- The trailing stop of the system does not have the known function of securing profits, but rather limiting losses to MAE (maximum adverse excursion) minus entry.  
  
\- For the small time frames you have to have a filter, for example Entrys only for Spread/LevelRange <= 20%  
  
\- Generally after a loss, which is sometimes very small, it is amazing how easily the increased bet is won later in the chart. As you have noticed, this is the case in the 3rd or 4th step.  
# In general, you can raise your bet after the loss. (A bet loss consists of the first entry loss (FEL) and the second hedge loss (SHL = FEL + 1).  
There are always two losses for a negative entry, and the total loss is (1 < Loss < 2).  
# The other possibility is to add up the results for one or more time frames and pairs in a certain period (1 day, 1 week) and to increase the base bet for the next period if there are losses. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#46](/thread/post/13410220#post13410220 "Post Permalink")

  * Feb 16, 2021 5:11am  Feb 16, 2021 5:11am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting forex1x8](/thread/post/13410154#post13410154 "View Quoted Post")
> 
> Disliked
> 
> Congratulations Swingman I would like to leave a collaboration here. This system can be fantastic with or active US30. TF M15 A hug to everyone and green pips.
> 
> Ignored

That would be good, because I've just decided to make the future EA only available to active members. If one can't comment or test the idea, one don't need an EA, one have a better system ... 

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#47](/thread/post/13410222#post13410222 "Post Permalink")

  * Feb 16, 2021 5:13am  Feb 16, 2021 5:13am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar472073_2.gif) ordosgoitia](ordosgoitia)

  * Joined Jun 2016 | Status: Trader | [268 Posts](/search?do=process&provider=Member&searchuser=472073)

i think this system works better on h1 or h4,, the setup is very clear, and you can win a lot of pips with higher timeframe.. i saw with m15, when you want to enter the trade after the indis confirm the entry, if the trend is not good you will have a loss trade. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#48](/thread/post/13410269#post13410269 "Post Permalink")

  * Feb 16, 2021 6:08am  Feb 16, 2021 6:08am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting ordosgoitia](/thread/post/13410222#post13410222 "View Quoted Post")
> 
> Disliked
> 
> i think this system works better on h1 or h4,, the setup is very clear, and you can win a lot of pips with higher timeframe.. i saw with m15, when you want to enter the trade after the indis confirm the entry, if the trend is not good you will have a loss trade.
> 
> Ignored

Try to forget the term "trend" as it is commonly used. There are also options for trading "with the trend" for this system, but this has to be explained later and actually brings good profits.  
  
Within a trend, e.g. on D1, there are, for example, more green bars than red bars for long, which is important.  
OK, then on H1 or M30 or M15 we try to trade a formation (pattern) at the beginning of a trend that is running in the same direction.  
  
If one makes the effort to statistically analyze the trades, one realizes that there are many simple gains.  
There are also sudden reversals caused by the speculators, and here one wins too.  
There are certainly also sideways movements with losses, but the hedging steps can compensate for that. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#49](/thread/post/13410272#post13410272 "Post Permalink")

  * Feb 16, 2021 6:09am  Feb 16, 2021 6:09am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar218703_1.gif) forexgrh](forexgrh)

  * | Joined Jan 2012  | Status: Trader | [36 Posts](/search?do=process&provider=Member&searchuser=218703)

> [Quoting SwingMan](/thread/post/13410220#post13410220 "View Quoted Post")
> 
> Disliked
> 
> {quote} That would be good, because I've just decided to make the future EA only available to active members. If one can't comment or test the idea, one don't need an EA, one have a better system ...
> 
> Ignored

I agree Swingman there is no EA that will ever be able to work with ZERO intervention, if it we the case it would already be available FOREX is about hard work not easy money. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#50](/thread/post/13410275#post13410275 "Post Permalink")

  * Feb 16, 2021 6:10am  Feb 16, 2021 6:10am 

  * [ Rce](rce)

  * | Joined Apr 2017  | Status: Trader | [39 Posts](/search?do=process&provider=Member&searchuser=573861)

Always providing good tools for trading. I have adapted your indicator to renko chart. I filter the entries with EMA100. I would miss alerts as another colleague commented, I like it !!!!!! THANK YOU SwingMan 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: renko swingman.JPG
Size: 99 KB](/attachment/image/3864118/thumbnail?d=1613423435)](/attachment/image/3864118?d=1613423435)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#51](/thread/post/13410281#post13410281 "Post Permalink")

  * Feb 16, 2021 6:16am  Feb 16, 2021 6:16am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting Rce](/thread/post/13410275#post13410275 "View Quoted Post")
> 
> Disliked
> 
> Always providing good tools for trading. I have adapted your indicator to renko chart. I filter the entries with EMA100.**I would miss alerts** as another colleague commented, I like it !!!!!! THANK YOU SwingMan
> 
> Ignored

Is being worked on!  
  
You have 4 wins / 1 loss without filter...  
  
Actually for you (Renko) one should be able to enter the upper time frame as a parameter... 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#52](/thread/post/13410291#post13410291 "Post Permalink")

  * Feb 16, 2021 6:25am  Feb 16, 2021 6:25am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar166111_2.gif) bopuc](bopuc)

  * | Joined Jan 2011  | Status: Trader | [53 Posts](/search?do=process&provider=Member&searchuser=166111)

Attached Image (click to enlarge)

[![Click to Enlarge

Name: 11cb80c6e909a507b3d09a2ec00ead25.png
Size: 406 KB](/attachment/image/3864132/thumbnail?d=1613424304)](/attachment/image/3864132?d=1613424304)   

  
It seems to me that trade 3 and 4 are loss, or maybe I have not fully understood entry/exit criteria? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#53](/thread/post/13410310#post13410310 "Post Permalink")

  * Feb 16, 2021 6:55am  Feb 16, 2021 6:55am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting bopuc](/thread/post/13410291#post13410291 "View Quoted Post")
> 
> Disliked
> 
> ...It seems to me that trade 3 and 4 are loss, or maybe I have not fully understood entry/exit criteria?
> 
> Ignored

You understood the entry criteria, but 4 is a reverse win, see my penultimate proposition in #Post 48! 

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#54](/thread/post/13410400#post13410400 "Post Permalink")

  * Feb 16, 2021 9:03am  Feb 16, 2021 9:03am 

  * [ gerval](gerval)

  * | Joined May 2020  | Status: Trader | [243 Posts](/search?do=process&provider=Member&searchuser=958353)

> [Quoting SwingMan](/thread/post/13410214#post13410214 "View Quoted Post")
> 
> Disliked
> 
> {quote} - The trailing stop of the system does not have the known function of securing profits, but rather limiting losses to MAE (maximum adverse excursion) minus entry. - For the small time frames you have to have a filter, for example Entrys only for Spread/LevelRange <= 20% - Generally after a loss, which is sometimes very small, it is amazing how easily the increased bet is won later in the chart. As you have noticed, this is the case in the 3rd or 4th step. # In general, you can raise your bet after the loss. (A bet loss consists of the first...
> 
> Ignored

I see that you have the system studied and developed.  
  
The trailing Stop is the one that gives magic to the system, since it modifies the levels in the range drawers, helping to chase the price and reduces the loss on many occasions, making us enter the new movement in favor with less level earlier by martingale  
  
I like it. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#55](/thread/post/13410673#post13410673 "Post Permalink")

  * Feb 16, 2021 3:09pm  Feb 16, 2021 3:09pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar330952_1.gif) derekw](derekw)

  * Joined Mar 2013 | Status: Trader | [1,581 Posts](/search?do=process&provider=Member&searchuser=330952)

I tried to filter failing trades. I do understand the hedging idea. Not sure if this idea is worth looking into. Trend bars are by Xard. In this image only the most recent trade is valid, (Buy trade off a green bar).  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Capture.PNG
Size: 121 KB](/attachment/image/3864424/thumbnail?d=1613455779)](/attachment/image/3864424?d=1613455779)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#56](/thread/post/13410812#post13410812 "Post Permalink")

  * Feb 16, 2021 5:02pm  Feb 16, 2021 5:02pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting derekw](/thread/post/13410673#post13410673 "View Quoted Post")
> 
> Disliked
> 
> I tried to filter failing trades. I do understand the hedging idea. Not sure if this idea is worth looking into. Trend bars are by Xard. In this image only the most recent trade is valid, (Buy trade off a green bar). {image}
> 
> Ignored

Can you please explain what Xard is doing? I do not know.  
  
On the left side we have a win.  
On the right side I also have a win with my broker (maybe you change yours ...)  
  
Of course, one has to test the hedging idea, I haven't done that in practice yet, so the thread's title suggests that the idea should be analyzed. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: EURUSD.rM15.png
Size: 98 KB](/attachment/image/3864487/thumbnail?d=1613462523)](/attachment/image/3864487?d=1613462523)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#57](/thread/post/13411436#post13411436 "Post Permalink")

  * Feb 16, 2021 10:15pm  Feb 16, 2021 10:15pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar166111_2.gif) bopuc](bopuc)

  * | Joined Jan 2011  | Status: Trader | [53 Posts](/search?do=process&provider=Member&searchuser=166111)

**SwingMan,**  
  
when you find some time can you add (optional) 'hedge entry/TP' line to the smLazyHedging TrendChannel_v1.5 indicator? What I mean is that beside entry/SL/TP lines there is another one opposite of entry that represents hedge TP. I think it will beneficial for visual backtest. Thanks!  
  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: hedge_tp.png
Size: 24 KB](/attachment/image/3864763/thumbnail?d=1613481485)](/attachment/image/3864763?d=1613481485)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#58](/thread/post/13411485#post13411485 "Post Permalink")

  * Feb 16, 2021 10:30pm  Feb 16, 2021 10:30pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting bopuc](/thread/post/13411436#post13411436 "View Quoted Post")
> 
> Disliked
> 
> SwingMan, when you find some time can you add (optional) 'hedge entry/TP' line to the smLazyHedging TrendChannel_v1.5 indicator? What I mean is that beside entry/SL/TP lines there is another one opposite of entry that represents hedge TP. I think it will beneficial for visual backtest. Thanks! {image}
> 
> Ignored

Maybe help to use the first parameter:   

Inserted Code
    
    
    Trading_Direction = Both_Directions

[0 ](javascript:void\(0\);) [3 ](javascript:void\(0\);)

  * [#59](/thread/post/13411571#post13411571 "Post Permalink")

  * Feb 16, 2021 10:56pm  Feb 16, 2021 10:56pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar166111_2.gif) bopuc](bopuc)

  * | Joined Jan 2011  | Status: Trader | [53 Posts](/search?do=process&provider=Member&searchuser=166111)

That's exactly what I meant. I somehow missed that option. Thanks! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#60](/thread/post/13412342#post13412342 "Post Permalink")

  * Feb 17, 2021 4:43am  Feb 17, 2021 4:43am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar166111_2.gif) bopuc](bopuc)

  * | Joined Jan 2011  | Status: Trader | [53 Posts](/search?do=process&provider=Member&searchuser=166111)

Found this one a bit odd, maybe it's a bug in the code... When we have short entry, all lines are red but for long entry, they are ( I think properly) coloured blue/red.  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: red.png
Size: 58 KB](/attachment/image/3865207/thumbnail?d=1613504566)](/attachment/image/3865207?d=1613504566)   

  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: blue.png
Size: 54 KB](/attachment/image/3865206/thumbnail?d=1613504552)](/attachment/image/3865206?d=1613504552)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * LazyHedging Trading Ideas
  *   * [ **Reply to Thread** ](/thread/1058948-lazyhedging-trading-ideas/reply#reply)

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

[EurCad Analysis and Trading Ideas](/thread/360980-eurcad-analysis-and-trading-ideas "Hello my friends. 
 
As of lately I have had remarkable success in trading EurCad and after hearing other traders ideas I decided that we...") 594 replies

[FSP Trading Journal and Trend Ideas](/thread/427493-fsp-trading-journal-and-trend-ideas "hello  
I am trying to post some of my trade Ideas here. 
there will be trend following and counter trend trades. 
I will post image rather...") 16 replies

[Forex trading platform that doesn't take your ideas](/thread/311080-forex-trading-platform-that-doesnt-take-your-ideas "Ninja trader, Metatrader, Tradestation all can copy the EA and indicators straight out of your PC. 
 
How do we go about developing a...") 11 replies

[Program Your Trading Ideas without being a programmer](/thread/225629-program-your-trading-ideas-without-being-a-programmer "I have to admit, I have a lot of trading ideas, but no programming skills. I hate paying a programmer to take 3 days to write an EA for me,...") 4 replies

[Exchanging trading ideas](/thread/136764-exchanging-trading-ideas "I'm opening this thread as a substitute for live chat like msn etc to exchange trading ideas and to filter of some posts at Igrok's thread,...") 37 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/1058948-lazyhedging-trading-ideas/reply#reply)
  * Subscribe
  * [271](javascript:void\(0\);)

Attachments: LazyHedging Trading Ideas

Tags: LazyHedging Trading Ideas

#  [](/thread/1058948-lazyhedging-trading-ideas)LazyHedging Trading Ideas 

  * 

  * [#61](/thread/post/13412385#post13412385 "Post Permalink")

  * Feb 17, 2021 5:34am  Feb 17, 2021 5:34am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

**New version "smLazyHedging TrendChannel_v1.5.1"**  
  

> [Quoting bopuc](/thread/post/13412342#post13412342 "View Quoted Post")
> 
> Disliked
> 
> Found this one a bit odd, maybe it's a bug in the code... When we have short entry, all lines are red but for long entry, they are ( I think properly) coloured blue/red.
> 
> Ignored

You are right, because of copy & paste the colors were identical. Thanks for the comment.  
Here is the corrected version. 

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [smLazyHedging TrendChannel_v1.5.1.ex4](/attachment/file/3865236?d=1613507664) 60 KB | 797 downloads 

[0 ](javascript:void\(0\);) [5 ](javascript:void\(0\);)

  * [#62](/thread/post/13412971#post13412971 "Post Permalink")

  * Feb 17, 2021 4:24pm  Feb 17, 2021 4:24pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar330952_1.gif) derekw](derekw)

  * Joined Mar 2013 | Status: Trader | [1,581 Posts](/search?do=process&provider=Member&searchuser=330952)

> [Quoting SwingMan](/thread/post/13410812#post13410812 "View Quoted Post")
> 
> Disliked
> 
> {quote} Can you please explain what Xard is doing? I do not know. On the left side we have a win. On the right side I also have a win with my broker (maybe you change yours ...) Of course, one has to test the hedging idea, I haven't done that in practice yet, so the thread's title suggests that the idea should be analyzed. {image}
> 
> Ignored

Hi Swingman.  
  
Xard always gives his work away for free, but not his code. He seems to calculate the trend bars by the cross of two moving averages, but also they must agree to another trend direction, which I think he is basing on Zig Zag. You can read all about his method here: [https://forex-station.com/viewtopic....73#p1295428873](https://forex-station.com/viewtopic.php?t=8416709&p=1295428873#p1295428873)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#63](/thread/post/13413506#post13413506 "Post Permalink")

  * Feb 17, 2021 8:52pm  Feb 17, 2021 8:52pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar970926_1.gif) carlosmartin](carlosmartin)

  * | Joined Jun 2020  | Status: Trader | [7 Posts](/search?do=process&provider=Member&searchuser=970926)

Incredible work SM, as always.  
  
Now I'm trying to work on an EA that opens the order (above 10MA in case of buy) and closes (below 8MA in case of buy) and vice versa by opening (below 8MA in case of sell) and close (the one above 10MA in case of sell) As I am still learning mq4, I will start from something ready like this attached file. It's like an MA-based stoploss and works well but is triggered on touch with the MA and not after the candle closes (above or below) Well, but it is already a start!  
  
Regarding smLazyHedging TrendOsc_v1.1 a very nice option would be an alert. I can try to place it if I have the file.  
  
ps. I started a journey of reading all your started threads and the 2,232 thread replies on FF. I have a lot to learn from you sir.

Attached File(s)

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [OrdMgrSL.mq4](/attachment/file/3865977?d=1613562754) 7 KB | 310 downloads 

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#64](/thread/post/13413646#post13413646 "Post Permalink")

  * Feb 17, 2021 10:14pm  Feb 17, 2021 10:14pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting carlosmartin](/thread/post/13413506#post13413506 "View Quoted Post")
> 
> Disliked
> 
> Incredible work SM, as always. Now I'm trying to work on an EA that opens the order (above 10MA in case of buy) and closes (below 8MA in case of buy) and vice versa by opening (below 8MA in case of sell) and close (the one above 10MA in case of sell) As I am still learning mq4, I will start from something ready like this attached file. It's like an MA-based stoploss and works well but is triggered on touch with the MA and not after the candle closes (above or below) Well, but it is already a start! Regarding smLazyHedging TrendOsc_v1.1 a very nice...
> 
> Ignored

Very nice, and I wish you every success!  
Until you're done, maybe I'll post an alternative exit indicator similar to that for "Mantra Strategy" [https://www.forexfactory.com/thread/...e-boat-trading](https://www.forexfactory.com/thread/1011744-price-boat-trading)

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#65](/thread/post/13414520#post13414520 "Post Permalink")

  * Feb 18, 2021 6:28am  Feb 18, 2021 6:28am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar970926_1.gif) carlosmartin](carlosmartin)

  * | Joined Jun 2020  | Status: Trader | [7 Posts](/search?do=process&provider=Member&searchuser=970926)

> [Quoting SwingMan](/thread/post/13413646#post13413646 "View Quoted Post")
> 
> Disliked
> 
> {quote}Until you're done, maybe I'll post an alternative exit indicator
> 
> Ignored

**...that would be amazing**! While we still don't have an alert, one option is to use this indicator from Lord [Mladen](https://forex-station.com/viewtopic.php?p=1295378801#p1295378801). Besides the lines I also like the colored bars ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: fa4dc661ed0f9a426bf81277db8d72d8.png
Size: 272 KB](/attachment/image/3866489/thumbnail?d=1613597171)](/attachment/image/3866489?d=1613597171)   
[![Click to Enlarge

Name: ee504bf2d3f55c9f7863ed14bdda40c2.png
Size: 161 KB](/attachment/image/3866490/thumbnail?d=1613597194)](/attachment/image/3866490?d=1613597194)   
[![Click to Enlarge

Name: f89baecf30316acf790ab1344eaedda5.png
Size: 159 KB](/attachment/image/3866491/thumbnail?d=1613597212)](/attachment/image/3866491?d=1613597212)   

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [averages - mtf - alerts 9.0.ex4](/attachment/file/3866492?d=1613597255) 154 KB | 337 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#66](/thread/post/13414572#post13414572 "Post Permalink")

  * Feb 18, 2021 7:25am  Feb 18, 2021 7:25am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting carlosmartin](/thread/post/13414520#post13414520 "View Quoted Post")
> 
> Disliked
> 
> ...Besides the lines I also like the colored bars ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)
> 
> Ignored

Appearances are deceptive ...  
  
Such colored bars as the Heikin Ashi candles are good for getting a global impression of the trend.  
In practice, however, you also need to know whether a bar is green or red or where the open and close are.  
  
I just read an article in Stocks & Commodities: "Ratio Of Red To Green Candles".  
The author - Ken Calhoun - sells various interesting courses for a lot of money (TradeMastery#com) and in the article he describes exactly what I wrote for free in #Post 1, Note #2 ...  
  
One can e.g. program a very simple trend trading system:  
\- trend determined with the HiLo 10/8 MAs  
\- Entrys for HiLo of previous bar if in the last 5 bars at least 3 bars have the same color in the direction of the trend  
\- filter or not with trend of upper time frame  
\- limitation of initial losses with hedging, break even, trailing  
\- exit on my not yet published indicator, or on MAs  
\- reentry in trend 

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#67](/thread/post/13414600#post13414600 "Post Permalink")

  * Feb 18, 2021 7:56am  Feb 18, 2021 7:56am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar970926_1.gif) carlosmartin](carlosmartin)

  * | Joined Jun 2020  | Status: Trader | [7 Posts](/search?do=process&provider=Member&searchuser=970926)

> [Quoting SwingMan](/thread/post/13414572#post13414572 "View Quoted Post")
> 
> Disliked
> 
> {quote} Appearances are deceptive ...
> 
> Ignored

**you're absolutely right!**

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#68](/thread/post/13418235#post13418235 "Post Permalink")

  * Feb 19, 2021 11:57pm  Feb 19, 2021 11:57pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar216171_2.gif) interbucks](interbucks)

  * | Joined Jan 2012  | Status: Trader | [279 Posts](/search?do=process&provider=Member&searchuser=216171)

Thank you for this one Swingman.  
Luv to have an alert when the signals come up.  
  
Have a great weekend, looking forward to next weeks posts. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#69](/thread/post/13418311#post13418311 "Post Permalink")

  * Feb 20, 2021 12:33am  Feb 20, 2021 12:33am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar166111_2.gif) bopuc](bopuc)

  * | Joined Jan 2011  | Status: Trader | [53 Posts](/search?do=process&provider=Member&searchuser=166111)

**SwingMan,**  
  
a question regarding **smLazyHeading TrendChannel v1.5.1.**  
At the screen-shot below is a typical situation that looks like we won until you check lower TF and see that the price first triggered entry, went to SL and then to TP. The current screenshot is H1/D1 timeframe and when I go to M5 I see M5/H4 timeframe. Is there a way to have entry/tp/sl lines from the H1/D1 time frame when looking at the M5 time frame? Thanks.  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: smaller_TF.png
Size: 48 KB](/attachment/image/3868797/thumbnail?d=1613748727)](/attachment/image/3868797?d=1613748727)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#70](/thread/post/13418325#post13418325 "Post Permalink")

  * Feb 20, 2021 12:40am  Feb 20, 2021 12:40am 

  * [ Takisd](takisd)

  * Joined Dec 2005 | Status: Com Member = Scammer | [5,092 Posts](/search?do=process&provider=Member&searchuser=4969)

> [Quoting bopuc](/thread/post/13418311#post13418311 "View Quoted Post")
> 
> Disliked
> 
> SwingMan, a question regarding smLazyHeading TrendChannel v1.5.1. At the screen-shot below is a typical situation that looks like we won until you check lower TF and see that the price first triggered entry, went to SL and then to TP. The current screenshot is H1/D1 timeframe and when I go to M5 I see M5/H4 timeframe. Is there a way to have entry/tp/sl lines from the H1/D1 time frame when looking at the M5 time frame? Thanks. {image}
> 
> Ignored

  
The indicator is time frame sensitive.. So your signal on 5 min and on 1 hour wont be the same i think. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#71](/thread/post/13418405#post13418405 "Post Permalink")

  * Feb 20, 2021 1:45am  Feb 20, 2021 1:45am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting bopuc](/thread/post/13418311#post13418311 "View Quoted Post")
> 
> Disliked
> 
> SwingMan, a question regarding smLazyHeading TrendChannel v1.5.1. At the screen-shot below is a typical situation that looks like we won until you check lower TF and see that the price first triggered entry, went to SL and then to TP. The current screenshot is H1/D1 timeframe and when I go to M5 I see M5/H4 timeframe. Is there a way to have entry/tp/sl lines from the H1/D1 time frame when looking at the M5 time frame? Thanks.
> 
> Ignored

It would be possible, but will not do, because it has nothing to do with the basic idea.  
As _@Takisd_ noted, there is no match between the signals, and if you want that, you can draw the charts one below the other. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: GBPUSD-H1M5.PNG
Size: 61 KB](/attachment/image/3868863/thumbnail?d=1613753050)](/attachment/image/3868863?d=1613753050)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#72](/thread/post/13418417#post13418417 "Post Permalink")

  * Edited 8:02am  Feb 20, 2021 1:56am | Edited 8:02am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

**New indicator "smSpreadOsc_v1.0"**  
  
For scalpers on M1 or M5 it is important to know how the spread develops dynamically.  
  
This spread oscillator is used to calculate the percentage: (100 * Spread / ATR).  
An EMA (50) is calculated with the spread for every tick!. ATR period is 14.  
  
I have set a threshold of 20% because scalping above is less economical. 

Attached Image

![](/attachment/image/3868870?d=1613753757)

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [smSpreadOsc_v1.0.ex4](/attachment/file/3868869?d=1613753748) 10 KB | 533 downloads 

[0 ](javascript:void\(0\);) [3 ](javascript:void\(0\);)

  * [#73](/thread/post/13418637#post13418637 "Post Permalink")

  * Feb 20, 2021 4:27am  Feb 20, 2021 4:27am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar166111_2.gif) bopuc](bopuc)

  * | Joined Jan 2011  | Status: Trader | [53 Posts](/search?do=process&provider=Member&searchuser=166111)

> [Quoting SwingMan](/thread/post/13418405#post13418405 "View Quoted Post")
> 
> Disliked
> 
> {quote} It would be possible, but will not do, because it has nothing to do with the basic idea. As @Takisd noted, there is no match between the signals, and if you want that, you can draw the charts one below the other. {image}
> 
> Ignored

I have not deviated from the original idea, but I may not articulate my wish in the best way ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
  
I want to speed up visual backtesting. I understand that the indicator is time frame sensitive and that was the exact reason to ask for 'feature' so that I can backtest H1 signals on M5 timeframe for better _precision_. Currently, one needs to jump from timeframe to timeframe and manually draw entry/sl/tp lines on H1 (or compare two charts) then jump to M5 to verify if the entry signal went to TP or SL first.  
  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: 1.png
Size: 44 KB](/attachment/image/3869036/thumbnail?d=1613762784)](/attachment/image/3869036?d=1613762784)   

  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: 2.png
Size: 47 KB](/attachment/image/3869037/thumbnail?d=1613762785)](/attachment/image/3869037?d=1613762785)   

  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: 3.png
Size: 63 KB](/attachment/image/3869038/thumbnail?d=1613762786)](/attachment/image/3869038?d=1613762786)   

  
  
I respect your decision SwingMan. Won't bring this topic anymore. Cheers. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#74](/thread/post/13418680#post13418680 "Post Permalink")

  * Feb 20, 2021 5:07am  Feb 20, 2021 5:07am 

  * [ Montrose](montrose)

  * | Joined Sep 2014  | Status: Trader | [48 Posts](/search?do=process&provider=Member&searchuser=382414)

Thanks SwingMan for this interesting idea! Little bit confused about rule 4:  
  
**Note #4** \- The first idea for trading is to set after entry a trailing stop identical to the calculated distance between the lines.  
At loss when the exit level is reached, one should trade in the opposite direction**(a small hedge trade)** with the same trailing stop.  
Anyone who examines this rule will find that the use of a martingale can be very beneficial (I'm curious if someone will do that ...).  
The number of lots can be calculated with a percentage of the capital, one can limit the number of simultaneous orders, etc.  
  
I was wondering about 'a small hedge trade' in the opposite direction; for me a hedge trade (hedging) is taking an opposite trade while the first (opposite) trade is still active and 'a small trade' should indicate this trade has a lower lotsize as the first position(?). When I study later posts it seems the first trade is stopped out and a second trade is entered with higher lotsize?  
  
thanks Montrose 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#75](/thread/post/13418709#post13418709 "Post Permalink")

  * Feb 20, 2021 5:33am  Feb 20, 2021 5:33am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar166111_2.gif) bopuc](bopuc)

  * | Joined Jan 2011  | Status: Trader | [53 Posts](/search?do=process&provider=Member&searchuser=166111)

**Montose** ,  
  
I also interpreted the 'hedge trade' as opening trade in the opposite direction when the previous hits SL. The difference between the classic Margingage and LazyHeding version is discussed more around post [#33](https://www.forexfactory.com/thread/post/13407947#post13407947). 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#76](/thread/post/13418722#post13418722 "Post Permalink")

  * Feb 20, 2021 5:38am  Feb 20, 2021 5:38am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting bopuc](/thread/post/13418637#post13418637 "View Quoted Post")
> 
> Disliked
> 
> I have not deviated from the original idea, but I may not articulate my wish in the best way ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) I want to speed up visual backtesting. I understand that the indicator is time frame sensitive and that was the exact reason to ask for 'feature' so that I can backtest H1 signals on M5 timeframe for better precision. Currently, one needs to jump from timeframe to timeframe and manually draw entry/sl/tp lines on H1 (or compare two charts) then jump to M5 to verify if the entry signal went to TP or SL first....
> 
> Ignored

It seems interesting to me how you want to use the indicator. But that is a step further and I should also think about it.  
Maybe later I can do an MTF version for the indicator, you can remind me. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#77](/thread/post/13418734#post13418734 "Post Permalink")

  * Feb 20, 2021 5:44am  Feb 20, 2021 5:44am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting bopuc](/thread/post/13418709#post13418709 "View Quoted Post")
> 
> Disliked
> 
> Montose, I also interpreted the 'hedge trade' as opening trade in the opposite direction when the previous hits SL. The difference between the classic Margingage and LazyHeding version is discussed more around post [#33](https://www.forexfactory.com/thread/post/13407947#post13407947).
> 
> Ignored

Please do not forget that the SL is sliding, and not one of the drawn levels, because then it is the classic martingale.  
That is the decisive idea, as only _@gerval_ has commented so far. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#78](/thread/post/13418745#post13418745 "Post Permalink")

  * Feb 20, 2021 5:50am  Feb 20, 2021 5:50am 

  * [ gerval](gerval)

  * | Joined May 2020  | Status: Trader | [243 Posts](/search?do=process&provider=Member&searchuser=958353)

I am doing a manual backtesting with that idea. It is a bit expensive to do it like this, but I hope to see the behavior of the Trailing and the Martingale.  
  
The way Swingman is aiming with the TS is the only way to have a martingale probably with a chance of survival, or so I hope. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#79](/thread/post/13418752#post13418752 "Post Permalink")

  * Feb 20, 2021 5:58am  Feb 20, 2021 5:58am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting gerval](/thread/post/13418745#post13418745 "View Quoted Post")
> 
> Disliked
> 
> I am doing a manual backtesting with that idea. It is a bit expensive to do it like this, but I hope to see the behavior of the Trailing and the Martingale. The way Swingman is aiming with the TS is the only way to have a martingale probably with a chance of survival, or so I hope.
> 
> Ignored

Good luck, we all hope so! Unfortunately I can only write the EA a little later, then it will be easier to test and adjust the parameters. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#80](/thread/post/13418754#post13418754 "Post Permalink")

  * Edited 7:21am  Feb 20, 2021 6:01am | Edited 7:21am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting Montrose](/thread/post/13418680#post13418680 "View Quoted Post")
> 
> Disliked
> 
> ...I was wondering about 'a small hedge trade' in the opposite direction; for me a hedge trade (hedging) is taking an opposite trade while the first (opposite) trade is still active and 'a small trade' should indicate this trade has a lower lotsize as the first position(?). When I study later posts it seems the first trade is stopped out and a second trade is entered with higher lotsize? thanks Montrose
> 
> Ignored

Surely I didn't explain it clearly enough, and I don't plan to do that either ...  
Those who recognize and understand the idea can continue studying or ask specific questions, no problem.  
  
The table in #Post 33 should be studied, preferably with percentages.  
You are right, at exit you close the trade, you take the loss, you add the desired profit and the lotize is increased. Because the SL is sliding, this lot size will be smaller than in the classic martingale and of course you can also use this method for other systems. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * LazyHedging Trading Ideas
  *   * [ **Reply to Thread** ](/thread/1058948-lazyhedging-trading-ideas/reply#reply)

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

[EurCad Analysis and Trading Ideas](/thread/360980-eurcad-analysis-and-trading-ideas "Hello my friends. 
 
As of lately I have had remarkable success in trading EurCad and after hearing other traders ideas I decided that we...") 594 replies

[FSP Trading Journal and Trend Ideas](/thread/427493-fsp-trading-journal-and-trend-ideas "hello  
I am trying to post some of my trade Ideas here. 
there will be trend following and counter trend trades. 
I will post image rather...") 16 replies

[Forex trading platform that doesn't take your ideas](/thread/311080-forex-trading-platform-that-doesnt-take-your-ideas "Ninja trader, Metatrader, Tradestation all can copy the EA and indicators straight out of your PC. 
 
How do we go about developing a...") 11 replies

[Program Your Trading Ideas without being a programmer](/thread/225629-program-your-trading-ideas-without-being-a-programmer "I have to admit, I have a lot of trading ideas, but no programming skills. I hate paying a programmer to take 3 days to write an EA for me,...") 4 replies

[Exchanging trading ideas](/thread/136764-exchanging-trading-ideas "I'm opening this thread as a substitute for live chat like msn etc to exchange trading ideas and to filter of some posts at Igrok's thread,...") 37 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/1058948-lazyhedging-trading-ideas/reply#reply)
  * Subscribe
  * [271](javascript:void\(0\);)

Attachments: LazyHedging Trading Ideas

Tags: LazyHedging Trading Ideas

#  [](/thread/1058948-lazyhedging-trading-ideas)LazyHedging Trading Ideas 

  * 

  * [#81](/thread/post/13418850#post13418850 "Post Permalink")

  * Feb 20, 2021 8:14am  Feb 20, 2021 8:14am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1053756_3.gif) Lopfx](lopfx)

  * | Joined Jan 2021  | Status: Trader | [1 Post](/search?do=process&provider=Member&searchuser=1053756)

Good morning Mr [SwingMan](https://www.forexfactory.com/swingman),  
I am just newbie to forex and FF forum. Subscribe and love to learn read to every single post. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#82](/thread/post/13419284#post13419284 "Post Permalink")

  * Feb 21, 2021 3:18am  Feb 21, 2021 3:18am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar222411_10.gif) salimc](salimc)

  * | Joined Jan 2012  | Status: Trader | [1,328 Posts](/search?do=process&provider=Member&searchuser=222411)

[quote=MoneyZilla;13408539]Just want to share something, I think it can be valuable for you. Me is working on over 500 MT4s. When I have a bad strategy, something that crashes an account, I keep the chart and the settings forever. Until I find time to break down the cause of the crash. This usually happens within a year or two. Here is the important part. Was passing by a few of these in Jan'21, and just added a condition for time. Something like a metronome? A repeatable trading condition, if  
  
From your post, I understand that you don't use S/L and manage your trade with hedging. I wonder how do you save your position successfully with hedging? Is it possible to successfully hedge and save a trade?  
Thanks for your input. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#83](/thread/post/13419315#post13419315 "Post Permalink")

  * Feb 21, 2021 4:46am  Feb 21, 2021 4:46am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar439469_22.gif) MoneyZilla](moneyzilla)

  * Joined Dec 2015 | Status: Suuka Maadik | [3,630 Posts](/search?do=process&provider=Member&searchuser=439469)

> [Quoting salimc](/thread/post/13419284#post13419284 "View Quoted Post")
> 
> Disliked
> 
> Is it possible to successfully hedge and save a trade?
> 
> Ignored

  
There are 4 basic ways to hedge. Each way can have multiple differences. Will not go into details, just laying the most basic ways:  
  
1\. Hedge with using a SL. Push and Release technique. Exactly like in skiing.  
2\. Hedge without using a SL. The most lazy way to hedge. Keep all trades open and close at pips TP target or average pips/$ targets or _whatever_. This one is the most hard to make profitable, as it is the simplest, less complex way of all. The simpler it is, the harder is to get to.  
3\. Hedge based on closing the opposite instead of opening a new one. This one is very complicated.  
4\. Hedge based on equilibrium, i.e. closing the extra heavier side at whatever the TP until both open positions get to an equal number. Constantly maintaining the balance between both. This is used in a trending movement where the trend signals outperform significantly their counterparts.  
  
Ideally, in a buy movement, you want to have the buys below the sells, while the buys being the bigger lot. How do you position yourself to make this happen?

Maadik Hugiis. IQ 69.

[0 ](javascript:void\(0\);) [3 ](javascript:void\(0\);)

  * [#84](/thread/post/13419320#post13419320 "Post Permalink")

  * Edited 5:43am  Feb 21, 2021 4:56am | Edited 5:43am 

  * [ Montrose](montrose)

  * | Joined Sep 2014  | Status: Trader | [48 Posts](/search?do=process&provider=Member&searchuser=382414)

> [Quoting SwingMan](/thread/post/13418754#post13418754 "View Quoted Post")
> 
> Disliked
> 
> {quote} Surely I didn't explain it clearly enough, and I don't plan to do that either ... Those who recognize and understand the idea can continue studying or ask specific questions, no problem. The table in #Post 33 should be studied, preferably with percentages. You are right, at exit you close the trade, you take the loss, you add the desired profit and the lotize is increased. Because the SL is sliding, this lot size will be smaller than in the classic martingale and of course you can also use this method for other systems.
> 
> Ignored

Thanks for your reply. I am not 'Those who recognize and understand the idea' (I have a low IQ just as MZ) but I have already traded similar strategies on live accounts and want to share my findings just to warn/contribute here, hope this will help. If you start a progression you do not have control anymore; you will have to accumulate positions and have to use stop orders to be sure to be filled at certain prices otherwise your plan will not work. Stop orders = carte blanche for brokers they like it very much. Imagine your accumulated strategy is entering news (huge [spreads](/brokers/spreads "View Live Spreads on the Broker Guide")) or Asian session (similar). Normally you will avoid these sessions.  
  
best Montrose 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#85](/thread/post/13419334#post13419334 "Post Permalink")

  * Feb 21, 2021 6:00am  Feb 21, 2021 6:00am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting Montrose](/thread/post/13419320#post13419320 "View Quoted Post")
> 
> Disliked
> 
> ...Thanks for your reply. I am not 'Those who recognize and understand the idea' (I have a low IQ just as MZ) but I have already traded similar strategies on live accounts and want to share my findings just to warn/contribute here, hope this will help. If you start a progression you do not have control anymore; you will have to accumulate positions and have to use stop orders to be sure to be filled at certain prices otherwise your plan will not work. Stop orders = carte blanche for brokers they like it very much. Imagine your accumulated strategy...
> 
> Ignored

I don't even want to debate how dangerous it is to make progressions.  
I wrote "a small hedge trade" with the thought that it is not a continuous trading (I also analyzed and renounced that), but step by step for every new signal. My description is surely too short and unclear, I have only presented a possible trading idea and a possible hedge.  
Certainly only a few will analyze and comment on it. General claims are correct, but don't help me, that's why I'm always happy that someone can contribute.  
  
I don't know which strategies you traded - I tested at least three of the ones in the previous post by _@MoneyZilla_ , programmed them and even traded some live without being enthusiastic.  
  
In the thread "MGH System (Martingale Grid & Hedging)" I posted an EA which I ran live for a long time until a major loss occurred (1000 € is not that much either ...), and then I stopped it. (roughly like variant 1. at _@MoneyZilla_)  
  
I also examined the "Snowballs and the anti-grid" by _@7bit_ for a while - (roughly like variant 2. at _@MoneyZilla_)  
  
etc.  
... 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#86](/thread/post/13419472#post13419472 "Post Permalink")

  * Feb 21, 2021 12:52pm  Feb 21, 2021 12:52pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar833238_1.gif) totocayetano](totocayetano)

  * | Membership Revoked  | Joined Jul 2019 | [94 Posts](/search?do=process&provider=Member&searchuser=833238)

Based on what I have experienced, with all the strategies that I have been using, hedging is the most profitable. Average of 50% profit in a month. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#87](/thread/post/13419513#post13419513 "Post Permalink")

  * Feb 21, 2021 3:06pm  Feb 21, 2021 3:06pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar427419_1.gif) suneth2](suneth2)

  * Joined Sep 2015 | Status: Learning Price Action & Discipline | [328 Posts](/search?do=process&provider=Member&searchuser=427419)

> [Quoting totocayetano](/thread/post/13419472#post13419472 "View Quoted Post")
> 
> Disliked
> 
> Based on what I have experienced, with all the strategies that I have been using, hedging is the most profitable. Average of 50% profit in a month.
> 
> Ignored

Can you share some good GRID EA for test ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

Failure is not failure if you learn from it...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#88](/thread/post/13419800#post13419800 "Post Permalink")

  * Feb 22, 2021 2:47am  Feb 22, 2021 2:47am 

  * [ Montrose](montrose)

  * | Joined Sep 2014  | Status: Trader | [48 Posts](/search?do=process&provider=Member&searchuser=382414)

[quote=SwingMan;13419334]{quote} I don't even want to debate how dangerous it is to make progressions. I wrote "a small hedge trade" with the thought that it is not a continuous trading (I also analyzed and renounced that), but step by step for every new signal.  
  
Yes I agree SwingMan, thanks for your reply. It does not matter which strategy we run but if it's using compounding lotsizes; eventually a trade will enter the liquidity provider heaven into news/Asian session.  
  
best Montrose 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#89](/thread/post/13420138#post13420138 "Post Permalink")

  * Feb 22, 2021 12:03pm  Feb 22, 2021 12:03pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar833238_1.gif) totocayetano](totocayetano)

  * | Membership Revoked  | Joined Jul 2019 | [94 Posts](/search?do=process&provider=Member&searchuser=833238)

> [Quoting suneth2](/thread/post/13419513#post13419513 "View Quoted Post")
> 
> Disliked
> 
> {quote} Can you share some good GRID EA for test ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)
> 
> Ignored

I haven't tested a good grid EA yet. But I'm searching for it. I want to test EA's with different methods. Right now, I've been testing two EA's with potentials. One is a hedging EA and another one is a multi-currencies/scalping EA. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#90](/thread/post/13420733#post13420733 "Post Permalink")

  * Feb 22, 2021 7:00pm  Feb 22, 2021 7:00pm 

  * [ gerval](gerval)

  * | Joined May 2020  | Status: Trader | [243 Posts](/search?do=process&provider=Member&searchuser=958353)

I have done a small manual backtest of EURUSD on H1, Feb-19 to Jul-19 with a fixed spread of 1.5 pips (15 ticks), it has been 75 cycles (206 trades). I have done it by taking the trades both for and against the indicator. With pending orders in the 2 immediate lines since the indicator appears and using the trailing stop for the sl.  
I have done it in both directions to know to what extent the indicator was working in the price sense, and also to test the martingale with the trailing stop in a possible more difficult situation. On many occasions the price goes in the same direction as the indicator, but first the price makes a retreat and we touch the sl, so when using the martingale at least 2 or 3 times it benefits us.  
  
This chart shows all the trades both for and against the indicator signal and the necessary entries with the martingale and the trailing stop.  

Attached Image

![](/attachment/image/3870341?d=1613987925)

  
In the following chart, the necessary number of entries with signals against the indicator, average of operations to exit in profit of 3.07.  

Attached Image

![](/attachment/image/3870342?d=1613987960)

  
In the last chart entering only in favor of the indicator when and the necessary martingale entries to end a cycle (from the time it is entered until it ends in profit), average of operations to exit in profit of 2.33.  

Attached Image

![](/attachment/image/3870343?d=1613987989)

  
The number is not very extensive, but it brings us a little closer to the idea of using the martingale with the trailing stop, which in many cases benefits us by closing for sl more times, but entering with a lower lot in the next and therefore being able to do more operations until the price goes in our favor. Although at some point the martingale forced us to open too much lot, the question is to know if it takes a long time and we can make the system profitable until that moment arrives.  
  
Another possibility to avoid an area in which the price enters the range and opens and closes us many times, is to limit the number of entries (3 or 4) and in case we do not profit, assume the losses and continue with those operations after The indicator will appear again, since several cycles of 3 or 4 consecutive losses are not repeated so many times and according to the necessary average it is 2.33. Although to know that, a much more extensive backtest is needed and in different pairs and timeframes.

[0 ](javascript:void\(0\);) [3 ](javascript:void\(0\);)

  * [#91](/thread/post/13420823#post13420823 "Post Permalink")

  * Feb 22, 2021 7:44pm  Feb 22, 2021 7:44pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting gerval](/thread/post/13420733#post13420733 "View Quoted Post")
> 
> Disliked
> 
> I have done a small manual backtest of EURUSD on H1, Feb-19 to Jul-19 ...
> 
> Ignored

A very careful evaluation, thank you very much!  
  
Is on the Y-axis the maximum level reached (as in my table)?  
In this case, one can sleep well with 0.1-0.2% risk. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#92](/thread/post/13420946#post13420946 "Post Permalink")

  * Feb 22, 2021 8:55pm  Feb 22, 2021 8:55pm 

  * [ gerval](gerval)

  * | Joined May 2020  | Status: Trader | [243 Posts](/search?do=process&provider=Member&searchuser=958353)

sleeping with a martingale is difficult, hehe  
  
When I have the numbers in front, I comment on how the TS's route has been and therefore the necessary lot to enter according to their tables. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#93](/thread/post/13421900#post13421900 "Post Permalink")

  * Edited 7:51pm  Feb 23, 2021 6:40am | Edited 7:51pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar375174_1.gif) Go5](go5)

  * Joined Jun 2014 | Status: Invisible | [1,437 Posts](/search?do=process&provider=Member&searchuser=375174) | Online Now 

> [Quoting gerval](/thread/post/13420946#post13420946 "View Quoted Post")
> 
> Disliked
> 
> sleeping with a martingale is difficult, hehe When I have the numbers in front, I comment on how the TS's route has been and therefore the necessary lot to enter according to their tables.
> 
> Ignored

Instead of MG, you might have a look at using a progressive betting sequence like 1-2-3 or 1-3-2-6.  
That way, as long as you have good statistics of the system's average consecutive winners/losers, you can adapt the type of sequence and control your DD with a good night's sleep...  
  
I made a little stop trailer( with xxreema - lol), makes it a bit easier.  
  

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [INSTANT-TRAIL-STEP.ex4](/attachment/file/3871450?d=1614077488) 113 KB | 445 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#94](/thread/post/13421930#post13421930 "Post Permalink")

  * Feb 23, 2021 7:11am  Feb 23, 2021 7:11am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting Go5](/thread/post/13421900#post13421900 "View Quoted Post")
> 
> Disliked
> 
> ... Instead of MG, you might have a look at using a progressive betting sequence like 1-2-3 or 1-3-2-6. That way, as long as you have good statistics of the system's average consecutive winners/losers, you can adapt the type of sequence and control your DD with a good night's sleep...
> 
> Ignored

Please all to not post any discussions about martingales here in the thread!  
  
I suggested to analyze an alternative to MGs, which I haven't seen anywhere else, _@gerval_ understood what it was about, that's all.  
  
About progressive betting I recommend studying the book/e-book and the systems of "roulettetrader#com". There one can maybe learn something and trade "good statistics" successfully. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#95](/thread/post/13421975#post13421975 "Post Permalink")

  * Feb 23, 2021 8:26am  Feb 23, 2021 8:26am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar472073_2.gif) ordosgoitia](ordosgoitia)

  * Joined Jun 2016 | Status: Trader | [268 Posts](/search?do=process&provider=Member&searchuser=472073)

> [Quoting SwingMan](/thread/post/13421930#post13421930 "View Quoted Post")
> 
> Disliked
> 
> {quote} Please all to not post any discussions about martingales here in the thread! I suggested to analyze an alternative to MGs, which I haven't seen anywhere else, @gerval understood what it was about, that's all. About progressive betting I recommend studying the book/e-book and the systems of "roulettetrader#com". There one can maybe learn something and trade "good statistics" successfully.
> 
> Ignored

his strategy is great,, i know him, his name is Don.. his progressive trading makes profits way bigger if you have a good system. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#96](/thread/post/13421977#post13421977 "Post Permalink")

  * Feb 23, 2021 8:30am  Feb 23, 2021 8:30am 

  * [ gerval](gerval)

  * | Joined May 2020  | Status: Trader | [243 Posts](/search?do=process&provider=Member&searchuser=958353)

I understand that the tables that he put, is based on the route of the TS and we would enter and with the lot of the tables combining it.  
  
Continuing with the data in the table, in the cycle of 8 operations in favor of the indicator, I do not respect the average of the middle of the route, the maximum that the TS reached in favor was 1/3 of the route in one of the inputs, the The rest was not in favor at all, the price moved between the entry and stop loss levels on many occasions (it is not usual), so the lot we would have had to double in all entries.  
0.1-0.2-0.4-0.6-1.2-2.4-4.8-OK  
  
The problem is that when the price enters the range, perhaps it is a possibility to stop, take the loss and start another cycle at another point on the chart, for example, the next time the indicator appears, and you could even look for a 3rd cycle.  
  
Or ... make a different sequence of entries, for example 2 sales in a row, 3 purchases in a row. It is already a matter of testing.  
  
Although if the normal thing is not that 8 operations or more are reached, and the usual thing is that the TS moves in favor avoiding so much lot, it could be sought to make it profitable. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#97](/thread/post/13421985#post13421985 "Post Permalink")

  * Feb 23, 2021 8:46am  Feb 23, 2021 8:46am 

  * [ gerval](gerval)

  * | Joined May 2020  | Status: Trader | [243 Posts](/search?do=process&provider=Member&searchuser=958353)

> [Quoting Go5](/thread/post/13421900#post13421900 "View Quoted Post")
> 
> Disliked
> 
> {quote} Instead of MG, you might have a look at using a progressive betting sequence like 1-2-3 or 1-3-2-6. That way, as long as you have good statistics of the system's average consecutive winners/losers, you can adapt the type of sequence and control your DD with a good night's sleep... I made a little stop trailer( with xxreema - lol), makes it a bit easier. {file}
> 
> Ignored

  
I will test your Trailing Stop, thank you. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#98](/thread/post/13422769#post13422769 "Post Permalink")

  * Edited Feb 24, 2021 6:58am  Feb 23, 2021 7:55pm | Edited Feb 24, 2021 6:58am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar375174_1.gif) Go5](go5)

  * Joined Jun 2014 | Status: Invisible | [1,437 Posts](/search?do=process&provider=Member&searchuser=375174) | Online Now 

> [Quoting gerval](/thread/post/13421985#post13421985 "View Quoted Post")
> 
> Disliked
> 
> {quote} I will test your Trailing Stop, thank you.
> 
> Ignored

I forgot to activate the TP option, you can download it again.  
  
Also - if SwingMan so desires, I'll delete it...  
  

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [INSTANT-TRAIL-STEP.ex4](/attachment/file/3872115?d=1614117513) 120 KB | 475 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#99](/thread/post/13426103#post13426103 "Post Permalink")

  * Feb 25, 2021 8:42am  Feb 25, 2021 8:42am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar726101_4.gif) Marcelomtn](marcelomtn)

  * Joined Oct 2018 | Status: Trader | [233 Posts](/search?do=process&provider=Member&searchuser=726101)

> [Quoting MoneyZilla](/thread/post/13419315#post13419315 "View Quoted Post")
> 
> Disliked
> 
> {quote} There are 4 basic ways to hedge. Each way can have multiple differences. Will not go into details, just laying the most basic ways: 1. Hedge with using a SL. Push and Release technique. Exactly like in skiing. 2. Hedge without using a SL. The most lazy way to hedge. Keep all trades open and close at pips TP target or average pips/$ targets or whatever. This one is the most hard to make profitable, as it is the simplest, less complex way of all. The simpler it is, the harder is to get to. 3. Hedge based on closing the opposite instead of...
> 
> Ignored

1) Surefire system?  
2) Do not double your lots or the lack of margin will kill your account ?  
3) Maybe you just right down the loss and make an increment on next signal if it good and try to profif from this one ?  
4) Avoiding swap ? you tp some of your positions to release margin and avoid swap, but maintain lot difference for desired bias.  
  
Well those are my guessings, my iq is not 69 =( ![](https://resources.faireconomy.media/images/emojis/64/1f61c.png?v=15.1)

MTN

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#100](/thread/post/13426218#post13426218 "Post Permalink")

  * Feb 25, 2021 12:36pm  Feb 25, 2021 12:36pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar439469_22.gif) MoneyZilla](moneyzilla)

  * Joined Dec 2015 | Status: Suuka Maadik | [3,630 Posts](/search?do=process&provider=Member&searchuser=439469)

> [Quoting Marcelomtn](/thread/post/13426103#post13426103 "View Quoted Post")
> 
> Disliked
> 
> {quote} 1) Surefire system? 2) Do not double your lots or the lack of margin will kill your account ? 3) Maybe you just right down the loss and make an increment on next signal if it good and try to profif from this one ? 4) Avoiding swap ? you tp some of your positions to release margin and avoid swap, but maintain lot difference for desired bias. Well those are my guessings, my iq is not 69 =( ![](https://resources.faireconomy.media/images/emojis/64/1f61c.png?v=15.1)
> 
> Ignored

  
Unfortunately, for you, I am keeping quite impressive library of the first three hedging ways...![](https://resources.faireconomy.media/images/emojis/64/1f923.png?v=15.1)  
Unfortunately, this time for me, the 4th hedge stopped working in my latest EA versions. For quite a while, it seems. When other ways were developed, the 4th one got broken. Historically the 4th was built second... Mr. Programmer will make it work again next week.  
  
Hedge 1  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: hedge1.gif
Size: 9 KB](/attachment/image/3873537/thumbnail?d=1614224212)](/attachment/image/3873537?d=1614224212)   

  
Hedge 2  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: hedge2.gif
Size: 7 KB](/attachment/image/3873538/thumbnail?d=1614224212)](/attachment/image/3873538?d=1614224212)   

  
Hedge 3  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: hedge3.gif
Size: 6 KB](/attachment/image/3873539/thumbnail?d=1614224212)](/attachment/image/3873539?d=1614224212)   

  
To crack down hedging, you need an IQ _below_ 75\. If you are a happy owner of a higher IQ volumes? I am really sorry...![](https://resources.faireconomy.media/images/emojis/64/1f937-1f3fb-200d-2642-fe0f.png?v=15.1)

Maadik Hugiis. IQ 69.

[0 ](javascript:void\(0\);) [3 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * LazyHedging Trading Ideas
  *   * [ **Reply to Thread** ](/thread/1058948-lazyhedging-trading-ideas/reply#reply)

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

[EurCad Analysis and Trading Ideas](/thread/360980-eurcad-analysis-and-trading-ideas "Hello my friends. 
 
As of lately I have had remarkable success in trading EurCad and after hearing other traders ideas I decided that we...") 594 replies

[FSP Trading Journal and Trend Ideas](/thread/427493-fsp-trading-journal-and-trend-ideas "hello  
I am trying to post some of my trade Ideas here. 
there will be trend following and counter trend trades. 
I will post image rather...") 16 replies

[Forex trading platform that doesn't take your ideas](/thread/311080-forex-trading-platform-that-doesnt-take-your-ideas "Ninja trader, Metatrader, Tradestation all can copy the EA and indicators straight out of your PC. 
 
How do we go about developing a...") 11 replies

[Program Your Trading Ideas without being a programmer](/thread/225629-program-your-trading-ideas-without-being-a-programmer "I have to admit, I have a lot of trading ideas, but no programming skills. I hate paying a programmer to take 3 days to write an EA for me,...") 4 replies

[Exchanging trading ideas](/thread/136764-exchanging-trading-ideas "I'm opening this thread as a substitute for live chat like msn etc to exchange trading ideas and to filter of some posts at Igrok's thread,...") 37 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/1058948-lazyhedging-trading-ideas/reply#reply)
  * Subscribe
  * [271](javascript:void\(0\);)

Attachments: LazyHedging Trading Ideas

Tags: LazyHedging Trading Ideas

#  [](/thread/1058948-lazyhedging-trading-ideas)LazyHedging Trading Ideas 

  * 

  * [#101](/thread/post/13427245#post13427245 "Post Permalink")

  * Feb 25, 2021 11:54pm  Feb 25, 2021 11:54pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar726101_4.gif) Marcelomtn](marcelomtn)

  * Joined Oct 2018 | Status: Trader | [233 Posts](/search?do=process&provider=Member&searchuser=726101)

> [Quoting MoneyZilla](/thread/post/13426218#post13426218 "View Quoted Post")
> 
> Disliked
> 
> {quote} Unfortunately, for you, I am keeping quite impressive library of the first three hedging ways...![](https://resources.faireconomy.media/images/emojis/64/1f923.png?v=15.1) Unfortunately, this time for me, the 4th hedge stopped working in my latest EA versions. For quite a while, it seems. When other ways were developed, the 4th one got broken. Historically the 4th was built second... Mr. Programmer will make it work again next week. Hedge 1 {image} Hedge 2 {image} Hedge 3 {image} To crack down hedging, you need an IQ below 75. If you are a happy owner of a higher IQ volumes? I am...
> 
> Ignored

  
Nah itś not unfortunate, to crack down hedging you only need to know addition and subtraction, if you don't, maybe just use rocks? ![](https://resources.faireconomy.media/images/emojis/64/1f937-200d-2642-fe0f.png?v=15.1)

Attached Image

![](/attachment/image/3874139?d=1614264683)

MTN

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#102](/thread/post/13427326#post13427326 "Post Permalink")

  * Feb 26, 2021 12:30am  Feb 26, 2021 12:30am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting Marcelomtn](/thread/post/13427245#post13427245 "View Quoted Post")
> 
> Disliked
> 
> ...Nah itś not unfortunate, to crack down hedging you only need to know addition and subtraction, if you don't, maybe just use rocks? ![](https://resources.faireconomy.media/images/emojis/64/1f937-200d-2642-fe0f.png?v=15.1)
> 
> Ignored

Dear Marcelo,  
please do not post your personal opinions and experiences about martingales anymore, this is not a thread for it.  
  
If you have the time and pleasure to study, comment or criticize my martingale variant, I would be very satisfied ... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#103](/thread/post/13427336#post13427336 "Post Permalink")

  * Feb 26, 2021 12:34am  Feb 26, 2021 12:34am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar439469_22.gif) MoneyZilla](moneyzilla)

  * Joined Dec 2015 | Status: Suuka Maadik | [3,630 Posts](/search?do=process&provider=Member&searchuser=439469)

> [Quoting Marcelomtn](/thread/post/13427245#post13427245 "View Quoted Post")
> 
> Disliked
> 
> {quote} Nah itś not unfortunate, to crack down hedging you only need to know addition and subtraction, if you don't, maybe just use rocks? ![](https://resources.faireconomy.media/images/emojis/64/1f937-200d-2642-fe0f.png?v=15.1) {image}
> 
> Ignored

  
Any kid from 1st grade or higher, can bring down the trading business! Poor stupid bankers! I agree with you! Entirely!![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f44f.png?v=15.1)  
  
Just wondering... why they are struggling with hedging, so hard, here, on this forum? Why don't you just _help_ them?🥸

Maadik Hugiis. IQ 69.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#104](/thread/post/13427384#post13427384 "Post Permalink")

  * Feb 26, 2021 12:51am  Feb 26, 2021 12:51am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar726101_4.gif) Marcelomtn](marcelomtn)

  * Joined Oct 2018 | Status: Trader | [233 Posts](/search?do=process&provider=Member&searchuser=726101)

> [Quoting MoneyZilla](/thread/post/13427336#post13427336 "View Quoted Post")
> 
> Disliked
> 
> {quote} Any kid from 1st grade or higher, can bring down the trading business! Poor stupid bankers! I agree with you! Entirely!![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f44f.png?v=15.1) Just wondering... why they are struggling with hedging, so hard, here, on this forum? Why don't you just help them?🥸
> 
> Ignored

  
I aways agreed with you ![](https://resources.faireconomy.media/images/emojis/64/1f61c.png?v=15.1) thats why i ![](https://resources.faireconomy.media/images/emojis/64/1f974.png?v=15.1) hedge, without using MG...  
  
  
**Why don't you just _help_ them?**  
  
\- Like you, i just did  
  
**And i agree with SwingMan, MG will aways blow the account.**

MTN

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#105](/thread/post/13427428#post13427428 "Post Permalink")

  * Feb 26, 2021 1:09am  Feb 26, 2021 1:09am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

_@MoneyZilla_ and _@Marcelomtn,_  
here I started a private thread for both of you, so that you can only post one here exclusively about my trading idea or forget about them.  
[  
Opinions and Experiences with Hedging and Martingale](https://www.forexfactory.com/thread/post/13427408#post13427408)  
. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#106](/thread/post/13428399#post13428399 "Post Permalink")

  * Feb 26, 2021 1:18pm  Feb 26, 2021 1:18pm 

  * [ sp00100](sp00100)

  * | Joined Feb 2021  | Status: Trader | [1 Post](/search?do=process&provider=Member&searchuser=1071992)

Can anyone help me with a EA like Killa-Gorilla please 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#107](/thread/post/13432719#post13432719 "Post Permalink")

  * Mar 2, 2021 4:57am  Mar 2, 2021 4:57am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar970926_1.gif) carlosmartin](carlosmartin)

  * | Joined Jun 2020  | Status: Trader | [7 Posts](/search?do=process&provider=Member&searchuser=970926)

Hi guys! I tried in many ways to work on my own EA but my knowledge is still limited and so I was not successful ![](https://resources.faireconomy.media/images/emojis/64/1f641.png?v=15.1) However in my search for solutions I found this EA made specifically for Jake Bernstein's MAC (moving average channel). I did some tests but apparently the orders are being made in the opposite direction...  
[Source](https://www.mql5.com/en/forum/180578)

Attached File(s)

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [ma_channel.mq4](/attachment/file/3877461?d=1614628512) 11 KB | 303 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#108](/thread/post/13432799#post13432799 "Post Permalink")

  * Mar 2, 2021 6:30am  Mar 2, 2021 6:30am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting carlosmartin](/thread/post/13432719#post13432719 "View Quoted Post")
> 
> Disliked
> 
> Hi guys! I tried in many ways to work on my own EA but my knowledge is still limited and so I was not successful ![](https://resources.faireconomy.media/images/emojis/64/1f641.png?v=15.1) However in my search for solutions I found this EA made specifically for Jake Bernstein's MAC (moving average channel). I did some tests but apparently the orders are being made in the opposite direction... [Source](https://www.mql5.com/en/forum/180578) {file}
> 
> Ignored

I've made a few adjustments for you and one can test both directions.  
  
I have not analyzed the algorithm for entries. 

Attached File(s)

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [ma_channel-SwichOrders.mq4](/attachment/file/3877505?d=1614634061) 14 KB | 656 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#109](/thread/post/13437329#post13437329 "Post Permalink")

  * Mar 4, 2021 7:53pm  Mar 4, 2021 7:53pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar444013_1.gif) bred](bred)

  * | Joined Jan 2016  | Status: Trader | [58 Posts](/search?do=process&provider=Member&searchuser=444013)

> [Quoting SwingMan](/thread/post/13397986#post13397986 "View Quoted Post")
> 
> Disliked
> 
> In his thread "Jake Bernstein 10 SMA high 8 SMA low trading system" [https://www.forexfactory.com/thread/...high-8-sma-low](https://www.forexfactory.com/thread/1006033-jake-bernstein-10-sma-high-8-sma-low), @Toto69 presented his personal trading variant with some discretionary trading options. I used to read a couple of books by Jake and here I am posting some comments and indicators for the 10/8 trading idea. Here I only post a small indicator, and when I have time I will continue to post more things and an EA, but everyone can test their ideas and apply other trend following or counter trend...
> 
> Ignored

smLazyHedging TrendOsc_v1.1 Nice indicator.  
Other 2 indi cause mt4 not responding.  
  
Jz some idea. if you have smLazyHedging TrendOsc_v1.1 dashboard version might help you re-enter/ filter pair quickly.  
  
Anyway, working nicely with below tools. 

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [CurrencyStrengthBoard_v1.8 600+.ex4](/attachment/file/3880321?d=1614855152) 54 KB | 452 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#110](/thread/post/13437394#post13437394 "Post Permalink")

  * Mar 4, 2021 8:31pm  Mar 4, 2021 8:31pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting bred](/thread/post/13437329#post13437329 "View Quoted Post")
> 
> Disliked
> 
> {quote} smLazyHedging TrendOsc_v1.1 Nice indicator. Other 2 indi cause mt4 not responding. Jz some idea. if you have smLazyHedging TrendOsc_v1.1 dashboard version might help you re-enter/ filter pair quickly. Anyway, working nicely with below tools. {file}
> 
> Ignored

  
OK,  
You can also test my Strength Indicators like here: [https://www.forexfactory.com/thread/...42#post9016342](https://www.forexfactory.com/thread/post/9016342#post9016342)

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#111](/thread/post/13447901#post13447901 "Post Permalink")

  * Mar 12, 2021 3:06am  Mar 12, 2021 3:06am 

  * [ lain7123](lain7123)

  * | Joined May 2020  | Status: Trader | [116 Posts](/search?do=process&provider=Member&searchuser=960495)

> [Quoting SwingMan](/thread/post/13437394#post13437394 "View Quoted Post")
> 
> Disliked
> 
> {quote} OK, You can also test my Strength Indicators like here: [https://www.forexfactory.com/thread/...42#post9016342](https://www.forexfactory.com/thread/post/9016342#post9016342)
> 
> Ignored

Greetings SwingMan, I hope this is not much of a bother, would you kindly add alerts to your smACME Rectangle_v2.1 indicator I got this on ex4 because I don´t think you ever share the mql4 for that version.  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: smacme rectangle.png
Size: 81 KB](/attachment/image/3886852/thumbnail?d=1615485964)](/attachment/image/3886852?d=1615485964)   

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [smACME Rectangle_v2.1.ex4](/attachment/file/3886853?d=1615485974) 14 KB | 407 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#112](/thread/post/13448110#post13448110 "Post Permalink")

  * Edited 7:54am  Mar 12, 2021 5:21am | Edited 7:54am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting lain7123](/thread/post/13447901#post13447901 "View Quoted Post")
> 
> Disliked
> 
> {quote} Greetings SwingMan, I hope this is not much of a bother, would you kindly add alerts to your smACME Rectangle_v2.1 indicator I got this on ex4 because I don´t think you ever share the mql4 for that version. {image}{file}
> 
> Ignored

No problem, here is the indicator, unfortunately I can't make any changes now. 

Attached File(s)

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [smACME Rectangle_v2.1.mq4](/attachment/file/3887122?d=1615503250) 21 KB | 835 downloads 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#113](/thread/post/13452372#post13452372 "Post Permalink")

  * Mar 15, 2021 11:47pm  Mar 15, 2021 11:47pm 

  * [ lain7123](lain7123)

  * | Joined May 2020  | Status: Trader | [116 Posts](/search?do=process&provider=Member&searchuser=960495)

> [Quoting SwingMan](/thread/post/13448110#post13448110 "View Quoted Post")
> 
> Disliked
> 
> {quote} No problem, here is the indicator, unfortunately I can't make any changes now. {file}
> 
> Ignored

For when you have time, I would really appreciate if you can make it work on renko charts, I have been trying to make it work but it still doesn´t appear.. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#114](/thread/post/13473850#post13473850 "Post Permalink")

  * Edited 4:47am  Mar 30, 2021 4:19am | Edited 4:47am 

  * [ ntk](ntk)

  * Joined Dec 2018 | Status: Trader | [1,263 Posts](/search?do=process&provider=Member&searchuser=747159)

> [Quoting lain7123](/thread/post/13447901#post13447901 "View Quoted Post")
> 
> Disliked
> 
> {quote} Greetings SwingMan, I hope this is not much of a bother, would you kindly add alerts to your smACME Rectangle_v2.1 indicator I got this on ex4 because I don´t think you ever share the mql4 for that version. {image}{file}
> 
> Ignored

Could you pls kindly advise how you want to have alert going off with this smACME Rectangle_v2.1 indicator. and on what reason.  
  
Here is one example could you pls show on chart so it is easier for me to understand  
  
ON GJ it appears only once while on GU it appears 3x near current price why? and what can you interpret from that appearance?  
  
Thanks 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: 9b3cddd2cf3ca8b660479a5bc4ea59b9.png
Size: 60 KB](/attachment/image/3901984/thumbnail?d=1617046096)](/attachment/image/3901984?d=1617046096)   
[![Click to Enlarge

Name: cf0d64b818b616acc79e46bafa7117a8.png
Size: 75 KB](/attachment/image/3901988/thumbnail?d=1617047104)](/attachment/image/3901988?d=1617047104)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#115](/thread/post/13474224#post13474224 "Post Permalink")

  * Mar 30, 2021 1:12pm  Mar 30, 2021 1:12pm 

  * [ ntk](ntk)

  * Joined Dec 2018 | Status: Trader | [1,263 Posts](/search?do=process&provider=Member&searchuser=747159)

> [Quoting Go5](/thread/post/13421900#post13421900 "View Quoted Post")
> 
> Disliked
> 
> {quote} Instead of MG, you might have a look at using a progressive betting sequence like 1-2-3 or 1-3-2-6. That way, as long as you have good statistics of the system's average consecutive winners/losers, you can adapt the type of sequence and control your DD with a good night's sleep... I made a little stop trailer( with xxreema - lol), makes it a bit easier. {file}
> 
> Ignored

Got a warning from broker "account due to hyper activity disabled, when use this EA, re check code" 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#116](/thread/post/13474226#post13474226 "Post Permalink")

  * Mar 30, 2021 1:15pm  Mar 30, 2021 1:15pm 

  * [ ntk](ntk)

  * Joined Dec 2018 | Status: Trader | [1,263 Posts](/search?do=process&provider=Member&searchuser=747159)

> [Quoting MoneyZilla](/thread/post/13426218#post13426218 "View Quoted Post")
> 
> Disliked
> 
> {quote} Unfortunately, for you, I am keeping quite impressive library of the first three hedging ways...![](https://resources.faireconomy.media/images/emojis/64/1f923.png?v=15.1) Unfortunately, this time for me, the 4th hedge stopped working in my latest EA versions. For quite a while, it seems. When other ways were developed, the 4th one got broken. Historically the 4th was built second... Mr. Programmer will make it work again next week. Hedge 1 {image} Hedge 2 {image} Hedge 3 {image} To crack down hedging, you need an IQ below 75. If you are a happy owner of a higher IQ volumes? I am...
> 
> Ignored

system 2 and 3 is impressive, what are requirement on capital, and orders, do you share the hedge EA? or are they commercial? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#117](/thread/post/13474307#post13474307 "Post Permalink")

  * Mar 30, 2021 3:16pm  Mar 30, 2021 3:16pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar439469_22.gif) MoneyZilla](moneyzilla)

  * Joined Dec 2015 | Status: Suuka Maadik | [3,630 Posts](/search?do=process&provider=Member&searchuser=439469)

> [Quoting ntk](/thread/post/13474226#post13474226 "View Quoted Post")
> 
> Disliked
> 
> {quote} system 2 and 3 is impressive, what are requirement on capital, and orders, do you share the hedge EA? or are they commercial?
> 
> Ignored

  
Low risk floats, depending on the time frame traded, usually around 4-8% of a draw-down vs 20-30% of an annual return.   
These two types of hedging are not suitable for high risk trading, as it is all turns into a gamble, at some point. If one is certain about the direction? Why hedge?   
Hedging here works at small bites, catching/closing at some fake counter trend movements or corrections.  
Bigger bites/revs = not proportionally bigger draw-downs...![](https://resources.faireconomy.media/images/emojis/64/1f937-1f3fb-200d-2642-fe0f.png?v=15.1)  
This is a private ai system (indies/eas).

Maadik Hugiis. IQ 69.

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#118](/thread/post/13474315#post13474315 "Post Permalink")

  * Mar 30, 2021 3:25pm  Mar 30, 2021 3:25pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar375174_1.gif) Go5](go5)

  * Joined Jun 2014 | Status: Invisible | [1,437 Posts](/search?do=process&provider=Member&searchuser=375174) | Online Now 

> [Quoting ntk](/thread/post/13474224#post13474224 "View Quoted Post")
> 
> Disliked
> 
> {quote} Got a warning from broker "account due to hyper activity disabled, when use this EA, re check code"
> 
> Ignored

Never happend to me...could happen if you set the step too low, like "1".  
You can try this version with BE (set it outside the TP range to deactivate). Don't set the step very low though.  
  

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [INSTANT-BE-TRAIL-STEP.ex4](/attachment/file/3902297?d=1617085495) 124 KB | 482 downloads 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#119](/thread/post/13476463#post13476463 "Post Permalink")

  * Mar 31, 2021 8:03pm  Mar 31, 2021 8:03pm 

  * [ ntk](ntk)

  * Joined Dec 2018 | Status: Trader | [1,263 Posts](/search?do=process&provider=Member&searchuser=747159)

> [Quoting Go5](/thread/post/13474315#post13474315 "View Quoted Post")
> 
> Disliked
> 
> {quote} Never happend to me...could happen if you set the step too low, like "1". You can try this version with BE (set it outside the TP range to deactivate). Don't set the step very low though. {file}
> 
> Ignored

i use default setting  
TSL 100  
step 50  
TP 100  
it continuously sends order modify and broker warns to deactivate account. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#120](/thread/post/13477042#post13477042 "Post Permalink")

  * Apr 1, 2021 1:32am  Apr 1, 2021 1:32am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar375174_1.gif) Go5](go5)

  * Joined Jun 2014 | Status: Invisible | [1,437 Posts](/search?do=process&provider=Member&searchuser=375174) | Online Now 

> [Quoting ntk](/thread/post/13476463#post13476463 "View Quoted Post")
> 
> Disliked
> 
> {quote} i use default setting TSL 100 step 50 TP 100 it continuously sends order modify and broker warns to deactivate account.
> 
> Ignored

Found the problem, should be fixed now...

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [INSTANT-TRAIL-STEP-v1.1.ex4](/attachment/file/3903698?d=1617208333) 122 KB | 503 downloads 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * LazyHedging Trading Ideas
  *   * [ **Reply to Thread** ](/thread/1058948-lazyhedging-trading-ideas/reply#reply)

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

[EurCad Analysis and Trading Ideas](/thread/360980-eurcad-analysis-and-trading-ideas "Hello my friends. 
 
As of lately I have had remarkable success in trading EurCad and after hearing other traders ideas I decided that we...") 594 replies

[FSP Trading Journal and Trend Ideas](/thread/427493-fsp-trading-journal-and-trend-ideas "hello  
I am trying to post some of my trade Ideas here. 
there will be trend following and counter trend trades. 
I will post image rather...") 16 replies

[Forex trading platform that doesn't take your ideas](/thread/311080-forex-trading-platform-that-doesnt-take-your-ideas "Ninja trader, Metatrader, Tradestation all can copy the EA and indicators straight out of your PC. 
 
How do we go about developing a...") 11 replies

[Program Your Trading Ideas without being a programmer](/thread/225629-program-your-trading-ideas-without-being-a-programmer "I have to admit, I have a lot of trading ideas, but no programming skills. I hate paying a programmer to take 3 days to write an EA for me,...") 4 replies

[Exchanging trading ideas](/thread/136764-exchanging-trading-ideas "I'm opening this thread as a substitute for live chat like msn etc to exchange trading ideas and to filter of some posts at Igrok's thread,...") 37 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/1058948-lazyhedging-trading-ideas/reply#reply)
  * Subscribe
  * [271](javascript:void\(0\);)

Attachments: LazyHedging Trading Ideas

Tags: LazyHedging Trading Ideas

#  [](/thread/1058948-lazyhedging-trading-ideas)LazyHedging Trading Ideas 

  * 

  * [#121](/thread/post/13477459#post13477459 "Post Permalink")

  * Apr 1, 2021 6:51am  Apr 1, 2021 6:51am 

  * [ ntk](ntk)

  * Joined Dec 2018 | Status: Trader | [1,263 Posts](/search?do=process&provider=Member&searchuser=747159)

> [Quoting Go5](/thread/post/13477042#post13477042 "View Quoted Post")
> 
> Disliked
> 
> {quote} Found the problem, should be fixed now...{file}
> 
> Ignored

it seems to work now. thanks? what was the issue? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#122](/thread/post/13478002#post13478002 "Post Permalink")

  * Apr 1, 2021 5:01pm  Apr 1, 2021 5:01pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar375174_1.gif) Go5](go5)

  * Joined Jun 2014 | Status: Invisible | [1,437 Posts](/search?do=process&provider=Member&searchuser=375174) | Online Now 

> [Quoting ntk](/thread/post/13477459#post13477459 "View Quoted Post")
> 
> Disliked
> 
> {quote} it seems to work now. thanks? what was the issue?
> 
> Ignored

The "step" input wasn't linked to any of the relevant code.... 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#123](/thread/post/13478710#post13478710 "Post Permalink")

  * Apr 2, 2021 12:53am  Apr 2, 2021 12:53am 

  * [ Theblessed](theblessed)

  * | Joined Apr 2021  | Status: Trader | [1 Post](/search?do=process&provider=Member&searchuser=1086773)

Hello SM, that so much for the trading system. Please permit me to ask you an ignoramus question. I tried installing this system but couldn't succeed. I did file--MQL4--Indicators. It did not show in the indicator file. Please SM, what do I do to install the LazyHedging Trading System. Thanks for your assistance. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#124](/thread/post/13479545#post13479545 "Post Permalink")

  * Apr 2, 2021 7:40pm  Apr 2, 2021 7:40pm 

  * [ ntk](ntk)

  * Joined Dec 2018 | Status: Trader | [1,263 Posts](/search?do=process&provider=Member&searchuser=747159)

> [Quoting Theblessed](/thread/post/13478710#post13478710 "View Quoted Post")
> 
> Disliked
> 
> Hello SM, that so much for the trading system. Please permit me to ask you an ignoramus question. I tried installing this system but couldn't succeed. I did file--MQL4--Indicators. It did not show in the indicator file. Please SM, what do I do to install the LazyHedging Trading System. Thanks for your assistance.
> 
> Ignored

if you have saved the files in MQL4/indicators, you have to refresh the navigator, or just restart your MT4 then you will file them in the list, and you can attach them to your chart 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#125](/thread/post/13479553#post13479553 "Post Permalink")

  * Apr 2, 2021 7:46pm  Apr 2, 2021 7:46pm 

  * [ ntk](ntk)

  * Joined Dec 2018 | Status: Trader | [1,263 Posts](/search?do=process&provider=Member&searchuser=747159)

> [Quoting Go5](/thread/post/13478002#post13478002 "View Quoted Post")
> 
> Disliked
> 
> {quote} The "step" input wasn't linked to any of the relevant code....
> 
> Ignored

trailing-stop 100  
trailing step 50  
takeprofit 100  
  
with this setting does it means EA will start trailing, when user is in profit of 100 pips, EA will remove the TP and starts trailing the SL at/from 50 pips, I am not clear as what is with the last setting could you explain pls.  
  
Could you also release the modified source svp, thanks 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#126](/thread/post/13481669#post13481669 "Post Permalink")

  * Apr 5, 2021 6:32pm  Apr 5, 2021 6:32pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar375174_1.gif) Go5](go5)

  * Joined Jun 2014 | Status: Invisible | [1,437 Posts](/search?do=process&provider=Member&searchuser=375174) | Online Now 

> [Quoting ntk](/thread/post/13479553#post13479553 "View Quoted Post")
> 
> Disliked
> 
> {quote} trailing-stop 100 trailing step 50 takeprofit 100 with this setting does it means EA will start trailing, when user is in profit of 100 pips, EA will remove the TP and starts trailing the SL at/from 50 pips, I am not clear as what is with the last setting could you explain pls. Could you also release the modified source svp, thanks
> 
> Ignored

This is really basic stuff and I don't want to clutter this thread; please experiment with all settings and any doubt will vanish...  
The source is loaded with auto- generated crap and not useful to anyone. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#127](/thread/post/13482535#post13482535 "Post Permalink")

  * Apr 6, 2021 6:58am  Apr 6, 2021 6:58am 

  * [ ntk](ntk)

  * Joined Dec 2018 | Status: Trader | [1,263 Posts](/search?do=process&provider=Member&searchuser=747159)

> [Quoting Go5](/thread/post/13481669#post13481669 "View Quoted Post")
> 
> Disliked
> 
> {quote} This is really basic stuff and I don't want to clutter this thread; please experiment with all settings and any doubt will vanish... The source is loaded with auto- generated crap and not useful to anyone.
> 
> Ignored

it is alright. Thank you again. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#128](/thread/post/13683208#post13683208 "Post Permalink")

  * Aug 27, 2021 1:39am  Aug 27, 2021 1:39am 

  * [ viet360](viet360)

  * | Joined Aug 2021  | Status: Trader | [2 Posts](/search?do=process&provider=Member&searchuser=1211798)

hello SwingMan, I use your indicator smLazyHedging TrendChannel_v1.5.1.ex4... the indicator is very good, the problem is that when I save it as a template, when I reopen the template, the colors are not seamless, you can you tell me how to fix it...thankyou 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot 2021-08-26 152033.png
Size: 51 KB](/attachment/image/4022655/thumbnail?d=1629995725)](/attachment/image/4022655?d=1629995725)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#129](/thread/post/13683386#post13683386 "Post Permalink")

  * Aug 27, 2021 4:26am  Aug 27, 2021 4:26am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting viet360](/thread/post/13683208#post13683208 "View Quoted Post")
> 
> Disliked
> 
> hello SwingMan, I use your indicator smLazyHedging TrendChannel_v1.5.1.ex4... the indicator is very good, the problem is that when I save it as a template, when I reopen the template, the colors are not seamless, you can you tell me how to fix it...thankyou
> 
> Ignored

Maybe it has to do with MT4 functionality.  
  
If one load the template in a chart and the colors are not correct, then one should change the time frame and then go back to the old one. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#130](/thread/post/13686562#post13686562 "Post Permalink")

  * Aug 30, 2021 5:37pm  Aug 30, 2021 5:37pm 

  * [ viet360](viet360)

  * | Joined Aug 2021  | Status: Trader | [2 Posts](/search?do=process&provider=Member&searchuser=1211798)

hi SwingMan, i have an indicator...i don't know how to show an alert when it changes color from red to green or green to red...can you help me...thank you 

Attached File(s)

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [precision trend histo 22.mq4](/attachment/file/4024609?d=1630312642) 6 KB | 260 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#131](/thread/post/13723875#post13723875 "Post Permalink")

  * Edited 11:52pm  Sep 28, 2021 8:30pm | Edited 11:52pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

Expert Advisor **smLazyHedging_v3.1**  
  
Here I am posting a first version of an EA with the "Hedging Sliding StopLoss".  
The entries are from the TrendChannel. However, the results are not so good in the tester 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: USDJPY.rH1.png
Size: 28 KB](/attachment/image/4046884/thumbnail?d=1632840766)](/attachment/image/4046884?d=1632840766)   

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [smLazyHedging EA_v3.1.ex4](/attachment/file/4046640?d=1632828510) 32 KB | 480 downloads 

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [smShow HistoryOrders.mq4](/attachment/file/4046649?d=1632828936) 7 KB | 423 downloads 

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#132](/thread/post/13723880#post13723880 "Post Permalink")

  * Sep 28, 2021 8:34pm  Sep 28, 2021 8:34pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

**Fractal Trading System**  
  
Some indicators.  
  
How to trade... everyone can have ideas.  
Maybe one can achieve good results with the "Hedging Sliding StopLoss". 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: FractalTrading.PNG
Size: 44 KB](/attachment/image/4046644/thumbnail?d=1632828875)](/attachment/image/4046644?d=1632828875)   

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [MTF_Fractal.ex4](/attachment/file/4046645?d=1632828876) 21 KB | 509 downloads 

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [smBodySwitchTrend_v2.ex4](/attachment/file/4046646?d=1632828876) 13 KB | 502 downloads 

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [smLazyHedging ChannelOsc_v1.5.ex4](/attachment/file/4046647?d=1632828877) 18 KB | 530 downloads 

[0 ](javascript:void\(0\);) [3 ](javascript:void\(0\);)

  * [#133](/thread/post/13725526#post13725526 "Post Permalink")

  * Sep 29, 2021 5:19pm  Sep 29, 2021 5:19pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

Nice crossing of the support zone. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: EURUSD-Fractals.PNG
Size: 27 KB](/attachment/image/4047525/thumbnail?d=1632903533)](/attachment/image/4047525?d=1632903533)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#134](/thread/post/13725720#post13725720 "Post Permalink")

  * Sep 29, 2021 7:28pm  Sep 29, 2021 7:28pm 

  * [ Night63](night63)

  * | Joined Sep 2020  | Status: Trader | [226 Posts](/search?do=process&provider=Member&searchuser=1003725) | Online Now 

> [Quoting SwingMan](/thread/post/13723875#post13723875 "View Quoted Post")
> 
> Disliked
> 
> Expert Advisor smLazyHedging_v3.1 Here I am posting a first version of an EA with the "Hedging Sliding StopLoss". The entries are from the TrendChannel. However, the results are not so good in the tester {file} {file} {image}
> 
> Ignored

Dear SwingMan  
What PAIR & TF for EA?? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#135](/thread/post/13725770#post13725770 "Post Permalink")

  * Sep 29, 2021 8:09pm  Sep 29, 2021 8:09pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting Night63](/thread/post/13725720#post13725720 "View Quoted Post")
> 
> Disliked
> 
> {quote} Dear SwingMan What PAIR & TF for EA??
> 
> Ignored

Every pair, H1.  
But is not finished. Only to see and understand the mechanismus. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#136](/thread/post/13725908#post13725908 "Post Permalink")

  * Sep 29, 2021 9:25pm  Sep 29, 2021 9:25pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1062490_1.gif) Zookeeper85](zookeeper85)

  * | Joined Feb 2021  | Status: Trader | [90 Posts](/search?do=process&provider=Member&searchuser=1062490)

> [Quoting SwingMan](/thread/post/13723880#post13723880 "View Quoted Post")
> 
> Disliked
> 
> Fractal Trading System Some indicators. How to trade... everyone can have ideas. Maybe one can achieve good results with the "Hedging Sliding StopLoss". {image} {file} {file} {file}
> 
> Ignored

I think it would make perfect sense to apply the Hedging Sliding StopLoss to the fractal strategy... the fractals on the daily chart are often points where the market either continues or reverses the trend ... With the Hedging Sliding StopLoss we would win in both cases.  
  
_**Example D1 (Picture 1)**_  
We use the BodySwitch-Indicator to determine the trend - so we know in which direction we want to open our first position.  
We are in a downtrend, we place a sell stop on the "support fractals" and wait until it is activated. The moment the sell stop is activated, we look at the ChannelOsc and use the channel width as Take Profit and StopLoss (you can try ATR (1x or 1,5) as well)  
  
**_Example H1/D1 (Picture 2)_**  
We use the BodySwitch-Indicator to determine the trend (D1).  
On our H1 chart we set the fractal indicator timeframe to D1 so that we can see the same fractals as on the daily chart.  
The only difference is that we are trading with the channel width of the H1 chart instead of the channel width of the D1 chart.  
  
of course there are many other ways... 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: InkedEURUSDDaily2_LI.jpg
Size: 271 KB](/attachment/image/4047724/thumbnail?d=1632918366)](/attachment/image/4047724?d=1632918366)   
[![Click to Enlarge

Name: EURUSDH1.png
Size: 24 KB](/attachment/image/4047725/thumbnail?d=1632918378)](/attachment/image/4047725?d=1632918378)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#137](/thread/post/13727504#post13727504 "Post Permalink")

  * Sep 30, 2021 6:49pm  Sep 30, 2021 6:49pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

Example of how the losses for trades are minimized (here for three trades).  
The small horizontal limits show where the initial losses would have occurred.  
NZDUSD  

Attached Image

![](/attachment/image/4048518?d=1632995109)

  
Or here the AUDJPY.  
The losses were minimized for the first two trades, but not for the third. 

Attached Image

![](/attachment/image/4048527?d=1632995932)

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#138](/thread/post/13727991#post13727991 "Post Permalink")

  * Sep 30, 2021 10:57pm  Sep 30, 2021 10:57pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1062490_1.gif) Zookeeper85](zookeeper85)

  * | Joined Feb 2021  | Status: Trader | [90 Posts](/search?do=process&provider=Member&searchuser=1062490)

_**Fractal - Channel Breakout (MTF)**_  
  
Idea1 (Picture 1):  
Trend (D1) = Bodyswitch  
Entry (H1) = Fractal Breakout  
  
Idea2 (Picture 2):  
Trend (D1) = Fractal Breakout (which ist sometimes very similar to ChannelOsc)  
Entry (H1) = Fractal Breakout  
  
_In the examples shown, I have set the option "Show all Breakouts true/false" to false... just that you get the main idea.. there are many other breaks in our favor_

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: fractal.PNG
Size: 160 KB](/attachment/image/4048763/thumbnail?d=1633010226)](/attachment/image/4048763?d=1633010226)   
[![Click to Enlarge

Name: option2.png
Size: 168 KB](/attachment/image/4048764/thumbnail?d=1633010230)](/attachment/image/4048764?d=1633010230)   

Attached File(s)

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [Fractal - channel breakout 1.01.mq4](/attachment/file/4048766?d=1633010267) 14 KB | 408 downloads 

[0 ](javascript:void\(0\);) [3 ](javascript:void\(0\);)

  * [#139](/thread/post/13734710#post13734710 "Post Permalink")

  * Edited 5:33pm  Oct 6, 2021 4:54pm | Edited 5:33pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1062490_1.gif) Zookeeper85](zookeeper85)

  * | Joined Feb 2021  | Status: Trader | [90 Posts](/search?do=process&provider=Member&searchuser=1062490)

Fractalbreak D1 on H1 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: eurusdtoday.png
Size: 20 KB](/attachment/image/4053091/thumbnail?d=1633506835)](/attachment/image/4053091?d=1633506835)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#140](/thread/post/13783501#post13783501 "Post Permalink")

  * Nov 12, 2021 8:18am  Nov 12, 2021 8:18am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

**The Fractal Kiss ...**  
  
A trading variant is following:  
  
\- Trend direction from D1  
\- On H1, if the direction is the same, wait until _two_ fractal lines meets a candle.  
  
Note:  
If a candle of the _opposite color_ appears in a D1 direction (e.g. long / red candle), one can also trade after a single fractal line meets a candle.  
  
It goes without saying that the sliding hedge compensates for any losses ...

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: Fractals-AUDUSD.PNG
Size: 37 KB](/attachment/image/4080912/thumbnail?d=1636672702)](/attachment/image/4080912?d=1636672702)   
[![Click to Enlarge

Name: Fractals-USDCAD-2.PNG
Size: 40 KB](/attachment/image/4080919/thumbnail?d=1636672955)](/attachment/image/4080919?d=1636672955)   

[0 ](javascript:void\(0\);) [3 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * LazyHedging Trading Ideas
  *   * [ **Reply to Thread** ](/thread/1058948-lazyhedging-trading-ideas/reply#reply)

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

[EurCad Analysis and Trading Ideas](/thread/360980-eurcad-analysis-and-trading-ideas "Hello my friends. 
 
As of lately I have had remarkable success in trading EurCad and after hearing other traders ideas I decided that we...") 594 replies

[FSP Trading Journal and Trend Ideas](/thread/427493-fsp-trading-journal-and-trend-ideas "hello  
I am trying to post some of my trade Ideas here. 
there will be trend following and counter trend trades. 
I will post image rather...") 16 replies

[Forex trading platform that doesn't take your ideas](/thread/311080-forex-trading-platform-that-doesnt-take-your-ideas "Ninja trader, Metatrader, Tradestation all can copy the EA and indicators straight out of your PC. 
 
How do we go about developing a...") 11 replies

[Program Your Trading Ideas without being a programmer](/thread/225629-program-your-trading-ideas-without-being-a-programmer "I have to admit, I have a lot of trading ideas, but no programming skills. I hate paying a programmer to take 3 days to write an EA for me,...") 4 replies

[Exchanging trading ideas](/thread/136764-exchanging-trading-ideas "I'm opening this thread as a substitute for live chat like msn etc to exchange trading ideas and to filter of some posts at Igrok's thread,...") 37 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/1058948-lazyhedging-trading-ideas/reply#reply)
  * Subscribe
  * [271](javascript:void\(0\);)

Attachments: LazyHedging Trading Ideas

Tags: LazyHedging Trading Ideas

#  [](/thread/1058948-lazyhedging-trading-ideas)LazyHedging Trading Ideas 

  * 

  * [#141](/thread/post/13783976#post13783976 "Post Permalink")

  * Nov 12, 2021 5:50pm  Nov 12, 2021 5:50pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar635587_11.gif) robots4me](robots4me)

  * Joined Dec 2017 | Status: Trader | [4,378 Posts](/search?do=process&provider=Member&searchuser=635587)

> [Quoting SwingMan](/thread/post/13723875#post13723875 "View Quoted Post")
> 
> Disliked
> 
> Expert Advisor smLazyHedging_v3.1 Here I am posting a first version of an EA with the "Hedging Sliding StopLoss". The entries are from the TrendChannel. However, the results are not so good in the tester {file} {file} {image}
> 
> Ignored

Hey @Swingman -- not too shabby... ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: stats-smLazyHedging_EA.png
Size: 85 KB](/attachment/image/4081171/thumbnail?d=1636706993)](/attachment/image/4081171?d=1636706993)   

  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: settings-smLazyHedging_EA.png
Size: 43 KB](/attachment/image/4081172/thumbnail?d=1636706994)](/attachment/image/4081172?d=1636706994)   

[2 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#142](/thread/post/13784051#post13784051 "Post Permalink")

  * Nov 12, 2021 6:34pm  Nov 12, 2021 6:34pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting robots4me](/thread/post/13783976#post13783976 "View Quoted Post")
> 
> Disliked
> 
> ...Hey @Swingman -- not too shabby... ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)
> 
> Ignored

OK, but the formula for calculating the lots is not correct and I was too lazy to correct it.  
  
In the meantime I follow the trading signals of the FractalKiss in several pairs every day, and I feel as happy as the princess who kissed the frog. Soon the prince will come for me too ... 

[0 ](javascript:void\(0\);) [3 ](javascript:void\(0\);)

  * [#143](/thread/post/13795542#post13795542 "Post Permalink")

  * Nov 21, 2021 2:00pm  Nov 21, 2021 2:00pm 

  * [ opita04](opita04)

  * | Joined Feb 2019  | Status: Trader | [24 Posts](/search?do=process&provider=Member&searchuser=765190)

> [Quoting SwingMan](/thread/post/13784051#post13784051 "View Quoted Post")
> 
> Disliked
> 
> {quote} OK, but the formula for calculating the lots is not correct and I was too lazy to correct it. In the meantime I follow the trading signals of the FractalKiss in several pairs every day, and I feel as happy as the princess who kissed the frog. Soon the prince will come for me too ...
> 
> Ignored

  
The EA is actually quite decent, with some fine-tuning and maybe a few manual interventions it could do really good.  
The biggest problem is the lot sizing is all over the place.  
Any chance of releasing it as an MQ4?  
  
  
Cheers,  
  
Opita 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#144](/thread/post/13832726#post13832726 "Post Permalink")

  * Dec 21, 2021 7:01pm  Dec 21, 2021 7:01pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar906852_5.gif) jjeswanth](jjeswanth)

  * | Joined Jan 2020  | Status: Trader | [7 Posts](/search?do=process&provider=Member&searchuser=906852)

Hi SwingMan Thankyou for the wonderfull work  
  
If you Don't Mind can i Get The Source of the smLazyHedging TrendOsc_v1.1 indicator   
  
Thank you  
  
Sorry for my bad English![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

Trade what's happening… Not what you think is gonna happen.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#145](/thread/post/13833423#post13833423 "Post Permalink")

  * Dec 22, 2021 1:55am  Dec 22, 2021 1:55am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting opita04](/thread/post/13795542#post13795542 "View Quoted Post")
> 
> Disliked
> 
> ...The EA is actually quite decent, with some fine-tuning and maybe a few manual interventions it could do really good. The biggest problem is the lot sizing is all over the place. Any chance of releasing it as an MQ4? Cheers, Opita
> 
> Ignored

Here the EA. 

Attached File(s)

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [smLazyHedging EA_v3.1.mq4](/attachment/file/4108090?d=1640105682) 49 KB | 606 downloads 

![File Type: mqh](https://assets.faireconomy.media/images/attach/mqh.gif) [smLazyHedging_Include_v3.0.mqh](/attachment/file/4108091?d=1640105688) 14 KB | 557 downloads 

[0 ](javascript:void\(0\);) [4 ](javascript:void\(0\);)

  * [#146](/thread/post/13833426#post13833426 "Post Permalink")

  * Dec 22, 2021 1:57am  Dec 22, 2021 1:57am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting jjeswanth](/thread/post/13832726#post13832726 "View Quoted Post")
> 
> Disliked
> 
> ... If you Don't Mind can i Get The Source of the smLazyHedging TrendOsc_v1.1 indicator
> 
> Ignored

Here the indicators for you. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: GBPUSD.rDaily.png
Size: 33 KB](/attachment/image/4108094/thumbnail?d=1640105767)](/attachment/image/4108094?d=1640105767)   

Attached File(s)

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [smLazyHedging TrendChannel_v2.1.mq4](/attachment/file/4108095?d=1640105777) 37 KB | 713 downloads 

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [smLazyHedging ChannelOsc_v1.5.mq4](/attachment/file/4108096?d=1640105791) 8 KB | 691 downloads 

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [smLazyHedging TrendOsc_v1.1.mq4](/attachment/file/4108097?d=1640105811) 8 KB | 686 downloads 

[0 ](javascript:void\(0\);) [10 ](javascript:void\(0\);)

  * [#147](/thread/post/13833438#post13833438 "Post Permalink")

  * Dec 22, 2021 2:11am  Dec 22, 2021 2:11am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar906852_5.gif) jjeswanth](jjeswanth)

  * | Joined Jan 2020  | Status: Trader | [7 Posts](/search?do=process&provider=Member&searchuser=906852)

> [Quoting SwingMan](/thread/post/13833426#post13833426 "View Quoted Post")
> 
> Disliked
> 
> {quote} Here the indicators for you. {image} {file} {file} {file}
> 
> Ignored

Thank You![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

Trade what's happening… Not what you think is gonna happen.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#148](/thread/post/13839088#post13839088 "Post Permalink")

  * Dec 29, 2021 10:42am  Dec 29, 2021 10:42am 

  * [ opita04](opita04)

  * | Joined Feb 2019  | Status: Trader | [24 Posts](/search?do=process&provider=Member&searchuser=765190)

Really appreciate it! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#149](/thread/post/13839150#post13839150 "Post Permalink")

  * Dec 29, 2021 1:03pm  Dec 29, 2021 1:03pm 

  * [ Sawaddee](sawaddee)

  * | Joined Jul 2015  | Status: Trader | [188 Posts](/search?do=process&provider=Member&searchuser=419326)

Hello SwingMan,  
For the indicator "smBodySwitchTrend", could it be possible to have info shown at the corner of the chart for the D1 direction? It just shows if the smBodySwitchTrend for D1 is UP or DOWN so when we switch to smaller TF we can still see the direction of the D1.  
  
Thanks. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#150](/thread/post/13839488#post13839488 "Post Permalink")

  * Dec 29, 2021 10:17pm  Dec 29, 2021 10:17pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting Sawaddee](/thread/post/13839150#post13839150 "View Quoted Post")
> 
> Disliked
> 
> Hello SwingMan, For the indicator "smBodySwitchTrend", could it be possible to have info shown at the corner of the chart for the D1 direction? It just shows if the smBodySwitchTrend for D1 is UP or DOWN so when we switch to smaller TF we can still see the direction of the D1. Thanks.
> 
> Ignored

I'll do that in the near future, when I have the time.  
Until then, you can study an idea with trading only on D1. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#151](/thread/post/13839493#post13839493 "Post Permalink")

  * Edited Dec 30, 2021 4:20pm  Dec 29, 2021 10:27pm | Edited Dec 30, 2021 4:20pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

Here I post a trading idea on D1, without much comment.  
One can easily see the entry and exit levels and change the factors for their values. The drawn levels are always valid for the next bar.  
At the moment the ATR is used as a reference, but slightly better values are calculated in the oscillator.  
I would now like to try to write an EA. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: smBodySwitch-D1.png
Size: 194 KB](/attachment/image/4111803/thumbnail?d=1640784394)](/attachment/image/4111803?d=1640784394)   

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [smBodySwitch ChannelOsc_v1.1.ex4](/attachment/file/4111805?d=1640784415) 23 KB | 456 downloads 

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [smBodySwitch Signals_v1.1.ex4](/attachment/file/4112264?d=1640848810) 17 KB | 399 downloads 

[0 ](javascript:void\(0\);) [7 ](javascript:void\(0\);)

  * [#152](/thread/post/13840266#post13840266 "Post Permalink")

  * Dec 30, 2021 4:24pm  Dec 30, 2021 4:24pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

In the previous #Post 151 I posted a small correction for the indicator **"smBodySwitch Signals_v1.1!"**  
If you have downloaded version 1.0, please replace it. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#153](/thread/post/13840406#post13840406 "Post Permalink")

  * Dec 30, 2021 7:30pm  Dec 30, 2021 7:30pm 

  * [ Night63](night63)

  * | Joined Sep 2020  | Status: Trader | [226 Posts](/search?do=process&provider=Member&searchuser=1003725) | Online Now 

I recommend OnePIN and PinTRADER from Jagzfx for your indicator.. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#154](/thread/post/13841799#post13841799 "Post Permalink")

  * Edited 5:58am  Jan 1, 2022 5:46am | Edited 5:58am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

New version **"smBodySwitch Signals_v2.0"**  
  
I wish all readers of this thread a successful year!  
If one have time, one can study a little the potential of the BodySwitch indicator ...  
  
The + and - arrows show the possible profits and losses, and a small statistic calculates possible trading results.  

Attached Image

![](/attachment/image/4113164?d=1640983225)

.  

Attached Image

![](/attachment/image/4113165?d=1640983226)

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [smBodySwitch Signals_v2.0.ex4](/attachment/file/4113166?d=1640983227) 40 KB | 418 downloads 

[0 ](javascript:void\(0\);) [8 ](javascript:void\(0\);)

  * [#155](/thread/post/13842059#post13842059 "Post Permalink")

  * Jan 2, 2022 12:20am  Jan 2, 2022 12:20am 

  * [ dr.butze](dr.butze)

  * | Joined Jun 2020  | Status: Trader | [165 Posts](/search?do=process&provider=Member&searchuser=965218)

> [Quoting SwingMan](/thread/post/13841799#post13841799 "View Quoted Post")
> 
> Disliked
> 
> New version "smBodySwitch Signals_v2.0" I wish all readers of this thread a successful year! If one have time, one can study a little the potential of the BodySwitch indicator ... The + and - arrows show the possible profits and losses, and a small statistic calculates possible trading results. {image}. {image} {file}
> 
> Ignored

Hello Swingman,   
thank you so much for sharing your ideas and work once again!!!  
I hope you had a good start into the new year. I wish you all the best and especially health.  
Could you please give a newbie like me info on the indicator?   
What do the green and pink dots, the green cross and the red bar stand for?  
Thank you very much.  
  
Greetings from Meenz to FFM 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#156](/thread/post/13842586#post13842586 "Post Permalink")

  * Edited 6:20am  Jan 3, 2022 5:59am | Edited 6:20am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

New version to test: **"smBodySwitch Signals_v2.1"**  
  
\- A little more informations.  
\- One can enter the lots for the Win/Loss calculation.  
\- One can enter the maximum spread (e.g. 20) if one shouldn't trade - the background will be gray. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: BodySwitch-01.01.2022.png
Size: 221 KB](/attachment/image/4113726/thumbnail?d=1641157138)](/attachment/image/4113726?d=1641157138)   

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [smBodySwitch Signals_v2.1.ex4](/attachment/file/4113727?d=1641157139) 47 KB | 402 downloads 

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#157](/thread/post/13843075#post13843075 "Post Permalink")

  * Jan 3, 2022 7:42pm  Jan 3, 2022 7:42pm 

  * [ cocowell](cocowell)

  * | Joined Oct 2018  | Status: Trader | [65 Posts](/search?do=process&provider=Member&searchuser=726975)

> [Quoting SwingMan](/thread/post/13842586#post13842586 "View Quoted Post")
> 
> Disliked
> 
> New version to test: "smBodySwitch Signals_v2.1" - A little more informations. - One can enter the lots for the Win/Loss calculation. - One can enter the maximum spread (e.g. 20) if one shouldn't trade - the background will be gray. {image} {file}
> 
> Ignored

Can you share a version that doesn't change the background color？ 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#158](/thread/post/13843139#post13843139 "Post Permalink")

  * Jan 3, 2022 8:58pm  Jan 3, 2022 8:58pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting cocowell](/thread/post/13843075#post13843075 "View Quoted Post")
> 
> Disliked
> 
> ... Can you share a version that doesn't change the background color？
> 
> Ignored

You can set the maximum Spread e.g. on 500. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#159](/thread/post/13843179#post13843179 "Post Permalink")

  * Jan 3, 2022 9:35pm  Jan 3, 2022 9:35pm 

  * [ cocowell](cocowell)

  * | Joined Oct 2018  | Status: Trader | [65 Posts](/search?do=process&provider=Member&searchuser=726975)

> [Quoting SwingMan](/thread/post/13843139#post13843139 "View Quoted Post")
> 
> Disliked
> 
> {quote} You can set the maximum Spread e.g. on 500.
> 
> Ignored

Still automatically change the chart background to white. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#160](/thread/post/13843299#post13843299 "Post Permalink")

  * Jan 3, 2022 10:53pm  Jan 3, 2022 10:53pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting cocowell](/thread/post/13843179#post13843179 "View Quoted Post")
> 
> Disliked
> 
> ...Still automatically change the chart background to white.
> 
> Ignored

OK.  
I'll put a switch in, that's not a problem.  
But what is the problem? I always believed that if my algorithms are correct, the colors are also correct ...  
Instead of analyzing the color of the background, one should analyze the background of the indicator, there are enough observations to make.  
I, too, when the indicator is running, make assessments of the functionality and prepare the changes for the next version.  
I suspect that all over a hundred downloaders have only collected the indicator for their indicator collection without using it. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * LazyHedging Trading Ideas
  *   * [ **Reply to Thread** ](/thread/1058948-lazyhedging-trading-ideas/reply#reply)

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

[EurCad Analysis and Trading Ideas](/thread/360980-eurcad-analysis-and-trading-ideas "Hello my friends. 
 
As of lately I have had remarkable success in trading EurCad and after hearing other traders ideas I decided that we...") 594 replies

[FSP Trading Journal and Trend Ideas](/thread/427493-fsp-trading-journal-and-trend-ideas "hello  
I am trying to post some of my trade Ideas here. 
there will be trend following and counter trend trades. 
I will post image rather...") 16 replies

[Forex trading platform that doesn't take your ideas](/thread/311080-forex-trading-platform-that-doesnt-take-your-ideas "Ninja trader, Metatrader, Tradestation all can copy the EA and indicators straight out of your PC. 
 
How do we go about developing a...") 11 replies

[Program Your Trading Ideas without being a programmer](/thread/225629-program-your-trading-ideas-without-being-a-programmer "I have to admit, I have a lot of trading ideas, but no programming skills. I hate paying a programmer to take 3 days to write an EA for me,...") 4 replies

[Exchanging trading ideas](/thread/136764-exchanging-trading-ideas "I'm opening this thread as a substitute for live chat like msn etc to exchange trading ideas and to filter of some posts at Igrok's thread,...") 37 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/1058948-lazyhedging-trading-ideas/reply#reply)
  * Subscribe
  * [271](javascript:void\(0\);)

Attachments: LazyHedging Trading Ideas

Tags: LazyHedging Trading Ideas

#  [](/thread/1058948-lazyhedging-trading-ideas)LazyHedging Trading Ideas 

  * 

  * [#161](/thread/post/13843880#post13843880 "Post Permalink")

  * Jan 4, 2022 4:20am  Jan 4, 2022 4:20am 

  * [ dr.butze](dr.butze)

  * | Joined Jun 2020  | Status: Trader | [165 Posts](/search?do=process&provider=Member&searchuser=965218)

> [Quoting SwingMan](/thread/post/13842586#post13842586 "View Quoted Post")
> 
> Disliked
> 
> New version to test: "smBodySwitch Signals_v2.1" - A little more informations. - One can enter the lots for the Win/Loss calculation. - One can enter the maximum spread (e.g. 20) if one shouldn't trade - the background will be gray. {image} {file}
> 
> Ignored

Could you please explain a little bit the signs (star, ,dots and bars) that the indicator gives? Many thanks 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#162](/thread/post/13845590#post13845590 "Post Permalink")

  * Jan 5, 2022 4:38am  Jan 5, 2022 4:38am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

Possible trading results for 04.01.2022 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: BodySwitch-04.01.2022.png
Size: 228 KB](/attachment/image/4115662/thumbnail?d=1641325110)](/attachment/image/4115662?d=1641325110)   

[0 ](javascript:void\(0\);) [3 ](javascript:void\(0\);)

  * [#163](/thread/post/13845913#post13845913 "Post Permalink")

  * Jan 5, 2022 3:22pm  Jan 5, 2022 3:22pm 

  * [ Sawaddee](sawaddee)

  * | Joined Jul 2015  | Status: Trader | [188 Posts](/search?do=process&provider=Member&searchuser=419326)

> [Quoting SwingMan](/thread/post/13845590#post13845590 "View Quoted Post")
> 
> Disliked
> 
> Possible trading results for 04.01.2022 {image}
> 
> Ignored

Would love to see the EA running on this signal and see its result. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#164](/thread/post/13846651#post13846651 "Post Permalink")

  * Edited 1:53am  Jan 6, 2022 1:22am | Edited 1:53am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting Sawaddee](/thread/post/13845913#post13845913 "View Quoted Post")
> 
> Disliked
> 
> ... Would love to see the EA running on this signal and see its result.
> 
> Ignored

Until an EA is developed, one should test with pending orders!  
  
Comparison with a grid strategie: here is a typical example of today's sliding hedge.  
  
\- Pair GBPNZD. (The background is gray because the spread is too big and one will not trade.)  
  
\- The grid has e.g. 227 points spacing.  
Entry (1.99179), Take Profit (1.99179) and lower grid (1.98952)  
  
\- If the price reaches (1.99116) falling from the high, one closes the order and one trades a sell.  
The result: instead of a loss of 227 pts when reaching the lower grid, one loses 63 pts, and one earns 227 pts with the hedge sell. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: GBPNZD.rDaily.PNG
Size: 28 KB](/attachment/image/4116300/thumbnail?d=1641399732)](/attachment/image/4116300?d=1641399732)   

[0 ](javascript:void\(0\);) [4 ](javascript:void\(0\);)

  * [#165](/thread/post/13847135#post13847135 "Post Permalink")

  * Jan 6, 2022 6:13am  Jan 6, 2022 6:13am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar472073_2.gif) ordosgoitia](ordosgoitia)

  * Joined Jun 2016 | Status: Trader | [268 Posts](/search?do=process&provider=Member&searchuser=472073)

> [Quoting SwingMan](/thread/post/13845590#post13845590 "View Quoted Post")
> 
> Disliked
> 
> Possible trading results for 04.01.2022 {image}
> 
> Ignored

Hi Swingman, thanks for your work  
  
can you explain a bit better how this indicator works??  
i mean, i see a purple dot, green dot, and a start 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#166](/thread/post/13847237#post13847237 "Post Permalink")

  * Jan 6, 2022 7:46am  Jan 6, 2022 7:46am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting ordosgoitia](/thread/post/13847135#post13847135 "View Quoted Post")
> 
> Disliked
> 
> ...Hi Swingman, thanks for your work can you explain a bit better how this indicator works?? i mean, i see a purple dot, green dot, and a start
> 
> Ignored

Oh no, again someone asks without examining the indicator. No problem. It is just a confirmation that all hundreds of downloaders have only downloaded it for their indicator collection. Because there is no interest and no one tests anything, I will not post an EA here either. If I see someone contributing, I'll send it later privately.  
In general, I do not give detailed explanations, and everyone should get by, if not one should leave indicators alone or trade without indicators.  
If I can invest many hours, one should also be able to study an indicator in half an hour.  
  
I just posted a picture 6 hours ago with a few explanations. All one have to do is start the indicator on a chart and try to understand what I've written. Ai, ai, ai ...  
  
\- The green / red circles are entry and take profit levels. You can read it when you move the mouse over it, or you can find the names and values in the "Data Window", then identify them in the chart.  
  
\- In Post #154 I wrote "The + and - arrows show the possible profits and losses". The star should be the plus sign and the line the minus sign, because I couldn't find anything else. Otherwise you can see with the naked eye whether after an entry at the value of the green circle, the red circle has been reached or not (+ and - signs). 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#167](/thread/post/13847273#post13847273 "Post Permalink")

  * Jan 6, 2022 8:38am  Jan 6, 2022 8:38am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar472073_2.gif) ordosgoitia](ordosgoitia)

  * Joined Jun 2016 | Status: Trader | [268 Posts](/search?do=process&provider=Member&searchuser=472073)

> [Quoting SwingMan](/thread/post/13847237#post13847237 "View Quoted Post")
> 
> Disliked
> 
> {quote} Oh no, again someone asks without examining the indicator. No problem. It is just a confirmation that all hundreds of downloaders have only downloaded it for their indicator collection. Because there is no interest and no one tests anything, I will not post an EA here either. If I see someone contributing, I'll send it later privately. In general, I do not give detailed explanations, and everyone should get by, if not one should leave indicators alone or trade without indicators. If I can invest many hours, one should also be able to study...
> 
> Ignored

Thanks. I am a Big follower of Your works   
I understand they red and green dot.  
But i ser You use yo hedge some trades. I thought this indicador shows that.  
GReAT WOrk again. I use this indicador to know they trend .. after that i put a simple martingale EA to Open just to they trend . Works great 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#168](/thread/post/13847404#post13847404 "Post Permalink")

  * Jan 6, 2022 12:25pm  Jan 6, 2022 12:25pm 

  * [ Sawaddee](sawaddee)

  * | Joined Jul 2015  | Status: Trader | [188 Posts](/search?do=process&provider=Member&searchuser=419326)

> [Quoting SwingMan](/thread/post/13846651#post13846651 "View Quoted Post")
> 
> Disliked
> 
> {quote} Until an EA is developed, one should test with pending orders! Comparison with a grid strategie: here is a typical example of today's sliding hedge. - Pair GBPNZD. (The background is gray because the spread is too big and one will not trade.) - The grid has e.g. 227 points spacing. Entry (1.99179), Take Profit (1.99179) and lower grid (1.98952) - If the price reaches (1.99116) falling from the high, one closes the order and one trades a sell. The result: instead of a loss of 227 pts when reaching the lower grid, one loses 63 pts, and one...
> 
> Ignored

For today 06 Jan, GBPNZD. As per my chart (GlobalPrime) Entry Buy = 1.99974, TP = 2.00216, SL = 1.99720  
  
If I want to apply the same hedging as per your post, how could this be possible? Entry - TP = 242 that means lower grid = 1.99974 - 0.00242 = 1.99732 <== this should be the TP for the Sell at 1.99720. Or do we have to go to another lower level?   
  
And yesterday on GBPNZD, a star should not be marked because SL was hit before the TP. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: 2022-01-06_10-19-08.jpg
Size: 197 KB](/attachment/image/4116771/thumbnail?d=1641439189)](/attachment/image/4116771?d=1641439189)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#169](/thread/post/13847441#post13847441 "Post Permalink")

  * Jan 6, 2022 1:43pm  Jan 6, 2022 1:43pm 

  * [ Sawaddee](sawaddee)

  * | Joined Jul 2015  | Status: Trader | [188 Posts](/search?do=process&provider=Member&searchuser=419326)

> [Quoting SwingMan](/thread/post/13846651#post13846651 "View Quoted Post")
> 
> Disliked
> 
> {quote} Until an EA is developed, one should test with pending orders! Comparison with a grid strategie: here is a typical example of today's sliding hedge. - Pair GBPNZD. (The background is gray because the spread is too big and one will not trade.) - The grid has e.g. 227 points spacing. Entry (1.99179), Take Profit (1.99179) and lower grid (1.98952) - If the price reaches (1.99116) falling from the high, one closes the order and one trades a sell. The result: instead of a loss of 227 pts when reaching the lower grid, one loses 63 pts, and one...
> 
> Ignored

Nice idea of hedging. But I wonder how the SL is calculated? For example with the NZDCAD chart for today, SELL entry = 0.86401, tp = 0.85934, and sl = 0.86553. Points to win = 107 while points to SL = 512. With this type of number, how do we plan for the sliding hedge? 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: 2022-01-06_11-29-23.jpg
Size: 174 KB](/attachment/image/4116807/thumbnail?d=1641443785)](/attachment/image/4116807?d=1641443785)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#170](/thread/post/13847655#post13847655 "Post Permalink")

  * Jan 6, 2022 5:31pm  Jan 6, 2022 5:31pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting Sawaddee](/thread/post/13847404#post13847404 "View Quoted Post")
> 
> Disliked
> 
> ...And yesterday on GBPNZD, a star should not be marked because SL was hit before the TP.
> 
> Ignored

You can be right!  
  
The Win/Loss arrows are drawn at the end of the day, and it is possible that the SL will be reached before the TP within the day.  
I can live with it and instead of a 70% hit rate in the statistics, the real rate is only 68% ...  
With the EA one will find out whether the trading idea works.  
  
Here are the "possible" profits until this morning. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: BodySwitch-06.01.2022-1.png
Size: 220 KB](/attachment/image/4116948/thumbnail?d=1641457914)](/attachment/image/4116948?d=1641457914)   

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#171](/thread/post/13847745#post13847745 "Post Permalink")

  * Edited 8:25pm  Jan 6, 2022 6:22pm | Edited 8:25pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting Sawaddee](/thread/post/13847404#post13847404 "View Quoted Post")
> 
> Disliked
> 
> ...For today 06 Jan, GBPNZD. As per my chart (GlobalPrime) Entry Buy = 1.99974, TP = 2.00216, SL = 1.99720 If I want to apply the same hedging as per your post, how could this be possible? Entry - TP = 242 that means lower grid = 1.99974 - 0.00242 = 1.99732 <== this should be the TP for the Sell at 1.99720. Or do we have to go to another lower level? And yesterday on GBPNZD, a star should not be marked because SL was hit before the TP.
> 
> Ignored

Forget the term "grid".  
Please read Post #164 again, where I wrote that you should NOT take the grid distance (PTW=PointsToWin) from the entry, but rather **SL=High-PointsToWin**(or **SL=Low+PointsToWin**)!  
So you have an advantage, and instead of 227 pts you only lose 63 pts and you switch to hedge trading (in the simplest case a martingale), where in this example you win straight away.  
  
The money management is optimized automatically!  
  
The lots multiplier for a classic grid, for 227 PTW pts Win/Loss is:  
M = (227 Loss + 227 Win) /227 PTW=2.00  
The lots multiplier for the sliding hedge, for 227 pts Win/Loss is:  
M = (63 Loss + 227 Win) /227 PTW=1.30 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#172](/thread/post/13847811#post13847811 "Post Permalink")

  * Jan 6, 2022 7:05pm  Jan 6, 2022 7:05pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

New indicator version **"smBodySwitch Signals_v2.2"**  
  
**Warning!**  
This version can only be downloaded by _@Sawaddee_ and _@ordosgoitia_ , who are using the old version and have posted something...  
  
I have made some corrections and some additional information is being written.  
\- The spread limit is now entered as a percentage of the value of the PTW (PointsToWin). If it's more than 25%, maybe one shouldn't make the trade.  
\- For the spread value I calculate an EMA of spread values for the last 40 ticks.  
  
A profit has just been made on AUDCAD: 

Attached Image

![](/attachment/image/4117003?d=1641463643)

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [smBodySwitch Signals_v2.2.ex4](/attachment/file/4116998?d=1641463436) 52 KB | 315 downloads 

[0 ](javascript:void\(0\);) [5 ](javascript:void\(0\);)

  * [#173](/thread/post/13847822#post13847822 "Post Permalink")

  * Jan 6, 2022 7:13pm  Jan 6, 2022 7:13pm 

  * [ Sawaddee](sawaddee)

  * | Joined Jul 2015  | Status: Trader | [188 Posts](/search?do=process&provider=Member&searchuser=419326)

> [Quoting SwingMan](/thread/post/13847811#post13847811 "View Quoted Post")
> 
> Disliked
> 
> New indicator version "smBodySwitch Signals_v2.2" Warning! This version can only be downloaded by @Sawaddee and @ordosgoitia, who are using the old version and have posted something... I have made some corrections and some additional information is being written. - The spread limit is now entered as a percentage of the value of the PTW (PointsToWin). If it's more than 25%, maybe one shouldn't make the trade. - For the spread value I calculate an EMA of spread values for the last 40 ticks. A profit has just been made on AUDCAD: {file} {image}
> 
> Ignored

AUDCAD. Mine is still in trading.  
  
Would it be possible to have a red dot as SL indication for every trade? 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 39 KB](/attachment/image/4117009/thumbnail?d=1641463979)](/attachment/image/4117009?d=1641463979)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#174](/thread/post/13847833#post13847833 "Post Permalink")

  * Jan 6, 2022 7:21pm  Jan 6, 2022 7:21pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting Sawaddee](/thread/post/13847822#post13847822 "View Quoted Post")
> 
> Disliked
> 
> ...AUDCAD. Mine is still in trading.
> 
> Ignored

Change the Broker! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#175](/thread/post/13847895#post13847895 "Post Permalink")

  * Edited 10:30pm  Jan 6, 2022 8:06pm | Edited 10:30pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting Sawaddee](/thread/post/13847822#post13847822 "View Quoted Post")
> 
> Disliked
> 
> ... Would it be possible to have a red dot as SL indication for every trade?
> 
> Ignored

Without much testing, here is the version **"smBodySwitch Signals_v2.3"** with a star for StopLoss on the current bar.  

Attached Image

![](/attachment/image/4117050?d=1641467142)

  
  
**Please download "Version 2.3.1" from Post #179**

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#176](/thread/post/13847911#post13847911 "Post Permalink")

  * Jan 6, 2022 8:18pm  Jan 6, 2022 8:18pm 

  * [ Sawaddee](sawaddee)

  * | Joined Jul 2015  | Status: Trader | [188 Posts](/search?do=process&provider=Member&searchuser=419326)

> [Quoting SwingMan](/thread/post/13847895#post13847895 "View Quoted Post")
> 
> Disliked
> 
> {quote} Without much testing, here is the version "smBodySwitch Signals_v2.3" with a star for StopLoss on the current bar. {image} {file}
> 
> Ignored

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 82 KB](/attachment/image/4117062/thumbnail?d=1641467880)](/attachment/image/4117062?d=1641467880)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#177](/thread/post/13847918#post13847918 "Post Permalink")

  * Jan 6, 2022 8:26pm  Jan 6, 2022 8:26pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

_@Sawaddee_ , please read Post #171 again, I think it's right.  
  
The star is on the current bar, to see/have the current High and Low 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#178](/thread/post/13847964#post13847964 "Post Permalink")

  * Jan 6, 2022 9:11pm  Jan 6, 2022 9:11pm 

  * [ Sawaddee](sawaddee)

  * | Joined Jul 2015  | Status: Trader | [188 Posts](/search?do=process&provider=Member&searchuser=419326)

> [Quoting SwingMan](/thread/post/13847918#post13847918 "View Quoted Post")
> 
> Disliked
> 
> @Sawaddee, please read Post #171 again, I think it's right. The star is on the current bar, to see/have the current High and Low
> 
> Ignored

I thought SL means the value showed in the box. 

Attached Image

![](/attachment/image/4117098?d=1641471080)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#179](/thread/post/13847991#post13847991 "Post Permalink")

  * Jan 6, 2022 9:32pm  Jan 6, 2022 9:32pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting Sawaddee](/thread/post/13847964#post13847964 "View Quoted Post")
> 
> Disliked
> 
> ...I thought SL means the value showed in the box.
> 
> Ignored

It would be nice if you and other members read what I have written more carefully. I wouldn't waste any additional time.  
Post #151 says:  

> Quote
> 
> Disliked
> 
> One can easily see the entry and exit levels and change the factors for their values.**The drawn levels are always valid for the next bar**.

If one trades today, one have drawn the signal levels on the previous bar (remains unchanged), and the SL on the current bar (changes during the day).  
Maybe you think it's better that the stars are also drawn on the previous bar?  
  
Here the version **"smBodySwitch Signals_v2.3.1"**  
  
Which is better, then I delete one of the versions? 

Attached Image

![](/attachment/image/4117129?d=1641472698)

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [smBodySwitch Signals_v2.3.1.ex4](/attachment/file/4117130?d=1641472710) 51 KB | 337 downloads 

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#180](/thread/post/13848031#post13848031 "Post Permalink")

  * Jan 6, 2022 10:03pm  Jan 6, 2022 10:03pm 

  * [ Sawaddee](sawaddee)

  * | Joined Jul 2015  | Status: Trader | [188 Posts](/search?do=process&provider=Member&searchuser=419326)

> [Quoting SwingMan](/thread/post/13847991#post13847991 "View Quoted Post")
> 
> Disliked
> 
> {quote} It would be nice if you and other members read what I have written more carefully. I wouldn't waste any additional time. Post #151 says: {quote} If one trades today, one have drawn the signal levels on the previous bar (remains unchanged), and the SL on the current bar (changes during the day). Maybe you think it's better that the stars are also drawn on the previous bar? Here the version "smBodySwitch Signals_v2.3.1" Which is better, then I delete one of the versions? {image} {file}
> 
> Ignored

**and the SL on the current bar (changes during the day)**  
  
Perhaps I don't understand the above sentence.   
  
I wanted to have the SL shown so that I can backtest day by day and see if SL or TP hit first. If SL was hit then how the sliding hedge would effect the result.   
  
But the SL (as red star) showed in the chart, some of them, confused me. For the Sell, SL should be above the entry point. I don't understand how can SL stay at the middle between the entry and TP.   
  
I tried my best but if the red star has something more than just SL then perhaps I had missed it.  
  
Feel free to reply at your convenience. I don't want to waste more of your time.  
  
PS. The red star needs to be the same or the next candle. It makes no difference for me.

Attached Image

![](/attachment/image/4117140?d=1641473997)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * LazyHedging Trading Ideas
  *   * [ **Reply to Thread** ](/thread/1058948-lazyhedging-trading-ideas/reply#reply)

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

[EurCad Analysis and Trading Ideas](/thread/360980-eurcad-analysis-and-trading-ideas "Hello my friends. 
 
As of lately I have had remarkable success in trading EurCad and after hearing other traders ideas I decided that we...") 594 replies

[FSP Trading Journal and Trend Ideas](/thread/427493-fsp-trading-journal-and-trend-ideas "hello  
I am trying to post some of my trade Ideas here. 
there will be trend following and counter trend trades. 
I will post image rather...") 16 replies

[Forex trading platform that doesn't take your ideas](/thread/311080-forex-trading-platform-that-doesnt-take-your-ideas "Ninja trader, Metatrader, Tradestation all can copy the EA and indicators straight out of your PC. 
 
How do we go about developing a...") 11 replies

[Program Your Trading Ideas without being a programmer](/thread/225629-program-your-trading-ideas-without-being-a-programmer "I have to admit, I have a lot of trading ideas, but no programming skills. I hate paying a programmer to take 3 days to write an EA for me,...") 4 replies

[Exchanging trading ideas](/thread/136764-exchanging-trading-ideas "I'm opening this thread as a substitute for live chat like msn etc to exchange trading ideas and to filter of some posts at Igrok's thread,...") 37 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/1058948-lazyhedging-trading-ideas/reply#reply)
  * Subscribe
  * [271](javascript:void\(0\);)

Attachments: LazyHedging Trading Ideas

Tags: LazyHedging Trading Ideas

#  [](/thread/1058948-lazyhedging-trading-ideas)LazyHedging Trading Ideas 

  * 

  * [#181](/thread/post/13848063#post13848063 "Post Permalink")

  * Jan 6, 2022 10:27pm  Jan 6, 2022 10:27pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting Sawaddee](/thread/post/13848031#post13848031 "View Quoted Post")
> 
> Disliked
> 
> ...and the SL on the current bar (changes during the day) Perhaps I don't understand the above sentence.
> 
> Ignored

Thanks for the message, that's how it is, unfortunately.  
  
Now you have to fight with my term "sliding stop", or more simply: trailing stop.  
  
For a long trade, e.g. for (distance = TP - Entry), the (StopLoss = High - distance) would have to be.  
That is why the position of the star is independent of TP and Entry. These are values "from yesterday" and the SL is "for today".  
  
Entry for today is (yesterday's body high + yesterday's ATR * Entry_Factor).  
Take Profit for today is (Entry + ATR * TP_SL_Factor)  
PointsToWin is (ATR * TP_SL_Factor)  
  
**So that the chart does not appear overloaded, we keep version 2.3.1.**

[0 ](javascript:void\(0\);) [4 ](javascript:void\(0\);)

  * [#182](/thread/post/13848456#post13848456 "Post Permalink")

  * Jan 7, 2022 2:03am  Jan 7, 2022 2:03am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

Possible trading results for 06.01.2022  
  
Don't forget that one has to subtract the spread value from the profit, because all trading values are calculated with bid prices. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: BodySwitch-06.01.2022.png
Size: 226 KB](/attachment/image/4117378/thumbnail?d=1641488596)](/attachment/image/4117378?d=1641488596)   

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#183](/thread/post/13848467#post13848467 "Post Permalink")

  * Edited 2:07pm  Jan 7, 2022 2:17am | Edited 2:07pm 

  * [ Night63](night63)

  * | Joined Sep 2020  | Status: Trader | [226 Posts](/search?do=process&provider=Member&searchuser=1003725) | Online Now 

Thank you for an interesting system. I completely understand and will test !!  
Today 7.1. after opening the D1 candle, I entered all the forex pairs according to yesterday's candle. we'll see .. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#184](/thread/post/13848890#post13848890 "Post Permalink")

  * Jan 7, 2022 2:16pm  Jan 7, 2022 2:16pm 

  * [ Sawaddee](sawaddee)

  * | Joined Jul 2015  | Status: Trader | [188 Posts](/search?do=process&provider=Member&searchuser=419326)

> [Quoting SwingMan](/thread/post/13848063#post13848063 "View Quoted Post")
> 
> Disliked
> 
> {quote} Thanks for the message, that's how it is, unfortunately. Now you have to fight with my term "sliding stop", or more simply: trailing stop. For a long trade, e.g. for (distance = TP - Entry), the (StopLoss = High - distance) would have to be. That is why the position of the star is independent of TP and Entry. These are values "from yesterday" and the SL is "for today". Entry for today is (yesterday's body high + yesterday's ATR * Entry_Factor). Take Profit for today is (Entry + ATR * TP_SL_Factor) PointsToWin is (ATR * TP_SL_Factor) So that...
> 
> Ignored

Thank you for your kind explanation. Now I fully understand all the calculations i.e. Entry, TP, and SL. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#185](/thread/post/13849021#post13849021 "Post Permalink")

  * Jan 7, 2022 5:22pm  Jan 7, 2022 5:22pm 

  * [ veslup](veslup)

  * | Joined Nov 2009  | Status: Trader | [141 Posts](/search?do=process&provider=Member&searchuser=124349)

Hi Swing Man,  
  
Happy New Year to you and all traders.  
I put on screen you last version. awaiting for triggering first trade.  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 270 KB](/attachment/image/4117827/thumbnail?d=1641543649)](/attachment/image/4117827?d=1641543649)   

  
  
This one will be much better and easily with EA. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#186](/thread/post/13849081#post13849081 "Post Permalink")

  * Jan 7, 2022 6:15pm  Jan 7, 2022 6:15pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting veslup](/thread/post/13849021#post13849021 "View Quoted Post")
> 
> Disliked
> 
> ...I put on screen you last version. awaiting for triggering first trade. This one will be much better and easily with EA.
> 
> Ignored

Nice that you test manually!  
  
Some pointers:  
  
\- Because the levels are calculated with bid prices, the average spread should be taken into account. This will also be done later in the EA.  
It means that  
\- for the Buy Order (Entry = Entry Value + Spread) and (Exit = TakeProfit).  
\- for the Sell Order (Entry = Entry Value) and (Exit = TakeProfit + Spread)  
If you think that it would be more helpful for manual trading to write in the panel the values calculated in this way, please let us know.  
  
\- For your orders you can also enter the TakeProfit value.  
\- One must manually track and change the trailing StopLoss.  
\- You can switch off the "Show OHLC" in the chart, it is clearer. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#187](/thread/post/13849275#post13849275 "Post Permalink")

  * Jan 7, 2022 9:14pm  Jan 7, 2022 9:14pm 

  * [ veslup](veslup)

  * | Joined Nov 2009  | Status: Trader | [141 Posts](/search?do=process&provider=Member&searchuser=124349)

> [Quoting SwingMan](/thread/post/13849081#post13849081 "View Quoted Post")
> 
> Disliked
> 
> {quote} Nice that you test manually! Some pointers: - Because the levels are calculated with bid prices, the average spread should be taken into account. This will also be done later in the EA. It means that - for the Buy Order (Entry = Entry Value + Spread) and (Exit = TakeProfit). - for the Sell Order (Entry = Entry Value) and (Exit = TakeProfit + Spread) If you think that it would be more helpful for manual trading to write in the panel the values calculated in this way, please let us know. - For your orders you can also enter the TakeProfit...
> 
> Ignored

Yes I think will be better to write in the panel to not need calculate all the time.  
Also my observation is that the targets and stops are very tight but maybe that is the strategy.  
This is one of trading.  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 112 KB](/attachment/image/4117972/thumbnail?d=1641557646)](/attachment/image/4117972?d=1641557646)   

  
  
most probably we have to choice pairs with tight [spreads](/brokers/spreads "View Live Spreads on the Broker Guide")

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#188](/thread/post/13849300#post13849300 "Post Permalink")

  * Jan 7, 2022 9:40pm  Jan 7, 2022 9:40pm 

  * [ Remuli](remuli)

  * | Joined May 2019  | Status: Trader | [18 Posts](/search?do=process&provider=Member&searchuser=809891)

Let's see how it goes... 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Sieppaa123.PNG
Size: 178 KB](/attachment/image/4117989/thumbnail?d=1641559141)](/attachment/image/4117989?d=1641559141)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#189](/thread/post/13849302#post13849302 "Post Permalink")

  * Jan 7, 2022 9:42pm  Jan 7, 2022 9:42pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting veslup](/thread/post/13849275#post13849275 "View Quoted Post")
> 
> Disliked
> 
> Yes I think will be better to write in the panel to not need calculate all the time. Also my observation is that the targets and stops are very tight but maybe that is the strategy. This is one of trading. Most probably we have to choice pairs with tight spreads
> 
> Ignored

Please replace the picture with a smaller section, because that way I can't check anything.  
  
\- For trading, the spread condition is a limit of 25% from PointsToWin, for example.  
Test with limit 10% and you will see that the background turns gray.  
  
\- One will see later if the TP and SL are too tight, when the hedging works to eliminate the losses. If so, one can trade e.g. with 10 lots and get rich quickly, no problem.  
The idea in the thread is hedging (lazy hedging), and not trend trading. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#190](/thread/post/13849375#post13849375 "Post Permalink")

  * Jan 7, 2022 10:27pm  Jan 7, 2022 10:27pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting Remuli](/thread/post/13849300#post13849300 "View Quoted Post")
> 
> Disliked
> 
> Let's see how it goes...
> 
> Ignored

Yes, interesting what you're doing, but the StopLoss is not quite right!  
  
The star (SL) moves when the High (or Low) changes to account for the sliding hedge.  
In your charts the SL would be too far ...  
  
I have now some time and post later a new version where the spread should be taken into account e.g. for buy orders.  
  
For manual orders I will calculate an SL (Initial Stop) from the entry. 

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#191](/thread/post/13849447#post13849447 "Post Permalink")

  * Jan 7, 2022 10:59pm  Jan 7, 2022 10:59pm 

  * [ Remuli](remuli)

  * | Joined May 2019  | Status: Trader | [18 Posts](/search?do=process&provider=Member&searchuser=809891)

Thank you. Gotta read this thread better 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#192](/thread/post/13849758#post13849758 "Post Permalink")

  * Jan 8, 2022 1:51am  Jan 8, 2022 1:51am 

  * [ veslup](veslup)

  * | Joined Nov 2009  | Status: Trader | [141 Posts](/search?do=process&provider=Member&searchuser=124349)

Some of the trade after hit the stop loss continue   
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 41 KB](/attachment/image/4118228/thumbnail?d=1641574078)](/attachment/image/4118228?d=1641574078)   

  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 65 KB](/attachment/image/4118232/thumbnail?d=1641574187)](/attachment/image/4118232?d=1641574187)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#193](/thread/post/13849858#post13849858 "Post Permalink")

  * Jan 8, 2022 3:04am  Jan 8, 2022 3:04am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting veslup](/thread/post/13849758#post13849758 "View Quoted Post")
> 
> Disliked
> 
> Some of the trade after hit the stop loss continue.
> 
> Ignored

It is certainly like that within the day.  
  
The indicator is intended for _hedge trading_ , not for _trend trading_ , and you have already noticed that the stop loss is quite tight.  
If one wants to trade manually, one should also set the stops differently.  
  
Trading the sliding hedge is extremely difficult and will be programmed with the EA at some point. I mean that the losses can be compensated quickly with the sliding hedge, and without a large increase in the lots.  
Of course one will be able to determine this with the EA, until then one can carefully trade manually. 

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#194](/thread/post/13849864#post13849864 "Post Permalink")

  * Jan 8, 2022 3:10am  Jan 8, 2022 3:10am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

An example from today.  
  
In AUDUSD the sliding stop was reached at (-71 points), then the price turned and (115 points) were gained. I couldn't follow this manually with several pairs, the EA should do that.  
  
Some values:  
  
SL = Low - 115 = 71298 - 115 = 71413  
  
Loss = Entry - Exit = 71342 - 71413 = -71 

Attached Image

![](/attachment/image/4118292?d=1641578994)

[0 ](javascript:void\(0\);) [3 ](javascript:void\(0\);)

  * [#195](/thread/post/13849957#post13849957 "Post Permalink")

  * Jan 8, 2022 4:56am  Jan 8, 2022 4:56am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

New indicator version **"smBodySwitch Signals_v2.4"**  
  
A few changes have been made in this version:  
  
\- An "Initial Stop" is written  
For manual trading it would be interesting:  
The star for the SL should initially be drawn for this value.  
When one reaches the entry, one should have an option for the star to stop for the IS or to move with the SL.  
Who has an opinion?  
  
\- For the option "Values_Type = ManualTrading_Values", the spread is taken into account when entering the order. An "M" will appear in the top left corner.  
  
\- The spread is not taken into account for the option "Values_Type = Calculated_Values". An "C" will appear in the top left corner.  
  
Everything relates to the values from the trading panel. The arrows in the chart are drawn with the calculated values. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: BodySwitch-07.01.2022.png
Size: 222 KB](/attachment/image/4118349/thumbnail?d=1641584728)](/attachment/image/4118349?d=1641584728)   

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [smBodySwitch Signals_v2.4.ex4](/attachment/file/4118351?d=1641585326) 56 KB | 369 downloads 

[0 ](javascript:void\(0\);) [5 ](javascript:void\(0\);)

  * [#196](/thread/post/13850313#post13850313 "Post Permalink")

  * Jan 9, 2022 1:26am  Jan 9, 2022 1:26am 

  * [ allan9](allan9)

  * | Joined Jan 2016  | Status: Trader | [16 Posts](/search?do=process&provider=Member&searchuser=441532)

Very interesting system and simple to follow, thank you. My preference would be for a trailing stop loss that can be monitored , manually if preferred. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#197](/thread/post/13850324#post13850324 "Post Permalink")

  * Jan 9, 2022 1:50am  Jan 9, 2022 1:50am 

  * [ allan9](allan9)

  * | Joined Jan 2016  | Status: Trader | [16 Posts](/search?do=process&provider=Member&searchuser=441532)

I have a3840 x 2160 screen which compresses the panel so it is unreadable. Would it be possible to add an option to alter spacing in the panel?, I appreciate that this will involve your valuable time. Regards. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#198](/thread/post/13850356#post13850356 "Post Permalink")

  * Jan 9, 2022 2:32am  Jan 9, 2022 2:32am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting allan9](/thread/post/13850324#post13850324 "View Quoted Post")
> 
> Disliked
> 
> I have a3840 x 2160 screen which compresses the panel so it is unreadable. Would it be possible to add an option to alter spacing in the panel?, I appreciate that this will involve your valuable time. Regards.
> 
> Ignored

Please post a chart excerpt with the panel. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#199](/thread/post/13850454#post13850454 "Post Permalink")

  * Jan 9, 2022 6:31am  Jan 9, 2022 6:31am 

  * [ allan9](allan9)

  * | Joined Jan 2016  | Status: Trader | [16 Posts](/search?do=process&provider=Member&searchuser=441532)

Screenshot 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 587 KB](/attachment/image/4118645/thumbnail?d=1641677427)](/attachment/image/4118645?d=1641677427)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#200](/thread/post/13850495#post13850495 "Post Permalink")

  * Jan 9, 2022 8:37am  Jan 9, 2022 8:37am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

New indicator version **"smBodySwitch Signals_v2.5"**  
  
\- "StopLoss_Type" parameter can be "Fixed_StopLoss" and "Trailing_StopLoss"  
  
\- Separate factors for "TakeProfit" and "StopLoss". Tried with 0.2 and 0.4 values.  
  
\- One can enter the width and height for the TradingPanel.  
The text is output with the internal function "Comment" and the font cannot be changed, but the line spacing can be doubled.  
  
Now at the weekend, one should start the indicator in the strategy tester and report any errors. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: EURUSD.rDaily.png
Size: 30 KB](/attachment/image/4118664/thumbnail?d=1641684766)](/attachment/image/4118664?d=1641684766)   

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [smBodySwitch Signals_v2.5.ex4](/attachment/file/4118665?d=1641684986) 60 KB | 347 downloads 

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * LazyHedging Trading Ideas
  *   * [ **Reply to Thread** ](/thread/1058948-lazyhedging-trading-ideas/reply#reply)

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

[EurCad Analysis and Trading Ideas](/thread/360980-eurcad-analysis-and-trading-ideas "Hello my friends. 
 
As of lately I have had remarkable success in trading EurCad and after hearing other traders ideas I decided that we...") 594 replies

[FSP Trading Journal and Trend Ideas](/thread/427493-fsp-trading-journal-and-trend-ideas "hello  
I am trying to post some of my trade Ideas here. 
there will be trend following and counter trend trades. 
I will post image rather...") 16 replies

[Forex trading platform that doesn't take your ideas](/thread/311080-forex-trading-platform-that-doesnt-take-your-ideas "Ninja trader, Metatrader, Tradestation all can copy the EA and indicators straight out of your PC. 
 
How do we go about developing a...") 11 replies

[Program Your Trading Ideas without being a programmer](/thread/225629-program-your-trading-ideas-without-being-a-programmer "I have to admit, I have a lot of trading ideas, but no programming skills. I hate paying a programmer to take 3 days to write an EA for me,...") 4 replies

[Exchanging trading ideas](/thread/136764-exchanging-trading-ideas "I'm opening this thread as a substitute for live chat like msn etc to exchange trading ideas and to filter of some posts at Igrok's thread,...") 37 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/1058948-lazyhedging-trading-ideas/reply#reply)
  * Subscribe
  * [271](javascript:void\(0\);)

Attachments: LazyHedging Trading Ideas

Tags: LazyHedging Trading Ideas

#  [](/thread/1058948-lazyhedging-trading-ideas)LazyHedging Trading Ideas 

  * 

  * [#201](/thread/post/13850611#post13850611 "Post Permalink")

  * Jan 9, 2022 5:57pm  Jan 9, 2022 5:57pm 

  * [ allan9](allan9)

  * | Joined Jan 2016  | Status: Trader | [16 Posts](/search?do=process&provider=Member&searchuser=441532)

Thank you, works perfectly with panel adjustment. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#202](/thread/post/13850775#post13850775 "Post Permalink")

  * Jan 9, 2022 11:35pm  Jan 9, 2022 11:35pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting allan9](/thread/post/13850611#post13850611 "View Quoted Post")
> 
> Disliked
> 
> Thank you, works perfectly with panel adjustment.
> 
> Ignored

That makes me happy!  
Please post a section of the upper left corner so I can see what it looks like. I'm not interested in the whole chart. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#203](/thread/post/13850800#post13850800 "Post Permalink")

  * Jan 10, 2022 12:25am  Jan 10, 2022 12:25am 

  * [ veslup](veslup)

  * | Joined Nov 2009  | Status: Trader | [141 Posts](/search?do=process&provider=Member&searchuser=124349)

Looks like much better.  
Lets see how will be tomorrow.  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 349 KB](/attachment/image/4118833/thumbnail?d=1641741785)](/attachment/image/4118833?d=1641741785)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#204](/thread/post/13850837#post13850837 "Post Permalink")

  * Jan 10, 2022 2:27am  Jan 10, 2022 2:27am 

  * [ veslup](veslup)

  * | Joined Nov 2009  | Status: Trader | [141 Posts](/search?do=process&provider=Member&searchuser=124349)

> [Quoting SwingMan](/thread/post/13850775#post13850775 "View Quoted Post")
> 
> Disliked
> 
> {quote} That makes me happy! Please post a section of the upper left corner so I can see what it looks like. I'm not interested in the whole chart.
> 
> Ignored

  

Attached Image

![](/attachment/image/4118862?d=1641749370)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#205](/thread/post/13850849#post13850849 "Post Permalink")

  * Jan 10, 2022 3:05am  Jan 10, 2022 3:05am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting veslup](/thread/post/13850837#post13850837 "View Quoted Post")
> 
> Disliked
> 
> {image}
> 
> Ignored

It's perfect, I'm happy! 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#206](/thread/post/13851449#post13851449 "Post Permalink")

  * Edited Jan 11, 2022 5:30pm  Jan 10, 2022 6:29pm | Edited Jan 11, 2022 5:30pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

New indicator version **"smBodySwitch Signals_v2.6.1"**  
  
**(See Post #218 / Download a fixed version in Post #219)**  
  
Money Management was added to the indicator.  
  
Because several changes had to be made, please test and report any discrepancies.  
Please test whether the trailing stop works properly.  
  
Here is a little example. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: EURGBP.rDaily.png
Size: 79 KB](/attachment/image/4119287/thumbnail?d=1641806747)](/attachment/image/4119287?d=1641806747)   

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#207](/thread/post/13851499#post13851499 "Post Permalink")

  * Jan 10, 2022 7:09pm  Jan 10, 2022 7:09pm 

  * [ veslup](veslup)

  * | Joined Nov 2009  | Status: Trader | [141 Posts](/search?do=process&provider=Member&searchuser=124349)

> [Quoting SwingMan](/thread/post/13850849#post13850849 "View Quoted Post")
> 
> Disliked
> 
> {quote} It's perfect, I'm happy!
> 
> Ignored

version 2.5 looking good. Tree targets hit.  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 285 KB](/attachment/image/4119324/thumbnail?d=1641809318)](/attachment/image/4119324?d=1641809318)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#208](/thread/post/13851509#post13851509 "Post Permalink")

  * Jan 10, 2022 7:18pm  Jan 10, 2022 7:18pm 

  * [ veslup](veslup)

  * | Joined Nov 2009  | Status: Trader | [141 Posts](/search?do=process&provider=Member&searchuser=124349)

> [Quoting SwingMan](/thread/post/13851449#post13851449 "View Quoted Post")
> 
> Disliked
> 
> New indicator version "smBodySwitch Signals_v2.6.1" Money Management was added to the indicator. Because several changes had to be made, please test and report any discrepancies. Please test whether the trailing stop works properly. Here is a little example. {image} {file}
> 
> Ignored

That is ver. 2.6.1 with trailing stop on.  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 265 KB](/attachment/image/4119333/thumbnail?d=1641809871)](/attachment/image/4119333?d=1641809871)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#209](/thread/post/13851514#post13851514 "Post Permalink")

  * Jan 10, 2022 7:22pm  Jan 10, 2022 7:22pm 

  * [ veslup](veslup)

  * | Joined Nov 2009  | Status: Trader | [141 Posts](/search?do=process&provider=Member&searchuser=124349)

GBPCHF already triggered v. 2.6.1  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 39 KB](/attachment/image/4119337/thumbnail?d=1641810117)](/attachment/image/4119337?d=1641810117)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#210](/thread/post/13852005#post13852005 "Post Permalink")

  * Jan 11, 2022 12:08am  Jan 11, 2022 12:08am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar472073_2.gif) ordosgoitia](ordosgoitia)

  * Joined Jun 2016 | Status: Trader | [268 Posts](/search?do=process&provider=Member&searchuser=472073)

I increase a bit the profit factor and stoploss,, some pairs tp and stop is to short,, like 3 pips.. so, i am aiming to 8 pips per trade,, so far is going good.. also works great on h4 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#211](/thread/post/13852142#post13852142 "Post Permalink")

  * Jan 11, 2022 1:02am  Jan 11, 2022 1:02am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting ordosgoitia](/thread/post/13852005#post13852005 "View Quoted Post")
> 
> Disliked
> 
> I increase a bit the profit factor and stoploss,, some pairs tp and stop is to short,, like 3 pips.. so, i am aiming to 8 pips per trade,, so far is going good.. also works great on h4
> 
> Ignored

Without charts I can't know what you're hiring ...  
Please post some because I wouldn't recommend H4, just when you need action.  
The system is intended for retirees like me. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#212](/thread/post/13852352#post13852352 "Post Permalink")

  * Edited 3:41am  Jan 11, 2022 3:25am | Edited 3:41am 

  * [ Remuli](remuli)

  * | Joined May 2019  | Status: Trader | [18 Posts](/search?do=process&provider=Member&searchuser=809891)

Trailing stop seems to work. So tomorrow only manually ( buy stop/sell stop) entry and TP.  
Or like veslup, that only Entry manually and TSL on. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#213](/thread/post/13852386#post13852386 "Post Permalink")

  * Jan 11, 2022 3:55am  Jan 11, 2022 3:55am 

  * [ veslup](veslup)

  * | Joined Nov 2009  | Status: Trader | [141 Posts](/search?do=process&provider=Member&searchuser=124349)

That is for today so far.   
8 - targets  
2 - stops  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 357 KB](/attachment/image/4119797/thumbnail?d=1641840937)](/attachment/image/4119797?d=1641840937)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#214](/thread/post/13852410#post13852410 "Post Permalink")

  * Jan 11, 2022 4:20am  Jan 11, 2022 4:20am 

  * [ Remuli](remuli)

  * | Joined May 2019  | Status: Trader | [18 Posts](/search?do=process&provider=Member&searchuser=809891)

Well done with entry alone and TSL. For example, that AUDCHF. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#215](/thread/post/13852587#post13852587 "Post Permalink")

  * Jan 11, 2022 10:41am  Jan 11, 2022 10:41am 

  * [ Remuli](remuli)

  * | Joined May 2019  | Status: Trader | [18 Posts](/search?do=process&provider=Member&searchuser=809891)

"The system is intended for retirees like me." as for me 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Sieppaa666.PNG
Size: 229 KB](/attachment/image/4119936/thumbnail?d=1641865288)](/attachment/image/4119936?d=1641865288)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#216](/thread/post/13852601#post13852601 "Post Permalink")

  * Jan 11, 2022 11:13am  Jan 11, 2022 11:13am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar541225_1.gif) 9money](9money)

  * | Joined Dec 2016  | Status: Trader | [59 Posts](/search?do=process&provider=Member&searchuser=541225)

> [Quoting SwingMan](/thread/post/13851449#post13851449 "View Quoted Post")
> 
> Disliked
> 
> New indicator version "smBodySwitch Signals_v2.6.1" Money Management was added to the indicator. Because several changes had to be made, please test and report any discrepancies. Please test whether the trailing stop works properly. Here is a little example. {image} {file}
> 
> Ignored

Thank for share bro. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#217](/thread/post/13852720#post13852720 "Post Permalink")

  * Jan 11, 2022 3:46pm  Jan 11, 2022 3:46pm 

  * [ Night63](night63)

  * | Joined Sep 2020  | Status: Trader | [226 Posts](/search?do=process&provider=Member&searchuser=1003725) | Online Now 

Please which EA can I conveniently place pending trades including SL ??  
  
For example, buy stop above the current price by 20 pips and SL minus 10 pips  
I place the display by clicking and then the mouse signs the position on the dot and cross 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#218](/thread/post/13852773#post13852773 "Post Permalink")

  * Edited 5:23pm  Jan 11, 2022 4:50pm | Edited 5:23pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting Remuli](/thread/post/13852587#post13852587 "View Quoted Post")
> 
> Disliked
> 
> ..."The system is intended for retirees like me." as for me
> 
> Ignored

**A note:**  
In your charts you can see that the number of lots is zero at the top right: (0.00 Lots).  
  
This is a small problem in the program and I will try to fix it in the next version.  
This happens when Metatrader is started. My current solution is to restart the indicator in all charts, then the calculated number of Lots appears. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#219](/thread/post/13852818#post13852818 "Post Permalink")

  * Edited 9:29pm  Jan 11, 2022 5:26pm | Edited 9:29pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

Fixed version **"smBodySwitch Signals_v2.6.1"**  
  
I found a quick fix.  
  
Please replace the old file with the new one in the indicator folder, and restart the platform.  
For safety, it also saves the old file ...  
  
(See Post#222)

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#220](/thread/post/13852890#post13852890 "Post Permalink")

  * Edited 9:30pm  Jan 11, 2022 6:43pm | Edited 9:30pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

New fixed version **"smBodySwitch Signals_v2.6.1"**  
  
The writing of the losses in the lower right corner was wrong.  
  
Please replace the old file with the new one in the indicator folder, and restart the platform.  
  
(See Post#222)

Attached Image

![](/attachment/image/4120137?d=1641894130)

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * LazyHedging Trading Ideas
  *   * [ **Reply to Thread** ](/thread/1058948-lazyhedging-trading-ideas/reply#reply)

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

[EurCad Analysis and Trading Ideas](/thread/360980-eurcad-analysis-and-trading-ideas "Hello my friends. 
 
As of lately I have had remarkable success in trading EurCad and after hearing other traders ideas I decided that we...") 594 replies

[FSP Trading Journal and Trend Ideas](/thread/427493-fsp-trading-journal-and-trend-ideas "hello  
I am trying to post some of my trade Ideas here. 
there will be trend following and counter trend trades. 
I will post image rather...") 16 replies

[Forex trading platform that doesn't take your ideas](/thread/311080-forex-trading-platform-that-doesnt-take-your-ideas "Ninja trader, Metatrader, Tradestation all can copy the EA and indicators straight out of your PC. 
 
How do we go about developing a...") 11 replies

[Program Your Trading Ideas without being a programmer](/thread/225629-program-your-trading-ideas-without-being-a-programmer "I have to admit, I have a lot of trading ideas, but no programming skills. I hate paying a programmer to take 3 days to write an EA for me,...") 4 replies

[Exchanging trading ideas](/thread/136764-exchanging-trading-ideas "I'm opening this thread as a substitute for live chat like msn etc to exchange trading ideas and to filter of some posts at Igrok's thread,...") 37 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/1058948-lazyhedging-trading-ideas/reply#reply)
  * Subscribe
  * [271](javascript:void\(0\);)

Attachments: LazyHedging Trading Ideas

Tags: LazyHedging Trading Ideas

#  [](/thread/1058948-lazyhedging-trading-ideas)LazyHedging Trading Ideas 

  * 

  * [#221](/thread/post/13852939#post13852939 "Post Permalink")

  * Jan 11, 2022 7:12pm  Jan 11, 2022 7:12pm 

  * [ Remuli](remuli)

  * | Joined May 2019  | Status: Trader | [18 Posts](/search?do=process&provider=Member&searchuser=809891)

> [Quoting SwingMan](/thread/post/13852818#post13852818 "View Quoted Post")
> 
> Disliked
> 
> Fixed version "smBodySwitch Signals_v2.6.1" I found a quick fix. Please replace the old file with the new one in the indicator folder, and restart the platform. For safety, it also saves the old file ... (See next Post)
> 
> Ignored

I used the script to load the same template for all the charts, it might have affected that. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#222](/thread/post/13853089#post13853089 "Post Permalink")

  * Jan 11, 2022 9:29pm  Jan 11, 2022 9:29pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

New corrected version **"smBodySwitch Signals_v2.6.1"**  
  
I'm sorry, but only with live prices did I see that in the lower right corner, the results were still written incorrectly.  
  
Please replace the old file with the new one in the indicator folder. 

Attached Image

![](/attachment/image/4120222?d=1641904084)

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [smBodySwitch Signals_v2.6.1.ex4](/attachment/file/4120223?d=1641904092) 63 KB | 398 downloads 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#223](/thread/post/13853121#post13853121 "Post Permalink")

  * Jan 11, 2022 9:48pm  Jan 11, 2022 9:48pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

**Comment:**  
  
If one uses the sliding hedge, the loss is turned into profit!  
  
The trailing stop is used to sell at SL, then short with an increased lot number, and win. 

Attached Image

![](/attachment/image/4120235?d=1641905302)

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#224](/thread/post/13853138#post13853138 "Post Permalink")

  * Jan 11, 2022 10:03pm  Jan 11, 2022 10:03pm 

  * [ Sawaddee](sawaddee)

  * | Joined Jul 2015  | Status: Trader | [188 Posts](/search?do=process&provider=Member&searchuser=419326)

> [Quoting SwingMan](/thread/post/13853121#post13853121 "View Quoted Post")
> 
> Disliked
> 
> Comment: If one uses the sliding hedge, the loss is turned into profit! The trailing stop is used to sell at SL, then short with an increased lot number, and win. {image}
> 
> Ignored

Could it be possible that the first SL hit then the sliding hedge was opened but then the price revert again? Does the sliding hedge have sl? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#225](/thread/post/13853228#post13853228 "Post Permalink")

  * Jan 11, 2022 10:54pm  Jan 11, 2022 10:54pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting Sawaddee](/thread/post/13853138#post13853138 "View Quoted Post")
> 
> Disliked
> 
> Could it be possible that the first SL hit then the sliding hedge was opened but then the price revert again? Does the sliding hedge have sl?
> 
> Ignored

One repeats everything, level by level.  
Is a sort grid/martingale trading, with sliding grids and dynamic martingales... Maybe is functioning.  
  
Please read _Note #4_ in the first post and try to understand the table in _Post #33_. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#226](/thread/post/13853596#post13853596 "Post Permalink")

  * Jan 12, 2022 2:09am  Jan 12, 2022 2:09am 

  * [ gerval](gerval)

  * | Joined May 2020  | Status: Trader | [243 Posts](/search?do=process&provider=Member&searchuser=958353)

A pleasure to follow you again on the Swingman thread, undoubtedly the best martingale and trailing stop master.  
  
Reading the last messages to understand the operation and test it. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#227](/thread/post/13853651#post13853651 "Post Permalink")

  * Jan 12, 2022 2:44am  Jan 12, 2022 2:44am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting gerval](/thread/post/13853596#post13853596 "View Quoted Post")
> 
> Disliked
> 
> ...Reading the last messages to understand the operation and test it.
> 
> Ignored

Hi _@gerval_ ,  
I am pleased to see that you are still interested in the idea.  
  
Maybe you can test the functionality of the indicator because it is the basis for the EA. It can also be easily used for manual trading.  
  
I believe that the individual functions are correct now and I can start writing the EA. 

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#228](/thread/post/13853788#post13853788 "Post Permalink")

  * Jan 12, 2022 5:25am  Jan 12, 2022 5:25am 

  * [ veslup](veslup)

  * | Joined Nov 2009  | Status: Trader | [141 Posts](/search?do=process&provider=Member&searchuser=124349)

Almost done for the day. Today I set withhold trailing stop. Not so bad.  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 376 KB](/attachment/image/4120640/thumbnail?d=1641932718)](/attachment/image/4120640?d=1641932718)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#229](/thread/post/13854090#post13854090 "Post Permalink")

  * Jan 12, 2022 3:14pm  Jan 12, 2022 3:14pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar836530_33.gif) josi](josi)

  * Joined Aug 2019 | Status: Trader | [730 Posts](/search?do=process&provider=Member&searchuser=836530)

mtf added by MrTools; in case you want to say: thank you 

Attached File(s)

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [!!!smLazyHedging TrendOsc_v1.1 (mtf).mq4](/attachment/file/4120888?d=1641968052) 11 KB | 277 downloads 

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#230](/thread/post/13854219#post13854219 "Post Permalink")

  * Jan 12, 2022 5:28pm  Jan 12, 2022 5:28pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting veslup](/thread/post/13853788#post13853788 "View Quoted Post")
> 
> Disliked
> 
> Almost done for the day. Today I set withhold trailing stop. Not so bad.
> 
> Ignored

One can see that the GBPNZD (top right), is profitable after hedging. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#231](/thread/post/13854942#post13854942 "Post Permalink")

  * Edited 1:38am  Jan 13, 2022 1:16am | Edited 1:38am 

  * [ gerval](gerval)

  * | Joined May 2020  | Status: Trader | [243 Posts](/search?do=process&provider=Member&searchuser=958353)

I have been testing the indicator and the trialing stop system with an EA that does what the indicator says.  
  
I have had 6 trades today, 3 winners and 3 losers, but when using the Trailing stop, the losses have been much less than the winners. So great for the results.  
  
Without a doubt, a very good solution to keep track of operations with TS as I said a long time ago.  
  
But I wanted to show the loss operation to see how it can hurt us significantly when the price enters a range, in case of using reentries, and the manipulation makes the price move between our orders, causing us to buy at a resistance and sell at a support, which forces us to open many operations with a lot increase due to the martingale, although a little reduced due to the TS.  
  
In this photo we see how the operation was in favor at first and later it turned around and hit the SL, which had moved through the Trailing stop reducing the loss.  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 31 KB](/attachment/image/4121277/thumbnail?d=1641999503)](/attachment/image/4121277?d=1641999503)   

  
And seeing in detail what the price does in M5, you can see how the orders hit the SL on several occasions, when performing operations against each time the previous one closes us, maintaining the original distance of the first operation between the entry and the TP (8.8 pips). The TS is updated every time the price goes in favor of the entry 1 pip.  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 55 KB](/attachment/image/4121346/thumbnail?d=1642003279)](/attachment/image/4121346?d=1642003279)   

  
To avoid those ranges that can affect us so much in a given time, a solution would be to assume the loss and enter the candle the next day with the increase in lot, so the ranges would affect us less, since we enter at different times from the market, and on several different days.  
And thanks to the use of the TS as Swingman says, there would be days that the increase in the lot would be much lower than the classic martingale. 

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#232](/thread/post/13855161#post13855161 "Post Permalink")

  * Jan 13, 2022 3:27am  Jan 13, 2022 3:27am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting gerval](/thread/post/13854942#post13854942 "View Quoted Post")
> 
> Disliked
> 
> ...And seeing in detail what the price does in M5, you can see how the orders hit the SL on several occasions, when performing operations against each time the previous one closes us, maintaining the original distance of the first operation between the entry and the TP (8.8 pips). The TS is updated every time the price goes in favor of the entry 1 pip. {image} To avoid those ranges that can affect us so much in a given time, a solution would be to assume the loss and enter the candle the next day with the increase in lot, so the ranges would affect...
> 
> Ignored

Thank you for your evaluation, it is very reasonable!  
  
A little explanation why I took the factor 0.20 for the TP / SL:  
\- I followed the price movements on H1 for a long time.  
\- A day has 24 hours  
\- The volatility on H1 is approx. Root of 24 = 4.90 approx. 5  
\- 1/5 = 0.20  
  
One of the notices on H1 was that trading in 3 steps (entry-hedge-hedge) is pretty good. Then repeat.  
Just one step and increase later would be possible, but not fast enough to get rich.  
It would also be possible "as basket trading" to place the increased lot number on a different pair.  
  
One can check this with the smLazyHedging EA. For me, however, the entries were not profitable enough, which is why I presented here this daily strategy for retirees.  
Perhaps because of the favorable win/loss ratio, one can renounce on hedging and increase the risk. Let's see. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#233](/thread/post/13855310#post13855310 "Post Permalink")

  * Jan 13, 2022 6:09am  Jan 13, 2022 6:09am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

Here is also an attempt for NZDCAD to track the price movements within the day.  
  
Hopefully everything is correct, if not one should correct it. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: NZDCAD.rM5.png
Size: 43 KB](/attachment/image/4121541/thumbnail?d=1642021756)](/attachment/image/4121541?d=1642021756)   

[0 ](javascript:void\(0\);) [3 ](javascript:void\(0\);)

  * [#234](/thread/post/13855632#post13855632 "Post Permalink")

  * Jan 13, 2022 4:48pm  Jan 13, 2022 4:48pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar71675_5.gif) Alberto_Jazz](alberto_jazz)

  * Joined Jun 2008 | Status: Trader | [593 Posts](/search?do=process&provider=Member&searchuser=71675)

Hi Swingman, is there the possibility to increase the font in the trading panel?  
  
Thank you 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#235](/thread/post/13855684#post13855684 "Post Permalink")

  * Jan 13, 2022 5:26pm  Jan 13, 2022 5:26pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting Alberto_Jazz](/thread/post/13855632#post13855632 "View Quoted Post")
> 
> Disliked
> 
> Hi Swingman, is there the possibility to increase the font in the trading panel? Thank you
> 
> Ignored

Unfortunately the text is written with the internal function "Comment" and one cannot change anything.  
  
Of course, one can also do this by program, but it was quicker that way.  
But, as always, if I don't see anything you're testing or doing, I can't invest any additional time. Now I have to focus on the EA. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#236](/thread/post/13855695#post13855695 "Post Permalink")

  * Jan 13, 2022 5:31pm  Jan 13, 2022 5:31pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

New indicator version **"smBodySwitch Signals_v2.7"**  
  
Presumably this version will remain valid for a longer period of time.  
  
I made one final correction, although no one noted that sometimes when the spread condition was not met, the background in the chart remained gray. The checking has now been done in general, and when the spread is OK again, the background will turn white again.  
  
I have set the default setting for the display of the values to "Calculated_Values" in order to be able to follow the development of the prices more easily.  
Those who trade manually can take the spread into account when ordering, or switch to the setting "ManualTrading_Values". 

Attached Image

![](/attachment/image/4121798?d=1642062728)

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [smBodySwitch Signals_v2.7.ex4](/attachment/file/4121793?d=1642062535) 64 KB | 347 downloads 

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#237](/thread/post/13855819#post13855819 "Post Permalink")

  * Jan 13, 2022 7:13pm  Jan 13, 2022 7:13pm 

  * [ veslup](veslup)

  * | Joined Nov 2009  | Status: Trader | [141 Posts](/search?do=process&provider=Member&searchuser=124349)

V. 2.7 with trailing stop active.  
  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 363 KB](/attachment/image/4121864/thumbnail?d=1642068734)](/attachment/image/4121864?d=1642068734)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#238](/thread/post/13855933#post13855933 "Post Permalink")

  * Jan 13, 2022 9:10pm  Jan 13, 2022 9:10pm 

  * [ gerval](gerval)

  * | Joined May 2020  | Status: Trader | [243 Posts](/search?do=process&provider=Member&searchuser=958353)

Thanks Swingman for the indicator update.  
The photos that I put come from a daily chart, in which the operation is lost (half of the path of the SL is avoided thanks to the TS) and later it was a manual simulation of what it would have been in case of entering re-entries with a spread about 1 pip). But if you have fewer operations for your recovery, I am glad that fewer operations are accomplished. That is the ideal.  
The EA will be a good tool to work and look for good configurations. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#239](/thread/post/13856029#post13856029 "Post Permalink")

  * Jan 13, 2022 10:27pm  Jan 13, 2022 10:27pm 

  * [ Night63](night63)

  * | Joined Sep 2020  | Status: Trader | [226 Posts](/search?do=process&provider=Member&searchuser=1003725) | Online Now 

EA for simple wait orders  
[https://www.earnforex.com/metatrader...ick-trade-pro/](https://www.earnforex.com/metatrader-expert-advisors/one-click-trade-pro/)

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#240](/thread/post/13856120#post13856120 "Post Permalink")

  * Edited Jan 14, 2022 12:01am  Jan 13, 2022 11:31pm | Edited Jan 14, 2022 12:01am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar71675_5.gif) Alberto_Jazz](alberto_jazz)

  * Joined Jun 2008 | Status: Trader | [593 Posts](/search?do=process&provider=Member&searchuser=71675)

I'm testing and trying to understand how the system works.  
  
I'm using the trailing stop function but I seem that at moment the hedging function (reversal trade with lot size increase after a stop loss) is not implemented, is it correct?  
  
Have you got a 20 Pts loss on GBPUSD daily? May be I attached the indicator too late in the morning.  
  
Thank you 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * LazyHedging Trading Ideas
  *   * [ **Reply to Thread** ](/thread/1058948-lazyhedging-trading-ideas/reply#reply)

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

[EurCad Analysis and Trading Ideas](/thread/360980-eurcad-analysis-and-trading-ideas "Hello my friends. 
 
As of lately I have had remarkable success in trading EurCad and after hearing other traders ideas I decided that we...") 594 replies

[FSP Trading Journal and Trend Ideas](/thread/427493-fsp-trading-journal-and-trend-ideas "hello  
I am trying to post some of my trade Ideas here. 
there will be trend following and counter trend trades. 
I will post image rather...") 16 replies

[Forex trading platform that doesn't take your ideas](/thread/311080-forex-trading-platform-that-doesnt-take-your-ideas "Ninja trader, Metatrader, Tradestation all can copy the EA and indicators straight out of your PC. 
 
How do we go about developing a...") 11 replies

[Program Your Trading Ideas without being a programmer](/thread/225629-program-your-trading-ideas-without-being-a-programmer "I have to admit, I have a lot of trading ideas, but no programming skills. I hate paying a programmer to take 3 days to write an EA for me,...") 4 replies

[Exchanging trading ideas](/thread/136764-exchanging-trading-ideas "I'm opening this thread as a substitute for live chat like msn etc to exchange trading ideas and to filter of some posts at Igrok's thread,...") 37 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/1058948-lazyhedging-trading-ideas/reply#reply)
  * Subscribe
  * [271](javascript:void\(0\);)

Attachments: LazyHedging Trading Ideas

Tags: LazyHedging Trading Ideas

#  [](/thread/1058948-lazyhedging-trading-ideas)LazyHedging Trading Ideas 

  * 

  * [#241](/thread/post/13856201#post13856201 "Post Permalink")

  * Jan 14, 2022 12:22am  Jan 14, 2022 12:22am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting Alberto_Jazz](/thread/post/13856120#post13856120 "View Quoted Post")
> 
> Disliked
> 
> I'm testing and trying to understand how the system works. I'm using the trailing stop function but I seem that at moment the hedging function (reversal trade with lot size increase after a stop loss) is not implemented, is it correct? Have you got a 20 Pts loss on GBPUSD daily? May be I attached the indicator too late in the morning. Thank you
> 
> Ignored

\- The indicator cannot show reverse orders, it would be too much.  
  
\- For manual trading, the EA recommended by _@Night63_ seems to me to be very suitable.  
  
\- Very well done, but you can post charts, is easier to check the results.  
  
\- That’s what I said for today. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: BodySwitch-13.01.2022.PNG
Size: 77 KB](/attachment/image/4122059/thumbnail?d=1642087277)](/attachment/image/4122059?d=1642087277)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#242](/thread/post/13856208#post13856208 "Post Permalink")

  * Jan 14, 2022 12:26am  Jan 14, 2022 12:26am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting Night63](/thread/post/13856029#post13856029 "View Quoted Post")
> 
> Disliked
> 
> EA for simple wait orders [https://www.earnforex.com/metatrader...ick-trade-pro/](https://www.earnforex.com/metatrader-expert-advisors/one-click-trade-pro/)
> 
> Ignored

A very useful EA for manual trading! 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#243](/thread/post/13856356#post13856356 "Post Permalink")

  * Jan 14, 2022 2:03am  Jan 14, 2022 2:03am 

  * [ amrhamdy](amrhamdy)

  * | Joined Feb 2021  | Status: Trader | [72 Posts](/search?do=process&provider=Member&searchuser=1062746)

Hello SwingMan,  
Is this an expert or just an indicator .. because I saw you talking about manual trading so is there are any expert to be the automated 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#244](/thread/post/13856450#post13856450 "Post Permalink")

  * Jan 14, 2022 3:54am  Jan 14, 2022 3:54am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting amrhamdy](/thread/post/13856356#post13856356 "View Quoted Post")
> 
> Disliked
> 
> Hello SwingMan, Is this an expert or just an indicator .. because I saw you talking about manual trading so is there are any expert to be the automated
> 
> Ignored

\- I always write "New _indicator_ version smBodySwitch Signals_vxxx", so what I post IS an indicator and NOT an EA.  
  
\- When I talk about manual trading, it means that one runs the indicator and trades manual what one thinks is right.  
One can have one's own ideas, use other indicators, or like _@Naight63_ posted, based on the calculated values with the indicator give the order with a good EA. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#245](/thread/post/13856489#post13856489 "Post Permalink")

  * Jan 14, 2022 4:47am  Jan 14, 2022 4:47am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

In post #241 I posted the status at 17:14.  
There were 3 wins.  
  
Now at 21:37 we have 3 losses (EURUSD, AUDUSD, GBPUSD)  
I don't know what will happen next with EURUSD, but AUDUSD and GBPUSD were brought into profit with the sliding hedge.  
Result is 5 wins and 1 loss! 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: BodySwitch-20.38.PNG
Size: 33 KB](/attachment/image/4122225/thumbnail?d=1642103220)](/attachment/image/4122225?d=1642103220)   

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#246](/thread/post/13856630#post13856630 "Post Permalink")

  * Jan 14, 2022 8:11am  Jan 14, 2022 8:11am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting gerval](/thread/post/13855933#post13855933 "View Quoted Post")
> 
> Disliked
> 
> ... But if you have fewer operations for your recovery, I am glad that fewer operations are accomplished. That is the ideal. The EA will be a good tool to work and look for good configurations.
> 
> Ignored

Let's hope to be able to find a right variant for the EA.  
  
As you have already observed, sometimes there are pronounced sideways movements.  
For the AUDUSD where I wrote that the loss ends in a profit, 6 levels were necessary.  
  
For levels 2 to 4, however, the martingale is reduced by around 15%, and for levels 5 and 6 by around 80% and 70% compared to the classic martingale. Not bad either.  
  
There is still the variant that one continues as classic trend trading after a successful entry, as long as the trend line does not change its color. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: BodySwitch-2.PNG
Size: 39 KB](/attachment/image/4122300/thumbnail?d=1642115465)](/attachment/image/4122300?d=1642115465)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#247](/thread/post/13856641#post13856641 "Post Permalink")

  * Jan 14, 2022 8:34am  Jan 14, 2022 8:34am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

And now the same trade with the classic martingale.  
  
There are also 6 levels as in trading with the sliding hedge, but the factor 2 is no longer reduced, and the capital is more heavily used. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: BodySwitch-3.PNG
Size: 40 KB](/attachment/image/4122307/thumbnail?d=1642116879)](/attachment/image/4122307?d=1642116879)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#248](/thread/post/13856904#post13856904 "Post Permalink")

  * Jan 14, 2022 4:16pm  Jan 14, 2022 4:16pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar71675_5.gif) Alberto_Jazz](alberto_jazz)

  * Joined Jun 2008 | Status: Trader | [593 Posts](/search?do=process&provider=Member&searchuser=71675)

Sorry but i'm not able to take a better screenshot on my VPS.  
  
Anyway, everything is grey at the moment and I seem it's correct.  
  
Let see how this trading day will go!  
  
Thank you 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 139 KB](/attachment/image/4122513/thumbnail?d=1642144502)](/attachment/image/4122513?d=1642144502)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#249](/thread/post/13856941#post13856941 "Post Permalink")

  * Edited 9:04pm  Jan 14, 2022 4:47pm | Edited 9:04pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting Alberto_Jazz](/thread/post/13856904#post13856904 "View Quoted Post")
> 
> Disliked
> 
> ... Anyway, everything is grey at the moment and I seem it's correct. Let see how this trading day will go! Thank you
> 
> Ignored

Hi Alberto, please use the **version 2.7** [in **Post #236**](https://www.forexfactory.com/thread/post/13855695#post13855695)  
  
I wrote:  
  

> Quote
> 
> Disliked
> 
> New indicator version **"smBodySwitch Signals_v2.7"**  
>    
>  I made one final correction, although no one noted that sometimes when the spread condition was not met, the background in the chart remained gray. The checking has now been done in general, and when the spread is OK again, the background will turn white again.

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#250](/thread/post/13857191#post13857191 "Post Permalink")

  * Edited 8:28pm  Jan 14, 2022 8:16pm | Edited 8:28pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

For today a new version for the indicator **"smBodySwitch Signals_v2.8"**  
  
\- I got the impression that sometimes after reaching TP or SL, the indicator forgot that they were reached, so I improved that.  
  
\- For the current status when entry was reached and TP/SL not yet, I added the information of the percentage achieved.  
Sometimes one doesn't want to wait until the full 100% is reached. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: GBPAUD.rDaily.png
Size: 10 KB](/attachment/image/4122678/thumbnail?d=1642158530)](/attachment/image/4122678?d=1642158530)   

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [smBodySwitch Signals_v2.8.ex4](/attachment/file/4122688?d=1642159698) 65 KB | 487 downloads 

[0 ](javascript:void\(0\);) [6 ](javascript:void\(0\);)

  * [#251](/thread/post/13857344#post13857344 "Post Permalink")

  * Jan 14, 2022 10:38pm  Jan 14, 2022 10:38pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar71675_5.gif) Alberto_Jazz](alberto_jazz)

  * Joined Jun 2008 | Status: Trader | [593 Posts](/search?do=process&provider=Member&searchuser=71675)

Hi SM, if I use daily charts do I need to switch the Uppder Period parameter to Weekly?  
  
Thank you 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#252](/thread/post/13857386#post13857386 "Post Permalink")

  * Jan 14, 2022 10:54pm  Jan 14, 2022 10:54pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting Alberto_Jazz](/thread/post/13857344#post13857344 "View Quoted Post")
> 
> Disliked
> 
> Hi SM, if I use daily charts do I need to switch the Uppder Period parameter to Weekly? Thank you
> 
> Ignored

No.  
  
I tested on D1 and remain so.  
  
If you want, you can take the trend of W1 into account and trade on D1 if the trends match. It's actually quite good to do that. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#253](/thread/post/13857421#post13857421 "Post Permalink")

  * Jan 14, 2022 11:08pm  Jan 14, 2022 11:08pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar71675_5.gif) Alberto_Jazz](alberto_jazz)

  * Joined Jun 2008 | Status: Trader | [593 Posts](/search?do=process&provider=Member&searchuser=71675)

> [Quoting SwingMan](/thread/post/13857191#post13857191 "View Quoted Post")
> 
> Disliked
> 
> I added the information of the percentage achieved.  
>  Sometimes one doesn't want to wait until the full 100% is reached.
> 
> Ignored

If you plan to trade this system as a basket, one could like a done 4 the day when a certain % gain is reached on the account.  
  
Today I have a loss on GBPUSD but I suspect it could be an easy profit with sliding hedge with only one sell. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#254](/thread/post/13857576#post13857576 "Post Permalink")

  * Edited 3:51am  Jan 15, 2022 12:31am | Edited 3:51am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting Alberto_Jazz](/thread/post/13857421#post13857421 "View Quoted Post")
> 
> Disliked
> 
> If you plan to trade this system as a basket, one could like a done 4 the day when a certain % gain is reached on the account.  
>  **I don't recommend that.**  
>    
>  Today I have a loss on GBPUSD but I suspect it could be an easy profit with sliding hedge with only one sell.
> 
> Ignored

In my evaluation from today were in profit:  
USDJPY  
AUDJPY  
NZDJPY  
AUDCAD  
GBPAUD  
GBPNZD  
Two pairs that showed losses could be wins:  
EURNZD  
EUAUD  
  
You are right about GBPUSD, the displayed loss is quickly changed to profit.  
  
NOT BAD FOR TODAY. 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: GBPUSD.rDaily.png
Size: 11 KB](/attachment/image/4122936/thumbnail?d=1642174286)](/attachment/image/4122936?d=1642174286)   
[![Click to Enlarge

Name: GBPUSD.rM5.png
Size: 26 KB](/attachment/image/4122937/thumbnail?d=1642174294)](/attachment/image/4122937?d=1642174294)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#255](/thread/post/13857864#post13857864 "Post Permalink")

  * Jan 15, 2022 3:56am  Jan 15, 2022 3:56am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

Done for today.  
  
6 wins and 3 losers who became winners after the sliding hedge.  
  
SpotBrent closed at 27% profit.  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Results BodySwitch 14.01.22-20_44.png
Size: 180 KB](/attachment/image/4123103/thumbnail?d=1642186595)](/attachment/image/4123103?d=1642186595)   

  
  
I have no idea if the EA can bring the same results...  
Of course, only those members who have understood and tested the indicator can test the EA, so that they do not get rich too quickly. 

[0 ](javascript:void\(0\);) [3 ](javascript:void\(0\);)

  * [#256](/thread/post/13857907#post13857907 "Post Permalink")

  * Jan 15, 2022 4:48am  Jan 15, 2022 4:48am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar71675_5.gif) Alberto_Jazz](alberto_jazz)

  * Joined Jun 2008 | Status: Trader | [593 Posts](/search?do=process&provider=Member&searchuser=71675)

Let's suppose this situation:  
  
1st order BUY: stop loss  
2nd order SELL: stop loss  
3rd order BUY: still opended at daily close  
  
Do you close the order at daily closing, or do you leave the trade open in the new day?   
  
In this case do you accept another BUY if there is a trigger in the new day or do you wait the previous BUY to be closed? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#257](/thread/post/13857922#post13857922 "Post Permalink")

  * Jan 15, 2022 5:15am  Jan 15, 2022 5:15am 

  * [ Remuli](remuli)

  * | Joined May 2019  | Status: Trader | [18 Posts](/search?do=process&provider=Member&searchuser=809891)

OK. I do sliding hedge calculations in Excel according to post 222.  
And I drop the chart amount to a minimum. When old, can't stare at the screen all day. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#258](/thread/post/13857952#post13857952 "Post Permalink")

  * Jan 15, 2022 6:00am  Jan 15, 2022 6:00am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting Alberto_Jazz](/thread/post/13857907#post13857907 "View Quoted Post")
> 
> Disliked
> 
> Let's suppose this situation: 1st order BUY: stop loss 2nd order SELL: stop loss 3rd order BUY: still opended at daily close Do you close the order at daily closing, or do you leave the trade open in the new day? In this case do you accept another BUY if there is a trigger in the new day or do you wait the previous BUY to be closed?
> 
> Ignored

I'm sorry, but such scenarios have to be tested first, including parameters, etc.  
  
Follow some signals and you will see that sometimes it is advantageous to continue trading on the second day, sometimes to stop.  
Conclusions can only be made when the EA is finished, at some point... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#259](/thread/post/13857961#post13857961 "Post Permalink")

  * Jan 15, 2022 6:15am  Jan 15, 2022 6:15am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting Remuli](/thread/post/13857922#post13857922 "View Quoted Post")
> 
> Disliked
> 
> OK. I do sliding hedge calculations in Excel according to post 222. And I drop the chart amount to a minimum. When old, can't stare at the screen all day.
> 
> Ignored

I think you did a calculation like in [Post #33](https://www.forexfactory.com/thread/post/13407947#post13407947).  
Can you show me what it looks like? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#260](/thread/post/13858009#post13858009 "Post Permalink")

  * Jan 15, 2022 7:46am  Jan 15, 2022 7:46am 

  * [ Remuli](remuli)

  * | Joined May 2019  | Status: Trader | [18 Posts](/search?do=process&provider=Member&searchuser=809891)

This weekend I do Excel. Now there is another thing to do.  
Nothing to do with post 33. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * LazyHedging Trading Ideas
  *   * [ **Reply to Thread** ](/thread/1058948-lazyhedging-trading-ideas/reply#reply)

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

[EurCad Analysis and Trading Ideas](/thread/360980-eurcad-analysis-and-trading-ideas "Hello my friends. 
 
As of lately I have had remarkable success in trading EurCad and after hearing other traders ideas I decided that we...") 594 replies

[FSP Trading Journal and Trend Ideas](/thread/427493-fsp-trading-journal-and-trend-ideas "hello  
I am trying to post some of my trade Ideas here. 
there will be trend following and counter trend trades. 
I will post image rather...") 16 replies

[Forex trading platform that doesn't take your ideas](/thread/311080-forex-trading-platform-that-doesnt-take-your-ideas "Ninja trader, Metatrader, Tradestation all can copy the EA and indicators straight out of your PC. 
 
How do we go about developing a...") 11 replies

[Program Your Trading Ideas without being a programmer](/thread/225629-program-your-trading-ideas-without-being-a-programmer "I have to admit, I have a lot of trading ideas, but no programming skills. I hate paying a programmer to take 3 days to write an EA for me,...") 4 replies

[Exchanging trading ideas](/thread/136764-exchanging-trading-ideas "I'm opening this thread as a substitute for live chat like msn etc to exchange trading ideas and to filter of some posts at Igrok's thread,...") 37 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/1058948-lazyhedging-trading-ideas/reply#reply)
  * Subscribe
  * [271](javascript:void\(0\);)

Attachments: LazyHedging Trading Ideas

Tags: LazyHedging Trading Ideas

#  [](/thread/1058948-lazyhedging-trading-ideas)LazyHedging Trading Ideas 

  * 

  * [#261](/thread/post/13859670#post13859670 "Post Permalink")

  * Jan 17, 2022 9:46pm  Jan 17, 2022 9:46pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar71675_5.gif) Alberto_Jazz](alberto_jazz)

  * Joined Jun 2008 | Status: Trader | [593 Posts](/search?do=process&provider=Member&searchuser=71675)

Hi SM, my spead input is 25 (default) but my CADJPY graph is white, is it correct?  
  
Thank you. 

Attached Image

![](/attachment/image/4124130?d=1642423561)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#262](/thread/post/13859709#post13859709 "Post Permalink")

  * Jan 17, 2022 10:24pm  Jan 17, 2022 10:24pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting Alberto_Jazz](/thread/post/13859670#post13859670 "View Quoted Post")
> 
> Disliked
> 
> Hi SM, my spead input is 25 (default) but my CADJPY graph is white, is it correct? Thank you.
> 
> Ignored

The spread percentage (Spread/PointsToWin) is limited, not the spread, and you can see that in the TradingPanel.  
See Post #254 with version 2.8.  
  
Please post it. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#263](/thread/post/13859785#post13859785 "Post Permalink")

  * Jan 17, 2022 11:03pm  Jan 17, 2022 11:03pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar71675_5.gif) Alberto_Jazz](alberto_jazz)

  * Joined Jun 2008 | Status: Trader | [593 Posts](/search?do=process&provider=Member&searchuser=71675)

Ok thank you 

Attached Image

![](/attachment/image/4124192?d=1642428208)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#264](/thread/post/13861000#post13861000 "Post Permalink")

  * Edited 11:58pm  Jan 18, 2022 7:49pm | Edited 11:58pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

New indicator version **"smBodySwitch Signals_v2.9"**  
  
\- For a better overview (only for retirees), the trading panel now has different background colors for active long or short trades.  

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [smBodySwitch Signals_v2.9.ex4](/attachment/file/4124891?d=1642502916) 78 KB | 542 downloads 

  
  
An interesting day so far in the morning!  
  
3 winners have been reached.  
The 3 losers shown, I checked on M5, are also winners after only 2 or 3 levels. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: BodySwitch-18_01_22 12_44.PNG
Size: 155 KB](/attachment/image/4124890/thumbnail?d=1642502831)](/attachment/image/4124890?d=1642502831)   

[0 ](javascript:void\(0\);) [7 ](javascript:void\(0\);)

  * [#265](/thread/post/13861298#post13861298 "Post Permalink")

  * Jan 18, 2022 10:42pm  Jan 18, 2022 10:42pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar433570_3.gif) simnz](simnz)

  * Joined Nov 2015 | Status: Trader | [2,525 Posts](/search?do=process&provider=Member&searchuser=433570)

> [Quoting SwingMan](/thread/post/13861000#post13861000 "View Quoted Post")
> 
> Disliked
> 
> New indicator version "smBodySwitch Signals_v2.9" - For a better overview (only for retirees), the trading panel now has different background colors for active long or short trades. {file} An interesting day so far! 3 winners have been reached. The 3 losers shown, I checked on M5, are also winners after only 2 or 3 levels. {image}
> 
> Ignored

Thank you for keeping retirees in mind. Can this be used for index symbols also? 

Practice makes a person perfect

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#266](/thread/post/13861328#post13861328 "Post Permalink")

  * Edited 11:12pm  Jan 18, 2022 11:01pm | Edited 11:12pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting simnz](/thread/post/13861298#post13861298 "View Quoted Post")
> 
> Disliked
> 
> Thank you for keeping retirees in mind. Can this be used for index symbols also?
> 
> Ignored

Yes, I think about retirees 24/24 hours...  
  
Sure one can apply for indexes.  
I'm just realizing that something is wrong with the currency indexes. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: BodySwitch-Indexes-180122-1555.PNG
Size: 68 KB](/attachment/image/4125065/thumbnail?d=1642514453)](/attachment/image/4125065?d=1642514453)   

[0 ](javascript:void\(0\);) [4 ](javascript:void\(0\);)

  * [#267](/thread/post/13862223#post13862223 "Post Permalink")

  * Jan 19, 2022 5:36am  Jan 19, 2022 5:36am 

  * [ veslup](veslup)

  * | Joined Nov 2009  | Status: Trader | [141 Posts](/search?do=process&provider=Member&searchuser=124349)

The market today is very difficult but the result is not so bad at all.  
  
  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 373 KB](/attachment/image/4125346/thumbnail?d=1642538054)](/attachment/image/4125346?d=1642538054)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#268](/thread/post/13862228#post13862228 "Post Permalink")

  * Jan 19, 2022 5:42am  Jan 19, 2022 5:42am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar71675_5.gif) Alberto_Jazz](alberto_jazz)

  * Joined Jun 2008 | Status: Trader | [593 Posts](/search?do=process&provider=Member&searchuser=71675)

Just added DAX on my monitor 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 103 KB](/attachment/image/4125352/thumbnail?d=1642538534)](/attachment/image/4125352?d=1642538534)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#269](/thread/post/13862927#post13862927 "Post Permalink")

  * Edited Jan 20, 2022 6:23pm  Jan 19, 2022 6:49pm | Edited Jan 20, 2022 6:23pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar71675_5.gif) Alberto_Jazz](alberto_jazz)

  * Joined Jun 2008 | Status: Trader | [593 Posts](/search?do=process&provider=Member&searchuser=71675)

Today I have a banked profit on DAX but it's referred to asian session, it's not so realistic. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 34 KB](/attachment/image/4125837/thumbnail?d=1642585703)](/attachment/image/4125837?d=1642585703)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#270](/thread/post/13863958#post13863958 "Post Permalink")

  * Edited 10:04am  Jan 20, 2022 9:36am | Edited 10:04am 

  * [ graphium](graphium)

  * | Joined Jul 2020  | Status: Trader | [25 Posts](/search?do=process&provider=Member&searchuser=973679)

Hi SwingMan,  
  
Thank you for sharing this system, indicators and all your hard work!  
  
I have just downloaded and installed the indicators and I was just about to start testing them on demo, however while placing my first order on GBPUSD I noticed the SL level displayed on left top corner panel does not match the actual level displayed on a chart by "cross" (cross level is correct) - please see the screenshot.  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 32 KB](/attachment/image/4126396/thumbnail?d=1642638843)](/attachment/image/4126396?d=1642638843)   

  
  
That fixed itself after mt4 restart... I think you mentioned about this issue before... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#271](/thread/post/13864257#post13864257 "Post Permalink")

  * Jan 20, 2022 5:12pm  Jan 20, 2022 5:12pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting graphium](/thread/post/13863958#post13863958 "View Quoted Post")
> 
> Disliked
> 
> ...I have just downloaded and installed the indicators and I was just about to start testing them on demo, however while placing my first order on GBPUSD I noticed the SL level displayed on left top corner panel does not match the actual level displayed on a chart by "cross" (cross level is correct) - please see the screenshot.
> 
> Ignored

The system is actually not suitable for manual trading because one also has to take into account the sliding trailing stop, and that is difficult.  
  
In any case, one should not forget that the calculated values are made with bid prices, i.e. the spread must be taken into account.  
For that you should read post #236: [https://www.forexfactory.com/thread/...5#post13855695](https://www.forexfactory.com/thread/post/13855695#post13855695)  
There is a switch in inputs.  
For manual trading Arrows are displayed for calculated values, and values for orders are written in the panel. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#272](/thread/post/13864375#post13864375 "Post Permalink")

  * Jan 20, 2022 6:23pm  Jan 20, 2022 6:23pm 

  * [ graphium](graphium)

  * | Joined Jul 2020  | Status: Trader | [25 Posts](/search?do=process&provider=Member&searchuser=973679)

Thank you SwingMan for your reply.  
It all makes sense…. I must admit I wanted to test if this system has an edge if traded only manually, without sliding SL - I have very limited time to trade – 2 small kids, full time-long hours job, etc….  
Essentially, I am ideally looking to create/find an end-of-day / daily set & forget system. I really like that your system execution is on daily and that It has a fairly small TPs and SLs (so even though it uses daily TF, it can be used to set a large number of trades daily and then one could benefit from the law of large numbers… if it has an edge traded this way…). I may fail, but it could also give me some other ideas…  
Of course there is an alternative - to use this system the way it was intended to – with an EA…  
Thanks again for sharing your ideas, I will get and use the version from post #236 as suggested. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#273](/thread/post/13864526#post13864526 "Post Permalink")

  * Jan 20, 2022 8:12pm  Jan 20, 2022 8:12pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting graphium](/thread/post/13864375#post13864375 "View Quoted Post")
> 
> Disliked
> 
> ...I will get and use the version from post #236 as suggested.
> 
> Ignored

I wrote Post #236 to read the text, and not apply the posted version. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#274](/thread/post/13864669#post13864669 "Post Permalink")

  * Jan 20, 2022 10:09pm  Jan 20, 2022 10:09pm 

  * [ graphium](graphium)

  * | Joined Jul 2020  | Status: Trader | [25 Posts](/search?do=process&provider=Member&searchuser=973679)

> [Quoting SwingMan](/thread/post/13864526#post13864526 "View Quoted Post")
> 
> Disliked
> 
> {quote} I wrote Post #236 to read the text, and not apply the posted version.
> 
> Ignored

Thanks for clarification... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#275](/thread/post/13864682#post13864682 "Post Permalink")

  * Jan 20, 2022 10:16pm  Jan 20, 2022 10:16pm 

  * [ helene1](helene1)

  * | Joined Jun 2021  | Status: Trader | [11 Posts](/search?do=process&provider=Member&searchuser=1138112)

Hi SwingMan,  
do you also have the indicator for MT5? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#276](/thread/post/13864708#post13864708 "Post Permalink")

  * Jan 20, 2022 10:34pm  Jan 20, 2022 10:34pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting helene1](/thread/post/13864682#post13864682 "View Quoted Post")
> 
> Disliked
> 
> Hi SwingMan, do you also have the indicator for MT5?
> 
> Ignored

I'm sorry but I don't intend to program for MT5. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#277](/thread/post/13865435#post13865435 "Post Permalink")

  * Jan 21, 2022 8:10am  Jan 21, 2022 8:10am 

  * [ graphium](graphium)

  * | Joined Jul 2020  | Status: Trader | [25 Posts](/search?do=process&provider=Member&searchuser=973679)

I placed yesterday 12 orders, all short, 5 were triggered, 3 winners EURGBP, EURJPY, CHFJPY; 2(1) losers - USDCAD - this could have been a winner with the sliding hedge entry, GBPJPY was only triggered just before the end of the trading day with/by a huuuge spread (my mistake - I should have cancelled this order 1-2 hours earlier). 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#278](/thread/post/13865821#post13865821 "Post Permalink")

  * Jan 21, 2022 5:44pm  Jan 21, 2022 5:44pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting graphium](/thread/post/13865435#post13865435 "View Quoted Post")
> 
> Disliked
> 
> ...GBPJPY was only triggered just before the end of the trading day with/by a huuuge spread (my mistake - I should have cancelled this order 1-2 hours earlier).
> 
> Ignored

  
This is true and the EA does not need to send orders 3-5 hours before the end of the day.  
  
But I saw from you that one should also close existing orders. OK. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#279](/thread/post/13866200#post13866200 "Post Permalink")

  * Jan 21, 2022 9:52pm  Jan 21, 2022 9:52pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar71675_5.gif) Alberto_Jazz](alberto_jazz)

  * Joined Jun 2008 | Status: Trader | [593 Posts](/search?do=process&provider=Member&searchuser=71675)

Today I have banked profit on GBPJPY, NZDUSD and DAX.  
  
Running on GBPUSD, USDJPY and USDCHF at the moment. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#280](/thread/post/13866356#post13866356 "Post Permalink")

  * Jan 21, 2022 10:59pm  Jan 21, 2022 10:59pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting Alberto_Jazz](/thread/post/13866200#post13866200 "View Quoted Post")
> 
> Disliked
> 
> Today I have banked profit on GBPJPY, NZDUSD and DAX. Running on GBPUSD, USDJPY and USDCHF at the moment.
> 
> Ignored

Nice. An interesting day, today.  
  
Until now, 11 Wins, and 2 Losses who are winners after hedging. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: BodySwitch-Indexes-210122-1555.png
Size: 242 KB](/attachment/image/4127877/thumbnail?d=1642773561)](/attachment/image/4127877?d=1642773561)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * LazyHedging Trading Ideas
  *   * [ **Reply to Thread** ](/thread/1058948-lazyhedging-trading-ideas/reply#reply)

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

[EurCad Analysis and Trading Ideas](/thread/360980-eurcad-analysis-and-trading-ideas "Hello my friends. 
 
As of lately I have had remarkable success in trading EurCad and after hearing other traders ideas I decided that we...") 594 replies

[FSP Trading Journal and Trend Ideas](/thread/427493-fsp-trading-journal-and-trend-ideas "hello  
I am trying to post some of my trade Ideas here. 
there will be trend following and counter trend trades. 
I will post image rather...") 16 replies

[Forex trading platform that doesn't take your ideas](/thread/311080-forex-trading-platform-that-doesnt-take-your-ideas "Ninja trader, Metatrader, Tradestation all can copy the EA and indicators straight out of your PC. 
 
How do we go about developing a...") 11 replies

[Program Your Trading Ideas without being a programmer](/thread/225629-program-your-trading-ideas-without-being-a-programmer "I have to admit, I have a lot of trading ideas, but no programming skills. I hate paying a programmer to take 3 days to write an EA for me,...") 4 replies

[Exchanging trading ideas](/thread/136764-exchanging-trading-ideas "I'm opening this thread as a substitute for live chat like msn etc to exchange trading ideas and to filter of some posts at Igrok's thread,...") 37 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/1058948-lazyhedging-trading-ideas/reply#reply)
  * Subscribe
  * [271](javascript:void\(0\);)

Attachments: LazyHedging Trading Ideas

Tags: LazyHedging Trading Ideas

#  [](/thread/1058948-lazyhedging-trading-ideas)LazyHedging Trading Ideas 

  * 

  * [#281](/thread/post/13866432#post13866432 "Post Permalink")

  * Jan 21, 2022 11:37pm  Jan 21, 2022 11:37pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar71675_5.gif) Alberto_Jazz](alberto_jazz)

  * Joined Jun 2008 | Status: Trader | [593 Posts](/search?do=process&provider=Member&searchuser=71675)

Hi SM, could you tell if the system can work on GOLD and WTI ?  
  
Thank you 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#282](/thread/post/13866522#post13866522 "Post Permalink")

  * Jan 22, 2022 12:09am  Jan 22, 2022 12:09am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting Alberto_Jazz](/thread/post/13866432#post13866432 "View Quoted Post")
> 
> Disliked
> 
> Hi SM, could you tell if the system can work on GOLD and WTI ? Thank you
> 
> Ignored

Please do not ask any questions about trading. I am not a trader and test as little as possible because I lose enough time programming.  
Why don't you test in the charts, that's easy?  
Actually, in my previous chart posted, you could see the gold and spot on the right. Click on the chart to enlarge it and one sees everything.  
  
Here other charts. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Spot-21.01.2022.PNG
Size: 42 KB](/attachment/image/4127945/thumbnail?d=1642777622)](/attachment/image/4127945?d=1642777622)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#283](/thread/post/13866654#post13866654 "Post Permalink")

  * Jan 22, 2022 1:04am  Jan 22, 2022 1:04am 

  * [ veslup](veslup)

  * | Joined Nov 2009  | Status: Trader | [141 Posts](/search?do=process&provider=Member&searchuser=124349)

Almost the same.  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 437 KB](/attachment/image/4128009/thumbnail?d=1642781059)](/attachment/image/4128009?d=1642781059)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#284](/thread/post/13867064#post13867064 "Post Permalink")

  * Jan 22, 2022 9:08am  Jan 22, 2022 9:08am 

  * [ graphium](graphium)

  * | Joined Jul 2020  | Status: Trader | [25 Posts](/search?do=process&provider=Member&searchuser=973679)

My day was not as good: 6 lost, 2 won. Interestingly enough some trades that you won, I lost.... here are my orders:   

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 22 KB](/attachment/image/4128209/thumbnail?d=1642809259)](/attachment/image/4128209?d=1642809259)   

  
It could have been because my broker's (UK IG) new daily candle starts at 00:00 GMT (BST in summer), so I probably have different entrly/tp/sl levels than rest of you...  
  
Also, I have noticed the indicator shows 4 wins/profits, not 2, not sure why.   

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 229 KB](/attachment/image/4128213/thumbnail?d=1642809781)](/attachment/image/4128213?d=1642809781)   

  
on GBPYJPY for example I marked 3 red levels for entry, SL, TP, - on 5min chart, it clearly shows the SL was hit first:  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 12 KB](/attachment/image/4128214/thumbnail?d=1642810050)](/attachment/image/4128214?d=1642810050)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#285](/thread/post/13867206#post13867206 "Post Permalink")

  * Jan 22, 2022 6:27pm  Jan 22, 2022 6:27pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting graphium](/thread/post/13867064#post13867064 "View Quoted Post")
> 
> Disliked
> 
> ...on GBPYJPY for example I marked 3 red levels for entry, SL, TP, - on 5min chart, it clearly shows the SL was hit first:
> 
> Ignored

One should consider please that I have only described a trading idea here.  
The indicator only makes a rough evaluation of possible outcomes, and cannot take into account intraday movements when calculating profits or losses.  
Only with the EA will one be able to determine whether the idea of the sliding hedge can win without straining the capital too much, or whether the capital will be used up too quickly.  
  
Your example with GBPJPY is one of the worst cases because it took 7 steps to reach the profit. (One will have to determine whether only 3 or 4 steps are sufficient.)  
  
In the chart I have drawn thick orange lines between the reverse points. One sees that the distances are mostly smaller than half the WinPoints value!  
In the Excel spreadsheet in [Post #33](https://www.forexfactory.com/thread/post/13407947#post13407947) one sees that a martingale should have bet 64 lots at this point, and with that trailing hedge only 11.39.  
(Please calculate with a percentage of the capital instead of lots. 1% risk e.g. Or 0.1%, 0.5% etc.) 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: GBPJPY.rM5.png
Size: 61 KB](/attachment/image/4128284/thumbnail?d=1642842719)](/attachment/image/4128284?d=1642842719)   

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#286](/thread/post/13867457#post13867457 "Post Permalink")

  * Jan 23, 2022 6:03am  Jan 23, 2022 6:03am 

  * [ graphium](graphium)

  * | Joined Jul 2020  | Status: Trader | [25 Posts](/search?do=process&provider=Member&searchuser=973679)

> [Quoting SwingMan](/thread/post/13867206#post13867206 "View Quoted Post")
> 
> Disliked
> 
> {quote} One should consider please that I have only described a trading idea here...
> 
> Ignored

Thanks for your reply SwingMan. All makes sense .  
  
From what I have seen so far the concept of your "sliding hedge" with martingale would greatly improve results. In fact that's probably the only profitable (in a long run) way of using martingale I have ever seen and now consider using...  
  
However, I am trying to check first if there is an edge in your system of entries and exits on its own... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#287](/thread/post/13867509#post13867509 "Post Permalink")

  * Edited 3:04pm  Jan 23, 2022 8:35am | Edited 3:04pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting graphium](/thread/post/13867457#post13867457 "View Quoted Post")
> 
> Disliked
> 
> ...I am trying to check first if there is an edge in your system of entries and exits on its own...
> 
> Ignored

Very good, when you're done the checking, please let us know...  
Have you tested the statistics module of the indicator? The number of over 60% wins should perhaps also be present in practice.  
  
Meanwhile the EA has started to work and a first version will be available maybe next week.  
  
I won't post the EA in the thread (yet) because I don't know if one has understood the indicator BodySwitch how it works, and it would be pointless to use the EA blindly.  
Only if one has also posted something in the thread, one can write me a PM and later I will send a link to download the EA.  
The EA needs serious testing before it will eventually work, and I'm not getting any helpful feedback from anonymous downloaders.  
  
Here is the chart of GBPJPY-M5 that I evaluated manually beforehand in Post #285. (MoneyManagement is not yet available)  
One sees that the result is identical. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: GBPJPY.rM5-EA.png
Size: 31 KB](/attachment/image/4128470/thumbnail?d=1642894444)](/attachment/image/4128470?d=1642894444)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#288](/thread/post/13867532#post13867532 "Post Permalink")

  * Jan 23, 2022 10:20am  Jan 23, 2022 10:20am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar95693_6.gif) jado911](jado911)

  * Joined Mar 2009 | Status: Trader | [331 Posts](/search?do=process&provider=Member&searchuser=95693)

> [Quoting SwingMan](/thread/post/13867509#post13867509 "View Quoted Post")
> 
> Disliked
> 
> {quote} Very good, when you're done the checking, please let us know... Have you tested the statistics module of the indicator? The number of over 60% wins should perhaps also be present in practice. Meanwhile the EA has started to work and a first version will be available maybe next week. I won't post the EA in the thread (yet) because I don't know if one has understood the indicator BodySwitch how it works, and it would be pointless to use the EA blindly. Only if one has also posted something in the thread, one can write me a PM and later I will...
> 
> Ignored

Hello SwingMan, From what I understood about the system, you are looking at the body switch and trading after the signal in that direction, I don't understand why the Results here are Sell to buy back to back? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#289](/thread/post/13867587#post13867587 "Post Permalink")

  * Jan 23, 2022 3:01pm  Jan 23, 2022 3:01pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting jado911](/thread/post/13867532#post13867532 "View Quoted Post")
> 
> Disliked
> 
> ...Hello SwingMan, From what I understood about the system, you are looking at the body switch and trading after the signal in that direction, I don't understand why the Results here are Sell to buy back to back?
> 
> Ignored

The BodySwitch indicator is a proprietary indicator, and I haven't seen the idea or the algorithm anywhere, maybe there is. The idea came to me after studying the "Mantra" indicator, but it's something completely different.  
  
In fact, the trend is signaled because "Big Bars" break through an existing trend level. You will also find some threads in the forum where "Big Bars" are traded.  
  
However, I wrote that the trend is not traded, but only a small part of the movement intraday (0.20 of the Volatility=ATR). It's an idea that should be tested to see what that brings, because the tools for this are still under development.  
In Post #189 I specifically wrote: "The idea in the thread is hedging (lazy hedging), and not trend trading." 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#290](/thread/post/13867792#post13867792 "Post Permalink")

  * Jan 24, 2022 12:52am  Jan 24, 2022 12:52am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

There is my first test for the EA.  
  
The quality of my historical data is very poor, and there are still some bugs in the program that negatively affect the results.  
If one corrects them, the results will be slightly better. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Tester Report EURUSD-D1 10months.PNG
Size: 59 KB](/attachment/image/4128652/thumbnail?d=1642953133)](/attachment/image/4128652?d=1642953133)   

[0 ](javascript:void\(0\);) [5 ](javascript:void\(0\);)

  * [#291](/thread/post/13867799#post13867799 "Post Permalink")

  * Jan 24, 2022 12:59am  Jan 24, 2022 12:59am 

  * [ veslup](veslup)

  * | Joined Nov 2009  | Status: Trader | [141 Posts](/search?do=process&provider=Member&searchuser=124349)

> [Quoting SwingMan](/thread/post/13867792#post13867792 "View Quoted Post")
> 
> Disliked
> 
> There is my first test for the EA. The quality of my historical data is very poor, and there are still some bugs in the program that negatively affect the results. If one corrects them, the results will be slightly better. {image}
> 
> Ignored

Hi SwingMan,  
  
I have 100% history and if you don't have mind I can test it. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#292](/thread/post/13867815#post13867815 "Post Permalink")

  * Jan 24, 2022 1:13am  Jan 24, 2022 1:13am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting veslup](/thread/post/13867799#post13867799 "View Quoted Post")
> 
> Disliked
> 
> ...Hi SwingMan, I have 100% history and if you don't have mind I can test it.
> 
> Ignored

Thank you very much for your offer.  
Be the first on the tester list and send you the EA when I have corrected two or three existing errors.  
  
I won't have any time and no reasonable price data to be able to test the next versions.  
In reality, I'm not interested in that either, even if the theory, which is so perfect, can't be applied in practice later... 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#293](/thread/post/13867986#post13867986 "Post Permalink")

  * Edited 11:47pm  Jan 24, 2022 6:39am | Edited 11:47pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

Here is the first version for **"smBodySwitch EA_v1.1** ".  
  
I tested EURUSD from January 2021.  
(One should test without VisualMode, it's faster.)  
  
It works well for $10,000 in tester and 0.1% risk.  
My big problem is with the margin/free margin.  
With InitialDeposit=$1,000, SpecifiedMoney=$1,000 and Risk 1%, the message that the FreeMargin has been exceeded quickly comes up. Already at 0.43 lots.  
(Typical is to test 6-8 January 2021, then bang it because of level 6 in the martingale.)  
Setting one to InitialDepot=$10,000 works fine.  
  
My account leverage is probably 100:1, and at 500:1, maybe 200:1 might work just fine.  
  
To see values for the margin one can set the switch "Show_MarginInfo=true".  
Maybe someone will explain under what account conditions (capital, leverage, risk) can the EA work with higher martingale levels.  
  
**See new version in Post #296**

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: TesterReport-EURUSD-D1-Jan21Jan22.PNG
Size: 58 KB](/attachment/image/4128753/thumbnail?d=1642972541)](/attachment/image/4128753?d=1642972541)   
[![Click to Enlarge

Name: Tester-Inputs.PNG
Size: 6 KB](/attachment/image/4128754/thumbnail?d=1642972549)](/attachment/image/4128754?d=1642972549)   
[![Click to Enlarge

Name: MarginInfo.PNG
Size: 2 KB](/attachment/image/4128771/thumbnail?d=1642973961)](/attachment/image/4128771?d=1642973961)   

[0 ](javascript:void\(0\);) [5 ](javascript:void\(0\);)

  * [#294](/thread/post/13868175#post13868175 "Post Permalink")

  * Jan 24, 2022 2:17pm  Jan 24, 2022 2:17pm 

  * [ d.dalal333](d.dalal333)

  * | Joined Jan 2013  | Status: Trader | [72 Posts](/search?do=process&provider=Member&searchuser=321856)

> [Quoting veslup](/thread/post/13867799#post13867799 "View Quoted Post")
> 
> Disliked
> 
> {quote} hi swingman, i have 100% history and if you don't have mind i can test it.
> 
> Ignored

will u pl share history file 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#295](/thread/post/13868281#post13868281 "Post Permalink")

  * Jan 24, 2022 4:50pm  Jan 24, 2022 4:50pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

Here is the stupid message with the FreeMargin.  
  
The display of the many arrows is a small error caused by the message, will correct it. 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: FreeMargin-6-Ian21.PNG
Size: 43 KB](/attachment/image/4128962/thumbnail?d=1643010585)](/attachment/image/4128962?d=1643010585)   
[![Click to Enlarge

Name: EURUSD.rDaily.png
Size: 8 KB](/attachment/image/4128963/thumbnail?d=1643010592)](/attachment/image/4128963?d=1643010592)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#296](/thread/post/13868408#post13868408 "Post Permalink")

  * Edited 7:07pm  Jan 24, 2022 6:50pm | Edited 7:07pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

Here is a new version **"smBodySwitch EA_v1.2"**  
with a little change: the EA stops when the FreeMargin is not enough anymore. 

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [smBodySwitch EA_v1.2.ex4](/attachment/file/4129007?d=1643017734) 70 KB | 347 downloads 

[0 ](javascript:void\(0\);) [3 ](javascript:void\(0\);)

  * [#297](/thread/post/13868489#post13868489 "Post Permalink")

  * Jan 24, 2022 7:39pm  Jan 24, 2022 7:39pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar71675_5.gif) Alberto_Jazz](alberto_jazz)

  * Joined Jun 2008 | Status: Trader | [593 Posts](/search?do=process&provider=Member&searchuser=71675)

Hi SM, many thanks for the expert.  
  
I'm trying to run it on a demo account. When I attach it to a graph, a pending order is immediatly opened.  
  
If I try to attach the expert on another symbol, previous pending order is deleted and a new one is opended on the last chart.  
  
Is the expert able to run on a single chart? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#298](/thread/post/13868558#post13868558 "Post Permalink")

  * Jan 24, 2022 8:16pm  Jan 24, 2022 8:16pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting SwingMan](/thread/post/13867986#post13867986 "View Quoted Post")
> 
> Disliked
> 
> ...My account leverage is probably 100:1, and at 500:1, maybe 200:1 might work just fine.
> 
> Ignored

OK, I have now clarified with my broker: my leverage is 30:1, and in Europe one can probably not get a better one for Forex trading.  
  
One would now have to adjust in EA the number of pairs traded to the capital and the corresponding pair margin. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#299](/thread/post/13868636#post13868636 "Post Permalink")

  * Jan 24, 2022 9:30pm  Jan 24, 2022 9:30pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar71675_5.gif) Alberto_Jazz](alberto_jazz)

  * Joined Jun 2008 | Status: Trader | [593 Posts](/search?do=process&provider=Member&searchuser=71675)

> [Quoting SwingMan](/thread/post/13868558#post13868558 "View Quoted Post")
> 
> Disliked
> 
> {quote} OK, I have now clarified with my broker: my leverage is 30:1, and in Europe one can probably not get a better one for Forex trading. One would now have to adjust in EA the number of pairs traded to the capital and the corresponding pair margin.
> 
> Ignored

I can confirm, my demo account with [FX Pro](/brokers/fxpro "View FxPro Broker Profile") is 30:1. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#300](/thread/post/13868701#post13868701 "Post Permalink")

  * Jan 24, 2022 10:09pm  Jan 24, 2022 10:09pm 

  * [ graphium](graphium)

  * | Joined Jul 2020  | Status: Trader | [25 Posts](/search?do=process&provider=Member&searchuser=973679)

> [Quoting SwingMan](/thread/post/13868558#post13868558 "View Quoted Post")
> 
> Disliked
> 
> {quote} OK, I have now clarified with my broker: my leverage is 30:1, and in Europe one can probably not get a better one for Forex trading. One would now have to adjust in EA the number of pairs traded to the capital and the corresponding pair margin.
> 
> Ignored

30:1 is standard in Europe since ESMA (European Securities & Markets Authority) regulation came in 2018.  
You can still get a higher leverage in Europe if you a professional trader / have professional account... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * LazyHedging Trading Ideas
  *   * [ **Reply to Thread** ](/thread/1058948-lazyhedging-trading-ideas/reply#reply)

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

[EurCad Analysis and Trading Ideas](/thread/360980-eurcad-analysis-and-trading-ideas "Hello my friends. 
 
As of lately I have had remarkable success in trading EurCad and after hearing other traders ideas I decided that we...") 594 replies

[FSP Trading Journal and Trend Ideas](/thread/427493-fsp-trading-journal-and-trend-ideas "hello  
I am trying to post some of my trade Ideas here. 
there will be trend following and counter trend trades. 
I will post image rather...") 16 replies

[Forex trading platform that doesn't take your ideas](/thread/311080-forex-trading-platform-that-doesnt-take-your-ideas "Ninja trader, Metatrader, Tradestation all can copy the EA and indicators straight out of your PC. 
 
How do we go about developing a...") 11 replies

[Program Your Trading Ideas without being a programmer](/thread/225629-program-your-trading-ideas-without-being-a-programmer "I have to admit, I have a lot of trading ideas, but no programming skills. I hate paying a programmer to take 3 days to write an EA for me,...") 4 replies

[Exchanging trading ideas](/thread/136764-exchanging-trading-ideas "I'm opening this thread as a substitute for live chat like msn etc to exchange trading ideas and to filter of some posts at Igrok's thread,...") 37 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/1058948-lazyhedging-trading-ideas/reply#reply)
  * Subscribe
  * [271](javascript:void\(0\);)

Attachments: LazyHedging Trading Ideas

Tags: LazyHedging Trading Ideas

#  [](/thread/1058948-lazyhedging-trading-ideas)LazyHedging Trading Ideas 

  * 

  * [#301](/thread/post/13868765#post13868765 "Post Permalink")

  * Jan 24, 2022 10:50pm  Jan 24, 2022 10:50pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting graphium](/thread/post/13868701#post13868701 "View Quoted Post")
> 
> Disliked
> 
> ...30:1 is standard in Europe since ESMA (European Securities & Markets Authority) regulation came in 2018. You can still get a higher leverage in Europe if you a professional trader / have professional account...
> 
> Ignored

You're right, one need an account of 500,000, and I'm only missing a few EUR... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#302](/thread/post/13868860#post13868860 "Post Permalink")

  * Jan 24, 2022 11:46pm  Jan 24, 2022 11:46pm 

  * [ gerval](gerval)

  * | Joined May 2020  | Status: Trader | [243 Posts](/search?do=process&provider=Member&searchuser=958353)

Testing the indicator on its own, without trailing stop or take profit. When opening a trade I only put the stop and let it run to follow the trend, a couple of days trying it like that, and positive results.  
  
If the EA can be added to that... it can improve the results.  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 63 KB](/attachment/image/4129318/thumbnail?d=1643035538)](/attachment/image/4129318?d=1643035538)   

  
So far one operation has been lost with SL. Which would have been recovered in a coverage. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#303](/thread/post/13868896#post13868896 "Post Permalink")

  * Jan 25, 2022 12:05am  Jan 25, 2022 12:05am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting gerval](/thread/post/13868860#post13868860 "View Quoted Post")
> 
> Disliked
> 
> Testing the indicator on its own, without trailing stop or take profit. When opening a trade I only put the stop and let it run to follow the trend, a couple of days trying it like that, and positive results. If the EA can be added to that... it can improve the results.
> 
> Ignored

If I haven't said so, then I'll repeat: the nude indicator "BodySwitch" should be used for trending trading with appropriate rules. The entry, TP and SL belong to "SlidingHedge" idea.  
  
If the "SlidingHedge EA" doesn't bring anything, I have to do something with the trend because of boredom.  
With the existing EA, one should test what brings to trade only a few levels (3-5 maybe). I underestimated the problem with the leverage and margin, so I will research in this direction.  
  
A quick solution would be: Capital 20,000, Risk 1% for Specified_Account=1,000, maximum 5 pairs at the same time.  
That would burden the private capital with a maximum of approx. 25% margin so that the orders can be carried out. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#304](/thread/post/13868907#post13868907 "Post Permalink")

  * Jan 25, 2022 12:13am  Jan 25, 2022 12:13am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting gerval](/thread/post/13868860#post13868860 "View Quoted Post")
> 
> Disliked
> 
> Testing the indicator on its own, without trailing stop or take profit. When opening a trade I only put the stop and let it run to follow the trend, a couple of days trying it like that, and positive results. If the EA can be added to that... it can improve the results.
> 
> Ignored

You may think that the EA only has the option to open trades without the sofisticate trailing and hedging. OK, that would be a version for people who look at the screen from time to time. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#305](/thread/post/13869460#post13869460 "Post Permalink")

  * Jan 25, 2022 5:51am  Jan 25, 2022 5:51am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

@graphium wrote in post #286  

> Quote
> 
> Disliked
> 
> However, I am trying to check first if there is an edge in your system of entries and exits on its own...

I mentioned it again in post #287  

> Quote
> 
> Disliked
> 
> ...Have you tested the statistics module of the indicator? The number of over 60% wins should perhaps also be present in practice.

My first tests were with the sliding hedge, but one still needs to do some extra work to get the margin under control.  
Now I have tested with a slightly improved version **"smBodySwitch EA_V1.3"**  
if the theory can work in practice and it seems that it can work for some pairs. One would have to test and post here results for different pairs.  
  
Note: (maximTrades=1) so that no reverse trades are started.  
  
Here are two evaluations of win/loss trades, without hedging, with a risk of 1% based on ($1,000 AccountBalance) and on (fixed $1,000 capital).  
The 60 win/40 loss ratio for EURUSD seems to be confirmed.  
  
I also tried to start the Optimization, but for reasons unknown to me, it doesn't work. 

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [smBodySwitch EA_v1.3.ex4](/attachment/file/4129698?d=1643057504) 70 KB | 344 downloads 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#306](/thread/post/13869464#post13869464 "Post Permalink")

  * Jan 25, 2022 5:53am  Jan 25, 2022 5:53am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

**risk of 1% based on ($1,000 AccountBalance)**

Attached Image (click to enlarge)

[![Click to Enlarge

Name: TradeReport-EURUSD-1000 Balance.PNG
Size: 59 KB](/attachment/image/4129699/thumbnail?d=1643057585)](/attachment/image/4129699?d=1643057585)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#307](/thread/post/13869465#post13869465 "Post Permalink")

  * Jan 25, 2022 5:54am  Jan 25, 2022 5:54am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

**risk of 1% based on (fixed $1,000 capital)**

Attached Image (click to enlarge)

[![Click to Enlarge

Name: TradeReport-EURUSD-1000 Capital.PNG
Size: 60 KB](/attachment/image/4129700/thumbnail?d=1643057674)](/attachment/image/4129700?d=1643057674)   

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#308](/thread/post/13869634#post13869634 "Post Permalink")

  * Jan 25, 2022 9:34am  Jan 25, 2022 9:34am 

  * [ graphium](graphium)

  * | Joined Jul 2020  | Status: Trader | [25 Posts](/search?do=process&provider=Member&searchuser=973679)

> [Quoting SwingMan](/thread/post/13869460#post13869460 "View Quoted Post")
> 
> Disliked
> 
> Here are two evaluations of win/loss trades, without hedging, with a risk of 1% based on ($1,000 AccountBalance) and on (fixed $1,000 capital). The 60 win/40 loss ratio for EURUSD seems to be confirmed...
> 
> Ignored

I really like this equity curve!   
  
Hopefully we will be able to replicate this in live trading!!!  
  
Yesterday I had 4 wins (GBPUSD, AUDJPY, AUDUSD, NZDUSD) and 3 loses (GBPJPY, EURJPY, EURGBP).   
Currently after 3rd day of trading this system (20 trades taken, manually with pending orders, no hedge,) I am at -2R. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#309](/thread/post/13869735#post13869735 "Post Permalink")

  * Edited 12:48pm  Jan 25, 2022 12:33pm | Edited 12:48pm 

  * [ Sawaddee](sawaddee)

  * | Joined Jul 2015  | Status: Trader | [188 Posts](/search?do=process&provider=Member&searchuser=419326)

FYI.  
Once orders are opened, they got deleted.  
Even spread < 25%, background still gray. 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 31 KB](/attachment/image/4129882/thumbnail?d=1643081612)](/attachment/image/4129882?d=1643081612)   
[![Click to Enlarge

Name: screenshot.png
Size: 99 KB](/attachment/image/4129883/thumbnail?d=1643081620)](/attachment/image/4129883?d=1643081620)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#310](/thread/post/13869865#post13869865 "Post Permalink")

  * Jan 25, 2022 3:33pm  Jan 25, 2022 3:33pm 

  * [ veslup](veslup)

  * | Joined Nov 2009  | Status: Trader | [141 Posts](/search?do=process&provider=Member&searchuser=124349)

> [Quoting SwingMan](/thread/post/13869465#post13869465 "View Quoted Post")
> 
> Disliked
> 
> risk of 1% based on (fixed $1,000 capital) {image}
> 
> Ignored

Hi SwingMan,  
  
Could you add fixed lot like option ? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#311](/thread/post/13869976#post13869976 "Post Permalink")

  * Jan 25, 2022 5:24pm  Jan 25, 2022 5:24pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting Sawaddee](/thread/post/13869735#post13869735 "View Quoted Post")
> 
> Disliked
> 
> FYI. Once orders are opened, they got deleted. Even spread < 25%, background still gray.
> 
> Ignored

I can not understand what you did.  
  
\- In this version of the EA he does not change background colors, maybe you had previously had the indicator in the chart, and the gray color has remained.  
  
\- I had EURUSD first in the chart, then I have USDCAD. The EA works. Did you click "Allow Live Trading"? 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: USDCAD.rDaily.png
Size: 19 KB](/attachment/image/4130062/thumbnail?d=1643099034)](/attachment/image/4130062?d=1643099034)   
[![Click to Enlarge

Name: Notifications USDCAD.PNG
Size: 8 KB](/attachment/image/4130063/thumbnail?d=1643099043)](/attachment/image/4130063?d=1643099043)   
[![Click to Enlarge

Name: Live trading.PNG
Size: 7 KB](/attachment/image/4130064/thumbnail?d=1643099053)](/attachment/image/4130064?d=1643099053)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#312](/thread/post/13870032#post13870032 "Post Permalink")

  * Edited 6:55pm  Jan 25, 2022 6:11pm | Edited 6:55pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting veslup](/thread/post/13869865#post13869865 "View Quoted Post")
> 
> Disliked
> 
> ...Hi SwingMan, Could you add fixed lot like option ?
> 
> Ignored

I only built for you the option "Enable_MoneyManagement = false".  
  
New EA version **"smBodySwitch EA_V1.5"**

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: MoneyManagement v1.4.PNG
Size: 5 KB](/attachment/image/4130097/thumbnail?d=1643102047)](/attachment/image/4130097?d=1643102047)   
[![Click to Enlarge

Name: USDCAD.rDaily-MM.png
Size: 13 KB](/attachment/image/4130098/thumbnail?d=1643102084)](/attachment/image/4130098?d=1643102084)   

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [smBodySwitch EA_v1.5.ex4](/attachment/file/4130157?d=1643104508) 70 KB | 403 downloads 

[0 ](javascript:void\(0\);) [4 ](javascript:void\(0\);)

  * [#313](/thread/post/13870056#post13870056 "Post Permalink")

  * Jan 25, 2022 6:23pm  Jan 25, 2022 6:23pm 

  * [ Sawaddee](sawaddee)

  * | Joined Jul 2015  | Status: Trader | [188 Posts](/search?do=process&provider=Member&searchuser=419326)

> [Quoting SwingMan](/thread/post/13869976#post13869976 "View Quoted Post")
> 
> Disliked
> 
> {quote} I can not understand what you did. - In this version of the EA he does not change background colors, maybe you had previously had the indicator in the chart, and the gray color has remained. - I had EURUSD first in the chart, then I have USDCAD. The EA works. Did you click "Allow Live Trading"? {image} {image} {image}
> 
> Ignored

I did 2 tries.  
First. I set up a template then apply this template to all 28 pairs (with AutoTrading button "Off"). When I allow autotrading all 28 EAs start to place the order but when the next pair placed an order the previous pair's order was deleted. I use F7 to reactivate the EA one chart at a time and the same result happens. Order of that pair was placed then cancelled when next pair placed the order.  
  
Second. I apply EA one at a time to each pair. The same result.  
  
So, the only order I have is the order of the chart that I activate the latest EA.  
  
Screenshot when I apply EA to each chart one at a time attached. Strange that no panel info. shown. Setting is default setting. I have not changed anything.  
  
A short video clip is attached to show you that the order was deleted when the EA on the new pair is activated. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 117 KB](/attachment/image/4130112/thumbnail?d=1643102735)](/attachment/image/4130112?d=1643102735)   

Attached File(s)

![File Type: mp4](https://assets.faireconomy.media/images/attach/mp4.gif) [2022-01-25_16-29-44.mp4](/attachment/file/4130129?d=1643103168) 4.0 MB | 255 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#314](/thread/post/13870117#post13870117 "Post Permalink")

  * Jan 25, 2022 6:58pm  Jan 25, 2022 6:58pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting Sawaddee](/thread/post/13870056#post13870056 "View Quoted Post")
> 
> Disliked
> 
> ...the order was deleted when the EA on the new pair is activated.
> 
> Ignored

Okay, that's fine.  
  
I am very sorry because a little mistake was in program, here the correction.  
New version **"smBodySwitch EA_v1.5"** in Post #312.

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#315](/thread/post/13870200#post13870200 "Post Permalink")

  * Jan 25, 2022 8:07pm  Jan 25, 2022 8:07pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting Sawaddee](/thread/post/13870056#post13870056 "View Quoted Post")
> 
> Disliked
> 
> ...I set up a template then apply this template to all 28 pairs
> 
> Ignored

I will not give StopOrders in the next version, because many pairs do not reach the Entries and end with Expiry at 22:00.  
  
I will do that by program, because the reverse orders are also sent by program as MarketOrders. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#316](/thread/post/13870292#post13870292 "Post Permalink")

  * Jan 25, 2022 9:28pm  Jan 25, 2022 9:28pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1404830_2.gif) 4xgan](4xgan)

  * | Joined Jan 2022  | Status: Trader | [4 Posts](/search?do=process&provider=Member&searchuser=1404830)

Thanks for your work, this fits my trading style, now i can see the trend is a easy way. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#317](/thread/post/13870698#post13870698 "Post Permalink")

  * Jan 26, 2022 1:36am  Jan 26, 2022 1:36am 

  * [ veslup](veslup)

  * | Joined Nov 2009  | Status: Trader | [141 Posts](/search?do=process&provider=Member&searchuser=124349)

> [Quoting SwingMan](/thread/post/13870032#post13870032 "View Quoted Post")
> 
> Disliked
> 
> {quote} I only built for you the option "Enable_MoneyManagement = false". New EA version "smBodySwitch EA_V1.5" {image} {image} {file}
> 
> Ignored

I am so upset but even with fixed lot I cant perform back test. I don't now what is the reason as I am using Quant data history. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#318](/thread/post/13870832#post13870832 "Post Permalink")

  * Jan 26, 2022 3:31am  Jan 26, 2022 3:31am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

I received a chart for Nasdaq in an email.  
  
When one compares the BodySwitch indicator to an indicator from a professional program that "is a principle-based trading software which received Reader's Choice Awards from S&C magazine for more than 25 years in a row since 1997", there are not major differences... 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: Nasdaq.jpg
Size: 155 KB](/attachment/image/4130606/thumbnail?d=1643135263)](/attachment/image/4130606?d=1643135263)   
[![Click to Enlarge

Name: NAS100.rH4.png
Size: 18 KB](/attachment/image/4130607/thumbnail?d=1643135269)](/attachment/image/4130607?d=1643135269)   

[0 ](javascript:void\(0\);) [4 ](javascript:void\(0\);)

  * [#319](/thread/post/13871151#post13871151 "Post Permalink")

  * Jan 26, 2022 8:38am  Jan 26, 2022 8:38am 

  * [ graphium](graphium)

  * | Joined Jul 2020  | Status: Trader | [25 Posts](/search?do=process&provider=Member&searchuser=973679)

Today's (day 4) results: 4 wins: AUDJPY, CHFJPY, NZDUSD, GBPUSD; 5 loses: GBPJPY, EURJPY, EURUSD, AUDUSD, USDCAD.  
Result after 29 trades triggered: -3R 

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#320](/thread/post/13871154#post13871154 "Post Permalink")

  * Jan 26, 2022 8:47am  Jan 26, 2022 8:47am 

  * [ graphium](graphium)

  * | Joined Jul 2020  | Status: Trader | [25 Posts](/search?do=process&provider=Member&searchuser=973679)

> [Quoting SwingMan](/thread/post/13870832#post13870832 "View Quoted Post")
> 
> Disliked
> 
> I received a chart for Nasdaq in an email. When one compares the BodySwitch indicator to an indicator from a professional program that "is a principle-based trading software which received Reader's Choice Awards from S&C magazine for more than 25 years in a row since 1997", there are not major differences...
> 
> Ignored

Interesting, well done!  
  
I must admit I am planning at some to test your indicator as a main signal for trend following system...  
looking at the chart above it looks promising... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * LazyHedging Trading Ideas
  *   * [ **Reply to Thread** ](/thread/1058948-lazyhedging-trading-ideas/reply#reply)

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

[EurCad Analysis and Trading Ideas](/thread/360980-eurcad-analysis-and-trading-ideas "Hello my friends. 
 
As of lately I have had remarkable success in trading EurCad and after hearing other traders ideas I decided that we...") 594 replies

[FSP Trading Journal and Trend Ideas](/thread/427493-fsp-trading-journal-and-trend-ideas "hello  
I am trying to post some of my trade Ideas here. 
there will be trend following and counter trend trades. 
I will post image rather...") 16 replies

[Forex trading platform that doesn't take your ideas](/thread/311080-forex-trading-platform-that-doesnt-take-your-ideas "Ninja trader, Metatrader, Tradestation all can copy the EA and indicators straight out of your PC. 
 
How do we go about developing a...") 11 replies

[Program Your Trading Ideas without being a programmer](/thread/225629-program-your-trading-ideas-without-being-a-programmer "I have to admit, I have a lot of trading ideas, but no programming skills. I hate paying a programmer to take 3 days to write an EA for me,...") 4 replies

[Exchanging trading ideas](/thread/136764-exchanging-trading-ideas "I'm opening this thread as a substitute for live chat like msn etc to exchange trading ideas and to filter of some posts at Igrok's thread,...") 37 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/1058948-lazyhedging-trading-ideas/reply#reply)
  * Subscribe
  * [271](javascript:void\(0\);)

Attachments: LazyHedging Trading Ideas

Tags: LazyHedging Trading Ideas

#  [](/thread/1058948-lazyhedging-trading-ideas)LazyHedging Trading Ideas 

  * 

  * [#321](/thread/post/13871244#post13871244 "Post Permalink")

  * Jan 26, 2022 12:35pm  Jan 26, 2022 12:35pm 

  * [ Sawaddee](sawaddee)

  * | Joined Jul 2015  | Status: Trader | [188 Posts](/search?do=process&provider=Member&searchuser=419326)

The attached picture is the result after v1.5 attached to 28 pairs.  
Starting account balance is USD5,000 but in the EA I leave it to $1,000  
  
End of day balance is USD5,052.37 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Report 26 Jan.png
Size: 87 KB](/attachment/image/4130841/thumbnail?d=1643168105)](/attachment/image/4130841?d=1643168105)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#322](/thread/post/13871329#post13871329 "Post Permalink")

  * Edited 3:30pm  Jan 26, 2022 3:08pm | Edited 3:30pm 

  * [ Night63](night63)

  * | Joined Sep 2020  | Status: Trader | [226 Posts](/search?do=process&provider=Member&searchuser=1003725) | Online Now 

What first order 0.1 and next 2.58 ??  
3rd 7,68..  
  
Version 1.5 --- SET:  
=======================================  
MagicNumber=1000  
Show_MarginInfo=false  
____Money_Management=---------------------------------------  
maximTrades=20  
Trading_Lots=0.1  
Enable_MoneyManagement=true  
Risk_Percent=1.5  
Reference_Account=0  
Account_SpecifiedMoney=1000.0  
____Factors=---------------------------------------  
Entry_Factor=0.5  
TakeProfit_Factor=0.2  
StopLoss_Factor=0.5  
____Infos=---------------------------------------  
Result_Text=0  
Show_TradingPanel=true  
Show_Comment=true  
Draw_StopLossArrows=true  
Draw_TradingResults=false  
Write_SymbolInfo=false  
Write_ResultsInFile=false  
____Spread_Condition=---------------------------------------  
Maximum_SpreadPercents=25  
ChangeBackground_ForMaxSpread=true  
____Other_Inputs=---------------------------------------  
Chart_Scale=3  
TradingPanelPosition_X=0  
TradingPanelPosition_Y=13  
TradingPanel_Width=250  
TradingPanel_Height=260  
Double_LineSpacing=true  
======================================= 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: Whatsm.jpg
Size: 283 KB](/attachment/image/4130919/thumbnail?d=1643177274)](/attachment/image/4130919?d=1643177274)   
[![Click to Enlarge

Name: 3rd.jpg
Size: 63 KB](/attachment/image/4130921/thumbnail?d=1643177478)](/attachment/image/4130921?d=1643177478)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#323](/thread/post/13871336#post13871336 "Post Permalink")

  * Jan 26, 2022 3:25pm  Jan 26, 2022 3:25pm 

  * [ Sawaddee](sawaddee)

  * | Joined Jul 2015  | Status: Trader | [188 Posts](/search?do=process&provider=Member&searchuser=419326)

> [Quoting Night63](/thread/post/13871329#post13871329 "View Quoted Post")
> 
> Disliked
> 
> What first order 0.1 and next 2.58 ?? 3rd 7,68.. Version 1.5 --- SET: ======================================= MagicNumber=1000 Show_MarginInfo=false ____Money_Management=--------------------------------------- maximTrades=20 Trading_Lots=0.1 Enable_MoneyManagement=true Risk_Percent=1.5 Reference_Account=0 Account_SpecifiedMoney=1000.0 ____Factors=--------------------------------------- Entry_Factor=0.5 TakeProfit_Factor=0.2 StopLoss_Factor=0.5 ____Infos=--------------------------------------- Result_Text=0 Show_TradingPanel=true Show_Comment=true...
> 
> Ignored

Please see attached picture for my setting (default). I can notice that my "Risk_Percent" is only 1.0 while yours shows 1.5 but it should not give such a big difference. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 61 KB](/attachment/image/4130928/thumbnail?d=1643178322)](/attachment/image/4130928?d=1643178322)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#324](/thread/post/13871338#post13871338 "Post Permalink")

  * Jan 26, 2022 3:27pm  Jan 26, 2022 3:27pm 

  * [ Sawaddee](sawaddee)

  * | Joined Jul 2015  | Status: Trader | [188 Posts](/search?do=process&provider=Member&searchuser=419326)

At the time I post this message, these are the pending orders for 26 Jan. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 46 KB](/attachment/image/4130931/thumbnail?d=1643178455)](/attachment/image/4130931?d=1643178455)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#325](/thread/post/13871424#post13871424 "Post Permalink")

  * Jan 26, 2022 5:13pm  Jan 26, 2022 5:13pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting graphium](/thread/post/13871151#post13871151 "View Quoted Post")
> 
> Disliked
> 
> Today's (day 4) results: 4 wins: AUDJPY, CHFJPY, NZDUSD, GBPUSD; 5 loses: GBPJPY, EURJPY, EURUSD, AUDUSD, USDCAD. Result after 29 trades triggered: -3R
> 
> Ignored

Be sure to do a few evaluations in the backtest.  
This is how you realize that not all pairs go well like the EURUSD.  
  
I also did a few tests with the Optimization (for 6 months so that it runs faster), but that didn't help much either.  
I'll use an additional trick to calculate the levels, let's see if that helps. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#326](/thread/post/13871439#post13871439 "Post Permalink")

  * Jan 26, 2022 5:22pm  Jan 26, 2022 5:22pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting graphium](/thread/post/13871154#post13871154 "View Quoted Post")
> 
> Disliked
> 
> ...Interesting, well done! I must admit I am planning at some to test your indicator as a main signal for trend following system... looking at the chart above it looks promising...
> 
> Ignored

Basically the strategy of AbleSys is to determine the trend with the indicator, and further use fractals and retraces for entries.  
You can do something similar with the "MTF_Fractal" indicator like this: 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: EURUSD.rDaily.png
Size: 37 KB](/attachment/image/4130974/thumbnail?d=1643185297)](/attachment/image/4130974?d=1643185297)   

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#327](/thread/post/13871870#post13871870 "Post Permalink")

  * Jan 26, 2022 11:03pm  Jan 26, 2022 11:03pm 

  * [ graphium](graphium)

  * | Joined Jul 2020  | Status: Trader | [25 Posts](/search?do=process&provider=Member&searchuser=973679)

> [Quoting SwingMan](/thread/post/13871424#post13871424 "View Quoted Post")
> 
> Disliked
> 
> {quote} Be sure to do a few evaluations in the backtest. This is how you realize that not all pairs go well like the EURUSD. I also did a few tests with the Optimization (for 6 months so that it runs faster), but that didn't help much either. I'll use an additional trick to calculate the levels, let's see if that helps.
> 
> Ignored

I think it's to early to make any conclusions from my results.  
  
I have just run a simple Monte Carlo simulation based on 60% win rate and series of 30 tests returning either 1 or -1. After just a few runs the lowest negative sum/result was -12!, and there were still a few results still below my trading results....  
  
So I think nothing unusual is happening here. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#328](/thread/post/13871878#post13871878 "Post Permalink")

  * Jan 26, 2022 11:06pm  Jan 26, 2022 11:06pm 

  * [ graphium](graphium)

  * | Joined Jul 2020  | Status: Trader | [25 Posts](/search?do=process&provider=Member&searchuser=973679)

> [Quoting SwingMan](/thread/post/13871439#post13871439 "View Quoted Post")
> 
> Disliked
> 
> {quote} Basically the strategy of AbleSys is to determine the trend with the indicator, and further use fractals and retraces for entries. You can do something similar with the "MTF_Fractal" indicator like this:
> 
> Ignored

Thanks SwingMan for the info, I was thinking about something similar, but MTF Fractal might actually be better for this. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#329](/thread/post/13872010#post13872010 "Post Permalink")

  * Jan 27, 2022 12:14am  Jan 27, 2022 12:14am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting graphium](/thread/post/13871878#post13871878 "View Quoted Post")
> 
> Disliked
> 
> ...Thanks SwingMan for the info, I was thinking about something similar, but MTF Fractal might actually be better for this.
> 
> Ignored

What I would always recommend is the [Fractal Kiss](https://www.forexfactory.com/thread/post/13783501#post13783501) idea.  
  
Wouldn't be bad to program if someone tests the idea and formulates a few rules. 

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#330](/thread/post/13872876#post13872876 "Post Permalink")

  * Jan 27, 2022 10:04am  Jan 27, 2022 10:04am 

  * [ graphium](graphium)

  * | Joined Jul 2020  | Status: Trader | [25 Posts](/search?do=process&provider=Member&searchuser=973679)

> [Quoting SwingMan](/thread/post/13872010#post13872010 "View Quoted Post")
> 
> Disliked
> 
> {quote} What I would always recommend is the [Fractal Kiss](https://www.forexfactory.com/thread/post/13783501#post13783501) idea. Wouldn't be bad to program if someone tests the idea and formulates a few rules.
> 
> Ignored

I just did a very quick visual backtest of fractal kiss idea, based on 1D direction and entry on 4H... looks very interesting indeed...  
I will try to get back to it next day, hopefully I will have a bit more time.  
  
...  
Today's (day 5) results: 2 trades triggered: EURUSD, USDCHF, both lost. Results after 31 trades: -5R. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#331](/thread/post/13873148#post13873148 "Post Permalink")

  * Jan 27, 2022 4:20pm  Jan 27, 2022 4:20pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar71675_5.gif) Alberto_Jazz](alberto_jazz)

  * Joined Jun 2008 | Status: Trader | [593 Posts](/search?do=process&provider=Member&searchuser=71675)

> [Quoting SwingMan](/thread/post/13872010#post13872010 "View Quoted Post")
> 
> Disliked
> 
> Wouldn't be bad to program if someone tests the idea and formulates a few rules.
> 
> Ignored

I seem fractal levels are not stored in buffers from MTF indicator, so I don't know how to recall them. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#332](/thread/post/13873170#post13873170 "Post Permalink")

  * Jan 27, 2022 4:50pm  Jan 27, 2022 4:50pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting Alberto_Jazz](/thread/post/13873148#post13873148 "View Quoted Post")
> 
> Disliked
> 
> {quote} I seem fractal levels are not stored in buffers from MTF indicator, so I don't know how to recall them.
> 
> Ignored

I don't understand the problem, this is not a question for a programmer...  
One can add to "init()" for better information:  

Inserted Code
    
    
    SetIndexLabel(0,"Fractal-UP");
    SetIndexLabel(1,"Fractal-DOWN");

and one has the values here anyway;  

Inserted Code
    
    
    UpBuffer[i] = iFractals(NULL,Fractal_Timeframe,1,iBarShift(NULL,Fractal_Timeframe,Time[i]));
    DoBuffer[i] = iFractals(NULL,Fractal_Timeframe,2,iBarShift(NULL,Fractal_Timeframe,Time[i]));

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#333](/thread/post/13874459#post13874459 "Post Permalink")

  * Jan 28, 2022 8:47am  Jan 28, 2022 8:47am 

  * [ graphium](graphium)

  * | Joined Jul 2020  | Status: Trader | [25 Posts](/search?do=process&provider=Member&searchuser=973679)

> [Quoting graphium](/thread/post/13872876#post13872876 "View Quoted Post")
> 
> Disliked
> 
> {quote}... Today's (day 5) results: 2 trades triggered: EURUSD, USDCHF, both lost. Results after 31 trades: -5R.
> 
> Ignored

Day 6 results: 10 trades triggered, 2 lost: CHFJPY, EURJPY, 8 winners: AUDUSD, NZDUSD, AUDJPY, USDCAD, GPBUSD, EURUSD, USDCHF, USDJPY,   
Results after 41 trades: +1R 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#334](/thread/post/13874692#post13874692 "Post Permalink")

  * Jan 28, 2022 4:24pm  Jan 28, 2022 4:24pm 

  * [ veslup](veslup)

  * | Joined Nov 2009  | Status: Trader | [141 Posts](/search?do=process&provider=Member&searchuser=124349)

> [Quoting SwingMan](/thread/post/13871424#post13871424 "View Quoted Post")
> 
> Disliked
> 
> {quote} Be sure to do a few evaluations in the backtest. This is how you realize that not all pairs go well like the EURUSD. I also did a few tests with the Optimization (for 6 months so that it runs faster), but that didn't help much either. I'll use an additional trick to calculate the levels, let's see if that helps.
> 
> Ignored

Hi SwingMan,  
  
I realize that after restart the EA clear all active position. Could you fix this problem to not delete and close already open positions and if possible to continue manage his positions. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#335](/thread/post/13874941#post13874941 "Post Permalink")

  * Jan 28, 2022 7:31pm  Jan 28, 2022 7:31pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting veslup](/thread/post/13874692#post13874692 "View Quoted Post")
> 
> Disliked
> 
> ...I realize that after restart the EA clear all active position. Could you fix this problem to not delete and close already open positions and if possible to continue manage his positions.
> 
> Ignored

OK, you mean the pending orders intraday? 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#336](/thread/post/13874988#post13874988 "Post Permalink")

  * Jan 28, 2022 8:13pm  Jan 28, 2022 8:13pm 

  * [ dr.butze](dr.butze)

  * | Joined Jun 2020  | Status: Trader | [165 Posts](/search?do=process&provider=Member&searchuser=965218)

Yesterday evening (MEZ) i started the EA with a demo acc. 1.000 USD - all 28 pairs - standard set.  
Actuall Balance 1.074 USD   
  
Thank You!!!! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#337](/thread/post/13875405#post13875405 "Post Permalink")

  * Jan 29, 2022 12:37am  Jan 29, 2022 12:37am 

  * [ veslup](veslup)

  * | Joined Nov 2009  | Status: Trader | [141 Posts](/search?do=process&provider=Member&searchuser=124349)

> [Quoting SwingMan](/thread/post/13874941#post13874941 "View Quoted Post")
> 
> Disliked
> 
> {quote} OK, you mean the pending orders intraday?
> 
> Ignored

Yes that correct. Also if I have another open positions from myself and activate EA immediately closing all of them. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#338](/thread/post/13876344#post13876344 "Post Permalink")

  * Jan 30, 2022 10:29pm  Jan 30, 2022 10:29pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting veslup](/thread/post/13874692#post13874692 "View Quoted Post")
> 
> Disliked
> 
> ... I realize that after restart the EA clear all active position.
> 
> Ignored

New version of Expert Advisor**"smBodySwitch EA_v1.6"**  
  
I hope that the error has been fixed.  
  
Added a parameter (Enable_StealthTrading=true/false) so that for many pairs not all pending orders are sent, because only a part of them are executed.  
Please test and let me know if this helps. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: StealthTrading.PNG
Size: 2 KB](/attachment/image/4133708/thumbnail?d=1643548923)](/attachment/image/4133708?d=1643548923)   

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [smBodySwitch EA_v1.6.ex4](/attachment/file/4133707?d=1643548918) 85 KB | 355 downloads 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#339](/thread/post/13876591#post13876591 "Post Permalink")

  * Jan 31, 2022 9:03am  Jan 31, 2022 9:03am 

  * [ graphium](graphium)

  * | Joined Jul 2020  | Status: Trader | [25 Posts](/search?do=process&provider=Member&searchuser=973679)

> [Quoting graphium](/thread/post/13874459#post13874459 "View Quoted Post")
> 
> Disliked
> 
> {quote} Day 6 results: 10 trades triggered, 2 lost: CHFJPY, EURJPY, 8 winners: AUDUSD, NZDUSD, AUDJPY, USDCAD, GPBUSD, EURUSD, USDCHF, USDJPY, Results after 41 trades: +1R
> 
> Ignored

Friday's results 3 wins: AUDUSD, NZDUSD, AUDJPY, 3 loses: USDJPY, USDCAD, EURGBP.  
Total after 47 trades: +1R 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#340](/thread/post/13876797#post13876797 "Post Permalink")

  * Jan 31, 2022 3:32pm  Jan 31, 2022 3:32pm 

  * [ veslup](veslup)

  * | Joined Nov 2009  | Status: Trader | [141 Posts](/search?do=process&provider=Member&searchuser=124349)

> [Quoting SwingMan](/thread/post/13876344#post13876344 "View Quoted Post")
> 
> Disliked
> 
> {quote} New version of Expert Advisor "smBodySwitch EA_v1.6" I hope that the error has been fixed. Added a parameter (Enable_StealthTrading=true/false) so that for many pairs not all pending orders are sent, because only a part of them are executed. Please test and let me know if this helps. {file} {image}
> 
> Ignored

The same story. For example I have opened by hand position on EURUSD. When I upload SM EA 1.6 on EURUSD immediately delete my hand open position.   
Also on same platform working another EA together with SM EA 1.6 when another EA open positions SM EA 1.6 immediately closed all of them. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * LazyHedging Trading Ideas
  *   * [ **Reply to Thread** ](/thread/1058948-lazyhedging-trading-ideas/reply#reply)

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

[EurCad Analysis and Trading Ideas](/thread/360980-eurcad-analysis-and-trading-ideas "Hello my friends. 
 
As of lately I have had remarkable success in trading EurCad and after hearing other traders ideas I decided that we...") 594 replies

[FSP Trading Journal and Trend Ideas](/thread/427493-fsp-trading-journal-and-trend-ideas "hello  
I am trying to post some of my trade Ideas here. 
there will be trend following and counter trend trades. 
I will post image rather...") 16 replies

[Forex trading platform that doesn't take your ideas](/thread/311080-forex-trading-platform-that-doesnt-take-your-ideas "Ninja trader, Metatrader, Tradestation all can copy the EA and indicators straight out of your PC. 
 
How do we go about developing a...") 11 replies

[Program Your Trading Ideas without being a programmer](/thread/225629-program-your-trading-ideas-without-being-a-programmer "I have to admit, I have a lot of trading ideas, but no programming skills. I hate paying a programmer to take 3 days to write an EA for me,...") 4 replies

[Exchanging trading ideas](/thread/136764-exchanging-trading-ideas "I'm opening this thread as a substitute for live chat like msn etc to exchange trading ideas and to filter of some posts at Igrok's thread,...") 37 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/1058948-lazyhedging-trading-ideas/reply#reply)
  * Subscribe
  * [271](javascript:void\(0\);)

Attachments: LazyHedging Trading Ideas

Tags: LazyHedging Trading Ideas

#  [](/thread/1058948-lazyhedging-trading-ideas)LazyHedging Trading Ideas 

  * 

  * [#341](/thread/post/13876918#post13876918 "Post Permalink")

  * Jan 31, 2022 5:57pm  Jan 31, 2022 5:57pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting veslup](/thread/post/13876797#post13876797 "View Quoted Post")
> 
> Disliked
> 
> ...The same story. For example I have opened by hand position on EURUSD. When I upload SM EA 1.6 on EURUSD immediately delete my hand open position. Also on same platform working another EA together with SM EA 1.6 when another EA open positions SM EA 1.6 immediately closed all of them.
> 
> Ignored

Were the opened orders pending or active orders?  
  
I actually deleted existing pending orders, but not active orders, I forgot to check the MagicNumber... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#342](/thread/post/13876971#post13876971 "Post Permalink")

  * Jan 31, 2022 6:39pm  Jan 31, 2022 6:39pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting veslup](/thread/post/13876797#post13876797 "View Quoted Post")
> 
> Disliked
> 
> ...Also on same platform working another EA together with SM EA 1.6 when another EA open positions SM EA 1.6 immediately closed all of them.
> 
> Ignored

I hope to have fixed the error.  
  
**Generation 3** , with a hopefully better adjustment of the limits to the volatility.   
  
Indicator:**"smBodySwitch Signals_v3.1"**   
  
ExpertAdvisor:**"smBodySwitch EA_v3.1"**

Attached Image (click to enlarge)

[![Click to Enlarge

Name: BodySwitch 3_1-EURCAD.PNG
Size: 42 KB](/attachment/image/4134135/thumbnail?d=1643621936)](/attachment/image/4134135?d=1643621936)   

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [smBodySwitch EA_v3.1.ex4](/attachment/file/4134136?d=1643621938) 88 KB | 409 downloads 

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [smBodySwitch Signals_v3.1.ex4](/attachment/file/4134137?d=1643621941) 81 KB | 495 downloads 

[0 ](javascript:void\(0\);) [4 ](javascript:void\(0\);)

  * [#343](/thread/post/13876984#post13876984 "Post Permalink")

  * Jan 31, 2022 6:58pm  Jan 31, 2022 6:58pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

As far as I can see nobody has done any tests with historical data.  
I examined the majors over the weekend and it would be advisable to set "maxTrades=1" so as not to strain capital with the martingale. 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: Tester EURJPY.PNG
Size: 61 KB](/attachment/image/4134147/thumbnail?d=1643623090)](/attachment/image/4134147?d=1643623090)   
[![Click to Enlarge

Name: Tester EURUSD.PNG
Size: 61 KB](/attachment/image/4134148/thumbnail?d=1643623093)](/attachment/image/4134148?d=1643623093)   
[![Click to Enlarge

Name: Tester GBPUSD.PNG
Size: 62 KB](/attachment/image/4134149/thumbnail?d=1643623094)](/attachment/image/4134149?d=1643623094)   
[![Click to Enlarge

Name: Tester USDCAD.PNG
Size: 62 KB](/attachment/image/4134150/thumbnail?d=1643623096)](/attachment/image/4134150?d=1643623096)   
[![Click to Enlarge

Name: Tester USDJPY.PNG
Size: 61 KB](/attachment/image/4134151/thumbnail?d=1643623097)](/attachment/image/4134151?d=1643623097)   

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#344](/thread/post/13876990#post13876990 "Post Permalink")

  * Jan 31, 2022 7:03pm  Jan 31, 2022 7:03pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

Here is a result for (maximTrades=3), where one need a little more capital to not exceed the margin.  
  
There are still small discrepancies with the martingales, maybe I'll make some adjustments in the future. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Tester EURUSD-3trades.PNG
Size: 61 KB](/attachment/image/4134156/thumbnail?d=1643623427)](/attachment/image/4134156?d=1643623427)   

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#345](/thread/post/13877604#post13877604 "Post Permalink")

  * Feb 1, 2022 1:57am  Feb 1, 2022 1:57am 

  * [ veslup](veslup)

  * | Joined Nov 2009  | Status: Trader | [141 Posts](/search?do=process&provider=Member&searchuser=124349)

> [Quoting SwingMan](/thread/post/13876918#post13876918 "View Quoted Post")
> 
> Disliked
> 
> {quote} Were the opened orders pending or active orders? I actually deleted existing pending orders, but not active orders, I forgot to check the MagicNumber...
> 
> Ignored

I mean the active trades. If there are active trades EA immediately closing another one. Can you see on picture I have another EA and hi try to open position but they are closed immediately from SM EA 1.6.  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 48 KB](/attachment/image/4134500/thumbnail?d=1643648268)](/attachment/image/4134500?d=1643648268)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#346](/thread/post/13877644#post13877644 "Post Permalink")

  * Feb 1, 2022 2:25am  Feb 1, 2022 2:25am 

  * [ veslup](veslup)

  * | Joined Nov 2009  | Status: Trader | [141 Posts](/search?do=process&provider=Member&searchuser=124349)

> [Quoting SwingMan](/thread/post/13876971#post13876971 "View Quoted Post")
> 
> Disliked
> 
> {quote} I hope to have fixed the error. Generation 3, with a hopefully better adjustment of the limits to the volatility. Indicator: "smBodySwitch Signals_v3.1" ExpertAdvisor: "smBodySwitch EA_v3.1" {image} {file} {file}
> 
> Ignored

Looks like with new version you fix this problems. I opened position by hand and SM EA 3.1 did not delete. Very nice.  
Thank you.  
Tomorrow will test wit another EA I hope will be keep all together. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#347](/thread/post/13877645#post13877645 "Post Permalink")

  * Feb 1, 2022 2:25am  Feb 1, 2022 2:25am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting veslup](/thread/post/13877604#post13877604 "View Quoted Post")
> 
> Disliked
> 
> ...I mean the active trades. If there are active trades EA immediately closing another one. Can you see on picture I have another EA and hi try to open position but they are closed immediately from SM EA 1.6.
> 
> Ignored

OK, in Post #342 you see that with version 3.1 I sended first a pending and a market order (0.01 lots), and after loading the EA the orders remains undeleted. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#348](/thread/post/13877924#post13877924 "Post Permalink")

  * Feb 1, 2022 5:40am  Feb 1, 2022 5:40am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting graphium](/thread/post/13867457#post13867457 "View Quoted Post")
> 
> Disliked
> 
> ...I am trying to check first if there is an edge in your system of entries and exits on its own...
> 
> Ignored

Maybe yes, Maybe no, one must test.  
  
Here is an interesting profit curve for EURCAD between February-2018 and January-2022. The lots are calculated with the AccountBalance, with 1% risk, without martingale. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Tester EURCAD-4years.PNG
Size: 62 KB](/attachment/image/4134667/thumbnail?d=1643661633)](/attachment/image/4134667?d=1643661633)   

[0 ](javascript:void\(0\);) [3 ](javascript:void\(0\);)

  * [#349](/thread/post/13877963#post13877963 "Post Permalink")

  * Feb 1, 2022 6:09am  Feb 1, 2022 6:09am 

  * [ veslup](veslup)

  * | Joined Nov 2009  | Status: Trader | [141 Posts](/search?do=process&provider=Member&searchuser=124349)

> [Quoting SwingMan](/thread/post/13877924#post13877924 "View Quoted Post")
> 
> Disliked
> 
> {quote} Maybe yes, Maybe no, one must test. Here is an interesting profit curve for EURCAD between February-2018 and January-2022. The lots are calculated with the AccountBalance, with 1% risk, without martingale. {image}
> 
> Ignored

Actually I am testing on real account with real money. The problem is that on real account the spread is quite different from demo account and I cannot trade so much currencies compare with demo account. But any way I will try. I see that in the new version 3.1 EA closed all pending orders in 22:00 Hrs. Will be good if possible as options to activate the new orders next day by himself let say 01:00 Hrs. because before 01:00 usually are very high and after that the [spreads](/brokers/spreads "View Live Spreads on the Broker Guide") going down. If that is possible I will leave to working withhold need to wake up to arrange again for new day. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#350](/thread/post/13877987#post13877987 "Post Permalink")

  * Edited 6:37pm  Feb 1, 2022 6:33am | Edited 6:37pm 

  * [ dr.butze](dr.butze)

  * | Joined Jun 2020  | Status: Trader | [165 Posts](/search?do=process&provider=Member&searchuser=965218)

Today the martingale crashed the demo. Too many pairs…  
which pairs are you @veslup trading live with this EA? Swingmans Testing of the majors without martingale Looks promising. Unfortenatly im Not really familiar with testing - so i use demo accounts.  
  
@swingman i saw, that you created a explorer - which pairs are you going to Trade with it? - > edit: now I can see that on the explorer - please excuse this question ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
  
thank you!! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#351](/thread/post/13878075#post13878075 "Post Permalink")

  * Feb 1, 2022 9:30am  Feb 1, 2022 9:30am 

  * [ graphium](graphium)

  * | Joined Jul 2020  | Status: Trader | [25 Posts](/search?do=process&provider=Member&searchuser=973679)

> [Quoting graphium](/thread/post/13876591#post13876591 "View Quoted Post")
> 
> Disliked
> 
> {quote} Friday's results 3 wins: AUDUSD, NZDUSD, AUDJPY, 3 loses: USDJPY, USDCAD, EURGBP. Total after 47 trades: +1R
> 
> Ignored

Monday's results: 1 trade 1 loss: USDCHF, after 48 trades i am at 0R 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#352](/thread/post/13878318#post13878318 "Post Permalink")

  * Feb 1, 2022 5:00pm  Feb 1, 2022 5:00pm 

  * [ veslup](veslup)

  * | Joined Nov 2009  | Status: Trader | [141 Posts](/search?do=process&provider=Member&searchuser=124349)

> [Quoting dr.butze](/thread/post/13877987#post13877987 "View Quoted Post")
> 
> Disliked
> 
> Today the martingale crashed the demo. Too many pairs… which pairs are you @veslup trading live with this EA? Swingmans Testing of the majors without martingale Looks promising. Unfortenatly im Not really familiar with testing - so i use demo accounts. @swingman i saw, that you created a explorer - which pairs are you going to Trade with it? thank you!!
> 
> Ignored

Please find attached my real account pairs. I am trading with 0 - max trades.  
  

Attached Image

![](/attachment/image/4134939?d=1643702253)

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#353](/thread/post/13878335#post13878335 "Post Permalink")

  * Feb 1, 2022 5:09pm  Feb 1, 2022 5:09pm 

  * [ veslup](veslup)

  * | Joined Nov 2009  | Status: Trader | [141 Posts](/search?do=process&provider=Member&searchuser=124349)

> [Quoting SwingMan](/thread/post/13876971#post13876971 "View Quoted Post")
> 
> Disliked
> 
> {quote} I hope to have fixed the error. Generation 3, with a hopefully better adjustment of the limits to the volatility. Indicator: "smBodySwitch Signals_v3.1" ExpertAdvisor: "smBodySwitch EA_v3.1" {image} {file} {file}
> 
> Ignored

Hi Swing Man,  
The new version 3.1 working perfecto together wit another EA and don't closing other position.  
Thanks allot once again. Great job. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#354](/thread/post/13878349#post13878349 "Post Permalink")

  * Feb 1, 2022 5:18pm  Feb 1, 2022 5:18pm 

  * [ dr.butze](dr.butze)

  * | Joined Jun 2020  | Status: Trader | [165 Posts](/search?do=process&provider=Member&searchuser=965218)

> [Quoting veslup](/thread/post/13878318#post13878318 "View Quoted Post")
> 
> Disliked
> 
> {quote} Please find attached my real account pairs. I am trading with 0 - max trades. {image}
> 
> Ignored

thank you very much!! That means all other settings you have left on default - except max trades?  
Thank you and many green pips for you 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#355](/thread/post/13878438#post13878438 "Post Permalink")

  * Feb 1, 2022 6:21pm  Feb 1, 2022 6:21pm 

  * [ veslup](veslup)

  * | Joined Nov 2009  | Status: Trader | [141 Posts](/search?do=process&provider=Member&searchuser=124349)

> [Quoting dr.butze](/thread/post/13878349#post13878349 "View Quoted Post")
> 
> Disliked
> 
> {quote} thank you very much!! That means all other settings you have left on default - except max trades? Thank you and many green pips for you
> 
> Ignored

That is my setting. Money management according to my account.  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 51 KB](/attachment/image/4134991/thumbnail?d=1643707176)](/attachment/image/4134991?d=1643707176)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#356](/thread/post/13878464#post13878464 "Post Permalink")

  * Feb 1, 2022 6:36pm  Feb 1, 2022 6:36pm 

  * [ dr.butze](dr.butze)

  * | Joined Jun 2020  | Status: Trader | [165 Posts](/search?do=process&provider=Member&searchuser=965218)

> [Quoting veslup](/thread/post/13878438#post13878438 "View Quoted Post")
> 
> Disliked
> 
> {quote} That is my setting. Money management according to my account. {image}
> 
> Ignored

thank you very much!! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#357](/thread/post/13879547#post13879547 "Post Permalink")

  * Feb 2, 2022 7:26am  Feb 2, 2022 7:26am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting veslup](/thread/post/13877963#post13877963 "View Quoted Post")
> 
> Disliked
> 
> Will be good if possible as options to activate the new orders next day by himself let say 01:00 Hrs. because before 01:00 usually are very high and after that the spreads going down. If that is possible I will leave to working withhold need to wake up to arrange again for new day.
> 
> Ignored

I just checked the orders at midnight.  
They look awful because of the spreads, you're right, and I also wanted to shift the starting hour by 2-3 hours.  
  
**But try to set the stealth mode, is a very good solution.**  
(I just did that!)  
Don't forget what I wrote sometime earlier, that the levels are calculated with bid prices.  
  
This is how one also tests its functionality. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#358](/thread/post/13879575#post13879575 "Post Permalink")

  * Feb 2, 2022 8:23am  Feb 2, 2022 8:23am 

  * [ graphium](graphium)

  * | Joined Jul 2020  | Status: Trader | [25 Posts](/search?do=process&provider=Member&searchuser=973679)

> [Quoting graphium](/thread/post/13878075#post13878075 "View Quoted Post")
> 
> Disliked
> 
> {quote} Monday's results: 1 trade 1 loss: USDCHF, after 48 trades i am at 0R
> 
> Ignored

Tuesday's results 2 trades taken, 1 won: EURUSD, 1 lost AUDUSD. Overall after 50 trades I am at BE 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#359](/thread/post/13879762#post13879762 "Post Permalink")

  * Feb 2, 2022 2:48pm  Feb 2, 2022 2:48pm 

  * [ budidharma19](budidharma19)

  * | Joined Aug 2013  | Status: Trader | [214 Posts](/search?do=process&provider=Member&searchuser=347146)

> [Quoting SwingMan](/thread/post/13877924#post13877924 "View Quoted Post")
> 
> Disliked
> 
> {quote} Maybe yes, Maybe no, one must test. Here is an interesting profit curve for EURCAD between February-2018 and January-2022. The lots are calculated with the AccountBalance, with 1% risk, without martingale. {image}
> 
> Ignored

Hello SWINGMAN,  
  
How are you ?  
I am watching and reading the thread,... until this BACKTEST result out here.  
I try with ICMarkets,.. I dont think its different a lot,.. but the result cannot match yours,..  
  
Kindly post your set file please, so we can double check without the hassle.   
  
I have also DUKASCOPY data at home,.. I will upload here after check with your set file.  
  
Thanks in advance,   
  
Cheers,  
  
Budi 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#360](/thread/post/13879903#post13879903 "Post Permalink")

  * Feb 2, 2022 4:52pm  Feb 2, 2022 4:52pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting budidharma19](/thread/post/13879762#post13879762 "View Quoted Post")
> 
> Disliked
> 
> ...Kindly post your set file please, so we can double check without the hassle. I have also DUKASCOPY data at home,.. I will upload here after check with your set file. Thanks in advance, Cheers, Budi
> 
> Ignored

But you have the setup in the picture.  
  
Specific are only  
maximTrades=1  
reference_Account=Balance  
Initial deposit=5000 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Setup v3.1.PNG
Size: 23 KB](/attachment/image/4135743/thumbnail?d=1643788322)](/attachment/image/4135743?d=1643788322)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * LazyHedging Trading Ideas
  *   * [ **Reply to Thread** ](/thread/1058948-lazyhedging-trading-ideas/reply#reply)

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

[EurCad Analysis and Trading Ideas](/thread/360980-eurcad-analysis-and-trading-ideas "Hello my friends. 
 
As of lately I have had remarkable success in trading EurCad and after hearing other traders ideas I decided that we...") 594 replies

[FSP Trading Journal and Trend Ideas](/thread/427493-fsp-trading-journal-and-trend-ideas "hello  
I am trying to post some of my trade Ideas here. 
there will be trend following and counter trend trades. 
I will post image rather...") 16 replies

[Forex trading platform that doesn't take your ideas](/thread/311080-forex-trading-platform-that-doesnt-take-your-ideas "Ninja trader, Metatrader, Tradestation all can copy the EA and indicators straight out of your PC. 
 
How do we go about developing a...") 11 replies

[Program Your Trading Ideas without being a programmer](/thread/225629-program-your-trading-ideas-without-being-a-programmer "I have to admit, I have a lot of trading ideas, but no programming skills. I hate paying a programmer to take 3 days to write an EA for me,...") 4 replies

[Exchanging trading ideas](/thread/136764-exchanging-trading-ideas "I'm opening this thread as a substitute for live chat like msn etc to exchange trading ideas and to filter of some posts at Igrok's thread,...") 37 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/1058948-lazyhedging-trading-ideas/reply#reply)
  * Subscribe
  * [271](javascript:void\(0\);)

Attachments: LazyHedging Trading Ideas

Tags: LazyHedging Trading Ideas

#  [](/thread/1058948-lazyhedging-trading-ideas)LazyHedging Trading Ideas 

  * 

  * [#361](/thread/post/13880288#post13880288 "Post Permalink")

  * Feb 2, 2022 9:44pm  Feb 2, 2022 9:44pm 

  * [ budidharma19](budidharma19)

  * | Joined Aug 2013  | Status: Trader | [214 Posts](/search?do=process&provider=Member&searchuser=347146)

> [Quoting SwingMan](/thread/post/13879903#post13879903 "View Quoted Post")
> 
> Disliked
> 
> {quote} But you have the setup in the picture. Specific are only maximTrades=1 reference_Account=Balance Initial deposit=5000 {image}
> 
> Ignored

Dear SWINGMAN,  
  
Glad to have your reply,... YES ,, I havethat setting CLEAR.  
  
But the problem,.. your EA have 2 different "spectacular" result when I backtesting between "Every Tick" and "Control Point".  
  
I am using DUKASCOPY tickdata.  
  
Below I report to you the result : 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 66 KB](/attachment/image/4135944/thumbnail?d=1643805886)](/attachment/image/4135944?d=1643805886)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#362](/thread/post/13880294#post13880294 "Post Permalink")

  * Feb 2, 2022 9:47pm  Feb 2, 2022 9:47pm 

  * [ budidharma19](budidharma19)

  * | Joined Aug 2013  | Status: Trader | [214 Posts](/search?do=process&provider=Member&searchuser=347146)

Here are the result with "Control Point" 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 66 KB](/attachment/image/4135947/thumbnail?d=1643806033)](/attachment/image/4135947?d=1643806033)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#363](/thread/post/13880299#post13880299 "Post Permalink")

  * Feb 2, 2022 9:49pm  Feb 2, 2022 9:49pm 

  * [ budidharma19](budidharma19)

  * | Joined Aug 2013  | Status: Trader | [214 Posts](/search?do=process&provider=Member&searchuser=347146)

Normally, "BOTH" method only different by very little ,.. because I am using TICKDATA.  
  
May be as a Senior programmer, you will find the bug.  
  
Here are my backtesting Setting panel : 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 33 KB](/attachment/image/4135953/thumbnail?d=1643806192)](/attachment/image/4135953?d=1643806192)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#364](/thread/post/13880680#post13880680 "Post Permalink")

  * Feb 3, 2022 1:18am  Feb 3, 2022 1:18am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting budidharma19](/thread/post/13880299#post13880299 "View Quoted Post")
> 
> Disliked
> 
> Normally, "BOTH" method only different by very little ,.. because I am using TICKDATA. May be as a Senior programmer, you will find the bug.
> 
> Ignored

Unfortunately I have no explanation regarding the tests.  
  
I did the same test with Spread=11 as you did. The equity curve is the same as before (with a spread of 2), only the profit is correspondingly smaller.  
Probably because my data is not quite correct, my tester works in the same way as yours in the second evaluation.  
  
I will run the evaluation for 9 pairs this month, and if it ends up with a minus value, program something else... 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Tester EURCAD-4years-Spread11.PNG
Size: 63 KB](/attachment/image/4136140/thumbnail?d=1643818733)](/attachment/image/4136140?d=1643818733)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#365](/thread/post/13881135#post13881135 "Post Permalink")

  * Feb 3, 2022 9:43am  Feb 3, 2022 9:43am 

  * [ graphium](graphium)

  * | Joined Jul 2020  | Status: Trader | [25 Posts](/search?do=process&provider=Member&searchuser=973679)

> [Quoting graphium](/thread/post/13879575#post13879575 "View Quoted Post")
> 
> Disliked
> 
> {quote} Tuesday's results 2 trades taken, 1 won: EURUSD, 1 lost AUDUSD. Overall after 50 trades I am at BE
> 
> Ignored

Wednesday's results: 3 loses: EURUSD, USDCHF, USDCAD, 1 win: GBPUSD. -2R after 54 trades.  
All trades were taken on demo account, set and triggered by pending orders submitted at midnight at the beginning of the daily candle. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#366](/thread/post/13881707#post13881707 "Post Permalink")

  * Feb 3, 2022 8:41pm  Feb 3, 2022 8:41pm 

  * [ veslup](veslup)

  * | Joined Nov 2009  | Status: Trader | [141 Posts](/search?do=process&provider=Member&searchuser=124349)

> [Quoting SwingMan](/thread/post/13879903#post13879903 "View Quoted Post")
> 
> Disliked
> 
> {quote} But you have the setup in the picture. Specific are only maximTrades=1 reference_Account=Balance Initial deposit=5000 {image}
> 
> Ignored

Hi Swing Man,  
  
Can you check there are entry value discrepancy between EA and Indicator.   
Here USDCAD entry value left corner is 1.04024 and as per EA should be 1.27138 and down in right corner already have profit 83 pt but the order still not yet open.  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 109 KB](/attachment/image/4136737/thumbnail?d=1643888239)](/attachment/image/4136737?d=1643888239)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#367](/thread/post/13881881#post13881881 "Post Permalink")

  * Feb 3, 2022 10:09pm  Feb 3, 2022 10:09pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting veslup](/thread/post/13881707#post13881707 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi Swing Man, Can you check there are entry value discrepancy between EA and Indicator. Here USDCAD entry value left corner is 1.04024 and as per EA should be 1.27138 and down in right corner already have profit 83 pt but the order still not yet open. {image}
> 
> Ignored

There will always be small differences between indicator and EA.  
Only if it is worth using the EA will I invest more time to put everything in order.  
  
Now I've found a big bug and I'm working at the stop and start +-3 hours from midnight.  
With you I see USDCHF in the chart and not USDCAD as you wrote. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#368](/thread/post/13882370#post13882370 "Post Permalink")

  * Edited 7:30am  Feb 4, 2022 1:16am | Edited 7:30am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting SwingMan](/thread/post/13881881#post13881881 "View Quoted Post")
> 
> Disliked
> 
> ...and I'm working at the stop and start +-3 hours from midnight.
> 
> Ignored

This is necessary because for your USDCHF the spread at 00:15 was 187 points, far over the calculated entry and WinPoints=83.  
At 13:34 the spread was 10 points!  
  
Such comments need I to make the EA better. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#369](/thread/post/13885451#post13885451 "Post Permalink")

  * Edited 4:41am  Feb 7, 2022 4:24am | Edited 4:41am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

New Expert Advisor version **"smBodySwitch EA_v3.2"**  
  
\- No orders between 21:00 and 03:00  
\- Some bugs fixed  
  
\- The background of the charts changes for active trades (Buy/Sell).  
  
A new script **"smApplayTemplate AllCharts"**  
with which one can assign a template in all charts of the workspace. This is helpful to save a lot of time.  
I have now started the Trade Explorer with 28 pairs, leverage 1:500. The parameter (maxTrades=7), let's see what happens. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: List of 28 pairs.PNG
Size: 6 KB](/attachment/image/4138625/thumbnail?d=1644173157)](/attachment/image/4138625?d=1644173157)   

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [smBodySwitch EA_v3.2.ex4](/attachment/file/4138623?d=1644173023) 95 KB | 438 downloads 

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [smApplayTemplate AllCharts.ex4](/attachment/file/4138624?d=1644173031) 7 KB | 469 downloads 

[0 ](javascript:void\(0\);) [8 ](javascript:void\(0\);)

  * [#370](/thread/post/13885473#post13885473 "Post Permalink")

  * Feb 7, 2022 4:55am  Feb 7, 2022 4:55am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar472073_2.gif) ordosgoitia](ordosgoitia)

  * Joined Jun 2016 | Status: Trader | [268 Posts](/search?do=process&provider=Member&searchuser=472073)

> [Quoting SwingMan](/thread/post/13885451#post13885451 "View Quoted Post")
> 
> Disliked
> 
> New Expert Advisor version "smBodySwitch EA_v3.2" - No orders between 21:00 and 03:00 - Some bugs fixed - The background of the charts changes for active trades (Buy/Sell). A new script "smApplayTemplate AllCharts" with which one can assign a template in all charts of the workspace. This is helpful to save a lot of time. I have now started the Trade Explorer with 28 pairs, leverage 1:500. The parameter (maxTrades=7), let's see what happens. {file} {file} {image}
> 
> Ignored

Great Work Swingman  
I will do foward testing 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#371](/thread/post/13885474#post13885474 "Post Permalink")

  * Edited 9:38pm  Feb 7, 2022 4:56am | Edited 9:38pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

Hi Alberto,  
watch out for the capital in testing if you test several pairs!  
  
With [FxPro](/brokers/fxpro "View FxPro Broker Profile") you have leverage 1:30.  
  
Margin for a pair is: Margin=Lots*(100,000/30)=Lots*3,333  
For 0.3 lots you need also $1,000 margin.  
  
At leverage 1:500, Margin=Lots*200, and for 0.3 lots you need $60 margin.  
  
In the test on EURUSD with 7 levels I used once in the year 7.5 lots.  
The margin would have been $1,500, so I bet $10,000 on Trade Explorer for that reason. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#372](/thread/post/13886553#post13886553 "Post Permalink")

  * Feb 7, 2022 10:18pm  Feb 7, 2022 10:18pm 

  * [ graphium](graphium)

  * | Joined Jul 2020  | Status: Trader | [25 Posts](/search?do=process&provider=Member&searchuser=973679)

> [Quoting graphium](/thread/post/13881135#post13881135 "View Quoted Post")
> 
> Disliked
> 
> {quote} Wednesday's results: 3 loses: EURUSD, USDCHF, USDCAD, 1 win: GBPUSD. -2R after 54 trades. All trades were taken on demo account, set and triggered by pending orders submitted at midnight at the beginning of the daily candle.
> 
> Ignored

My last week Thursday's results are 5 wins, 4 losses, so ended up at -1R after 63 trades. I have decided to pause testing this system with original settings on live market for now and I will try to look into the trend-following idea SwingMan mentioned earlier. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#373](/thread/post/13886713#post13886713 "Post Permalink")

  * Feb 7, 2022 11:43pm  Feb 7, 2022 11:43pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting graphium](/thread/post/13886553#post13886553 "View Quoted Post")
> 
> Disliked
> 
> {...I have decided to pause testing this system with original settings on live market for now and I will try to look into the trend-following idea SwingMan mentioned earlier.
> 
> Ignored

You shall never test an EA live again, until the author gives you written confirmation that the program is running error free! 

[0 ](javascript:void\(0\);) [3 ](javascript:void\(0\);)

  * [#374](/thread/post/13886842#post13886842 "Post Permalink")

  * Feb 8, 2022 12:54am  Feb 8, 2022 12:54am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

I stopped the TradeExplorer because the ReverseOrder was not executed for AUDNZD and also the TrailingStop is not displayed correctly.  
  
Now I have to find the causes. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#375](/thread/post/13887123#post13887123 "Post Permalink")

  * Feb 8, 2022 3:58am  Feb 8, 2022 3:58am 

  * [ graphium](graphium)

  * | Joined Jul 2020  | Status: Trader | [25 Posts](/search?do=process&provider=Member&searchuser=973679)

> [Quoting SwingMan](/thread/post/13886713#post13886713 "View Quoted Post")
> 
> Disliked
> 
> You shall never test an EA live again, until the author gives you written confirmation that the program is running error free!
> 
> Ignored

For clarification, I have newer used your EA (only indicator). As I mentioned earlier I was trying to test if there is an edge in your system entries and exists on its own based on what your indicator showed at the begining of new daily candle. All the trades were set up via pending orders and traded on demo account (we have already discussed this couple pages back !?)  
  

> [Quoting SwingMan](/thread/post/13867509#post13867509 "View Quoted Post")
> 
> Disliked
> 
> Very good, when you're done the checking, please let us know..
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#376](/thread/post/13887291#post13887291 "Post Permalink")

  * Feb 8, 2022 6:58am  Feb 8, 2022 6:58am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting graphium](/thread/post/13887123#post13887123 "View Quoted Post")
> 
> Disliked
> 
> ...For clarification, I have newer used your EA (only indicator).
> 
> Ignored

OK, I forgot about that. Then I'm not responsible for what you do, nor do I take part in the profits... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#377](/thread/post/13889133#post13889133 "Post Permalink")

  * Feb 9, 2022 9:42am  Feb 9, 2022 9:42am 

  * [ budidharma19](budidharma19)

  * | Joined Aug 2013  | Status: Trader | [214 Posts](/search?do=process&provider=Member&searchuser=347146)

Dear SwingMan,  
  
Thanks for the V 3.2 --> anyway I try to backtesting this version,...  
  
Lets see what will happened.  
  
Cheers,  
  
Budi 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#378](/thread/post/13889538#post13889538 "Post Permalink")

  * Feb 9, 2022 6:01pm  Feb 9, 2022 6:01pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

New ExpertAdvisor version**"smBodySwitch EA_v3.3"**  
  
\- Some corrections and adjustments were made.  
  
\- Workspace with 28 pairs and 2 dummys.  
  
Right now there are three pending orders activated. This is only done near the entry levels so that one does not send 28 pending orders at once, and many are not activated later. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Workspace BodySwitch 3.3.png
Size: 196 KB](/attachment/image/4140856/thumbnail?d=1644397241)](/attachment/image/4140856?d=1644397241)   

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [smBodySwitch EA_v3.3.ex4](/attachment/file/4140857?d=1644397249) 100 KB | 368 downloads 

[0 ](javascript:void\(0\);) [3 ](javascript:void\(0\);)

  * [#379](/thread/post/13889591#post13889591 "Post Permalink")

  * Feb 9, 2022 6:52pm  Feb 9, 2022 6:52pm 

  * [ budidharma19](budidharma19)

  * | Joined Aug 2013  | Status: Trader | [214 Posts](/search?do=process&provider=Member&searchuser=347146)

> [Quoting SwingMan](/thread/post/13889538#post13889538 "View Quoted Post")
> 
> Disliked
> 
> New ExpertAdvisor version "smBodySwitch EA_v3.3" - Some corrections and adjustments were made. - Workspace with 28 pairs and 2 dummys. Right now there are three pending orders activated. This is only done near the entry levels so that one does not send 28 pending orders at once, and many are not activated later. {image} {file}
> 
> Ignored

Dear SwingMan,  
  
Congratulations,....  
  
May you share us the setting you use ?  
  
Best Regards,  
  
Budi 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#380](/thread/post/13889651#post13889651 "Post Permalink")

  * Feb 9, 2022 7:38pm  Feb 9, 2022 7:38pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting budidharma19](/thread/post/13889591#post13889591 "View Quoted Post")
> 
> Disliked
> 
> ...May you share us the setting you use ?
> 
> Ignored

It's the default settings because I load the EA directly and don't want to make any changes.  
Later when I do any tests I might make adjustments for certain pairs.  
  
So far have found in the tester that the default values are satisfactory. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * LazyHedging Trading Ideas
  *   * [ **Reply to Thread** ](/thread/1058948-lazyhedging-trading-ideas/reply#reply)

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

[EurCad Analysis and Trading Ideas](/thread/360980-eurcad-analysis-and-trading-ideas "Hello my friends. 
 
As of lately I have had remarkable success in trading EurCad and after hearing other traders ideas I decided that we...") 594 replies

[FSP Trading Journal and Trend Ideas](/thread/427493-fsp-trading-journal-and-trend-ideas "hello  
I am trying to post some of my trade Ideas here. 
there will be trend following and counter trend trades. 
I will post image rather...") 16 replies

[Forex trading platform that doesn't take your ideas](/thread/311080-forex-trading-platform-that-doesnt-take-your-ideas "Ninja trader, Metatrader, Tradestation all can copy the EA and indicators straight out of your PC. 
 
How do we go about developing a...") 11 replies

[Program Your Trading Ideas without being a programmer](/thread/225629-program-your-trading-ideas-without-being-a-programmer "I have to admit, I have a lot of trading ideas, but no programming skills. I hate paying a programmer to take 3 days to write an EA for me,...") 4 replies

[Exchanging trading ideas](/thread/136764-exchanging-trading-ideas "I'm opening this thread as a substitute for live chat like msn etc to exchange trading ideas and to filter of some posts at Igrok's thread,...") 37 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/1058948-lazyhedging-trading-ideas/reply#reply)
  * Subscribe
  * [271](javascript:void\(0\);)

Attachments: LazyHedging Trading Ideas

Tags: LazyHedging Trading Ideas

#  [](/thread/1058948-lazyhedging-trading-ideas)LazyHedging Trading Ideas 

  * 

  * [#381](/thread/post/13889739#post13889739 "Post Permalink")

  * Feb 9, 2022 8:48pm  Feb 9, 2022 8:48pm 

  * [ budidharma19](budidharma19)

  * | Joined Aug 2013  | Status: Trader | [214 Posts](/search?do=process&provider=Member&searchuser=347146)

> [Quoting SwingMan](/thread/post/13889651#post13889651 "View Quoted Post")
> 
> Disliked
> 
> {quote} It's the default settings because I load the EA directly and don't want to make any changes. Later when I do any tests I might make adjustments for certain pairs. So far have found in the tester that the default values are satisfactory.
> 
> Ignored

Dear SwingMan,  
  
DEFAULT setting means "maxim Trades = 10 ", "Reference_Account = Account Specified" ,  
  
or you change to other setting ?  
  
Thanks,  
  
Budi Dharma 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#382](/thread/post/13889763#post13889763 "Post Permalink")

  * Feb 9, 2022 9:15pm  Feb 9, 2022 9:15pm 

  * [ veslup](veslup)

  * | Joined Nov 2009  | Status: Trader | [141 Posts](/search?do=process&provider=Member&searchuser=124349)

> [Quoting SwingMan](/thread/post/13885451#post13885451 "View Quoted Post")
> 
> Disliked
> 
> New Expert Advisor version "smBodySwitch EA_v3.2" - No orders between 21:00 and 03:00 - Some bugs fixed - The background of the charts changes for active trades (Buy/Sell). A new script "smApplayTemplate AllCharts" with which one can assign a template in all charts of the workspace. This is helpful to save a lot of time. I have now started the Trade Explorer with 28 pairs, leverage 1:500. The parameter (maxTrades=7), let's see what happens. {file} {file} {image}
> 
> Ignored

Very good job. When I wakeup morning all orders were on please. No need any more to wait until midnight.  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 540 KB](/attachment/image/4140984/thumbnail?d=1644409075)](/attachment/image/4140984?d=1644409075)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#383](/thread/post/13889809#post13889809 "Post Permalink")

  * Feb 9, 2022 9:48pm  Feb 9, 2022 9:48pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting budidharma19](/thread/post/13889739#post13889739 "View Quoted Post")
> 
> Disliked
> 
> ...DEFAULT setting means "maxim Trades = 10 ", "Reference_Account = Account Specified" , or you change to other setting ?
> 
> Ignored

I am not changing anything at this time.  
  
If you test and find better settings, let us know.  
  
\- The "maxTrades" limit the levels of the martingale, and hopefully the margin will be valid at this broker.  
\- The "Reference_Account" is intended for the calculation of the initial lots, which can be increased a lot in martingale. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#384](/thread/post/13889818#post13889818 "Post Permalink")

  * Feb 9, 2022 9:52pm  Feb 9, 2022 9:52pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting veslup](/thread/post/13889763#post13889763 "View Quoted Post")
> 
> Disliked
> 
> {...Very good job. When I wakeup morning all orders were on please. No need any more to wait until midnight.
> 
> Ignored

I'm glad because you can now earn many thousands of money while you sleep.  
(I do that too...) 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#385](/thread/post/13891008#post13891008 "Post Permalink")

  * Feb 10, 2022 5:43pm  Feb 10, 2022 5:43pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

The account in TradeExplorer was heavily used by the trades on NZDCHF because all CHF pairs have leverage 1:33 instead of 1:500 like all others, and the margin was no longer sufficient.  
  
So I had to remove these pairs from the workspace: AUDCHF, CADCHF, CHFJPY, EURCHF, GBPCHF, NZDCHF, UJSDCHF.  
  
A new account has been created and will be connected to TradeExplorer. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#386](/thread/post/13891536#post13891536 "Post Permalink")

  * Edited Feb 11, 2022 12:23am  Feb 10, 2022 11:01pm | Edited Feb 11, 2022 12:23am 

  * [ veslup](veslup)

  * | Joined Nov 2009  | Status: Trader | [141 Posts](/search?do=process&provider=Member&searchuser=124349)

Excellent job today until now. On my real account.  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 392 KB](/attachment/image/4142032/thumbnail?d=1644501587)](/attachment/image/4142032?d=1644501587)   

  
  
Thanks a lot once again SwingMan. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#387](/thread/post/13892280#post13892280 "Post Permalink")

  * Feb 11, 2022 4:33am  Feb 11, 2022 4:33am 

  * [ kitpu](kitpu)

  * | Joined Sep 2020  | Status: Trader | [27 Posts](/search?do=process&provider=Member&searchuser=997605)

I was trying to optimize those 3 factors (Entry, Take Profit, Stop Loss) for GBPUSD.   
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 4 KB](/attachment/image/4142386/thumbnail?d=1644521332)](/attachment/image/4142386?d=1644521332)   

  
  
Here is the best performance report.   

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 78 KB](/attachment/image/4142385/thumbnail?d=1644521278)](/attachment/image/4142385?d=1644521278)   

  
One error in the tester journal shows this:  
OrderSend error: 130   
  

Attached Image

![](/attachment/image/4142390?d=1644521483)

  
Just report back, and maybe need to be checked.   
Thank you SwingMan. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#388](/thread/post/13892364#post13892364 "Post Permalink")

  * Feb 11, 2022 5:33am  Feb 11, 2022 5:33am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting kitpu](/thread/post/13892280#post13892280 "View Quoted Post")
> 
> Disliked
> 
> I was trying to optimize those 3 factors (Entry, Take Profit, Stop Loss) for GBPUSD...
> 
> Ignored

Thanks _@kitpu_ for your analysis!  
  
Generally speaking, there are very interesting conclusions:  
  
\- The entry can be close to the previous high/low of the body (0.1).  
  
\- The TakeProfit factor remains quite small (0.30).  
  
\- The StopLoss factor is twice the TakeProfit factor (0.60), and this corresponds to many recommendations for a ratio (1:2 Win/Loss).  
Many recommend a ratio (2:1 win/loss) but we have to blindly follow _@kitpu's_ proof! 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#389](/thread/post/13892384#post13892384 "Post Permalink")

  * Feb 11, 2022 5:46am  Feb 11, 2022 5:46am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting veslup](/thread/post/13891536#post13891536 "View Quoted Post")
> 
> Disliked
> 
> Excellent job today until now. On my real account...
> 
> Ignored

It's ok, congratulations, but please delete all CHF pairs if you have leverage of 1:500. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#390](/thread/post/13892505#post13892505 "Post Permalink")

  * Feb 11, 2022 7:51am  Feb 11, 2022 7:51am 

  * [ kitpu](kitpu)

  * | Joined Sep 2020  | Status: Trader | [27 Posts](/search?do=process&provider=Member&searchuser=997605)

> [Quoting SwingMan](/thread/post/13892364#post13892364 "View Quoted Post")
> 
> Disliked
> 
> {quote} Thanks @kitpu for your analysis! Generally speaking, there are very interesting conclusions: - The entry can be close to the previous high/low of the body (0.1). - The TakeProfit factor remains quite small (0.30). - The StopLoss factor is twice the TakeProfit factor (0.60), and this corresponds to many recommendations for a ratio (1:2 Win/Loss). Many recommend a ratio (2:1 win/loss) but we have to blindly follow @kitpu's proof!
> 
> Ignored

I also backtest the same parameter with Entry 0.1/TP 0.3/ SL 0.6 for GBPUSD but using H4 instead of D1. Just to get a sense how the other time frame performs.   
I got slightly better performance in terms of profit, as attached.   
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 77 KB](/attachment/image/4142489/thumbnail?d=1644533138)](/attachment/image/4142489?d=1644533138)   

  
Some OrderSend Error 3 and 130 are still presented in the journal, FYI.   
  

Attached Image

![](/attachment/image/4142492?d=1644533264)

  
error code 130 seems to be invalid stops  
error code 3 is probably invalid trade parameters, don't know what those are   
  
Appreciate SwingMan for the efforts.   
I will test out these parameters for the rest of the pairs and instruments and check back later. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#391](/thread/post/13892543#post13892543 "Post Permalink")

  * Feb 11, 2022 8:55am  Feb 11, 2022 8:55am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting kitpu](/thread/post/13892505#post13892505 "View Quoted Post")
> 
> Disliked
> 
> ...Some OrderSend Error 3 and 130 are still presented in the journal
> 
> Ignored

Here is a temporary version 3.4.0  
Please test the days near the error messages, maybe it will get better.  
If you post, please include the lines before the messages, maybe I can find the cause faster. 

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [smBodySwitch EA_v3.4.0.ex4](/attachment/file/4142514?d=1644537295) 102 KB | 397 downloads 

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#392](/thread/post/13892567#post13892567 "Post Permalink")

  * Feb 11, 2022 9:46am  Feb 11, 2022 9:46am 

  * [ kitpu](kitpu)

  * | Joined Sep 2020  | Status: Trader | [27 Posts](/search?do=process&provider=Member&searchuser=997605)

> [Quoting SwingMan](/thread/post/13892543#post13892543 "View Quoted Post")
> 
> Disliked
> 
> {quote} Here is a temporary version 3.4.0 Please test the days near the error messages, maybe it will get better. If you post, please include the lines before the messages, maybe I can find the cause faster. {file}
> 
> Ignored

Hi SwingMan, please see the attached 3.4.0 tester zipped log (the file size without zipped is huge) as well as the set file. Hope this helps. Cheers. 

Attached File(s)

![File Type: zip](https://assets.faireconomy.media/images/attach/zip.gif) [20220210_v3.4.0 tester journal.zip](/attachment/file/4142530?d=1644540258) 1.0 MB | 205 downloads 

![File Type: txt](https://assets.faireconomy.media/images/attach/txt.gif) [gbpusd H4 or D1_v3.3.set.txt](/attachment/file/4142531?d=1644540344) 4 KB | 155 downloads 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#393](/thread/post/13892633#post13892633 "Post Permalink")

  * Feb 11, 2022 11:12am  Feb 11, 2022 11:12am 

  * [ budidharma19](budidharma19)

  * | Joined Aug 2013  | Status: Trader | [214 Posts](/search?do=process&provider=Member&searchuser=347146)

> [Quoting SwingMan](/thread/post/13892543#post13892543 "View Quoted Post")
> 
> Disliked
> 
> {quote} Here is a temporary version 3.4.0 Please test the days near the error messages, maybe it will get better. If you post, please include the lines before the messages, maybe I can find the cause faster. {file}
> 
> Ignored

Hello SwingMan,  
  
I tried also version 3.4,...  
Still got error messages,.. as follow,...  
  
Hope can help you to make the EA bugless,..  
  
Cheers,  
  
Budi 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 128 KB](/attachment/image/4142572/thumbnail?d=1644545572)](/attachment/image/4142572?d=1644545572)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#394](/thread/post/13893055#post13893055 "Post Permalink")

  * Edited 10:02pm  Feb 11, 2022 6:38pm | Edited 10:02pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

I believe the errors are caused by the spread.  
  
Here's a small change, test if it helps.  
  
Until the errors are fixed, please only test from January 2022 so that I can also have M5 prices.  
Write the broker and the setting as well, because I have completely different test results for [Pepperstone](/brokers/pepperstone "View Pepperstone Broker Profile") and Valutrades. 

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [smBodySwitch EA_v3.4.1.ex4](/attachment/file/4142862?d=1644572295) 103 KB | 472 downloads 

[0 ](javascript:void\(0\);) [4 ](javascript:void\(0\);)

  * [#395](/thread/post/13893205#post13893205 "Post Permalink")

  * Feb 11, 2022 9:00pm  Feb 11, 2022 9:00pm 

  * [ budidharma19](budidharma19)

  * | Joined Aug 2013  | Status: Trader | [214 Posts](/search?do=process&provider=Member&searchuser=347146)

> [Quoting SwingMan](/thread/post/13893055#post13893055 "View Quoted Post")
> 
> Disliked
> 
> I believe the errors are caused by the spread. Here's a small change, test if it helps. Until the errors are fixed, please only test from January 2022 so that I can also have M5 prices. Write the broker and the setting as well, because I have completely different test results for Pepperstone and Valutrade. {file}
> 
> Ignored

Dear SWINGMAN,  
  
Thanks for your response,...  
  
I am testing using DUKASCOPY Tickdata ,... so the data will be OK,.. and complete all the TF.  
  
I will retest once again and let you know the result,...  
  
Cheers,  
  
Budi 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#396](/thread/post/13893410#post13893410 "Post Permalink")

  * Edited Feb 12, 2022 1:17am  Feb 11, 2022 11:43pm | Edited Feb 12, 2022 1:17am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting budidharma19](/thread/post/13893205#post13893205 "View Quoted Post")
> 
> Disliked
> 
> {quote} Dear SWINGMAN, Thanks for your response,... I am testing using DUKASCOPY Tickdata ,... so the data will be OK,.. and complete all the TF. I will retest once again and let you know the result,... Cheers, Budi
> 
> Ignored

There are no TF's.  
Everything is calculated for D1 even if the chart is H4, H1 etc.  
  
I must learn to download the Dukascopy data - if that helps... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#397](/thread/post/13894123#post13894123 "Post Permalink")

  * Feb 12, 2022 1:36pm  Feb 12, 2022 1:36pm 

  * [ kitpu](kitpu)

  * | Joined Sep 2020  | Status: Trader | [27 Posts](/search?do=process&provider=Member&searchuser=997605)

> [Quoting SwingMan](/thread/post/13893055#post13893055 "View Quoted Post")
> 
> Disliked
> 
> I believe the errors are caused by the spread. Here's a small change, test if it helps. Until the errors are fixed, please only test from January 2022 so that I can also have M5 prices. Write the broker and the setting as well, because I have completely different test results for Pepperstone and Valutrades. {file}
> 
> Ignored

This version looks good to me. Those OrderSend errors no longer appear. Thank you SwingMan. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#398](/thread/post/13894144#post13894144 "Post Permalink")

  * Feb 12, 2022 2:30pm  Feb 12, 2022 2:30pm 

  * [ d.dalal333](d.dalal333)

  * | Joined Jan 2013  | Status: Trader | [72 Posts](/search?do=process&provider=Member&searchuser=321856)

> [Quoting SwingMan](/thread/post/13868408#post13868408 "View Quoted Post")
> 
> Disliked
> 
> Here is a new version "smBodySwitch EA_v1.2" with a little change: the EA stops when the FreeMargin is not enough anymore. {file}
> 
> Ignored

I have backtested from 01.09.2021 till 09.02.2022 for 5 months and after proper reports in "eurusd" installed in demo with another my own EA but it clash with my old robot (EA) and after installation of smBody EA my all trade with SL hits and closing trade in loss in my own EA and sm Body EA open BUY trade 4.13LOT initiated and market crash and 2882.74 open trade yet.  
  
is it advisable to install when 1 old robo is working in same acct ?   
  
how i can installed both in big equity acct ? Pl. guide me 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#399](/thread/post/13894204#post13894204 "Post Permalink")

  * Feb 12, 2022 5:26pm  Feb 12, 2022 5:26pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting d.dalal333](/thread/post/13894144#post13894144 "View Quoted Post")
> 
> Disliked
> 
> {quote} I have backtested from 01.09.2021 till 09.02.2022 for 5 months and after proper reports in "eurusd" installed in demo with another my own EA but it clash with my old robot (EA) and after installation of smBody EA my all trade with SL hits and closing trade in loss in my own EA and sm Body EA open BUY trade 4.13LOT initiated and market crash and 2882.74 open trade yet. is it advisable to install when 1 old robo is working in same acct ? how i can installed both in big equity acct ? Pl. guide me
> 
> Ignored

If I understand correctly, the "BodySwitch EA" closes order from another EA.  
  
The "BodySwitch EA" works with (MagicNumber=1000), and only closes orders with this number.  

Inserted Code
    
    
    if(dClose<=lossLevel && order.MagicNumberX==MagicNumber)

If that's how I understand it, you also have "MagicNumber=1000" and have to change the MagicNumber in your EA or in the BodySwitch. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#400](/thread/post/13894297#post13894297 "Post Permalink")

  * Feb 12, 2022 9:27pm  Feb 12, 2022 9:27pm 

  * [ budidharma19](budidharma19)

  * | Joined Aug 2013  | Status: Trader | [214 Posts](/search?do=process&provider=Member&searchuser=347146)

Dear SwingMan,  
  
I am dedicated this optimized result for EURUSD since 2021 for this THREAD,.. hope helpful.  
Using Dukascopy Tick data for >99% quality  
  
If you all like it I will optimize more pairs.  
  
Cheers,  
  
Budi 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 66 KB](/attachment/image/4143514/thumbnail?d=1644668821)](/attachment/image/4143514?d=1644668821)   

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * LazyHedging Trading Ideas
  *   * [ **Reply to Thread** ](/thread/1058948-lazyhedging-trading-ideas/reply#reply)

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

[EurCad Analysis and Trading Ideas](/thread/360980-eurcad-analysis-and-trading-ideas "Hello my friends. 
 
As of lately I have had remarkable success in trading EurCad and after hearing other traders ideas I decided that we...") 594 replies

[FSP Trading Journal and Trend Ideas](/thread/427493-fsp-trading-journal-and-trend-ideas "hello  
I am trying to post some of my trade Ideas here. 
there will be trend following and counter trend trades. 
I will post image rather...") 16 replies

[Forex trading platform that doesn't take your ideas](/thread/311080-forex-trading-platform-that-doesnt-take-your-ideas "Ninja trader, Metatrader, Tradestation all can copy the EA and indicators straight out of your PC. 
 
How do we go about developing a...") 11 replies

[Program Your Trading Ideas without being a programmer](/thread/225629-program-your-trading-ideas-without-being-a-programmer "I have to admit, I have a lot of trading ideas, but no programming skills. I hate paying a programmer to take 3 days to write an EA for me,...") 4 replies

[Exchanging trading ideas](/thread/136764-exchanging-trading-ideas "I'm opening this thread as a substitute for live chat like msn etc to exchange trading ideas and to filter of some posts at Igrok's thread,...") 37 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/1058948-lazyhedging-trading-ideas/reply#reply)
  * Subscribe
  * [271](javascript:void\(0\);)

Attachments: LazyHedging Trading Ideas

Tags: LazyHedging Trading Ideas

#  [](/thread/1058948-lazyhedging-trading-ideas)LazyHedging Trading Ideas 

  * 

  * [#401](/thread/post/13894344#post13894344 "Post Permalink")

  * Feb 12, 2022 10:54pm  Feb 12, 2022 10:54pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting budidharma19](/thread/post/13894297#post13894297 "View Quoted Post")
> 
> Disliked
> 
> Dear SwingMan, I am dedicated this optimized result for EURUSD since 2021 for this THREAD,.. hope helpful. Using Dukascopy Tick data for >99% quality If you all like it I will optimize more pairs. Cheers, Budi
> 
> Ignored

If you have time, please test a few more pairs and create a small table with the essential characteristic, possibly also with the largest LotValue.  
  
I now have a new EA variant for what I called "Generation-5", and later it would be important to know if it is better or not than "Generation-3".  
I don't have the time to program it now, but maybe I'll be able to start in about two weeks. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#402](/thread/post/13894424#post13894424 "Post Permalink")

  * Feb 13, 2022 2:02am  Feb 13, 2022 2:02am 

  * [ d.dalal333](d.dalal333)

  * | Joined Jan 2013  | Status: Trader | [72 Posts](/search?do=process&provider=Member&searchuser=321856)

> [Quoting SwingMan](/thread/post/13894204#post13894204 "View Quoted Post")
> 
> Disliked
> 
> {quote} If I understand correctly, the "BodySwitch EA" closes order from another EA. The "BodySwitch EA" works with (MagicNumber=1000), and only closes orders with this number. if(dClose<=lossLevel && order.MagicNumberX==MagicNumber) If that's how I understand it, you also have "MagicNumber=1000" and have to change the MagicNumber in your EA or in the BodySwitch.
> 
> Ignored

MAGIC NO. 1000 FOR SwingMan  
another Ea having 5 digit magic no.  
then also  
any order open with otherthan Swingman it get SL and closed that trade, like that so many order closed hence finally have to stop SwingMan EA and then market gone don and hat trade still open in loss. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#403](/thread/post/13894441#post13894441 "Post Permalink")

  * Feb 13, 2022 2:39am  Feb 13, 2022 2:39am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting d.dalal333](/thread/post/13894424#post13894424 "View Quoted Post")
> 
> Disliked
> 
> {quote} MAGIC NO. 1000 FOR SwingMan another Ea having 5 digit magic no. then also any order open with otherthan Swingman it get SL and closed that trade, like that so many order closed hence finally have to stop SwingMan EA and then market gone don and hat trade still open in loss.
> 
> Ignored

From your description, with my English I honestly don't understand where the problem is. Maybe if you had written: 1.Start EA1 on pair XXX and EA2 on same pair XXX, 2.EA1 close Order, 3.EA2 dont close, Order etc.  
  
You can have two accounts if you use two EAs for the same pairs, or don't use the "BodySwitch EA" anymore. Very simple, you just have to trade on two separate platforms.  
  
Or you trade some pairs with one EA and others with the second, no problem. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#404](/thread/post/13894462#post13894462 "Post Permalink")

  * Feb 13, 2022 3:28am  Feb 13, 2022 3:28am 

  * [ kitpu](kitpu)

  * | Joined Sep 2020  | Status: Trader | [27 Posts](/search?do=process&provider=Member&searchuser=997605)

Hi SwingMan, could you please shade some light what the "StealthTrading" parameter is in the EA? Thanks. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#405](/thread/post/13894485#post13894485 "Post Permalink")

  * Feb 13, 2022 4:18am  Feb 13, 2022 4:18am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting kitpu](/thread/post/13894462#post13894462 "View Quoted Post")
> 
> Disliked
> 
> Hi SwingMan, could you please shade some light what the "StealthTrading" parameter is in the EA? Thanks.
> 
> Ignored

If you don't know the term "StealthTrading" for the EAs, then you might know "StealthBomber"...  
  
If you want to send orders without the broker noticing where is your Entry, TP and SL to fish your lots, then the orders are sent as MarketOrders, then when a BuyStop would have fired them too ![](https://resources.faireconomy.media/images/emojis/64/1f680.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/2708-fe0f.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f6f8.png?v=15.1). 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#406](/thread/post/13894596#post13894596 "Post Permalink")

  * Feb 13, 2022 9:52am  Feb 13, 2022 9:52am 

  * [ budidharma19](budidharma19)

  * | Joined Aug 2013  | Status: Trader | [214 Posts](/search?do=process&provider=Member&searchuser=347146)

Dear SwingMan and all friends,  
  
Here are GBPUSD for year 2021-2022  
For LARGER lot size, just add in more RISK to go,...  
  
Cheers,... 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 67 KB](/attachment/image/4143692/thumbnail?d=1644713534)](/attachment/image/4143692?d=1644713534)   

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#407](/thread/post/13894640#post13894640 "Post Permalink")

  * Feb 13, 2022 11:47am  Feb 13, 2022 11:47am 

  * [ d.dalal333](d.dalal333)

  * | Joined Jan 2013  | Status: Trader | [72 Posts](/search?do=process&provider=Member&searchuser=321856)

> [Quoting swingman](/thread/post/13894441#post13894441 "View Quoted Post")
> 
> Disliked
> 
> {quote} from your description, with my english i honestly don't understand where the problem is. Maybe if you had written: 1.start ea1 on pair xxx and ea2 on same pair xxx, 2.ea1 close order, 3.ea2 dont close, order etc. You can have two accounts if you use two eas for the same pairs, or don't use the "bodyswitch ea" anymore. Very simple, you just have to trade on two separate platforms. Or you trade some pairs with one ea and others with the second, no problem.
> 
> Ignored

ok. Noted ( will not use same pair two different ea, particularly swingman) 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#408](/thread/post/13894694#post13894694 "Post Permalink")

  * Feb 13, 2022 3:07pm  Feb 13, 2022 3:07pm 

  * [ budidharma19](budidharma19)

  * | Joined Aug 2013  | Status: Trader | [214 Posts](/search?do=process&provider=Member&searchuser=347146)

Here are AUDUSD,.... 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 66 KB](/attachment/image/4143750/thumbnail?d=1644732453)](/attachment/image/4143750?d=1644732453)   

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#409](/thread/post/13894708#post13894708 "Post Permalink")

  * Feb 13, 2022 4:08pm  Feb 13, 2022 4:08pm 

  * [ d.dalal333](d.dalal333)

  * | Joined Jan 2013  | Status: Trader | [72 Posts](/search?do=process&provider=Member&searchuser=321856)

> [Quoting swingman](/thread/post/13889538#post13889538 "View Quoted Post")
> 
> Disliked
> 
> new expertadvisor version "smbodyswitch ea_v3.3" - some corrections and adjustments were made. - workspace with 28 pairs and 2 dummys. Right now there are three pending orders activated. This is only done near the entry levels so that one does not send 28 pending orders at once, and many are not activated later. {image} {file}
> 
> Ignored

this to be installed as normal ex4 file in mql/ expert folder ?  
It will start trading in all pairs ? Instead of 1 pair only. ?  
  
This will be excellent if it is multi pair... Pl guide .. Will act as per your instruction.  
  
Waiting.. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#410](/thread/post/13894728#post13894728 "Post Permalink")

  * Feb 13, 2022 4:54pm  Feb 13, 2022 4:54pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting budidharma19](/thread/post/13894596#post13894596 "View Quoted Post")
> 
> Disliked
> 
> ... Here are GBPUSD for year 2021-2022. For LARGER lot size, just add in more RISK to go,... Cheers,...
> 
> Ignored

Even that wouldn't be bad, with 20 pairs at a bet of $5,000 one earns $20,000 in a year...  
  
But for multiple pairs one should pay attention to the margin for the largest lot number. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#411](/thread/post/13894736#post13894736 "Post Permalink")

  * Feb 13, 2022 5:15pm  Feb 13, 2022 5:15pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting d.dalal333](/thread/post/13894708#post13894708 "View Quoted Post")
> 
> Disliked
> 
> ...This will be excellent if it is multi pair...
> 
> Ignored

Not now.  
But why? I only program a dashboard with several pairs if someone is satisfied with the EA for a long time.  
The EA is still in development and testing, and because it works with martingale it can bring big losses. 

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#412](/thread/post/13895191#post13895191 "Post Permalink")

  * Feb 14, 2022 8:54am  Feb 14, 2022 8:54am 

  * [ budidharma19](budidharma19)

  * | Joined Aug 2013  | Status: Trader | [214 Posts](/search?do=process&provider=Member&searchuser=347146)

Here are USDCAD with a bit LOW RISK 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 65 KB](/attachment/image/4143997/thumbnail?d=1644796474)](/attachment/image/4143997?d=1644796474)   

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#413](/thread/post/13895192#post13895192 "Post Permalink")

  * Feb 14, 2022 8:56am  Feb 14, 2022 8:56am 

  * [ budidharma19](budidharma19)

  * | Joined Aug 2013  | Status: Trader | [214 Posts](/search?do=process&provider=Member&searchuser=347146)

> [Quoting SwingMan](/thread/post/13894728#post13894728 "View Quoted Post")
> 
> Disliked
> 
> {quote} Even that wouldn't be bad, with 20 pairs at a bet of $5,000 one earns $20,000 in a year... But for multiple pairs one should pay attention to the margin for the largest lot number.
> 
> Ignored

I will calculate as a PACKAGES, when all the pairs finished, likely 0,5% Risk can apply all pairs with satisfied Profit  
Hoping,..... 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#414](/thread/post/13895194#post13895194 "Post Permalink")

  * Feb 14, 2022 9:00am  Feb 14, 2022 9:00am 

  * [ budidharma19](budidharma19)

  * | Joined Aug 2013  | Status: Trader | [214 Posts](/search?do=process&provider=Member&searchuser=347146)

Here USDCHF ,... 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 66 KB](/attachment/image/4144000/thumbnail?d=1644796793)](/attachment/image/4144000?d=1644796793)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#415](/thread/post/13895466#post13895466 "Post Permalink")

  * Feb 14, 2022 4:36pm  Feb 14, 2022 4:36pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting budidharma19](/thread/post/13895194#post13895194 "View Quoted Post")
> 
> Disliked
> 
> Here USDCHF...
> 
> Ignored

For CHF pairs the results are not so good.  
  
Away with it...  
  
The margin is risky to stop the trade. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#416](/thread/post/13895639#post13895639 "Post Permalink")

  * Feb 14, 2022 6:01pm  Feb 14, 2022 6:01pm 

  * [ budidharma19](budidharma19)

  * | Joined Aug 2013  | Status: Trader | [214 Posts](/search?do=process&provider=Member&searchuser=347146)

Here are USDJPY,..also not so good,... 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 66 KB](/attachment/image/4144260/thumbnail?d=1644829260)](/attachment/image/4144260?d=1644829260)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#417](/thread/post/13895651#post13895651 "Post Permalink")

  * Feb 14, 2022 6:04pm  Feb 14, 2022 6:04pm 

  * [ budidharma19](budidharma19)

  * | Joined Aug 2013  | Status: Trader | [214 Posts](/search?do=process&provider=Member&searchuser=347146)

Here good enough AUDCAD ,... 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 64 KB](/attachment/image/4144265/thumbnail?d=1644829451)](/attachment/image/4144265?d=1644829451)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#418](/thread/post/13895946#post13895946 "Post Permalink")

  * Feb 14, 2022 9:52pm  Feb 14, 2022 9:52pm 

  * [ budidharma19](budidharma19)

  * | Joined Aug 2013  | Status: Trader | [214 Posts](/search?do=process&provider=Member&searchuser=347146)

Here are AUDCHF,... 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 66 KB](/attachment/image/4144414/thumbnail?d=1644843137)](/attachment/image/4144414?d=1644843137)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#419](/thread/post/13895957#post13895957 "Post Permalink")

  * Feb 14, 2022 9:59pm  Feb 14, 2022 9:59pm 

  * [ budidharma19](budidharma19)

  * | Joined Aug 2013  | Status: Trader | [214 Posts](/search?do=process&provider=Member&searchuser=347146)

Here are AUDJPY,... 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 66 KB](/attachment/image/4144417/thumbnail?d=1644843592)](/attachment/image/4144417?d=1644843592)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#420](/thread/post/13896861#post13896861 "Post Permalink")

  * Feb 15, 2022 11:06am  Feb 15, 2022 11:06am 

  * [ budidharma19](budidharma19)

  * | Joined Aug 2013  | Status: Trader | [214 Posts](/search?do=process&provider=Member&searchuser=347146)

Here AUDNZD ( dont try this at home ! ),... 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 66 KB](/attachment/image/4144868/thumbnail?d=1644890791)](/attachment/image/4144868?d=1644890791)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * LazyHedging Trading Ideas
  *   * [ **Reply to Thread** ](/thread/1058948-lazyhedging-trading-ideas/reply#reply)

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

[EurCad Analysis and Trading Ideas](/thread/360980-eurcad-analysis-and-trading-ideas "Hello my friends. 
 
As of lately I have had remarkable success in trading EurCad and after hearing other traders ideas I decided that we...") 594 replies

[FSP Trading Journal and Trend Ideas](/thread/427493-fsp-trading-journal-and-trend-ideas "hello  
I am trying to post some of my trade Ideas here. 
there will be trend following and counter trend trades. 
I will post image rather...") 16 replies

[Forex trading platform that doesn't take your ideas](/thread/311080-forex-trading-platform-that-doesnt-take-your-ideas "Ninja trader, Metatrader, Tradestation all can copy the EA and indicators straight out of your PC. 
 
How do we go about developing a...") 11 replies

[Program Your Trading Ideas without being a programmer](/thread/225629-program-your-trading-ideas-without-being-a-programmer "I have to admit, I have a lot of trading ideas, but no programming skills. I hate paying a programmer to take 3 days to write an EA for me,...") 4 replies

[Exchanging trading ideas](/thread/136764-exchanging-trading-ideas "I'm opening this thread as a substitute for live chat like msn etc to exchange trading ideas and to filter of some posts at Igrok's thread,...") 37 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/1058948-lazyhedging-trading-ideas/reply#reply)
  * Subscribe
  * [271](javascript:void\(0\);)

Attachments: LazyHedging Trading Ideas

Tags: LazyHedging Trading Ideas

#  [](/thread/1058948-lazyhedging-trading-ideas)LazyHedging Trading Ideas 

  * 

  * [#421](/thread/post/13896862#post13896862 "Post Permalink")

  * Feb 15, 2022 11:08am  Feb 15, 2022 11:08am 

  * [ budidharma19](budidharma19)

  * | Joined Aug 2013  | Status: Trader | [214 Posts](/search?do=process&provider=Member&searchuser=347146)

Here are CADCHF, 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 65 KB](/attachment/image/4144869/thumbnail?d=1644890892)](/attachment/image/4144869?d=1644890892)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#422](/thread/post/13897152#post13897152 "Post Permalink")

  * Feb 15, 2022 5:37pm  Feb 15, 2022 5:37pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting budidharma19](/thread/post/13896861#post13896861 "View Quoted Post")
> 
> Disliked
> 
> Here AUDNZD ( dont try this at home ! ),...
> 
> Ignored

Strange... For only 3 losses, such a drawdown? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#423](/thread/post/13897174#post13897174 "Post Permalink")

  * Feb 15, 2022 5:48pm  Feb 15, 2022 5:48pm 

  * [ budidharma19](budidharma19)

  * | Joined Aug 2013  | Status: Trader | [214 Posts](/search?do=process&provider=Member&searchuser=347146)

> [Quoting SwingMan](/thread/post/13897152#post13897152 "View Quoted Post")
> 
> Disliked
> 
> {quote} Strange... For only 3 losses, such a drawdown?
> 
> Ignored

Will check it again after finished with another pairs,... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#424](/thread/post/13897209#post13897209 "Post Permalink")

  * Feb 15, 2022 6:08pm  Feb 15, 2022 6:08pm 

  * [ budidharma19](budidharma19)

  * | Joined Aug 2013  | Status: Trader | [214 Posts](/search?do=process&provider=Member&searchuser=347146)

Here are CADJPY, 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 66 KB](/attachment/image/4145102/thumbnail?d=1644916112)](/attachment/image/4145102?d=1644916112)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#425](/thread/post/13897217#post13897217 "Post Permalink")

  * Feb 15, 2022 6:10pm  Feb 15, 2022 6:10pm 

  * [ budidharma19](budidharma19)

  * | Joined Aug 2013  | Status: Trader | [214 Posts](/search?do=process&provider=Member&searchuser=347146)

Here are CHFJPY,.. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 65 KB](/attachment/image/4145105/thumbnail?d=1644916217)](/attachment/image/4145105?d=1644916217)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#426](/thread/post/13897344#post13897344 "Post Permalink")

  * Feb 15, 2022 7:43pm  Feb 15, 2022 7:43pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting budidharma19](/thread/post/13897174#post13897174 "View Quoted Post")
> 
> Disliked
> 
> ...Will check it again after finished with another pairs,...
> 
> Ignored

I suppose is a hedge trade on a day (weekend?) with gap. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#427](/thread/post/13898359#post13898359 "Post Permalink")

  * Feb 16, 2022 9:28am  Feb 16, 2022 9:28am 

  * [ budidharma19](budidharma19)

  * | Joined Aug 2013  | Status: Trader | [214 Posts](/search?do=process&provider=Member&searchuser=347146)

Here are EURAUD : 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 66 KB](/attachment/image/4145693/thumbnail?d=1644971299)](/attachment/image/4145693?d=1644971299)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#428](/thread/post/13898360#post13898360 "Post Permalink")

  * Feb 16, 2022 9:30am  Feb 16, 2022 9:30am 

  * [ budidharma19](budidharma19)

  * | Joined Aug 2013  | Status: Trader | [214 Posts](/search?do=process&provider=Member&searchuser=347146)

Here are EURCAD : 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 64 KB](/attachment/image/4145694/thumbnail?d=1644971415)](/attachment/image/4145694?d=1644971415)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#429](/thread/post/13898425#post13898425 "Post Permalink")

  * Feb 16, 2022 11:31am  Feb 16, 2022 11:31am 

  * [ budidharma19](budidharma19)

  * | Joined Aug 2013  | Status: Trader | [214 Posts](/search?do=process&provider=Member&searchuser=347146)

Here are EURCHF, always PROBLEM,..dont try this at HOME : 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 66 KB](/attachment/image/4145749/thumbnail?d=1644978688)](/attachment/image/4145749?d=1644978688)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#430](/thread/post/13898767#post13898767 "Post Permalink")

  * Feb 16, 2022 5:53pm  Feb 16, 2022 5:53pm 

  * [ budidharma19](budidharma19)

  * | Joined Aug 2013  | Status: Trader | [214 Posts](/search?do=process&provider=Member&searchuser=347146)

Here are EURGBP : 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 66 KB](/attachment/image/4145945/thumbnail?d=1645001594)](/attachment/image/4145945?d=1645001594)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#431](/thread/post/13898776#post13898776 "Post Permalink")

  * Feb 16, 2022 5:58pm  Feb 16, 2022 5:58pm 

  * [ budidharma19](budidharma19)

  * | Joined Aug 2013  | Status: Trader | [214 Posts](/search?do=process&provider=Member&searchuser=347146)

Here are EURJPY : 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 66 KB](/attachment/image/4145949/thumbnail?d=1645001878)](/attachment/image/4145949?d=1645001878)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#432](/thread/post/13899006#post13899006 "Post Permalink")

  * Feb 16, 2022 9:13pm  Feb 16, 2022 9:13pm 

  * [ budidharma19](budidharma19)

  * | Joined Aug 2013  | Status: Trader | [214 Posts](/search?do=process&provider=Member&searchuser=347146)

Here are EURNZD : 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 66 KB](/attachment/image/4146082/thumbnail?d=1645013598)](/attachment/image/4146082?d=1645013598)   

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#433](/thread/post/13899043#post13899043 "Post Permalink")

  * Feb 16, 2022 9:40pm  Feb 16, 2022 9:40pm 

  * [ budidharma19](budidharma19)

  * | Joined Aug 2013  | Status: Trader | [214 Posts](/search?do=process&provider=Member&searchuser=347146)

Here are GBPAUD : 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 65 KB](/attachment/image/4146093/thumbnail?d=1645015235)](/attachment/image/4146093?d=1645015235)   

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#434](/thread/post/13899612#post13899612 "Post Permalink")

  * Feb 17, 2022 3:06am  Feb 17, 2022 3:06am 

  * [ kitpu](kitpu)

  * | Joined Sep 2020  | Status: Trader | [27 Posts](/search?do=process&provider=Member&searchuser=997605)

AUDCAD went a wild run today, possibly due to news:  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 8 KB](/attachment/image/4146357/thumbnail?d=1645034449)](/attachment/image/4146357?d=1645034449)   

1: Buy 0.24 lot, hit SL, P/L $-64.75  
2: Sell 1.79 lot, hit another SL, P/L $-388.94  
3: Buy 11.11 lot, hit TP, P/L 358.91, so overall still P/L $-94.78, with some commission fee.   
Cheers. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#435](/thread/post/13899661#post13899661 "Post Permalink")

  * Feb 17, 2022 3:46am  Feb 17, 2022 3:46am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar337765_5.gif) dokopy](dokopy)

  * Joined May 2013 | Status: Trader | [894 Posts](/search?do=process&provider=Member&searchuser=337765)

I wish you good luck, but I'm done. For several days I tested 28 pairs and found all the shortcomings of the martingale. 

Please excuse the bad English via Google Translate.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#436](/thread/post/13899997#post13899997 "Post Permalink")

  * Feb 17, 2022 8:51am  Feb 17, 2022 8:51am 

  * [ budidharma19](budidharma19)

  * | Joined Aug 2013  | Status: Trader | [214 Posts](/search?do=process&provider=Member&searchuser=347146)

Here are GBPCAD : 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 65 KB](/attachment/image/4146564/thumbnail?d=1645055486)](/attachment/image/4146564?d=1645055486)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#437](/thread/post/13899998#post13899998 "Post Permalink")

  * Feb 17, 2022 8:53am  Feb 17, 2022 8:53am 

  * [ budidharma19](budidharma19)

  * | Joined Aug 2013  | Status: Trader | [214 Posts](/search?do=process&provider=Member&searchuser=347146)

Here are GBPCHF : 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 65 KB](/attachment/image/4146565/thumbnail?d=1645055590)](/attachment/image/4146565?d=1645055590)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#438](/thread/post/13900127#post13900127 "Post Permalink")

  * Feb 17, 2022 11:53am  Feb 17, 2022 11:53am 

  * [ budidharma19](budidharma19)

  * | Joined Aug 2013  | Status: Trader | [214 Posts](/search?do=process&provider=Member&searchuser=347146)

Here are NZDJPY : 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 65 KB](/attachment/image/4146629/thumbnail?d=1645066412)](/attachment/image/4146629?d=1645066412)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#439](/thread/post/13900135#post13900135 "Post Permalink")

  * Feb 17, 2022 12:08pm  Feb 17, 2022 12:08pm 

  * [ budidharma19](budidharma19)

  * | Joined Aug 2013  | Status: Trader | [214 Posts](/search?do=process&provider=Member&searchuser=347146)

Here are GBPJPY , danger : 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 66 KB](/attachment/image/4146630/thumbnail?d=1645067285)](/attachment/image/4146630?d=1645067285)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#440](/thread/post/13900506#post13900506 "Post Permalink")

  * Feb 17, 2022 5:09pm  Feb 17, 2022 5:09pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

Optimization results: 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 22 KB](/attachment/image/4146844/thumbnail?d=1645085318)](/attachment/image/4146844?d=1645085318)   

Attached Image

![](/attachment/image/4146845?d=1645085358)

[0 ](javascript:void\(0\);) [4 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * LazyHedging Trading Ideas
  *   * [ **Reply to Thread** ](/thread/1058948-lazyhedging-trading-ideas/reply#reply)

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

[EurCad Analysis and Trading Ideas](/thread/360980-eurcad-analysis-and-trading-ideas "Hello my friends. 
 
As of lately I have had remarkable success in trading EurCad and after hearing other traders ideas I decided that we...") 594 replies

[FSP Trading Journal and Trend Ideas](/thread/427493-fsp-trading-journal-and-trend-ideas "hello  
I am trying to post some of my trade Ideas here. 
there will be trend following and counter trend trades. 
I will post image rather...") 16 replies

[Forex trading platform that doesn't take your ideas](/thread/311080-forex-trading-platform-that-doesnt-take-your-ideas "Ninja trader, Metatrader, Tradestation all can copy the EA and indicators straight out of your PC. 
 
How do we go about developing a...") 11 replies

[Program Your Trading Ideas without being a programmer](/thread/225629-program-your-trading-ideas-without-being-a-programmer "I have to admit, I have a lot of trading ideas, but no programming skills. I hate paying a programmer to take 3 days to write an EA for me,...") 4 replies

[Exchanging trading ideas](/thread/136764-exchanging-trading-ideas "I'm opening this thread as a substitute for live chat like msn etc to exchange trading ideas and to filter of some posts at Igrok's thread,...") 37 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/1058948-lazyhedging-trading-ideas/reply#reply)
  * Subscribe
  * [271](javascript:void\(0\);)

Attachments: LazyHedging Trading Ideas

Tags: LazyHedging Trading Ideas

#  [](/thread/1058948-lazyhedging-trading-ideas)LazyHedging Trading Ideas 

  * 

  * [#441](/thread/post/13900807#post13900807 "Post Permalink")

  * Feb 17, 2022 8:31pm  Feb 17, 2022 8:31pm 

  * [ budidharma19](budidharma19)

  * | Joined Aug 2013  | Status: Trader | [214 Posts](/search?do=process&provider=Member&searchuser=347146)

Here are GBPNZD : 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 65 KB](/attachment/image/4146958/thumbnail?d=1645097478)](/attachment/image/4146958?d=1645097478)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#442](/thread/post/13900809#post13900809 "Post Permalink")

  * Feb 17, 2022 8:33pm  Feb 17, 2022 8:33pm 

  * [ budidharma19](budidharma19)

  * | Joined Aug 2013  | Status: Trader | [214 Posts](/search?do=process&provider=Member&searchuser=347146)

Here are NZDCAD : 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 65 KB](/attachment/image/4146959/thumbnail?d=1645097582)](/attachment/image/4146959?d=1645097582)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#443](/thread/post/13901126#post13901126 "Post Permalink")

  * Feb 17, 2022 11:47pm  Feb 17, 2022 11:47pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

Congratulations _@budidharma19_!  
  
You have traded a whole year with a lot of patience, and your success is visible:  
you turned $5,000 into $17,900, and even though the HedgeMartingale seemed dangerous at times, your nerves resisted.  
  
I can now take your example, transfer $50,000 to my trading account, and this year I can live comfortably with a profit of around $180,000. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 21 KB](/attachment/image/4147107/thumbnail?d=1645109232)](/attachment/image/4147107?d=1645109232)   

[0 ](javascript:void\(0\);) [7 ](javascript:void\(0\);)

  * [#444](/thread/post/13901644#post13901644 "Post Permalink")

  * Feb 18, 2022 7:01am  Feb 18, 2022 7:01am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar588299_3.gif) RiskFighter](riskfighter)

  * Joined Jun 2017 | Status: Trader | [1,566 Posts](/search?do=process&provider=Member&searchuser=588299)

> [Quoting SwingMan](/thread/post/13901126#post13901126 "View Quoted Post")
> 
> Disliked
> 
> Congratulations @budidharma19! You have traded a whole year with a lot of patience, and your success is visible: you turned $5,000 into $17,900, and even though the HedgeMartingale seemed dangerous at times, your nerves resisted. I can now take your example, transfer $50,000 to my trading account, and this year I can live comfortably with a profit of around $180,000. {image}
> 
> Ignored

I recon that he did not trade - he tested on demo. And he invested 5.000 in each test. That is a total of 130.000 and the total gain were 18.000. I guess that I am wrong about this. Sorry to bring it up. 

Read post #1 !! Then read it again 10 more times before you ask.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#445](/thread/post/13901648#post13901648 "Post Permalink")

  * Feb 18, 2022 7:09am  Feb 18, 2022 7:09am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

Hi Sparrow, messages to you are blocked. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#446](/thread/post/13901675#post13901675 "Post Permalink")

  * Feb 18, 2022 7:50am  Feb 18, 2022 7:50am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting RiskFighter](/thread/post/13901644#post13901644 "View Quoted Post")
> 
> Disliked
> 
> ...I recon that he did not trade - he tested on demo. And he invested 5.000 in each test. That is a total of 130.000 and the total gain were 18.000. I guess that I am wrong about this. Sorry to bring it up.
> 
> Ignored

I could also have written "had you traded live all year...etc".  
  
But then where would be my fun and the recognition and encouragement for @budi's work?  
  
Great respect also for the nickname:  

> Quote
> 
> Disliked
> 
> _From Wikipedia, the free encyclopedia:_  
>  Bodhidharma was a semi-legendary Buddhist monk who lived during the 5th or 6th century. He is traditionally credited as the transmitter of Buddhism to China, and regarded as its first Chinese patriarch. According to Chinese legend, he also began the physical training of the monks of Shaolin Monastery that led to the creation of Shaolin kungfu. He is known as Dámó in China and as Daruma in Japan. His name means "dharma of awakening (bodhi)" in Sanskrit.

  
He can take for his avatar the image of the monk :  
[https://upload.wikimedia.org/wikiped...itoshi1887.jpg](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/BodhidharmaYoshitoshi1887.jpg/232px-BodhidharmaYoshitoshi1887.jpg)  
  
Now as far as the practical thing goes, I can't say much, I'm not a trader but you are.  
I guess that $5,000 can be traded for a while, maybe better with $10,000 and risk 2%.  
  
The big problem with the martingales will be the margin, so at first don't trade CHF pairs (leverage 1:30).  
With these EA, a maximum of maybe 4-5 pairs are traded per day, not all at the same time, and then the margin would be sufficient (for leverage 1:500).  
I posted the formula:  
Margin=Lots*(100,000/500)  
For 1 lot = $200, and for reached 8 lots = $1,600, everything is doable. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#447](/thread/post/13901991#post13901991 "Post Permalink")

  * Feb 18, 2022 4:37pm  Feb 18, 2022 4:37pm 

  * [ budidharma19](budidharma19)

  * | Joined Aug 2013  | Status: Trader | [214 Posts](/search?do=process&provider=Member&searchuser=347146)

Here the last NZDCHF : 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: screenshot.png
Size: 65 KB](/attachment/image/4147571/thumbnail?d=1645169835)](/attachment/image/4147571?d=1645169835)   

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#448](/thread/post/13902000#post13902000 "Post Permalink")

  * Feb 18, 2022 4:44pm  Feb 18, 2022 4:44pm 

  * [ budidharma19](budidharma19)

  * | Joined Aug 2013  | Status: Trader | [214 Posts](/search?do=process&provider=Member&searchuser=347146)

Dear SwingMan and all,  
  
Let me deliver my point of view,...  
  
The backtest result can be adjusted statistically to be FIX amount of risk. I mean that the "RISK" adjustment can be up and down compared to DRAWDOWN. Lets make the DRAWDOWN FIX,.. lets say USD 1000, and lets assume that 8 pairs traded together. So USD 10000 equity likely enough.  
  
I will make table,.. and I will adjust, which PROFIT projection will good for which PAIRS,.. and lets see. But I need time,...  
  
Cheers,  
  
Budi 

[0 ](javascript:void\(0\);) [4 ](javascript:void\(0\);)

  * [#449](/thread/post/13903853#post13903853 "Post Permalink")

  * Feb 21, 2022 2:51am  Feb 21, 2022 2:51am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

Last week level 10 was reached in AUDCAD, and the lot number was not increased anymore.  
If the EA had traded another level, the losses would be compensated! 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: AUDCADM15.png
Size: 24 KB](/attachment/image/4148658/thumbnail?d=1645379325)](/attachment/image/4148658?d=1645379325)   

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#450](/thread/post/13903859#post13903859 "Post Permalink")

  * Feb 21, 2022 2:59am  Feb 21, 2022 2:59am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

**New generation "5" for the BodySwitch signals and for the EA.**  
  
The reference is no longer at the previous bar, but at the open of the current bar, in the direction of the main trend.  
  
The factors without optimization are 0.4, 0.3, 0.3  
  
After my few tests, however, I have no better results than with the 3-versions, and the maximum lot number was often reached...  
As a conclusion - probably this is not a better version. But I will run them until a substantial loss will take place. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: GBPUSDDaily.png
Size: 25 KB](/attachment/image/4148660/thumbnail?d=1645379859)](/attachment/image/4148660?d=1645379859)   

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [smBodySwitch EA_v5.0.ex4](/attachment/file/4148661?d=1645379872) 101 KB | 596 downloads 

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [smBodySwitch Signals_v5.1.ex4](/attachment/file/4148662?d=1645379874) 66 KB | 795 downloads 

[0 ](javascript:void\(0\);) [6 ](javascript:void\(0\);)

  * [#451](/thread/post/13904017#post13904017 "Post Permalink")

  * Edited 11:02pm  Feb 21, 2022 6:38am | Edited 11:02pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1423900_6.gif) profits7](profits7)

  * Joined Feb 2022 | Status: RedCross Crusader | [2,431 Posts](/search?do=process&provider=Member&searchuser=1423900)

_______________ Thanks SwingMan for ALL ur Hard work ! 

Don’t focus on making $$$, focus on protecting what you have.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#452](/thread/post/13924419#post13924419 "Post Permalink")

  * Mar 8, 2022 6:13pm  Mar 8, 2022 6:13pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar883539_1.gif) Nonip](nonip)

  * | Joined Nov 2019  | Status: Trader | [206 Posts](/search?do=process&provider=Member&searchuser=883539)

Hello Swingman,  
  
Would like to first thank you for your contribution in FF as a whole. I however have a request regarding one your fantastic works that I rely on heavily for my trading. Could you kindly add a signal to smBBMA_Amir DB_v2.0? It does screens the pairs and give awesome signals but doesn't give an alert. 

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [smBBMA_Amir DB_v2.0.ex4](/attachment/file/4159441?d=1646730818) 53 KB | 298 downloads 

"You can't buy the bottom, nor sell the top. The best you can strive for is

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#453](/thread/post/13931683#post13931683 "Post Permalink")

  * Mar 14, 2022 11:20pm  Mar 14, 2022 11:20pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar71675_5.gif) Alberto_Jazz](alberto_jazz)

  * Joined Jun 2008 | Status: Trader | [593 Posts](/search?do=process&provider=Member&searchuser=71675)

> [Quoting SwingMan](/thread/post/13903859#post13903859 "View Quoted Post")
> 
> Disliked
> 
> The reference is no longer at the previous bar, but at the open of the current bar, in the direction of the main trend.
> 
> Ignored

Hi SM  
  
could you confirm that the entry point (for long trades) is defined as follow?  
  
Entry_Point = Open[0]+iATR(NULL,0,14,1)*factor  
  
I don't know if the ATR inputs are correct.  
  
Thank you 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#454](/thread/post/13931803#post13931803 "Post Permalink")

  * Mar 15, 2022 1:12am  Mar 15, 2022 1:12am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting Alberto_Jazz](/thread/post/13931683#post13931683 "View Quoted Post")
> 
> Disliked
> 
> ...Hi SM could you confirm that the entry point (for long trades) is defined as follow? Entry_Point = Open[0]+iATR(NULL,0,14,1)*factor I don't know if the ATR inputs are correct. Thank you
> 
> Ignored

In principle it is as you wrote.  
  
But it is not always the ATR.  
At some point I found that an optimal value is the minimum value of ATR and the bandwidth of MA's 10 and 8 on the high and low.  
I posted the indicator.  
  
The EA is too dangerous (!) and will not develop it further. Until I program a new one, let it run. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#455](/thread/post/13931969#post13931969 "Post Permalink")

  * Mar 15, 2022 4:14am  Mar 15, 2022 4:14am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar337765_5.gif) dokopy](dokopy)

  * Joined May 2013 | Status: Trader | [894 Posts](/search?do=process&provider=Member&searchuser=337765)

> [Quoting Nonip](/thread/post/13924419#post13924419 "View Quoted Post")
> 
> Disliked
> 
> Hello Swingman, Would like to first thank you for your contribution in FF as a whole. I however have a request regarding one your fantastic works that I rely on heavily for my trading. Could you kindly add a signal to smBBMA_Amir DB_v2.0? It does screens the pairs and give awesome signals but doesn't give an alert. {file}
> 
> Ignored

The indicator is incorrect. 

Please excuse the bad English via Google Translate.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#456](/thread/post/13932024#post13932024 "Post Permalink")

  * Mar 15, 2022 5:31am  Mar 15, 2022 5:31am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar71675_5.gif) Alberto_Jazz](alberto_jazz)

  * Joined Jun 2008 | Status: Trader | [593 Posts](/search?do=process&provider=Member&searchuser=71675)

I just started a new thread based on SM Body Switch Indicator.  
  
[https://www.forexfactory.com/thread/...itch-indicator](https://www.forexfactory.com/thread/1144348-smbodyswitch-indicator)

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#457](/thread/post/13932028#post13932028 "Post Permalink")

  * Mar 15, 2022 5:38am  Mar 15, 2022 5:38am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar883539_1.gif) Nonip](nonip)

  * | Joined Nov 2019  | Status: Trader | [206 Posts](/search?do=process&provider=Member&searchuser=883539)

> [Quoting dokopy](/thread/post/13931969#post13931969 "View Quoted Post")
> 
> Disliked
> 
> {quote} The indicator is incorrect.
> 
> Ignored

Hi Dokopy. What do you mean incorrect?. I'm looking at it now on several pairs I traded today and it's very accurate. What is missing is the alerts. It would also be disrespectful for us to discuss this EA here since this is a different thread. Kindly go to the relevant thread and post screenshots showing your charts and the EA so you can verify your claim, I may as well be wrong![](https://resources.faireconomy.media/images/emojis/64/1f937-200d-2642-fe0f.png?v=15.1). 

"You can't buy the bottom, nor sell the top. The best you can strive for is

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#458](/thread/post/13932092#post13932092 "Post Permalink")

  * Mar 15, 2022 7:51am  Mar 15, 2022 7:51am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting Nonip](/thread/post/13924419#post13924419 "View Quoted Post")
> 
> Disliked
> 
> Hello Swingman, Would like to first thank you for your contribution in FF as a whole. I however have a request regarding one your fantastic works that I rely on heavily for my trading. Could you kindly add a signal to smBBMA_Amir DB_v2.0? It does screens the pairs and give awesome signals but doesn't give an alert.
> 
> Ignored

  
Hi _@Nonip_ ,  
I'm sorry I haven't found the right source code yet. Something has been lost. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#459](/thread/post/13932240#post13932240 "Post Permalink")

  * Mar 15, 2022 1:01pm  Mar 15, 2022 1:01pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar337765_5.gif) dokopy](dokopy)

  * Joined May 2013 | Status: Trader | [894 Posts](/search?do=process&provider=Member&searchuser=337765)

> [Quoting Nonip](/thread/post/13932028#post13932028 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi Dokopy. What do you mean incorrect?. I'm looking at it now on several pairs I traded today and it's very accurate. What is missing is the alerts. It would also be disrespectful for us to discuss this EA here since this is a different thread. Kindly go to the relevant thread and post screenshots showing your charts and the EA so you can verify your claim, I may as well be wrong![](https://resources.faireconomy.media/images/emojis/64/1f937-200d-2642-fe0f.png?v=15.1).
> 
> Ignored

I put it among the other indicators. Cannot move to chart. Is it EA? 

Please excuse the bad English via Google Translate.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#460](/thread/post/13932399#post13932399 "Post Permalink")

  * Mar 15, 2022 4:40pm  Mar 15, 2022 4:40pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar883539_1.gif) Nonip](nonip)

  * | Joined Nov 2019  | Status: Trader | [206 Posts](/search?do=process&provider=Member&searchuser=883539)

> [Quoting dokopy](/thread/post/13932240#post13932240 "View Quoted Post")
> 
> Disliked
> 
> {quote} I put it among the other indicators. Cannot move to chart. Is it EA?
> 
> Ignored

Yes, its EA. Put it among experts and open it on blank chart. 

"You can't buy the bottom, nor sell the top. The best you can strive for is

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * LazyHedging Trading Ideas
  *   * [ **Reply to Thread** ](/thread/1058948-lazyhedging-trading-ideas/reply#reply)

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

[EurCad Analysis and Trading Ideas](/thread/360980-eurcad-analysis-and-trading-ideas "Hello my friends. 
 
As of lately I have had remarkable success in trading EurCad and after hearing other traders ideas I decided that we...") 594 replies

[FSP Trading Journal and Trend Ideas](/thread/427493-fsp-trading-journal-and-trend-ideas "hello  
I am trying to post some of my trade Ideas here. 
there will be trend following and counter trend trades. 
I will post image rather...") 16 replies

[Forex trading platform that doesn't take your ideas](/thread/311080-forex-trading-platform-that-doesnt-take-your-ideas "Ninja trader, Metatrader, Tradestation all can copy the EA and indicators straight out of your PC. 
 
How do we go about developing a...") 11 replies

[Program Your Trading Ideas without being a programmer](/thread/225629-program-your-trading-ideas-without-being-a-programmer "I have to admit, I have a lot of trading ideas, but no programming skills. I hate paying a programmer to take 3 days to write an EA for me,...") 4 replies

[Exchanging trading ideas](/thread/136764-exchanging-trading-ideas "I'm opening this thread as a substitute for live chat like msn etc to exchange trading ideas and to filter of some posts at Igrok's thread,...") 37 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/1058948-lazyhedging-trading-ideas/reply#reply)
  * Subscribe
  * [271](javascript:void\(0\);)

Attachments: LazyHedging Trading Ideas

Tags: LazyHedging Trading Ideas

#  [](/thread/1058948-lazyhedging-trading-ideas)LazyHedging Trading Ideas 

  * 

  * [#461](/thread/post/13932535#post13932535 "Post Permalink")

  * Mar 15, 2022 5:43pm  Mar 15, 2022 5:43pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar883539_1.gif) Nonip](nonip)

  * | Joined Nov 2019  | Status: Trader | [206 Posts](/search?do=process&provider=Member&searchuser=883539)

> [Quoting SwingMan](/thread/post/13932092#post13932092 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi @Nonip, I'm sorry I haven't found the right source code yet. Something has been lost.
> 
> Ignored

No pressure swingman, will wait patiently![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1). 

"You can't buy the bottom, nor sell the top. The best you can strive for is

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#462](/thread/post/13932577#post13932577 "Post Permalink")

  * Mar 15, 2022 6:14pm  Mar 15, 2022 6:14pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar337765_5.gif) dokopy](dokopy)

  * Joined May 2013 | Status: Trader | [894 Posts](/search?do=process&provider=Member&searchuser=337765)

> [Quoting Nonip](/thread/post/13932399#post13932399 "View Quoted Post")
> 
> Disliked
> 
> {quote} Yes, its EA. Put it among experts and open it on blank chart.
> 
> Ignored

Thanks, I'm glad to try it. The notification can be replaced by placing it on a demo account together with an indicator that signals the opening of trades. 

Please excuse the bad English via Google Translate.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#463](/thread/post/13941854#post13941854 "Post Permalink")

  * Mar 23, 2022 4:08am  Mar 23, 2022 4:08am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar883539_1.gif) Nonip](nonip)

  * | Joined Nov 2019  | Status: Trader | [206 Posts](/search?do=process&provider=Member&searchuser=883539)

> [Quoting SwingMan](/thread/post/13932092#post13932092 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi @Nonip, I'm sorry I haven't found the right source code yet. Something has been lost.
> 
> Ignored

Hi Swingman,  
  
Any progress on this, I'm missing so many trades and feeling really overwhelmed monitoring a number of charts concurrently. Please SAVE me here ![](https://resources.faireconomy.media/images/emojis/64/1f64f.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f64f.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f64f.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f64f.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f64f.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f64f.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f64f.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f64f.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f64f.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f64f.png?v=15.1). 

"You can't buy the bottom, nor sell the top. The best you can strive for is

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#464](/thread/post/13942097#post13942097 "Post Permalink")

  * Mar 23, 2022 9:59am  Mar 23, 2022 9:59am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting Nonip](/thread/post/13941854#post13941854 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi Swingman, Any progress on this, I'm missing so many trades and feeling really overwhelmed monitoring a number of charts concurrently. Please SAVE me here ![](https://resources.faireconomy.media/images/emojis/64/1f64f.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f64f.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f64f.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f64f.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f64f.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f64f.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f64f.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f64f.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f64f.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f64f.png?v=15.1).
> 
> Ignored

Unfortunately not. I've been suffering from a mouth infection for a week, and I can only answer you when I'm in great pain... But keep asking, maybe I'll find somewhere. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#465](/thread/post/13942387#post13942387 "Post Permalink")

  * Mar 23, 2022 4:45pm  Mar 23, 2022 4:45pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar883539_1.gif) Nonip](nonip)

  * | Joined Nov 2019  | Status: Trader | [206 Posts](/search?do=process&provider=Member&searchuser=883539)

> [Quoting SwingMan](/thread/post/13942097#post13942097 "View Quoted Post")
> 
> Disliked
> 
> {quote} Unfortunately not. I've been suffering from a mouth infection for a week, and I can only answer you when I'm in great pain... But keep asking, maybe I'll find somewhere.
> 
> Ignored

Sorry to hear this Swingman, I wish you quick recovery. 

"You can't buy the bottom, nor sell the top. The best you can strive for is

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#466](/thread/post/13942392#post13942392 "Post Permalink")

  * Mar 23, 2022 4:47pm  Mar 23, 2022 4:47pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar71675_5.gif) Alberto_Jazz](alberto_jazz)

  * Joined Jun 2008 | Status: Trader | [593 Posts](/search?do=process&provider=Member&searchuser=71675)

Hi SM, have a nice recovery! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#467](/thread/post/13942650#post13942650 "Post Permalink")

  * Mar 23, 2022 7:19pm  Mar 23, 2022 7:19pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting Nonip](/thread/post/13924419#post13924419 "View Quoted Post")
> 
> Disliked
> 
> Hello Swingman, Would like to first thank you for your contribution in FF as a whole. I however have a request regarding one your fantastic works that I rely on heavily for my trading. Could you kindly add a signal to smBBMA_Amir DB_v2.0? It does screens the pairs and give awesome signals but doesn't give an alert. {file}
> 
> Ignored

Hi @nonip,  
because I couldn't find the original code, I've now made an adjustment so that everything works.  
  
What kind of alert is that supposed to be?  
When both arrows appear with the same direction in a TimeFrame?  
  
Please compare the functionality in both EAs and write if and what differences there are. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: NZDJPY.rH1.png
Size: 22 KB](/attachment/image/4170184/thumbnail?d=1648030665)](/attachment/image/4170184?d=1648030665)   

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [smBBMA_Amir DB_v3.0.ex4](/attachment/file/4170185?d=1648030674) 52 KB | 851 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#468](/thread/post/13942781#post13942781 "Post Permalink")

  * Mar 23, 2022 8:42pm  Mar 23, 2022 8:42pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar883539_1.gif) Nonip](nonip)

  * | Joined Nov 2019  | Status: Trader | [206 Posts](/search?do=process&provider=Member&searchuser=883539)

> [Quoting SwingMan](/thread/post/13942650#post13942650 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi @nonip, because I couldn't find the original code, I've now made an adjustment so that everything works. What kind of alert is that supposed to be? When both arrows appear with the same direction in a TimeFrame? Please compare the functionality in both EAs and write if and what differences there are. {image} {file}
> 
> Ignored

Wow swingman![](https://resources.faireconomy.media/images/emojis/64/1f60d.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f60d.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f64c.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f64c.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f64c.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f64c.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f64c.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f64c.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f64c.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f64c.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f64c.png?v=15.1) You're God sent. I will have a look at both and tell precisely which alert type would be most effective. Thanks again swing man. WOW WOW WOW 

"You can't buy the bottom, nor sell the top. The best you can strive for is

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#469](/thread/post/13943160#post13943160 "Post Permalink")

  * Mar 23, 2022 11:48pm  Mar 23, 2022 11:48pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar883539_1.gif) Nonip](nonip)

  * | Joined Nov 2019  | Status: Trader | [206 Posts](/search?do=process&provider=Member&searchuser=883539)

> [Quoting SwingMan](/thread/post/13942650#post13942650 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi @nonip, because I couldn't find the original code, I've now made an adjustment so that everything works. What kind of alert is that supposed to be? When both arrows appear with the same direction in a TimeFrame? Please compare the functionality in both EAs and write if and what differences there are. {image} {file}
> 
> Ignored

I hope I’m not demanding too much Swingman. Having worked a little with programmers before, I understand how important it is for you guys that the requirements be as detailed as possible. To this end I will provide attached annotated pictures as well.  
Terminologies I will use in explaining the alerts;  
**MAHI** is MA10 & MA5 high.  
**MALO** is MA10 & MA5 low.  
I’m only interested in the re-entry alerts of BBMA and I hope that this can be achieved through the framework that already exist within the dashboard or with a little adjustment. This happens only after two conditions:  
**1.****After a CSDC (Candlestick direction confirmed)**. That is a Candlestick that closes below moving average low (MALO) and Mid BB & vice versa.   
**_For initial alert_**  
Let’s assume we have a bullish CSDC (current candlestick closes above moving average high (MAHI) and Mid BB) the dashboard should indicate an alert message such as “Bullish CSDC H4”. (This was indicated in the previous dashboard by both the round arrow for MAHI touch and a straight arrow for a bound touch).  
**_For reentry alert._**  
Now I would suggest that if within the same timeframe should price touch opposite moving averages (MALO) within the next 7 candles the dashboard should provide an alert “Bullish CSDC reentry H4”. The same should be true for a sell.  
  
NB: Kindly ignore the green large line (EMA 50) in the above picture.  
**1.****After a momentum candlestick also known as CSM**. This is a Candle stick that closes below the lower BB or above the upper BB.  
  
**_For initial alert_**  
Let’s assume we have a bullish CSM (current candlestick closes above top BB) the dashboard should indicate an alert message such as “Bullish CSM H4”. (This was indicated in the previous dashboard by a straight arrow appearing for band touch).  
  
**_For reentry alert._**  
Now I would suggest that if within the same timeframe should price touch the (MALO) moving average low within the next 7 candles the dashboard should provide an alert “Bullish CSM reentry H4”. The same should be true for a sell.  
  
I have also attached a word document for the same.  
  
Regards,  
Nonip. 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: CSM Reentry.png
Size: 20 KB](/attachment/image/4170435/thumbnail?d=1648046824)](/attachment/image/4170435?d=1648046824)   
[![Click to Enlarge

Name: Candle Stick direction confirmed-Reentry.png
Size: 9 KB](/attachment/image/4170437/thumbnail?d=1648046846)](/attachment/image/4170437?d=1648046846)   

Attached File(s)

![File Type: docx](https://assets.faireconomy.media/images/attach/docx.gif) [BBMA ALERTS DASHBOARD DOC FOR SWINGMAN ..docx](/attachment/file/4170439?d=1648046895) 136 KB | 277 downloads 

"You can't buy the bottom, nor sell the top. The best you can strive for is

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#470](/thread/post/13943168#post13943168 "Post Permalink")

  * Mar 23, 2022 11:51pm  Mar 23, 2022 11:51pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar883539_1.gif) Nonip](nonip)

  * | Joined Nov 2019  | Status: Trader | [206 Posts](/search?do=process&provider=Member&searchuser=883539)

> [Quoting Nonip](/thread/post/13943160#post13943160 "View Quoted Post")
> 
> Disliked
> 
> {quote} I hope I’m not demanding too much Swingman. Having worked a little with programmers before, I understand how important it is for you guys that the requirements be as detailed as possible. To this end I will provide attached annotated pictures as well. Terminologies I will use in explaining the alerts; MAHI is MA10 & MA5 high. MALO is MA10 & MA5 low. I’m only interested in the re-entry alerts of BBMA and I hope that this can be achieved through the framework that already exist within the dashboard or with a little adjustment. This happens...
> 
> Ignored

  
I understand that the above suggested adjustments may require your extra effort and time which may not be available now. In that case I would gladly settle for an alert whenever there's a touch of the **MALO/MAHI** and a Bollinger band at the same time on any timeframe.  
  
Regards,  
Nonip. 

"You can't buy the bottom, nor sell the top. The best you can strive for is

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#471](/thread/post/13943179#post13943179 "Post Permalink")

  * Mar 23, 2022 11:57pm  Mar 23, 2022 11:57pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1436496_1.gif) Enagy](enagy)

  * Joined Mar 2022 | Status: Trader | [1,070 Posts](/search?do=process&provider=Member&searchuser=1436496)

Pls I need someone to tell me what is happening to cadjpy right now because its not making me happy 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#472](/thread/post/13946954#post13946954 "Post Permalink")

  * Mar 27, 2022 3:32am  Mar 27, 2022 3:32am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1428829_1.gif) FundedCoffee](fundedcoffee)

  * | Joined Mar 2022  | Status: Trader | [127 Posts](/search?do=process&provider=Member&searchuser=1428829)

> [Quoting Enagy](/thread/post/13943179#post13943179 "View Quoted Post")
> 
> Disliked
> 
> Pls I need someone to tell me what is happening to cadjpy right now because its not making me happy
> 
> Ignored

CAD is strong and Yen is weak so its going up. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#473](/thread/post/13954960#post13954960 "Post Permalink")

  * Apr 2, 2022 7:44pm  Apr 2, 2022 7:44pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar883539_1.gif) Nonip](nonip)

  * | Joined Nov 2019  | Status: Trader | [206 Posts](/search?do=process&provider=Member&searchuser=883539)

> [Quoting SwingMan](/thread/post/13942650#post13942650 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi @nonip, because I couldn't find the original code, I've now made an adjustment so that everything works. What kind of alert is that supposed to be? When both arrows appear with the same direction in a TimeFrame? Please compare the functionality in both EAs and write if and what differences there are. {image} {file}
> 
> Ignored

Hello SwingMan,  
  
I hope you are well. You never got back to me regarding this post which I responded to with posts #469 and # 470. TIA.  
  
Kind regards,  
Nonip. 

"You can't buy the bottom, nor sell the top. The best you can strive for is

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#474](/thread/post/13979599#post13979599 "Post Permalink")

  * Apr 25, 2022 5:42pm  Apr 25, 2022 5:42pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar883539_1.gif) Nonip](nonip)

  * | Joined Nov 2019  | Status: Trader | [206 Posts](/search?do=process&provider=Member&searchuser=883539)

Hello SwingMan,  
  
I hope you are well. Still hoping you will assist with regards to post 456. TIA.  
  
kind regards,  
Nonip. 

"You can't buy the bottom, nor sell the top. The best you can strive for is

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#475](/thread/post/13985553#post13985553 "Post Permalink")

  * Apr 29, 2022 4:39pm  Apr 29, 2022 4:39pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting Nonip](/thread/post/13954960#post13954960 "View Quoted Post")
> 
> Disliked
> 
> ...Hello SwingMan, I hope you are well. You never got back to me regarding this post which I responded to with posts #469 and # 470. TIA. Kind regards, Nonip.
> 
> Ignored

Hi @Nonip,  
honestly, I'm very sorry that I don't have time for programming right now. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#476](/thread/post/13985570#post13985570 "Post Permalink")

  * Apr 29, 2022 4:49pm  Apr 29, 2022 4:49pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar883539_1.gif) Nonip](nonip)

  * | Joined Nov 2019  | Status: Trader | [206 Posts](/search?do=process&provider=Member&searchuser=883539)

> [Quoting SwingMan](/thread/post/13985553#post13985553 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi @Nonip, honestly, I'm very sorry that I don't have time for programming right now.
> 
> Ignored

Okay Swingman, I understand. Still very grateful for all your other tools I use![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1). 

"You can't buy the bottom, nor sell the top. The best you can strive for is

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#477](/thread/post/13987069#post13987069 "Post Permalink")

  * May 1, 2022 2:37pm  May 1, 2022 2:37pm 

  * [ lazamoro](lazamoro)

  * | Joined Feb 2011  | Status: Trader | [27 Posts](/search?do=process&provider=Member&searchuser=170548)

SR SwingMan. Are you so kind to enter BTCUSD in your indicator. Thank you very much Greetings from Tenerife Spain  
  
[smBBMA_Amir DB_v3.0.ex4](https://www.forexfactory.com/attachment.php/4170185?attachmentid=4170185&d=1648030674)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#478](/thread/post/13987247#post13987247 "Post Permalink")

  * May 1, 2022 11:39pm  May 1, 2022 11:39pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar608462_3.gif) T4Trade](t4trade)

  * Joined Sep 2017 | Status: Trend Following,Price Action,Grid | [2,484 Posts](/search?do=process&provider=Member&searchuser=608462)

> [Quoting Nonip](/thread/post/13943160#post13943160 "View Quoted Post")
> 
> Disliked
> 
> {quote} I hope I’m not demanding too much Swingman. Having worked a little with programmers before, I understand how important it is for you guys that the requirements be as detailed as possible. To this end I will provide attached annotated pictures as well. Terminologies I will use in explaining the alerts; MAHI is MA10 & MA5 high. MALO is MA10 & MA5 low. I’m only interested in the re-entry alerts of BBMA and I hope that this can be achieved through the framework that already exist within the dashboard or with a little adjustment. This happens...
> 
> Ignored

do you use this strategy? and wat is the success rate,i always liked this strategy 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#479](/thread/post/13987280#post13987280 "Post Permalink")

  * May 2, 2022 1:00am  May 2, 2022 1:00am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1428829_1.gif) FundedCoffee](fundedcoffee)

  * | Joined Mar 2022  | Status: Trader | [127 Posts](/search?do=process&provider=Member&searchuser=1428829)

> [Quoting lazamoro](/thread/post/13987069#post13987069 "View Quoted Post")
> 
> Disliked
> 
> SR SwingMan. Are you so kind to enter BTCUSD in your indicator. Thank you very much Greetings from Tenerife Spain [smBBMA_Amir DB_v3.0.ex4](https://www.forexfactory.com/attachment.php/4170185?attachmentid=4170185&d=1648030674)
> 
> Ignored

He literally wrote that he doesnt have time for programming currently 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#480](/thread/post/13987325#post13987325 "Post Permalink")

  * May 2, 2022 3:26am  May 2, 2022 3:26am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar883539_1.gif) Nonip](nonip)

  * | Joined Nov 2019  | Status: Trader | [206 Posts](/search?do=process&provider=Member&searchuser=883539)

> [Quoting T4Trade](/thread/post/13987247#post13987247 "View Quoted Post")
> 
> Disliked
> 
> {quote} do you use this strategy? and wat is the success rate,i always liked this strategy
> 
> Ignored

I did use it for a while but stopped. Its really difficult to monitor multiple pairs with this strategy so you need a good indicator or EA to compliment. It's a good strategy but you have to use good risk management like with every strategy. 

"You can't buy the bottom, nor sell the top. The best you can strive for is

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * LazyHedging Trading Ideas
  *   * [ **Reply to Thread** ](/thread/1058948-lazyhedging-trading-ideas/reply#reply)

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

[EurCad Analysis and Trading Ideas](/thread/360980-eurcad-analysis-and-trading-ideas "Hello my friends. 
 
As of lately I have had remarkable success in trading EurCad and after hearing other traders ideas I decided that we...") 594 replies

[FSP Trading Journal and Trend Ideas](/thread/427493-fsp-trading-journal-and-trend-ideas "hello  
I am trying to post some of my trade Ideas here. 
there will be trend following and counter trend trades. 
I will post image rather...") 16 replies

[Forex trading platform that doesn't take your ideas](/thread/311080-forex-trading-platform-that-doesnt-take-your-ideas "Ninja trader, Metatrader, Tradestation all can copy the EA and indicators straight out of your PC. 
 
How do we go about developing a...") 11 replies

[Program Your Trading Ideas without being a programmer](/thread/225629-program-your-trading-ideas-without-being-a-programmer "I have to admit, I have a lot of trading ideas, but no programming skills. I hate paying a programmer to take 3 days to write an EA for me,...") 4 replies

[Exchanging trading ideas](/thread/136764-exchanging-trading-ideas "I'm opening this thread as a substitute for live chat like msn etc to exchange trading ideas and to filter of some posts at Igrok's thread,...") 37 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/1058948-lazyhedging-trading-ideas/reply#reply)
  * Subscribe
  * [271](javascript:void\(0\);)

Attachments: LazyHedging Trading Ideas

Tags: LazyHedging Trading Ideas

#  [](/thread/1058948-lazyhedging-trading-ideas)LazyHedging Trading Ideas 

  * 

  * [#481](/thread/post/13987344#post13987344 "Post Permalink")

  * May 2, 2022 4:14am  May 2, 2022 4:14am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar608462_3.gif) T4Trade](t4trade)

  * Joined Sep 2017 | Status: Trend Following,Price Action,Grid | [2,484 Posts](/search?do=process&provider=Member&searchuser=608462)

> [Quoting Nonip](/thread/post/13987325#post13987325 "View Quoted Post")
> 
> Disliked
> 
> {quote} I did use it for a while but stopped. Its really difficult to monitor multiple pairs with this strategy so you need a good indicator or EA to compliment. It's a good strategy but you have to use good risk management like with every strategy.
> 
> Ignored

risk management is very importnat,so jsut pick few pairs and trade,many trades will mess up with account equity 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#482](/thread/post/14357305#post14357305 "Post Permalink")

  * Edited 8:56pm  Mar 12, 2023 8:32pm | Edited 8:56pm 

  * [ alian710](alian710)

  * | Joined May 2018  | Status: Trader | [12 Posts](/search?do=process&provider=Member&searchuser=675530)

Hello.  
Could you please tell me how to test the smBodySwitch EA_v5.0 on M1 and M5 timeframes?  
Why does it not trade on these lower timeframes?  
I want to test it on these timeframes.  
Please make it possible to trade on lower timeframes. M1, M5.  
Thanks for the tip. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#483](/thread/post/14411002#post14411002 "Post Permalink")

  * May 1, 2023 12:00pm  May 1, 2023 12:00pm 

  * [ ifx777](ifx777)

  * | Joined Apr 2023  | Status: Trader | [19 Posts](/search?do=process&provider=Member&searchuser=1628985)

> [Quoting MoneyZilla](/thread/post/13426218#post13426218 "View Quoted Post")
> 
> Disliked
> 
> {quote} Unfortunately, for you, I am keeping quite impressive library of the first three hedging ways...![](https://resources.faireconomy.media/images/emojis/64/1f923.png?v=15.1) Unfortunately, this time for me, the 4th hedge stopped working in my latest EA versions. For quite a while, it seems. When other ways were developed, the 4th one got broken. Historically the 4th was built second... Mr. Programmer will make it work again next week. Hedge 1 {image} Hedge 2 {image} Hedge 3 {image} To crack down hedging, you need an IQ below 75. If you are a happy owner of a higher IQ volumes? I am...
> 
> Ignored

Would you be willing to share the EA that you build with us? thanks. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#484](/thread/post/14411018#post14411018 "Post Permalink")

  * May 1, 2023 12:27pm  May 1, 2023 12:27pm 

  * [ ifx777](ifx777)

  * | Joined Apr 2023  | Status: Trader | [19 Posts](/search?do=process&provider=Member&searchuser=1628985)

> [Quoting SwingMan](/thread/post/13903859#post13903859 "View Quoted Post")
> 
> Disliked
> 
> New generation "5" for the BodySwitch signals and for the EA. The reference is no longer at the previous bar, but at the open of the current bar, in the direction of the main trend. The factors without optimization are 0.4, 0.3, 0.3 After my few tests, however, I have no better results than with the 3-versions, and the maximum lot number was often reached... As a conclusion - probably this is not a better version. But I will run them until a substantial loss will take place. {image} {file} {file}
> 
> Ignored

Hello,  
  
Is there a chance that you can share a source code? I would like to make some improvements to it to trading needs. thanks. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#485](/thread/post/14411260#post14411260 "Post Permalink")

  * May 1, 2023 6:10pm  May 1, 2023 6:10pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar45031_4.gif) SwingMan](swingman)

  * Joined Aug 2007 | Status: Trader | [2,653 Posts](/search?do=process&provider=Member&searchuser=45031)

> [Quoting ifx777](/thread/post/14411018#post14411018 "View Quoted Post")
> 
> Disliked
> 
> Hello, Is there a chance that you can share a source code? I would like to make some improvements to it to trading needs. thanks.
> 
> Ignored

Exceptionally, because today is May 1st, I am posting the source code for smBodySwitch for you... 

Attached File(s)

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [smBodySwitch EA_v5.0.mq4](/attachment/file/4449141?d=1682932206) 83 KB | 459 downloads 

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [smBodySwitch Signals_v5.1.mq4](/attachment/file/4449142?d=1682932209) 131 KB | 525 downloads 

![File Type: mqh](https://assets.faireconomy.media/images/attach/mqh.gif) [smBodySwitch_Include_v5.0.mqh](/attachment/file/4449143?d=1682932210) 69 KB | 439 downloads 

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#486](/thread/post/14411301#post14411301 "Post Permalink")

  * Last Post: May 1, 2023 6:57pm  May 1, 2023 6:57pm 

  * [ ifx777](ifx777)

  * | Joined Apr 2023  | Status: Trader | [19 Posts](/search?do=process&provider=Member&searchuser=1628985)

> [Quoting SwingMan](/thread/post/14411260#post14411260 "View Quoted Post")
> 
> Disliked
> 
> {quote} Exceptionally, because today is May 1st, I am posting the source code for smBodySwitch for you... {file} {file} {file}
> 
> Ignored

thank you so much!!! this is very incredible, I will make additional changes and share back with you. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * LazyHedging Trading Ideas
  *   * [ **Reply to Thread** ](/thread/1058948-lazyhedging-trading-ideas/reply#reply)

[](https://www.forexfactory.com "Homepage")

  * [Forums](forums)
  * [Trades](trades)
  * [Calendar](calendar)
  * [News](news)
  * [Market](market)
  * [Brokers](brokers)

****

[](https://www.faireconomy.com/)
