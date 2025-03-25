

  * 

[Doubling up method or playing casino](/thread/4169-doubling-up-method-or-playing-casino "Hi everyone, 
  
I was thinking about one strategy which I called doubling up method but I want to share it and you to review and make...") 24 replies

[Playing the Double-Up Game?](/thread/42119-playing-the-double-up-game "It's sure a crazy full of risk system. I was just wondering if anyone ever heard of someone doing this and winning? 
  
With this system...") 40 replies

[Playing with datetime...](/thread/36065-playing-with-datetime "Hi, 
  
Setting the date, manually, in Alert 2 to todays date, why does Alert 1 return a different value than Alert 2? Even using...") 2 replies

[Playing the Breakout Trade](/thread/6189-playing-the-breakout-trade "by Abe Cofnas 
 
When markets move, particularly in Forex, they move fast. We all have witnessed breakouts and have had the occasion to...") 4 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/739272-playing-with-the-currencies-gabin-system/reply#reply)
  * Subscribe
  * [161](javascript:void\(0\);)

Attachments: Playing with the currencies: Gabin System

Tags: Playing with the currencies: Gabin System

#  [](/thread/739272-playing-with-the-currencies-gabin-system)Playing with the currencies: Gabin System 

  * 

  * Opened Feb 26, 2018 | Never Closes | 66 Votes
  * ## Poll Results

  * 

  * Is Gabin System profitable ?
  * Yes
  * No
  * View Poll Results

Is Gabin System profitable ? |   
---|---  
_Yes_ | 39 Votes |  | 59%  
| _None_  
 _No_ | 27 Votes |  | 41%  
| _None_  
  
  * [#1](/thread/739272-playing-with-the-currencies-gabin-system "Post Permalink")

  * First Post: Edited Feb 27, 2018 3:53pm  Feb 17, 2018 5:02pm | Edited Feb 27, 2018 3:53pm 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

Hi traders  
On the picture # post 2, we can see the moves of the 8 currencies during a session. The main methods to trade are to wait for a cross of 2 currencies and to take position in the good direction. Unfortunately I have never had good results because after a cross often occurs a cross in the other direction. So I have tried another method thinking that if a currency is very strong (or weak) compared to others, its move is over or almost. But I needed a good indicator to compare the strenght ( or the weakness ) of the currency compared to others. Ezios made it ...thank you.  
This indicator modified by Ezios displays 2 important parameters : DeltaUp and DeltaDown.  
_Explanation_ :  
Currency in 1 st position ; Value of Upper Currency (VUC)  
Currency in 8 st position : Value of Lower Currency (VLC)  
Average of the 7 Others Currencies : ( A7OC )  
Calculation: DeltaUp = VUC - A7OC and DeltaDown = A7OC-VLC.  
You understand how is calculated the strenght or the weakness compared to the 7 others currencies.  
_Example_ :  
On the picture # post 3 , the upper currency is USD with 7.0.  
The average of the 7 others is ( 6.6+5.9+5.1+3.7+3.1+3.1+1.4)/7 = 4.1  
So the DeltaUp is 7.0 - 4.1 = 2.9....same calculation for DeltaDown.  
More the Delta is high more the probability of return of the currency to others is great.  
_Practice_ :  
I live in France... so the London session is perfect for me...30 mn before open until NY open...sometimes later  
I set delta = 4.4. As soon as the DeltaUp or the DeltaDown reaches this value, the indicator displays the order.  
If DeltaUp > 4.4, we sell Upper Currency basket. If DeltaDown > 4.4 , we buy Lower Currency basket.  
To trigger the orders, there are many tools. I use Dashboard Power Meter V3 cust_Curr.  
Sometimes at the beginning the market is going against us. I trigger another order at delta = 4.8 and another at 5.2.  
Of course, a SL is an absolute need.  
You can see another indication on the indicator... Delta 1/8.  
Delta 1/8 is the calculation of the upper currency versus the lower. The good value of Delta 1/8 is 7 or higher.  
In this case, the indicator displays the order. So you can trade only the pair and not the basket.  
_Close_ :  
Depending your trading style. I'm waiting for a position of the currency in middle of board ( position 4 or 5 ) to close the trades.  
I suggest strongly too the use of a lock tool to protect your gain ( see post # 39 )  
Currently Ezios and faryne are working on an EA to automate the trades with the same trigger as the indicator and 3 levels of delta.  
For instance with USD upper currency 1 st sell USD basket at 4.4... 2 nd sell USD basket at 4.8 3rd sell USD basket at 5.2.  
Of course, the levels of delta can be set by the trader according his trading style ( spacing out the deltas during the periods of volatility )  
If some coders want to work with us, they are welcome to improve Gabin System.  
  
Warning  
This thread is only for education purpose and you have not to go to live account.  
Gabin System is a countertrend system used to catch a reversal currency move.  
So it is risky especially during the periods of volatility.  
The provided tools in this thread are also for testing and haven't to be used in real account.  
But if you understand the logic and use Gabin System with your brain avoiding news, with good settings, a correct SL and a lock tool, you can make some decent pips regularly.  
Enjoy it.  
Many thanks especially for Ezios, faryne and gvc, the creator of the dashboard below.  
  
Don't forget to leave your appreciation on the poll above

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [Ezios_indy.ex4](/attachment/file/2681062?d=1518854803) 40 KB | 1,474 downloads 

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [Dashboard - Power MeterV3_Cust_Curr.mq4](/attachment/file/2681063?d=1518854815) 173 KB | 1,526 downloads 

  * [#2](/thread/post/10788435#post10788435 "Post Permalink")

  * Feb 17, 2018 5:02pm  Feb 17, 2018 5:02pm 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

Attached Image (click to enlarge)

[![Click to Enlarge

Name: 6.jpg
Size: 287 KB](/attachment/image/2681056/thumbnail?d=1518854563)](/attachment/image/2681056?d=1518854563)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#3](/thread/post/10788438#post10788438 "Post Permalink")

  * Feb 17, 2018 5:03pm  Feb 17, 2018 5:03pm 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

Attached Image

![](/attachment/image/2681057?d=1518854585)

Attached Image

![](/attachment/image/2681059?d=1518854590)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#4](/thread/post/10788439#post10788439 "Post Permalink")

  * Feb 17, 2018 5:03pm  Feb 17, 2018 5:03pm 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

Attached Image (click to enlarge)

[![Click to Enlarge

Name: 5.jpg
Size: 225 KB](/attachment/image/2681061/thumbnail?d=1518854620)](/attachment/image/2681061?d=1518854620)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#5](/thread/post/10788460#post10788460 "Post Permalink")

  * Feb 17, 2018 5:31pm  Feb 17, 2018 5:31pm 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

Example of a good trade 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: 10.jpg
Size: 297 KB](/attachment/image/2681066/thumbnail?d=1518856276)](/attachment/image/2681066?d=1518856276)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#6](/thread/post/10788508#post10788508 "Post Permalink")

  * Feb 17, 2018 6:26pm  Feb 17, 2018 6:26pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar266087_1.gif) jdva](jdva)

  * Joined Jun 2012 | Status: Trader | [1,281 Posts](/search?do=process&provider=Member&searchuser=266087)

> [Quoting madscalp](/thread/post/10788460#post10788460 "View Quoted Post")
> 
> Disliked
> 
> Example of a good trade {image}
> 
> Ignored

...looks interesting, wish you good luck ![](https://resources.faireconomy.media/images/emojis/64/1f60b.png?v=15.1)! 

I never lose - either I win or I learn...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#7](/thread/post/10788513#post10788513 "Post Permalink")

  * Edited 7:00pm  Feb 17, 2018 6:34pm | Edited 7:00pm 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

> [Quoting jdva](/thread/post/10788508#post10788508 "View Quoted Post")
> 
> Disliked
> 
> {quote} ...looks interesting, wish you good luck ![](https://resources.faireconomy.media/images/emojis/64/1f60b.png?v=15.1)!
> 
> Ignored

Thank you. The main difficulty in this system is the entry.  
We need a good entry to avoid a too important DD.  
So sometimes we have to add new baskets in order to average.  
I suggest strongly baskets with small lots.  
Syndicat, a member, tried the system this week..... IMO DD too big but good results  
[https://www.myfxbook.com/members/Str...ndmade/2421353](https://www.myfxbook.com/members/Strateg2000/handmade/2421353)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#8](/thread/post/10788756#post10788756 "Post Permalink")

  * Feb 17, 2018 10:17pm  Feb 17, 2018 10:17pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar395711_10.gif) LuXing](luxing)

  * Joined Jan 2015 | Status: Error 404: LuXing not found | [1,586 Posts](/search?do=process&provider=Member&searchuser=395711)

> [Quoting madscalp](/thread/post/10788432#post10788432 "View Quoted Post")
> 
> Disliked
> 
> Hi traders On the picture # post 2, we can see the moves of the 8 currencies during a session. The main methods to trade are to wait for a cross of 2 currencies and to take position in the good direction. Unfortunately I have never had good results because after a cross often occurs a cross in the other direction. So I have tried another method thinking that if a currency is very strong (or weak) compared to others, its move is over or almost. But I needed a good indicator to compare the strenght ( or the weakness ) of the currency compared to others....
> 
> Ignored

@Madscalp  
Nice to see that somebody is playing with currency strength numbers and devising formulas to pinpoint triggers.  
My "first love" in forex was basket trading. Since a couple of years, my trading is almost exclusively based on currency strength / weakness.  
Here's my take on what you propose...  
  
First and foremost, it is important to understand that this system is countertrend basket trading, using reversion to the mean as main trigger.  
I am not too sure if this is a good idea (combo of basket and countertrend).  
  
Baskets - with the exception of USD - are comprised of 1 major and 6 crosses.  
i.e. EUR basket: EURUSD (major), EURAUD, EURCAD, EURCHF, EURGBP, EURJPY, EURNZD (6 crosses).  
What is the common denominator in crosses ?  
Depending on what the USD is doing, once a couple of crosses start "motoring", they can get to hefty ATRs.  
i.e. look at the daily range of EURAUD, EURCAD, EURJPY, EURNZD as opposed to the major (EURUSD).  
  
Graphically, here's what the "interconnection" looks like.  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot1.png
Size: 429 KB](/attachment/image/2681132/thumbnail?d=1518870656)](/attachment/image/2681132?d=1518870656)   

  
  
Back to this "motoring" thing.  
You go countertrend on a EUR basket, but what if the bottom falls out and EUR tanks across the board ?  
The crosses will very possibly start tanking big style (read: going against you). Not 1 cross, but mostly 3 to 4.  
  
Now for your formula part.  
Delta up, Delta down, Average Other Currencies, etc.  
The currency strength meter you are using (FWIW I am using the same): 8 currencies, arithmetic mean = 4.5, the sum of the 8 currency values is _always_ 36.  
Knowing this and plugging a simple formula into Excel, it's a piece of cake to calculate your initial trigger.  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot2.png
Size: 35 KB](/attachment/image/2681135/thumbnail?d=1518871135)](/attachment/image/2681135?d=1518871135)   

  
  
You will buy a first basket when the "weaker currency" value is 0.8. At that value, your delta down >= 4.2.  
  
In terms of money management, let's assume that you have a $10K. A conservative (total) lot size for a basket would be 0.10-0.14.  
Chopped up in 7 pairs that would be 0.02 lots per pair.  
  
So, I will replay your trading scenario in slow motion.  
Please bear in mind that this is not a "black swan" scenario. This scenario will play out at least once per month, but usually 3-4 times.  
  
Friday 9 Feb.  
The time you see in the screenshot of my EAs log file is your (and my) local time. GMT +1.  
London opens, apparently shortly there is some high impact news on the GBP.  
Nice, this is maybe going to move things a bit. Let's see what direction the market takes.  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot3.png
Size: 244 KB](/attachment/image/2681139/thumbnail?d=1518871788)](/attachment/image/2681139?d=1518871788)   

  
  
Took a while, but your patience is rewarded.  
Three hours into the London session, at 12h14 to be precise a GBP long basket is triggered.  
At that moment, GBP CS (currency strength) dips below the 0.8 value.  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot4.png
Size: 197 KB](/attachment/image/2681141/thumbnail?d=1518872003)](/attachment/image/2681141?d=1518872003)   

  
  
About 40 minutes later, time to open the second GBP long basket. GBP currency strength value prints 0.40  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot5.png
Size: 4 KB](/attachment/image/2681145/thumbnail?d=1518872330)](/attachment/image/2681145?d=1518872330)   

  
  
Still no pullback, but patience. Reversion to the mean will come, right ?  
  
Well, about 1.5 hours after NY open, we get the six sigma event.  
GBP currency strength goes below 0.1 and a third GBP long basket should be opened.  
  
I am not going to run the drawdown numbers, but seeing that there was an additional drop >100 pips (GNPAUD, GBPCAD, GBPJPY) things look rather nasty.  
  
Just my thought of course, but a basket of currencies in combination with countertrend trading is something that can very easily spiral out of control.  
Happy (basket) trading !  
  
LuXing 

Wisdom begins in wonder

[0 ](javascript:void\(0\);) [6 ](javascript:void\(0\);)

  * [#9](/thread/post/10788806#post10788806 "Post Permalink")

  * Edited Feb 18, 2018 12:52am  Feb 17, 2018 11:13pm | Edited Feb 18, 2018 12:52am 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

Thx Luxing for your opinion...it's very precious  
Of course, this system is still experimental...I forgot to say it ...only demo ..no live...no overnight trading...no trading during news (currently GBP is very volatile)  
I have given a link of trades this week with 40 % profit. For me this trading is too agressive but I think that it's possible to make 1 % daily with a good management without news.  
I agree with you about issues because last tuesday JPY has been very strong during all the day dropping very late.  
In these cases, we have to accept a breakeven or a small loss: that's what happened.  
But your experience is precious since you tell that this "black scenario" can occur 2-3 times a month.  
So we need a SL. With a daily profit of 1-2 % and a SL (balance - equity) of 5 %, it's still profitable.  
Once again, we have to beware of the news in London session to optimize the trading.  
What's your trading approach with the currencies ? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#10](/thread/post/10788896#post10788896 "Post Permalink")

  * Feb 18, 2018 1:09am  Feb 18, 2018 1:09am 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

thank you Luxing for your contribution. We will try the system in demo step by step to understand  
the levels of trigger, take profit and stop loss to apply.  
Preparing me to transform the indicator into ea I post a last version where i put a black  
background box to hide the lines of graphic that disturb the vision of the values.  
I cutt off from the input x and y axis because i want all this in fixed position.  
I will continue the ea adding step by step what we need. 

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [cm_mod_v1.ex4](/attachment/file/2681198?d=1518883780) 40 KB | 615 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#11](/thread/post/10788965#post10788965 "Post Permalink")

  * Feb 18, 2018 2:14am  Feb 18, 2018 2:14am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar620434_4.gif) syndicat](syndicat)

  * | Additional Username  | Joined Oct 2017 | [432 Posts](/search?do=process&provider=Member&searchuser=620434)

> [Quoting madscalp](/thread/post/10788513#post10788513 "View Quoted Post")
> 
> Disliked
> 
> {quote} Thank you. The main difficulty in this system is the entry. We need a good entry to avoid a too important DD. So sometimes we have to add new baskets in order to average. I suggest strongly baskets with small lots. Syndicat, a member, tried the system this week..... IMO DD too big but good results [https://www.myfxbook.com/members/Str...ndmade/2421353](https://www.myfxbook.com/members/Strateg2000/handmade/2421353)
> 
> Ignored

At the moment I try to trade all signals when there is a possibility is at the computer , irrespective of sessions. 

"Money makes Money"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#12](/thread/post/10789051#post10789051 "Post Permalink")

  * Edited 5:11pm  Feb 18, 2018 4:01am | Edited 5:11pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar395711_10.gif) LuXing](luxing)

  * Joined Jan 2015 | Status: Error 404: LuXing not found | [1,586 Posts](/search?do=process&provider=Member&searchuser=395711)

> [Quoting madscalp](/thread/post/10788806#post10788806 "View Quoted Post")
> 
> Disliked
> 
> Thx Luxing for your opinion...it's very precious Of course, this system is still experimental...I forgot to say it ...only demo ..no live...no overnight trading...no trading during news (currently GBP is very volatile) I have given a link of trades this week with 40 % profit. For me **this trading is too agressive** but I think that it's possible to make 1 % daily with a good management without news. I agree with you about issues because last tuesday JPY has been very strong during all the day dropping very late. In these cases, we have to accept...
> 
> Ignored

_"this trading is too aggressive"_  
Yes it is. As a rule of thumb, consider 1 basket as a single trade.  
For conservative lot sizing take 0.1-0.15 lots / $10K capital, aggressive lot sizing 0.2-0.3 lots / $ 10K capital.  
Aggressive would be for example 0.21 lots / 7 (pairs in the basket) = 0.03 lot size per pair.  
For this sort of system it is essential to control the downside (DD). Overszing / overlevereging will kill it.  
  
_"you tell that this "black scenario" can occur 2-3 times a month"_  
It's not really a doom scenario, but part of market behaviour. This is why martingale systems eventually crash during extended moves.  
When I say 2-3 times a month, what I am really saying is that a series of correlated pairs move well beyond their 5/10/20 day Average Daily Range.  
If you get trapped on the wrong side, you will have to cater for this (trade small).  
  
_"What's your trading approach with the currencies ?"_  
I do exactly the opposite from what this system does. That is, based on currency weakness I go short (with the trend) whilst this system would go long (contrarian) expecting mean reversion. In essence, IMHO this system could be very successful using the "right" settings.  
Testing and fine tuning a system is very tedious as there are many variables with many different combinations.  
A good way to narrow down settings, variables, is by taking screenshots of key numbers at certain intervals, logging data, etc.  
  
To conclude, I will give you one important pointer.  
As I said, I do exactly the opposite from this system.  
Pareto rule: 80% of my system's trades are during the Asian session and the first hours of London. Very few trades after NY opens.  
When should your system take the majority of trades and why ?  
  
Look at the charts in [this post](https://www.forexfactory.com/showthread.php?p=9418623#post9418623)  
Bottom left is (a variant of) the xADR renko indicator.  
If (using the xADR indicator's standard setting of 20%) room up/down is exceeded it will light up in red.  
It means a pair is far up in its range and I / my EA will not trade this pair anymore because trading is about maximising possibilities.  
What do you think "your" system should do ?  
  
Hope this helps you a bit in the right direction.  
Good luck.  
  
LuXing 

Wisdom begins in wonder

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#13](/thread/post/10789134#post10789134 "Post Permalink")

  * Feb 18, 2018 6:24am  Feb 18, 2018 6:24am 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

Hi luxing  
I'm not sure I understood your way of trading with TMM....no matter.  
I agree with you this system is a countertrend trading but when the delta is big I'm considering that the move is enough important  
and that the probability of reversal seems high. Nethertheless , i agree , we need a _stoploss_.  
If members are interested by this method, let's see their results in next days.  
If they are bad, let's forget. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#14](/thread/post/10789137#post10789137 "Post Permalink")

  * Edited 6:42am  Feb 18, 2018 6:27am | Edited 6:42am 

  * [ Fxforum](fxforum)

  * | Joined Mar 2017  | Status: Trader | [118 Posts](/search?do=process&provider=Member&searchuser=564174)

> [Quoting LuXing](/thread/post/10788756#post10788756 "View Quoted Post")
> 
> Disliked
> 
> {quote} GBP currency strength goes below 0.1 and a third GBP long basket should be opened. I am not going to run the drawdown numbers, but seeing that there was an additional drop >100 pips (GNPAUD, GBPCAD, GBPJPY) things look rather nasty. Just my thought of course, but a basket of currencies in combination with countertrend trading is something that can very easily spiral out of control. Happy (basket) trading ! LuXing
> 
> Ignored

The momentum is reflected in the price. The graph is about correlation. (Nicely done, post #8) because it is my experience of its veracity. A system should be good if reflect price action, the closer to the price; the better the system. Then, no need to look for correlation. Keep it simple. If you still looking for an entry then concentrate on the graph of post #5. meaning, a filter is necessary. Now, if you decide to use the correlation you can be sure it is real. The logic of your system is very good things happens as you pointed out. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#15](/thread/post/10789244#post10789244 "Post Permalink")

  * Feb 18, 2018 8:43am  Feb 18, 2018 8:43am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar620434_4.gif) syndicat](syndicat)

  * | Additional Username  | Joined Oct 2017 | [432 Posts](/search?do=process&provider=Member&searchuser=620434)

> [Quoting madscalp](/thread/post/10789134#post10789134 "View Quoted Post")
> 
> Disliked
> 
> Hi luxing I'm not sure I understood your way of trading with TMM....no matter. I agree with you this system is a countertrend trading but when the delta is big I'm considering that the move is enough important and that the probability of reversal seems high. Nethertheless , i agree , we need a stoploss. If members are interested by this method, let's see their results in next days. If they are bad, let's forget.
> 
> Ignored

Strategy currency strength profitable and promising direction in trading. I have an Advisor who trades on this strategy.Only   
manufacturing is not the basket of orders, and the individual currencies. Here's a look monitoring:  
  
[https://www.myfxbook.com/members/Str.../fx-60/2402826](https://www.myfxbook.com/members/Strateg2000/fx-60/2402826)

"Money makes Money"

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#16](/thread/post/10789613#post10789613 "Post Permalink")

  * Edited 4:28pm  Feb 18, 2018 4:11pm | Edited 4:28pm 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

> [Quoting LuXing](/thread/post/10789051#post10789051 "View Quoted Post")
> 
> Disliked
> 
> {quote} I haved named it TMM (Total Market Movement), because it is an indication for me what has happened since the open of my broker's D1 candle. Probably best to compare it to the engine temperature of a car. It is the % ATR / ADR (5 days) measured over all 28 pairs. i.e. if in a market cycle or D1 candle of 24 hrs an average of 3.500 pips is the sum of the move in pips of 28 pairs and at a given moment the ATR measured over these 28 pairs is 700 pips (thus TMM = 0.2 or 20%). What does this tell you ? That the market as a whole has moved to its...
> 
> Ignored

Hi LuXing  
Please could you give any examples of your strategy and your W/R ?  
Many thanks. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#17](/thread/post/10789895#post10789895 "Post Permalink")

  * Feb 18, 2018 9:16pm  Feb 18, 2018 9:16pm 

  * [ mankindeg](mankindeg)

  * | Joined Mar 2015  | Status: Trader | [143 Posts](/search?do=process&provider=Member&searchuser=405444)

> [Quoting syndicat](/thread/post/10789244#post10789244 "View Quoted Post")
> 
> Disliked
> 
> {quote} Strategy currency strength profitable and promising direction in trading. I have an Advisor who trades on this strategy.Only manufacturing is not the basket of orders, and the individual currencies. Here's a look monitoring: [https://www.myfxbook.com/members/Str.../fx-60/2402826](https://www.myfxbook.com/members/Strateg2000/fx-60/2402826)
> 
> Ignored

  
Can you maybe explain this strategy a bit more in-depth. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#18](/thread/post/10789924#post10789924 "Post Permalink")

  * Feb 18, 2018 9:38pm  Feb 18, 2018 9:38pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar313004_2.gif) braintheboss](braintheboss)

  * Joined Nov 2012 | Status: Coder | [8,520 Posts](/search?do=process&provider=Member&searchuser=313004)

> [Quoting madscalp](/thread/post/10788438#post10788438 "View Quoted Post")
> 
> Disliked
> 
> {image}{image}
> 
> Ignored

Knowing CSM have that calculation made but not showed ( only shows arrows ) but other systems like EAX uses that approach then what is the new here? 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot_20180218-124223.png
Size: 1.6 MB](/attachment/image/2681723/thumbnail?d=1518957764)](/attachment/image/2681723?d=1518957764)   

Try don't lose pants never...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#19](/thread/post/10789954#post10789954 "Post Permalink")

  * Feb 18, 2018 9:57pm  Feb 18, 2018 9:57pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar620434_4.gif) syndicat](syndicat)

  * | Additional Username  | Joined Oct 2017 | [432 Posts](/search?do=process&provider=Member&searchuser=620434)

> [Quoting mankindeg](/thread/post/10789895#post10789895 "View Quoted Post")
> 
> Disliked
> 
> {quote} Can you maybe explain this strategy a bit more in-depth.
> 
> Ignored

  
Post 1, post 18  
  
<https://www.forexfactory.com/showthread.php?t=532236>

"Money makes Money"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#20](/thread/post/10790065#post10790065 "Post Permalink")

  * Feb 18, 2018 11:27pm  Feb 18, 2018 11:27pm 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

> [Quoting Husky77](/thread/post/10789933#post10789933 "View Quoted Post")
> 
> Disliked
> 
> just a little thing to add on your first post -the place from where you have this dashboard. -who made it -and a bit of friendly behaviour for the original coder who created this <https://www.forexfactory.com/gvc> otherwise some may think at some point in your journey you can start selling something as you have the code and you can edit that as your wish.if you want i can show you few places where those free codes are for sell renamed and edited of course.thats why no more free codes for recent of those dashboards are not shared in FF....
> 
> Ignored

Hi man...calm I sell nothing. These tools are available in FF. Really a big thank at the creators mainly gvc. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Playing with the currencies: Gabin System
  *   * [ **Reply to Thread** ](/thread/739272-playing-with-the-currencies-gabin-system/reply#reply)

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

[Doubling up method or playing casino](/thread/4169-doubling-up-method-or-playing-casino "Hi everyone, 
  
I was thinking about one strategy which I called doubling up method but I want to share it and you to review and make...") 24 replies

[Playing the Double-Up Game?](/thread/42119-playing-the-double-up-game "It's sure a crazy full of risk system. I was just wondering if anyone ever heard of someone doing this and winning? 
  
With this system...") 40 replies

[Playing with datetime...](/thread/36065-playing-with-datetime "Hi, 
  
Setting the date, manually, in Alert 2 to todays date, why does Alert 1 return a different value than Alert 2? Even using...") 2 replies

[Playing the Breakout Trade](/thread/6189-playing-the-breakout-trade "by Abe Cofnas 
 
When markets move, particularly in Forex, they move fast. We all have witnessed breakouts and have had the occasion to...") 4 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/739272-playing-with-the-currencies-gabin-system/reply#reply)
  * Subscribe
  * [161](javascript:void\(0\);)

Attachments: Playing with the currencies: Gabin System

Tags: Playing with the currencies: Gabin System

#  [](/thread/739272-playing-with-the-currencies-gabin-system)Playing with the currencies: Gabin System 

  * 

  * [#21](/thread/post/10790074#post10790074 "Post Permalink")

  * Feb 18, 2018 11:29pm  Feb 18, 2018 11:29pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar373306_81.gif) Sparrow](sparrow)

  * Joined May 2014 | Status: Trader | [4,734 Posts](/search?do=process&provider=Member&searchuser=373306)

> [Quoting madscalp](/thread/post/10790065#post10790065 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi man...calm I sell nothing. These tools are available in FF. Really a big thank at the creators mainly gvc.
> 
> Ignored

do not mind me please.   
since some time everyone is a suspect for me ![](https://resources.faireconomy.media/images/emojis/64/1f602.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f602.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f602.png?v=15.1)  
out of this yes your new aproach is ... good 

Take what you can, give nothing back

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#22](/thread/post/10790095#post10790095 "Post Permalink")

  * Feb 18, 2018 11:44pm  Feb 18, 2018 11:44pm 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

> [Quoting Husky77](/thread/post/10790074#post10790074 "View Quoted Post")
> 
> Disliked
> 
> {quote} do not mind me please. since some time everyone is a suspect for me ![](https://resources.faireconomy.media/images/emojis/64/1f602.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f602.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f602.png?v=15.1) out of this yes your new aproach is ... good
> 
> Ignored

the only file ex4 provided here is the Ezios' s work but luXing showed that a single CM_Strength may be enough. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#23](/thread/post/10790355#post10790355 "Post Permalink")

  * Feb 19, 2018 2:03am  Feb 19, 2018 2:03am 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

> [Quoting madscalp](/thread/post/10790095#post10790095 "View Quoted Post")
> 
> Disliked
> 
> {quote} the only file ex4 provided here is the Ezios' s work but luXing showed that a single CM_Strength may be enough.
> 
> Ignored

exactly. I want to follow the rules of madscalp and to build an auto trading ea for this rules and we will see how this will go.  
if someone wants to trade this system manually there are already the tools to do it. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#24](/thread/post/10790421#post10790421 "Post Permalink")

  * Feb 19, 2018 2:48am  Feb 19, 2018 2:48am 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

> [Quoting Ezios](/thread/post/10790355#post10790355 "View Quoted Post")
> 
> Disliked
> 
> {quote} exactly. I want to follow the rules of madscalp and to build an auto trading ea for this rules and we will see how this will go. if someone wants to trade this system manually there are already the tools to do it.
> 
> Ignored

Thanks Ezios. Don't forget 3 levels and a SL. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#25](/thread/post/10790625#post10790625 "Post Permalink")

  * Feb 19, 2018 4:53am  Feb 19, 2018 4:53am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar395711_10.gif) LuXing](luxing)

  * Joined Jan 2015 | Status: Error 404: LuXing not found | [1,586 Posts](/search?do=process&provider=Member&searchuser=395711)

> [Quoting madscalp](/thread/post/10789134#post10789134 "View Quoted Post")
> 
> Disliked
> 
> If members are interested by this method, let's see their results in next days. If they are bad, let's forget.
> 
> Ignored

Not the best of ways to determine if a strategy has potential (unless traded 100% mechanically using the same EA, .set file, and broker).  
Give a strategy to 10 different traders, they will all have completely different results. You want to be basing your decision on that ?  
  

> [Quoting madscalp](/thread/post/10789613#post10789613 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi LuXing Please could you give any examples of your strategy and your W/R ? Many thanks.
> 
> Ignored

My strategy ?  
As outlined in post #8, it is based on currency strength / weakness, going with the trend (away from the daily open) strongly biased toward shortselling.   
It is documented in > 1000 posts, many of which include rationale and screenshots, in [this](https://www.forexfactory.com/showthread.php?t=487923) thread.  
  
W/R ?  
If you refer to win rate, this is a totally irrelevant performance metric.  
What if I were to tell you that my system/robot has a 92% winrate ?  
But based on a sample size of 100 trades I have 92 winners x 5 pips = 460 pips. The 8 losers x 100 pips SL = -800 pips...  
Is this system profitable ? Could be, but that would depend on the position size of each trade...  
Even the number of pips is not a good performance metric. Last time I checked, my mortgage had to be paid in €€€, not in win rate % nor in pips.  
Without going into too much details, profit factor, peak to though drawdown, % equity growth measured over an extended period are far more revealing for a trader/system performance. Read Van Tharpe's "definite guide to position sizing" book. Even though it's 10 years old, it's an excellent manual to measure a strategy's performance (or even 1 strategy traded using an infinite number of settings).  
  

> [Quoting syndicat](/thread/post/10789244#post10789244 "View Quoted Post")
> 
> Disliked
> 
> {quote} Strategy currency strength profitable and promising direction in trading. I have an Advisor who trades on this strategy.Only manufacturing is not the basket of orders, and the individual currencies. Here's a look monitoring: [https://www.myfxbook.com/members/Str.../fx-60/2402826](https://www.myfxbook.com/members/Strateg2000/fx-60/2402826)
> 
> Ignored

Decent results. But...  
Not much point in posting a demo TE and hiding your entries.  
If you are afraid of some Chinese guy reverse engineering your EA, better not posting the link to the TE in the first place.  
Unless of course the TE is to attract investors, in which case it should be a real account and your post belongs in the Commercial Section.  
Observations at a quick glance (before you were hiding your history): 6 trading days, 200 trades in total of which half involved scaling in.  
Need bigger trade sample size (z-score it), I haven't seen control mechanism for the downside (equity stoploss of 40% ?).  
  
Happy trading guys.  
  
LuXing 

Wisdom begins in wonder

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#26](/thread/post/10790787#post10790787 "Post Permalink")

  * Feb 19, 2018 6:18am  Feb 19, 2018 6:18am 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

@ Luxing  
I know the best system in Forex is to go with the trend...with the currencies too.  
But the problem is that I don't know _when the trend starts_. Nobody knows it. With the excellent dashboards available in FF, I have tried also methods to determine the entry.  
Sometimes it's working sometimes it's too late...the move is over.  
A trading style is based on the probability of win with decent signals.  
I don't know the signals of the beginning of a trend...you maybe ?  
So I'm thinking that when a currency is very strong ( or very weak ) versus the others, there is a probability of reversal under certain conditions ( no news , good money management, SL )  
Even a simple pullback can be profitable with a lock tool....it's even better if the trend change totally.  
Every method has its own risk...yours too.  
I understood that you don't like the system. ...you have warned the readers...thank you. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#27](/thread/post/10791009#post10791009 "Post Permalink")

  * Feb 19, 2018 8:47am  Feb 19, 2018 8:47am 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

Madscalp we want to make this system as simple as possible.  
so i will put in the ea only the needed.lot size, magic number, stop loss in currency,  
take profit in currency, and the signal delta delta1 and delta2 where the ea must to open  
the 3 baskets. perhaps also a buttom close all is useful when one wants to stop all and close the ea.  
and this ea will work only for demo accounts. work in progress.... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#28](/thread/post/10791147#post10791147 "Post Permalink")

  * Edited 10:56am  Feb 19, 2018 10:44am | Edited 10:56am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar620434_4.gif) syndicat](syndicat)

  * | Additional Username  | Joined Oct 2017 | [432 Posts](/search?do=process&provider=Member&searchuser=620434)

> [Quoting LuXing](/thread/post/10790625#post10790625 "View Quoted Post")
> 
> Disliked
> 
> {quote} Not the best of ways to determine if a strategy has potential (unless traded 100% mechanically using the same EA, .set file, and broker). Give a strategy to 10 different traders, they will all have completely different results. You want to be basing your decision on that ? {quote} My strategy ? As outlined in post #8, it is based on currency strength / weakness, going with the trend (away from the daily open) strongly biased toward shortselling. It is documented in > 1000 posts, many of which include rationale and screenshots, in [this](https://www.forexfactory.com/showthread.php?t=487923)...
> 
> Ignored

  
Beautiful and much writing but the practical advice is not given and only expressed their criticism. To listen to your advice, I would like to make sure that your strategy is profitable. Show me monitoring?  
  
In this topic no one nothing not sells. We are trying to improve this strategy. 

"Money makes Money"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#29](/thread/post/10791512#post10791512 "Post Permalink")

  * Edited 3:50pm  Feb 19, 2018 3:02pm | Edited 3:50pm 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

> [Quoting syndicat](/thread/post/10791147#post10791147 "View Quoted Post")
> 
> Disliked
> 
> {quote} Beautiful and much writing but the practical advice is not given and only expressed their criticism. To listen to your advice, I would like to make sure that your strategy is profitable. Show me monitoring? In this topic no one nothing not sells. We are trying to improve this strategy.
> 
> Ignored

You are right...the LuXing's warning is heard  
but his strategy seems logic, not yet profitable. 

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [NewsCal-v107.ex4](/attachment/file/2682300?d=1519020360) 29 KB | 321 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#30](/thread/post/10791586#post10791586 "Post Permalink")

  * Feb 19, 2018 3:58pm  Feb 19, 2018 3:58pm 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

> [Quoting Ezios](/thread/post/10791009#post10791009 "View Quoted Post")
> 
> Disliked
> 
> Madscalp we want to make this system as simple as possible. so i will put in the ea only the needed.lot size, magic number, stop loss in currency, take profit in currency, and the signal delta delta1 and delta2 where the ea must to open the 3 baskets. perhaps also a buttom close all is useful when one wants to stop all and close the ea. and this ea will work only for demo accounts. work in progress....
> 
> Ignored

Correct. Lot size is important ![](https://resources.faireconomy.media/images/emojis/64/1f600.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f600.png?v=15.1) because the basket have to be composed with small lots (0.01) to make the average. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#31](/thread/post/10791600#post10791600 "Post Permalink")

  * Feb 19, 2018 4:10pm  Feb 19, 2018 4:10pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar620434_4.gif) syndicat](syndicat)

  * | Additional Username  | Joined Oct 2017 | [432 Posts](/search?do=process&provider=Member&searchuser=620434)

Hi Madscalp . Today I started trading in the Asian session. Sold AUD, NZD, bought JPY, USD - closed at a profit 

"Money makes Money"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#32](/thread/post/10791648#post10791648 "Post Permalink")

  * Feb 19, 2018 4:30pm  Feb 19, 2018 4:30pm 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

> [Quoting syndicat](/thread/post/10791600#post10791600 "View Quoted Post")
> 
> Disliked
> 
> Hi Madscalp . Today I started trading in the Asian session. Sold AUD, NZD, bought JPY, USD - closed at a profit
> 
> Ignored

Yes I have seen a signal buy JPY at 6:40 GMT outside my hours of trading.  
What's your delta ? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#33](/thread/post/10791654#post10791654 "Post Permalink")

  * Feb 19, 2018 4:32pm  Feb 19, 2018 4:32pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar620434_4.gif) syndicat](syndicat)

  * | Additional Username  | Joined Oct 2017 | [432 Posts](/search?do=process&provider=Member&searchuser=620434)

> [Quoting madscalp](/thread/post/10791648#post10791648 "View Quoted Post")
> 
> Disliked
> 
> {quote} Yes I have seen a signal buy JPY at 6:40 GMT outside my hours of trading. What's your delta ?
> 
> Ignored

4 

"Money makes Money"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#34](/thread/post/10791662#post10791662 "Post Permalink")

  * Feb 19, 2018 4:34pm  Feb 19, 2018 4:34pm 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

> [Quoting syndicat](/thread/post/10791654#post10791654 "View Quoted Post")
> 
> Disliked
> 
> {quote} 4
> 
> Ignored

Maybe you can set a bit more.... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#35](/thread/post/10791664#post10791664 "Post Permalink")

  * Feb 19, 2018 4:36pm  Feb 19, 2018 4:36pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar620434_4.gif) syndicat](syndicat)

  * | Additional Username  | Joined Oct 2017 | [432 Posts](/search?do=process&provider=Member&searchuser=620434)

> [Quoting madscalp](/thread/post/10791662#post10791662 "View Quoted Post")
> 
> Disliked
> 
> {quote} Maybe you can set a bit more....
> 
> Ignored

I, too, think increase until 4.5 

"Money makes Money"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#36](/thread/post/10791692#post10791692 "Post Permalink")

  * Feb 19, 2018 4:47pm  Feb 19, 2018 4:47pm 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

For any reason, the Dasboard PowerMeter V3 is not working currently ....and you ? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#37](/thread/post/10791720#post10791720 "Post Permalink")

  * Feb 19, 2018 4:55pm  Feb 19, 2018 4:55pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar620434_4.gif) syndicat](syndicat)

  * | Additional Username  | Joined Oct 2017 | [432 Posts](/search?do=process&provider=Member&searchuser=620434)

> [Quoting madscalp](/thread/post/10791692#post10791692 "View Quoted Post")
> 
> Disliked
> 
> For any reason, the Dasboard PowerMeter V3 is not working currently ....and you ?
> 
> Ignored

I have works 

"Money makes Money"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#38](/thread/post/10791762#post10791762 "Post Permalink")

  * Edited 5:34pm  Feb 19, 2018 5:06pm | Edited 5:34pm 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

> [Quoting syndicat](/thread/post/10791720#post10791720 "View Quoted Post")
> 
> Disliked
> 
> {quote} I have works
> 
> Ignored

I set again and it's OK now...CPU issue on my computer ?  
Arrrgh I missed sell AUD a bit after London open 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#39](/thread/post/10792225#post10792225 "Post Permalink")

  * Feb 19, 2018 7:57pm  Feb 19, 2018 7:57pm 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

Discussion about the London session today :  
I say again:  
\- my time of trading is 30 mn before London open until NY open  
\- my delta is 4.3 then 4.6 then 5  
Today according with the rules...only 2 possible trades ( I missed both due at a computer issue ...no matter )  
\- Sell AUD basket a bit after London open  
AUD first dropped to go up again  
I strongly suggest to use a lock tool...I'm using the settings of the dashboard but you can use another EA ( see below)  
so when your trade is in a positive territory, you have to use it to protect your trade  
for AUD it was a simple pullback but with a lock tool you get a small profit or a breakeven  
\- Buy JPY basket a bit before 10:00 GMT  
same thought  
Quiet day...bad for trading..I'd just gained a few pips selling USDPY and AUDJPY at LO...on another computer...lol  
The session is not over but I wait nothing. Have a good day. Beware of overtrading. 

Attached Image

![](/attachment/image/2682564?d=1519037771)

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [CM Position Manager.ex4](/attachment/file/2682567?d=1519037819) 12 KB | 366 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#40](/thread/post/10793776#post10793776 "Post Permalink")

  * Feb 20, 2018 2:56am  Feb 20, 2018 2:56am 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

Finally I repaired my computer and I've shorted USD in NY session ( just for test ) ...2 baskets  
daily goal reached....350 pips 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: 12.jpg
Size: 267 KB](/attachment/image/2683200/thumbnail?d=1519062921)](/attachment/image/2683200?d=1519062921)   
[![Click to Enlarge

Name: 13.jpg
Size: 58 KB](/attachment/image/2683202/thumbnail?d=1519062929)](/attachment/image/2683202?d=1519062929)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Playing with the currencies: Gabin System
  *   * [ **Reply to Thread** ](/thread/739272-playing-with-the-currencies-gabin-system/reply#reply)

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

[Doubling up method or playing casino](/thread/4169-doubling-up-method-or-playing-casino "Hi everyone, 
  
I was thinking about one strategy which I called doubling up method but I want to share it and you to review and make...") 24 replies

[Playing the Double-Up Game?](/thread/42119-playing-the-double-up-game "It's sure a crazy full of risk system. I was just wondering if anyone ever heard of someone doing this and winning? 
  
With this system...") 40 replies

[Playing with datetime...](/thread/36065-playing-with-datetime "Hi, 
  
Setting the date, manually, in Alert 2 to todays date, why does Alert 1 return a different value than Alert 2? Even using...") 2 replies

[Playing the Breakout Trade](/thread/6189-playing-the-breakout-trade "by Abe Cofnas 
 
When markets move, particularly in Forex, they move fast. We all have witnessed breakouts and have had the occasion to...") 4 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/739272-playing-with-the-currencies-gabin-system/reply#reply)
  * Subscribe
  * [161](javascript:void\(0\);)

Attachments: Playing with the currencies: Gabin System

Tags: Playing with the currencies: Gabin System

#  [](/thread/739272-playing-with-the-currencies-gabin-system)Playing with the currencies: Gabin System 

  * 

  * [#41](/thread/post/10794118#post10794118 "Post Permalink")

  * Feb 20, 2018 5:06am  Feb 20, 2018 5:06am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar44734_21.gif) Pips_Cruiser](pips_cruiser)

  * Joined Jul 2007 | Status: Following The Trade Winds | [8,442 Posts](/search?do=process&provider=Member&searchuser=44734)

> [Quoting LuXing](/thread/post/10788756#post10788756 "View Quoted Post")
> 
> Disliked
> 
> {quote} @Madscalp Nice to see that somebody is playing with currency strength numbers and devising formulas to pinpoint triggers. My "first love" in forex was basket trading. Since a couple of years, my trading is almost exclusively based on currency strength / weakness. Here's my take on what you propose ... LuXing
> 
> Ignored

Excellent post! ![](https://resources.faireconomy.media/images/emojis/64/1f60e.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#42](/thread/post/10794576#post10794576 "Post Permalink")

  * Feb 20, 2018 8:28am  Feb 20, 2018 8:28am 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

Good night buys, the first version is ready.  
Keep in mind that it works only on demo account and it will open baskets following the  
rule of madscalp. when it reaches first loss or first gain it will not open more baskets.  
if you want to trade more you have to remove and restart. ok?  
enjoy it and let me know about the results.  
as it is a automatic trading no time filter only takes signal. no more than 1 basket for every signal detected. bye. 

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [pwtcea.ex4](/attachment/file/2683416?d=1519082897) 95 KB | 268 downloads 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#43](/thread/post/10794587#post10794587 "Post Permalink")

  * Feb 20, 2018 8:35am  Feb 20, 2018 8:35am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar395711_10.gif) LuXing](luxing)

  * Joined Jan 2015 | Status: Error 404: LuXing not found | [1,586 Posts](/search?do=process&provider=Member&searchuser=395711)

> [Quoting madscalp](/thread/post/10790787#post10790787 "View Quoted Post")
> 
> Disliked
> 
> @ Luxing I know the best system in Forex is to go with the trend...with the currencies too. But the problem is that I don't know when the trend starts. Nobody knows it. With the excellent dashboards available in FF, I have tried also methods to determine the entry. Sometimes it's working sometimes it's too late...the move is over. A trading style is based on the probability of win with decent signals. I don't know the signals of the beginning of a trend...you maybe ? So I'm thinking that when a currency is very strong ( or very weak ) versus the...
> 
> Ignored

_"I know the best system in Forex is to go with the trend...with the currencies too."_  
“Best” is subjective, to say the least.  
Fan boys of trading with the trend are firm believers of Newton’s laws of motion but not everybody’s a fan of Isaac Newton.  
  
_"But the problem is that I don't know _when the trend starts_. Nobody knows it."_  
I agree with you: nobody knows when the trend starts.   
I will even take this one step further: nobody knows what a trend is !!!   
Is a trend a H1 candle starting at minute zero ? Or maybe a never ending floating 60 x M1 tendency ? Is it the direction of EURUSD since the inception of the Euro ?   
  
_"With the excellent dashboards available in FF, I have tried also methods to determine the entry. Sometimes it's working sometimes it's too late...the move is over."_There is a great collection of dashboards on FF, made by really gifted coders.  
To my knowledge, none are (consistently) profitable in full automatic mode.  
If there was one, Forexfactory would be out of business because we would all be filling our pockets, driving Ferraris and having cocktails with the most gorgeous women.  
As you said, it works until it doesn’t. But then, I think there is no such thing as “one size fits all” (read: 1 .set file for a dashboard EA is suitable for all market circumstances). That is usually the point where traders start curve fitting and devising conservative, moderate and aggressive set files for a robot.   
  
_"A trading style is based on the probability of win with decent signals.  
I don't know the signals of the beginning of a trend...you maybe ?"_  
Yes, of course I know the signals of the beginning of a trend.   
I am not being a smartass here, but the answer is very simple: look in the mirror…   
You, and only you decide whether or not the trigger should be pulled for a trade on your account. Pulling the trigger means that a pre-defined set of criteria signals a “GO”. Who is it who defines these criteria and who defines when these criteria are met ?  
  
  
_"So I'm thinking that when a currency is very strong ( or very weak ) versus the others, there is a probability of reversal under certain conditions ( no news , good money management, SL )"_  
I agree 99%. The 1% is regarding news. It can be your friend in a trade, but also cause nasty slippage or high DD if things do not work out the way you thought.  
  
_“Even a simple pullback can be profitable with a lock tool....it's even better if the trend change totally. ”_  
Yes, you can trail. Have to give it room to breathe though. % of ATR could be a decent measure.  
Again, trend change ? What is a trend ;-)  
  
_“Every method has its own risk...yours too. ”_  
Of course, we would not be trading if we were not embracing the fact that each trade has an uncertain outcome and risk.  
That goes – without exception – for all trading strategies. My strategy is certainly not an exception.  
__  
_“I understood that you don't like the system. ...you have warned the readers..._  
_thank you.”_  
  
You’re welcome but you misunderstood. It’s quite the contrary.   
I like systems that have an edge and I believe that this system has an edge.   
We just differ on how to exploit that edge.  
I discreetly gave a hint on the exploitation of one of the aspects of the edge in post #12.  
  
Most will agree that if an edge is not exploited properly and/or if the downside (DD) isn’t strictly controlled the edge and therewith the likelihood of profitability is gone.   
  
Maybe. Maybe not.  
  
Who is to say, after all it’s mostly the blind leading the blind in FF.  
  
LuXing 

Wisdom begins in wonder

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#44](/thread/post/10795157#post10795157 "Post Permalink")

  * Feb 20, 2018 2:20pm  Feb 20, 2018 2:20pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar620434_4.gif) syndicat](syndicat)

  * | Additional Username  | Joined Oct 2017 | [432 Posts](/search?do=process&provider=Member&searchuser=620434)

> [Quoting Ezios](/thread/post/10794576#post10794576 "View Quoted Post")
> 
> Disliked
> 
> Good night buys, the first version is ready. Keep in mind that it works only on demo account and it will open baskets following the rule of madscalp. when it reaches first loss or first gain it will not open more baskets. if you want to trade more you have to remove and restart. ok? enjoy it and let me know about the results. as it is a automatic trading no time filter only takes signal. no more than 1 basket for every signal detected. bye. {file}
> 
> Ignored

  
hi Ezios ! Good job, I checked the shopping cart opens correctly! I propose to add the selection function of a basket of currencies(AUD/NZD/EUR/JPY/AUD/USD/GBP/CHF) at which it will trade, I open the recycle bin by drawdown in percentage, I think it would be better. 

"Money makes Money"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#45](/thread/post/10795232#post10795232 "Post Permalink")

  * Feb 20, 2018 3:03pm  Feb 20, 2018 3:03pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar556193_1.gif) Fatso](fatso)

  * | Joined Feb 2017  | Status: Trader | [111 Posts](/search?do=process&provider=Member&searchuser=556193)

> [Quoting Ezios](/thread/post/10794576#post10794576 "View Quoted Post")
> 
> Disliked
> 
> Good night buys, the first version is ready. Keep in mind that it works only on demo account and it will open baskets following the rule of madscalp. when it reaches first loss or first gain it will not open more baskets. if you want to trade more you have to remove and restart. ok? enjoy it and let me know about the results. as it is a automatic trading no time filter only takes signal. no more than 1 basket for every signal detected. bye. {file}
> 
> Ignored

On my side the EA is not uploading; maybe I am missing something. I will check again.   
HOWEVER I opened the trades manually. I had a USD basket during Asia session and closed with 100 plus pips profit. I later got AUD basket and it is currently running. Will update result by close of business after trading London and US sessions 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#46](/thread/post/10795236#post10795236 "Post Permalink")

  * Feb 20, 2018 3:04pm  Feb 20, 2018 3:04pm 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

> [Quoting syndicat](/thread/post/10795157#post10795157 "View Quoted Post")
> 
> Disliked
> 
> {quote} hi Ezios ! Good job, I checked the shopping cart opens correctly! I propose to add the selection function of a basket of currencies(AUD/NZD/EUR/JPY/AUD/USD/GBP/CHF) at which it will trade, I open the recycle bin by drawdown in percentage, I think it would be better.
> 
> Ignored

i dont want to put any button on this robot apart that there are. this is a full automatic sistem.  
if ou have a signal to add and a trigger rule i can add the trigger rule and the signal but no buttons.  
if ou want to trade with buttons in ff there are toons of dashboards. try this robot for the original setting  
or change the risk/reward as you want. that's all. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#47](/thread/post/10795259#post10795259 "Post Permalink")

  * Edited 5:26pm  Feb 20, 2018 3:22pm | Edited 5:26pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar620434_4.gif) syndicat](syndicat)

  * | Additional Username  | Joined Oct 2017 | [432 Posts](/search?do=process&provider=Member&searchuser=620434)

> [Quoting Ezios](/thread/post/10795236#post10795236 "View Quoted Post")
> 
> Disliked
> 
> {quote} i dont want to put any button on this robot apart that there are. this is a full automatic sistem. if ou have a signal to add and a trigger rule i can add the trigger rule and the signal but no buttons. if ou want to trade with buttons in ff there are toons of dashboards. try this robot for the original setting or change the risk/reward as you want. that's all.
> 
> Ignored

Don't need buttons. You need to install one copy of the EA for example for the AUD basket, another copy for the NZD basket, and then  
The EA closes a basket of different currencies all together. you need to close the basket for each currency separately.  
  
  
error:  
2018.02.20 15:36:30.847 '29660177': order sell 0.01 EURGBP opening at market sl: 0.00000 tp: 0.00000 failed [Off quotes]  
  
[me_TradingDashboard v3.mq4](https://www.forexfactory.com/attachment.php/2676832?attachmentid=2676832&d=1518609399) \- Ezios this panel is not working correctly. I already wrote about it 

"Money makes Money"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#48](/thread/post/10795500#post10795500 "Post Permalink")

  * Edited 5:24pm  Feb 20, 2018 5:07pm | Edited 5:24pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar523703_1.gif) faryne](faryne)

  * | Joined Oct 2016  | Status: Trader | [93 Posts](/search?do=process&provider=Member&searchuser=523703)

> [Quoting Ezios](/thread/post/10794576#post10794576 "View Quoted Post")
> 
> Disliked
> 
> Good night buys, the first version is ready. Keep in mind that it works only on demo account and it will open baskets following the rule of madscalp. when it reaches first loss or first gain it will not open more baskets. if you want to trade more you have to remove and restart. ok? enjoy it and let me know about the results. as it is a automatic trading no time filter only takes signal. no more than 1 basket for every signal detected. bye. {file}
> 
> Ignored

Is it possible to set a TP/SL on each open basket (for now, the TP apply on all open orders, so it can be 1/2/3/... baskets).  
(+ add a reverse option to trade trend instead of mean reverting)  
Thanks 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#49](/thread/post/10795554#post10795554 "Post Permalink")

  * Feb 20, 2018 5:24pm  Feb 20, 2018 5:24pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar409665_1.gif) Fancysegs](fancysegs)

  * | Joined Apr 2015  | Status: Trader | [52 Posts](/search?do=process&provider=Member&searchuser=409665)

this indicator works very well...I have filter a way to use it to minimize continuous drawdown...Thanks to the originator of this indicator...I will keep posting on anything new i found on this...it will be good if you can code the one we can select time frame like 30 min to 1day 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#50](/thread/post/10795726#post10795726 "Post Permalink")

  * Edited 6:31pm  Feb 20, 2018 6:12pm | Edited 6:31pm 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

Thank you Ezios for your work.  
Currently the EA seems to open the baskets correctly...to see over time if there is not issue.  
Later -it's true - you can do a close basket by basket and a close all emergency....it would take a dashboard ...hmmmm.  
Take your time...you're the only coder here.  
@ syndicat I don't understand all about your trades  
you don't close always your baskets ? overnight trading ?  
[https://www.myfxbook.com/members/Str...ndmade/2421353](https://www.myfxbook.com/members/Strateg2000/handmade/2421353)  
@ LuXing who said "Who is to say, after all it’s mostly the blind leading the blind in FF."  
I like this philosophic thought...happily there are a few one-eyed men in FF ![](https://resources.faireconomy.media/images/emojis/64/1f600.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f600.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#51](/thread/post/10795807#post10795807 "Post Permalink")

  * Feb 20, 2018 6:30pm  Feb 20, 2018 6:30pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar620434_4.gif) syndicat](syndicat)

  * | Additional Username  | Joined Oct 2017 | [432 Posts](/search?do=process&provider=Member&searchuser=620434)

> [Quoting madscalp](/thread/post/10795726#post10795726 "View Quoted Post")
> 
> Disliked
> 
> Thank you Ezios for your work. Currently the EA seems to open the baskets correctly...to see over time if there is not issue. Later -it's true - you can do a close basket by basket and a close all emergency....it would take a dashboard ...hmmmm. Take your time...you're the only coder here. @ syndicat I don't understand all about your trades you don't close always your baskets ? overnight trading ? [https://www.myfxbook.com/members/Str...ndmade/2421353](https://www.myfxbook.com/members/Strateg2000/handmade/2421353)
> 
> Ignored

  
I begin to trade during the Asian session my time zone is GMT + 8 

"Money makes Money"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#52](/thread/post/10795816#post10795816 "Post Permalink")

  * Feb 20, 2018 6:35pm  Feb 20, 2018 6:35pm 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

> [Quoting syndicat](/thread/post/10795807#post10795807 "View Quoted Post")
> 
> Disliked
> 
> {quote} I begin to trade during the Asian session my time zone is GMT + 8
> 
> Ignored

Ah OK you are russian.   
Greetings from France. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#53](/thread/post/10795870#post10795870 "Post Permalink")

  * Feb 20, 2018 6:51pm  Feb 20, 2018 6:51pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar620434_4.gif) syndicat](syndicat)

  * | Additional Username  | Joined Oct 2017 | [432 Posts](/search?do=process&provider=Member&searchuser=620434)

> [Quoting madscalp](/thread/post/10795816#post10795816 "View Quoted Post")
> 
> Disliked
> 
> {quote} Ah OK you are russian. Greetings from France.
> 
> Ignored

I'm from Russia. Greetings from Siberia. This is lake Baikal. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Ð‘ÐÐ™ÐšÐÐ›.jpg
Size: 53 KB](/attachment/image/2683974/thumbnail?d=1519120297)](/attachment/image/2683974?d=1519120297)   

"Money makes Money"

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#54](/thread/post/10795997#post10795997 "Post Permalink")

  * Feb 20, 2018 7:23pm  Feb 20, 2018 7:23pm 

  * [ Namor](namor)

  * | Joined Sep 2012  | Status: Trader | [106 Posts](/search?do=process&provider=Member&searchuser=293510)

> [Quoting Ezios](/thread/post/10794576#post10794576 "View Quoted Post")
> 
> Disliked
> 
> Good night buys, the first version is ready. Keep in mind that it works only on demo account and it will open baskets following the rule of madscalp. when it reaches first loss or first gain it will not open more baskets. if you want to trade more you have to remove and restart. ok? enjoy it and let me know about the results. as it is a automatic trading no time filter only takes signal. no more than 1 basket for every signal detected. bye. {file}
> 
> Ignored

Hi Ezios,  
I tried your EA today. It went very well. You write that when it reaches first loss or first gain it will not open more baskets. It will. It reaches gain  
and EA opened another basket without restarting EA. Let's see how it will go!  
Here are the results. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: abc.jpeg
Size: 181 KB](/attachment/image/2684027/thumbnail?d=1519122174)](/attachment/image/2684027?d=1519122174)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#55](/thread/post/10796067#post10796067 "Post Permalink")

  * Feb 20, 2018 7:56pm  Feb 20, 2018 7:56pm 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

in theory it may not occur but perhaps if our platform  
disconnected after the make profit the ea restarts and make the task.  
but if the Platform dont disconnect the ea stops.  
so i am glad that is going well.  

> [Quoting Namor](/thread/post/10795997#post10795997 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi Ezios, I tried your EA today. It went very well. You write that when it reaches first loss or first gain it will not open more baskets. It will. It reaches gain and EA opened another basket without restarting EA. Let's see how it will go! Here are the results. {image}
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#56](/thread/post/10796125#post10796125 "Post Permalink")

  * Feb 20, 2018 8:06pm  Feb 20, 2018 8:06pm 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

i repeat. i dont want to make dashboard.  
the thing i can do to trade basket for basket is to insert in the next version  
an input string TradebBasket="aud,usd,jpg,...." where you can select wih basket to trade  
but keep in mind that you have to attach the same ea to each graph if you want to trade a basket at a time  
and in each chart you have to use different magic number.  
this is the more easy way for me to do it. i have no more free time.  

> [Quoting syndicat](/thread/post/10795259#post10795259 "View Quoted Post")
> 
> Disliked
> 
> {quote} Don't need buttons. You need to install one copy of the EA for example for the AUD basket, another copy for the NZD basket, and then The EA closes a basket of different currencies all together. you need to close the basket for each currency separately. error: 2018.02.20 15:36:30.847 '29660177': order sell 0.01 EURGBP opening at market sl: 0.00000 tp: 0.00000 failed [Off quotes] [me_TradingDashboard v3.mq4](https://www.forexfactory.com/attachment.php/2676832?attachmentid=2676832&d=1518609399) \- Ezios this panel is not working correctly....
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#57](/thread/post/10796126#post10796126 "Post Permalink")

  * Feb 20, 2018 8:06pm  Feb 20, 2018 8:06pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar556193_1.gif) Fatso](fatso)

  * | Joined Feb 2017  | Status: Trader | [111 Posts](/search?do=process&provider=Member&searchuser=556193)

> [Quoting Namor](/thread/post/10795997#post10795997 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi Ezios, I tried your EA today. It went very well. You write that when it reaches first loss or first gain it will not open more baskets. It will. It reaches gain and EA opened another basket without restarting EA. Let's see how it will go! Here are the results. {image}
> 
> Ignored

Thank you so much for posting your results; it confirmed that I was going the wrong direction with my trades which I was trading manually.![](https://resources.faireconomy.media/images/emojis/64/1f644.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f605.png?v=15.1). So my results should improve from now onwards 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#58](/thread/post/10796195#post10796195 "Post Permalink")

  * Feb 20, 2018 8:30pm  Feb 20, 2018 8:30pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar620434_4.gif) syndicat](syndicat)

  * | Additional Username  | Joined Oct 2017 | [432 Posts](/search?do=process&provider=Member&searchuser=620434)

> [Quoting Ezios](/thread/post/10796125#post10796125 "View Quoted Post")
> 
> Disliked
> 
> i repeat. i dont want to make dashboard. the thing i can do to trade basket for basket is to insert in the next version an input string TradebBasket="aud,usd,jpg,...." where you can select wih basket to trade but keep in mind that you have to attach the same ea to each graph if you want to trade a basket at a time and in each chart you have to use different magic number. this is the more easy way for me to do it. i have no more free time. {quote}
> 
> Ignored

the next version  
an input string Tradebasket= " aud,usd, jpg,...."- This is what I and asked!!!  
  
I see you took the code from this: me_Trading Dashboard v3.mq4 I already many times spoke that in this panel works with mistakes mistakes!!! Did you take lines of code from him???  
  
This error was in the pwtcea Advisor today  
error:2018.02.20 15:36:30.847 '29660177': order sell 0.01 EURGBP opening at market sl: 0.00000 tp: 0.00000 failed [Off quotes]  
  
Similar error I had with me_Trading Dashboard v3.mq4 here is an example of early:  
  
2018.02.13 18:36:30.718 '60051764': order sell 0.10 EURCAD opening at market sl: 0.00000 tp: 0.00000 failed [Off quotes]  
2018.02.13 18:25:51.752 '60051764': order buy 0.10 EURGBP opening at market sl: 0.00000 tp: 0.00000 failed [Off quotes]  
2018.02.13 16:32:48.243 '60051764': order sell 0.10 EURUSD opening at market sl: 0.00000 tp: 0.00000 failed [Off quotes] 

"Money makes Money"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#59](/thread/post/10796225#post10796225 "Post Permalink")

  * Feb 20, 2018 8:37pm  Feb 20, 2018 8:37pm 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

this error i think depends from the broker.  
in my broker there is no so error because the broker dont accept the sl and tp = 0.  
anyway i will look to my log if there is the error. i ask to you all if you find this error...  
surely is from your broker.  

> [Quoting syndicat](/thread/post/10796195#post10796195 "View Quoted Post")
> 
> Disliked
> 
> {quote} the next version an input string Tradebasket= " aud,usd, jpg,...."- This is what I and asked!!! I see you took the code from this: me_Trading Dashboard v3.mq4 I already many times spoke that in this panel works with mistakes mistakes!!! Did you take lines of code from him??? This error was in the pwtcea Advisor today error:2018.02.20 15:36:30.847 '29660177': order sell 0.01 EURGBP opening at market sl: 0.00000 tp: 0.00000 failed [Off quotes]
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#60](/thread/post/10796239#post10796239 "Post Permalink")

  * Feb 20, 2018 8:41pm  Feb 20, 2018 8:41pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar620434_4.gif) syndicat](syndicat)

  * | Additional Username  | Joined Oct 2017 | [432 Posts](/search?do=process&provider=Member&searchuser=620434)

> [Quoting Ezios](/thread/post/10796225#post10796225 "View Quoted Post")
> 
> Disliked
> 
> this error i think depends from the broker. in my broker there is no so error because the broker dont accept the sl and tp = 0. anyway i will look to my log if there is the error. i ask to you all if you find this error... surely is from your broker. {quote}
> 
> Ignored

  
Experts tab:  
  
2018.02.20 19:40:23.374 pwtcea AUDUSD,H1: ButtonCreate: failed to create the button! Error code = 4200 

"Money makes Money"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Playing with the currencies: Gabin System
  *   * [ **Reply to Thread** ](/thread/739272-playing-with-the-currencies-gabin-system/reply#reply)

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

[Doubling up method or playing casino](/thread/4169-doubling-up-method-or-playing-casino "Hi everyone, 
  
I was thinking about one strategy which I called doubling up method but I want to share it and you to review and make...") 24 replies

[Playing the Double-Up Game?](/thread/42119-playing-the-double-up-game "It's sure a crazy full of risk system. I was just wondering if anyone ever heard of someone doing this and winning? 
  
With this system...") 40 replies

[Playing with datetime...](/thread/36065-playing-with-datetime "Hi, 
  
Setting the date, manually, in Alert 2 to todays date, why does Alert 1 return a different value than Alert 2? Even using...") 2 replies

[Playing the Breakout Trade](/thread/6189-playing-the-breakout-trade "by Abe Cofnas 
 
When markets move, particularly in Forex, they move fast. We all have witnessed breakouts and have had the occasion to...") 4 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/739272-playing-with-the-currencies-gabin-system/reply#reply)
  * Subscribe
  * [161](javascript:void\(0\);)

Attachments: Playing with the currencies: Gabin System

Tags: Playing with the currencies: Gabin System

#  [](/thread/739272-playing-with-the-currencies-gabin-system)Playing with the currencies: Gabin System 

  * 

  * [#61](/thread/post/10796293#post10796293 "Post Permalink")

  * Feb 20, 2018 8:56pm  Feb 20, 2018 8:56pm 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

no, try it on a fresh chart, as the error code 4200 means "Object already exists", the buttons were created  
but this error has not hing to do whith the stop loss error is an error on che chart.  

> [Quoting syndicat](/thread/post/10796239#post10796239 "View Quoted Post")
> 
> Disliked
> 
> {quote} Experts tab: 2018.02.20 19:40:23.374 pwtcea AUDUSD,H1: ButtonCreate: failed to create the button! Error code = 4200
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#62](/thread/post/10796437#post10796437 "Post Permalink")

  * Feb 20, 2018 9:47pm  Feb 20, 2018 9:47pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar620434_4.gif) syndicat](syndicat)

  * | Additional Username  | Joined Oct 2017 | [432 Posts](/search?do=process&provider=Member&searchuser=620434)

> [Quoting Ezios](/thread/post/10796293#post10796293 "View Quoted Post")
> 
> Disliked
> 
> no, try it on a fresh chart, as the error code 4200 means "Object already exists", the buttons were created but this error has not hing to do whith the stop loss error is an error on che chart. {quote}
> 
> Ignored

  
2018.02.20 20:46:36.553 pwtcea EURJPY,H1: ButtonCreate: failed to create the button! Error code = 4200 

"Money makes Money"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#63](/thread/post/10796472#post10796472 "Post Permalink")

  * Feb 20, 2018 9:54pm  Feb 20, 2018 9:54pm 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

dont know... perhaps your setting of chart... in my Platform no this error and no ettor noting  
so i cannot help... sorry. 

> [Quoting syndicat](/thread/post/10796437#post10796437 "View Quoted Post")
> 
> Disliked
> 
> {quote} 2018.02.20 20:46:36.553 pwtcea EURJPY,H1: ButtonCreate: failed to create the button! Error code = 4200
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#64](/thread/post/10796515#post10796515 "Post Permalink")

  * Feb 20, 2018 10:13pm  Feb 20, 2018 10:13pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar620434_4.gif) syndicat](syndicat)

  * | Additional Username  | Joined Oct 2017 | [432 Posts](/search?do=process&provider=Member&searchuser=620434)

> [Quoting Ezios](/thread/post/10796472#post10796472 "View Quoted Post")
> 
> Disliked
> 
> dont know... perhaps your setting of chart... in my Platform no this error and no ettor noting so i cannot help... sorry. {quote}
> 
> Ignored

Here's a clean platform  
  
  
2018.02.20 21:11:01.530 pwtcea AUDNZD,H1: ButtonCreate: failed to create the button! Error code = 4200 

"Money makes Money"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#65](/thread/post/10796594#post10796594 "Post Permalink")

  * Feb 20, 2018 10:39pm  Feb 20, 2018 10:39pm 

  * [ humblewise](humblewise)

  * | Joined Feb 2018  | Status: Trader | [21 Posts](/search?do=process&provider=Member&searchuser=650639)

@Ezios: button create problem can be easily resolved, just make an object delete before create the button 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#66](/thread/post/10796609#post10796609 "Post Permalink")

  * Feb 20, 2018 10:42pm  Feb 20, 2018 10:42pm 

  * [ humblewise](humblewise)

  * | Joined Feb 2018  | Status: Trader | [21 Posts](/search?do=process&provider=Member&searchuser=650639)

this system has no real edge. it works well when market is weak, but will kill the account when strong trend takes place  
it is purely luck-based system in this form 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#67](/thread/post/10796649#post10796649 "Post Permalink")

  * Feb 20, 2018 10:56pm  Feb 20, 2018 10:56pm 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

this evening when i come bacik from office i will see my Platform if the log gives  
some errors but , as no one in this tread reported this , i suppose its only yours problem.  
if i report the error from me i will try to help but , i repeat , if i have not the error i can not help.  

> [Quoting syndicat](/thread/post/10796515#post10796515 "View Quoted Post")
> 
> Disliked
> 
> {quote} Here's a clean platform 2018.02.20 21:11:01.530 pwtcea AUDNZD,H1: ButtonCreate: failed to create the button! Error code = 4200
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#68](/thread/post/10796784#post10796784 "Post Permalink")

  * Edited 11:44pm  Feb 20, 2018 11:30pm | Edited 11:44pm 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

> [Quoting humblewise](/thread/post/10796609#post10796609 "View Quoted Post")
> 
> Disliked
> 
> this system has no real edge. it works well when market is weak, but will kill the account when strong trend takes place it is purely luck-based system in this form
> 
> Ignored

Yes we know it. We are waiting for the death... ![](https://resources.faireconomy.media/images/emojis/64/1f600.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f600.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f600.png?v=15.1)  
Seriously there is a SL in the system like in all system.  
Currently we are testing to avoid a death trade or to minimize the loss.  
Without news, the system is working nicely but on 9 Feb, GBP has dropped hardly during 4 hours.  
To be honest, I'm waiting again for a same event to judge the method. Maybe a Without News System ? 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#69](/thread/post/10796828#post10796828 "Post Permalink")

  * Feb 20, 2018 11:41pm  Feb 20, 2018 11:41pm 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

> [Quoting Ezios](/thread/post/10796649#post10796649 "View Quoted Post")
> 
> Disliked
> 
> this evening when i come bacik from office i will see my Platform if the log gives some errors but , as no one in this tread reported this , i suppose its only yours problem. if i report the error from me i will try to help but , i repeat , if i have not the error i can not help. {quote}
> 
> Ignored

Ezios...just a request for the next version : the EA have _to stop itself after a SL_  
maybe can you introduce a reset fonction if the user wants to trade again ?  
@ syndicat I see on your fxbook on 7 trading days : balance 62 % and equity only 42 % ...is it correct ? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#70](/thread/post/10796894#post10796894 "Post Permalink")

  * Feb 20, 2018 11:56pm  Feb 20, 2018 11:56pm 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

i'm not sure if i can do this. surely when stop loss occurs i will remove the ea from  
the chart and is the responsabilty of trader to restart the ea.  
i can continue to trade if the gain is hit until stop if it is this the sense.  

> [Quoting madscalp](/thread/post/10796828#post10796828 "View Quoted Post")
> 
> Disliked
> 
> {quote} Ezios...just a request for the next version : the EA have to stop itself after a SL maybe can you introduce a reset fonction if the user wants to trade again ? @ syndicat I see on your fxbook on 7 trading days : balance 62 % and equity only 42 % ...is it correct ?
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#71](/thread/post/10796915#post10796915 "Post Permalink")

  * Feb 20, 2018 11:59pm  Feb 20, 2018 11:59pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar620434_4.gif) syndicat](syndicat)

  * | Additional Username  | Joined Oct 2017 | [432 Posts](/search?do=process&provider=Member&searchuser=620434)

> [Quoting madscalp](/thread/post/10796828#post10796828 "View Quoted Post")
> 
> Disliked
> 
> {quote} Ezios...just a request for the next version : the EA have to stop itself after a SL maybe can you introduce a reset fonction if the user wants to trade again ? @ syndicat I see on your fxbook on 7 trading days : balance 62 % and equity only 42 % ...is it correct ?
> 
> Ignored

  
  
  
updated monitoring 

"Money makes Money"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#72](/thread/post/10796985#post10796985 "Post Permalink")

  * Feb 21, 2018 12:15am  Feb 21, 2018 12:15am 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

> [Quoting Ezios](/thread/post/10796894#post10796894 "View Quoted Post")
> 
> Disliked
> 
> i'm not sure if i can do this. surely when stop loss occurs i will remove the ea from the chart and is the responsabilty of trader to restart the ea. i can continue to trade if the gain is hit until stop if it is this the sense. {quote}
> 
> Ignored

I didn't need SL as far as now...so the EA can start again after a SL ? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#73](/thread/post/10797005#post10797005 "Post Permalink")

  * Feb 21, 2018 12:19am  Feb 21, 2018 12:19am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar395711_10.gif) LuXing](luxing)

  * Joined Jan 2015 | Status: Error 404: LuXing not found | [1,586 Posts](/search?do=process&provider=Member&searchuser=395711)

> [Quoting syndicat](/thread/post/10791147#post10791147 "View Quoted Post")
> 
> Disliked
> 
> {quote} the practical advice is not given.
> 
> Ignored

> [Quoting syndicat](/thread/post/10791147#post10791147 "View Quoted Post")
> 
> Disliked
> 
> {quote} To listen to your advice,
> 
> Ignored

> [Quoting syndicat](/thread/post/10791147#post10791147 "View Quoted Post")
> 
> Disliked
> 
> {quote} In this topic no one nothing not sells.
> 
> Ignored

Triple negation is the first that comes to my mind.  
A bit confusing, but duly noted: I shall give no more constructive criticism.  
  

> [Quoting syndicat](/thread/post/10791147#post10791147 "View Quoted Post")
> 
> Disliked
> 
> {quote} I would like to make sure that your strategy is profitable.
> 
> Ignored

Mmm, I hate to break the bad news, but statistically in the long run _no strategy is profitable_. If any, it’s the trader who is profitable (or lucky).  
Statistical proof in [this excellent post](https://www.forexfactory.com/showthread.php?p=9385836#post9385836).  
  

> [Quoting syndicat](/thread/post/10791147#post10791147 "View Quoted Post")
> 
> Disliked
> 
> {quote} Show me monitoring? We are trying to improve this strategy.
> 
> Ignored

Monitoring of what ? Of my trading account(s) ?  
That will not make you better traders, nor will it improve this strategy.  
You are absolutely right to ask somebody for “transparency and proof” if a Fool’s Factory member is selling some junk robot, a service or trading other people’s money. That’s not my case though.  
  
Back to the “trying to improve this strategy”.  
My robot does the exact opposite of this strategy. Hopefully the entries it took in full auto mode can somehow help you guys in finding a sweetspot for entries.   
I have blacked out some irrelevant information, but the most important (Currency Strength) is printed in the comments column.  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot1.png
Size: 489 KB](/attachment/image/2684509/thumbnail?d=1519139841)](/attachment/image/2684509?d=1519139841)   

  
  
Happy basketing.  
LuXing

Wisdom begins in wonder

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#74](/thread/post/10797011#post10797011 "Post Permalink")

  * Feb 21, 2018 12:22am  Feb 21, 2018 12:22am 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

if i program the nest version to remove itself after a sl obviusly cannot restart by itse.f  
as it is now if the sl occurs no trades. the only thing is... if the Platform disconnect after sl it will be the ea  
to continue trading. so it is necessary after sl that ea remove itself if we want to be sure not disaster.  

> [Quoting madscalp](/thread/post/10796985#post10796985 "View Quoted Post")
> 
> Disliked
> 
> {quote} I didn't need SL as far as now...so the EA can start again after a SL ?
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#75](/thread/post/10797040#post10797040 "Post Permalink")

  * Feb 21, 2018 12:30am  Feb 21, 2018 12:30am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar523703_1.gif) faryne](faryne)

  * | Joined Oct 2016  | Status: Trader | [93 Posts](/search?do=process&provider=Member&searchuser=523703)

I made my own version with some "modifications":  
-button for close all orders,  
-button for close each basket,  
-tp/sl set for each basket (not all open orders)  
-parameter to "reset" each pair from last open basket (in hours).  
  
Let me know if you're insterested.  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: medusa.png
Size: 49 KB](/attachment/image/2684530/thumbnail?d=1519140518)](/attachment/image/2684530?d=1519140518)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#76](/thread/post/10797087#post10797087 "Post Permalink")

  * Feb 21, 2018 12:38am  Feb 21, 2018 12:38am 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

> [Quoting LuXing](/thread/post/10797005#post10797005 "View Quoted Post")
> 
> Disliked
> 
> {quote} {quote} {quote} Triple negation is the first that comes to my mind. A bit confusing, but duly noted: I shall give no more constructive criticism. {quote} Mmm, I hate to break the bad news, but statistically in the long run no strategy is profitable. If any, it’s the trader who is profitable (or lucky). Statistical proof in [this excellent post](https://www.forexfactory.com/showthread.php?p=9385836#post9385836). {quote} Monitoring of what ? Of my trading account(s) ? That will not make you better traders, nor will it improve this...
> 
> Ignored

Many thanks for your post.  
I see really many good trades with small TP...however it seems not exactly a basket trading  
It's funny because our both opposite systems are winning today.  
Maybe a mix of the both ? 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: 2.jpg
Size: 138 KB](/attachment/image/2684555/thumbnail?d=1519141113)](/attachment/image/2684555?d=1519141113)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#77](/thread/post/10797104#post10797104 "Post Permalink")

  * Feb 21, 2018 12:40am  Feb 21, 2018 12:40am 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

you very fast coder. and the trigger signal? as mine or manual?  

> [Quoting faryne](/thread/post/10797040#post10797040 "View Quoted Post")
> 
> Disliked
> 
> I made my own version with some "modifications": -button for close all orders, -button for close each basket, -tp/sl set for each basket (not all open orders) -parameter to "reset" each pair from last open basket (in hours). Let me know if you're insterested. {image}
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#78](/thread/post/10797115#post10797115 "Post Permalink")

  * Feb 21, 2018 12:44am  Feb 21, 2018 12:44am 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

> [Quoting Ezios](/thread/post/10797104#post10797104 "View Quoted Post")
> 
> Disliked
> 
> you very fast coder. and the trigger signal? as mine or manual? {quote}
> 
> Ignored

I'm thinking it's a adding tool.  
Welcome faryne. Of course, it's surely useful. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#79](/thread/post/10797125#post10797125 "Post Permalink")

  * Edited 3:39am  Feb 21, 2018 12:49am | Edited 3:39am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar523703_1.gif) faryne](faryne)

  * | Joined Oct 2016  | Status: Trader | [93 Posts](/search?do=process&provider=Member&searchuser=523703)

For now same logic with 3 steps.  
I also added a reverse button for news trading for example (hard strong trend), and maybe a parameter to trade trend and mean-reverting same time on different step.  
Here is the ea.  
  
(Some details: I removed the "delta_18", and magic numbers are calculated in the code (for basket management)). 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#80](/thread/post/10797137#post10797137 "Post Permalink")

  * Feb 21, 2018 12:54am  Feb 21, 2018 12:54am 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

wow.... very promising tool... i would not be able to realize this... ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) you very clever coder.  

> [Quoting faryne](/thread/post/10797125#post10797125 "View Quoted Post")
> 
> Disliked
> 
> For now same logic with 3 steps. I also added a reverse button for news trading for example (hard strong trend), and maybe a parameter to trade trend and mean-reverting same time on different step. Here is the ea. {file}
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Playing with the currencies: Gabin System
  *   * [ **Reply to Thread** ](/thread/739272-playing-with-the-currencies-gabin-system/reply#reply)

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

[Doubling up method or playing casino](/thread/4169-doubling-up-method-or-playing-casino "Hi everyone, 
  
I was thinking about one strategy which I called doubling up method but I want to share it and you to review and make...") 24 replies

[Playing the Double-Up Game?](/thread/42119-playing-the-double-up-game "It's sure a crazy full of risk system. I was just wondering if anyone ever heard of someone doing this and winning? 
  
With this system...") 40 replies

[Playing with datetime...](/thread/36065-playing-with-datetime "Hi, 
  
Setting the date, manually, in Alert 2 to todays date, why does Alert 1 return a different value than Alert 2? Even using...") 2 replies

[Playing the Breakout Trade](/thread/6189-playing-the-breakout-trade "by Abe Cofnas 
 
When markets move, particularly in Forex, they move fast. We all have witnessed breakouts and have had the occasion to...") 4 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/739272-playing-with-the-currencies-gabin-system/reply#reply)
  * Subscribe
  * [161](javascript:void\(0\);)

Attachments: Playing with the currencies: Gabin System

Tags: Playing with the currencies: Gabin System

#  [](/thread/739272-playing-with-the-currencies-gabin-system)Playing with the currencies: Gabin System 

  * 

  * [#81](/thread/post/10797264#post10797264 "Post Permalink")

  * Edited 2:18am  Feb 21, 2018 1:28am | Edited 2:18am 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

> [Quoting faryne](/thread/post/10797125#post10797125 "View Quoted Post")
> 
> Disliked
> 
> For now same logic with 3 steps. I also added a reverse button for news trading for example (hard strong trend), and maybe a parameter to trade trend and mean-reverting same time on different step. Here is the ea. (Some details: I removed the "delta_18", and magic numbers are calculated in the code (for basket management)). {file}
> 
> Ignored

Woooh it's a complete EA. Congratulations.  
What's about reverse button ?  
I was not in front of my computer and the EA has opened these 14 orders ? it seems according with CHF ????? 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: 3.jpg
Size: 143 KB](/attachment/image/2684725/thumbnail?d=1519147096)](/attachment/image/2684725?d=1519147096)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#82](/thread/post/10797615#post10797615 "Post Permalink")

  * Edited 4:57pm  Feb 21, 2018 3:38am | Edited 4:57pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar523703_1.gif) faryne](faryne)

  * | Joined Oct 2016  | Status: Trader | [93 Posts](/search?do=process&provider=Member&searchuser=523703)

> [Quoting madscalp](/thread/post/10797264#post10797264 "View Quoted Post")
> 
> Disliked
> 
> {quote} Woooh it's a complete EA. Congratulations. What's about reverse button ? I was not in front of my computer and the EA has opened these 14 orders ? it seems according with CHF ????? {image}
> 
> Ignored

Thanks, that was a problem.  
Fixed.  
  
Reverse is in parameter. Also added magic number to use EA with the two modes (on 2 different charts) in same time. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#83](/thread/post/10797770#post10797770 "Post Permalink")

  * Feb 21, 2018 4:34am  Feb 21, 2018 4:34am 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

> [Quoting LuXing](/thread/post/10797668#post10797668 "View Quoted Post")
> 
> Disliked
> 
> {quote} {image}
> 
> Ignored

the issue was that it was not CHF baskets  
you seem to show some interest for this tool ...for reverting_all option ? ![](https://resources.faireconomy.media/images/emojis/64/1f600.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f600.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#84](/thread/post/10797843#post10797843 "Post Permalink")

  * Feb 21, 2018 5:03am  Feb 21, 2018 5:03am 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

ok guys i post version 2.  
\- eliminated the issue of the buttons  
\- create string input for selecting the basket to trade or not  
\- when tp is hit ea continue to trade  
\- when sl is hit ea remove itself from chart.  
could be easy to do version 2r with the signal reversed so.... only to test the results.  
I continue to believe in madscalp approach until my demo account will be blown ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [pwtcea_v2.ex4](/attachment/file/2684856?d=1519156970) 99 KB | 279 downloads 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#85](/thread/post/10797913#post10797913 "Post Permalink")

  * Feb 21, 2018 5:42am  Feb 21, 2018 5:42am 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

> [Quoting Ezios](/thread/post/10797843#post10797843 "View Quoted Post")
> 
> Disliked
> 
> when sl is hit ea remove itself from chart.
> 
> Ignored

good...it's to avoid to come back in the market if there is a very big move  
  

> [Quoting Ezios](/thread/post/10797843#post10797843 "View Quoted Post")
> 
> Disliked
> 
> I continue to believe in madscalp approach until my demo account will be blown ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) {file}
> 
> Ignored

if you trade cautionly avoiding the news...why not ! there will be sometimes the use of the SL like in all system.  
What are your results in demo ? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#86](/thread/post/10797965#post10797965 "Post Permalink")

  * Feb 21, 2018 6:13am  Feb 21, 2018 6:13am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar556193_1.gif) Fatso](fatso)

  * | Joined Feb 2017  | Status: Trader | [111 Posts](/search?do=process&provider=Member&searchuser=556193)

> [Quoting syndicat](/thread/post/10796437#post10796437 "View Quoted Post")
> 
> Disliked
> 
> {quote} 2018.02.20 20:46:36.553 pwtcea EURJPY,H1: ButtonCreate: failed to create the button! Error code = 4200
> 
> Ignored

Hi Syndicat. Did you manage to resolve this error. I am getting the same error:  
_**"2018.02.20 23:06:49.023 pwtcea_v2 USDJPY-,H1: ButtonDelete: Failed to delete the button! Error code = 4202"**_  
Please let me know if you managed to resolve the error 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#87](/thread/post/10798103#post10798103 "Post Permalink")

  * Feb 21, 2018 7:24am  Feb 21, 2018 7:24am 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

> [Quoting Fatso](/thread/post/10797965#post10797965 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi Syndicat. Did you manage to resolve this error. I am getting the same error: "2018.02.20 23:06:49.023 pwtcea_v2 USDJPY-,H1: ButtonDelete: Failed to delete the button! Error code = 4202" Please let me know if you managed to resolve the error
> 
> Ignored

i will going to fix also this... ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) it's error in the functions. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#88](/thread/post/10798178#post10798178 "Post Permalink")

  * Feb 21, 2018 7:48am  Feb 21, 2018 7:48am 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

> [Quoting Ezios](/thread/post/10798103#post10798103 "View Quoted Post")
> 
> Disliked
> 
> {quote} i will going to fix also this... ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) it's error in the functions.
> 
> Ignored

these are annoying but unconsistent errors ... now it should be fixed.. 

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [pwtcea_v2.ex4](/attachment/file/2684979?d=1519166902) 99 KB | 269 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#89](/thread/post/10798651#post10798651 "Post Permalink")

  * Feb 21, 2018 12:19pm  Feb 21, 2018 12:19pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar620434_4.gif) syndicat](syndicat)

  * | Additional Username  | Joined Oct 2017 | [432 Posts](/search?do=process&provider=Member&searchuser=620434)

> [Quoting faryne](/thread/post/10797040#post10797040 "View Quoted Post")
> 
> Disliked
> 
> I made my own version with some "modifications": -button for close all orders, -button for close each basket, -tp/sl set for each basket (not all open orders) -parameter to "reset" each pair from last open basket (in hours). Let me know if you're insterested. {image}
> 
> Ignored

  
Excellent work!!! Can add a function to lock profits? 

"Money makes Money"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#90](/thread/post/10799098#post10799098 "Post Permalink")

  * Feb 21, 2018 3:09pm  Feb 21, 2018 3:09pm 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

Hi traders  
Beware of GBP news today at 9:30 GMT.  
I'd like too to thank Ezios and faryne for their work. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#91](/thread/post/10799101#post10799101 "Post Permalink")

  * Feb 21, 2018 3:09pm  Feb 21, 2018 3:09pm 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

Good morning, how is it going? from my sie all right. i am running version 2 on my demo account  
and actually 5 basket open. This night 2 profits. I wait for the first stop loss....  
Madscalp you think the friday we have to close the ea or to leave running? 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: demo_account.png
Size: 26 KB](/attachment/image/2685365/thumbnail?d=1519193336)](/attachment/image/2685365?d=1519193336)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#92](/thread/post/10799210#post10799210 "Post Permalink")

  * Feb 21, 2018 3:58pm  Feb 21, 2018 3:58pm 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

> [Quoting Ezios](/thread/post/10799101#post10799101 "View Quoted Post")
> 
> Disliked
> 
> Good morning, how is it going? from my sie all right. i am running version 2 on my demo account and actually 5 basket open. This night 2 profits. I wait for the first stop loss.... Madscalp you think the friday we have to close the ea or to leave running? {image}
> 
> Ignored

Hi Ezios  
I suggest for settings 4.4 ...4.8...5.2.  
About friday, my answer is no, don't forget we are in demo...so for testing.  
We need to test news.  
I'm thinking about a new option: it's a bool "basket limit option":  
for instance, after 3 or 4 or 5 basket open, the EA doesn't open new baskets (IMO easy to code) 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#93](/thread/post/10799235#post10799235 "Post Permalink")

  * Feb 21, 2018 4:13pm  Feb 21, 2018 4:13pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar620434_4.gif) syndicat](syndicat)

  * | Additional Username  | Joined Oct 2017 | [432 Posts](/search?do=process&provider=Member&searchuser=620434)

> [Quoting Ezios](/thread/post/10798178#post10798178 "View Quoted Post")
> 
> Disliked
> 
> {quote} these are annoying but unconsistent errors ... now it should be fixed.. {file}
> 
> Ignored

Ezios thank you now there is no mistakes. Put to the test 

"Money makes Money"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#94](/thread/post/10799277#post10799277 "Post Permalink")

  * Feb 21, 2018 4:29pm  Feb 21, 2018 4:29pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar620434_4.gif) syndicat](syndicat)

  * | Additional Username  | Joined Oct 2017 | [432 Posts](/search?do=process&provider=Member&searchuser=620434)

> [Quoting Fatso](/thread/post/10797965#post10797965 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi Syndicat. Did you manage to resolve this error. I am getting the same error: "2018.02.20 23:06:49.023 pwtcea_v2 USDJPY-,H1: ButtonDelete: Failed to delete the button! Error code = 4202" Please let me know if you managed to resolve the error
> 
> Ignored

Hey Fatso! Ezios has fixed, now there is no this error. Post 88 

"Money makes Money"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#95](/thread/post/10799293#post10799293 "Post Permalink")

  * Feb 21, 2018 4:38pm  Feb 21, 2018 4:38pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar556193_1.gif) Fatso](fatso)

  * | Joined Feb 2017  | Status: Trader | [111 Posts](/search?do=process&provider=Member&searchuser=556193)

> [Quoting syndicat](/thread/post/10799277#post10799277 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hey Fatso! Ezios has fixed, now there is no this error. Post 88
> 
> Ignored

Thanks; I will test it later after work. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#96](/thread/post/10799338#post10799338 "Post Permalink")

  * Feb 21, 2018 4:54pm  Feb 21, 2018 4:54pm 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

> [Quoting faryne](/thread/post/10797615#post10797615 "View Quoted Post")
> 
> Disliked
> 
> {quote} Thanks, that was a problem. Fixed. Reverse is in parameter. Also added magic number to use EA with the two modes (on 2 different charts) in same time. {file}
> 
> Ignored

Hi faryne  
Your EA doesn't work properly.  
The rules are 1st level open 1st basket ...2nd level open 2nd basket....3rd level 3rd basket  
So in all no more 3 baskets.  
10 mn ago, your EA has opened more 7 baskets AUD....happily in profit 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#97](/thread/post/10799339#post10799339 "Post Permalink")

  * Feb 21, 2018 4:57pm  Feb 21, 2018 4:57pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar523703_1.gif) faryne](faryne)

  * | Joined Oct 2016  | Status: Trader | [93 Posts](/search?do=process&provider=Member&searchuser=523703)

> [Quoting madscalp](/thread/post/10799338#post10799338 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi faryne Your EA doesn't work properly. The rules are 1st level open 1st basket ...2nd level open 2nd basket....3rd level 3rd basket So in all no more 3 baskets. 10 mn ago, your EA has opened more 7 baskets AUD....happily in profit
> 
> Ignored

Yep, just see that. That was a big position. Currently working on it. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#98](/thread/post/10799390#post10799390 "Post Permalink")

  * Feb 21, 2018 5:07pm  Feb 21, 2018 5:07pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar620434_4.gif) syndicat](syndicat)

  * | Additional Username  | Joined Oct 2017 | [432 Posts](/search?do=process&provider=Member&searchuser=620434)

> [Quoting faryne](/thread/post/10799339#post10799339 "View Quoted Post")
> 
> Disliked
> 
> {quote} Yep, just see that. That was a big position. Currently working on it.
> 
> Ignored

take profit doesn't work either... 

"Money makes Money"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#99](/thread/post/10799397#post10799397 "Post Permalink")

  * Feb 21, 2018 5:08pm  Feb 21, 2018 5:08pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar620434_4.gif) syndicat](syndicat)

  * | Additional Username  | Joined Oct 2017 | [432 Posts](/search?do=process&provider=Member&searchuser=620434)

> [Quoting Ezios](/thread/post/10799101#post10799101 "View Quoted Post")
> 
> Disliked
> 
> Good morning, how is it going? from my sie all right. i am running version 2 on my demo account and actually 5 basket open. This night 2 profits. I wait for the first stop loss.... Madscalp you think the friday we have to close the ea or to leave running? {image}
> 
> Ignored

  
Ezios if I select one basket to trade the EA does not open trades... 

"Money makes Money"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#100](/thread/post/10799692#post10799692 "Post Permalink")

  * Feb 21, 2018 7:01pm  Feb 21, 2018 7:01pm 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

Hi syndicat  
I didn't trade at 7:30 GMT during asian session.  
There was probably a sell USD at this time.  
Have you taken it ? because it has dropped nicely 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Playing with the currencies: Gabin System
  *   * [ **Reply to Thread** ](/thread/739272-playing-with-the-currencies-gabin-system/reply#reply)

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

[Doubling up method or playing casino](/thread/4169-doubling-up-method-or-playing-casino "Hi everyone, 
  
I was thinking about one strategy which I called doubling up method but I want to share it and you to review and make...") 24 replies

[Playing the Double-Up Game?](/thread/42119-playing-the-double-up-game "It's sure a crazy full of risk system. I was just wondering if anyone ever heard of someone doing this and winning? 
  
With this system...") 40 replies

[Playing with datetime...](/thread/36065-playing-with-datetime "Hi, 
  
Setting the date, manually, in Alert 2 to todays date, why does Alert 1 return a different value than Alert 2? Even using...") 2 replies

[Playing the Breakout Trade](/thread/6189-playing-the-breakout-trade "by Abe Cofnas 
 
When markets move, particularly in Forex, they move fast. We all have witnessed breakouts and have had the occasion to...") 4 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/739272-playing-with-the-currencies-gabin-system/reply#reply)
  * Subscribe
  * [161](javascript:void\(0\);)

Attachments: Playing with the currencies: Gabin System

Tags: Playing with the currencies: Gabin System

#  [](/thread/739272-playing-with-the-currencies-gabin-system)Playing with the currencies: Gabin System 

  * 

  * [#101](/thread/post/10799718#post10799718 "Post Permalink")

  * Feb 21, 2018 7:09pm  Feb 21, 2018 7:09pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar620434_4.gif) syndicat](syndicat)

  * | Additional Username  | Joined Oct 2017 | [432 Posts](/search?do=process&provider=Member&searchuser=620434)

> [Quoting madscalp](/thread/post/10799692#post10799692 "View Quoted Post")
> 
> Disliked
> 
> Hi syndicat I didn't trade at 7:30 GMT during asian session. There was probably a sell USD at this time. Have you taken it ? because it has dropped nicely
> 
> Ignored

Yes, I sold the USD and closed with profit. I'm starting an experiment with lock-in profits. 

"Money makes Money"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#102](/thread/post/10799762#post10799762 "Post Permalink")

  * Edited 7:33pm  Feb 21, 2018 7:22pm | Edited 7:33pm 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

> [Quoting syndicat](/thread/post/10799718#post10799718 "View Quoted Post")
> 
> Disliked
> 
> {quote} Yes, I sold the USD and closed with profit. I'm starting an experiment with lock-in profits.
> 
> Ignored

Sure.... it's a good idea. I suggest at least a breakeven option in positive territory to protect the trade.  
A lock tool is sometimes useful ...better a small profit than risk a big reversal....see post 39 # 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#103](/thread/post/10799814#post10799814 "Post Permalink")

  * Feb 21, 2018 7:40pm  Feb 21, 2018 7:40pm 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

i dont fully tested that way but the program will trade the basket only  
if there is the signal for that basket otherwise no trade. if this dont work i will look for.  

> [Quoting syndicat](/thread/post/10799397#post10799397 "View Quoted Post")
> 
> Disliked
> 
> {quote} Ezios if I select one basket to trade the EA does not open trades...
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#104](/thread/post/10799830#post10799830 "Post Permalink")

  * Feb 21, 2018 7:45pm  Feb 21, 2018 7:45pm 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

madscalp as i have programmed the basket open is max 6 because the program opens  
a basket for every possible signal regardless the currency. the possible signals are 6 3 for delta up and 3 for delta down so  
in my intention was so.... but this morning i had a problem at my plaform i saw some floating  
operation that had to be closed... perhaps there is an issue with the stop loss. this evening i will  
look for this. it s very difficult to program an ea and to make it to go in perfect way... but finally we will succeed.  

> [Quoting madscalp](/thread/post/10799210#post10799210 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi Ezios I suggest for settings 4.4 ...4.8...5.2. About friday, my answer is no, don't forget we are in demo...so for testing. We need to test news. I'm thinking about a new option: it's a bool "basket limit option": for instance, after 3 or 4 or 5 basket open, the EA doesn't open new baskets (IMO easy to code)
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#105](/thread/post/10799837#post10799837 "Post Permalink")

  * Edited Feb 22, 2018 2:30am  Feb 21, 2018 7:47pm | Edited Feb 22, 2018 2:30am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar523703_1.gif) faryne](faryne)

  * | Joined Oct 2016  | Status: Trader | [93 Posts](/search?do=process&provider=Member&searchuser=523703)

Here is my latest release. Bugs are fixed.  
I added a breakeven parameter to lock profit @1, and the standard deviation of curencies's strenght to get the "volatility" of forex. It may be a condition to mean reverting.  
Let me know if everything works well. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#106](/thread/post/10799902#post10799902 "Post Permalink")

  * Feb 21, 2018 8:06pm  Feb 21, 2018 8:06pm 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

in teory if we attach in a chart the system counter trend and in another chart  
the system in trend when counter trend goes stop loss the trend goes in profit so...  
but with the fluctuation of market ic can happen both system go in profit in different times...  
i think this is the final solution to have both strategis working together.  
with Medusa it can be done. ...  

> [Quoting faryne](/thread/post/10799837#post10799837 "View Quoted Post")
> 
> Disliked
> 
> Here is my latest release. Bugs are fixed. I added a breakeven parameter to lock profit @1, and the standard deviation of curencies's strenght to get the "volatility" of forex. It may be a condition to mean reverting. Let me know if everything works well. {file}
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#107](/thread/post/10799922#post10799922 "Post Permalink")

  * Feb 21, 2018 8:13pm  Feb 21, 2018 8:13pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar523703_1.gif) faryne](faryne)

  * | Joined Oct 2016  | Status: Trader | [93 Posts](/search?do=process&provider=Member&searchuser=523703)

> [Quoting Ezios](/thread/post/10799902#post10799902 "View Quoted Post")
> 
> Disliked
> 
> in teory if we attach in a chart the system counter trend and in another chart the system in trend when counter trend goes stop loss the trend goes in profit so... but with the fluctuation of market ic can happen both system go in profit in different times... i think this is the final solution to have both strategis working together. with Medusa it can be done. ... {quote}
> 
> Ignored

My idea was to choose the one to trade by the market condition. Working on standard deviation right now. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#108](/thread/post/10800006#post10800006 "Post Permalink")

  * Feb 21, 2018 8:41pm  Feb 21, 2018 8:41pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar395711_10.gif) LuXing](luxing)

  * Joined Jan 2015 | Status: Error 404: LuXing not found | [1,586 Posts](/search?do=process&provider=Member&searchuser=395711)

> [Quoting faryne](/thread/post/10799837#post10799837 "View Quoted Post")
> 
> Disliked
> 
> Here is my latest release. Bugs are fixed. I added a breakeven parameter to lock profit @1, and the standard deviation of curencies's strenght to get the "volatility" of forex. It may be a condition to mean reverting. Let me know if everything works well. {file}
> 
> Ignored

Good thinking !  
Getting in interesting territory.  
Might be a good idea to adjust stdev to cater for volatility decay over time ;-)  
Jonathan Kinlay explains how you could do that in [this article](http://jonathankinlay.com/2014/05/the-mathematics-of-scalping/).  
Of course I am not saying you should, but once adjusted you could maybe think about plenty of neat things such as statistical outliers, ...  
  
LuXing 

Wisdom begins in wonder

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#109](/thread/post/10800040#post10800040 "Post Permalink")

  * Feb 21, 2018 8:52pm  Feb 21, 2018 8:52pm 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

> [Quoting Ezios](/thread/post/10799830#post10799830 "View Quoted Post")
> 
> Disliked
> 
> madscalp as i have programmed the basket open is max 6 because the program opens a basket for every possible signal regardless the currency. the possible signals are 6 3 for delta up and 3 for delta down so in my intention was so.... but this morning i had a problem at my plaform i saw some floating operation that had to be closed... perhaps there is an issue with the stop loss. this evening i will look for this. it s very difficult to program an ea and to make it to go in perfect way... but finally we will succeed. {quote}
> 
> Ignored

Don't worry Ezios you make a wonderful work  
For any reason a buy GBP didn't open with a displayed signal  
Could you check that too ? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#110](/thread/post/10800078#post10800078 "Post Permalink")

  * Feb 21, 2018 9:00pm  Feb 21, 2018 9:00pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar620434_4.gif) syndicat](syndicat)

  * | Additional Username  | Joined Oct 2017 | [432 Posts](/search?do=process&provider=Member&searchuser=620434)

> [Quoting madscalp](/thread/post/10800040#post10800040 "View Quoted Post")
> 
> Disliked
> 
> {quote} Don't worry Ezios you make a wonderful work For any reason a buy GBP didn't open with a displayed signal Could you check that too ?
> 
> Ignored

  
Today, I have not opened AUD 

"Money makes Money"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#111](/thread/post/10800094#post10800094 "Post Permalink")

  * Feb 21, 2018 9:06pm  Feb 21, 2018 9:06pm 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

> [Quoting syndicat](/thread/post/10800078#post10800078 "View Quoted Post")
> 
> Disliked
> 
> {quote} Today, I have not opened AUD
> 
> Ignored

The previous version was working fine...minor issue.  
We ask too many things at the same time.  
Let our buddies fix the issues quietly. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#112](/thread/post/10800101#post10800101 "Post Permalink")

  * Feb 21, 2018 9:09pm  Feb 21, 2018 9:09pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar620434_4.gif) syndicat](syndicat)

  * | Additional Username  | Joined Oct 2017 | [432 Posts](/search?do=process&provider=Member&searchuser=620434)

> [Quoting faryne](/thread/post/10799837#post10799837 "View Quoted Post")
> 
> Disliked
> 
> Here is my latest release. Bugs are fixed. I added a breakeven parameter to lock profit @1, and the standard deviation of curencies's strenght to get the "volatility" of forex. It may be a condition to mean reverting. Let me know if everything works well. {file}
> 
> Ignored

faryne what is the responsibility of this parameter - add new trades ? 

"Money makes Money"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#113](/thread/post/10800161#post10800161 "Post Permalink")

  * Feb 21, 2018 9:26pm  Feb 21, 2018 9:26pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar158134_11.gif) jusiur](jusiur)

  * Joined Oct 2010 | Status: Trader | [646 Posts](/search?do=process&provider=Member&searchuser=158134)

> [Quoting madscalp](/thread/post/10788513#post10788513 "View Quoted Post")
> 
> Disliked
> 
> {quote} Thank you. The main difficulty in this system is the entry. We need a good entry to avoid a too important DD. So sometimes we have to add new baskets in order to average. I suggest strongly baskets with small lots. Syndicat, a member, tried the system this week..... IMO DD too big but good results [https://www.myfxbook.com/members/Str...ndmade/2421353](https://www.myfxbook.com/members/Strateg2000/handmade/2421353)
> 
> Ignored

SM at some point realize this and give a good alternative in [this](https://www.forexfactory.com/showthread.php?p=9060567#post9060567) post 

Humble & Kalcker CLO2 = Covid killer

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#114](/thread/post/10800209#post10800209 "Post Permalink")

  * Feb 21, 2018 9:43pm  Feb 21, 2018 9:43pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar523703_1.gif) faryne](faryne)

  * | Joined Oct 2016  | Status: Trader | [93 Posts](/search?do=process&provider=Member&searchuser=523703)

> [Quoting LuXing](/thread/post/10800006#post10800006 "View Quoted Post")
> 
> Disliked
> 
> {quote} Good thinking ! Getting in interesting territory. Might be a good idea to adjust stdev to cater for volatility decay over time ;-) Jonathan Kinlay explains how you could do that in [this article](http://jonathankinlay.com/2014/05/the-mathematics-of-scalping/). Of course I am not saying you should, but once adjusted you could maybe think about plenty of neat things such as statistical outliers, ... LuXing
> 
> Ignored

Nice suggestion. I'm a huge fan of statistical trading.  
  

> Quote
> 
> Disliked
> 
> faryne what is the responsibility of this parameter - add new trades ?

If "false", any new trade will be open (but still profit/loss management).  
That let you change other parameters (like TP/SL) without reset the timer and reopen same basket. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#115](/thread/post/10800369#post10800369 "Post Permalink")

  * Feb 21, 2018 10:28pm  Feb 21, 2018 10:28pm 

  * [ leougo](leougo)

  * | Joined Jul 2010  | Status: Trader | [35 Posts](/search?do=process&provider=Member&searchuser=149780)

hi guys am in on this. could you pls show your trades with chats for us to understand. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#116](/thread/post/10800457#post10800457 "Post Permalink")

  * Feb 21, 2018 10:48pm  Feb 21, 2018 10:48pm 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

difficult to answer.. the display signal was meant for manual trade.  
when you introduced the logic of 3 steps i did not updated the dispoay signal upon this logic  
so the signal is display when deltaup >= delta or deltaup >= delta regardless of delta1 and delta2.  
so.. it depends on wat was this signal and wen and how many basket were opened... I told you no more than 6  
basket 

> [Quoting madscalp](/thread/post/10800040#post10800040 "View Quoted Post")
> 
> Disliked
> 
> {quote} Don't worry Ezios you make a wonderful work For any reason a buy GBP didn't open with a displayed signal Could you check that too ?
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#117](/thread/post/10800520#post10800520 "Post Permalink")

  * Feb 21, 2018 11:00pm  Feb 21, 2018 11:00pm 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

> [Quoting Ezios](/thread/post/10800457#post10800457 "View Quoted Post")
> 
> Disliked
> 
> difficult to answer.. the display signal was meant for manual trade. when you introduced the logic of 3 steps i did not updated the dispoay signal upon this logic so the signal is display when deltaup >= delta or deltaup >= delta regardless of delta1 and delta2. so.. it depends on wat was this signal and wen and how many basket were opened... I told you no more than 6 basket {quote}
> 
> Ignored

So for you all is OK in the last version v2 to open trades ?  

> [Quoting leougo](/thread/post/10800369#post10800369 "View Quoted Post")
> 
> Disliked
> 
> hi guys am in on this. could you pls show your trades with chats for us to understand.
> 
> Ignored

You are welcome. Currently this thread has 6 pages. You can find the spirit of the method. No need charts. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#118](/thread/post/10800563#post10800563 "Post Permalink")

  * Feb 21, 2018 11:10pm  Feb 21, 2018 11:10pm 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

yes. unless the string of selection of currencies gives some issue. i did not test it fully.  
this evening i will do some try and if i see dont working this string is better i remove it.  
the main goal is to make the system working for all currencies.... we will se... i dont want to co mplicate  
the task ... e

> [Quoting madscalp](/thread/post/10800520#post10800520 "View Quoted Post")
> 
> Disliked
> 
> {quote} So for you all is OK in the last version v2 to open trades ? {quote} You are welcome. Currently this thread has 6 pages. You can find the spirit of the method. No need charts.
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#119](/thread/post/10800668#post10800668 "Post Permalink")

  * Edited Feb 22, 2018 12:04am  Feb 21, 2018 11:24pm | Edited Feb 22, 2018 12:04am 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

> [Quoting Ezios](/thread/post/10800563#post10800563 "View Quoted Post")
> 
> Disliked
> 
> yes. unless the string of selection of currencies gives some issue. i did not test it fully. this evening i will do some try and if i see dont working this string is better i remove it. the main goal is to make the system working for all currencies.... we will se... i dont want to co mplicate the task ... e{quote}
> 
> Ignored

no problem  
as said above, the EA didn't open a buy GBP with my settings....I don't know why...maybe a mistake from me but I had no basket open at this time  

> [Quoting jusiur](/thread/post/10800161#post10800161 "View Quoted Post")
> 
> Disliked
> 
> {quote} SM at some point realize this and give a good alternative in [this](https://www.forexfactory.com/showthread.php?p=9060567#post9060567) post
> 
> Ignored

many thx jusiur for this link but it seems relevant for a pair no a basket...what do you think about ?  

> [Quoting faryne](/thread/post/10799837#post10799837 "View Quoted Post")
> 
> Disliked
> 
> the standard deviation of curencies's strenght to get the "volatility" of forex {file}
> 
> Ignored

interesting concept and in addition certified by LuXing....wooooh  
surely a good add  

> [Quoting LuXing](/thread/post/10800006#post10800006 "View Quoted Post")
> 
> Disliked
> 
> {quote} Jonathan Kinlay explains how you could do that in [this article](http://jonathankinlay.com/2014/05/the-mathematics-of-scalping/).
> 
> Ignored

Gripping reading...I see that your trading style is widely inspired by this theory...small TP big SL  
Do you note a positive effect in practice ?  
How do you advise the introduction of this notion in basket trading ? because you trade only pairs 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#120](/thread/post/10801319#post10801319 "Post Permalink")

  * Edited 1:55am  Feb 22, 2018 1:26am | Edited 1:55am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar620434_4.gif) syndicat](syndicat)

  * | Additional Username  | Joined Oct 2017 | [432 Posts](/search?do=process&provider=Member&searchuser=620434)

> [Quoting faryne](/thread/post/10799837#post10799837 "View Quoted Post")
> 
> Disliked
> 
> Here is my latest release. Bugs are fixed. I added a breakeven parameter to lock profit @1, and the standard deviation of curencies's strenght to get the "volatility" of forex. It may be a condition to mean reverting. Let me know if everything works well. {file}
> 
> Ignored

  
faryne You can add moving breakeven? step 4 ?  
  
  
  
Was opened on 1 shopping cart at AUD value of -4.2, then the value was -3.5 and the achievement of the second time value -4.2 Advisor again opened the basket purchase AUD..... 

"Money makes Money"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Playing with the currencies: Gabin System
  *   * [ **Reply to Thread** ](/thread/739272-playing-with-the-currencies-gabin-system/reply#reply)

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

[Doubling up method or playing casino](/thread/4169-doubling-up-method-or-playing-casino "Hi everyone, 
  
I was thinking about one strategy which I called doubling up method but I want to share it and you to review and make...") 24 replies

[Playing the Double-Up Game?](/thread/42119-playing-the-double-up-game "It's sure a crazy full of risk system. I was just wondering if anyone ever heard of someone doing this and winning? 
  
With this system...") 40 replies

[Playing with datetime...](/thread/36065-playing-with-datetime "Hi, 
  
Setting the date, manually, in Alert 2 to todays date, why does Alert 1 return a different value than Alert 2? Even using...") 2 replies

[Playing the Breakout Trade](/thread/6189-playing-the-breakout-trade "by Abe Cofnas 
 
When markets move, particularly in Forex, they move fast. We all have witnessed breakouts and have had the occasion to...") 4 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/739272-playing-with-the-currencies-gabin-system/reply#reply)
  * Subscribe
  * [161](javascript:void\(0\);)

Attachments: Playing with the currencies: Gabin System

Tags: Playing with the currencies: Gabin System

#  [](/thread/739272-playing-with-the-currencies-gabin-system)Playing with the currencies: Gabin System 

  * 

  * [#121](/thread/post/10801644#post10801644 "Post Permalink")

  * Edited 4:22am  Feb 22, 2018 2:29am | Edited 4:22am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar523703_1.gif) faryne](faryne)

  * | Joined Oct 2016  | Status: Trader | [93 Posts](/search?do=process&provider=Member&searchuser=523703)

> [Quoting syndicat](/thread/post/10801319#post10801319 "View Quoted Post")
> 
> Disliked
> 
> {quote} faryne You can add moving breakeven? step 4 ? Was opened on 1 shopping cart at AUD value of -4.2, then the value was -3.5 and the achievement of the second time value -4.2 Advisor again opened the basket purchase AUD.....
> 
> Ignored

Weird, I had same basket but only open once. Remember that once "Must Wait" is NULL, **all** signal are reset. So it could take step1 again.  
Here is the version with breakeven value in parameter (so not trailing, you must change it every time you want).  
I also added a normalized version of VUC/VLC (SDV) which isthe number of standard deviation exprimed.  
And the hurst exponent. Don't know if it will be usefull, but I'm testing. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot1.png
Size: 16 KB](/attachment/image/2686449/thumbnail?d=1519234135)](/attachment/image/2686449?d=1519234135)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#122](/thread/post/10801667#post10801667 "Post Permalink")

  * Feb 22, 2018 2:44am  Feb 22, 2018 2:44am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar556193_1.gif) Fatso](fatso)

  * | Joined Feb 2017  | Status: Trader | [111 Posts](/search?do=process&provider=Member&searchuser=556193)

> [Quoting Ezios](/thread/post/10788896#post10788896 "View Quoted Post")
> 
> Disliked
> 
> thank you Luxing for your contribution. We will try the system in demo step by step to understand the levels of trigger, take profit and stop loss to apply. Preparing me to transform the indicator into ea I post a last version where i put a black background box to hide the lines of graphic that disturb the vision of the values. I cutt off from the input x and y axis because i want all this in fixed position. I will continue the ea adding step by step what we need. {file}
> 
> Ignored

Hi Ezios or  [faryne](https://www.forexfactory.com/faryne). I would like to kindly request a **_SOUND ALERT_** to the indicator. I am trading manual; so during the day when I am at work I depend on the email alert. However for Asia session its early morning/ _just after midnigh_ t here in South Africa and I will need a SOUND ALERT to be alerted when trading opportunity arises so I wake up to place trades.  
Your EMAIL ALERT is doing great for me....I just need the _SOUND ALERT_ for ASIA SESSION. Please

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#123](/thread/post/10801899#post10801899 "Post Permalink")

  * Feb 22, 2018 4:03am  Feb 22, 2018 4:03am 

  * [ Namor](namor)

  * | Joined Sep 2012  | Status: Trader | [106 Posts](/search?do=process&provider=Member&searchuser=293510)

Hi faryne,  
  
I am trying your Ea. It goes well, but I don't know why it opens the same baskets twice. Once would be enough.  
Look at the screenshot! AUD baskets was opened twice. First time at 18:49:50 and then at 20:46:36. Thank you for your reply. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: aaa.jpeg
Size: 125 KB](/attachment/image/2686572/thumbnail?d=1519239793)](/attachment/image/2686572?d=1519239793)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#124](/thread/post/10802015#post10802015 "Post Permalink")

  * Edited 5:59pm  Feb 22, 2018 4:22am | Edited 5:59pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar523703_1.gif) faryne](faryne)

  * | Joined Oct 2016  | Status: Trader | [93 Posts](/search?do=process&provider=Member&searchuser=523703)

> [Quoting Namor](/thread/post/10801899#post10801899 "View Quoted Post")
> 
> Disliked
> 
> Hi faryne, I am trying your Ea. It goes well, but I don't know why it opens the same baskets twice. Once would be enough. Look at the screenshot! AUD baskets was opened twice. First time at 18:49:50 and then at 20:46:36. Thank you for your reply. {image}
> 
> Ignored

As I said, soon as the timer is at 0 (by default 1 hour next last open basket for each pair), all step and basket are reset. So the EA will reopen the same basket if condition is met.  
Version with trailing stop (stop set at be_level-be_value). 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#125](/thread/post/10802218#post10802218 "Post Permalink")

  * Feb 22, 2018 5:02am  Feb 22, 2018 5:02am 

  * [ Namor](namor)

  * | Joined Sep 2012  | Status: Trader | [106 Posts](/search?do=process&provider=Member&searchuser=293510)

> [Quoting faryne](/thread/post/10802015#post10802015 "View Quoted Post")
> 
> Disliked
> 
> {quote} As I said, soon as the timer is at 0 (by default 1 hour next last open basket for each pair), all step and basket are reset. So the EA will reopen the same basket if condition is met. Version with trailing stop (stop set at be_level-be_value). {file}
> 
> Ignored

Thank you for your reply. Is it possible to open the baskets for the individual currency only once and not be relied on the timer? Because nobody knows how log will the trade last and it is difficult to set hour on the timer. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#126](/thread/post/10802253#post10802253 "Post Permalink")

  * Feb 22, 2018 5:06am  Feb 22, 2018 5:06am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar620434_4.gif) syndicat](syndicat)

  * | Additional Username  | Joined Oct 2017 | [432 Posts](/search?do=process&provider=Member&searchuser=620434)

faryne Now the AUD Delta -5 !!! the EA does not open trading.... USD Delta -4,8 !!! the EA does not open trading....![](https://resources.faireconomy.media/images/emojis/64/1f602.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f602.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f602.png?v=15.1)

"Money makes Money"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#127](/thread/post/10802339#post10802339 "Post Permalink")

  * Feb 22, 2018 5:18am  Feb 22, 2018 5:18am 

  * [ Namor](namor)

  * | Joined Sep 2012  | Status: Trader | [106 Posts](/search?do=process&provider=Member&searchuser=293510)

> [Quoting syndicat](/thread/post/10802253#post10802253 "View Quoted Post")
> 
> Disliked
> 
> faryne Now the AUD Delta -5 !!! the EA does not open trading.... USD Delta -4,8 !!! the EA does not open trading....![](https://resources.faireconomy.media/images/emojis/64/1f602.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f602.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f602.png?v=15.1)
> 
> Ignored

My Ea opened baskets AUD and USD. There must be something wrong with your platform. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#128](/thread/post/10802463#post10802463 "Post Permalink")

  * Edited 5:55am  Feb 22, 2018 5:45am | Edited 5:55am 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

I agree with syndicat...the EA doesn't work properly..same issue and I don't understand really this timer option  
faryne ...maybe could you explain your dashboard ,  
for me VUC is Value of Upper Currency and you probably delta ? SDV Hurst ????  
Thank you. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#129](/thread/post/10802637#post10802637 "Post Permalink")

  * Edited 8:07am  Feb 22, 2018 6:49am | Edited 8:07am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar395711_10.gif) LuXing](luxing)

  * Joined Jan 2015 | Status: Error 404: LuXing not found | [1,586 Posts](/search?do=process&provider=Member&searchuser=395711)

Is one eye king in the land of the blind ?  
  
LuXing 

Wisdom begins in wonder

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#130](/thread/post/10802720#post10802720 "Post Permalink")

  * Edited 8:07am  Feb 22, 2018 7:10am | Edited 8:07am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar395711_10.gif) LuXing](luxing)

  * Joined Jan 2015 | Status: Error 404: LuXing not found | [1,586 Posts](/search?do=process&provider=Member&searchuser=395711)

Yes, one eye is king in the land of the blind.  
  
LuXing 

Wisdom begins in wonder

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#131](/thread/post/10802736#post10802736 "Post Permalink")

  * Feb 22, 2018 7:13am  Feb 22, 2018 7:13am 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

Good evening, I did a check on my version 2 on the selection string of the pairs to trade.  
It warks, but keep in mind you have to insert in the string the value in Upper case (AUD,CAD...)  
If you insert a blank string any pair is traded and it is for observation of the ea.  
The edit function to change magic number and lot size on the fly does not work. perhaps I will remove it.  
you can change this value from the property of the ea as usual. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#132](/thread/post/10802751#post10802751 "Post Permalink")

  * Feb 22, 2018 7:15am  Feb 22, 2018 7:15am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar620434_4.gif) syndicat](syndicat)

  * | Additional Username  | Joined Oct 2017 | [432 Posts](/search?do=process&provider=Member&searchuser=620434)

> [Quoting LuXing](/thread/post/10802637#post10802637 "View Quoted Post")
> 
> Disliked
> 
> Right then. Where were we ? {image} First and foremost, are the 8 currencies the entire population (read: all currencies) or is it a merely a sample of the population ? If you consider NOK, SEK, SGD, ZAR to name just a few should you not be taking the standard deviation of the sample instead ? Not to worry, we'll take your unadjusted stdev of the population for this example. I see you z-scored it. Good ! Post #8: {image} Six sigma was a bit exaggerated, but I was trying to make the following point. What does this standard deviation of the population...
> 
> Ignored

  
Again, a great story was written by a philosopher.![](https://resources.faireconomy.media/images/emojis/64/1f607.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f607.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f607.png?v=15.1) Maybe you should stick to the practical tips and tell us how to insert your stories in EA code???![](https://resources.faireconomy.media/images/emojis/64/1f923.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f923.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f923.png?v=15.1)

"Money makes Money"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#133](/thread/post/10802820#post10802820 "Post Permalink")

  * Edited 8:24am  Feb 22, 2018 7:59am | Edited 8:24am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar395711_10.gif) LuXing](luxing)

  * Joined Jan 2015 | Status: Error 404: LuXing not found | [1,586 Posts](/search?do=process&provider=Member&searchuser=395711)

> [Quoting syndicat](/thread/post/10802751#post10802751 "View Quoted Post")
> 
> Disliked
> 
> {quote} Again, a great story was written by a philosopher.![](https://resources.faireconomy.media/images/emojis/64/1f607.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f607.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f607.png?v=15.1) Maybe you should stick to the practical tips and tell us how to insert your stories in EA code???![](https://resources.faireconomy.media/images/emojis/64/1f923.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f923.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f923.png?v=15.1)
> 
> Ignored

  
Aw, you are really not the brightest are you ?  
On top of that, seems you have difficulties in making up your mind.  
LuXing you are not giving advice, no hang on I don't want your advice unless you prove your strategy is profitable.  
Oh no no, maybe you should stick to the practical tips and tell us how to insert your stories in EA code.  
No hang on, before you do that I have a button on my EA that does not work.  
Aw fuck, now the EA gives me another error.  
Aw what is it now, the Take Profit doesn't work.  
Aw I selected a basket but the EA does not open any trades.  
Aw, but what is the responsability of this parameter in a blackbox I have no knowledge of ?  
Aw, now the delta is -6 and is does not open trading !  
Aw, aw, awful !!!  
  
Do you really think i would disclose all my algos and explain YOU how to insert this in "your EA" code ?  
See phrase #1 of my post.  
  
Without too much spoonfeeding, I have given more hints on my EA in this thread than ever before.  
Anyway, congratulations on the great contributions you have made to this thread mate. They have been very thought provoking indeed. Keep it up demo warrior.  
  
_"Ce qui importe, ce n'est pas d'arriver, mais d'aller vers."_  
Antoine De Saint-Exupéry  
  
Best of luck to all of you bringing this project to a good end, Syndicat will guide the way !  
My participation in this one stops here and now.  
  
LuXing 

Wisdom begins in wonder

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#134](/thread/post/10802853#post10802853 "Post Permalink")

  * Feb 22, 2018 8:23am  Feb 22, 2018 8:23am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar620434_4.gif) syndicat](syndicat)

  * | Additional Username  | Joined Oct 2017 | [432 Posts](/search?do=process&provider=Member&searchuser=620434)

> [Quoting LuXing](/thread/post/10802820#post10802820 "View Quoted Post")
> 
> Disliked
> 
> {quote} Aw, you are really not the brightest are you ? On top of that, seems you have difficulties in making up your mind. LuXing you are not giving advice, no hang on I don't want your advice unless you prove your strategy is profitable. Oh no no, maybe you should stick to the practical tips and tell us how to insert your stories in EA code. No hang on, before you do that I have a button on my EA that does not work. Aw fuck, now the EA gives me another error. Aw what is it now, the Take Profit doesn't work. Aw I selected a basket but the EA does...
> 
> Ignored

  
Calm down philosopher![](https://resources.faireconomy.media/images/emojis/64/1f607.png?v=15.1) Go... Meditate![](https://resources.faireconomy.media/images/emojis/64/1f92b.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f92b.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f92b.png?v=15.1)

"Money makes Money"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#135](/thread/post/10802878#post10802878 "Post Permalink")

  * Feb 22, 2018 8:43am  Feb 22, 2018 8:43am 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

Good night boys, little modification to my v2.  
\- magic number cut from input... it can be modified by editing and pushing in the button. very confortable for me.  
\- i tried doing the same with lotsize but dont succeed so... leaved in inputs.  
\- add the visualization of magic number and lot size for debugging purpose.  
\- my v2 is running... perhaps this night we will have stop loss .... the black swan.... happy sleeping and be calm..... ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [pwtcea_v2.ex4](/attachment/file/2686900?d=1519256620) 99 KB | 265 downloads 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#136](/thread/post/10803101#post10803101 "Post Permalink")

  * Feb 22, 2018 10:59am  Feb 22, 2018 10:59am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar143927_8.gif) moodybot](moodybot)

  * Joined May 2010 | Status: Straight line Fest | [2,998 Posts](/search?do=process&provider=Member&searchuser=143927)

> [Quoting LuXing](/thread/post/10802820#post10802820 "View Quoted Post")
> 
> Disliked
> 
> {quote} Aw, you are really not the brightest are you ? On top of that, seems you have difficulties in making up your mind. LuXing you are not giving advice, no hang on I don't want your advice unless you prove your strategy is profitable. Oh no no, maybe you should stick to the practical tips and tell us how to insert your stories in EA code. No hang on, before you do that I have a button on my EA that does not work. Aw fuck, now the EA gives me another error. Aw what is it now, the Take Profit doesn't work. Aw I selected a basket but the EA does...
> 
> Ignored

  
Quite possibly, the best sequence of posts I have ever seen on FF.  
Hopefully the drama queens haven't put you off.  
  
M. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#137](/thread/post/10803385#post10803385 "Post Permalink")

  * Feb 22, 2018 1:42pm  Feb 22, 2018 1:42pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar620434_4.gif) syndicat](syndicat)

  * | Additional Username  | Joined Oct 2017 | [432 Posts](/search?do=process&provider=Member&searchuser=620434)

Madscalp hi! What is the maximum Delta Up/ Delta Down value can be? 

"Money makes Money"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#138](/thread/post/10803493#post10803493 "Post Permalink")

  * Feb 22, 2018 2:14pm  Feb 22, 2018 2:14pm 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

Good morning followers, have you had a good night? this morning i went to see the platform with my v2 running  
and i noticed 70 open orders (i.e 10 baskets). I was thinking to have programmed so that it never had to appen.  
I thought the maximum possible was 6 baskets. I remain confused.... in the next update i will insert MaxOrders that i put as  
default 42 for every magic number. Meanwhile this night no stop loss have arrived we wait for the take profit... who knows?  
good continuation.... 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: demo1.png
Size: 25 KB](/attachment/image/2687169/thumbnail?d=1519276426)](/attachment/image/2687169?d=1519276426)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#139](/thread/post/10803507#post10803507 "Post Permalink")

  * Feb 22, 2018 2:21pm  Feb 22, 2018 2:21pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar620434_4.gif) syndicat](syndicat)

  * | Additional Username  | Joined Oct 2017 | [432 Posts](/search?do=process&provider=Member&searchuser=620434)

> [Quoting Ezios](/thread/post/10803493#post10803493 "View Quoted Post")
> 
> Disliked
> 
> Good morning followers, have you had a good night? this morning i went to see the platform with my v2 running and i noticed 70 open orders (i.e 10 baskets). I was thinking to have programmed so that it never had to appen. I thought the maximum possible was 6 baskets. I remain confused.... in the next update i will insert MaxOrders that i put as default 42 for every magic number. Meanwhile this night no stop loss have arrived we wait for the take profit... who knows? good continuation.... {image}
> 
> Ignored

Hi Ezios ! I just put your EA on the test ... You have a very small drawdown for 70 orders!!! 

"Money makes Money"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#140](/thread/post/10803589#post10803589 "Post Permalink")

  * Feb 22, 2018 3:05pm  Feb 22, 2018 3:05pm 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

> [Quoting LuXing](/thread/post/10802820#post10802820 "View Quoted Post")
> 
> Disliked
> 
> {quote} My participation in this one stops here and now. LuXing
> 
> Ignored

Your participation ...really ? In FF, I have seen often sarcastic and non constructive people. You are the king.  
For the first time, you have taken a good decision.....leave this thread and don't come back ! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Playing with the currencies: Gabin System
  *   * [ **Reply to Thread** ](/thread/739272-playing-with-the-currencies-gabin-system/reply#reply)

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

[Doubling up method or playing casino](/thread/4169-doubling-up-method-or-playing-casino "Hi everyone, 
  
I was thinking about one strategy which I called doubling up method but I want to share it and you to review and make...") 24 replies

[Playing the Double-Up Game?](/thread/42119-playing-the-double-up-game "It's sure a crazy full of risk system. I was just wondering if anyone ever heard of someone doing this and winning? 
  
With this system...") 40 replies

[Playing with datetime...](/thread/36065-playing-with-datetime "Hi, 
  
Setting the date, manually, in Alert 2 to todays date, why does Alert 1 return a different value than Alert 2? Even using...") 2 replies

[Playing the Breakout Trade](/thread/6189-playing-the-breakout-trade "by Abe Cofnas 
 
When markets move, particularly in Forex, they move fast. We all have witnessed breakouts and have had the occasion to...") 4 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/739272-playing-with-the-currencies-gabin-system/reply#reply)
  * Subscribe
  * [161](javascript:void\(0\);)

Attachments: Playing with the currencies: Gabin System

Tags: Playing with the currencies: Gabin System

#  [](/thread/739272-playing-with-the-currencies-gabin-system)Playing with the currencies: Gabin System 

  * 

  * [#141](/thread/post/10803595#post10803595 "Post Permalink")

  * Feb 22, 2018 3:08pm  Feb 22, 2018 3:08pm 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

> [Quoting syndicat](/thread/post/10803507#post10803507 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi Ezios ! I just put your EA on the test ... You have a very small drawdown for 70 orders!!!
> 
> Ignored

meanwhile the ea got take profit and closed all 70 tickets... other turn other gift as we say in italy....  
test it .... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#142](/thread/post/10803602#post10803602 "Post Permalink")

  * Feb 22, 2018 3:10pm  Feb 22, 2018 3:10pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar620434_4.gif) syndicat](syndicat)

  * | Additional Username  | Joined Oct 2017 | [432 Posts](/search?do=process&provider=Member&searchuser=620434)

> [Quoting Ezios](/thread/post/10803595#post10803595 "View Quoted Post")
> 
> Disliked
> 
> {quote} meanwhile the ea got take profit and closed all 70 tickets... other turn other gift as we say in italy.... test it ....
> 
> Ignored

Congratulations on a great start!!!![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/270c-fe0f.png?v=15.1)  
  
  
I will come in may at the Giro d'italia![](https://resources.faireconomy.media/images/emojis/64/1f6b4-200d-2640-fe0f.png?v=15.1)

"Money makes Money"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#143](/thread/post/10803605#post10803605 "Post Permalink")

  * Feb 22, 2018 3:13pm  Feb 22, 2018 3:13pm 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

> [Quoting syndicat](/thread/post/10803385#post10803385 "View Quoted Post")
> 
> Disliked
> 
> Madscalp hi! What is the maximum Delta Up/ Delta Down value can be?
> 
> Ignored

Hi syndicat...I set the maximum delta at 5.2 but in theory it can reach more (see calculation)  
How many do you have seen ? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#144](/thread/post/10803621#post10803621 "Post Permalink")

  * Feb 22, 2018 3:17pm  Feb 22, 2018 3:17pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar620434_4.gif) syndicat](syndicat)

  * | Additional Username  | Joined Oct 2017 | [432 Posts](/search?do=process&provider=Member&searchuser=620434)

> [Quoting madscalp](/thread/post/10803605#post10803605 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi syndicat...I set the maximum delta at 5.2 but in theory it can reach more (see calculation) How many do you have seen ?
> 
> Ignored

  
I've seen 5.2 

"Money makes Money"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#145](/thread/post/10803622#post10803622 "Post Permalink")

  * Feb 22, 2018 3:20pm  Feb 22, 2018 3:20pm 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

> [Quoting syndicat](/thread/post/10803621#post10803621 "View Quoted Post")
> 
> Disliked
> 
> {quote} I've seen 5.2
> 
> Ignored

no more ? if it is the case, no problem ... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#146](/thread/post/10803630#post10803630 "Post Permalink")

  * Feb 22, 2018 3:26pm  Feb 22, 2018 3:26pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar620434_4.gif) syndicat](syndicat)

  * | Additional Username  | Joined Oct 2017 | [432 Posts](/search?do=process&provider=Member&searchuser=620434)

> [Quoting madscalp](/thread/post/10803622#post10803622 "View Quoted Post")
> 
> Disliked
> 
> {quote} no more ? if it is the case, no problem ...
> 
> Ignored

Have to wait for important news and see![](https://resources.faireconomy.media/images/emojis/64/1f9d0.png?v=15.1)

"Money makes Money"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#147](/thread/post/10803751#post10803751 "Post Permalink")

  * Edited 4:17pm  Feb 22, 2018 4:07pm | Edited 4:17pm 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

> [Quoting syndicat](/thread/post/10803630#post10803630 "View Quoted Post")
> 
> Disliked
> 
> {quote} Have to wait for important news and see![](https://resources.faireconomy.media/images/emojis/64/1f9d0.png?v=15.1)
> 
> Ignored

yes I'm going to remove GBP from EA  
currently I'm positive with AUD and GBP but I'm going to close GBP nextly  
Have you made a productive asian session ? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#148](/thread/post/10803882#post10803882 "Post Permalink")

  * Feb 22, 2018 5:01pm  Feb 22, 2018 5:01pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar620434_4.gif) syndicat](syndicat)

  * | Additional Username  | Joined Oct 2017 | [432 Posts](/search?do=process&provider=Member&searchuser=620434)

> [Quoting madscalp](/thread/post/10803751#post10803751 "View Quoted Post")
> 
> Disliked
> 
> {quote} yes I'm going to remove GBP from EA currently I'm positive with AUD and GBP but I'm going to close GBP nextly Have you made a productive asian session ?
> 
> Ignored

I've turned on profit protection, now covers quite a bit of $ 30-50... It is necessary to think further 

"Money makes Money"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#149](/thread/post/10803903#post10803903 "Post Permalink")

  * Feb 22, 2018 5:08pm  Feb 22, 2018 5:08pm 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

> [Quoting moodybot](/thread/post/10803101#post10803101 "View Quoted Post")
> 
> Disliked
> 
> {quote} Quite possibly, the best sequence of posts I have ever seen on FF. Hopefully the drama queens haven't put you off. M.
> 
> Ignored

Yes it's really funny ...but I have seen worse in FF since 10 years.  
Like in the true life, there are brilliant brains which want to display their knowledge with great theories of mathematicians and philosophers.  
I would have had respect for this kind of people if he had provided us good results of his methods. It is not the case...he just sneers.  
Maybe we are working for nothing but it's to us to decide. Go on, guys. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#150](/thread/post/10804071#post10804071 "Post Permalink")

  * Edited 7:56pm  Feb 22, 2018 5:55pm | Edited 7:56pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar523703_1.gif) faryne](faryne)

  * | Joined Oct 2016  | Status: Trader | [93 Posts](/search?do=process&provider=Member&searchuser=523703)

Hello guys,  
  
Latest version attached. Some explanations:  
  
**Parameters:**  
_**-t_profit**_ : once reached, all orders opened for one pair are closed  
_**-s_loss**_ : once reached (negative), all orders opened for one pair are closed  
_-breakeven_level:_ once reached, s_loss is set to current pnl-breakeven_value  
_**-breakeven_value:**_ trailing stop= distance to set the stop from current pnl  
_**-time_spread:**_ minimum time to prevent from re-entering basket (each pair). example "3"= if last trade was 2 hours ago, ea can't trade that pair for 1 hour left. Different levels are not affected : if step 1 was reached and countdown>0, ea can still trade step 2/3.  
_**-active_hurst:**_ activate of not hurst display (cpu killer)  
_**-reverting_all:**_ revert all orders  
_**-step1_min (etc):**_ step to reach to trade  
_**-magic_partial:**_ if you apply ea on multiple charts...  
_**-alert**_ : activate sound alert on new trade  
  
**About this version:**  
I added verbose details. Let me know if you met any problem with it.  
I keep the ea from re-entering same step once countdown is 0. So same basket at same level is always unique.  
I keep the ea from trading before 3am: signal are made from High/Low on the day. So the first High/Low (0.01am) is irrelevant.  
Hurst exponent: is the mean of husrt exponent from a basket for each pair. [0:0.5]=mean reverting; [0.5:1]=trending.  
VUC is the original VUC/VLC form 1st post (signed).  
SDV is the VUC/VLC normalized by the standard deviation. So VUC=5 could be SDV=2.5 if there is huge dispersion into currencies or SDV=4.5 is the pair is the exception into currencies.  
  
Please inform me from any bug.  
  
EA:  
[https://www.forexfactory.com/showthr...7#post10804477](https://www.forexfactory.com/showthread.php?p=10804477#post10804477)

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot1.png
Size: 93 KB](/attachment/image/2687391/thumbnail?d=1519289517)](/attachment/image/2687391?d=1519289517)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#151](/thread/post/10804188#post10804188 "Post Permalink")

  * Feb 22, 2018 6:28pm  Feb 22, 2018 6:28pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar523703_1.gif) faryne](faryne)

  * | Joined Oct 2016  | Status: Trader | [93 Posts](/search?do=process&provider=Member&searchuser=523703)

> [Quoting madscalp](/thread/post/10804168#post10804168 "View Quoted Post")
> 
> Disliked
> 
> Very good faryne but for clarification you can call VUC column delta column. Thank you.
> 
> Ignored

No problem ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#152](/thread/post/10804234#post10804234 "Post Permalink")

  * Feb 22, 2018 6:37pm  Feb 22, 2018 6:37pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar143927_8.gif) moodybot](moodybot)

  * Joined May 2010 | Status: Straight line Fest | [2,998 Posts](/search?do=process&provider=Member&searchuser=143927)

> [Quoting madscalp](/thread/post/10803903#post10803903 "View Quoted Post")
> 
> Disliked
> 
> {quote} Yes it's really funny ...but I have seen worse in FF since 10 years. Like in the true life, there are brilliant brains which want to display their knowledge with great theories of mathematicians and philosophers. I would have had respect for this kind of people if he had provided us good results of his methods. It is not the case...he just sneers. Maybe we are working for nothing but it's to us to decide. Go on, guys.
> 
> Ignored

What's funny to me is that I found the same when counter-trading based on strength, I also looked for the reversal from 28 pairs.  
Made my own CSM, take the data, break it down into groups, break that into individual pairs, take the average from the 28, sell at % of max, buy at % min...basket after basket.... then whammo, fast big move out of nowhere, classic manipulation. Go with the flow, not against.  
I now look to manually trade when the fan on my PC goes into overdrive with the data being accumulated... The currencies are moving. Just look at the direction.  
  
M. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#153](/thread/post/10804236#post10804236 "Post Permalink")

  * Feb 22, 2018 6:38pm  Feb 22, 2018 6:38pm 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

> [Quoting faryne](/thread/post/10804188#post10804188 "View Quoted Post")
> 
> Disliked
> 
> {quote} No problem ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)
> 
> Ignored

Are you sure that "VUC column" displays delta ?  
I remember the delta formula  
  
Currency in 1 st position ; Value of Upper Currency (VUC)  
Currency in 8 st position : Value of Lower Currency (VLC)  
Average of the 7 Others Currencies : ( A7OC )  
Calculation: DeltaUp = VUC - A7OC and DeltaDown = A7OC-VLC.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#154](/thread/post/10804249#post10804249 "Post Permalink")

  * Feb 22, 2018 6:42pm  Feb 22, 2018 6:42pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar523703_1.gif) faryne](faryne)

  * | Joined Oct 2016  | Status: Trader | [93 Posts](/search?do=process&provider=Member&searchuser=523703)

> [Quoting madscalp](/thread/post/10804236#post10804236 "View Quoted Post")
> 
> Disliked
> 
> {quote} Are you sure that "VUC column" displays delta ? I remember the delta formula Currency in 1 st position ; Value of Upper Currency (VUC) Currency in 8 st position : Value of Lower Currency (VLC) Average of the 7 Others Currencies : ( A7OC ) Calculation: DeltaUp = VUC - A7OC and DeltaDown = A7OC-VLC.
> 
> Ignored

Pretty sure yes!  
Delta=Value of Currency-A7OC  
i.e.  
VUC=Delta(1)  
VLC=-Delta(8) 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#155](/thread/post/10804281#post10804281 "Post Permalink")

  * Edited 7:32pm  Feb 22, 2018 6:50pm | Edited 7:32pm 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

> [Quoting moodybot](/thread/post/10804234#post10804234 "View Quoted Post")
> 
> Disliked
> 
> {quote} What's funny to me is that I found the same when counter-trading based on strength, I also looked for the reversal from 28 pairs. Made my own CSM, take the data, break it down into groups, break that into individual pairs, take the average from the 28, sell at % of max, buy at % min...basket after basket.... then whammo, fast big move out of nowhere, classic manipulation. Go with the flow, not against. I now look to manually trade when the fan on my PC goes into overdrive with the data being accumulated... The currencies are moving. Just...
> 
> Ignored

Yes I said many times it's a method against the flow. We are trying to use it a bit as a scalping with many precautions ( avoiding news, SL, lock tool, etc.. etc..)  
It is clear that during a big battle we'll have to be out of the market.  
Just curious to see your results...maybe a new constructive thread from you ?  

> [Quoting faryne](/thread/post/10804249#post10804249 "View Quoted Post")
> 
> Disliked
> 
> {quote} Pretty sure yes! Delta=Value of Currency-A7OC i.e. VUC=Delta(1) VLC=-Delta(8)
> 
> Ignored

You are right. The designation "VUC column" had troubled me ![](https://resources.faireconomy.media/images/emojis/64/1f600.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#156](/thread/post/10804404#post10804404 "Post Permalink")

  * Feb 22, 2018 7:31pm  Feb 22, 2018 7:31pm 

  * [ grc69](grc69)

  * | Joined Mar 2009  | Status: Trader | [21 Posts](/search?do=process&provider=Member&searchuser=97249)

Hello faryne!  
Ea has closed CHF basket according trailing stop. Attached is screenshot with ea's display! 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Medusa_1.5.png
Size: 286 KB](/attachment/image/2687477/thumbnail?d=1519295485)](/attachment/image/2687477?d=1519295485)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#157](/thread/post/10804477#post10804477 "Post Permalink")

  * Feb 22, 2018 7:55pm  Feb 22, 2018 7:55pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar523703_1.gif) faryne](faryne)

  * | Joined Oct 2016  | Status: Trader | [93 Posts](/search?do=process&provider=Member&searchuser=523703)

> [Quoting grc69](/thread/post/10804404#post10804404 "View Quoted Post")
> 
> Disliked
> 
> Hello faryne! Ea has closed CHF basket according trailing stop. Attached is screenshot with ea's display! {image}
> 
> Ignored

Thank you for you reply.  
Some display fixing. (sorry, it's hard to predict all possibilities) 

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [Medusa.ex4](/attachment/file/2687516?d=1519297090) 107 KB | 396 downloads 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#158](/thread/post/10804629#post10804629 "Post Permalink")

  * Edited 9:11pm  Feb 22, 2018 8:54pm | Edited 9:11pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar620434_4.gif) syndicat](syndicat)

  * | Additional Username  | Joined Oct 2017 | [432 Posts](/search?do=process&provider=Member&searchuser=620434)

> [Quoting faryne](/thread/post/10804477#post10804477 "View Quoted Post")
> 
> Disliked
> 
> {quote} Thank you for you reply. Some display fixing. (sorry, it's hard to predict all possibilities) {file}
> 
> Ignored

tell magik number for each shopping cart  
  
Useful indicator 

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [TradeInfo.ex4](/attachment/file/2687604?d=1519301471) 91 KB | 291 downloads 

"Money makes Money"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#159](/thread/post/10804686#post10804686 "Post Permalink")

  * Feb 22, 2018 9:17pm  Feb 22, 2018 9:17pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar523703_1.gif) faryne](faryne)

  * | Joined Oct 2016  | Status: Trader | [93 Posts](/search?do=process&provider=Member&searchuser=523703)

> [Quoting syndicat](/thread/post/10804629#post10804629 "View Quoted Post")
> 
> Disliked
> 
> {quote} tell magik number for each shopping cart Useful indicator {file}
> 
> Ignored

You've got the magic in the order comment. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#160](/thread/post/10804715#post10804715 "Post Permalink")

  * Feb 22, 2018 9:25pm  Feb 22, 2018 9:25pm 

  * [ grc69](grc69)

  * | Joined Mar 2009  | Status: Trader | [21 Posts](/search?do=process&provider=Member&searchuser=97249)

Hello again faryne!  
Another suggestion for dashboard of Medusa. Ea closed GBP basket. So instead of time EA could display profit or lose at wich orders are closed.  
  
Regards 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Medusa_1.5_1.png
Size: 305 KB](/attachment/image/2687629/thumbnail?d=1519302270)](/attachment/image/2687629?d=1519302270)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Playing with the currencies: Gabin System
  *   * [ **Reply to Thread** ](/thread/739272-playing-with-the-currencies-gabin-system/reply#reply)

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

[Doubling up method or playing casino](/thread/4169-doubling-up-method-or-playing-casino "Hi everyone, 
  
I was thinking about one strategy which I called doubling up method but I want to share it and you to review and make...") 24 replies

[Playing the Double-Up Game?](/thread/42119-playing-the-double-up-game "It's sure a crazy full of risk system. I was just wondering if anyone ever heard of someone doing this and winning? 
  
With this system...") 40 replies

[Playing with datetime...](/thread/36065-playing-with-datetime "Hi, 
  
Setting the date, manually, in Alert 2 to todays date, why does Alert 1 return a different value than Alert 2? Even using...") 2 replies

[Playing the Breakout Trade](/thread/6189-playing-the-breakout-trade "by Abe Cofnas 
 
When markets move, particularly in Forex, they move fast. We all have witnessed breakouts and have had the occasion to...") 4 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/739272-playing-with-the-currencies-gabin-system/reply#reply)
  * Subscribe
  * [161](javascript:void\(0\);)

Attachments: Playing with the currencies: Gabin System

Tags: Playing with the currencies: Gabin System

#  [](/thread/739272-playing-with-the-currencies-gabin-system)Playing with the currencies: Gabin System 

  * 

  * [#161](/thread/post/10804724#post10804724 "Post Permalink")

  * Feb 22, 2018 9:26pm  Feb 22, 2018 9:26pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar620434_4.gif) syndicat](syndicat)

  * | Additional Username  | Joined Oct 2017 | [432 Posts](/search?do=process&provider=Member&searchuser=620434)

> [Quoting faryne](/thread/post/10804686#post10804686 "View Quoted Post")
> 
> Disliked
> 
> {quote} You've got the magic in the order comment.
> 
> Ignored

  
I'll see it when you open the recycle bin... I need to now to insert in indicator which I sent  
  
hard to write numbers? 

"Money makes Money"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#162](/thread/post/10804733#post10804733 "Post Permalink")

  * Feb 22, 2018 9:28pm  Feb 22, 2018 9:28pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar620434_4.gif) syndicat](syndicat)

  * | Additional Username  | Joined Oct 2017 | [432 Posts](/search?do=process&provider=Member&searchuser=620434)

> [Quoting Ezios](/thread/post/10803595#post10803595 "View Quoted Post")
> 
> Disliked
> 
> {quote} meanwhile the ea got take profit and closed all 70 tickets... other turn other gift as we say in italy.... test it ....
> 
> Ignored

  
magic number cannot be changed.... 

"Money makes Money"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#163](/thread/post/10804922#post10804922 "Post Permalink")

  * Feb 22, 2018 10:05pm  Feb 22, 2018 10:05pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar523703_1.gif) faryne](faryne)

  * | Joined Oct 2016  | Status: Trader | [93 Posts](/search?do=process&provider=Member&searchuser=523703)

> [Quoting grc69](/thread/post/10804715#post10804715 "View Quoted Post")
> 
> Disliked
> 
> Hello again faryne! Another suggestion for dashboard of Medusa. Ea closed GBP basket. So instead of time EA could display profit or lose at wich orders are closed. Regards {image}
> 
> Ignored

No problem I'll add that on next release.  
  

> Quote
> 
> Disliked
> 
> I'll see it when you open the recycle bin... I need to now to insert in indicator which I sent  
>  hard to write numbers?

I don't understand what you want. Is that EA put magic on display corner?  
  
  
Also working on calendar integration now. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#164](/thread/post/10804939#post10804939 "Post Permalink")

  * Feb 22, 2018 10:13pm  Feb 22, 2018 10:13pm 

  * [ Namor](namor)

  * | Joined Sep 2012  | Status: Trader | [106 Posts](/search?do=process&provider=Member&searchuser=293510)

Hi faryne,  
Can your Ea be used for live account or is there any restriction? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#165](/thread/post/10804980#post10804980 "Post Permalink")

  * Feb 22, 2018 10:23pm  Feb 22, 2018 10:23pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar523703_1.gif) faryne](faryne)

  * | Joined Oct 2016  | Status: Trader | [93 Posts](/search?do=process&provider=Member&searchuser=523703)

> [Quoting Namor](/thread/post/10804939#post10804939 "View Quoted Post")
> 
> Disliked
> 
> Hi faryne, Can your Ea be used for live account or is there any restriction?
> 
> Ignored

I put a restriction, not because of any limitation, but because I coded it very quickly and it need to be well tested to debug. I don't want to be responsible for blowing accounts because of code problem (like stop don't work or other).![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#166](/thread/post/10804993#post10804993 "Post Permalink")

  * Edited 11:58pm  Feb 22, 2018 10:27pm | Edited 11:58pm 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

> [Quoting faryne](/thread/post/10804980#post10804980 "View Quoted Post")
> 
> Disliked
> 
> {quote} I put a restriction, not because of any limitation, but because I coded it very quickly and it need to be well tested to debug. I don't want to be responsible for blowing accounts because of code problem (like stop don't work or other).![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)
> 
> Ignored

You are a wise man ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)  
More the robot is improved more it is expensive for sale.  
Don't forget my royalties faryne ![](https://resources.faireconomy.media/images/emojis/64/1f600.png?v=15.1)  
Seriously it is really not recommended to go for live account. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#167](/thread/post/10805429#post10805429 "Post Permalink")

  * Feb 22, 2018 11:39pm  Feb 22, 2018 11:39pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar409665_1.gif) Fancysegs](fancysegs)

  * | Joined Apr 2015  | Status: Trader | [52 Posts](/search?do=process&provider=Member&searchuser=409665)

Weldone Guys you are doing a great Job your indicator is making me extracting money from market..sincerely i have make over 100 usd this week...God Bless You..cheers.Love from Nigeria 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#168](/thread/post/10805679#post10805679 "Post Permalink")

  * Edited 12:28am  Feb 23, 2018 12:13am | Edited 12:28am 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

> [Quoting Fancysegs](/thread/post/10805429#post10805429 "View Quoted Post")
> 
> Disliked
> 
> Weldone Guys you are doing a great Job your indicator is making me extracting money from market..sincerely i have make over 100 usd this week...God Bless You..cheers.Love from Nigeria
> 
> Ignored

Thanks for your feedback but be careful. Does your broker accept your orders ?  
  
  
Guys  
By PM, a friend has warned me that somebody was trying to copy lines of code in order to sell an EA about the system.  
This system is for free since I don't even know if it is good.  
So, coders buddies, if you post something, be sure there is a restriction. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#169](/thread/post/10805709#post10805709 "Post Permalink")

  * Feb 23, 2018 12:18am  Feb 23, 2018 12:18am 

  * [ mankindeg](mankindeg)

  * | Joined Mar 2015  | Status: Trader | [143 Posts](/search?do=process&provider=Member&searchuser=405444)

Hi guys, can anyone tell me, what timeframe the Currency strength is actually working on?   
Like, Is it the currency strength of the last hour or last 4 hours or 30 minutes...?   
Does someone know? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#170](/thread/post/10805988#post10805988 "Post Permalink")

  * Feb 23, 2018 1:09am  Feb 23, 2018 1:09am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar620434_4.gif) syndicat](syndicat)

  * | Additional Username  | Joined Oct 2017 | [432 Posts](/search?do=process&provider=Member&searchuser=620434)

> [Quoting mankindeg](/thread/post/10805709#post10805709 "View Quoted Post")
> 
> Disliked
> 
> Hi guys, can anyone tell me, what timeframe the Currency strength is actually working on? Like, Is it the currency strength of the last hour or last 4 hours or 30 minutes...? Does someone know?
> 
> Ignored

Hi 1 D 

"Money makes Money"

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#171](/thread/post/10806122#post10806122 "Post Permalink")

  * Feb 23, 2018 1:34am  Feb 23, 2018 1:34am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar409665_1.gif) Fancysegs](fancysegs)

  * | Joined Apr 2015  | Status: Trader | [52 Posts](/search?do=process&provider=Member&searchuser=409665)

> [Quoting madscalp](/thread/post/10805679#post10805679 "View Quoted Post")
> 
> Disliked
> 
> {quote} Thanks for your feedback but be careful. Does your broker accept your orders ? Guys By PM, a friend has warned me that somebody was trying to copy lines of code in order to sell an EA about the system. This system is for free since I don't even know if it is good. So, coders buddies, if you post something, be sure there is a restriction.
> 
> Ignored

  
Yes they accept the trade..I use your indicator to trade both Spread and Binary OPtion sincerely after adding my own filter to avoid excess drawdown..Its is a wonderful work..thanks 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#172](/thread/post/10806139#post10806139 "Post Permalink")

  * Feb 23, 2018 1:38am  Feb 23, 2018 1:38am 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

> [Quoting Fancysegs](/thread/post/10806122#post10806122 "View Quoted Post")
> 
> Disliked
> 
> {quote} Yes they accept the trade..I use your indicator to trade both Spread and Binary OPtion sincerely after adding my own filter to avoid excess drawdown..Its is a wonderful work..thanks
> 
> Ignored

Excellent management if you can be in front of your computer.  
It seems some brokers don't accept. Which one is yours ? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#173](/thread/post/10806323#post10806323 "Post Permalink")

  * Feb 23, 2018 2:20am  Feb 23, 2018 2:20am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar409665_1.gif) Fancysegs](fancysegs)

  * | Joined Apr 2015  | Status: Trader | [52 Posts](/search?do=process&provider=Member&searchuser=409665)

> [Quoting madscalp](/thread/post/10806139#post10806139 "View Quoted Post")
> 
> Disliked
> 
> {quote} Excellent management if you can be in front of your computer. It seems some brokers don't accept. Which one is yours ?
> 
> Ignored

am using NordFX for Spread and Binary.com for BinaryOPtions 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#174](/thread/post/10807827#post10807827 "Post Permalink")

  * Feb 23, 2018 1:32pm  Feb 23, 2018 1:32pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar620434_4.gif) syndicat](syndicat)

  * | Additional Username  | Joined Oct 2017 | [432 Posts](/search?do=process&provider=Member&searchuser=620434)

> [Quoting Ezios](/thread/post/10803595#post10803595 "View Quoted Post")
> 
> Disliked
> 
> {quote} meanwhile the ea got take profit and closed all 70 tickets... other turn other gift as we say in italy.... test it ....
> 
> Ignored

Hi Ezios! The EA opens an incomplete basket...  
  
  
2018.02.23 06:04:14.208 '60056652': order sell 0.01 CADCHF opening at market sl: 0.00000 tp: 0.00000 failed [Off quotes]  
2018.02.23 06:04:13.332 '60056652': order sell 0.01 NZDCHF opening at market sl: 0.00000 tp: 0.00000 failed [Off quotes]  
2018.02.23 06:04:12.521 '60056652': order sell 0.01 GBPCHF opening at market sl: 0.00000 tp: 0.00000 failed [Off quotes]  
2018.02.23 06:01:03.705 '60056652': order sell 0.01 AUDNZD opening at market sl: 0.00000 tp: 0.00000 failed [Off quotes]  
2018.02.23 06:01:03.216 '60056652': order sell 0.01 GBPNZD opening at market sl: 0.00000 tp: 0.00000 failed [Off quotes]  
2018.02.23 06:01:02.647 '60056652': order sell 0.01 EURNZD opening at market sl: 0.00000 tp: 0.00000 failed [Off quotes]  
2018.02.23 06:01:02.647 '60056652': order sell 0.01 EURNZD opening at market sl: 0.00000 tp: 0.00000 failed [Off quotes]  
2018.02.23 06:00:50.678 '60056652': order buy 0.01 CHFJPY opening at market sl: 0.000 tp: 0.000 failed [Off quotes]  
2018.02.23 06:00:50.223 '60056652': order buy 0.01 CADJPY opening at market sl: 0.000 tp: 0.000 failed [Off quotes]  
2018.02.23 06:00:49.666 '60056652': order buy 0.01 USDJPY opening at market sl: 0.000 tp: 0.000 failed [Off quotes] 

"Money makes Money"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#175](/thread/post/10807913#post10807913 "Post Permalink")

  * Feb 23, 2018 2:04pm  Feb 23, 2018 2:04pm 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

> [Quoting syndicat](/thread/post/10807827#post10807827 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi Ezios! The EA opens an incomplete basket... 2018.02.23 06:04:14.208 '60056652': order sell 0.01 CADCHF opening at market sl: 0.00000 tp: 0.00000 failed [Off quotes] 2018.02.23 06:04:13.332 '60056652': order sell 0.01 NZDCHF opening at market sl: 0.00000 tp: 0.00000 failed [Off quotes] 2018.02.23 06:04:12.521 '60056652': order sell 0.01 GBPCHF opening at market sl: 0.00000 tp: 0.00000 failed [Off quotes] 2018.02.23 06:01:03.705 '60056652': order sell 0.01 AUDNZD opening at market sl: 0.00000 tp: 0.00000 failed [Off quotes] 2018.02.23 06:01:03.216...
> 
> Ignored

i told you another time.... i can t help you with this error because from my broker all ok... this error depends on+  
your broker. change the broker and you will have no the error.  
for that of the magic number you have to go with mouse in the magic change it and push on the button.  
thats all. test.... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#176](/thread/post/10807931#post10807931 "Post Permalink")

  * Feb 23, 2018 2:07pm  Feb 23, 2018 2:07pm 

  * [ rakhi345](rakhi345)

  * | Joined Oct 2017  | Status: Trader | [7 Posts](/search?do=process&provider=Member&searchuser=622790)

One of the best ways to see if currency trading is right for you is to try a trading demo. You can practice your trading techniques with "play money", so there is no risk involved. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#177](/thread/post/10807944#post10807944 "Post Permalink")

  * Feb 23, 2018 2:12pm  Feb 23, 2018 2:12pm 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

> [Quoting madscalp](/thread/post/10805679#post10805679 "View Quoted Post")
> 
> Disliked
> 
> {quote} Thanks for your feedback but be careful. Does your broker accept your orders ? Guys By PM, a friend has warned me that somebody was trying to copy lines of code in order to sell an EA about the system. This system is for free since I don't even know if it is good. So, coders buddies, if you post something, be sure there is a restriction.
> 
> Ignored

I know Madscalp... there is always someone trying to copy good system.  
In my ea i ave put the restriction ONLY DEMO ACCOUNT but nothing ... if you have a copier you can  
copy tha trade from demo to real... so in next version i will put expiration date...  
the world is full of scammers... we work for free and we are testing... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#178](/thread/post/10808142#post10808142 "Post Permalink")

  * Feb 23, 2018 3:53pm  Feb 23, 2018 3:53pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar71675_5.gif) Alberto_Jazz](alberto_jazz)

  * Joined Jun 2008 | Status: Trader | [593 Posts](/search?do=process&provider=Member&searchuser=71675)

Hi, just to understand: in the expert settings I place a stop @ 100 and a take profit @ 10.   
  
So if the stop is hit only one time it burns 10 profit cycles, is it correct?  
  
Thank you 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#179](/thread/post/10808154#post10808154 "Post Permalink")

  * Feb 23, 2018 4:00pm  Feb 23, 2018 4:00pm 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

> [Quoting Alberto_Jazz](/thread/post/10808142#post10808142 "View Quoted Post")
> 
> Disliked
> 
> Hi, just to understand: in the expert settings I place a stop @ 100 and a take profit @ 10. So if the stop is hit only one time it burns 10 profit cycles, is it correct? Thank you
> 
> Ignored

exactly. for now never hit stop. the market moves so that its difficult to reach 100 euro of stop but.. who knows?  
we are testing... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#180](/thread/post/10808253#post10808253 "Post Permalink")

  * Edited 5:06pm  Feb 23, 2018 4:34pm | Edited 5:06pm 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

Hi all  
Congratulations for our coders.  
At 7:00 GMT, both EA took together the same trades in the same conditions.  
No errors in expert tab...IMO offquotes issue is due at broker.  
Just a question for faryne:  
the chart with EA attached close with 2 conditions: clicking CLOSE ALL button and SL reached. Is it correct ?  
your "basket close" function is working fine with the mention "Close by user" ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)  
small suggestion in your next version: a profit/loss indicator like the Ezios's EA. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Playing with the currencies: Gabin System
  *   * [ **Reply to Thread** ](/thread/739272-playing-with-the-currencies-gabin-system/reply#reply)

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

[Doubling up method or playing casino](/thread/4169-doubling-up-method-or-playing-casino "Hi everyone, 
  
I was thinking about one strategy which I called doubling up method but I want to share it and you to review and make...") 24 replies

[Playing the Double-Up Game?](/thread/42119-playing-the-double-up-game "It's sure a crazy full of risk system. I was just wondering if anyone ever heard of someone doing this and winning? 
  
With this system...") 40 replies

[Playing with datetime...](/thread/36065-playing-with-datetime "Hi, 
  
Setting the date, manually, in Alert 2 to todays date, why does Alert 1 return a different value than Alert 2? Even using...") 2 replies

[Playing the Breakout Trade](/thread/6189-playing-the-breakout-trade "by Abe Cofnas 
 
When markets move, particularly in Forex, they move fast. We all have witnessed breakouts and have had the occasion to...") 4 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/739272-playing-with-the-currencies-gabin-system/reply#reply)
  * Subscribe
  * [161](javascript:void\(0\);)

Attachments: Playing with the currencies: Gabin System

Tags: Playing with the currencies: Gabin System

#  [](/thread/739272-playing-with-the-currencies-gabin-system)Playing with the currencies: Gabin System 

  * 

  * [#181](/thread/post/10808384#post10808384 "Post Permalink")

  * Feb 23, 2018 5:11pm  Feb 23, 2018 5:11pm 

  * [ mankindeg](mankindeg)

  * | Joined Mar 2015  | Status: Trader | [143 Posts](/search?do=process&provider=Member&searchuser=405444)

> [Quoting Ezios](/thread/post/10807944#post10807944 "View Quoted Post")
> 
> Disliked
> 
> {quote} I know Madscalp... there is always someone trying to copy good system. In my ea i ave put the restriction ONLY DEMO ACCOUNT but nothing ... if you have a copier you can copy tha trade from demo to real... so in next version i will put expiration date... the world is full of scammers... we work for free and we are testing...
> 
> Ignored

  
Can't you add a text to the corner of the screen of your ea, that says something like: "For free at forexfactory" so that way, no one can sell your ea, because it says that you can get it here... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#182](/thread/post/10808498#post10808498 "Post Permalink")

  * Feb 23, 2018 6:59pm  Feb 23, 2018 6:59pm 

  * [ flashlj2008](flashlj2008)

  * | Joined Jul 2016  | Status: Trader | [32 Posts](/search?do=process&provider=Member&searchuser=474892)

Hi，Madscalp,both eas default setting？ 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#183](/thread/post/10808536#post10808536 "Post Permalink")

  * Feb 23, 2018 7:09pm  Feb 23, 2018 7:09pm 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

> [Quoting flashlj2008](/thread/post/10808498#post10808498 "View Quoted Post")
> 
> Disliked
> 
> Hi，Madscalp,both eas default setting？
> 
> Ignored

Yeah 4.4...4.8...5.2 sell USD and buy NZD....close USD basket in profit and NZD basket at breakeven 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#184](/thread/post/10808546#post10808546 "Post Permalink")

  * Feb 23, 2018 7:10pm  Feb 23, 2018 7:10pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar523703_1.gif) faryne](faryne)

  * | Joined Oct 2016  | Status: Trader | [93 Posts](/search?do=process&provider=Member&searchuser=523703)

> [Quoting madscalp](/thread/post/10808253#post10808253 "View Quoted Post")
> 
> Disliked
> 
> Hi all Congratulations for our coders. At 7:00 GMT, both EA took together the same trades in the same conditions. No errors in expert tab...IMO offquotes issue is due at broker. Just a question for faryne: the chart with EA attached close with 2 conditions: clicking CLOSE ALL button and SL reached. Is it correct ? your "basket close" function is working fine with the mention "Close by user" ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1) small suggestion in your next version: a profit/loss indicator like the Ezios's EA.
> 
> Ignored

Great.  
  
Do you mean global profit/loss? because it's currently display for each pair.  
  
For closing conditions: TP reached OR SL reached OR trailing stop (locking) reached OR "close all" OR "close basket". 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#185](/thread/post/10808566#post10808566 "Post Permalink")

  * Edited 7:36pm  Feb 23, 2018 7:20pm | Edited 7:36pm 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

> [Quoting faryne](/thread/post/10808546#post10808546 "View Quoted Post")
> 
> Disliked
> 
> {quote} Great. Do you mean global profit/loss? because it's currently display for each pair. For closing conditions: TP reached OR SL reached OR trailing stop (locking) reached OR "close all" OR "close basket".
> 
> Ignored

Hi faryne  
Of course it's the global P/L since P/L is displayed for each currency ( it's a child's play for you ![](https://resources.faireconomy.media/images/emojis/64/1f600.png?v=15.1))  
You can display the different mentions but IMO it's important to do an absolute STOP TRADING after a SL. Maybe a reset if the trader wants to come back in the market.  
What do you think about ?  
  
Many people have contacted me by PM for explanations often for the same things. I'm sorry but I can't answer at everybody.  
Please read the first post and the warning. It seems clear.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#186](/thread/post/10808702#post10808702 "Post Permalink")

  * Feb 23, 2018 7:50pm  Feb 23, 2018 7:50pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar523703_1.gif) faryne](faryne)

  * | Joined Oct 2016  | Status: Trader | [93 Posts](/search?do=process&provider=Member&searchuser=523703)

> [Quoting madscalp](/thread/post/10808566#post10808566 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi faryne Of course it's the global P/L since P/L is displayed for each currency ( it's a child's play for you ![](https://resources.faireconomy.media/images/emojis/64/1f600.png?v=15.1)) You can display the different mentions but IMO it's important to do an absolute STOP TRADING after a SL. Maybe a reset if the trader wants to come back in the market. What do you think about ? Many people have contacted me by PM for explanations often for the same things. I'm sorry but I can't answer at everybody. Please read the first post and the warning. It seems clear.
> 
> Ignored

Something like that? 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot1.png
Size: 43 KB](/attachment/image/2689132/thumbnail?d=1519383016)](/attachment/image/2689132?d=1519383016)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#187](/thread/post/10808796#post10808796 "Post Permalink")

  * Edited 8:29pm  Feb 23, 2018 8:13pm | Edited 8:29pm 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

> [Quoting faryne](/thread/post/10808702#post10808702 "View Quoted Post")
> 
> Disliked
> 
> {quote} Something like that? {image}
> 
> Ignored

Wonderful. You are a genius.  
What is your thouhgt about absolute Stop trading after SL ? 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: 4.jpg
Size: 123 KB](/attachment/image/2689180/thumbnail?d=1519385384)](/attachment/image/2689180?d=1519385384)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#188](/thread/post/10808976#post10808976 "Post Permalink")

  * Feb 23, 2018 9:03pm  Feb 23, 2018 9:03pm 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

yes i will put some credit lines in next version too.  

> [Quoting mankindeg](/thread/post/10808384#post10808384 "View Quoted Post")
> 
> Disliked
> 
> {quote} Can't you add a text to the corner of the screen of your ea, that says something like: "For free at forexfactory" so that way, no one can sell your ea, because it says that you can get it here...
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#189](/thread/post/10809171#post10809171 "Post Permalink")

  * Feb 23, 2018 10:11pm  Feb 23, 2018 10:11pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar71675_5.gif) Alberto_Jazz](alberto_jazz)

  * Joined Jun 2008 | Status: Trader | [593 Posts](/search?do=process&provider=Member&searchuser=71675)

I try to add my 2 cents with this idea.  
  
1\. When the trigger is hit we open a FAKE BASKET: not a real basket on the market, but a basket on the paper.  
2\. When the loss on the FAKE BASKET is (for instance) -4%, we prepare to open the REAL BASKET.  
3\. When the loss on the FAKE BASKET is -2% we open the REAL BASKET.  
4\. We are assuming that the trend has hit the bottom @ -4%.  
5\. We will close the REAL BASKET @ -4 (loss will be -2%), or we will close the REAL BASKET @ +1% (gain will be +3%).  
6\. In this way the risk/reward is much better.  
  
The power of the system is that we define a clear stop zone and we hope that market has hit the bottom behind us.  
  
The problem is how to trace the FAKE BASKET on the paper.  
  
I hope it’s clear. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#190](/thread/post/10809217#post10809217 "Post Permalink")

  * Feb 23, 2018 10:27pm  Feb 23, 2018 10:27pm 

  * [ maaRIF2015](maarif2015)

  * | Joined Feb 2016  | Status: Trader | [37 Posts](/search?do=process&provider=Member&searchuser=446971)

Thanks [ madscalp](https://www.forexfactory.com/madscalp) for your kind gift to ff traders.  
i think VUC values for different currencies are different.For example GBP is volatile currency so its VUC value easily reach 5 or -5 where NZD currency VUC value on average is 4.7 I want to ask you can you please add one feature in EA so that we can set VUC values according to each currency .i mean the feature like:  
Min VUC value for GBP=  
Max VUC value for GBP=  
Min value for NZD=  
Max value for NZD=  
and so on.because when GBP is on the top i need to adjust VUC values for each currency according to their strength  
thanks a lot for your efforts i found this EA very interesting and profitable. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#191](/thread/post/10809218#post10809218 "Post Permalink")

  * Feb 23, 2018 10:28pm  Feb 23, 2018 10:28pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar523703_1.gif) faryne](faryne)

  * | Joined Oct 2016  | Status: Trader | [93 Posts](/search?do=process&provider=Member&searchuser=523703)

> [Quoting madscalp](/thread/post/10808796#post10808796 "View Quoted Post")
> 
> Disliked
> 
> {quote} Wonderful. You are a genius. What is your thouhgt about absolute Stop trading after SL ? {image}
> 
> Ignored

I set an absolute SL which prevent from automatic new open (you must reinit the EA). On the contrary, SL for individual pair is not a EA stopper.  
  

> Quote
> 
> Disliked
> 
> I try to add my 2 cents with this idea.  
>  1\. When the trigger is hit we open a FAKE BASKET: not a real basket on the market, but a basket on the paper.  
>  2\. When the loss on the FAKE BASKET is (for instance) -4%, we prepare to open the REAL BASKET.  
>  3\. When the loss on the FAKE BASKET is -2% we open the REAL BASKET.  
>  4\. We are assuming that the trend has hit the bottom @ -4%.  
>  5\. We will close the REAL BASKET @ -4 (loss will be -2%), or we will close the REAL BASKET @ +1% (gain will be +3%).  
>  6\. In this way the risk/reward is much better.  
>  The power of the...

  
Interesting, and definitly not the same result as simply shifting triggers. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#192](/thread/post/10809360#post10809360 "Post Permalink")

  * Feb 23, 2018 10:58pm  Feb 23, 2018 10:58pm 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

I will leave this task to faryne... i dont know how to handle a phantom basket or 2 or 3 or 4....  
and i like kiss systems....  

> [Quoting Alberto_Jazz](/thread/post/10809171#post10809171 "View Quoted Post")
> 
> Disliked
> 
> I try to add my 2 cents with this idea. 1. When the trigger is hit we open a FAKE BASKET: not a real basket on the market, but a basket on the paper. 2. When the loss on the FAKE BASKET is (for instance) -4%, we prepare to open the REAL BASKET. 3. When the loss on the FAKE BASKET is -2% we open the REAL BASKET. 4. We are assuming that the trend has hit the bottom @ -4%. 5. We will close the REAL BASKET @ -4 (loss will be -2%), or we will close the REAL BASKET @ +1% (gain will be +3%). 6. In this way the risk/reward is much better. The power of the...
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#193](/thread/post/10809452#post10809452 "Post Permalink")

  * Edited 11:44pm  Feb 23, 2018 11:27pm | Edited 11:44pm 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

Guys  
The new ideas are gushing.  
Me too I'm thinking about a NO MORE button.  
What is it ?  
I suppose a period of volatility with already 3 open USD baskets.  
My DD is increasing dangerously and I see on the indicator another possibility of trade on JPY.  
Of course, I don't want to open a new basket.  
So I click on NO MORE button to avoid a new open and keep the control of my 3 baskets.  
Is it possible ?  
  
About the ghost basket, I don't know if faryne can make it. He has already worked a lot this week ![](https://resources.faireconomy.media/images/emojis/64/1f600.png?v=15.1)  
In addition, we risk to miss some interesting trades. Depending the level...If the ghost basket opens at 4.4 and that there is a reversal, we miss the trade.  
Or I didn't understood...  
  

> [Quoting maaRIF2015](/thread/post/10809217#post10809217 "View Quoted Post")
> 
> Disliked
> 
> Thanks [madscalp](https://www.forexfactory.com/madscalp) for your kind gift to ff traders. i think VUC values for different currencies are different.For example GBP is volatile currency so its VUC value easily reach 5 or -5 where NZD currency VUC value on average is 4.7 I want to ask you can you please add one feature in EA so that we can set VUC values according to each currency .i mean the feature like: Min VUC value for GBP= Max VUC value for GBP= Min value for NZD= Max value for NZD= and so on.because when GBP is on the top i need...
> 
> Ignored

I'm not sure to understand. NZD is a quiet currency and today it has touched many times an inhabitual VLC of 0.2. What precisely do you propose ? a recalculation of delta ? see with a coder  
[EDIT] Currently in the day NZD is my only (small) loss in progress ..LOL... happily 3 others good winning baskets 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#194](/thread/post/10809533#post10809533 "Post Permalink")

  * Feb 23, 2018 11:50pm  Feb 23, 2018 11:50pm 

  * [ mankindeg](mankindeg)

  * | Joined Mar 2015  | Status: Trader | [143 Posts](/search?do=process&provider=Member&searchuser=405444)

> [Quoting Alberto_Jazz](/thread/post/10809171#post10809171 "View Quoted Post")
> 
> Disliked
> 
> I try to add my 2 cents with this idea. 1. When the trigger is hit we open a FAKE BASKET: not a real basket on the market, but a basket on the paper. 2. When the loss on the FAKE BASKET is (for instance) -4%, we prepare to open the REAL BASKET. 3. When the loss on the FAKE BASKET is -2% we open the REAL BASKET. 4. We are assuming that the trend has hit the bottom @ -4%. 5. We will close the REAL BASKET @ -4 (loss will be -2%), or we will close the REAL BASKET @ +1% (gain will be +3%). 6. In this way the risk/reward is much better. The power of the...
> 
> Ignored

  
This sounds counterproductive to be honest, because it can also work against you.   
For example, if your "fake basket" ist @ **+2%** and doesn't go back down, you have to either miss the trade, or, make less profit, than if you would have just entered as the signal was there. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#195](/thread/post/10810587#post10810587 "Post Permalink")

  * Feb 24, 2018 3:02am  Feb 24, 2018 3:02am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar46777_5.gif) shiva](shiva)

  * Joined Aug 2007 | Status: Doing It In Dubai | [2,457 Posts](/search?do=process&provider=Member&searchuser=46777)

> [Quoting mankindeg](/thread/post/10809533#post10809533 "View Quoted Post")
> 
> Disliked
> 
> {quote} This sounds counterproductive to be honest, because it can also work against you. For example, if your "fake basket" ist @ +2% and doesn't go back down, you have to either miss the trade, or, make less profit, than if you would have just entered as the signal was there.
> 
> Ignored

Missing a trade to get a high probability entry is a good thing really. AND, "less profit" is not a bad thing at all. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#196](/thread/post/10812035#post10812035 "Post Permalink")

  * Feb 24, 2018 9:43pm  Feb 24, 2018 9:43pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar352244_2.gif) vinvlad](vinvlad)

  * Joined Oct 2013 | Status: Trader | [146 Posts](/search?do=process&provider=Member&searchuser=352244) | Online Now 

Thanks to [madscalp](https://www.forexfactory.com/madscalp) for sharing your idea of trading.Thanks to [Ezios](https://www.forexfactory.com/ezios) and [ faryne](https://www.forexfactory.com/faryne) for translating this idea into technical tools.  
I have been testing the strategy for several days. I prefer to trade manually on currency pairs. Revers almost perfectly, especially if they are at R/S levels. Well, you can visually control the SL and TP.  
I appeal to [Ezios](https://www.forexfactory.com/ezios) ![](https://resources.faireconomy.media/images/emojis/64/1f64f.png?v=15.1)  
A huge relief would be the addition of these options to the indicator cm_mod. I think that many people will support and appreciate this. ![](https://resources.faireconomy.media/images/emojis/64/1f514.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f514.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f514.png?v=15.1)  

Attached Image

![](/attachment/image/2690515?d=1519476225)

  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Chart_Csm.png
Size: 147 KB](/attachment/image/2690516/thumbnail?d=1519476504)](/attachment/image/2690516?d=1519476504)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#197](/thread/post/10812282#post10812282 "Post Permalink")

  * Feb 25, 2018 12:22am  Feb 25, 2018 12:22am 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

> [Quoting vinvlad](/thread/post/10812035#post10812035 "View Quoted Post")
> 
> Disliked
> 
> Thanks to [madscalp](https://www.forexfactory.com/madscalp) for sharing your idea of trading.Thanks to [Ezios](https://www.forexfactory.com/ezios) and [ faryne](https://www.forexfactory.com/faryne) for translating this idea into technical tools. I have been testing the strategy for several days. I prefer to trade manually on currency pairs. Revers almost perfectly, especially if they are at R/S levels. Well, you can visually control the SL and TP. I appeal to [Ezios](https://www.forexfactory.com/ezios) ![](https://resources.faireconomy.media/images/emojis/64/1f64f.png?v=15.1)...
> 
> Ignored

Hi vinvlad  
Yes Ezios made an excellent indicator which displays too a good pair to trade.  
Sometimes I do it also with S/R help like you but curiously the discussion here has been mostly about basket trading.  
See with him if he wants to make your request. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#198](/thread/post/10812943#post10812943 "Post Permalink")

  * Feb 25, 2018 12:00pm  Feb 25, 2018 12:00pm 

  * [ G.Kad](g.kad)

  * | Joined Oct 2017  | Status: LOL | [160 Posts](/search?do=process&provider=Member&searchuser=616697)

> [Quoting madscalp](/thread/post/10809452#post10809452 "View Quoted Post")
> 
> Disliked
> 
> Guys The new ideas are gushing. Me too I'm thinking about a NO MORE button. What is it ? I suppose a period of volatility with already 3 open USD baskets. My DD is increasing dangerously and I see on the indicator another possibility of trade on JPY. Of course, I don't want to open a new basket. So I click on NO MORE button to avoid a new open and keep the control of my 3 baskets. Is it possible ? About the ghost basket, I don't know if faryne can make it. He has already worked a lot this week ![](https://resources.faireconomy.media/images/emojis/64/1f600.png?v=15.1)...
> 
> Ignored

There was a thread named "Basked Trading EA" and there was 3 options in EA for such things:  
1.The "Stop After <#>" button. (The EA will stop trading after <#> numbers of baskets traded or profit/loss triggered.   
2\. "One trade per candle" true/false (if EA is placed on 1hr TF, it will only take 1 trade for every 1hr(4hr,days, weeks, etc.))   
3\. Max trades open.   
You can search for member Seller9. maybe he can advice some coding logic.   

> [Quoting madscalp](/thread/post/10809452#post10809452 "View Quoted Post")
> 
> Disliked
> 
> ... I'm not sure to understand. NZD is a quiet currency and today it has touched many times an inhabitual VLC of 0.2. What precisely do you propose ? a recalculation of delta ? see with a coder [EDIT] Currently in the day NZD is my only (small) loss in progress ..LOL... happily 3 others good winning baskets
> 
> Ignored

Are you aware of NZD news before previous day closed?   
Don't blindly follow indicators, they lag. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#199](/thread/post/10813061#post10813061 "Post Permalink")

  * Edited 4:16pm  Feb 25, 2018 3:19pm | Edited 4:16pm 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

> [Quoting G.Kad](/thread/post/10812943#post10812943 "View Quoted Post")
> 
> Disliked
> 
> There was a thread named "Basked Trading EA" and there was 3 options in EA for such things: 1.The "Stop After <#>" button. (The EA will stop trading after <#> numbers of baskets traded or profit/loss triggered. 2. "One trade per candle" true/false (if EA is placed on 1hr TF, it will only take 1 trade for every 1hr(4hr,days, weeks, etc.)) 3. Max trades open. You can search for member Seller9. maybe he can advice some coding logic.
> 
> Ignored

I think faryne can do that easily. It's just a command to not open momentarily new trades.  
  
  

> Quote
> 
> Disliked
> 
> Are you aware of NZD news before previous day closed? Don't blindly follow indicators, they lag.

Sure. It's why we need a news calendar ( post # 29 ) . I admit that I do not always look at minor currencies ![](https://resources.faireconomy.media/images/emojis/64/1f44e.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f641.png?v=15.1)  
faryne have to include it in the next version 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#200](/thread/post/10813201#post10813201 "Post Permalink")

  * Edited Feb 26, 2018 12:40am  Feb 25, 2018 6:05pm | Edited Feb 26, 2018 12:40am 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

Hi all  
I have opened on feb 19 a small demo account ( $ 1 000 ) to test the system.  
You see the results below but there are some mistakes:  
1 st from me : several baskets were opened with 0.1 lots...of course only 0.01 lot ...no more  
2 nd from EA testing : too many baskets due at bugs  
So the results turn around 20 % weekly profit instead of 36 %.  
I set a 5 % SL and it was never reached ( of course it will be one day )  
Max baskets in progress : 5....max DD observed : 3 %.  
What conclusion ? lucky week ? probably...  
I still don't know the best way to close the trades. Mostly were closed by lock and sometimes the profit continued.  
Just curious to see your results and to read your suggestions to do even more a safer system. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: 6.jpg
Size: 47 KB](/attachment/image/2691111/thumbnail?d=1519549460)](/attachment/image/2691111?d=1519549460)   

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Playing with the currencies: Gabin System
  *   * [ **Reply to Thread** ](/thread/739272-playing-with-the-currencies-gabin-system/reply#reply)

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

[Doubling up method or playing casino](/thread/4169-doubling-up-method-or-playing-casino "Hi everyone, 
  
I was thinking about one strategy which I called doubling up method but I want to share it and you to review and make...") 24 replies

[Playing the Double-Up Game?](/thread/42119-playing-the-double-up-game "It's sure a crazy full of risk system. I was just wondering if anyone ever heard of someone doing this and winning? 
  
With this system...") 40 replies

[Playing with datetime...](/thread/36065-playing-with-datetime "Hi, 
  
Setting the date, manually, in Alert 2 to todays date, why does Alert 1 return a different value than Alert 2? Even using...") 2 replies

[Playing the Breakout Trade](/thread/6189-playing-the-breakout-trade "by Abe Cofnas 
 
When markets move, particularly in Forex, they move fast. We all have witnessed breakouts and have had the occasion to...") 4 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/739272-playing-with-the-currencies-gabin-system/reply#reply)
  * Subscribe
  * [161](javascript:void\(0\);)

Attachments: Playing with the currencies: Gabin System

Tags: Playing with the currencies: Gabin System

#  [](/thread/739272-playing-with-the-currencies-gabin-system)Playing with the currencies: Gabin System 

  * 

  * [#201](/thread/post/10813238#post10813238 "Post Permalink")

  * Feb 25, 2018 7:25pm  Feb 25, 2018 7:25pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar46777_5.gif) shiva](shiva)

  * Joined Aug 2007 | Status: Doing It In Dubai | [2,457 Posts](/search?do=process&provider=Member&searchuser=46777)

> [Quoting madscalp](/thread/post/10813201#post10813201 "View Quoted Post")
> 
> Disliked
> 
> Hi all I have opened on feb 19 a small demo account ( $ 1 000 ) to test the system. You see the results below but there are some mistakes: 1 st from me : several baskets were opened with 0.1 lots...of course only 0.01 lot ...no more 2 nd from EA testing : too many baskets due at bugs So the results turn around 20 % weekly profit instead of 36 %. I set a 5 % SL and it was never reached ( of course it will be one day ) What conclusion ? lucky week ? probably... I still don't know the best way to close the trades. Mostly were closed by lock and sometimes...
> 
> Ignored

How about using a standalone basket manager like MPTM or Milanese trade manager? They can manage trades based on magic number, trade comment etc. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#202](/thread/post/10813262#post10813262 "Post Permalink")

  * Feb 25, 2018 7:45pm  Feb 25, 2018 7:45pm 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

> [Quoting shiva](/thread/post/10813238#post10813238 "View Quoted Post")
> 
> Disliked
> 
> {quote} How about using a standalone basket manager like MPTM or Milanese trade manager? They can manage trades based on magic number, trade comment etc.
> 
> Ignored

Many thanks. Milanese is a member of Steve Hopwood's forum , I presume ? Where do we can find this trade manager ? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#203](/thread/post/10813273#post10813273 "Post Permalink")

  * Feb 25, 2018 7:54pm  Feb 25, 2018 7:54pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar523703_1.gif) faryne](faryne)

  * | Joined Oct 2016  | Status: Trader | [93 Posts](/search?do=process&provider=Member&searchuser=523703)

> [Quoting madscalp](/thread/post/10813061#post10813061 "View Quoted Post")
> 
> Disliked
> 
> {quote} I think faryne can do that easily. It's just a command to not open momentarily new trades. {quote} Sure. It's why we need a news calendar ( post # 29 ) . I admit that I do not always look at minor currencies ![](https://resources.faireconomy.media/images/emojis/64/1f44e.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f641.png?v=15.1) faryne have to include it in the next version
> 
> Ignored

I already added On/Off button to stop EA (="add_new_trades" parameter) and buttons to manual open basket with.  
I also added news filter with: stop trading before/after news, and revert trading only on news.  
I will not add S/R indicator, because I can't see what to do with. The system is based on Currency, not on pair, so pairs related on same currency can be on support and resistance same time etc.  
I will not add (for now) the ghost basket idea. Because it's a lot of work (due to passing from basket profit to pairs pips on code) and we don't know if it will add any value. So I propose you to paper trading it (with 2 demo account), and if it's intersting, I will definitively work on that ![](https://resources.faireconomy.media/images/emojis/64/1f60b.png?v=15.1).  
  
Feel free to propose your others improvments. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#204](/thread/post/10813358#post10813358 "Post Permalink")

  * Feb 25, 2018 9:03pm  Feb 25, 2018 9:03pm 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

> [Quoting faryne](/thread/post/10813273#post10813273 "View Quoted Post")
> 
> Disliked
> 
> {quote} I already added On/Off button to stop EA (="add_new_trades" parameter) and buttons to manual open basket with. I also added news filter with: stop trading before/after news, and revert trading only on news. I will not add S/R indicator, because I can't see what to do with. The system is based on Currency, not on pair, so pairs related on same currency can be on support and resistance same time etc. I will not add (for now) the ghost basket idea. Because it's a lot of work (due to passing from basket profit to pairs pips on code) and we don't...
> 
> Ignored

OOOPS ...these options are in the settings and no on the dashboard with buttons ...i apologize ..i didn't seen  
faryne ...you are right...the EA is very complete and now it's up to the trader to make good use of it with his own management  
just a question : post 186 you showed a screenshot...what's the EA version with news calendar and total P/L ? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#205](/thread/post/10813361#post10813361 "Post Permalink")

  * Feb 25, 2018 9:05pm  Feb 25, 2018 9:05pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar46777_5.gif) shiva](shiva)

  * Joined Aug 2007 | Status: Doing It In Dubai | [2,457 Posts](/search?do=process&provider=Member&searchuser=46777)

> [Quoting madscalp](/thread/post/10813262#post10813262 "View Quoted Post")
> 
> Disliked
> 
> {quote} Many thanks. Milanese is a member of Steve Hopwood's forum , I presume ? Where do we can find this trade manager ?
> 
> Ignored

Yes he is from Steve's forum and here is the [link ](http://www.stevehopwoodforex.com/phpBB3/viewtopic.php?f=21&t=3482&start=580&hilit=milanese)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#206](/thread/post/10813391#post10813391 "Post Permalink")

  * Feb 25, 2018 9:22pm  Feb 25, 2018 9:22pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar523703_1.gif) faryne](faryne)

  * | Joined Oct 2016  | Status: Trader | [93 Posts](/search?do=process&provider=Member&searchuser=523703)

> [Quoting madscalp](/thread/post/10813358#post10813358 "View Quoted Post")
> 
> Disliked
> 
> {quote} OOOPS ...these options are in the settings and no on the dashboard with buttons ...i apologize ..i didn't seen faryne ...you are right...the EA is very complete and now it's up to the trader to make good use of it with his own management just a question : post 186 you showed a screenshot...what's the EA version with news calendar and total P/L ?
> 
> Ignored

This is the next version (not uploaded yet). I added lot of stuff (included news, buttons, etc.) so I need to test code in live with data and orders. Surely delivered tomorrow. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#207](/thread/post/10813599#post10813599 "Post Permalink")

  * Feb 26, 2018 12:08am  Feb 26, 2018 12:08am 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

Perfect...faryne.  
When I'm talking about improvment, I'm thinking about trading management no EA.  
About ghost basket, I agree with you . It's a lot of coding for an uncertain value.  
Another request is for Ezios no for you. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#208](/thread/post/10814781#post10814781 "Post Permalink")

  * Feb 26, 2018 3:14pm  Feb 26, 2018 3:14pm 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

> [Quoting madscalp](/thread/post/10813599#post10813599 "View Quoted Post")
> 
> Disliked
> 
> Perfect...faryne. When I'm talking about improvment, I'm thinking about trading management no EA. About ghost basket, I agree with you . It's a lot of coding for an uncertain value. Another request is for Ezios no for you.
> 
> Ignored

Madscalp I can add sound alert in the indicator but... for the other options that someone required i have not  
the idea how thei and what they do so.. if someone have some source code that include this i can to attempt...  
if not, nothing to do for me. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#209](/thread/post/10814845#post10814845 "Post Permalink")

  * Edited 4:33pm  Feb 26, 2018 3:38pm | Edited 4:33pm 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

> [Quoting Ezios](/thread/post/10814781#post10814781 "View Quoted Post")
> 
> Disliked
> 
> {quote} Madscalp I can add sound alert in the indicator but... for the other options that someone required i have not the idea how thei and what they do so.. if someone have some source code that include this i can to attempt... if not, nothing to do for me.
> 
> Ignored

Hi Ezios  
You are right. A sound alert with Shakira's voice would be wonderful ![](https://resources.faireconomy.media/images/emojis/64/1f600.png?v=15.1)  
Maybe vinvlad can explicite his request about "AlertCandle"... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#210](/thread/post/10815136#post10815136 "Post Permalink")

  * Feb 26, 2018 5:40pm  Feb 26, 2018 5:40pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar352244_2.gif) vinvlad](vinvlad)

  * Joined Oct 2013 | Status: Trader | [146 Posts](/search?do=process&provider=Member&searchuser=352244) | Online Now 

As far as I understand, this option (Alert Candle) eliminates numerous alerts when a trigger signal appears. For example, when we put the indicator on the chart with tf 1 minute, an alert appears only once after the candle is closed in 1 minute. Again - I'm not a coder, I can be wrong.  
I sent the code options to you in the PM.  
Perhaps help. Thank you.![](https://resources.faireconomy.media/images/emojis/64/1f600.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#211](/thread/post/10815185#post10815185 "Post Permalink")

  * Feb 26, 2018 5:55pm  Feb 26, 2018 5:55pm 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

> [Quoting vinvlad](/thread/post/10815136#post10815136 "View Quoted Post")
> 
> Disliked
> 
> As far as I understand, this option (Alert Candle) eliminates numerous alerts when a trigger signal appears. For example, when we put the indicator on the chart with tf 1 minute, an alert appears only once after the candle is closed in 1 minute. Again - I'm not a coder, I can be wrong. I sent the code options to you in the PM. Perhaps help. Thank you.![](https://resources.faireconomy.media/images/emojis/64/1f600.png?v=15.1)
> 
> Ignored

OK ...I see your idea....IMO M5 is a good TF...maybe M1  
If the signal is confirmed at candle close, it's valid.  
I'm using the indicator below _in M5_ to "visualize" the market ( useful for manual trading )  
You can send the code to Ezios to know if he can make that. 

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [smStrengthRange09_v2.4.ex4](/attachment/file/2691955?d=1519635497) 53 KB | 516 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#212](/thread/post/10815434#post10815434 "Post Permalink")

  * Feb 26, 2018 7:12pm  Feb 26, 2018 7:12pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar352244_2.gif) vinvlad](vinvlad)

  * Joined Oct 2013 | Status: Trader | [146 Posts](/search?do=process&provider=Member&searchuser=352244) | Online Now 

![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1) I'm testing the version 5.1 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: sm_5.png
Size: 57 KB](/attachment/image/2692042/thumbnail?d=1519639944)](/attachment/image/2692042?d=1519639944)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#213](/thread/post/10815530#post10815530 "Post Permalink")

  * Feb 26, 2018 7:35pm  Feb 26, 2018 7:35pm 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

> [Quoting vinvlad](/thread/post/10815434#post10815434 "View Quoted Post")
> 
> Disliked
> 
> ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1) I'm testing the version 5.1 {image}
> 
> Ignored

Good entry with delta 1-8 > 7 on Daily R2 and Weekly R1  
Beware ...maybe just a pullback ?  
What's the 5.1 ? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#214](/thread/post/10815639#post10815639 "Post Permalink")

  * Feb 26, 2018 7:59pm  Feb 26, 2018 7:59pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar352244_2.gif) vinvlad](vinvlad)

  * Joined Oct 2013 | Status: Trader | [146 Posts](/search?do=process&provider=Member&searchuser=352244) | Online Now 

> [Quoting madscalp](/thread/post/10815530#post10815530 "View Quoted Post")
> 
> Disliked
> 
> {quote} What's the 5.1 ?
> 
> Ignored

[SwingMans ![](https://resources.faireconomy.media/images/emojis/64/1f44b.png?v=15.1)](https://www.forexfactory.com/swingman) Masterpieces  
  

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [smStrengthRange09_v5.1.ex4](/attachment/file/2692125?d=1519642767) 57 KB | 611 downloads 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#215](/thread/post/10816122#post10816122 "Post Permalink")

  * Feb 26, 2018 10:19pm  Feb 26, 2018 10:19pm 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

I understand the concept , Vinvlad but keep in mind that if I add this option for current timeframe,  
for example 5 min , if the signal appears for example at 2:00:35 and then disappears you wll never have the mesage.  
is this what you want? i dont think that is for this system. we must to meep signals in seconds.  

> [Quoting vinvlad](/thread/post/10815136#post10815136 "View Quoted Post")
> 
> Disliked
> 
> As far as I understand, this option (Alert Candle) eliminates numerous alerts when a trigger signal appears. For example, when we put the indicator on the chart with tf 1 minute, an alert appears only once after the candle is closed in 1 minute. Again - I'm not a coder, I can be wrong. I sent the code options to you in the PM. Perhaps help. Thank you.![](https://resources.faireconomy.media/images/emojis/64/1f600.png?v=15.1)
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#216](/thread/post/10816180#post10816180 "Post Permalink")

  * Edited 10:55pm  Feb 26, 2018 10:34pm | Edited 10:55pm 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

> [Quoting Ezios](/thread/post/10816122#post10816122 "View Quoted Post")
> 
> Disliked
> 
> I understand the concept , Vinvlad but keep in mind that if I add this option for current timeframe, for example 5 min , if the signal appears for example at 2:00:35 and then disappears you wll never have the mesage. is this what you want? i dont think that is for this system. we must to meep signals in seconds. {quote}
> 
> Ignored

I think to understand but I don't know if it can be coded.  
Let's suppose a delta set at 4.4. The signal is valid only if _at the candle end_ the delta is yet 4.4.  
It would be necessary to use the indicator below which would display the valid order at the end of the candle ...for instance M1.  
True improvement ???? A lot of coding work for little added value...  
  
Correct session for me and you ?  
Beware of red news nextly...I'm out of the market 

Attached File(s)

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [CM_Strength_TF V1.0.mq4](/attachment/file/2692395?d=1519652810) 20 KB | 578 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#217](/thread/post/10816311#post10816311 "Post Permalink")

  * Feb 26, 2018 10:58pm  Feb 26, 2018 10:58pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar523703_1.gif) faryne](faryne)

  * | Joined Oct 2016  | Status: Trader | [93 Posts](/search?do=process&provider=Member&searchuser=523703)

> [Quoting madscalp](/thread/post/10816180#post10816180 "View Quoted Post")
> 
> Disliked
> 
> {quote} I think to understand but I don't know if it can be coded. Let's suppose a delta set at 4.4. The signal is valid only if at the candle end the delta is yet 4.4. It would be necessary to use the indicator below which would display the valid order at the end of the candle ...for instance M1. True improvement ???? A lot of coding work for little added value... Correct session for me and you ? {file}
> 
> Ignored

Actually it's nothing to code, but IMO i don't see any interest with this strategy. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#218](/thread/post/10816390#post10816390 "Post Permalink")

  * Edited 11:40pm  Feb 26, 2018 11:04pm | Edited 11:40pm 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

> [Quoting faryne](/thread/post/10816311#post10816311 "View Quoted Post")
> 
> Disliked
> 
> {quote} Actually it's nothing to code, but IMO i don't see any interest with this strategy.
> 
> Ignored

I agree ...our tools are excellent....after, it is the management which makes money...or no ![](https://resources.faireconomy.media/images/emojis/64/1f61c.png?v=15.1)  
  
  
Wooooh Sell GBP basket ![](https://resources.faireconomy.media/images/emojis/64/1f4aa.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1) and Buy USD basket too. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#219](/thread/post/10816783#post10816783 "Post Permalink")

  * Feb 26, 2018 11:59pm  Feb 26, 2018 11:59pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar352244_2.gif) vinvlad](vinvlad)

  * Joined Oct 2013 | Status: Trader | [146 Posts](/search?do=process&provider=Member&searchuser=352244) | Online Now 

> [Quoting Ezios](/thread/post/10816122#post10816122 "View Quoted Post")
> 
> Disliked
> 
> I understand the concept , Vinvlad but keep in mind that if I add this option for current timeframe, for example 5 min , if the signal appears for example at 2:00:35 and then disappears you wll never have the mesage. is this what you want? i dont think that is for this system. we must to meep signals in seconds. {quote}
> 
> Ignored

You are right![](https://resources.faireconomy.media/images/emojis/64/1f3af.png?v=15.1) \- a signal for 1 minute. And then it does not repeat. This is if you can not just limit it with one alert. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#220](/thread/post/10816936#post10816936 "Post Permalink")

  * Feb 27, 2018 12:16am  Feb 27, 2018 12:16am 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

the indicator is used to trade manual so... the decision is of the trader. the indicator displays every  
signals whe3n they appear... then the trade decides what to do.. it is useless for all of use to concentrata our attention in the  
thing of discretionary trading. we have to improve the automatic system. the rest is alreay done.  

> [Quoting vinvlad](/thread/post/10816783#post10816783 "View Quoted Post")
> 
> Disliked
> 
> {quote} You are right![](https://resources.faireconomy.media/images/emojis/64/1f3af.png?v=15.1) \- a signal for 1 minute. And then it does not repeat. This is if you can not just limit it with one alert.
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Playing with the currencies: Gabin System
  *   * [ **Reply to Thread** ](/thread/739272-playing-with-the-currencies-gabin-system/reply#reply)

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

[Doubling up method or playing casino](/thread/4169-doubling-up-method-or-playing-casino "Hi everyone, 
  
I was thinking about one strategy which I called doubling up method but I want to share it and you to review and make...") 24 replies

[Playing the Double-Up Game?](/thread/42119-playing-the-double-up-game "It's sure a crazy full of risk system. I was just wondering if anyone ever heard of someone doing this and winning? 
  
With this system...") 40 replies

[Playing with datetime...](/thread/36065-playing-with-datetime "Hi, 
  
Setting the date, manually, in Alert 2 to todays date, why does Alert 1 return a different value than Alert 2? Even using...") 2 replies

[Playing the Breakout Trade](/thread/6189-playing-the-breakout-trade "by Abe Cofnas 
 
When markets move, particularly in Forex, they move fast. We all have witnessed breakouts and have had the occasion to...") 4 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/739272-playing-with-the-currencies-gabin-system/reply#reply)
  * Subscribe
  * [161](javascript:void\(0\);)

Attachments: Playing with the currencies: Gabin System

Tags: Playing with the currencies: Gabin System

#  [](/thread/739272-playing-with-the-currencies-gabin-system)Playing with the currencies: Gabin System 

  * 

  * [#221](/thread/post/10817740#post10817740 "Post Permalink")

  * Feb 27, 2018 2:44am  Feb 27, 2018 2:44am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar620434_4.gif) syndicat](syndicat)

  * | Additional Username  | Joined Oct 2017 | [432 Posts](/search?do=process&provider=Member&searchuser=620434)

Hey, guys! How are the tests of expert advisors? Somebody trades in <https://www.lmax.com?>

"Money makes Money"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#222](/thread/post/10818252#post10818252 "Post Permalink")

  * Feb 27, 2018 6:20am  Feb 27, 2018 6:20am 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

> [Quoting syndicat](/thread/post/10817740#post10817740 "View Quoted Post")
> 
> Disliked
> 
> Hey, guys! How are the tests of expert advisors? Somebody trades in <https://www.lmax.com?>
> 
> Ignored

i am continuing the test my demo account... for now its in draw down.... no this broker. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#223](/thread/post/10818280#post10818280 "Post Permalink")

  * Edited 6:48am  Feb 27, 2018 6:36am | Edited 6:48am 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

> [Quoting Ezios](/thread/post/10818252#post10818252 "View Quoted Post")
> 
> Disliked
> 
> {quote} i am continuing the test my demo account... for now its in draw down.... no this broker.
> 
> Ignored

How many your DD have you seen today ?  
Curious because it was a good day.... my initial account $ 1 000 from feb 19  
so daily 7 % 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: 1.jpg
Size: 124 KB](/attachment/image/2693135/thumbnail?d=1519681598)](/attachment/image/2693135?d=1519681598)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#224](/thread/post/10818731#post10818731 "Post Permalink")

  * Feb 27, 2018 12:34pm  Feb 27, 2018 12:34pm 

  * [ cpips](cpips)

  * | Joined Aug 2016  | Status: Trader | [90 Posts](/search?do=process&provider=Member&searchuser=485383)

Attached Image (click to enlarge)

[![Click to Enlarge

Name: report 21 to 26 feb.png
Size: 27 KB](/attachment/image/2693366/thumbnail?d=1519702456)](/attachment/image/2693366?d=1519702456)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#225](/thread/post/10818981#post10818981 "Post Permalink")

  * Feb 27, 2018 2:48pm  Feb 27, 2018 2:48pm 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

Hi cpips ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)  
I have about same results...  
We don't have to leave turn on the EA 24/24 and close the good trades.  
  
manual or EA ? 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#226](/thread/post/10819026#post10819026 "Post Permalink")

  * Feb 27, 2018 3:05pm  Feb 27, 2018 3:05pm 

  * [ majamivice](majamivice)

  * | Joined Jun 2017  | Status: Trader | [551 Posts](/search?do=process&provider=Member&searchuser=591683)

Hi all. My EA don't open trades in 2 days now. What can be wrong?  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Screenshot_20180227-065224.jpg
Size: 1.1 MB](/attachment/image/2693568/thumbnail?d=1519711510)](/attachment/image/2693568?d=1519711510)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#227](/thread/post/10819089#post10819089 "Post Permalink")

  * Feb 27, 2018 3:26pm  Feb 27, 2018 3:26pm 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

Maybe restriction by faryne ?  
If you appreciate the Gabin Sys. , you can poll in post #1 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#228](/thread/post/10819111#post10819111 "Post Permalink")

  * Feb 27, 2018 3:38pm  Feb 27, 2018 3:38pm 

  * [ majamivice](majamivice)

  * | Joined Jun 2017  | Status: Trader | [551 Posts](/search?do=process&provider=Member&searchuser=591683)

> [Quoting madscalp](/thread/post/10819089#post10819089 "View Quoted Post")
> 
> Disliked
> 
> Maybe restriction by faryne ? If you appreciate the Gabin Sys. , you can poll in post #1
> 
> Ignored

What restriction? It's a demo account. I didn't try yet the system. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#229](/thread/post/10819135#post10819135 "Post Permalink")

  * Feb 27, 2018 3:47pm  Feb 27, 2018 3:47pm 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

> [Quoting majamivice](/thread/post/10819111#post10819111 "View Quoted Post")
> 
> Disliked
> 
> {quote} What restriction? It's a demo account. I didn't try yet the system.
> 
> Ignored

I've had just the idea of the system...I'm not the coder of the EA.  
IMO the creator faryne will reply you about this issue ... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#230](/thread/post/10819211#post10819211 "Post Permalink")

  * Feb 27, 2018 4:30pm  Feb 27, 2018 4:30pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar523703_1.gif) faryne](faryne)

  * | Joined Oct 2016  | Status: Trader | [93 Posts](/search?do=process&provider=Member&searchuser=523703)

> [Quoting majamivice](/thread/post/10819026#post10819026 "View Quoted Post")
> 
> Disliked
> 
> Hi all. My EA don't open trades in 2 days now. What can be wrong? {image}
> 
> Ignored

Seeing "too late", it is a problem "rearming" the ea after opening of the day.  
You can simply reinit the EA, and you should see "H ok" instead of "too late". Maybe an issue with this version. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#231](/thread/post/10819279#post10819279 "Post Permalink")

  * Feb 27, 2018 4:57pm  Feb 27, 2018 4:57pm 

  * [ majamivice](majamivice)

  * | Joined Jun 2017  | Status: Trader | [551 Posts](/search?do=process&provider=Member&searchuser=591683)

> [Quoting faryne](/thread/post/10819211#post10819211 "View Quoted Post")
> 
> Disliked
> 
> {quote} Seeing "too late", it is a problem "rearming" the ea after opening of the day. You can simply reinit the EA, and you should see "H ok" instead of "too late". Maybe an issue with this version.
> 
> Ignored

Yes when I reinit the EA it's OK, but we'll see if it stays so. Btw, thanks for EA's to both coders and the brain of this system Madscalp. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#232](/thread/post/10819522#post10819522 "Post Permalink")

  * Feb 27, 2018 5:55pm  Feb 27, 2018 5:55pm 

  * [ cpips](cpips)

  * | Joined Aug 2016  | Status: Trader | [90 Posts](/search?do=process&provider=Member&searchuser=485383)

> [Quoting madscalp](/thread/post/10818981#post10818981 "View Quoted Post")
> 
> Disliked
> 
> Hi cpips ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1) I have about same results... We don't have to leave turn on the EA 24/24 and close the good trades. manual or EA ?
> 
> Ignored

Hi,  
Thanks to madscalp,Ezios,faryne...  
  
  
cpips.

Attached Image (click to enlarge)

[![Click to Enlarge

Name: trade from LO to LC.png
Size: 80 KB](/attachment/image/2693808/thumbnail?d=1519721721)](/attachment/image/2693808?d=1519721721)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#233](/thread/post/10819539#post10819539 "Post Permalink")

  * Feb 27, 2018 6:01pm  Feb 27, 2018 6:01pm 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

> [Quoting cpips](/thread/post/10819522#post10819522 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi, Thanks to madscalp,Ezios,faryne... cpips. {image}
> 
> Ignored

Good management with London session.  
Often good opportunities around London open...this morning nothing...no matter. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#234](/thread/post/10819546#post10819546 "Post Permalink")

  * Edited 6:15pm  Feb 27, 2018 6:05pm | Edited 6:15pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar526867_15.gif) AndrewBa-](andrewba-)

  * | Commercial User  | Joined Nov 2016 | [422 Posts](/search?do=process&provider=Member&searchuser=526867)

Hi guys,  
I read the threat and read, any maybe I get it wrong, but madscalp said this is not yet a well demo-tested version, and no one should trade it live. Well, the results start to look better...  
Is anybody trading the EA on a (small) live account?!  
Or is it a version that only may be applied to demo account (as I read somewhere).  
Am just wondering, ... 

Check page 1 for all infos...

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#235](/thread/post/10819568#post10819568 "Post Permalink")

  * Feb 27, 2018 6:14pm  Feb 27, 2018 6:14pm 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

> [Quoting AndrewBa-](/thread/post/10819546#post10819546 "View Quoted Post")
> 
> Disliked
> 
> Hi guys, I read the threat and read, any maybe I get it wrong, but madscalp said this is not yet a well demo-tested version, and no one should trade it live. Well, the results start to look better... Is anybody trading the EA on a (small) live account?!
> 
> Ignored

Gabin System is too new to be used in live...we need more feedback.  
Our coders make an awesome work but they don't want that their tools are used in live...not yet...maybe later...I don't know because I'm not the owner  
so if you want to go in live, you can spend a little time to begin to trade slowly in manual with the tools post # 1  
see too post # 167 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#236](/thread/post/10819612#post10819612 "Post Permalink")

  * Edited 9:51pm  Feb 27, 2018 6:27pm | Edited 9:51pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar523703_1.gif) faryne](faryne)

  * | Joined Oct 2016  | Status: Trader | [93 Posts](/search?do=process&provider=Member&searchuser=523703)

Hello all,  
  
Here is the latest version of Medusa including:  
-News management (stop trading before x min, auto close positive basket before x min, restart trading after x min, reverse trading on news, etc)  
-More buttons for manual trading (open/close/on off by pair and total)  
-Improvments on verbose  
-Many bugs fixation (like the rearming situation)  
  
Need to be test on **demo.**  
  
I'm also working on the "ghost" version. Code is ok, I'm currently testing it.  
  
Edit: "Stop for news" verbose was not updated. 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: Screenshot1.png
Size: 160 KB](/attachment/image/2693848/thumbnail?d=1519723484)](/attachment/image/2693848?d=1519723484)   
[![Click to Enlarge

Name: Screenshot2.png
Size: 162 KB](/attachment/image/2693849/thumbnail?d=1519723518)](/attachment/image/2693849?d=1519723518)   

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [Medusa.ex4](/attachment/file/2694176?d=1519735850) 154 KB | 526 downloads 

[0 ](javascript:void\(0\);) [5 ](javascript:void\(0\);)

  * [#237](/thread/post/10819623#post10819623 "Post Permalink")

  * Edited 7:12pm  Feb 27, 2018 6:37pm | Edited 7:12pm 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

Wonderful. It's really a masterpiece.  
Just a clarification about "trending on news" OK it's a reverse function but what's exactly it happens ?  
The EA takes an opposite basket with a signal or no ? or just manual ? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#238](/thread/post/10819626#post10819626 "Post Permalink")

  * Feb 27, 2018 6:37pm  Feb 27, 2018 6:37pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar573585_1.gif) forexfans](forexfans)

  * | Joined Apr 2017  | Status: Trader | [64 Posts](/search?do=process&provider=Member&searchuser=573585)

Oh my god, this thread gonna hot!  
thank you guys very much!!! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#239](/thread/post/10819687#post10819687 "Post Permalink")

  * Feb 27, 2018 6:52pm  Feb 27, 2018 6:52pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar116307_2.gif) rosalieone](rosalieone)

  * Joined Sep 2009 | Status: Trader | [540 Posts](/search?do=process&provider=Member&searchuser=116307)

Wow well done. I love the count down on the news 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#240](/thread/post/10819794#post10819794 "Post Permalink")

  * Feb 27, 2018 7:15pm  Feb 27, 2018 7:15pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar620434_4.gif) syndicat](syndicat)

  * | Additional Username  | Joined Oct 2017 | [432 Posts](/search?do=process&provider=Member&searchuser=620434)

> [Quoting faryne](/thread/post/10819612#post10819612 "View Quoted Post")
> 
> Disliked
> 
> Hello all, Here is the latest version of Medusa including: -News management (stop trading before x min, auto close positive basket before x min, restart trading after x min, reverse trading on news, etc) -More buttons for manual trading (open/close/on off by pair and total) -Improvments on verbose -Many bugs fixation (like the rearming situation) Need to be test on demo. I'm also working on the "ghost" version. Code is ok, I'm currently testing it. {image} {image} {file}
> 
> Ignored

  
  
Excellent work!!!![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)

"Money makes Money"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Playing with the currencies: Gabin System
  *   * [ **Reply to Thread** ](/thread/739272-playing-with-the-currencies-gabin-system/reply#reply)

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

[Doubling up method or playing casino](/thread/4169-doubling-up-method-or-playing-casino "Hi everyone, 
  
I was thinking about one strategy which I called doubling up method but I want to share it and you to review and make...") 24 replies

[Playing the Double-Up Game?](/thread/42119-playing-the-double-up-game "It's sure a crazy full of risk system. I was just wondering if anyone ever heard of someone doing this and winning? 
  
With this system...") 40 replies

[Playing with datetime...](/thread/36065-playing-with-datetime "Hi, 
  
Setting the date, manually, in Alert 2 to todays date, why does Alert 1 return a different value than Alert 2? Even using...") 2 replies

[Playing the Breakout Trade](/thread/6189-playing-the-breakout-trade "by Abe Cofnas 
 
When markets move, particularly in Forex, they move fast. We all have witnessed breakouts and have had the occasion to...") 4 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/739272-playing-with-the-currencies-gabin-system/reply#reply)
  * Subscribe
  * [161](javascript:void\(0\);)

Attachments: Playing with the currencies: Gabin System

Tags: Playing with the currencies: Gabin System

#  [](/thread/739272-playing-with-the-currencies-gabin-system)Playing with the currencies: Gabin System 

  * 

  * [#241](/thread/post/10820223#post10820223 "Post Permalink")

  * Feb 27, 2018 9:15pm  Feb 27, 2018 9:15pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar621485_5.gif) northwind](northwind)

  * Joined Oct 2017 | Status: Trader | [362 Posts](/search?do=process&provider=Member&searchuser=621485)

Madscalp, Faryne, & Ezios,  
Fantastic idea and excellent coding skills. Thank you for starting this tread and sharing so generously.  
Read from the beginning and ready to take it for a test drive. Just download Medusa 5.1 for testing on demo acct.  
Some questions:  
1\. What are the settings for "Strategy"? Default is 0 - what are the other possible options?  
2\. What switches EA from manual to auto trading?  
3\. Which individual currency value is the key impulse value (Strength, Delta or Ratio) to trigger the EA? Currently, USD is 6.6, 2.37, 1.56.  
Thanks a million,  
John 

Perfidious Pips

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#242](/thread/post/10820294#post10820294 "Post Permalink")

  * Feb 27, 2018 9:39pm  Feb 27, 2018 9:39pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar523703_1.gif) faryne](faryne)

  * | Joined Oct 2016  | Status: Trader | [93 Posts](/search?do=process&provider=Member&searchuser=523703)

> [Quoting northwind](/thread/post/10820223#post10820223 "View Quoted Post")
> 
> Disliked
> 
> Madscalp, Faryne, & Ezios, Fantastic idea and excellent coding skills. Thank you for starting this tread and sharing so generously. Read from the beginning and ready to take it for a test drive. Just download Medusa 5.1 for testing on demo acct. Some questions: 1. What are the settings for "Strategy"? Default is 0 - what are the other possible options? 2. What switches EA from manual to auto trading? 3. Which individual currency value is the key impulse value (Strength, Delta or Ratio) to trigger the EA? Currently, USD is 6.6, 2.37, 1.56. Thanks...
> 
> Ignored

1\. Strategy is a parameter for hard-coding strategy (like reversal only between some steps, etc.). Currently, only once is coded but I've not tested it yet. So you can let this parameter to 0.  
2\. 1st solution: "OnOff" button. 2nd: "add_new_trades"=0/1. 3rd: "OF" buttons (by pair). 4th: AutoTrading on MT4. Be aware that 1/2/3 keep the TP/SL management but Autotrading one don't.  
3\. EA only check the Delta value. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#243](/thread/post/10820297#post10820297 "Post Permalink")

  * Feb 27, 2018 9:42pm  Feb 27, 2018 9:42pm 

  * [ ian52](ian52)

  * | Joined Jul 2009  | Status: Trader | [31 Posts](/search?do=process&provider=Member&searchuser=109429)

Hi Everyone, what your current USD delta reading?  
  
Ezios_indy.ex4 and pwtcea reflect two different value, which 1 i should refer to?  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Capture.PNG
Size: 130 KB](/attachment/image/2694168/thumbnail?d=1519735335)](/attachment/image/2694168?d=1519735335)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#244](/thread/post/10820361#post10820361 "Post Permalink")

  * Feb 27, 2018 10:01pm  Feb 27, 2018 10:01pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar71675_5.gif) Alberto_Jazz](alberto_jazz)

  * Joined Jun 2008 | Status: Trader | [593 Posts](/search?do=process&provider=Member&searchuser=71675)

> [Quoting faryne](/thread/post/10819612#post10819612 "View Quoted Post")
> 
> Disliked
> 
> I'm also working on the "ghost" version. Code is ok, I'm currently testing it.
> 
> Ignored

Thank you very much! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#245](/thread/post/10820369#post10820369 "Post Permalink")

  * Feb 27, 2018 10:03pm  Feb 27, 2018 10:03pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar621485_5.gif) northwind](northwind)

  * Joined Oct 2017 | Status: Trader | [362 Posts](/search?do=process&provider=Member&searchuser=621485)

> [Quoting faryne](/thread/post/10820294#post10820294 "View Quoted Post")
> 
> Disliked
> 
> {quote} 1. Strategy is a parameter for hard-coding strategy (like reversal only between some steps, etc.). Currently, only once is coded but I've not tested it yet. So you can let this parameter to 0. 2. 1st solution: "OnOff" button. 2nd: "add_new_trades"=0/1. 3rd: "OF" buttons (by pair). 4th: AutoTrading on MT4. Be aware that 1/2/3 keep the TP/SL management but Autotrading one don't. 3. EA only check the Delta value.
> 
> Ignored

Thank you Faryne for your quick reply.  
MT4 has "Auto Trading" enabled and Medusa Common Tab has "Allow Live Trading".  
To confirm, if dashboard shows "Waiting signal" flashing then Medusa EA is in control waiting for Delta value trigger.  
Thanks again for your work.  
John 

Perfidious Pips

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#246](/thread/post/10820381#post10820381 "Post Permalink")

  * Feb 27, 2018 10:08pm  Feb 27, 2018 10:08pm 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

the indicator you have to follow if you manual trade.  
the ea opens automatic trades upon the conditions.  
about deltaup it can vary in seconds as can vary the currency in top of the list or in botton...  
so it depends the second. the code from the indicator is the same in the ea for the calculation.  

> [Quoting ian52](/thread/post/10820297#post10820297 "View Quoted Post")
> 
> Disliked
> 
> Hi Everyone, what your current USD delta reading? Ezios_indy.ex4 and pwtcea reflect two different value, which 1 i should refer to? {image}
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#247](/thread/post/10820418#post10820418 "Post Permalink")

  * Feb 27, 2018 10:15pm  Feb 27, 2018 10:15pm 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

yes... it was little draw down... after this my message i got take profit. for now this ea never stop loss  
with default setting. its good thing... very good....  

> [Quoting madscalp](/thread/post/10818280#post10818280 "View Quoted Post")
> 
> Disliked
> 
> {quote} How many your DD have you seen today ? Curious because it was a good day.... my initial account $ 1 000 from feb 19 so daily 7 % {image}
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#248](/thread/post/10820549#post10820549 "Post Permalink")

  * Feb 27, 2018 10:39pm  Feb 27, 2018 10:39pm 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

LOL ...testing news I have taken 2 USD baskets but I have forgotten BE lvl at 5  
so only $ 5 profit...it's working  
faryne...please read again post # 237 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#249](/thread/post/10820639#post10820639 "Post Permalink")

  * Feb 27, 2018 10:53pm  Feb 27, 2018 10:53pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar523703_1.gif) faryne](faryne)

  * | Joined Oct 2016  | Status: Trader | [93 Posts](/search?do=process&provider=Member&searchuser=523703)

> [Quoting madscalp](/thread/post/10820549#post10820549 "View Quoted Post")
> 
> Disliked
> 
> LOL ...testing news I have taken 2 USD baskets but I have forgotten BE lvl at 5 so only $ 5 profit...it's working faryne...please read again post # 237
> 
> Ignored

Oh, I didn't see your question.  
reverse_news change the direction to revert trades on news (if trade_news is 1). But I was testing on USD it might be a bug the basket was shorting. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#250](/thread/post/10820715#post10820715 "Post Permalink")

  * Feb 27, 2018 11:03pm  Feb 27, 2018 11:03pm 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

> [Quoting faryne](/thread/post/10820639#post10820639 "View Quoted Post")
> 
> Disliked
> 
> {quote} Oh, I didn't see your question. reverse_news change the direction to revert trades on news (if trade_news is 1). But I was testing on USD it might be a bug the basket was shorting.
> 
> Ignored

Oh no...no mistake  
I have set Trading news=true and Trending on news=false...so the EA have taken a correct USD sell.  
My question is : when Trending on news=true, is the EA taking an opposite trade _with the same conditions of delta_ ? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#251](/thread/post/10820746#post10820746 "Post Permalink")

  * Feb 27, 2018 11:08pm  Feb 27, 2018 11:08pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar523703_1.gif) faryne](faryne)

  * | Joined Oct 2016  | Status: Trader | [93 Posts](/search?do=process&provider=Member&searchuser=523703)

> [Quoting madscalp](/thread/post/10820715#post10820715 "View Quoted Post")
> 
> Disliked
> 
> {quote} Oh no...no mistake I have set Trading news=true and Trending on news=false...so the EA have taken a correct USD sell. My question is : when Trending on news=true, is the EA taking an opposite trade with the same conditions of delta ?
> 
> Ignored

Working to improve news management, but yeah if no revert it is ok.  
  
if delta>step1 and trade_news=1 and reverse_news=0 it will SELL  
if delta>step1 and trade_news=1 and reverse_news=1 it will BUY  
no other condition is verified for news 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#252](/thread/post/10820792#post10820792 "Post Permalink")

  * Feb 27, 2018 11:15pm  Feb 27, 2018 11:15pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar573585_1.gif) forexfans](forexfans)

  * | Joined Apr 2017  | Status: Trader | [64 Posts](/search?do=process&provider=Member&searchuser=573585)

> [Quoting Ezios](/thread/post/10820418#post10820418 "View Quoted Post")
> 
> Disliked
> 
> yes... it was little draw down... after this my message i got take profit. for now this ea never stop loss with default setting. its good thing... very good.... {quote}
> 
> Ignored

Hi Ezios, the EA open 7 trades and close automatic, should I reload the EA or the EA will keep working?  
I am using the EA on POST #125  
Thanks, all trade profit! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#253](/thread/post/10820829#post10820829 "Post Permalink")

  * Feb 27, 2018 11:19pm  Feb 27, 2018 11:19pm 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

> [Quoting faryne](/thread/post/10820746#post10820746 "View Quoted Post")
> 
> Disliked
> 
> {quote} Working to improve news management, but yeah if no revert it is ok. if delta>step1 and trade_news=1 and reverse_news=0 it will SELL if delta>step1 and trade_news=1 and reverse_news=1 it will BUY no other condition is verified for news
> 
> Ignored

OK it's very clear  
but traders, be sure to use this option with caution because you can take a ugly DD  
the currency don't stay a long time with a delta > 5.2 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#254](/thread/post/10820893#post10820893 "Post Permalink")

  * Feb 27, 2018 11:31pm  Feb 27, 2018 11:31pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar523703_1.gif) faryne](faryne)

  * | Joined Oct 2016  | Status: Trader | [93 Posts](/search?do=process&provider=Member&searchuser=523703)

> [Quoting madscalp](/thread/post/10820829#post10820829 "View Quoted Post")
> 
> Disliked
> 
> {quote} OK it's very clear but traders, be sure to use this option with caution because you can take a ugly DD the currency don't stay a long time with a delta > 5.2
> 
> Ignored

This is why trailing stop is VERY important. On news, if you reach 5.2, you must be in profit (with 2 other step) and had locked it with trailing stop. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#255](/thread/post/10820909#post10820909 "Post Permalink")

  * Feb 27, 2018 11:34pm  Feb 27, 2018 11:34pm 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

> [Quoting faryne](/thread/post/10820893#post10820893 "View Quoted Post")
> 
> Disliked
> 
> {quote} This is why trailing stop is VERY important. On news, if you reach 5.2, you must be in profit (with 2 other step) and had locked it with trailing stop.
> 
> Ignored

You are right. Fellows, check cautionly the settings before trading. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#256](/thread/post/10820920#post10820920 "Post Permalink")

  * Feb 27, 2018 11:36pm  Feb 27, 2018 11:36pm 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

the last version that i did it continues to trade until the stop loss. then it wil auto remove itself from Platform and you will have to restart.  

> [Quoting forexfans](/thread/post/10820792#post10820792 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi Ezios, the EA open 7 trades and close automatic, should I reload the EA or the EA will keep working? I am using the EA on POST #125 Thanks, all trade profit!
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#257](/thread/post/10821046#post10821046 "Post Permalink")

  * Feb 27, 2018 11:58pm  Feb 27, 2018 11:58pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar573585_1.gif) forexfans](forexfans)

  * | Joined Apr 2017  | Status: Trader | [64 Posts](/search?do=process&provider=Member&searchuser=573585)

> [Quoting Ezios](/thread/post/10820920#post10820920 "View Quoted Post")
> 
> Disliked
> 
> the last version that i did it continues to trade until the stop loss. then it wil auto remove itself from Platform and you will have to restart. {quote}
> 
> Ignored

Got it, thank you so much! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#258](/thread/post/10821181#post10821181 "Post Permalink")

  * Feb 28, 2018 12:17am  Feb 28, 2018 12:17am 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

Hmmm with Trending news=true and Trending on news=true....I have had a USD sell instead of a buy  
please check this last option and maybe renamed "Opposite option" to avoid the confusion 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#259](/thread/post/10821226#post10821226 "Post Permalink")

  * Feb 28, 2018 12:26am  Feb 28, 2018 12:26am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar523703_1.gif) faryne](faryne)

  * | Joined Oct 2016  | Status: Trader | [93 Posts](/search?do=process&provider=Member&searchuser=523703)

> [Quoting madscalp](/thread/post/10821181#post10821181 "View Quoted Post")
> 
> Disliked
> 
> Hmmm with Trending news=true and Trending on news=true....I have had a USD sell instead of a buy please check this last option and maybe renamed "Opposite option" to avoid the confusion
> 
> Ignored

Well trending is not an appropriate word. Will change.  
I'll remove hurst (don't find any edge with) and add "Cost of trading" value which is the cost for opening a basket (basically spread+commission) to monitor it. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#260](/thread/post/10822356#post10822356 "Post Permalink")

  * Feb 28, 2018 4:25am  Feb 28, 2018 4:25am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar621485_5.gif) northwind](northwind)

  * Joined Oct 2017 | Status: Trader | [362 Posts](/search?do=process&provider=Member&searchuser=621485)

Tried Medusa this morning. It opened 2 USD baskets on positive Delta and closed with nice profit. It also opened 1 GBP basket on negative Delta in the wrong direction. All went to SL.  
Does Medusa correctly open both positive Delta and negative Delta baskets at the same time?  
Or, does only open in one direction?  
  
Thanks for the terrific EA.  
John 

Perfidious Pips

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Playing with the currencies: Gabin System
  *   * [ **Reply to Thread** ](/thread/739272-playing-with-the-currencies-gabin-system/reply#reply)

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

[Doubling up method or playing casino](/thread/4169-doubling-up-method-or-playing-casino "Hi everyone, 
  
I was thinking about one strategy which I called doubling up method but I want to share it and you to review and make...") 24 replies

[Playing the Double-Up Game?](/thread/42119-playing-the-double-up-game "It's sure a crazy full of risk system. I was just wondering if anyone ever heard of someone doing this and winning? 
  
With this system...") 40 replies

[Playing with datetime...](/thread/36065-playing-with-datetime "Hi, 
  
Setting the date, manually, in Alert 2 to todays date, why does Alert 1 return a different value than Alert 2? Even using...") 2 replies

[Playing the Breakout Trade](/thread/6189-playing-the-breakout-trade "by Abe Cofnas 
 
When markets move, particularly in Forex, they move fast. We all have witnessed breakouts and have had the occasion to...") 4 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/739272-playing-with-the-currencies-gabin-system/reply#reply)
  * Subscribe
  * [161](javascript:void\(0\);)

Attachments: Playing with the currencies: Gabin System

Tags: Playing with the currencies: Gabin System

#  [](/thread/739272-playing-with-the-currencies-gabin-system)Playing with the currencies: Gabin System 

  * 

  * [#261](/thread/post/10822363#post10822363 "Post Permalink")

  * Feb 28, 2018 4:27am  Feb 28, 2018 4:27am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar621485_5.gif) northwind](northwind)

  * Joined Oct 2017 | Status: Trader | [362 Posts](/search?do=process&provider=Member&searchuser=621485)

I'm away form my PC so I'll have to post screen shots of EA settings and trade history this evening.  
Thanks. 

Perfidious Pips

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#262](/thread/post/10823463#post10823463 "Post Permalink")

  * Edited 3:48pm  Feb 28, 2018 3:37pm | Edited 3:48pm 

  * [ madscalp](madscalp)

  * Joined Jan 2008 | Status: French Trader | [895 Posts](/search?do=process&provider=Member&searchuser=57934)

Hi all  
Yesyerday I've wanted to try the last version of medusa for testing the news.  
For the 1 st, I've set Trending on news= false and for the second, Trending of news=true.  
Of course it was USD the queen currency but in both cases I have had _a sell USD_.  
The results have been bad with a loss of 1.5 % for the day.  
So my conclusion don't change about news: we have to avoid them...there is an option in the EA for that.  
If you want to play the news, there are others strategies or you can throw a coin ...50/50.  
There are others signals in a session out of news.  
I remind that GS don't have to be used 24/24 but by session...if at the end of the session you observe a loss you cut your position. 

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#263](/thread/post/10823534#post10823534 "Post Permalink")

  * Feb 28, 2018 4:22pm  Feb 28, 2018 4:22pm 

  * [ cpips](cpips)

  * | Joined Aug 2016  | Status: Trader | [90 Posts](/search?do=process&provider=Member&searchuser=485383)

Attached Image (click to enlarge)

[![Click to Enlarge

Name: erro send.png
Size: 83 KB](/attachment/image/2695423/thumbnail?d=1519802512)](/attachment/image/2695423?d=1519802512)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#264](/thread/post/10823745#post10823745 "Post Permalink")

  * Feb 28, 2018 5:41pm  Feb 28, 2018 5:41pm 

  * [ majamivice](majamivice)

  * | Joined Jun 2017  | Status: Trader | [551 Posts](/search?do=process&provider=Member&searchuser=591683)

> [Quoting madscalp](/thread/post/10823463#post10823463 "View Quoted Post")
> 
> Disliked
> 
> Hi all Yesyerday I've wanted to try the last version of medusa for testing the news. For the 1 st, I've set Trending on news= false and for the second, Trending of news=true. Of course it was USD the queen currency but in both cases I have had a sell USD. The results have been bad with a loss of 1.5 % for the day. So my conclusion don't change about news: we have to avoid them...there is an option in the EA for that. If you want to play the news, there are others strategies or you can throw a coin ...50/50. There are others signals in a session...
> 
> Ignored

Perhaps our coders can code "trade by session 1,2,3" settings. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#265](/thread/post/10823929#post10823929 "Post Permalink")

  * Feb 28, 2018 6:30pm  Feb 28, 2018 6:30pm 

  * [ flashlj2008](flashlj2008)

  * | Joined Jul 2016  | Status: Trader | [32 Posts](/search?do=process&provider=Member&searchuser=474892)

Between the opening and closing of a few seconds.please help? 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: QQå›¾ç‰‡20180228172737.png
Size: 25 KB](/attachment/image/2695608/thumbnail?d=1519810190)](/attachment/image/2695608?d=1519810190)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#266](/thread/post/10823997#post10823997 "Post Permalink")

  * Feb 28, 2018 6:49pm  Feb 28, 2018 6:49pm 

  * [ forexbandit7](forexbandit7)

  * Joined Aug 2015 | Status: All praise to the lord | [346 Posts](/search?do=process&provider=Member&searchuser=425105)

nice indi, any one trading this on manual?, i prefer manual. it would be a great help if there is a alert .  
  
Thanks 

Early bird gets the worm

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#267](/thread/post/10824062#post10824062 "Post Permalink")

  * Feb 28, 2018 7:05pm  Feb 28, 2018 7:05pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar556193_1.gif) Fatso](fatso)

  * | Joined Feb 2017  | Status: Trader | [111 Posts](/search?do=process&provider=Member&searchuser=556193)

> [Quoting flashlj2008](/thread/post/10823929#post10823929 "View Quoted Post")
> 
> Disliked
> 
> Between the opening and closing of a few seconds.please help? {image}
> 
> Ignored

I suspect your SL is -$100 on the EA? If so then it is too small compared to the deal size you are using 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#268](/thread/post/10824482#post10824482 "Post Permalink")

  * Feb 28, 2018 9:03pm  Feb 28, 2018 9:03pm 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

if you want to use 1 lot for this system you have to put sl to -10000 and tp to 1000 is absurd....  
no use lot  

> [Quoting flashlj2008](/thread/post/10823929#post10823929 "View Quoted Post")
> 
> Disliked
> 
> Between the opening and closing of a few seconds.please help? {image}
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#269](/thread/post/10824526#post10824526 "Post Permalink")

  * Feb 28, 2018 9:19pm  Feb 28, 2018 9:19pm 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

Today perhaps very strong news and currencies... my ea first time hit stop loss....  
making a sum allways is the profit but... continue testing my demo account.. monitoring this evening to restart the ea. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#270](/thread/post/10824696#post10824696 "Post Permalink")

  * Feb 28, 2018 9:50pm  Feb 28, 2018 9:50pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar523703_1.gif) faryne](faryne)

  * | Joined Oct 2016  | Status: Trader | [93 Posts](/search?do=process&provider=Member&searchuser=523703)

> [Quoting Ezios](/thread/post/10824526#post10824526 "View Quoted Post")
> 
> Disliked
> 
> Today perhaps very strong news and currencies... my ea first time hit stop loss.... making a sum allways is the profit but... continue testing my demo account.. monitoring this evening to restart the ea.
> 
> Ignored

Moving fast today. And news coming...  
Not yet stopped on my side. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#271](/thread/post/10824776#post10824776 "Post Permalink")

  * Feb 28, 2018 10:06pm  Feb 28, 2018 10:06pm 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

yes.. we are here for that... testing.. no easy on forex... perhaps it will be helpful this you call the standard deviation of a currency but i know nothing about it and how to exclude it from trading because it is too strong the directio0n???? too complicate to mee....  

> [Quoting faryne](/thread/post/10824696#post10824696 "View Quoted Post")
> 
> Disliked
> 
> {quote} Moving fast today. And news coming... Not yet stopped on my side.
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#272](/thread/post/10825193#post10825193 "Post Permalink")

  * Edited Mar 1, 2018 11:29am  Feb 28, 2018 11:48pm | Edited Mar 1, 2018 11:29am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar620434_4.gif) syndicat](syndicat)

  * | Additional Username  | Joined Oct 2017 | [432 Posts](/search?do=process&provider=Member&searchuser=620434)

A good day today + 6%!!! I trade with my hands, I use the EA only to open 1 basket. 

"Money makes Money"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#273](/thread/post/10825209#post10825209 "Post Permalink")

  * Feb 28, 2018 11:51pm  Feb 28, 2018 11:51pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar409665_1.gif) Fancysegs](fancysegs)

  * | Joined Apr 2015  | Status: Trader | [52 Posts](/search?do=process&provider=Member&searchuser=409665)

For those that code and mould this indicator..God bless the day you were born...With your indicator i have made hundred of dollars from forex market especially binary options....God bless all the contributors here...I cherish you and love you all. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#274](/thread/post/10829145#post10829145 "Post Permalink")

  * Mar 1, 2018 10:51pm  Mar 1, 2018 10:51pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar620434_4.gif) syndicat](syndicat)

  * | Additional Username  | Joined Oct 2017 | [432 Posts](/search?do=process&provider=Member&searchuser=620434)

I need a programmer to write an expert Advisor! Anyone interested? 

"Money makes Money"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#275](/thread/post/10829223#post10829223 "Post Permalink")

  * Mar 1, 2018 11:07pm  Mar 1, 2018 11:07pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar523703_1.gif) faryne](faryne)

  * | Joined Oct 2016  | Status: Trader | [93 Posts](/search?do=process&provider=Member&searchuser=523703)

> [Quoting syndicat](/thread/post/10829145#post10829145 "View Quoted Post")
> 
> Disliked
> 
> I need a programmer to write an expert Advisor! Anyone interested?
> 
> Ignored

What's your idea? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#276](/thread/post/10829265#post10829265 "Post Permalink")

  * Mar 1, 2018 11:12pm  Mar 1, 2018 11:12pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar620434_4.gif) syndicat](syndicat)

  * | Additional Username  | Joined Oct 2017 | [432 Posts](/search?do=process&provider=Member&searchuser=620434)

> [Quoting faryne](/thread/post/10829223#post10829223 "View Quoted Post")
> 
> Disliked
> 
> {quote} What's your idea?
> 
> Ignored

idea on this same system! But need only in my terms of reference 

"Money makes Money"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#277](/thread/post/10831344#post10831344 "Post Permalink")

  * Mar 2, 2018 5:54am  Mar 2, 2018 5:54am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar71675_5.gif) Alberto_Jazz](alberto_jazz)

  * Joined Jun 2008 | Status: Trader | [593 Posts](/search?do=process&provider=Member&searchuser=71675)

> [Quoting faryne](/thread/post/10819612#post10819612 "View Quoted Post")
> 
> Disliked
> 
> I'm also working on the "ghost" version.
> 
> Ignored

Another way instead of use the ghost basket, the logic is the same:  
  
1\. Wait the trigger as usual, for instance @ delta -4.7  
2\. Wait the drawdown for instance @ delta -6.5  
3\. Open the basket when delta returns to -4.7  
4\. Place the stop @ delta -6.5  
5\. Difference between open and stop deltas is 1.8, so if we close the basket when delta is -1.1 the risk reward will be 2. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#278](/thread/post/10831371#post10831371 "Post Permalink")

  * Mar 2, 2018 6:06am  Mar 2, 2018 6:06am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar523703_1.gif) faryne](faryne)

  * | Joined Oct 2016  | Status: Trader | [93 Posts](/search?do=process&provider=Member&searchuser=523703)

> [Quoting Alberto_Jazz](/thread/post/10831344#post10831344 "View Quoted Post")
> 
> Disliked
> 
> {quote} Another way instead of use the ghost basket, the logic is the same: 1. Wait the trigger as usual, for instance @ delta -4.7 2. Wait the drawdown for instance @ delta -6.5 3. Open the basket when delta returns to -4.7 4. Place the stop @ delta -6.5 5. Difference between open and stop deltas is 1.8, so if we close the basket when delta is -1.1 the risk reward will be 2.
> 
> Ignored

That doesn't work like that.  
Between @-4.7 and @ -6.5, you can virtually have a -30% basket, or a -0.1% basket (if delta jump directly to the max).  
  
And,  
Between a @-0.1% basket and a @-5% basket, you can virtually have the same delta, even a negative differential delta. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#279](/thread/post/10831394#post10831394 "Post Permalink")

  * Mar 2, 2018 6:17am  Mar 2, 2018 6:17am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar71675_5.gif) Alberto_Jazz](alberto_jazz)

  * Joined Jun 2008 | Status: Trader | [593 Posts](/search?do=process&provider=Member&searchuser=71675)

> [Quoting faryne](/thread/post/10831371#post10831371 "View Quoted Post")
> 
> Disliked
> 
> {quote} That doesn't work like that. Between @-4.7 and @ -6.5, you can virtually have a -30% basket, or a -0.1% basket (if delta jump directly to the max). And, Between a @-0.1% basket and a @-5% basket, you can virtually have the same delta, even a negative differential delta.
> 
> Ignored

  
![](https://resources.faireconomy.media/images/emojis/64/1f914.png?v=15.1) Yes, now I see the point. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#280](/thread/post/10842385#post10842385 "Post Permalink")

  * Mar 6, 2018 11:02am  Mar 6, 2018 11:02am 

  * [ flashlj2008](flashlj2008)

  * | Joined Jul 2016  | Status: Trader | [32 Posts](/search?do=process&provider=Member&searchuser=474892)

please recommend. how to set lots,tp,sl for [Medusa？](https://www.forexfactory.com/attachment.php/2694176?attachmentid=2694176)  
thanks. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Playing with the currencies: Gabin System
  *   * [ **Reply to Thread** ](/thread/739272-playing-with-the-currencies-gabin-system/reply#reply)

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

[Doubling up method or playing casino](/thread/4169-doubling-up-method-or-playing-casino "Hi everyone, 
  
I was thinking about one strategy which I called doubling up method but I want to share it and you to review and make...") 24 replies

[Playing the Double-Up Game?](/thread/42119-playing-the-double-up-game "It's sure a crazy full of risk system. I was just wondering if anyone ever heard of someone doing this and winning? 
  
With this system...") 40 replies

[Playing with datetime...](/thread/36065-playing-with-datetime "Hi, 
  
Setting the date, manually, in Alert 2 to todays date, why does Alert 1 return a different value than Alert 2? Even using...") 2 replies

[Playing the Breakout Trade](/thread/6189-playing-the-breakout-trade "by Abe Cofnas 
 
When markets move, particularly in Forex, they move fast. We all have witnessed breakouts and have had the occasion to...") 4 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/739272-playing-with-the-currencies-gabin-system/reply#reply)
  * Subscribe
  * [161](javascript:void\(0\);)

Attachments: Playing with the currencies: Gabin System

Tags: Playing with the currencies: Gabin System

#  [](/thread/739272-playing-with-the-currencies-gabin-system)Playing with the currencies: Gabin System 

  * 

  * [#281](/thread/post/10842800#post10842800 "Post Permalink")

  * Mar 6, 2018 4:10pm  Mar 6, 2018 4:10pm 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

Madscalp, i still testing with my ea. Yesterday I got a take profit and a stop loss.  
Today i got 3 take profit and its in progress to have a 4? take profit.  
I see this system works well with flat market and when there are the strong movements it hit stop loss.  
Can you to find an index to measure when market is flat and so i make the ea to trade only on flat market.  
think about it to improve this madscalp.... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#282](/thread/post/10851602#post10851602 "Post Permalink")

  * Mar 8, 2018 6:52pm  Mar 8, 2018 6:52pm 

  * [ cvdm001](cvdm001)

  * | Joined Sep 2015  | Status: Trader | [45 Posts](/search?do=process&provider=Member&searchuser=425764)

> [Quoting madscalp](/thread/post/10812282#post10812282 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi vinvlad Yes Ezios made an excellent indicator which displays too a good pair to trade. Sometimes I do it also with S/R help like you but curiously the discussion here has been mostly about basket trading. See with him if he wants to make your request.
> 
> Ignored

Hi Ezios,  
Are you willing to share the indicator which Ezios coded, as per your above comment.  
  
I would appreciate you sharing it.  
  
Many Thanks  
  
Chris 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#283](/thread/post/10852647#post10852647 "Post Permalink")

  * Mar 8, 2018 11:36pm  Mar 8, 2018 11:36pm 

  * [ juraia](juraia)

  * Joined Nov 2015 | Status: A great member he understands! | [462 Posts](/search?do=process&provider=Member&searchuser=432953)

Wow, it's like an ATM. Enter the pin code 4.2 4.6 5.0 7.0 and the picture shows how much you downloaded during news EUR, CAD and USD. If you enter the madscalp pin code, you may download more. Expert pwtcea_v2 released it at 09:55 GMT opened 2 baskets NZD and USD, gathered $ 10 to 10:22 GMT. I rebooted the expert. Until 11:40 you can not find a basket. Open USD in a dangerous time, then EUR, again NZD and get 35 deals I think, right in the news. She reached DD -50 $ and more. Then I said, this expert swims in calm waters, not for that time. And when the effect of news drops, usually after 15 minutes, prices have returned. In the end, he closed his baskets and at 13:52 it was over. This is a bit of luck to me as you enter strict news rules. I call it another effect on the first test.  
I have questions. As far as I read in a topic, if you hit SL, restart the expert. And when he hit TP and closed the baskets, should he be restarted?  
When will the live account come out?  
Thank you for the efforts you have made!  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Capture.PNG
Size: 12 KB](/attachment/image/2707995/thumbnail?d=1520519812)](/attachment/image/2707995?d=1520519812)   

  
  
Уау, това е като банкомат. Въвеждаш пин код 4.2 4.6 5.0 7.0 и от снимката се вижда колко си изтеглил по време на новини EUR, CAD и USD. Ако въведеш пин кода на madscalp, може и повече да изтеглиш. Експерта pwtcea_v2 го пуснах в 09:55 GMT отвори 2 кошници NZD и USD, събра 10 $ до 10:22 GMT. Рестартирах експерта. До 11:40 не си намери кошница. Отвори USD в опасно време, после EUR, отново NZD и стигна 35 сделки мисля, точно в новината. Достигна DD -50$ и повече. Тогава си казах, този експерт плува в по-спокойни води, не е за това време. И когато намаля ефекта от новините, обикновенно след 15 мин., цените се върнаха. Последователно си затвори кошниците и в 13:52 всичко приключи. Това за мене е и малко късмет, щом въвеждате стриктни правила за новини. Наричам го още ефект на първи тест.  
Имам въпроси. Доколкото прочетох в тема, ако се удари SL, рестартираш експерта. А когато удари TP и затвори кошниците, трябва ли да се рестартира?  
Кога ще излезе версия за сметка на живо?  
Благодаря Ви за усилията, които сте положили! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#284](/thread/post/10853210#post10853210 "Post Permalink")

  * Mar 9, 2018 1:26am  Mar 9, 2018 1:26am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar71675_5.gif) Alberto_Jazz](alberto_jazz)

  * Joined Jun 2008 | Status: Trader | [593 Posts](/search?do=process&provider=Member&searchuser=71675)

> [Quoting Ezios](/thread/post/10842800#post10842800 "View Quoted Post")
> 
> Disliked
> 
> I see this system works well with flat market and when there are the strong movements it hit stop loss.
> 
> Ignored

May be we could open a basket just after a strong movement, when we see the volatility is coming down... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#285](/thread/post/10853565#post10853565 "Post Permalink")

  * Mar 9, 2018 2:48am  Mar 9, 2018 2:48am 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

> [Quoting Alberto_Jazz](/thread/post/10853210#post10853210 "View Quoted Post")
> 
> Disliked
> 
> {quote} May be we could open a basket just after a strong movement, when we see the volatility is coming down...
> 
> Ignored

but first we have to defined what's strong movement.  
I observed the average level is 4.5 because 36/8 is 4.5. this is the average of each symbol.  
When there are 4 symbols under 4.5 and 4 symbols over 4.5 this is equilibrium market.  
when there are for example 6 symbols over 4.5 and 2 under 4.5 is strong  
when there are 6 under 4.5 and 2 over 4.5 is weak. this is an ipotesi. i can not to trade when strong market  
because when strong market often there is the stop loss because no inversion.  
but i want to know if this is the right approach to valutate if strong or weak the market.  
for now i have 28 market orders open in my ea (4 baskets) and a dd of about 40 euros and market is in equilibrium so....  
can not be true valutation of me.... if i have no index to validate the market i cant to take a decision about trade or not trade.  
For today i had 2 take profit but it can be a stop loss... who knows? ... continuing testing and expecting for new ideas..... 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#286](/thread/post/10855171#post10855171 "Post Permalink")

  * Mar 9, 2018 3:30pm  Mar 9, 2018 3:30pm 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

this morning nzd basket is very strong. I got in my ea 42 orders 6 baskets and then.. due to a my debugging error another basket  
was open so 49 orders.... i am in dd about 20 euros but... its a question of luck to have sl or tp...  
for now i will not go live with this system neither with cent account... we have to find more strict rules. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#287](/thread/post/10855864#post10855864 "Post Permalink")

  * Mar 9, 2018 7:27pm  Mar 9, 2018 7:27pm 

  * [ zoraxfx](zoraxfx)

  * | Joined Mar 2015  | Status: Trader | [255 Posts](/search?do=process&provider=Member&searchuser=402886)

i'm new in forex and i'm following this thread  
for me it is a risky method but with a filter it's possible de improve it...maybe ?  
i set the indicator with different TF H4 H1 M30 M15 M5 M1  
Earlier in the day there was JPY as a weak currency  
we see in the pic that the JPY strenght is increasing from H4 to M1  
I have bought JPY at this time with success...i don't know if that can be useful for the method  
create a new indicator which represents the evolution of the currency from H4 to M1 ???? 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: 6.jpg
Size: 187 KB](/attachment/image/2709468/thumbnail?d=1520591252)](/attachment/image/2709468?d=1520591252)   

Attached File(s)

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [CM_Strength_TF V1.0.mq4](/attachment/file/2709466?d=1520591231) 20 KB | 310 downloads 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#288](/thread/post/10855940#post10855940 "Post Permalink")

  * Mar 9, 2018 7:46pm  Mar 9, 2018 7:46pm 

  * [ tiwana207](tiwana207)

  * | Joined Apr 2017  | Status: Trader | [1 Post](/search?do=process&provider=Member&searchuser=570072)

> [Quoting faryne](/thread/post/10819612#post10819612 "View Quoted Post")
> 
> Disliked
> 
> Hello all, Here is the latest version of Medusa including: -News management (stop trading before x min, auto close positive basket before x min, restart trading after x min, reverse trading on news, etc) -More buttons for manual trading (open/close/on off by pair and total) -Improvments on verbose -Many bugs fixation (like the rearming situation) Need to be test on demo. I'm also working on the "ghost" version. Code is ok, I'm currently testing it. Edit: "Stop for news" verbose was not updated. {image} {image} {file}
> 
> Ignored

Hi,  
  
I'm getting error to "Allow Dll files". I've already allowed. Please help me to resolve. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#289](/thread/post/10855996#post10855996 "Post Permalink")

  * Mar 9, 2018 7:56pm  Mar 9, 2018 7:56pm 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

> [Quoting zoraxfx](/thread/post/10855864#post10855864 "View Quoted Post")
> 
> Disliked
> 
> i'm new in forex and i'm following this thread for me it is a risky method but with a filter it's possible de improve it...maybe ? i set the indicator with different TF H4 H1 M30 M15 M5 M1 Earlier in the day there was JPY as a weak currency we see in the pic that the JPY strenght is increasing from H4 to M1 I have bought JPY at this time with success...i don't know if that can be useful for the method create a new indicator which represents the evolution of the currency from H4 to M1 ???? {file} {image}
> 
> Ignored

interesting. this is a completely different approach from madscal's. it is based on the grow of the strengh of the basket.  
the rule can be: 6 tf period 3: h4,h1,m30,m15,m5,m1 find a symbol that in every tf is more strong or more weak. when you find it for strong  
you buy it for weak you sell. when hit tp in currency fixed by user close all baskets wen it sl fixed by user close all bsket.  
it is easy to say but difficult to do for me.... the coding... but.... if anyone wants to try??? faryne??????? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#290](/thread/post/10856406#post10856406 "Post Permalink")

  * Mar 9, 2018 9:36pm  Mar 9, 2018 9:36pm 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

as today i am in vacation i enjoyed to do this:  
modify the indicator cutting off the annoying rectangle and adding black background  
to not be disturbed by ghe chart.  
I did 6 different setting for the indicator and attached 6 instances in a single chart.  
I saved the template.  
who wants to try this manual can do. if someone find it useful  
i will to try to merge it in an unique indicator. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: cm6tf.png
Size: 39 KB](/attachment/image/2709678/thumbnail?d=1520598891)](/attachment/image/2709678?d=1520598891)   

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [cm6tf.ex4](/attachment/file/2709679?d=1520598914) 39 KB | 293 downloads 

![File Type: tpl](https://assets.faireconomy.media/images/attach/tpl.gif) [cm6tf.tpl](/attachment/file/2709681?d=1520598998) 58 KB | 273 downloads 

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#291](/thread/post/10857628#post10857628 "Post Permalink")

  * Mar 10, 2018 1:27am  Mar 10, 2018 1:27am 

  * [ zoraxfx](zoraxfx)

  * | Joined Mar 2015  | Status: Trader | [255 Posts](/search?do=process&provider=Member&searchuser=402886)

maybe a bad idea...?  
it's difficult to test during the news 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#292](/thread/post/10857659#post10857659 "Post Permalink")

  * Mar 10, 2018 1:32am  Mar 10, 2018 1:32am 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

> [Quoting juraia](/thread/post/10852647#post10852647 "View Quoted Post")
> 
> Disliked
> 
> Wow, it's like an ATM. Enter the pin code 4.2 4.6 5.0 7.0 and the picture shows how much you downloaded during news EUR, CAD and USD. If you enter the madscalp pin code, you may download more. Expert pwtcea_v2 released it at 09:55 GMT opened 2 baskets NZD and USD, gathered $ 10 to 10:22 GMT. I rebooted the expert. Until 11:40 you can not find a basket. Open USD in a dangerous time, then EUR, again NZD and get 35 deals I think, right in the news. She reached DD -50 $ and more. Then I said, this expert swims in calm waters, not for that time. And...
> 
> Ignored

im testind only demo for now. today close 1 take profit and another 35 orders are in the market.  
i trade from 2 to 22 my broker is gmt+2. i trade max 6 basket at a time. when stop 100 euro the ea auto removes.  
when tp 10 euro the ea continue to trade. if you want remove close all and remove from chart. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#293](/thread/post/10857754#post10857754 "Post Permalink")

  * Mar 10, 2018 1:52am  Mar 10, 2018 1:52am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar653399_2.gif) scalper16](scalper16)

  * | Membership Revoked  | Joined Feb 2018 | [111 Posts](/search?do=process&provider=Member&searchuser=653399)

> [Quoting Ezios](/thread/post/10857659#post10857659 "View Quoted Post")
> 
> Disliked
> 
> {quote} im testind only demo for now. today close 1 take profit and another 35 orders are in the market. i trade from 2 to 22 my broker is gmt+2. i trade max 6 basket at a time. when stop 100 euro the ea auto removes. when tp 10 euro the ea continue to trade. if you want remove close all and remove from chart.
> 
> Ignored

  
  
  
**hellow Ezios**  
  
  
**can you code CCFp 5.2 (170606)-MD4-std indicator 0.007 level and 0.005 level break out time sound alert send notification code?**  
  
  
**regards**  
**scalper16**

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Picture3.jpg
Size: 235 KB](/attachment/image/2710225/thumbnail?d=1520613912)](/attachment/image/2710225?d=1520613912)   

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [CCFp 5.2 (170606)-MD4-std.ex4](/attachment/file/2710228?d=1520613971) 108 KB | 285 downloads 

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [CCFp 5.2 (170606)-MD4-std.mq4](/attachment/file/2710229?d=1520613973) 129 KB | 370 downloads 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#294](/thread/post/10858396#post10858396 "Post Permalink")

  * Mar 10, 2018 5:21am  Mar 10, 2018 5:21am 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

> [Quoting scalper16](/thread/post/10857754#post10857754 "View Quoted Post")
> 
> Disliked
> 
> {quote} hellow Ezios can you code CCFp 5.2 (170606)-MD4-std indicator 0.007 level and 0.005 level break out time sound alert send notification code? regards scalper16 {image} {file} {file}
> 
> Ignored

dont' know this indicator how it works... perhaps it can be used to measure the streght of all the market to establish the moment when to trade and when not to trade... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#295](/thread/post/10858536#post10858536 "Post Permalink")

  * Edited 9:22am  Mar 10, 2018 6:05am | Edited 9:22am 

  * [ juraia](juraia)

  * Joined Nov 2015 | Status: A great member he understands! | [462 Posts](/search?do=process&provider=Member&searchuser=432953)

> [Quoting Ezios](/thread/post/10857659#post10857659 "View Quoted Post")
> 
> Disliked
> 
> {quote} im testind only demo for now. today close 1 take profit and another 35 orders are in the market. i trade from 2 to 22 my broker is gmt+2. i trade max 6 basket at a time. when stop 100 euro the ea auto removes. when tp 10 euro the ea continue to trade. if you want remove close all and remove from chart.
> 
> Ignored

Ok, I already understood it. Just to mention that my experience shows that this is an absolute scalping. You go in, you take a little and you go out. The next moment again and so on. The picture is visible. I tracked alerts before news, during and after news. If you trade inside a daily chart, such as H1, there are no problems for now. You receive signals, you enter with 7 pairs, maybe seven more, you make $ 10 and go out. EUR-pairs from the day before, noon did nothing during Asia, I manually closed them before LO today. There is no volatility. If you do not, then the currency market is flat. This is a price action signal. If you do not have a trend filter, SnR, pivot or fibo, you are doomed. But that's what the big boys do. News is probably not a problem. Yesterday he did well today. This is a strategy for a highly volatile signal. With such an impression I remain. All day-to-day trading indicators showed a reverse signal and entered big DD, waiting for the news. I use BQR and TDI with EAX dashboard. I was looking for the winner. Again, pwtcea_v2 went into trading GBP and JPY at 12:55 GMT, 35 min ago. big news affecting USD and CAD, but at 13:25 it reached $ 10. Followed by short-term news, within minutes. No winner, egalit. I restrict BQR to many signals, but I am struggling with the big DD. Today's day is not indicative, I guess many systems are green.  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Capture.PNG
Size: 41 KB](/attachment/image/2710598/thumbnail?d=1520629375)](/attachment/image/2710598?d=1520629375)   

  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Capture_0.PNG
Size: 195 KB](/attachment/image/2710600/thumbnail?d=1520629475)](/attachment/image/2710600?d=1520629475)   

  
  
Ок, това вече го разбрах. Само да спомена, че моят опит показва, че това е абсолютен скалпинг. Влизаш, взимаш малко и излизаш. В следващият момент отново и т. н. В снимката се вижда. Проследих сигналите преди новини, по време на новини и след тях. Ако търгуваш на вътре дневна графика, примерно H1, засега няма проблеми. Получаваш сигнали, влизаш с 7 двойки, може с още 7, правиш 10$ и излизаш. Двойките с EUR от предишният ден, след обяд, нищо не направиха по време на Азия, ръчно ги затворих преди LO днес. Няма волатилност. Ако не ги направиш, значи е плосък пазара за валутата. Това е price action сигнал. Ако нямаш филтър за тренд, SnR, pivot или fibo, обречен си. Но така правят големите момчета. Новините вероятно не са проблем. Вчера и днес се справи чудесно. Това е стратегия за силно волативен сигнал. С такова впечатление оставам. Всички индикатори за дневна търговия показваха обратен сигнал и влизаха в голям DD, чакаха новините. Аз използвам BQR и TDI с табло EAX. Търсех победителя. Отново pwtcea_v2 влезе в търговия GBP и JPY в 12:55 GMT, 35 мин. преди т.н. големи новини, засягащи USD и CAD, но в 13:25 постигна 10$. Последваха новините, които краткосрочно въздействат, в рамките на минути. Победител няма, равенство. Аз ограничавам BQR в многото сигнали, но се боря с големият DD. Днешният ден, не е показателен, предполагам много системи са на зелено. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#296](/thread/post/10858563#post10858563 "Post Permalink")

  * Edited 9:12am  Mar 10, 2018 6:22am | Edited 9:12am 

  * [ juraia](juraia)

  * Joined Nov 2015 | Status: A great member he understands! | [462 Posts](/search?do=process&provider=Member&searchuser=432953)

I suggest you enter the magical number into the EA settings themselves. Get it out of the buttons. It makes no sense to start EA, have a default number of 6161 and then change it. I took a picture of the dashboard I use to track signals with the same magical number.  
The other I think is important for EA, prohibiting and resolving automatic trading. Just an example: I launch EA, immediately finds currency for trading and starts deals. The merchant can not blink with his eyes to change the magical number, and what remains to look at the graphics.  
  
  
Предлагам ти магическият номер, да се въвежда в самите настройки на EA. Махни го от бутоните. Няма смисъл да стартираш EA, да е с номер по подразбиране 6161 и после да го променяш. Направих снимка на таблото, което използвам за да проследя сигналите със същият магически номер.  
Другото, което мисля, че е важно за EA, забраняване и разрешаване на автоматичната търговия. Просто пример: Стартирам EA, веднага намира валута за търговия и стартира сделки. Търговеца няма възможност и да мигне с очите си, за да промени магическият номер, а какво остава да погледне графиките. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#297](/thread/post/10858656#post10858656 "Post Permalink")

  * Mar 10, 2018 7:14am  Mar 10, 2018 7:14am 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

> [Quoting juraia](/thread/post/10858563#post10858563 "View Quoted Post")
> 
> Disliked
> 
> I suggest you enter the magical number into the EA settings themselves. Get it out of the buttons. It makes no sense to start EA, have a default number of 6161 and then change it. I took a picture of the dashboard I use to track signals with the same magical number. The other I think is important for EA, prohibiting and resolving automatic trading. Just an example: I launch EA, immediately finds currency for trading and starts deals. The merchant can not blink with his eyes to change the magical number, and what remains to look at the graphics....
> 
> Ignored

i use magic 6161 but i do many tries with more ea and they have magic different so i put magic 6464 and i close all... so  
it is very useful to me to change magic at the fly without to go in the setting and change it.  
also if i want to watch other eas what they doing i change magic and i see the numbers.. so its the same thing if you dont  
change it dont look at it. some eas use magic = 0 and i put 0 and i see the trades. so...  
the other indicators and dashboards that you use i dont know... 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#298](/thread/post/10858714#post10858714 "Post Permalink")

  * Edited 9:13am  Mar 10, 2018 7:48am | Edited 9:13am 

  * [ juraia](juraia)

  * Joined Nov 2015 | Status: A great member he understands! | [462 Posts](/search?do=process&provider=Member&searchuser=432953)

Parallel to the pwtcea_v2 test, I tested the Medusa. Almost the same proposal. Please put a magical number.  
Allow currency selections. Just an example: I never trade CHF because my broker requires a big margin and so I release funds for the other couples.  
I tried to remove Breakeven and TS by entering 0, the basket went in a positive direction, then returned to 0 and closed.  
Allow the trader to choose whether or not to use TS.  
Probably I need more explanation from post 251. Example: I want to trade pairs that are not directly related to the news. Naturally, if there is a signal for AUD today, there is a connection with USD and CAD, but if I enter 90 minutes before the news does not trade, it prohibits all pairs with AUD. I entered 1 minute after the news, but EA did not release the pairs list. Absolutely no currency has entered into the terms. That can not be true. I saw opening CAD and JPY from pwtcea_v2  
Actually this is a price action signal based on daily chart and I think pwtcea_v2 and Medusa do well in the calculations of signals and logic. Another question is whether this signal is along with the trend, has economic news, has an earthquake happened, someone has resigned or uncle Donald has said some stupidity. Just one example: Correct signal, only 7 pairs, each doing 15 pips = 105. About 10 $ with 0.01. If there is a pair pulling fast and doing more, again $ 10. If there are 2 or 3 more signals, it depends on the day, here are 300 pips. It looks simple, but there is a manual closing. The 7 pairs range between 20 pips and -20, reach 50, return to -30 and so more than 1-2 hours. I will not wait for them, I will just close them with a small profit. It is clear that couples are in consensus. I think that about 300 pips is a very good option for the day.  
  
  
Паралелно с теста на pwtcea_v2, тествах и Medusa. Почти същото предложение. Моля Ви, сложете магически номер.  
Дайте възможност за избор на валути. Просто пример: Аз никога не търгувам CHF, защото моят брокер изисква голям марджин и така освобождавам средства за останалите двойки.  
Опитах се да премахна Breakeven и TS, като въведох 0, кошницата отиде в положителна посока, после върна до 0 и затвори.  
Дайте възможност на търговеца да избира, иска или не, да използва TS.  
Вероятно ми трябва повече обяснение от пост 251. Примерно: Искам да търгувам двойки, които не са свързани пряко с новината. Естествено, ако има сигнал за AUD днес, има връзка с USD и CAD, но ако въведа 90 мин. преди новина да не търгува, забранява всички двойки с AUD. Въведох 1 мин. след новината, но EA не освободи списъка от двойки. Абсолютно нито една валута не влезе в условията. Това няма как да е вярно. Видях отваряне на CAD и JPY от pwtcea_v2  
Всъщност това е price action сигнал на базата на дневна графика и аз мисля, че pwtcea_v2 и Medusa добре се справят в изчисленията на сигналите и логиката. Друг е въпроса, дали този сигнал е заедно с тренда, икономическа новина ли има, земетресение ли е станало, някой си е подал оставката или чичо Доналд е казал някаква глупост. Само един пример: Правилен сигнал, само 7 двойки, всяка прави по 15 пипа = 105. Около 10$ с 0.01. Ако има двойка да дърпа бързо и прави повече, пак 10$. Ако има още 2 или 3 сигнала, зависи от деня, ето ти 300 пипа. Изглежда просто, но има и ръчно затваряне. 7-те двойки варират между 20 пипа и -20, достигат 50, връщат на -30 и така повече от 1 - 2 часа. Няма да ги чакам, просто ще ги затворя с малка печалба. Ясно е, че двойките са в консенсус. Аз мисля, че около 300 пипа, е един много добър вариант за деня. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#299](/thread/post/10858784#post10858784 "Post Permalink")

  * Mar 10, 2018 8:29am  Mar 10, 2018 8:29am 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

I upload version 3.  
One has the ablity to set trade time from-to , use time filter true or false  
open max baskets , set daily profit target so.. if you want trade 1 our a day and take 10 dollars you can....  
the settings of default are as i like from my broker. test and good luck. 

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [pwtceav3ff.ex4](/attachment/file/2710707?d=1520638148) 112 KB | 247 downloads 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#300](/thread/post/10858852#post10858852 "Post Permalink")

  * Mar 10, 2018 9:10am  Mar 10, 2018 9:10am 

  * [ juraia](juraia)

  * Joined Nov 2015 | Status: A great member he understands! | [462 Posts](/search?do=process&provider=Member&searchuser=432953)

> [Quoting Ezios](/thread/post/10858656#post10858656 "View Quoted Post")
> 
> Disliked
> 
> {quote} i use magic 6161 but i do many tries with more ea and they have magic different so i put magic 6464 and i close all... so it is very useful to me to change magic at the fly without to go in the setting and change it. also if i want to watch other eas what they doing i change magic and i see the numbers.. so its the same thing if you dont change it dont look at it. some eas use magic = 0 and i put 0 and i see the trades. so... the other indicators and dashboards that you use i dont know...
> 
> Ignored

I write slowly and with many mistakes. Only until I write this and you publish the new version. You're incredible! ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
  
Ok, this is not a big problem. I gave you an example simply, you run EA and immediately make deals. It is clear that it will stay with 6161. The other is more important, authorizing and disabling automatic trading. Manually control when EA is trading. Business sessions have many key moments. For example, during the London session closing the Asian markets, EA has open deals, but I do not want to open new ones at this point because the signal is uncertain. Then come USA. With one click of a button, the merchant can ban the trade for a certain amount of time and start again. If you know you follow news and you are not a risky player, just OFF. Of course, this is just a proposal.  
I guess the goal is purely automatic trading. Many things are needed to make this happen. It is best for EA to choose the trading time (GMT or PC time). So you can easily avoid inappropriate trading times.  
There is a very crucial moment. Limiting EA to the number of transactions made at a time. If it does not, you risk the whole balance. Example: The Merchant has no idea which of the eight currencies will signal during the day and puts them all. Only three currencies receive a signal at some time. Theoretically, even just two to go through 2 levels, there are 28 deals, plus the third one in 1 level, another 7, that's a total of 35 deals. Just think if this is the limit of your account and some currency passes the next level. Even if they have a very good signal, margin call. Let's think a little about the options for MM and R:R.  
  
Аз пиша бавно и с много грешки. Само докато напиша това и ти публикува новата версия. Невероятен си!  
  
Ок, това не е голям проблем. Дадох Ви пример просто, пускате EA и веднага пуска сделки. Ясно е, че ще остане с 6161. Другото е по-важно, разрешаване и забраняване на автоматичната търговия. Ръчно управление, кога EA да търгува. Търговските сесии, имат много ключови моменти. Например по времето на Лондон сесия, затварят Азиатските пазари, EA има отворени сделки, но не искам да отваря нови, точно в този момент, защото сигнала е несигурен. После идват USA. Търговеца с едно натискане на бутон, може да забрани търговията за определено време и отново да стартира. Ако знаеш, че следва новина и не си рисков играч, просто OFF. Разбира се, това е само предложение.  
Предполагам, че целта е изцяло автоматична търговия. Много неща са необходими, за да се случи това. Най-добре е, в EA да се избира времето за търговия (по GMT или PC време). Така лесно избягваш неподходящите времена на търговия.  
Има един много ключов момент. Ограничаването на EA в броя на сключените сделки в даден момент. Ако това го няма, рискуваш целият баланс. Пример: Търговеца няма представа, кои от 8-те валути ще имат сигнал през деня и ги пуска всичките. Само три валути, получават сигнал през някакво време. Теоретично, дори само 2 да минат през 2 нива, са 28 сделки, плюс третата през 1 ниво, още 7, това е общо 35 сделки. Просто помислете, ако това е границата на вашата сметка и някоя валута премине следващо ниво. Дори и да са с много изгоден сигнал, margin call. Нека да помислим малко за вариантите за MM и R:R. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Playing with the currencies: Gabin System
  *   * [ **Reply to Thread** ](/thread/739272-playing-with-the-currencies-gabin-system/reply#reply)

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

[Doubling up method or playing casino](/thread/4169-doubling-up-method-or-playing-casino "Hi everyone, 
  
I was thinking about one strategy which I called doubling up method but I want to share it and you to review and make...") 24 replies

[Playing the Double-Up Game?](/thread/42119-playing-the-double-up-game "It's sure a crazy full of risk system. I was just wondering if anyone ever heard of someone doing this and winning? 
  
With this system...") 40 replies

[Playing with datetime...](/thread/36065-playing-with-datetime "Hi, 
  
Setting the date, manually, in Alert 2 to todays date, why does Alert 1 return a different value than Alert 2? Even using...") 2 replies

[Playing the Breakout Trade](/thread/6189-playing-the-breakout-trade "by Abe Cofnas 
 
When markets move, particularly in Forex, they move fast. We all have witnessed breakouts and have had the occasion to...") 4 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/739272-playing-with-the-currencies-gabin-system/reply#reply)
  * Subscribe
  * [161](javascript:void\(0\);)

Attachments: Playing with the currencies: Gabin System

Tags: Playing with the currencies: Gabin System

#  [](/thread/739272-playing-with-the-currencies-gabin-system)Playing with the currencies: Gabin System 

  * 

  * [#301](/thread/post/10858883#post10858883 "Post Permalink")

  * Mar 10, 2018 9:33am  Mar 10, 2018 9:33am 

  * [ juraia](juraia)

  * Joined Nov 2015 | Status: A great member he understands! | [462 Posts](/search?do=process&provider=Member&searchuser=432953)

> [Quoting Ezios](/thread/post/10858784#post10858784 "View Quoted Post")
> 
> Disliked
> 
> I upload version 3. One has the ablity to set trade time from-to , use time filter true or false open max baskets , set daily profit target so.. if you want trade 1 our a day and take 10 dollars you can.... the settings of default are as i like from my broker. test and good luck. {file}
> 
> Ignored

How can I change Max Baskets 6? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#302](/thread/post/10859129#post10859129 "Post Permalink")

  * Mar 10, 2018 3:13pm  Mar 10, 2018 3:13pm 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

> [Quoting juraia](/thread/post/10858852#post10858852 "View Quoted Post")
> 
> Disliked
> 
> {quote} I write slowly and with many mistakes. Only until I write this and you publish the new version. You're incredible! ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) Ok, this is not a big problem. I gave you an example simply, you run EA and immediately make deals. It is clear that it will stay with 6161. The other is more important, authorizing and disabling automatic trading. Manually control when EA is trading. Business sessions have many key moments. For example, during the London session closing the Asian markets, EA has open deals, but I do not want to open new ones at this...
> 
> Ignored

ok i understood. but im not ready to handle the news with this ea.. but remember that you can program the day of trading  
by setting in the string which basket you want to trade if a day there is big news in cad you cut off cad from the string and the ea will not trade cad.  
if you want to limit the number of basket there is the setting and you do. remember you have to do this when you attach the ea and it will be effect  
until you remove the ea. when you remove the ea all variables are initialized to their default value. all we want is full automatic but it is impossible. the  
news... the account balance... the number of basket... is a thing that one must set by himself. ok? test it. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#303](/thread/post/10859158#post10859158 "Post Permalink")

  * Mar 10, 2018 4:05pm  Mar 10, 2018 4:05pm 

  * [ zoraxfx](zoraxfx)

  * | Joined Mar 2015  | Status: Trader | [255 Posts](/search?do=process&provider=Member&searchuser=402886)

i like this idea  
the true challenge is to find the time of reversal ...LOL  
yesterday after news there was a good opportunity buying JPY   
first a big DD then finally a win  
i'm following you 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#304](/thread/post/10859253#post10859253 "Post Permalink")

  * Mar 10, 2018 5:44pm  Mar 10, 2018 5:44pm 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

> [Quoting zoraxfx](/thread/post/10859158#post10859158 "View Quoted Post")
> 
> Disliked
> 
> i like this idea the true challenge is to find the time of reversal ...LOL yesterday after news there was a good opportunity buying JPY first a big DD then finally a win i'm following you
> 
> Ignored

in fact... the reason i put sl of 100 is to give the possibility to the market to move....  
in theory you can to attach an ea for every 8 chart and make it to work only in 1 currency  
1 for eur 1 for usd 1 for jpg with different magic number and so you can also change the sto ploss and take profit.  
dont know if this is the right way or it is better to trade all together... we will se... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#305](/thread/post/10859457#post10859457 "Post Permalink")

  * Mar 10, 2018 8:55pm  Mar 10, 2018 8:55pm 

  * [ AlHaggag](alhaggag)

  * | Joined Apr 2016  | Status: Trader | [7 Posts](/search?do=process&provider=Member&searchuser=458669)

Hi traders.  
below is my contribution to this thread  
please find attached two currency strength indicator that I personally use.  
attached in this post one is called closed cycle v1.5 .  
it display the major symbols reading.  
I Have changed the default settings from H4 to M5.  
and I trade the trend when the different between the symbol is grater than 500.( or as the trader prefer )  
also one of the symbols must be red and the other must be blue. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Closed-cycle-FI_22.png
Size: 24 KB](/attachment/image/2711042/thumbnail?d=1520682582)](/attachment/image/2711042?d=1520682582)   

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [Closed cycle FI 1.5.ex4](/attachment/file/2711043?d=1520682606) 26 KB | 284 downloads 

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [Closed cycle FI 1.5.mq4](/attachment/file/2711058?d=1520683475) 18 KB | 326 downloads 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#306](/thread/post/10859471#post10859471 "Post Permalink")

  * Mar 10, 2018 9:02pm  Mar 10, 2018 9:02pm 

  * [ AlHaggag](alhaggag)

  * | Joined Apr 2016  | Status: Trader | [7 Posts](/search?do=process&provider=Member&searchuser=458669)

The second indicator i use is similar to the one posted in this thread. thus I have found that it gives little different readings.  
I usually trade the pair that give me reading not less than 2 some times 3.  
  
I like trade with both indicator and both must agree to catch good pips from the trend 

Attached File(s)

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [Currency Strength Giraia 28 pairs TRO MODIFIED.mq4](/attachment/file/2711055?d=1520683339) 22 KB | 315 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#307](/thread/post/10859496#post10859496 "Post Permalink")

  * Mar 10, 2018 9:35pm  Mar 10, 2018 9:35pm 

  * [ juraia](juraia)

  * Joined Nov 2015 | Status: A great member he understands! | [462 Posts](/search?do=process&provider=Member&searchuser=432953)

> [Quoting Ezios](/thread/post/10859129#post10859129 "View Quoted Post")
> 
> Disliked
> 
> {quote} ok i understood. but im not ready to handle the news with this ea.. but remember that you can program the day of trading by setting in the string which basket you want to trade if a day there is big news in cad you cut off cad from the string and the ea will not trade cad. if you want to limit the number of basket there is the setting and you do. remember you have to do this when you attach the ea and it will be effect until you remove the ea. when you remove the ea all variables are initialized to their default value. all we want is full...
> 
> Ignored

I really do not understand how to change the number of baskets. I want to trade three baskets. For example, EUR passes 1st level and EA opens 1 basket, JPY also passes 1st level and EA opens 2nd basket. Let's say the JPY passes level 2 and EA opens the 3rd basket. I want EA to stop opening more baskets at this point.  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Capture.PNG
Size: 87 KB](/attachment/image/2711065/thumbnail?d=1520685319)](/attachment/image/2711065?d=1520685319)   

  
  
Аз наистина неразбирам, как да променя броя на кошниците. Искам да търгувам 3 кошници. Примерно: EUR преминава 1-во ниво и EA отваря 1 кошница, JPY също преминава 1-во ниво и EA отваря 2-ра кошница. Да кажем, че JPY преминава 2-ро ниво и EA отваря 3-та кошница. Искам в този момент EA да спре да отваря повече кошници. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#308](/thread/post/10859968#post10859968 "Post Permalink")

  * Mar 11, 2018 5:49am  Mar 11, 2018 5:49am 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

> [Quoting juraia](/thread/post/10859496#post10859496 "View Quoted Post")
> 
> Disliked
> 
> {quote} I really do not understand how to change the number of baskets. I want to trade three baskets. For example, EUR passes 1st level and EA opens 1 basket, JPY also passes 1st level and EA opens 2nd basket. Let's say the JPY passes level 2 and EA opens the 3rd basket. I want EA to stop opening more baskets at this point. {image} Аз наистина неразбирам, как да променя...
> 
> Ignored

f you want do so go in the setting the final string you putonly a pair for example eur  
it will trade only eur. you change the magic and you attach to a chart for others you do the same.  
ifyou leave the string full it will trade all. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#309](/thread/post/10859996#post10859996 "Post Permalink")

  * Mar 11, 2018 6:15am  Mar 11, 2018 6:15am 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

> [Quoting AlHaggag](/thread/post/10859457#post10859457 "View Quoted Post")
> 
> Disliked
> 
> Hi traders. below is my contribution to this thread please find attached two currency strength indicator that I personally use. attached in this post one is called closed cycle v1.5 . it display the major symbols reading. I Have changed the default settings from H4 to M5. and I trade the trend when the different between the symbol is grater than 500.( or as the trader prefer ) also one of the symbols must be red and the other must be blue. {image} {file} {file}
> 
> Ignored

thanx very much for the indicators. i did not understand the picture... you sold gbpjpg pair or you sold  
the 2 baskets gbp and jpg? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#310](/thread/post/10860004#post10860004 "Post Permalink")

  * Mar 11, 2018 6:17am  Mar 11, 2018 6:17am 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

Faryne you become famous with your Medusa ea...  
Look here:  
<https://soehoe.id/medusa-ea.t10218/>

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#311](/thread/post/10860397#post10860397 "Post Permalink")

  * Mar 11, 2018 3:25pm  Mar 11, 2018 3:25pm 

  * [ AlHaggag](alhaggag)

  * | Joined Apr 2016  | Status: Trader | [7 Posts](/search?do=process&provider=Member&searchuser=458669)

> [Quoting Ezios](/thread/post/10859996#post10859996 "View Quoted Post")
> 
> Disliked
> 
> {quote} thanx very much for the indicators. i did not understand the picture... you sold gbpjpg pair or you sold the 2 baskets gbp and jpg?
> 
> Ignored

yes. you sell GBPJPY only.  
  
look at the attache picture for more explanation. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Untitled.png
Size: 251 KB](/attachment/image/2711560/thumbnail?d=1520749466)](/attachment/image/2711560?d=1520749466)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#312](/thread/post/10860402#post10860402 "Post Permalink")

  * Mar 11, 2018 3:33pm  Mar 11, 2018 3:33pm 

  * [ juraia](juraia)

  * Joined Nov 2015 | Status: A great member he understands! | [462 Posts](/search?do=process&provider=Member&searchuser=432953)

> [Quoting Ezios](/thread/post/10859968#post10859968 "View Quoted Post")
> 
> Disliked
> 
> {quote} f you want do so go in the setting the final string you putonly a pair for example eur it will trade only eur. you change the magic and you attach to a chart for others you do the same. ifyou leave the string full it will trade all.
> 
> Ignored

The problem is that when I enter only one currency, Max Baskets remains 6.  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Capture.PNG
Size: 72 KB](/attachment/image/2711566/thumbnail?d=1520749982)](/attachment/image/2711566?d=1520749982)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#313](/thread/post/10860472#post10860472 "Post Permalink")

  * Mar 11, 2018 5:02pm  Mar 11, 2018 5:02pm 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

> [Quoting juraia](/thread/post/10860402#post10860402 "View Quoted Post")
> 
> Disliked
> 
> {quote} The problem is that when I enter only one currency, Max Baskets remains 6. {image}
> 
> Ignored

you are right... when itry the ea i forgot to put in the setting.... this updated version.  
remember tu put the basket in uppercase EUR CAD , USD if not the ea will not work. 

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [pwtceav3ff.ex4](/attachment/file/2711616?d=1520755346) 113 KB | 238 downloads 

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#314](/thread/post/10860529#post10860529 "Post Permalink")

  * Mar 11, 2018 6:30pm  Mar 11, 2018 6:30pm 

  * [ juraia](juraia)

  * Joined Nov 2015 | Status: A great member he understands! | [462 Posts](/search?do=process&provider=Member&searchuser=432953)

> [Quoting Ezios](/thread/post/10860472#post10860472 "View Quoted Post")
> 
> Disliked
> 
> {quote} you are right... when itry the ea i forgot to put in the setting.... this updated version. remember tu put the basket in uppercase EUR CAD , USD if not the ea will not work. {file}
> 
> Ignored

Just one more clarification. How many times will EUR pairs trade in this case? There is a buy signal, EA opens 7 pairs but does not reach the set TP 10. If there is a second buy signal, EA will open another 7 pairs of EUR? If so, I think it's good to restrict the EUR basket itself from opening new 7 until reaching TP or ST. If it reaches TP 10, EA closes the basket and, if there is a new signal, reopens the basket. And it all ends when Target 50 arrives.  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Capture.PNG
Size: 78 KB](/attachment/image/2711625/thumbnail?d=1520758932)](/attachment/image/2711625?d=1520758932)   

  
  
Само още едно уточнение. Колко пъти ще търгува двойките на EUR в този случай? Има сигнал купува, EA отваря 7 двойки, но не достига зададеният TP 10. Ако има втори сигнал за купува, EA ще отвори ли още 7 двойки на EUR? Ако е така, мисля че е добре да се ограничи самата кошница на EUR да не отваря нови 7 до достигане на TP или ST. Ако достигне TP 10, EA затваря кошницата и ако вече има нов сигнал, да отвори отново кошницата. И всичко приключва при достигане на Таргет 50. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#315](/thread/post/10860574#post10860574 "Post Permalink")

  * Mar 11, 2018 7:26pm  Mar 11, 2018 7:26pm 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

> [Quoting juraia](/thread/post/10860529#post10860529 "View Quoted Post")
> 
> Disliked
> 
> {quote} Just one more clarification. How many times will EUR pairs trade in this case? There is a buy signal, EA opens 7 pairs but does not reach the set TP 10. If there is a second buy signal, EA will open another 7 pairs of EUR? If so, I think it's good to restrict the EUR basket itself from opening new 7 until reaching TP or ST. If it reaches TP 10, EA closes the basket and, if there is a new signal, reopens the basket. And it all ends when Target 50 arrives. {image} Само още едно...
> 
> Ignored

the signal is 3 step. when 1 step open 7 orders if anoter 1 step no signal when signal 2 step and no sl or tp open other 7 order  
and so on till 3 step. after 3 step if you have st basket 3 no more orders untill stop loss or take profit. so works.... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#316](/thread/post/10860703#post10860703 "Post Permalink")

  * Mar 11, 2018 8:58pm  Mar 11, 2018 8:58pm 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

This week I do an experiment: put 8 chart everyone with 1 basket to trade eur,usd,cad,....  
for every ea i set max basket 3 tp 5 and sl 50 and max daily profit 25. i want to see every basket how goes....  
i put the 3 step 4.2 4.7 and 5.0 and different magic number from each ea 6262...6969. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#317](/thread/post/10860781#post10860781 "Post Permalink")

  * Mar 11, 2018 10:11pm  Mar 11, 2018 10:11pm 

  * [ juraia](juraia)

  * Joined Nov 2015 | Status: A great member he understands! | [462 Posts](/search?do=process&provider=Member&searchuser=432953)

> [Quoting Ezios](/thread/post/10860703#post10860703 "View Quoted Post")
> 
> Disliked
> 
> This week I do an experiment: put 8 chart everyone with 1 basket to trade eur,usd,cad,.... for every ea i set max basket 3 tp 5 and sl 50 and max daily profit 25. i want to see every basket how goes.... i put the 3 step 4.2 4.7 and 5.0 and different magic number from each ea 6262...6969.
> 
> Ignored

If I understand correctly, the EUR basket can open 21 trades in 3 consecutive signals and reach TP or SL. This is a very large volume of trading, especially for small bills (cents). If you also include a basket limitation, EA can only trade at Level 1, EA to open only 7 deals. In this case, you can include at least two more baskets. This increases your chances of getting good signals in 3 currencies a day, and you can still trade with a volume of 21 (0.21 Lots). The idea is to include more currencies with the best 1st signal. Even in 1 EA can happen, with the same magical number. Merchant does not know which currencies to include. For example, all currencies included, you limit EA, trade up to 3 baskets (ie the first 3 who receive a signal) and a second limit is that each currency trades at level 1. I think it is a better option. Put on all TP 45 (or a basket of 15) as you decide. What do you think?  
  
Ако правилно те разбирам, кошницата EUR, може да отвори 21 сделки при 3 последователни сигнала и достигане на TP или SL. Това е много голям обем за търговия, особено за малките сметки (центови). Ако включиш и ограничаване на кошницата, EA да сключва сделки само при ниво 1, т.е. EA да отвори само 7 сделки. В този случай можеш да включиш поне още две кошници. Така увеличаваш шансовете да хванеш добри сигнали, при 3 валути в деня и пак да търгуваш с обем 21 (0.21 Lots). Идеята е, да се включат повече валути с най-добрият 1-ви сигнал. Дори в 1 EA може да стане, с един и същи магически номер. Търговеца не знае кои валути да включи. Примерно: Всички валути включени, ограничаваш EA, да търгува с до 3 кошници (т.е. първите 3, които получат сигнал) и второ ограничение е всяка валута да търгува с ниво 1. Мисля, че е по-добър вариант. Слагаш на всички TP 45 (или на кошница по 15), както решиш. Ти как мислиш? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#318](/thread/post/10860948#post10860948 "Post Permalink")

  * Mar 12, 2018 12:28am  Mar 12, 2018 12:28am 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

> [Quoting juraia](/thread/post/10860781#post10860781 "View Quoted Post")
> 
> Disliked
> 
> {quote} If I understand correctly, the EUR basket can open 21 trades in 3 consecutive signals and reach TP or SL. This is a very large volume of trading, especially for small bills (cents). If you also include a basket limitation, EA can only trade at Level 1, EA to open only 7 deals. In this case, you can include at least two more baskets. This increases your chances of getting good signals in 3 currencies a day, and you can still trade with a volume of 21 (0.21 Lots). The idea is to include more currencies with the best 1st signal. Even in 1 EA...
> 
> Ignored

dont know... must try... but if you set all 3 signals to 4.2 and max basket 3 and leave the string all currencies can work. but you must consider the signal is up and down so the signals are 6 3 for up and 3 for down... dont know. try.... i try what i told in the precend post. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#319](/thread/post/10861608#post10861608 "Post Permalink")

  * Mar 12, 2018 8:53am  Mar 12, 2018 8:53am 

  * [ Groffobonchi](groffobonchi)

  * | Joined Mar 2018  | Status: Trader | [6 Posts](/search?do=process&provider=Member&searchuser=659957)

Sorry friends, but why suddenly you can no longer load on the chart?  
Grazie 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#320](/thread/post/10861644#post10861644 "Post Permalink")

  * Mar 12, 2018 9:40am  Mar 12, 2018 9:40am 

  * [ Groffobonchi](groffobonchi)

  * | Joined Mar 2018  | Status: Trader | [6 Posts](/search?do=process&provider=Member&searchuser=659957)

I refer to Medusa 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Playing with the currencies: Gabin System
  *   * [ **Reply to Thread** ](/thread/739272-playing-with-the-currencies-gabin-system/reply#reply)

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

[Doubling up method or playing casino](/thread/4169-doubling-up-method-or-playing-casino "Hi everyone, 
  
I was thinking about one strategy which I called doubling up method but I want to share it and you to review and make...") 24 replies

[Playing the Double-Up Game?](/thread/42119-playing-the-double-up-game "It's sure a crazy full of risk system. I was just wondering if anyone ever heard of someone doing this and winning? 
  
With this system...") 40 replies

[Playing with datetime...](/thread/36065-playing-with-datetime "Hi, 
  
Setting the date, manually, in Alert 2 to todays date, why does Alert 1 return a different value than Alert 2? Even using...") 2 replies

[Playing the Breakout Trade](/thread/6189-playing-the-breakout-trade "by Abe Cofnas 
 
When markets move, particularly in Forex, they move fast. We all have witnessed breakouts and have had the occasion to...") 4 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/739272-playing-with-the-currencies-gabin-system/reply#reply)
  * Subscribe
  * [161](javascript:void\(0\);)

Attachments: Playing with the currencies: Gabin System

Tags: Playing with the currencies: Gabin System

#  [](/thread/739272-playing-with-the-currencies-gabin-system)Playing with the currencies: Gabin System 

  * 

  * [#321](/thread/post/10862058#post10862058 "Post Permalink")

  * Mar 12, 2018 2:44pm  Mar 12, 2018 2:44pm 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

i tried onlyonce medusa with ootb setting buty tried when market closed. noly 3 o4 raws display but dont know...  
ebaut my ea... today nzd very strong I had 3 signals and its running. I will add next version the string that's trading.  
we will see if will revert.. in this case i will have take profit.... its good experiment trying currency one at a time... 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: pwtcea_nzd.png
Size: 29 KB](/attachment/image/2712437/thumbnail?d=1520833432)](/attachment/image/2712437?d=1520833432)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#322](/thread/post/10862067#post10862067 "Post Permalink")

  * Mar 12, 2018 2:48pm  Mar 12, 2018 2:48pm 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

pardon no nzd usd... sorry... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#323](/thread/post/10862352#post10862352 "Post Permalink")

  * Mar 12, 2018 5:25pm  Mar 12, 2018 5:25pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar523703_1.gif) faryne](faryne)

  * | Joined Oct 2016  | Status: Trader | [93 Posts](/search?do=process&provider=Member&searchuser=523703)

> [Quoting Groffobonchi](/thread/post/10861644#post10861644 "View Quoted Post")
> 
> Disliked
> 
> I refer to Medusa
> 
> Ignored

Here updated version. 

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [Medusa.ex4](/attachment/file/2712572?d=1520843138) 153 KB | 427 downloads 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#324](/thread/post/10863074#post10863074 "Post Permalink")

  * Mar 12, 2018 9:09pm  Mar 12, 2018 9:09pm 

  * [ Groffobonchi](groffobonchi)

  * | Joined Mar 2018  | Status: Trader | [6 Posts](/search?do=process&provider=Member&searchuser=659957)

Thanks, I forced you, it's simply spectacular if used with a bit of forex knowledge 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#325](/thread/post/10864041#post10864041 "Post Permalink")

  * Mar 13, 2018 12:10am  Mar 13, 2018 12:10am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar523703_1.gif) faryne](faryne)

  * | Joined Oct 2016  | Status: Trader | [93 Posts](/search?do=process&provider=Member&searchuser=523703)

> [Quoting Groffobonchi](/thread/post/10863074#post10863074 "View Quoted Post")
> 
> Disliked
> 
> Thanks, I forced you, it's simply spectacular if used with a bit of forex knowledge
> 
> Ignored

Feel free to contribute to improve the EA... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#326](/thread/post/10864524#post10864524 "Post Permalink")

  * Mar 13, 2018 1:56am  Mar 13, 2018 1:56am 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

the situatin of today:  
\- running magic 6161 all currencies wth 5 open baskets and about -11 eur dd  
\- magic 6969 usd took profit 5.61 eur now not trading  
\- magic 6868 nzd took profit 5,29 eur now running 1 basket dd -3,36 eur  
\- magic 6767 jpg no trade  
\- magic 6666 gbp 2 basket open about -11 eur dd  
\- magic 6565 eur profit 5,08 eur no trade  
\- magic 6464 chf profit 5,04 eur no trade  
\- magic 6363 cad profit 5,03 eur running 1 basket in profit 1,97  
\- magic 6262 aud no trade  
for today no stop loss encountered.  
I think this system is going well....see tomorrow 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#327](/thread/post/10864924#post10864924 "Post Permalink")

  * Mar 13, 2018 4:33am  Mar 13, 2018 4:33am 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

I changed slightly the ea: default signal set to 4.2 , 4.7 , and 5.0.  
Inserted magic number in the input so you can select it when attaching the ea.  
Added in the display near the magic number the currencies that magic is trading.  
I remain in the opinion that this system is better to be traded currency by currency with a max of 3 basket open  
a tp of 5 and sl -50 and lot size 0.01. I will dedicated a magic to every currency  
startint from 6161 aud to 6868 usd. Now for the moment 6161 is in progres by all the currencies  
but when will be sl or tp i will substitute that magic. Good testing to all. 

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [pwtceav3ff.ex4](/attachment/file/2713785?d=1520883080) 112 KB | 214 downloads 

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#328](/thread/post/10866361#post10866361 "Post Permalink")

  * Mar 13, 2018 5:05pm  Mar 13, 2018 5:05pm 

  * [ kasuncj](kasuncj)

  * | Joined Mar 2018  | Status: Trader | [3 Posts](/search?do=process&provider=Member&searchuser=660424)

> [Quoting faryne](/thread/post/10862352#post10862352 "View Quoted Post")
> 
> Disliked
> 
> {quote} Here updated version. {file}
> 
> Ignored

HI thank you EA sir but i have some problem... news filter not work how to fix it ? 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Capture.png
Size: 87 KB](/attachment/image/2714612/thumbnail?d=1520928335)](/attachment/image/2714612?d=1520928335)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#329](/thread/post/10866903#post10866903 "Post Permalink")

  * Mar 13, 2018 7:31pm  Mar 13, 2018 7:31pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar523703_1.gif) faryne](faryne)

  * | Joined Oct 2016  | Status: Trader | [93 Posts](/search?do=process&provider=Member&searchuser=523703)

> [Quoting kasuncj](/thread/post/10866361#post10866361 "View Quoted Post")
> 
> Disliked
> 
> {quote} HI thank you EA sir but i have some problem... news filter not work how to fix it ? {image}
> 
> Ignored

Did you allowed dll? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#330](/thread/post/10867832#post10867832 "Post Permalink")

  * Mar 13, 2018 10:38pm  Mar 13, 2018 10:38pm 

  * [ kasuncj](kasuncj)

  * | Joined Mar 2018  | Status: Trader | [3 Posts](/search?do=process&provider=Member&searchuser=660424)

> [Quoting faryne](/thread/post/10866903#post10866903 "View Quoted Post")
> 
> Disliked
> 
> {quote} Did you allowed dll?
> 
> Ignored

yes all are ok 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#331](/thread/post/10868537#post10868537 "Post Permalink")

  * Mar 14, 2018 12:38am  Mar 14, 2018 12:38am 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

Bad day for the system today on my side:  
I got stop loss from magic 6161 all currencies -100 euro  
stop loss from magic 6363 cad -50 eur. I am now in the office and have not the detail  
because i got mail from the Platform. when come back home i will see...  
perhaps today was nesc on cad currency... i not able for now to handle news...  
to next post.... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#332](/thread/post/10868966#post10868966 "Post Permalink")

  * Mar 14, 2018 1:53am  Mar 14, 2018 1:53am 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

here the details:  
magic 6161 stop all currncies stop loss -100 eur auto removed from chart  
magic 6262 aud profit 5.01 eur now not trading  
magic 6363 cad stop loss -50 euro autoremoved from chart  
magic 6464 chf here there is something wrong... dont know what happended has 2 open orders and -5 eur dd....  
magic 6565 eur no trade  
magic 6666 gbp 3 basket open -44 eur dd  
magic 6767 jpg no trade  
magic 6868 nzd 3 baskets open -13 eur dd  
magic 6969 usd no trade  
so... in conclusion today market very strong and system is in loss...  
i will not replacing the loosing charts and let the system go on with remaining currencies  
at the end when nothing remain i will start it from scratch.... best wishes and testing. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#333](/thread/post/10869452#post10869452 "Post Permalink")

  * Mar 14, 2018 4:31am  Mar 14, 2018 4:31am 

  * [ Namor](namor)

  * | Joined Sep 2012  | Status: Trader | [106 Posts](/search?do=process&provider=Member&searchuser=293510)

> [Quoting zoraxfx](/thread/post/10855864#post10855864 "View Quoted Post")
> 
> Disliked
> 
> i'm new in forex and i'm following this thread for me it is a risky method but with a filter it's possible de improve it...maybe ? i set the indicator with different TF H4 H1 M30 M15 M5 M1 Earlier in the day there was JPY as a weak currency we see in the pic that the JPY strenght is increasing from H4 to M1 I have bought JPY at this time with success...i don't know if that can be useful for the method create a new indicator which represents the evolution of the currency from H4 to M1 ???? {file} {image}
> 
> Ignored

I've got the best results with this system. These are today's results and my setting. 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: Image1.jpeg
Size: 303 KB](/attachment/image/2716001/thumbnail?d=1520969399)](/attachment/image/2716001?d=1520969399)   
[![Click to Enlarge

Name: Image2.jpeg
Size: 57 KB](/attachment/image/2716007/thumbnail?d=1520969460)](/attachment/image/2716007?d=1520969460)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#334](/thread/post/10869474#post10869474 "Post Permalink")

  * Mar 14, 2018 4:41am  Mar 14, 2018 4:41am 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

> [Quoting Namor](/thread/post/10869452#post10869452 "View Quoted Post")
> 
> Disliked
> 
> {quote} I've got the best results with this system. These are today's results and my setting. {image} {image}
> 
> Ignored

for today this sistem is good because of the market very strong. its good idea to start from daily and end 15m  
5m and 1m can be the fake signal. Here we dont trade for the inversion we trade for continuation of trend... every system  
can be good or bad it depends on the days..... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#335](/thread/post/10869545#post10869545 "Post Permalink")

  * Mar 14, 2018 5:02am  Mar 14, 2018 5:02am 

  * [ Namor](namor)

  * | Joined Sep 2012  | Status: Trader | [106 Posts](/search?do=process&provider=Member&searchuser=293510)

> [Quoting Ezios](/thread/post/10869474#post10869474 "View Quoted Post")
> 
> Disliked
> 
> {quote} for today this sistem is good because of the market very strong. its good idea to start from daily and end 15m 5m and 1m can be the fake signal. Here we dont trade for the inversion we trade for continuation of trend... every system can be good or bad it depends on the days.....
> 
> Ignored

You are right. The market was today very strong. But the entries were opposite the trend. And this is interested that this system was profitable opposite the strong trend. If you look at the screenshot above there were entries on GBP short. It is against the strong trend. I entered. So far so good. Let's wait how it will end. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#336](/thread/post/10870446#post10870446 "Post Permalink")

  * Mar 14, 2018 3:23pm  Mar 14, 2018 3:23pm 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

Update for this morning:  
magic 6262 aud profit 5,03 eur running 1 open basket about -1 eur dd  
magic 6464 chf 2 market orders opened about -6 eur dd  
magic 6565 eur no trade  
magic 6666 gbp got stop loss overnight -50 eur autoremoved from chart  
magic 6767 jpg no trade  
magic 6868 nza 3 open baskets about -6 eur dd  
magic 6969 usd profit 5,02 eur no trade  
we will see... its like HighLander: only one will remanin.....  
I am thinking about to add a reversal option for each currency the reversal option can work so:  
wait for the hgher signal deltaup (5.0) and buy  
wait for lower signal deltaup (4.7) and buy  
wait for lower signal deltaup (4.2) and buy  
for signals for delta down sell. in this way running all 2 settings when there is stop los from one side is profit from the other side but  
only with the higher signal... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#337](/thread/post/10870457#post10870457 "Post Permalink")

  * Mar 14, 2018 3:27pm  Mar 14, 2018 3:27pm 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

> [Quoting Namor](/thread/post/10869545#post10869545 "View Quoted Post")
> 
> Disliked
> 
> {quote} You are right. The market was today very strong. But the entries were opposite the trend. And this is interested that this system was profitable opposite the strong trend. If you look at the screenshot above there were entries on GBP short. It is against the strong trend. I entered. So far so good. Let's wait how it will end.
> 
> Ignored

Namor explain better your rules i can do ea.... we looking for a system thats profitable the majority of times...  
you look 6 chart daily 4hr 1hr 30m 15m 5m and then? whats the rule? compare? tell.... i can do ea.... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#338](/thread/post/10870572#post10870572 "Post Permalink")

  * Mar 14, 2018 4:31pm  Mar 14, 2018 4:31pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar620434_4.gif) syndicat](syndicat)

  * | Additional Username  | Joined Oct 2017 | [432 Posts](/search?do=process&provider=Member&searchuser=620434)

> [Quoting Ezios](/thread/post/10870457#post10870457 "View Quoted Post")
> 
> Disliked
> 
> {quote} Namor explain better your rules i can do ea.... we looking for a system thats profitable the majority of times... you look 6 chart daily 4hr 1hr 30m 15m 5m and then? whats the rule? compare? tell.... i can do ea....
> 
> Ignored

  
Ezios Hello! I asked you to make this indicator a month ago!!!  
  
[https://www.forexfactory.com/showthr...8#post10774128](https://www.forexfactory.com/showthread.php?p=10774128#post10774128)

"Money makes Money"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#339](/thread/post/10870938#post10870938 "Post Permalink")

  * Mar 14, 2018 6:22pm  Mar 14, 2018 6:22pm 

  * [ Namor](namor)

  * | Joined Sep 2012  | Status: Trader | [106 Posts](/search?do=process&provider=Member&searchuser=293510)

> [Quoting Ezios](/thread/post/10870457#post10870457 "View Quoted Post")
> 
> Disliked
> 
> {quote} Namor explain better your rules i can do ea.... we looking for a system thats profitable the majority of times... you look 6 chart daily 4hr 1hr 30m 15m 5m and then? whats the rule? compare? tell.... i can do ea....
> 
> Ignored

I don't have time to explain it now. I'll do it in 5-6 hours later. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#340](/thread/post/10871545#post10871545 "Post Permalink")

  * Mar 14, 2018 9:37pm  Mar 14, 2018 9:37pm 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

for now i cut off the rectangle and added the background in black next time  
i will add the signal deltaup and deltadown and the message  
. for to hae 6 indicators one near the other its better to put the message under the display

> [Quoting syndicat](/thread/post/10870572#post10870572 "View Quoted Post")
> 
> Disliked
> 
> {quote} Ezios Hello! I asked you to make this indicator a month ago!!! [https://www.forexfactory.com/showthr...8#post10774128](https://www.forexfactory.com/showthread.php?p=10774128#post10774128)
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Playing with the currencies: Gabin System
  *   * [ **Reply to Thread** ](/thread/739272-playing-with-the-currencies-gabin-system/reply#reply)

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

[Doubling up method or playing casino](/thread/4169-doubling-up-method-or-playing-casino "Hi everyone, 
  
I was thinking about one strategy which I called doubling up method but I want to share it and you to review and make...") 24 replies

[Playing the Double-Up Game?](/thread/42119-playing-the-double-up-game "It's sure a crazy full of risk system. I was just wondering if anyone ever heard of someone doing this and winning? 
  
With this system...") 40 replies

[Playing with datetime...](/thread/36065-playing-with-datetime "Hi, 
  
Setting the date, manually, in Alert 2 to todays date, why does Alert 1 return a different value than Alert 2? Even using...") 2 replies

[Playing the Breakout Trade](/thread/6189-playing-the-breakout-trade "by Abe Cofnas 
 
When markets move, particularly in Forex, they move fast. We all have witnessed breakouts and have had the occasion to...") 4 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/739272-playing-with-the-currencies-gabin-system/reply#reply)
  * Subscribe
  * [161](javascript:void\(0\);)

Attachments: Playing with the currencies: Gabin System

Tags: Playing with the currencies: Gabin System

#  [](/thread/739272-playing-with-the-currencies-gabin-system)Playing with the currencies: Gabin System 

  * 

  * [#341](/thread/post/10872143#post10872143 "Post Permalink")

  * Mar 14, 2018 11:49pm  Mar 14, 2018 11:49pm 

  * [ Namor](namor)

  * | Joined Sep 2012  | Status: Trader | [106 Posts](/search?do=process&provider=Member&searchuser=293510)

Hi Ezios,  
The first screenshot is today's results.  
The second one is opened trades.  
On the third one I explain my entry.  
On the TF1440 is CAD the weakest. In this case I'm looking for CAD to buy.  
On the TF 240 must be CAD higher than on TF 1440.  
On the TF 60 must be CAD higher or equal as on TF 240.  
On the TF 30 must be CAD higher or equal as on TF 60.  
I think it is irrelevant to use lower timeframe. I didn't enter CADCHF long because CHF was nearest to CAD on TF1440.  
I hope it is clear for you. 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: Image1.jpeg
Size: 135 KB](/attachment/image/2717441/thumbnail?d=1521038923)](/attachment/image/2717441?d=1521038923)   
[![Click to Enlarge

Name: Image2.jpeg
Size: 61 KB](/attachment/image/2717442/thumbnail?d=1521038941)](/attachment/image/2717442?d=1521038941)   
[![Click to Enlarge

Name: Image3.jpeg
Size: 45 KB](/attachment/image/2717444/thumbnail?d=1521038945)](/attachment/image/2717444?d=1521038945)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#342](/thread/post/10872278#post10872278 "Post Permalink")

  * Mar 15, 2018 12:19am  Mar 15, 2018 12:19am 

  * [ zoraxfx](zoraxfx)

  * | Joined Mar 2015  | Status: Trader | [255 Posts](/search?do=process&provider=Member&searchuser=402886)

Yes I trade like that but it's a method totally different of Gabin S.  
I'm thinking an indicator with lines would be useful for instance a curve by currency which would show the evolution of the strenght from H 4 to M15. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#343](/thread/post/10872365#post10872365 "Post Permalink")

  * Mar 15, 2018 12:36am  Mar 15, 2018 12:36am 

  * [ cvdm001](cvdm001)

  * | Joined Sep 2015  | Status: Trader | [45 Posts](/search?do=process&provider=Member&searchuser=425764)

Hi Namor,  
Thank you for explaining your strategy.  
Would you please explain what method you use for Take Profit (preferably your recommendation for manual trading).  
  
Thank you, much appreciated.  
  
Chris 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#344](/thread/post/10872497#post10872497 "Post Permalink")

  * Mar 15, 2018 1:00am  Mar 15, 2018 1:00am 

  * [ Namor](namor)

  * | Joined Sep 2012  | Status: Trader | [106 Posts](/search?do=process&provider=Member&searchuser=293510)

> [Quoting cvdm001](/thread/post/10872365#post10872365 "View Quoted Post")
> 
> Disliked
> 
> Hi Namor, Thank you for explaining your strategy. Would you please explain what method you use for Take Profit (preferably your recommendation for manual trading). Thank you, much appreciated. Chris
> 
> Ignored

My Take profit for 0.01 lot is 37 Eur. For 1 lot it is 3700.  
My Stop loss for 0.01 lot is 30. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#345](/thread/post/10872689#post10872689 "Post Permalink")

  * Mar 15, 2018 1:40am  Mar 15, 2018 1:40am 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

> [Quoting Namor](/thread/post/10872143#post10872143 "View Quoted Post")
> 
> Disliked
> 
> Hi Ezios, The first screenshot is today's results. The second one is opened trades. On the third one I explain my entry. On the TF1440 is CAD the weakest. In this case I'm looking for CAD to buy. On the TF 240 must be CAD higher than on TF 1440. On the TF 60 must be CAD higher or equal as on TF 240. On the TF 30 must be CAD higher or equal as on TF 60. I think it is irrelevant to use lower timeframe. I didn't enter CADCHF long because CHF was nearest to CAD on TF1440. I hope it is clear for you. {image} {image} {image}
> 
> Ignored

Namor but in the picture cad in tf 30 was not higher then tf 60... anyway i uderstood y our rule  
you go with the trend and not against the trend. if cad is growing y ou buy it not sell ad madscalp system 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#346](/thread/post/10872738#post10872738 "Post Permalink")

  * Mar 15, 2018 1:52am  Mar 15, 2018 1:52am 

  * [ Namor](namor)

  * | Joined Sep 2012  | Status: Trader | [106 Posts](/search?do=process&provider=Member&searchuser=293510)

> [Quoting Ezios](/thread/post/10872689#post10872689 "View Quoted Post")
> 
> Disliked
> 
> {quote} Namor but in the picture cad in tf 30 was not higher then tf 60... anyway i uderstood y our rule you go with the trend and not against the trend. if cad is growing y ou buy it not sell ad madscalp system
> 
> Ignored

It is not higher, but it is equal. I wrote it in my rules. I don't agree with you. I go against the trend. Look at the daily chart f.e. GBPCAD. 

Attached Image

![](/attachment/image/2717641?d=1521046307)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#347](/thread/post/10872760#post10872760 "Post Permalink")

  * Mar 15, 2018 2:00am  Mar 15, 2018 2:00am 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

> [Quoting Namor](/thread/post/10872738#post10872738 "View Quoted Post")
> 
> Disliked
> 
> {quote} It is not higher, but it is equal. I wrote it in my rules. I don't agree with you. I go against the trend. Look at the daily chart f.e. GBPCAD. {image}
> 
> Ignored

excuse Namor in the pictur tf 60 cad whas 5,60 and tf 30 was 5,30....  
about the trend i intend the trend of the whole basket not single pairs... here we are basketting... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#348](/thread/post/10872826#post10872826 "Post Permalink")

  * Mar 15, 2018 2:22am  Mar 15, 2018 2:22am 

  * [ Namor](namor)

  * | Joined Sep 2012  | Status: Trader | [106 Posts](/search?do=process&provider=Member&searchuser=293510)

> [Quoting Ezios](/thread/post/10872760#post10872760 "View Quoted Post")
> 
> Disliked
> 
> {quote} excuse Namor in the pictur tf 60 cad whas 5,60 and tf 30 was 5,30.... about the trend i intend the trend of the whole basket not single pairs... here we are basketting...
> 
> Ignored

I don't look at the digits, I look at the location. But maybe it would be better to look at the digits. We should try it.  
  
It is not important whether we call it with the trend or against the trend. Important is whether it works or not. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#349](/thread/post/10872969#post10872969 "Post Permalink")

  * Mar 15, 2018 3:18am  Mar 15, 2018 3:18am 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

yes Namor i agree... it must work and work not allways but more often than not working. wirh r:r about 1.1 if not so the system is failure.... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#350](/thread/post/10873196#post10873196 "Post Permalink")

  * Mar 15, 2018 4:52am  Mar 15, 2018 4:52am 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

Ok now about my test:  
magic 6262 aud got stop loss -50 eur autoremoved from chart  
magic 6464 chf take profit 5 eur not trading  
magic 6565 eur 1 bsket open about -1 eur dd  
magic 6767 jpg no trade  
magic 6868 nzd 3 basket open -9.42 eur dd  
magic 6969 usd profit 5.02 not trading  
it seem no god in this way.. but we will see next days 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#351](/thread/post/10873343#post10873343 "Post Permalink")

  * Mar 15, 2018 5:56am  Mar 15, 2018 5:56am 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

and finally added the signal deltaup deltadown and delta 1/8 to the indicator here you can set tf and period as you want 

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [cm6tf.ex4](/attachment/file/2717977?d=1521060987) 44 KB | 230 downloads 

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#352](/thread/post/10873705#post10873705 "Post Permalink")

  * Edited 12:33pm  Mar 15, 2018 9:54am | Edited 12:33pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar620434_4.gif) syndicat](syndicat)

  * | Additional Username  | Joined Oct 2017 | [432 Posts](/search?do=process&provider=Member&searchuser=620434)

> [Quoting Ezios](/thread/post/10873343#post10873343 "View Quoted Post")
> 
> Disliked
> 
> and finally added the signal deltaup deltadown and delta 1/8 to the indicator here you can set tf and period as you want {file}
> 
> Ignored

  
  
Ezios Thank you for your huge contribution to the development of this theme. I have a request, make a new indicator cm6tf like you used to do cm mod, without the big black square and with the ability to move in the right place , but if you do, an alert and a message on the screen it will be a masterpiece !!! 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: AUDUSDH1.png
Size: 44 KB](/attachment/image/2718168/thumbnail?d=1521075707)](/attachment/image/2718168?d=1521075707)   

"Money makes Money"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#353](/thread/post/10874063#post10874063 "Post Permalink")

  * Mar 15, 2018 2:46pm  Mar 15, 2018 2:46pm 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

> [Quoting syndicat](/thread/post/10873705#post10873705 "View Quoted Post")
> 
> Disliked
> 
> {quote} Ezios Thank you for your huge contribution to the development of this theme. I have a request, make a new indicator cm6tf like you used to do cm mod, without the big black square and with the ability to move in the right place , but if you do, an alert and a message on the screen it will be a masterpiece !!! {image}
> 
> Ignored

yesterday i forgot to insert the message buy sell and the mail alert. i will nsert  
input bool blacksquare true or false i will insert the message alert but under the display because of some people  
want to use this indicator 4 5 6 times one near the other. this evening when coming back from the office. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#354](/thread/post/10874069#post10874069 "Post Permalink")

  * Mar 15, 2018 2:51pm  Mar 15, 2018 2:51pm 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

about my test: yesterday nzd got another 5 eur profit and this morning too  
eur is in progres with a open basket. I will test until all basket go stop los then restart the test  
with other options. i want to add option down or up to consider only delta down or only delta up signals  
for example if you put in the string DOWN EUR the ea will trigger only buy basket when delta down signals  
if you put UP EUR the ea will trigger only sell basket when delta up signals. i want to select the best  
signals and the best basket to be in action . 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#355](/thread/post/10874340#post10874340 "Post Permalink")

  * Mar 15, 2018 4:54pm  Mar 15, 2018 4:54pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar620434_4.gif) syndicat](syndicat)

  * | Additional Username  | Joined Oct 2017 | [432 Posts](/search?do=process&provider=Member&searchuser=620434)

> [Quoting Ezios](/thread/post/10874063#post10874063 "View Quoted Post")
> 
> Disliked
> 
> {quote} yesterday i forgot to insert the message buy sell and the mail alert. i will nsert input bool blacksquare true or false i will insert the message alert but under the display because of some people want to use this indicator 4 5 6 times one near the other. this evening when coming back from the office.
> 
> Ignored

  
Ezios explain to me why you need the email alert? The signal lasts for a few seconds. When the message with the alert on the screen is much more convenient and intuitive. 

"Money makes Money"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#356](/thread/post/10874385#post10874385 "Post Permalink")

  * Mar 15, 2018 5:06pm  Mar 15, 2018 5:06pm 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

personally i dont use mail alert nor manual trading i only automatic but as someone asked me for mail alert in  
preceding indicator i want to maintain this as no problem for me to insert  

> [Quoting syndicat](/thread/post/10874340#post10874340 "View Quoted Post")
> 
> Disliked
> 
> {quote} Ezios explain to me why you need the email alert? The signal lasts for a few seconds. When the message with the alert on the screen is much more convenient and intuitive.
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#357](/thread/post/10874417#post10874417 "Post Permalink")

  * Mar 15, 2018 5:14pm  Mar 15, 2018 5:14pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar620434_4.gif) syndicat](syndicat)

  * | Additional Username  | Joined Oct 2017 | [432 Posts](/search?do=process&provider=Member&searchuser=620434)

> [Quoting Ezios](/thread/post/10874385#post10874385 "View Quoted Post")
> 
> Disliked
> 
> personally i dont use mail alert nor manual trading i only automatic but as someone asked me for mail alert in preceding indicator i want to maintain this as no problem for me to insert {quote}
> 
> Ignored

  
The message alert on the screen you can do or is it a problem for you ? 

"Money makes Money"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#358](/thread/post/10874503#post10874503 "Post Permalink")

  * Mar 15, 2018 5:33pm  Mar 15, 2018 5:33pm 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

i will do but not now this evening. now i am in the office  

> [Quoting syndicat](/thread/post/10874417#post10874417 "View Quoted Post")
> 
> Disliked
> 
> {quote} The message alert on the screen you can do or is it a problem for you ?
> 
> Ignored

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#359](/thread/post/10875775#post10875775 "Post Permalink")

  * Mar 15, 2018 10:59pm  Mar 15, 2018 10:59pm 

  * [ juraia](juraia)

  * Joined Nov 2015 | Status: A great member he understands! | [462 Posts](/search?do=process&provider=Member&searchuser=432953)

See what it looks like to me. Remove this black background, anyone can put the indicator on a black background.  
  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Capture.PNG
Size: 32 KB](/attachment/image/2719233/thumbnail?d=1521122369)](/attachment/image/2719233?d=1521122369)   

  
  
Виж как изглежда при мен. Махнете този черен фон, всеки може да си сложи индикатора на черен фон. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#360](/thread/post/10875785#post10875785 "Post Permalink")

  * Mar 15, 2018 11:01pm  Mar 15, 2018 11:01pm 

  * [ AlHaggag](alhaggag)

  * | Joined Apr 2016  | Status: Trader | [7 Posts](/search?do=process&provider=Member&searchuser=458669)

> [Quoting AlHaggag](/thread/post/10859457#post10859457 "View Quoted Post")
> 
> Disliked
> 
> Hi traders. below is my contribution to this thread please find attached two currency strength indicator that I personally use. attached in this post one is called closed cycle v1.5 . it display the major symbols reading. I Have changed the default settings from H4 to M5. and I trade the trend when the different between the symbol is grater than 500.( or as the trader prefer ) also one of the symbols must be red and the other must be blue. {image} {file} {file}
> 
> Ignored

greetings to all if you  
  
please replace the indicator mentioned in post # 305 with attached updated one.  
  
programmers can code this indicator to the experts in this thread to test trading the trend.  
  
thank you 

Attached File(s)

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [Closed cycle FI 1.6.mq4](/attachment/file/2719234?d=1521122478) 18 KB | 242 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Playing with the currencies: Gabin System
  *   * [ **Reply to Thread** ](/thread/739272-playing-with-the-currencies-gabin-system/reply#reply)

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

[Doubling up method or playing casino](/thread/4169-doubling-up-method-or-playing-casino "Hi everyone, 
  
I was thinking about one strategy which I called doubling up method but I want to share it and you to review and make...") 24 replies

[Playing the Double-Up Game?](/thread/42119-playing-the-double-up-game "It's sure a crazy full of risk system. I was just wondering if anyone ever heard of someone doing this and winning? 
  
With this system...") 40 replies

[Playing with datetime...](/thread/36065-playing-with-datetime "Hi, 
  
Setting the date, manually, in Alert 2 to todays date, why does Alert 1 return a different value than Alert 2? Even using...") 2 replies

[Playing the Breakout Trade](/thread/6189-playing-the-breakout-trade "by Abe Cofnas 
 
When markets move, particularly in Forex, they move fast. We all have witnessed breakouts and have had the occasion to...") 4 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/739272-playing-with-the-currencies-gabin-system/reply#reply)
  * Subscribe
  * [161](javascript:void\(0\);)

Attachments: Playing with the currencies: Gabin System

Tags: Playing with the currencies: Gabin System

#  [](/thread/739272-playing-with-the-currencies-gabin-system)Playing with the currencies: Gabin System 

  * 

  * [#361](/thread/post/10876106#post10876106 "Post Permalink")

  * Mar 15, 2018 11:59pm  Mar 15, 2018 11:59pm 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

yes but i like to do bool BlackSquare=false if i want i put BlackSquare=true and the game is done  

> [Quoting juraia](/thread/post/10875775#post10875775 "View Quoted Post")
> 
> Disliked
> 
> See what it looks like to me. Remove this black background, anyone can put the indicator on a black background. {image} Виж как изглежда при мен. Махнете този черен фон, всеки може да си сложи индикатора...
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#362](/thread/post/10876138#post10876138 "Post Permalink")

  * Mar 16, 2018 12:03am  Mar 16, 2018 12:03am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar620434_4.gif) syndicat](syndicat)

  * | Additional Username  | Joined Oct 2017 | [432 Posts](/search?do=process&provider=Member&searchuser=620434)

> [Quoting Ezios](/thread/post/10874063#post10874063 "View Quoted Post")
> 
> Disliked
> 
> {quote} yesterday i forgot to insert the message buy sell and the mail alert. i will nsert input bool blacksquare true or false i will insert the message alert but under the display because of some people want to use this indicator 4 5 6 times one near the other. this evening when coming back from the office.
> 
> Ignored

  
Ezios I didn't see the posts in this thread where you were asked to do a warning under the display??? Under the display is very inconvenient... 

"Money makes Money"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#363](/thread/post/10876152#post10876152 "Post Permalink")

  * Mar 16, 2018 12:07am  Mar 16, 2018 12:07am 

  * [ cvdm001](cvdm001)

  * | Joined Sep 2015  | Status: Trader | [45 Posts](/search?do=process&provider=Member&searchuser=425764)

Hi Ezios,  
I would tend to agree with syndicat, your indicator is much more useful in it's original form. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#364](/thread/post/10876168#post10876168 "Post Permalink")

  * Mar 16, 2018 12:12am  Mar 16, 2018 12:12am 

  * [ juraia](juraia)

  * Joined Nov 2015 | Status: A great member he understands! | [462 Posts](/search?do=process&provider=Member&searchuser=432953)

> [Quoting Ezios](/thread/post/10876106#post10876106 "View Quoted Post")
> 
> Disliked
> 
> yes but i like to do bool BlackSquare=false if i want i put BlackSquare=true and the game is done {quote}
> 
> Ignored

My friend, I just do not see this option BlackSquare?  

Attached Image (click to enlarge)

[![Click to Enlarge

Name: Capture.PNG
Size: 65 KB](/attachment/image/2719453/thumbnail?d=1521126765)](/attachment/image/2719453?d=1521126765)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#365](/thread/post/10876666#post10876666 "Post Permalink")

  * Mar 16, 2018 1:33am  Mar 16, 2018 1:33am 

  * [ zoraxfx](zoraxfx)

  * | Joined Mar 2015  | Status: Trader | [255 Posts](/search?do=process&provider=Member&searchuser=402886)

> [Quoting AlHaggag](/thread/post/10875785#post10875785 "View Quoted Post")
> 
> Disliked
> 
> {quote} greetings to all if you please replace the indicator mentioned in post # 305 with attached updated one. programmers can code this indicator to the experts in this thread to test trading the trend. thank you {file}
> 
> Ignored

Hi AlHaggag  
Could you explain again how you trade with this indicator ?  
Thx. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#366](/thread/post/10876757#post10876757 "Post Permalink")

  * Mar 16, 2018 1:59am  Mar 16, 2018 1:59am 

  * [ AlHaggag](alhaggag)

  * | Joined Apr 2016  | Status: Trader | [7 Posts](/search?do=process&provider=Member&searchuser=458669)

> [Quoting zoraxfx](/thread/post/10876666#post10876666 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi AlHaggag Could you explain again how you trade with this indicator ? Thx.
> 
> Ignored

please go back to the picture in post #311 page 16 for more explanation.  
  
and if its not understood. I will explain again. ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#367](/thread/post/10876988#post10876988 "Post Permalink")

  * Mar 16, 2018 3:11am  Mar 16, 2018 3:11am 

  * [ Groffobonchi](groffobonchi)

  * | Joined Mar 2018  | Status: Trader | [6 Posts](/search?do=process&provider=Member&searchuser=659957)

good evening friends, it does not work me again Jellyfish, empty screen, someone has my same problem? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#368](/thread/post/10876992#post10876992 "Post Permalink")

  * Mar 16, 2018 3:14am  Mar 16, 2018 3:14am 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

updated cm6tf indicator: put deltaup-down-18 message and signals where in the other indicator  
\- put background as false in the setting if you want turn on true.  
. i put the indicator in center but you can move where you want by setting xAnchor and yAnchor  
Closed the discussion about indicator. Who want manual trade use this or cm_mod_v1 its the same a part from setting tf and period. 

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [cm6tf.ex4](/attachment/file/2719841?d=1521137671) 48 KB | 211 downloads 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#369](/thread/post/10877093#post10877093 "Post Permalink")

  * Mar 16, 2018 3:44am  Mar 16, 2018 3:44am 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

Now about my test:  
magic 6767 jpg no trade  
magic 6565 eur 1 basket opened about -4 eur dd  
magic 6464 chf no trade  
magic 6969 usd profit 5,06 eur no trade  
magic 6868 nzd profit 10,21 eur no trade.  
see tomorrow... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#370](/thread/post/10877127#post10877127 "Post Permalink")

  * Mar 16, 2018 3:59am  Mar 16, 2018 3:59am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar556193_1.gif) Fatso](fatso)

  * | Joined Feb 2017  | Status: Trader | [111 Posts](/search?do=process&provider=Member&searchuser=556193)

> [Quoting Ezios](/thread/post/10876992#post10876992 "View Quoted Post")
> 
> Disliked
> 
> updated cm6tf indicator: put deltaup-down-18 message and signals where in the other indicator - put background as false in the setting if you want turn on true. . i put the indicator in center but you can move where you want by setting xAnchor and yAnchor Closed the discussion about indicator. Who want manual trade use this or cm_mod_v1 its the same a part from setting tf and period. {file}
> 
> Ignored

Hi Ezios. I am one of those who trade manual with the indicator using email alert. The updated indicator is not sending emails even when I choose email to "true". 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#371](/thread/post/10877197#post10877197 "Post Permalink")

  * Mar 16, 2018 4:17am  Mar 16, 2018 4:17am 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

> [Quoting Fatso](/thread/post/10877127#post10877127 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi Ezios. I am one of those who trade manual with the indicator using email alert. The updated indicator is not sending emails even when I choose email to "true".
> 
> Ignored

i will try this option... not tried. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#372](/thread/post/10877238#post10877238 "Post Permalink")

  * Mar 16, 2018 4:31am  Mar 16, 2018 4:31am 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

> [Quoting Fatso](/thread/post/10877127#post10877127 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi Ezios. I am one of those who trade manual with the indicator using email alert. The updated indicator is not sending emails even when I choose email to "true".
> 
> Ignored

ok try now it works... 

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [cm6tf.ex4](/attachment/file/2719967?d=1521142279) 48 KB | 279 downloads 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#373](/thread/post/10877348#post10877348 "Post Permalink")

  * Mar 16, 2018 5:01am  Mar 16, 2018 5:01am 

  * [ juraia](juraia)

  * Joined Nov 2015 | Status: A great member he understands! | [462 Posts](/search?do=process&provider=Member&searchuser=432953)

> [Quoting Ezios](/thread/post/10876992#post10876992 "View Quoted Post")
> 
> Disliked
> 
> updated cm6tf indicator: put deltaup-down-18 message and signals where in the other indicator - put background as false in the setting if you want turn on true. . i put the indicator in center but you can move where you want by setting xAnchor and yAnchor Closed the discussion about indicator. Who want manual trade use this or cm_mod_v1 its the same a part from setting tf and period. {file}
> 
> Ignored

Bravo, it's OK! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#374](/thread/post/10878349#post10878349 "Post Permalink")

  * Mar 16, 2018 3:29pm  Mar 16, 2018 3:29pm 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

This morning my test: nothing happend overnight.  
magic 6565 eur still running 1 basket about -2 eur dd  
magic 6464 chf no trade  
magic 6969 usd running 1 basket about +2 eur profit  
magic 6868 nzd running 3 baskets about -24 eur dd.  
Next week I will begin another test only on DOWN signals with these parameters:  
sl -50 tp +5 maxbasket 3 dailytarget 25 in thefollowing order:  
magic 5151 down aud  
magic 5252 down cad  
magic 5353 down chf  
magic 5454 down eur  
magic 5555 down gbp  
magic 5656 down jpg  
magic 5757 down nzd  
magic 5858 down usd  
i will buy the weakest currency when its the signal.  
i wanted to put sl and tp 1:1 but for now i try this setting.  
on free time saturday and sunday i will add the option to ea. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#375](/thread/post/10880696#post10880696 "Post Permalink")

  * Mar 17, 2018 1:44am  Mar 17, 2018 1:44am 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

results for the test today tll now:  
magic 6868 nzd got stop loss -50 eur autoremoved from chart  
magic 6565 eur take profit 5,01 eur no trade  
magic 6464 chf no trade  
magic 6969 usd 5 eur take profit running 1 basket +1,43 eur profit  
*************for this week eur and usd was the best profit. we will see next week. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#376](/thread/post/10881146#post10881146 "Post Permalink")

  * Mar 17, 2018 4:56am  Mar 17, 2018 4:56am 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

Sarted nes tests:from magic 5151 to 5858 with the down option down aud to down usd  
we will see next week how it goes. i will attach also 6161 eur and 6969 usd with remaining ootb setting 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: DOWN.png
Size: 30 KB](/attachment/image/2722068/thumbnail?d=1521230141)](/attachment/image/2722068?d=1521230141)   

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [pwtceav3ff.ex4](/attachment/file/2722070?d=1521230170) 113 KB | 237 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#377](/thread/post/10884757#post10884757 "Post Permalink")

  * Mar 19, 2018 2:19pm  Mar 19, 2018 2:19pm 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

Starting this week's test with bad news:  
magic 5151 down aud got stop loss overnight -50 eur autoremoved from chart  
magic 5757 down nzd has 2 baskets open and dd about -5 eur  
magic 6161 eur 1 basket open about +4 eur profit  
All the other no trade.  
I have replaced magic 5151 by the default setting trading all signals. I want to make the point of the situation.  
I am thinking about to do a template of 5 indicators d1 h4 h1 m30 m15 and doing an ea to test the Namor system  
for trading from gmt 8 to 17 or 7 to 18 and max 3 basket open sl -30 tp +30. We will see if i will be able and what the results.  
For now good testing to all 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#378](/thread/post/10887213#post10887213 "Post Permalink")

  * Mar 20, 2018 2:10am  Mar 20, 2018 2:10am 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

update for test today:  
magic 6161 eur got 10 eur profit no trade  
magic 6969 usd no trade  
magic 5151 default setting got stop los -100 eur autoremove from chart tomorrow i will attach the same  
magic 5252 down cad no trade  
magic 5353 down chf no trade  
magic 5454 down eur got 5 eur profit no trade now  
magic 5555 down gbp no trade  
magic 5656 down jpg no trade  
magic 5757 down nzd 5.84 eur profit no trading now  
magic 5858 down usd no trade.  
i am thinking this system is going well only for eur and usd . we will see next weeks... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#379](/thread/post/10888549#post10888549 "Post Permalink")

  * Mar 20, 2018 2:29pm  Mar 20, 2018 2:29pm 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

Good morning, at the moment when i wake up as i have the very short sleeping time  
I go to see how the platform is going. This night the market was very quiet and the situation is:  
\- magic 5151 all default 3 basket opened -6.44 eur dd  
\- magic 5757 down nzd has opened 2 basket ad is about -9 eur dd  
all the remaining are doing nothing.  
Another idea that i had: to put an hedging funcion in each pair and a take profit in each pair.  
I explain: when each pair reach x pip take profit we close the pair and, when each pair reach  
x pip of loss, we hedge the pair with the opposite opeeration and wait for break even.  
To me its not a bad idea in this system. For the take profit no problem opening the order with a take profit in the  
platform. For the virtual stop loss i have to think how to code. Perhaps testing the Bid of the symbol and when the Bid is at a certain  
lwevel open the opposite operation. I will think about it....  
Good day to all. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#380](/thread/post/10891515#post10891515 "Post Permalink")

  * Mar 21, 2018 5:21am  Mar 21, 2018 5:21am 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

Good evening,  
today the system went very good:  
magic 6161 eur has opened 2 baskets about 1,80 eur in profit  
magic 6969 usd got 10 eur profit no trade now  
magic 5151 all default got 30 eur profit and running now 1 backet about 50 cent in profit  
magic 5252 down cad no trade  
magic 5353 down chf 5,13 eur profit no trade now  
magic 5454 down eur 5,07 eur profit running 1 basket now few cent in profit  
magic 5555 down gbp no trade  
magic 5656 down jpy 5,06 eur profit now not trading  
magic 5757 down nzd 2 basket opened -33,33 dd  
magic 5858 down usd 5 eur profit no trading now  
as in the life all the strong will survive and will go alive (perhaps).... good testing.... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Playing with the currencies: Gabin System
  *   * [ **Reply to Thread** ](/thread/739272-playing-with-the-currencies-gabin-system/reply#reply)

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

[Doubling up method or playing casino](/thread/4169-doubling-up-method-or-playing-casino "Hi everyone, 
  
I was thinking about one strategy which I called doubling up method but I want to share it and you to review and make...") 24 replies

[Playing the Double-Up Game?](/thread/42119-playing-the-double-up-game "It's sure a crazy full of risk system. I was just wondering if anyone ever heard of someone doing this and winning? 
  
With this system...") 40 replies

[Playing with datetime...](/thread/36065-playing-with-datetime "Hi, 
  
Setting the date, manually, in Alert 2 to todays date, why does Alert 1 return a different value than Alert 2? Even using...") 2 replies

[Playing the Breakout Trade](/thread/6189-playing-the-breakout-trade "by Abe Cofnas 
 
When markets move, particularly in Forex, they move fast. We all have witnessed breakouts and have had the occasion to...") 4 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/739272-playing-with-the-currencies-gabin-system/reply#reply)
  * Subscribe
  * [161](javascript:void\(0\);)

Attachments: Playing with the currencies: Gabin System

Tags: Playing with the currencies: Gabin System

#  [](/thread/739272-playing-with-the-currencies-gabin-system)Playing with the currencies: Gabin System 

  * 

  * [#381](/thread/post/10892486#post10892486 "Post Permalink")

  * Mar 21, 2018 2:26pm  Mar 21, 2018 2:26pm 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

Only to update the results of yesterday: magic 5757 down nzd got stop los -50 eur  
other day other run. It's very boring to test a system but i have to do it. If someone is not interested on my tests  
tell me and i will stop to post my results. Good day to all. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#382](/thread/post/10895809#post10895809 "Post Permalink")

  * Mar 22, 2018 5:18am  Mar 22, 2018 5:18am 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

Situation of the system today:  
\- magic 6161 eur 2 basket open about 1,51 eur profit  
\- magic 6969 usd 3 basket opened , about -86 dd  
\- magic 5151 all default hit +53,62 profit . here daily target is 50 so no more trades.  
\- magic 5252 down cad no trade.  
\- magic 5353 down chf no trade.  
\- magic 5454 down eur 5,24 profit no trade  
\- magic 5555 down gbp no trade  
\- magic 5656 down jpy no trade  
\- magic 5858 down usd hit stop loss -50 autoremoved from chart. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#383](/thread/post/10898874#post10898874 "Post Permalink")

  * Mar 23, 2018 12:20am  Mar 23, 2018 12:20am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar620434_4.gif) syndicat](syndicat)

  * | Additional Username  | Joined Oct 2017 | [432 Posts](/search?do=process&provider=Member&searchuser=620434)

> [Quoting Ezios](/thread/post/10895809#post10895809 "View Quoted Post")
> 
> Disliked
> 
> Situation of the system today: - magic 6161 eur 2 basket open about 1,51 eur profit - magic 6969 usd 3 basket opened , about -86 dd - magic 5151 all default hit +53,62 profit . here daily target is 50 so no more trades. - magic 5252 down cad no trade. - magic 5353 down chf no trade. - magic 5454 down eur 5,24 profit no trade - magic 5555 down gbp no trade - magic 5656 down jpy no trade - magic 5858 down usd hit stop loss -50 autoremoved from chart.
> 
> Ignored

  
  
hi Ezios! You can in pwtceav3ff Advisor.ex4 to replace the indicator cm6tf.ex4 instead of cm_mod_v1.ex4 ? 

"Money makes Money"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#384](/thread/post/10899333#post10899333 "Post Permalink")

  * Mar 23, 2018 1:54am  Mar 23, 2018 1:54am 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

In next version i will add in the inputs tf and period so you can change them. no need to replace indicator its the same.  
It seems to me the ea already good with this tf. Today the default setting take profit 50 eur daily target.  
the stop loss occurs only once a week and so.... enyway i can to adjust it... 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#385](/thread/post/10899361#post10899361 "Post Permalink")

  * Mar 23, 2018 2:05am  Mar 23, 2018 2:05am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar620434_4.gif) syndicat](syndicat)

  * | Additional Username  | Joined Oct 2017 | [432 Posts](/search?do=process&provider=Member&searchuser=620434)

> [Quoting Ezios](/thread/post/10899333#post10899333 "View Quoted Post")
> 
> Disliked
> 
> In next version i will add in the inputs tf and period so you can change them. no need to replace indicator its the same. It seems to me the ea already good with this tf. Today the default setting take profit 50 eur daily target. the stop loss occurs only once a week and so.... enyway i can to adjust it...
> 
> Ignored

Quite well! When do you plan on releasing a new version? 

"Money makes Money"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#386](/thread/post/10899888#post10899888 "Post Permalink")

  * Mar 23, 2018 5:27am  Mar 23, 2018 5:27am 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

results for today:  
magic 6161 eur default setting running 2 baskets about be  
magic 5151 all default hit 54,65 profit now daily target is 50 so now no trading.  
magic 5252 down cad no trade  
magic 5353 down chf no trade  
magic 5454 down eur trading 1 basket about be  
magic 5555 down gbp 5 eur profit now no trade  
magic 5656 down jpy no trade  
magic 6969 usd got stop loss -100 auto removed from chart.  
New version:  
\- added in the display global tp sl  
\- added input bool usecustomtf default false if you turn to true you can change tf and period  
if you change tf and period but leave this to false it will have no effect.  
\- when you set usecustomtf to true the actual tf and period will be displayed.  
\- other internal changes in opening and closing orders functions to handle in better way platform errors.  
good testing. 

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [pwtceav3ff.ex4](/attachment/file/2730787?d=1521750466) 145 KB | 172 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#387](/thread/post/10902483#post10902483 "Post Permalink")

  * Mar 23, 2018 10:59pm  Mar 23, 2018 10:59pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar620434_4.gif) syndicat](syndicat)

  * | Additional Username  | Joined Oct 2017 | [432 Posts](/search?do=process&provider=Member&searchuser=620434)

> [Quoting Ezios](/thread/post/10899888#post10899888 "View Quoted Post")
> 
> Disliked
> 
> results for today: magic 6161 eur default setting running 2 baskets about be magic 5151 all default hit 54,65 profit now daily target is 50 so now no trading. magic 5252 down cad no trade magic 5353 down chf no trade magic 5454 down eur trading 1 basket about be magic 5555 down gbp 5 eur profit now no trade magic 5656 down jpy no trade magic 6969 usd got stop loss -100 auto removed from chart. New version: - added in the display global tp sl - added input bool usecustomtf default false if you turn to true you can change tf and period if you change...
> 
> Ignored

  
Ezios will this version work on a real account? Are there any restrictions on the period of use?   
I want to try to put on a real account and test. 

"Money makes Money"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#388](/thread/post/10902531#post10902531 "Post Permalink")

  * Mar 23, 2018 11:07pm  Mar 23, 2018 11:07pm 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

this ea works only in demo account. its only for test.  

> [Quoting syndicat](/thread/post/10902483#post10902483 "View Quoted Post")
> 
> Disliked
> 
> {quote} Ezios will this version work on a real account? Are there any restrictions on the period of use? I want to try to put on a real account and test.
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#389](/thread/post/10902556#post10902556 "Post Permalink")

  * Mar 23, 2018 11:13pm  Mar 23, 2018 11:13pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar620434_4.gif) syndicat](syndicat)

  * | Additional Username  | Joined Oct 2017 | [432 Posts](/search?do=process&provider=Member&searchuser=620434)

> [Quoting Ezios](/thread/post/10902531#post10902531 "View Quoted Post")
> 
> Disliked
> 
> this ea works only in demo account. its only for test. {quote}
> 
> Ignored

  
Can you give me the version for a real account? 

"Money makes Money"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#390](/thread/post/10903188#post10903188 "Post Permalink")

  * Mar 24, 2018 1:44am  Mar 24, 2018 1:44am 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

> [Quoting syndicat](/thread/post/10902556#post10902556 "View Quoted Post")
> 
> Disliked
> 
> {quote} Can you give me the version for a real account?
> 
> Ignored

there are still bugs in this ea.... anyway if y ou want to test y our live account  
pm me with your email adres and number of account and i will send to you  
a version with valildity 1 week. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#391](/thread/post/10903193#post10903193 "Post Permalink")

  * Mar 24, 2018 1:45am  Mar 24, 2018 1:45am 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

k guys... the profit of the ea for this day was about 20 euro for magic 5151 running all devault  
and other 10 in other 2 magic but... as i had to restart my plaftorm rhe ea did not remember the profit...  
its a little bug that i will fix next version... good testing to all. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#392](/thread/post/10903456#post10903456 "Post Permalink")

  * Edited 3:31am  Mar 24, 2018 3:09am | Edited 3:31am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar620434_4.gif) syndicat](syndicat)

  * | Additional Username  | Joined Oct 2017 | [432 Posts](/search?do=process&provider=Member&searchuser=620434)

> [Quoting Ezios](/thread/post/10903188#post10903188 "View Quoted Post")
> 
> Disliked
> 
> {quote} there are still bugs in this ea.... anyway if y ou want to test y our live account pm me with your email adres and number of account and i will send to you a version with valildity 1 week.
> 
> Ignored

  
only a week... it's ridiculous how you can test the EA in one week??? If you want to sell it, you need to open a branch in the commercial section. This branch was created to improve this strategy , so it is better to post a version here with a deadline of at least one month!!! Traders will test and make suggestions for improvements!!!  
  
For the sake of interest, compare the indicator readings on a demo account and on a real account. And you'd be surprised what the difference is in the testimony !!! 

"Money makes Money"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#393](/thread/post/10903595#post10903595 "Post Permalink")

  * Mar 24, 2018 4:13am  Mar 24, 2018 4:13am 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

> [Quoting syndicat](/thread/post/10903456#post10903456 "View Quoted Post")
> 
> Disliked
> 
> {quote} only a week... it's ridiculous how you can test the EA in one week??? If you want to sell it, you need to open a branch in the commercial section. This branch was created to improve this strategy , so it is better to post a version here with a deadline of at least one month!!! Traders will test and make suggestions for improvements!!! For the sake of interest, compare the indicator readings on a demo account and on a real account. And you'd be surprised what the difference is in the testimony !!!
> 
> Ignored

for now i dont want to sell nothing... only testing... neither me put this on my live account.  
to me a week ot a month for testing its the same...theproblem with the real account is real money and real people that wont  
to sell the work of others... so.. if you want 1 month i give 1 month. Me and faryne we are programmers and we protect oru work  
if you permit and also if you dont permit ok? now stop this discussion from me. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#394](/thread/post/10903699#post10903699 "Post Permalink")

  * Edited 5:12am  Mar 24, 2018 4:58am | Edited 5:12am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar620434_4.gif) syndicat](syndicat)

  * | Additional Username  | Joined Oct 2017 | [432 Posts](/search?do=process&provider=Member&searchuser=620434)

> [Quoting Ezios](/thread/post/10903595#post10903595 "View Quoted Post")
> 
> Disliked
> 
> {quote} for now i dont want to sell nothing... only testing... neither me put this on my live account. to me a week ot a month for testing its the same...theproblem with the real account is real money and real people that wont to sell the work of others... so.. if you want 1 month i give 1 month. Me and faryne we are programmers and we protect oru work if you permit and also if you dont permit ok? now stop this discussion from me.
> 
> Ignored

I fully support you in your desire to protect your adviser.  
I suggest you make an Advisor with a limit of one month,  
with the ability to test both on a demo account and on a real account.  
Trading on a live account is very different from trading on a demo account  
where not considered slippage rates, spread widening, requotes, etc.  
The more people start the EA tests the more accurate the results and  
faster to find out all the errors in the EA.  
If you want to test one, I won't bother you...  
And advice for those who are testing:  
For a more accurate reading of the indicator, you need to install a script to download the history  
on currency pairs. 

Attached File(s)

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [LoadHistory-1 script.mq4](/attachment/file/2732395?d=1521835849) 8 KB | 220 downloads 

"Money makes Money"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#395](/thread/post/10903737#post10903737 "Post Permalink")

  * Mar 24, 2018 5:14am  Mar 24, 2018 5:14am 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

> [Quoting syndicat](/thread/post/10903699#post10903699 "View Quoted Post")
> 
> Disliked
> 
> {quote} I fully support you in your desire to protect your adviser. I suggest you make an Advisor with a limit of one month, with the ability to test both on a demo account and on a real account. Trading on a live account is very different from trading on a demo account where not considered slippage rates, spread widening, requotes, etc. The more people start the EA tests the more accurate the results and faster to find out all the errors in the EA. If you want to test one, I won't bother you... And advice for those who are testing: For a more accurate...
> 
> Ignored

I will not put public version for real for all. if someone want 1 month have to pm to me giving his account number. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#396](/thread/post/10903933#post10903933 "Post Permalink")

  * Mar 24, 2018 7:21am  Mar 24, 2018 7:21am 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

Bugfixed the ea: now go in the history and look for daily profit for any magic.  
So i can give the situation of today:  
\- magic 5151 all default made 19,75 eur profit now no trading  
\- magic 6161 eur 2 basket opened about -4 dd  
\- magic 5252 down cad no trade  
\- magic 5353 down chf no trade  
\- magic 5454 down eur no trade  
-magic 5555 down gbp no trade  
-magic 5656 down jpy 5,05 profit no trade  
good weekend to all 

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [pwtceav3ff.ex4](/attachment/file/2732483?d=1521843701) 146 KB | 186 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#397](/thread/post/10904849#post10904849 "Post Permalink")

  * Mar 25, 2018 1:15am  Mar 25, 2018 1:15am 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

Another thing to fix in this ea is that it executes orders without stop loss and take profit.  
It can be very risky if the platform disconnect for tecnical problems and you dont see it and  
the virtual stop loss or take profit cannot be tested by the ea so.... it is necessary to add a  
guard stop loss and take profit. I will think about it also if i all days go to control the account and theeas but...  
its better to put stop loss and take profit in the broker platform. I will think about it in new version. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#398](/thread/post/10906531#post10906531 "Post Permalink")

  * Mar 26, 2018 7:41am  Mar 26, 2018 7:41am 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

New update: i added the ability to put a guard stop loss / take profit for all pairs  
The option is set to false by default if you turn to true it will put a 100 pip sl and tp guard in every  
trade opened or if the magic is empty when opening a trade it will modify sl and tp according to your setting.  
If the option is set to false (default) sl and tp are ignored.  
When you turn the option to true the sl and tp value are displayed.  
Added new magic number 8181 whith all default and the sl/tp option set to true and 100 pips. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: 8181.png
Size: 33 KB](/attachment/image/2733663/thumbnail?d=1522017642)](/attachment/image/2733663?d=1522017642)   

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [pwtceav3ff.ex4](/attachment/file/2733664?d=1522017709) 149 KB | 181 downloads 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#399](/thread/post/10908952#post10908952 "Post Permalink")

  * Mar 27, 2018 12:51am  Mar 27, 2018 12:51am 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

Today catastrofic for the system:  
magic 5151 all default got stop los -104,52  
magic 8181 all default but with 100 pip sl tp got stoploss -100,99  
magic 5656 down jpy stop los -51,92  
magic 5252 down cad trading 1 basket about be  
magic 5353 down chf no trade  
magic 5454 down eur no trade  
magic 5555 down gbp no trade  
magic 6161 trading eur 4 basket opened abiut -4 dd.  
i will attach new magic 8181 with standard setting but 10 pip sl and tp for pair. will see how it does.  
no time for go live for now..........continuing the test......... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#400](/thread/post/10909650#post10909650 "Post Permalink")

  * Mar 27, 2018 4:39am  Mar 27, 2018 4:39am 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

last news: magic 5252 down cad got 5 eur profit  
magic 8181 bought a jpy basket and had stoploss in all 7 pairs -6,55 sl.  
tomorrow i will attach new 5151 default setting and will continue 8181 magic.  
applying sl of 10 pips per pair we loose soon or win soon.... it can be a choice.... testing....suer of nothing. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Playing with the currencies: Gabin System
  *   * [ **Reply to Thread** ](/thread/739272-playing-with-the-currencies-gabin-system/reply#reply)

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

[Doubling up method or playing casino](/thread/4169-doubling-up-method-or-playing-casino "Hi everyone, 
  
I was thinking about one strategy which I called doubling up method but I want to share it and you to review and make...") 24 replies

[Playing the Double-Up Game?](/thread/42119-playing-the-double-up-game "It's sure a crazy full of risk system. I was just wondering if anyone ever heard of someone doing this and winning? 
  
With this system...") 40 replies

[Playing with datetime...](/thread/36065-playing-with-datetime "Hi, 
  
Setting the date, manually, in Alert 2 to todays date, why does Alert 1 return a different value than Alert 2? Even using...") 2 replies

[Playing the Breakout Trade](/thread/6189-playing-the-breakout-trade "by Abe Cofnas 
 
When markets move, particularly in Forex, they move fast. We all have witnessed breakouts and have had the occasion to...") 4 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/739272-playing-with-the-currencies-gabin-system/reply#reply)
  * Subscribe
  * [161](javascript:void\(0\);)

Attachments: Playing with the currencies: Gabin System

Tags: Playing with the currencies: Gabin System

#  [](/thread/739272-playing-with-the-currencies-gabin-system)Playing with the currencies: Gabin System 

  * 

  * [#401](/thread/post/10913092#post10913092 "Post Permalink")

  * Mar 28, 2018 12:38am  Mar 28, 2018 12:38am 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

system today:  
magic 8181 all default but sl 10 tp 10 for pair is in profit +5,67 now no trading  
magic 5151 all default is in profit 40,20 now not trading  
magic 6161 trading eur 3 basket open about -1 dd  
magic 5252 down cad no trade remove from chart no more interest  
magic 5353 down chf no trade remove from card no more interest  
magic 5454 down eur no trade remove from chart no more interest  
magic 5555 down gbp got stop loss -50,86 auto removed from chart.  
8181 its the most conservative its slight profit but also slight loss.....  
also 5151 is good for all week is going well... we will see this week. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#402](/thread/post/10913154#post10913154 "Post Permalink")

  * Mar 28, 2018 12:50am  Mar 28, 2018 12:50am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar620434_4.gif) syndicat](syndicat)

  * | Additional Username  | Joined Oct 2017 | [432 Posts](/search?do=process&provider=Member&searchuser=620434)

Hi [ Ezios](https://www.forexfactory.com/ezios)! if I open the first set and the signal for the first set again on the next candle, will the EA open another set? 

"Money makes Money"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#403](/thread/post/10913265#post10913265 "Post Permalink")

  * Mar 28, 2018 1:12am  Mar 28, 2018 1:12am 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

> [Quoting syndicat](/thread/post/10913154#post10913154 "View Quoted Post")
> 
> Disliked
> 
> Hi [ Ezios](https://www.forexfactory.com/ezios)! if I open the first set and the signal for the first set again on the next candle, will the EA open another set?
> 
> Ignored

no this ea is ontimer not see the candle. every second the ea goest to look for signal.  
if there is signal first step open a basket and then wait for signal 2 step.  
no more basket opened for 1 step when signal 2 step is it open another basket and wait for 3 step so.....  
if you are 2 signals for 1 step eur and use it take the first. no more. usd is out.all mixed. only if you set only a currency  
then the ea trade all signal in what yu want but tha candle its no matter. the tf and the period you can set.  
if you set 4h and period 3 the signal is computer on 4h period 3. its the indicator cm6tf. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#404](/thread/post/10917467#post10917467 "Post Permalink")

  * Mar 29, 2018 1:24am  Mar 29, 2018 1:24am 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

I noticed most stop loss happens on monday . I think because when the market opens  
there are the gaps and too strong signals and fake signals so... i decide to put a switch to not trade on monday.  
It is set by default on false so the ea will not trade on monday (not yet tested but its easy to do).  
The same i did for trade on friday because i dont want to leave opened trades before che close of the market.  
In demo all is good but in real... the thing is different.  
so, this switch too is set to false so the ea will not trade on friday by default.  
Another important change: add a digit in the display and in the indicator's signal.  
Remember that 4,2 is 4.20 2,7 is 4,70 and so when you see the signal you cen see the exact signal.  
I wanted to add also trailing and be setting but i wll test next version.  
good testing. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: new.png
Size: 54 KB](/attachment/image/2738642/thumbnail?d=1522254217)](/attachment/image/2738642?d=1522254217)   

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [pwtceav3ff.ex4](/attachment/file/2738646?d=1522254288) 149 KB | 197 downloads 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#405](/thread/post/10918226#post10918226 "Post Permalink")

  * Mar 29, 2018 5:27am  Mar 29, 2018 5:27am 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

Ok now update from the test:  
today I made an error: i wanted to make magic 8181 with stop loss and take profit of 10 but  
I leaved to 100 and so 8181 has behaving as the default setting and made profit 30 eur  
now is running with 2 basket opened and about -16 dd.  
nagig 6161 trading eur is about +6 profit with 3 basket opened  
magic 5151 all default is 2 basket opened and about -17 dd.  
we will see tomorrow. i will attack new 9191 with standard settings but 10 eur guard sl tp.  
good testing. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#406](/thread/post/10919059#post10919059 "Post Permalink")

  * Mar 29, 2018 2:01pm  Mar 29, 2018 2:01pm 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

Today yen very strong. I imagine there will be stop loss ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) still demoing...... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#407](/thread/post/10919899#post10919899 "Post Permalink")

  * Mar 29, 2018 7:26pm  Mar 29, 2018 7:26pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar620434_4.gif) syndicat](syndicat)

  * | Additional Username  | Joined Oct 2017 | [432 Posts](/search?do=process&provider=Member&searchuser=620434)

[Ezios](https://www.forexfactory.com/ezios) hi! After rebooting the MT4 terminal, the set lot is reset to 0.01. Do so as specified in the settings. 

"Money makes Money"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#408](/thread/post/10919996#post10919996 "Post Permalink")

  * Mar 29, 2018 8:03pm  Mar 29, 2018 8:03pm 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

i will put lot in the setting as magic. have to fix some other things  
want to insert also trailing stops.  

> [Quoting syndicat](/thread/post/10919899#post10919899 "View Quoted Post")
> 
> Disliked
> 
> [Ezios](https://www.forexfactory.com/ezios) hi! After rebooting the MT4 terminal, the set lot is reset to 0.01. Do so as specified in the settings.
> 
> Ignored

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#409](/thread/post/10921515#post10921515 "Post Permalink")

  * Mar 30, 2018 3:07am  Mar 30, 2018 3:07am 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

Today got 2 stop loss in magic 5151 all default and 8181 all default with guard sl tp 100 pips.  
about -89 eur each stop loss . Magic 9191 all default but sl tp of 10 pips got profit 4,55 eur.  
It's small profit with lot 0.01 but if you put lot 0.10 become good profit for day.  
magic 6161 all default but trading only eur did not trade.  
I fixed a bug that let the ea to open too many orders when the terminal was rebooted.  
I put the lotsize in the setting so as one can change it when attaching the ea.  
I will leave magic 9191 standard setting with tp sl 10 pips but lotsize 0.10.  
I will put magic 6161 with standard setting but lotsize 0.10 and tp 20 and sl 10. we will see...  
It is not clear for me if putting trailing stops and breakeven is an advantage or not.  
Perhaps it's better and more easy to leave fixed sl and tp . If the trades are good the system will win.  
Dont wanted to trade on friday but i am too curious to see the results for tomorrow.  
Good testing. 

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [pwtceav3ff.ex4](/attachment/file/2740677?d=1522346875) 156 KB | 202 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#410](/thread/post/10922277#post10922277 "Post Permalink")

  * Mar 30, 2018 12:53pm  Mar 30, 2018 12:53pm 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

This night the test did not go as i exected too many sl and no take profit because i leaved  
the global profit to 10 euro but i have to put to 100 because i m ultiplied lotsize by 10.  
i will adjust now to 100. Huge loss to the account. next week i will change the demo account to another  
more capitalized.... tests are tests.... money is no true money ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

Attached Image (click to enlarge)

[![Click to Enlarge

Name: nogod.png
Size: 32 KB](/attachment/image/2741030/thumbnail?d=1522381992)](/attachment/image/2741030?d=1522381992)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#411](/thread/post/10922283#post10922283 "Post Permalink")

  * Mar 30, 2018 1:05pm  Mar 30, 2018 1:05pm 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

for the day i will leave to run only this setting. we will see.... 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: good.png
Size: 32 KB](/attachment/image/2741033/thumbnail?d=1522382692)](/attachment/image/2741033?d=1522382692)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#412](/thread/post/10923353#post10923353 "Post Permalink")

  * Mar 31, 2018 12:34am  Mar 31, 2018 12:34am 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

From next week I will start the test of this system with the rules:  
no trade overnight only from gmt 6 to gmt 21 -2 hours from start londeon and +2 hour from end london.  
i willl put oly 2 magic: 6161 standard set but 100 pip sl and 100 tp for guard no trade on monday ad friday  
and time filter as i told.  
Magic 9191 with lot 0.1 and all the other values multiplied by 10 and sl and tp 10:10 pips.  
and time filter as i told. This is the test thet tells if system is profitable or not.  
Good luck to all and to next week. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#413](/thread/post/10923578#post10923578 "Post Permalink")

  * Mar 31, 2018 2:26am  Mar 31, 2018 2:26am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar409665_1.gif) Fancysegs](fancysegs)

  * | Joined Apr 2015  | Status: Trader | [52 Posts](/search?do=process&provider=Member&searchuser=409665)

EZIOS Please reply to my Private Message 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#414](/thread/post/10931259#post10931259 "Post Permalink")

  * Apr 4, 2018 2:53am  Apr 4, 2018 2:53am 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

catastrofic today... 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: catastrofe6161.png
Size: 46 KB](/attachment/image/2745406/thumbnail?d=1522777975)](/attachment/image/2745406?d=1522777975)   
[![Click to Enlarge

Name: catastrofe9191.png
Size: 46 KB](/attachment/image/2745408/thumbnail?d=1522778005)](/attachment/image/2745408?d=1522778005)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#415](/thread/post/10931375#post10931375 "Post Permalink")

  * Apr 4, 2018 3:36am  Apr 4, 2018 3:36am 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

i am working to new ea... when its ready for the test i will post it...  
complete different system... based on trend.... 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: newea.png
Size: 54 KB](/attachment/image/2745439/thumbnail?d=1522780608)](/attachment/image/2745439?d=1522780608)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#416](/thread/post/10931412#post10931412 "Post Permalink")

  * Apr 4, 2018 3:53am  Apr 4, 2018 3:53am 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

for tomorrow and till end of week i will attach this setting: 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: fortomorrow.png
Size: 48 KB](/attachment/image/2745470/thumbnail?d=1522781632)](/attachment/image/2745470?d=1522781632)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#417](/thread/post/10934641#post10934641 "Post Permalink")

  * Apr 5, 2018 12:43am  Apr 5, 2018 12:43am 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

today the system got target profit.  
We will see tomorrow how the results. Friday no trading. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: result040418.png
Size: 42 KB](/attachment/image/2747063/thumbnail?d=1522856571)](/attachment/image/2747063?d=1522856571)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#418](/thread/post/10938493#post10938493 "Post Permalink")

  * Apr 6, 2018 12:43am  Apr 6, 2018 12:43am 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

today the system performed very good: daily target 52 euro. For whis week its finished.  
Next week same setting no monday. If someone wants to test real  
contact me in pm and give me your account number and mail adres. i will give you the working expiry 01 06 2018.  
good testing to all. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: good050418.png
Size: 48 KB](/attachment/image/2748941/thumbnail?d=1522942981)](/attachment/image/2748941?d=1522942981)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#419](/thread/post/10938724#post10938724 "Post Permalink")

  * Apr 6, 2018 1:42am  Apr 6, 2018 1:42am 

  * [ spojka](spojka)

  * | Joined Oct 2016  | Status: Trader | [42 Posts](/search?do=process&provider=Member&searchuser=506593)

> [Quoting Ezios](/thread/post/10938493#post10938493 "View Quoted Post")
> 
> Disliked
> 
> today the system performed very good: daily target 52 euro. For whis week its finished. Next week same setting no monday. If someone wants to test real contact me in pm and give me your account number and mail adres. i will give you the working expiry 01 06 2018. good testing to all. {image}
> 
> Ignored

Do you have any perfomance graph for longer period? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#420](/thread/post/10940374#post10940374 "Post Permalink")

  * Apr 6, 2018 4:00pm  Apr 6, 2018 4:00pm 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

till now i changed various settings and tested the ea only to frix the bugs.  
from next week i will test only this setting and sowing avry day the result of my account.  
no more. we will see the results of this ea in the time...

> [Quoting spojka](/thread/post/10938724#post10938724 "View Quoted Post")
> 
> Disliked
> 
> {quote} Do you have any perfomance graph for longer period?
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Playing with the currencies: Gabin System
  *   * [ **Reply to Thread** ](/thread/739272-playing-with-the-currencies-gabin-system/reply#reply)

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

[Doubling up method or playing casino](/thread/4169-doubling-up-method-or-playing-casino "Hi everyone, 
  
I was thinking about one strategy which I called doubling up method but I want to share it and you to review and make...") 24 replies

[Playing the Double-Up Game?](/thread/42119-playing-the-double-up-game "It's sure a crazy full of risk system. I was just wondering if anyone ever heard of someone doing this and winning? 
  
With this system...") 40 replies

[Playing with datetime...](/thread/36065-playing-with-datetime "Hi, 
  
Setting the date, manually, in Alert 2 to todays date, why does Alert 1 return a different value than Alert 2? Even using...") 2 replies

[Playing the Breakout Trade](/thread/6189-playing-the-breakout-trade "by Abe Cofnas 
 
When markets move, particularly in Forex, they move fast. We all have witnessed breakouts and have had the occasion to...") 4 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/739272-playing-with-the-currencies-gabin-system/reply#reply)
  * Subscribe
  * [161](javascript:void\(0\);)

Attachments: Playing with the currencies: Gabin System

Tags: Playing with the currencies: Gabin System

#  [](/thread/739272-playing-with-the-currencies-gabin-system)Playing with the currencies: Gabin System 

  * 

  * [#421](/thread/post/10942764#post10942764 "Post Permalink")

  * Apr 7, 2018 2:57am  Apr 7, 2018 2:57am 

  * [ spojka](spojka)

  * | Joined Oct 2016  | Status: Trader | [42 Posts](/search?do=process&provider=Member&searchuser=506593)

> [Quoting Ezios](/thread/post/10940374#post10940374 "View Quoted Post")
> 
> Disliked
> 
> till now i changed various settings and tested the ea only to frix the bugs. from next week i will test only this setting and sowing avry day the result of my account. no more. we will see the results of this ea in the time...{quote}
> 
> Ignored

What do you thing about back testing? Is there any possibility? I will help you if there is interest from your side. Your idea looks good. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#422](/thread/post/10943496#post10943496 "Post Permalink")

  * Apr 7, 2018 2:07pm  Apr 7, 2018 2:07pm 

  * [ spojka](spojka)

  * | Joined Oct 2016  | Status: Trader | [42 Posts](/search?do=process&provider=Member&searchuser=506593)

What do you thing about back testing? Is there any possibility? I will help you if there is interest from your side. Your idea looks good. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#423](/thread/post/10946650#post10946650 "Post Permalink")

  * Apr 9, 2018 4:29pm  Apr 9, 2018 4:29pm 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

> [Quoting spojka](/thread/post/10943496#post10943496 "View Quoted Post")
> 
> Disliked
> 
> What do you thing about back testing? Is there any possibility? I will help you if there is interest from your side. Your idea looks good.
> 
> Ignored

this is multipair system it can't be backtested.  
the orders opened at a time are 7. only ft in demo accounts. 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#424](/thread/post/10948790#post10948790 "Post Permalink")

  * Apr 10, 2018 1:55am  Apr 10, 2018 1:55am 

  * [ spojka](spojka)

  * | Joined Oct 2016  | Status: Trader | [42 Posts](/search?do=process&provider=Member&searchuser=506593)

> [Quoting Ezios](/thread/post/10946650#post10946650 "View Quoted Post")
> 
> Disliked
> 
> {quote} this is multipair system it can't be backtested. the orders opened at a time are 7. only ft in demo accounts.
> 
> Ignored

What will be price of version for real account? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#425](/thread/post/10948907#post10948907 "Post Permalink")

  * Apr 10, 2018 2:36am  Apr 10, 2018 2:36am 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

i give free version for testing until 01-06-2018 you send me number of your real account and your email.  
after 1-6-2018 in base of profit of this ea i will decide what to do. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#426](/thread/post/10950014#post10950014 "Post Permalink")

  * Apr 10, 2018 1:01pm  Apr 10, 2018 1:01pm 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

Good morning to all. Game over for today. The robot got a cycle of take profit and a stop loss  
New day tomorrow.  
image attached: 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: gameover.png
Size: 53 KB](/attachment/image/2754011/thumbnail?d=1523332904)](/attachment/image/2754011?d=1523332904)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#427](/thread/post/10950027#post10950027 "Post Permalink")

  * Apr 10, 2018 1:05pm  Apr 10, 2018 1:05pm 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

New monster in action. It's name is TrendBasket. Tested for the first time yesterdy got  
good results. I will post this evening the result for today now running.... 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: trendbasket.png
Size: 50 KB](/attachment/image/2754014/thumbnail?d=1523333054)](/attachment/image/2754014?d=1523333054)   

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [trendbasketv1ff.ex4](/attachment/file/2754017?d=1523333082) 149 KB | 222 downloads 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#428](/thread/post/10952293#post10952293 "Post Permalink")

  * Apr 11, 2018 12:31am  Apr 11, 2018 12:31am 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

Today the monster is in big dd and it got a sl in a pair. I think i will change sl/tp to 30 pips to reduce the loss  
and to have the abililty to renew the trades during the day. To me this ea has great potential...  
we sill see in the tests.... 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: badtoday.png
Size: 50 KB](/attachment/image/2755139/thumbnail?d=1523374308)](/attachment/image/2755139?d=1523374308)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#429](/thread/post/10953645#post10953645 "Post Permalink")

  * Apr 11, 2018 8:40am  Apr 11, 2018 8:40am 

  * [ cpips](cpips)

  * | Joined Aug 2016  | Status: Trader | [90 Posts](/search?do=process&provider=Member&searchuser=485383)

Update from 21Feb to 11Apr 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: update chart 21Feb 11Apr.png
Size: 45 KB](/attachment/image/2755705/thumbnail?d=1523403592)](/attachment/image/2755705?d=1523403592)   
[![Click to Enlarge

Name: update 21Feb 11Apr.png
Size: 24 KB](/attachment/image/2755707/thumbnail?d=1523403614)](/attachment/image/2755707?d=1523403614)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#430](/thread/post/10953945#post10953945 "Post Permalink")

  * Apr 11, 2018 1:02pm  Apr 11, 2018 1:02pm 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

> [Quoting cpips](/thread/post/10953645#post10953645 "View Quoted Post")
> 
> Disliked
> 
> Update from 21Feb to 11Apr {image} {image}
> 
> Ignored

I think its good result 40% in 2 months.... i have to change the settings often to test the robots but  
a full time test as this without to change any setting is very useful to all. thanks. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#431](/thread/post/10953948#post10953948 "Post Permalink")

  * Apr 11, 2018 1:09pm  Apr 11, 2018 1:09pm 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

I attached all 2 robots to same account.  
I changed the setting sl/tp of TrendBasaket from 100 to 30 pips.  
this night little profit from the 2 robots: 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: 110418.png
Size: 53 KB](/attachment/image/2755900/thumbnail?d=1523419708)](/attachment/image/2755900?d=1523419708)   
[![Click to Enlarge

Name: 110418_1.png
Size: 62 KB](/attachment/image/2755903/thumbnail?d=1523419731)](/attachment/image/2755903?d=1523419731)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#432](/thread/post/10954025#post10954025 "Post Permalink")

  * Apr 11, 2018 2:11pm  Apr 11, 2018 2:11pm 

  * [ cpips](cpips)

  * | Joined Aug 2016  | Status: Trader | [90 Posts](/search?do=process&provider=Member&searchuser=485383)

> [Quoting Ezios](/thread/post/10953945#post10953945 "View Quoted Post")
> 
> Disliked
> 
> {quote} I think its good result 40% in 2 months.... i have to change the settings often to test the robots but a full time test as this without to change any setting is very useful to all. thanks.
> 
> Ignored

![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#433](/thread/post/10954946#post10954946 "Post Permalink")

  * Apr 11, 2018 8:06pm  Apr 11, 2018 8:06pm 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

This evening i will add an option to pwtcea_v3 and TrendBasket : AutoRemoveOnSl true or false.  
if turn to true the ea will autoremove from chart when global stop loss (as now does) but if you turn to false  
the ea will continue to trade. This is useful if you want to test the robot in vps leaving it for 2 3 4 months without human  
intervention. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#434](/thread/post/10956115#post10956115 "Post Permalink")

  * Apr 12, 2018 12:43am  Apr 12, 2018 12:43am 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

Tday pwtcea_v3 is going good... TrendBasket no good... .I expected more from this robot but... perhaps no good signals.  
Will wait... 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: 1104pw.png
Size: 33 KB](/attachment/image/2756889/thumbnail?d=1523461345)](/attachment/image/2756889?d=1523461345)   
[![Click to Enlarge

Name: 1104tb.png
Size: 50 KB](/attachment/image/2756890/thumbnail?d=1523461386)](/attachment/image/2756890?d=1523461386)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#435](/thread/post/10956216#post10956216 "Post Permalink")

  * Apr 12, 2018 1:09am  Apr 12, 2018 1:09am 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

New version of the robots: added AutoRemoveOnSl=false  
if you want the robot to auto remove itself from chart when global sl reached turn it to true. 

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [pwtceav3ff.ex4](/attachment/file/2756938?d=1523462944) 164 KB | 218 downloads 

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [trendbasketv1ff.ex4](/attachment/file/2756939?d=1523462973) 149 KB | 218 downloads 

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#436](/thread/post/10956240#post10956240 "Post Permalink")

  * Apr 12, 2018 1:21am  Apr 12, 2018 1:21am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar404331_1.gif) merlin1331](merlin1331)

  * | Joined Mar 2015  | Status: Trader | [232 Posts](/search?do=process&provider=Member&searchuser=404331)

> [Quoting cpips](/thread/post/10953645#post10953645 "View Quoted Post")
> 
> Disliked
> 
> Update from 21Feb to 11Apr {image} {image}
> 
> Ignored

do you use default setting to run this ea? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#437](/thread/post/10956865#post10956865 "Post Permalink")

  * Apr 12, 2018 5:12am  Apr 12, 2018 5:12am 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

I will put pwtceav3ff in my demo account with the following setting stable  
running every day for 2 months and we will see the results.  
here is the setting: 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#438](/thread/post/10956874#post10956874 "Post Permalink")

  * Apr 12, 2018 5:14am  Apr 12, 2018 5:14am 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

rema,ed it to .txt rename to .set 

Attached File(s)

![File Type: txt](https://assets.faireconomy.media/images/attach/txt.gif) [pwtceav3ff.txt](/attachment/file/2757222?d=1523477656) < 1 KB | 171 downloads 

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#439](/thread/post/10957139#post10957139 "Post Permalink")

  * Apr 12, 2018 7:33am  Apr 12, 2018 7:33am 

  * [ cpips](cpips)

  * | Joined Aug 2016  | Status: Trader | [90 Posts](/search?do=process&provider=Member&searchuser=485383)

> [Quoting merlin1331](/thread/post/10956240#post10956240 "View Quoted Post")
> 
> Disliked
> 
> {quote} do you use default setting to run this ea?
> 
> Ignored

use this setting 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: magino6161.png
Size: 17 KB](/attachment/image/2757305/thumbnail?d=1523485992)](/attachment/image/2757305?d=1523485992)   

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#440](/thread/post/10957170#post10957170 "Post Permalink")

  * Apr 12, 2018 7:51am  Apr 12, 2018 7:51am 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

interesting the setting. i will change my demo account. see wat's happen. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Playing with the currencies: Gabin System
  *   * [ **Reply to Thread** ](/thread/739272-playing-with-the-currencies-gabin-system/reply#reply)

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

[Doubling up method or playing casino](/thread/4169-doubling-up-method-or-playing-casino "Hi everyone, 
  
I was thinking about one strategy which I called doubling up method but I want to share it and you to review and make...") 24 replies

[Playing the Double-Up Game?](/thread/42119-playing-the-double-up-game "It's sure a crazy full of risk system. I was just wondering if anyone ever heard of someone doing this and winning? 
  
With this system...") 40 replies

[Playing with datetime...](/thread/36065-playing-with-datetime "Hi, 
  
Setting the date, manually, in Alert 2 to todays date, why does Alert 1 return a different value than Alert 2? Even using...") 2 replies

[Playing the Breakout Trade](/thread/6189-playing-the-breakout-trade "by Abe Cofnas 
 
When markets move, particularly in Forex, they move fast. We all have witnessed breakouts and have had the occasion to...") 4 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/739272-playing-with-the-currencies-gabin-system/reply#reply)
  * Subscribe
  * [161](javascript:void\(0\);)

Attachments: Playing with the currencies: Gabin System

Tags: Playing with the currencies: Gabin System

#  [](/thread/739272-playing-with-the-currencies-gabin-system)Playing with the currencies: Gabin System 

  * 

  * [#441](/thread/post/10957624#post10957624 "Post Permalink")

  * Apr 12, 2018 1:26pm  Apr 12, 2018 1:26pm 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

New version TrendBasketv2ff. Changed the detection of the signal: not only the strenght of the basket but also  
the position of it. Changed the setting stop loss for pair 30 and tp 10. We take little profit at a time. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: 1204tb.png
Size: 50 KB](/attachment/image/2757486/thumbnail?d=1523507064)](/attachment/image/2757486?d=1523507064)   

Attached File(s)

![File Type: txt](https://assets.faireconomy.media/images/attach/txt.gif) [trendbasketv2.txt](/attachment/file/2757487?d=1523507116) < 1 KB | 241 downloads 

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [trendbasketv2ff.ex4](/attachment/file/2757490?d=1523507162) 150 KB | 235 downloads 

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#442](/thread/post/10957631#post10957631 "Post Permalink")

  * Apr 12, 2018 1:29pm  Apr 12, 2018 1:29pm 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

Changed the setting for pwtceav3. Now its alone in the account and making his profit. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: 1204pw.png
Size: 32 KB](/attachment/image/2757494/thumbnail?d=1523507333)](/attachment/image/2757494?d=1523507333)   

Attached File(s)

![File Type: txt](https://assets.faireconomy.media/images/attach/txt.gif) [pwtceav3ff.txt](/attachment/file/2757497?d=1523507370) < 1 KB | 186 downloads 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#443](/thread/post/10959886#post10959886 "Post Permalink")

  * Apr 13, 2018 12:30am  Apr 13, 2018 12:30am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar404331_1.gif) merlin1331](merlin1331)

  * | Joined Mar 2015  | Status: Trader | [232 Posts](/search?do=process&provider=Member&searchuser=404331)

**hi, Ezios, can you link your ea test account in your TE explore? so we can check these two eas perfromance.**

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#444](/thread/post/10961002#post10961002 "Post Permalink")

  * Apr 13, 2018 7:00am  Apr 13, 2018 7:00am 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

> [Quoting merlin1331](/thread/post/10959886#post10959886 "View Quoted Post")
> 
> Disliked
> 
> hi, Ezios, can you link your ea test account in your TE explore? so we can check these two eas perfromance.
> 
> Ignored

i tried to do this thing but didnt be able to do... first problem my broker is not in the list.  
so.... i will send the result in puctures... if i will find the way i will do trade explorer 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#445](/thread/post/10961113#post10961113 "Post Permalink")

  * Apr 13, 2018 8:28am  Apr 13, 2018 8:28am 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

> [Quoting HumanEA](/thread/post/10961033#post10961033 "View Quoted Post")
> 
> Disliked
> 
> I actually love the system..People should think deeper and have more patience for systems..There is no shortcut to heaven..
> 
> Ignored

![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#446](/thread/post/10963356#post10963356 "Post Permalink")

  * Apr 14, 2018 12:19am  Apr 14, 2018 12:19am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar404331_1.gif) merlin1331](merlin1331)

  * | Joined Mar 2015  | Status: Trader | [232 Posts](/search?do=process&provider=Member&searchuser=404331)

> [Quoting Ezios](/thread/post/10961002#post10961002 "View Quoted Post")
> 
> Disliked
> 
> {quote} i tried to do this thing but didnt be able to do... first problem my broker is not in the list. so.... i will send the result in puctures... if i will find the way i will do trade explorer
> 
> Ignored

**maybe you can post your performance via myfxbook or mql5 link here. no need to TE.**

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#447](/thread/post/10963867#post10963867 "Post Permalink")

  * Apr 14, 2018 3:33am  Apr 14, 2018 3:33am 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

> [Quoting merlin1331](/thread/post/10963356#post10963356 "View Quoted Post")
> 
> Disliked
> 
> {quote} maybe you can post your performance via myfxbook or mql5 link here. no need to TE.
> 
> Ignored

I have mql5 account. I can to try with it... for now the images:  
\- changed setting to TrendBasket sl/tp for individual pair moved to 30 pips. its equal risk/reward. we will see.  
\- pwtceav3ff run with the setting given. only took about 10 eur profit. 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: 1304tb.png
Size: 50 KB](/attachment/image/2760220/thumbnail?d=1523644361)](/attachment/image/2760220?d=1523644361)   
[![Click to Enlarge

Name: 1304pw.png
Size: 32 KB](/attachment/image/2760223/thumbnail?d=1523644411)](/attachment/image/2760223?d=1523644411)   

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#448](/thread/post/10963889#post10963889 "Post Permalink")

  * Apr 14, 2018 3:39am  Apr 14, 2018 3:39am 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

pardon... posted the picture of yesterday. picture of today: 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: 1304pwtcea.png
Size: 33 KB](/attachment/image/2760235/thumbnail?d=1523644782)](/attachment/image/2760235?d=1523644782)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#449](/thread/post/10964687#post10964687 "Post Permalink")

  * Apr 14, 2018 3:16pm  Apr 14, 2018 3:16pm 

  * [ spojka](spojka)

  * | Joined Oct 2016  | Status: Trader | [42 Posts](/search?do=process&provider=Member&searchuser=506593)

Friday BAD DAY 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: friday.png
Size: 18 KB](/attachment/image/2760548/thumbnail?d=1523686564)](/attachment/image/2760548?d=1523686564)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#450](/thread/post/10964808#post10964808 "Post Permalink")

  * Apr 14, 2018 5:38pm  Apr 14, 2018 5:38pm 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

> [Quoting spojka](/thread/post/10964687#post10964687 "View Quoted Post")
> 
> Disliked
> 
> Friday BAD DAY {image}
> 
> Ignored

i think the setting of the 3 steps of signal is very important. now i use 4.5 , 5.0 and 5.5.  
with the default you do many cycles of take profit but when the market moves strongly you get stop loss.  
The other setting its more strong for the signals you have - take profit but also - stop loss. i think so.  
we will see... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#451](/thread/post/10965469#post10965469 "Post Permalink")

  * Apr 15, 2018 3:06am  Apr 15, 2018 3:06am 

  * [ spojka](spojka)

  * | Joined Oct 2016  | Status: Trader | [42 Posts](/search?do=process&provider=Member&searchuser=506593)

> [Quoting Ezios](/thread/post/10964808#post10964808 "View Quoted Post")
> 
> Disliked
> 
> {quote} i think the setting of the 3 steps of signal is very important. now i use 4.5 , 5.0 and 5.5. with the default you do many cycles of take profit but when the market moves strongly you get stop loss. The other setting its more strong for the signals you have - take profit but also - stop loss. i think so. we will see...
> 
> Ignored

I thing that for succesfull trades is necessary to choose trading hours. But problem is that backtest is not possible. You idea is good but only for exact time. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#452](/thread/post/10965530#post10965530 "Post Permalink")

  * Apr 15, 2018 4:07am  Apr 15, 2018 4:07am 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

> [Quoting spojka](/thread/post/10965469#post10965469 "View Quoted Post")
> 
> Disliked
> 
> {quote} I thing that for succesfull trades is necessary to choose trading hours. But problem is that backtest is not possible. You idea is good but only for exact time.
> 
> Ignored

the time i used is from 3.00 to 21.59. my broker is +2 gmt so is gmt from 1.00 to 19.59.  
you try 2 o4 3 months in your demo account and you see... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#453](/thread/post/10966304#post10966304 "Post Permalink")

  * Apr 15, 2018 8:46pm  Apr 15, 2018 8:46pm 

  * [ spojka](spojka)

  * | Joined Oct 2016  | Status: Trader | [42 Posts](/search?do=process&provider=Member&searchuser=506593)

Is it possible to add another parametr to be able to trade between 6-8am and second period between 10-12 am in one day? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#454](/thread/post/10966378#post10966378 "Post Permalink")

  * Apr 15, 2018 9:44pm  Apr 15, 2018 9:44pm 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

> [Quoting spojka](/thread/post/10966304#post10966304 "View Quoted Post")
> 
> Disliked
> 
> Is it possible to add another parametr to be able to trade between 6-8am and second period between 10-12 am in one day?
> 
> Ignored

i dont want more complicated things... you just can do it attaching 2 different ea with 2 magic numbers and different times....  
so no need to do it. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#455](/thread/post/10966586#post10966586 "Post Permalink")

  * Apr 16, 2018 12:00am  Apr 16, 2018 12:00am 

  * [ spojka](spojka)

  * | Joined Oct 2016  | Status: Trader | [42 Posts](/search?do=process&provider=Member&searchuser=506593)

> [Quoting Ezios](/thread/post/10966378#post10966378 "View Quoted Post")
> 
> Disliked
> 
> {quote} i dont want more complicated things... you just can do it attaching 2 different ea with 2 magic numbers and different times.... so no need to do it.
> 
> Ignored

You are right. Thank you 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#456](/thread/post/10967808#post10967808 "Post Permalink")

  * Apr 16, 2018 4:20pm  Apr 16, 2018 4:20pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar620434_4.gif) syndicat](syndicat)

  * | Additional Username  | Joined Oct 2017 | [432 Posts](/search?do=process&provider=Member&searchuser=620434)

> [Quoting Ezios](/thread/post/10964808#post10964808 "View Quoted Post")
> 
> Disliked
> 
> {quote} i think the setting of the 3 steps of signal is very important. now i use 4.5 , 5.0 and 5.5. with the default you do many cycles of take profit but when the market moves strongly you get stop loss. The other setting its more strong for the signals you have - take profit but also - stop loss. i think so. we will see...
> 
> Ignored

  
Hi Ezios ! The maximum indicator reading which I saw always stayed in a value of 5.16 . Maybe it's worth checking the correctness of the calculation ? 

"Money makes Money"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#457](/thread/post/10970072#post10970072 "Post Permalink")

  * Apr 17, 2018 3:18am  Apr 17, 2018 3:18am 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

> [Quoting syndicat](/thread/post/10967808#post10967808 "View Quoted Post")
> 
> Disliked
> 
> {quote} Hi Ezios ! The maximum indicator reading which I saw always stayed in a value of 5.16 . Maybe it's worth checking the correctness of the calculation ?
> 
> Ignored

the calculation i copied from indicator my calculation follow Madscalp's rule and its correct.  
This the result for today the robots: 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: 1604pw.png
Size: 33 KB](/attachment/image/2763061/thumbnail?d=1523902699)](/attachment/image/2763061?d=1523902699)   
[![Click to Enlarge

Name: 1604tb.png
Size: 50 KB](/attachment/image/2763063/thumbnail?d=1523902722)](/attachment/image/2763063?d=1523902722)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#458](/thread/post/10970179#post10970179 "Post Permalink")

  * Apr 17, 2018 4:03am  Apr 17, 2018 4:03am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar620434_4.gif) syndicat](syndicat)

  * | Additional Username  | Joined Oct 2017 | [432 Posts](/search?do=process&provider=Member&searchuser=620434)

Help me get answers to these questions: Can the strength of any of the 8 currencies always be the maximum of 5.16 ??? Why in the EA settings 4.5; 5.0; 5.5; if we know the maximum 5.16 ??? 

"Money makes Money"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#459](/thread/post/10970280#post10970280 "Post Permalink")

  * Edited 5:27am  Apr 17, 2018 4:52am | Edited 5:27am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar620434_4.gif) syndicat](syndicat)

  * | Additional Username  | Joined Oct 2017 | [432 Posts](/search?do=process&provider=Member&searchuser=620434)

Hi Ezios Calculation in the indicator is wrong. The sum of all currencies are always 36 !!! In this screenshot, the sum of all currencies is 36.35 ???  
  
Calculation error is almost 1% for each trade . If there are 30 deals in a month ... 30% profit You do not get 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: AUDUSDM1.png
Size: 65 KB](/attachment/image/2763141/thumbnail?d=1523908356)](/attachment/image/2763141?d=1523908356)   

"Money makes Money"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#460](/thread/post/10970979#post10970979 "Post Permalink")

  * Apr 17, 2018 12:50pm  Apr 17, 2018 12:50pm 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

> [Quoting syndicat](/thread/post/10970280#post10970280 "View Quoted Post")
> 
> Disliked
> 
> Hi Ezios Calculation in the indicator is wrong. The sum of all currencies are always 36 !!! In this screenshot, the sum of all currencies is 36.35 ??? Calculation error is almost 1% for each trade . If there are 30 deals in a month ... 30% profit You do not get {image}
> 
> Ignored

i added the second digit for more precision of signal. with 1 digit the result is rounded and is 36. no worry.  
calculation is not wrong. you want to go witn 3 4 5 6 digits? it will be about 36.....  
for the question of 5.16 you are free to put 5.16 instead of 5.5 no problem for me. everyone tests the sigals he want... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Playing with the currencies: Gabin System
  *   * [ **Reply to Thread** ](/thread/739272-playing-with-the-currencies-gabin-system/reply#reply)

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

[Doubling up method or playing casino](/thread/4169-doubling-up-method-or-playing-casino "Hi everyone, 
  
I was thinking about one strategy which I called doubling up method but I want to share it and you to review and make...") 24 replies

[Playing the Double-Up Game?](/thread/42119-playing-the-double-up-game "It's sure a crazy full of risk system. I was just wondering if anyone ever heard of someone doing this and winning? 
  
With this system...") 40 replies

[Playing with datetime...](/thread/36065-playing-with-datetime "Hi, 
  
Setting the date, manually, in Alert 2 to todays date, why does Alert 1 return a different value than Alert 2? Even using...") 2 replies

[Playing the Breakout Trade](/thread/6189-playing-the-breakout-trade "by Abe Cofnas 
 
When markets move, particularly in Forex, they move fast. We all have witnessed breakouts and have had the occasion to...") 4 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/739272-playing-with-the-currencies-gabin-system/reply#reply)
  * Subscribe
  * [161](javascript:void\(0\);)

Attachments: Playing with the currencies: Gabin System

Tags: Playing with the currencies: Gabin System

#  [](/thread/739272-playing-with-the-currencies-gabin-system)Playing with the currencies: Gabin System 

  * 

  * [#461](/thread/post/10971002#post10971002 "Post Permalink")

  * Apr 17, 2018 1:03pm  Apr 17, 2018 1:03pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar620434_4.gif) syndicat](syndicat)

  * | Additional Username  | Joined Oct 2017 | [432 Posts](/search?do=process&provider=Member&searchuser=620434)

> [Quoting Ezios](/thread/post/10970979#post10970979 "View Quoted Post")
> 
> Disliked
> 
> {quote} i added the second digit for more precision of signal. with 1 digit the result is rounded and is 36. no worry. calculation is not wrong. you want to go witn 3 4 5 6 digits? it will be about 36..... for the question of 5.16 you are free to put 5.16 instead of 5.5 no problem for me. everyone tests the sigals he want...
> 
> Ignored

Thanks for the explanation Ezios. Can you make the second and third basket of orders open on the next new candle ? 

"Money makes Money"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#462](/thread/post/10971046#post10971046 "Post Permalink")

  * Apr 17, 2018 1:37pm  Apr 17, 2018 1:37pm 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

> [Quoting syndicat](/thread/post/10971002#post10971002 "View Quoted Post")
> 
> Disliked
> 
> {quote} Thanks for the explanation Ezios. Can you make the second and third basket of orders open on the next new candle ?
> 
> Ignored

the candle is not relevant in this ea. it is an ontimer ea. it calculates the signal every 1 second not every 1 minute candle.  
i can to add a parameter time in second and you can set to 60 so the ea will calculates every 60 second but i dont advise you to do it. the logic is every 1 second. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#463](/thread/post/10971071#post10971071 "Post Permalink")

  * Apr 17, 2018 1:44pm  Apr 17, 2018 1:44pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar620434_4.gif) syndicat](syndicat)

  * | Additional Username  | Joined Oct 2017 | [432 Posts](/search?do=process&provider=Member&searchuser=620434)

> [Quoting Ezios](/thread/post/10971046#post10971046 "View Quoted Post")
> 
> Disliked
> 
> {quote} the candle is not relevant in this ea. it is an ontimer ea. it calculates the signal every 1 second not every 1 minute candle. i can to add a parameter time in second and you can set to 60 so the ea will calculates every 60 second but i dont advise you to do it. the logic is every 1 second.
> 
> Ignored

As a rule, the price reaches 5.0 several times in one or several days. I want there to be a time lag between basket openings. So that the baskets do not open next to the same price. Is obtained if the price immediately bounced back and You have closed basket of, if the price goes against you the drawdown will less. 

"Money makes Money"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#464](/thread/post/10971096#post10971096 "Post Permalink")

  * Apr 17, 2018 1:54pm  Apr 17, 2018 1:54pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar620434_4.gif) syndicat](syndicat)

  * | Additional Username  | Joined Oct 2017 | [432 Posts](/search?do=process&provider=Member&searchuser=620434)

Ezios I give advice which I tried to trade hands and they improve results!!! I also like You want to make this EA profitable !!! Why don't you listen to me?![](https://resources.faireconomy.media/images/emojis/64/1f9d0.png?v=15.1)

"Money makes Money"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#465](/thread/post/10971106#post10971106 "Post Permalink")

  * Apr 17, 2018 1:59pm  Apr 17, 2018 1:59pm 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

> [Quoting syndicat](/thread/post/10971071#post10971071 "View Quoted Post")
> 
> Disliked
> 
> {quote} As a rule, the price reaches 5.0 several times in one or several days. I want there to be a time lag between basket openings. So that the baskets do not open next to the same price. Is obtained if the price immediately bounced back and You have closed basket of, if the price goes against you the drawdown will less.
> 
> Ignored

this ea can not to open the same basket 2 times at the same signal every signal is considered only 1 time  
if y ou get 5.0 trigger only first time the remainder is not considered.  
if you get 5 down signal same thing. only 2 basket for 2 signals. so the problem does not exist.  
max basket can be opened is 6. 1 for every signal. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#466](/thread/post/10971122#post10971122 "Post Permalink")

  * Apr 17, 2018 2:11pm  Apr 17, 2018 2:11pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar620434_4.gif) syndicat](syndicat)

  * | Additional Username  | Joined Oct 2017 | [432 Posts](/search?do=process&provider=Member&searchuser=620434)

> [Quoting Ezios](/thread/post/10971106#post10971106 "View Quoted Post")
> 
> Disliked
> 
> {quote} this ea can not to open the same basket 2 times at the same signal every signal is considered only 1 time if y ou get 5.0 trigger only first time the remainder is not considered. if you get 5 down signal same thing. only 2 basket for 2 signals. so the problem does not exist. max basket can be opened is 6. 1 for every signal.
> 
> Ignored

For example, I set the settings 4.8 5.0 5.1 and the price goes in one move, and I will open 3 baskets at the same price !!! 

"Money makes Money"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#467](/thread/post/10971129#post10971129 "Post Permalink")

  * Apr 17, 2018 2:16pm  Apr 17, 2018 2:16pm 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

> [Quoting syndicat](/thread/post/10971122#post10971122 "View Quoted Post")
> 
> Disliked
> 
> {quote} For example, I set the settings 4.8 5.0 5.1 and the price goes in one move, and I will open 3 baskets at the same price !!!
> 
> Ignored

no it is impossible. it open a basket for every signal. if is not so download the last version.  
max 6 basket. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#468](/thread/post/10971133#post10971133 "Post Permalink")

  * Apr 17, 2018 2:17pm  Apr 17, 2018 2:17pm 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

new version upload. set input log=true every basket is bought or sold it arrives y ou a email with the signal.  
good luck and good day. 

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [pwtceav3ff.ex4](/attachment/file/2763471?d=1523942258) 174 KB | 209 downloads 

[0 ](javascript:void\(0\);) [2 ](javascript:void\(0\);)

  * [#469](/thread/post/10971136#post10971136 "Post Permalink")

  * Apr 17, 2018 2:19pm  Apr 17, 2018 2:19pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar620434_4.gif) syndicat](syndicat)

  * | Additional Username  | Joined Oct 2017 | [432 Posts](/search?do=process&provider=Member&searchuser=620434)

> [Quoting Ezios](/thread/post/10971129#post10971129 "View Quoted Post")
> 
> Disliked
> 
> {quote} no it is impossible. it open a basket for every signal. if is not so download the last version. max 6 basket.
> 
> Ignored

4.8-1 cart 5.0 - 2 cart 5.1-3 cart Correct ???  
  
3 signals - 3 baskets of one currency!!! 

"Money makes Money"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#470](/thread/post/10971155#post10971155 "Post Permalink")

  * Apr 17, 2018 2:24pm  Apr 17, 2018 2:24pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar620434_4.gif) syndicat](syndicat)

  * | Additional Username  | Joined Oct 2017 | [432 Posts](/search?do=process&provider=Member&searchuser=620434)

And all 3 signals can pass in 5 minutes !!! And there will be an opening 3 baskets in 5 minutes !!!  
  
  
Do you understand what I'm explaining to you?  
  
  
Explain why I need an e-mail ??? The EA will become more profitable to trade ??? Add the right things, not the trash... 

"Money makes Money"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#471](/thread/post/10971229#post10971229 "Post Permalink")

  * Apr 17, 2018 2:57pm  Apr 17, 2018 2:57pm 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

advice to all want to test this ea:  
attach with your setting and dont change while the ea is running.  
If you want to change setting change also magic number so it restart the count from zero.  
I have no more to tell about it and i will not make any changes to this ea. if you dont like it dont test. point. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#472](/thread/post/10971270#post10971270 "Post Permalink")

  * Apr 17, 2018 3:17pm  Apr 17, 2018 3:17pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar620434_4.gif) syndicat](syndicat)

  * | Additional Username  | Joined Oct 2017 | [432 Posts](/search?do=process&provider=Member&searchuser=620434)

> [Quoting Ezios](/thread/post/10971229#post10971229 "View Quoted Post")
> 
> Disliked
> 
> advice to all want to test this ea: attach with your setting and dont change while the ea is running. If you want to change setting change also magic number so it restart the count from zero. I have no more to tell about it and i will not make any changes to this ea. if you dont like it dont test. point.
> 
> Ignored

  
You want it was profitable, but to make changes to improve the work do not want ... What is the point of testing an expert Advisor that does not make a profit ??? Head to think and not just in order to wear a hat ! 

"Money makes Money"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#473](/thread/post/10974164#post10974164 "Post Permalink")

  * Apr 18, 2018 5:29am  Apr 18, 2018 5:29am 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

Ok i read more attemption the posts. i didnt understood about what someone wants to say...  
anyway... i say that if you trade only one synmbol at a time all 3 signals are respected.  
for example if you do 8 chart every chart one eur one aud one chf etc etc all 3 signals are respected.  
in this way you have max 6 basket opened and low dd. in the other way if i do the change the basket maximum  
becamo more more mobe because there are 8*3=24 for high and 24 for low signal possibility. thats is no practicable.  
so.... i remain the idea to not change anything.  
i post the results for today: 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: 1704pw.png
Size: 33 KB](/attachment/image/2764789/thumbnail?d=1523996924)](/attachment/image/2764789?d=1523996924)   
[![Click to Enlarge

Name: 1704tb.png
Size: 50 KB](/attachment/image/2764792/thumbnail?d=1523996960)](/attachment/image/2764792?d=1523996960)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#474](/thread/post/10974174#post10974174 "Post Permalink")

  * Apr 18, 2018 5:35am  Apr 18, 2018 5:35am 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

Second observation: if its true that the limit for last signal is 5.16 then the best setting for  
to catch all 3 signal is 4.5 4.8 5.1 in this way all 3 signals are covered.  
I expected more from the other robot TrendBasket but I see its not profitable. Perhaps i have to cut off  
the 15, tf that's irrelevant or i juswt must to cut off the robot itself.. i dont know... time will tell me.  
Good evening to all. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#475](/thread/post/10977288#post10977288 "Post Permalink")

  * Apr 19, 2018 1:09am  Apr 19, 2018 1:09am 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

Today i started final tests with setting of signals 4.5 4.8 5.1 . I attached mgic 5555 gbp magic 5656 jpy magic 5454 eur and 5858 usd.  
its best setting so last and final tests. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: 180418.png
Size: 31 KB](/attachment/image/2766241/thumbnail?d=1524067782)](/attachment/image/2766241?d=1524067782)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#476](/thread/post/10978663#post10978663 "Post Permalink")

  * Apr 19, 2018 12:44pm  Apr 19, 2018 12:44pm 

  * [ hock87](hock87)

  * | Joined Nov 2015  | Status: Trader | [5 Posts](/search?do=process&provider=Member&searchuser=433407)

> [Quoting AlHaggag](/thread/post/10876757#post10876757 "View Quoted Post")
> 
> Disliked
> 
> {quote} please go back to the picture in post #311 page 16 for more explanation. and if its not understood. I will explain again. ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)
> 
> Ignored

Hi, friend.  
I don't understood.  
Can use in M15/ H1?  
M5 are more the 500 just trade.  
then M15 and H1 how much?  
Where can find this indicator Explanation....  
If can email to me: { email address deleted by staff }  
Thanks. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#477](/thread/post/10980243#post10980243 "Post Permalink")

  * Apr 19, 2018 9:33pm  Apr 19, 2018 9:33pm 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

Ok. Little bugfix the ea did not send right value to email for log of signals thats very useful.  
Today results very good with the setting 4.5 4.8 5.1 i think really the best. Good luck to all. 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: 1904gbp.png
Size: 32 KB](/attachment/image/2767398/thumbnail?d=1524141115)](/attachment/image/2767398?d=1524141115)   
[![Click to Enlarge

Name: 1904jpy.png
Size: 32 KB](/attachment/image/2767407/thumbnail?d=1524141148)](/attachment/image/2767407?d=1524141148)   
[![Click to Enlarge

Name: 1904usd.png
Size: 32 KB](/attachment/image/2767408/thumbnail?d=1524141167)](/attachment/image/2767408?d=1524141167)   

Attached File(s)

![File Type: ex4](https://assets.faireconomy.media/images/attach/ex4.gif) [pwtceav3ff.ex4](/attachment/file/2767410?d=1524141200) 180 KB | 231 downloads 

[0 ](javascript:void\(0\);) [1 ](javascript:void\(0\);)

  * [#478](/thread/post/10980256#post10980256 "Post Permalink")

  * Apr 19, 2018 9:36pm  Apr 19, 2018 9:36pm 

  * [ spojka](spojka)

  * | Joined Oct 2016  | Status: Trader | [42 Posts](/search?do=process&provider=Member&searchuser=506593)

> [Quoting Ezios](/thread/post/10977288#post10977288 "View Quoted Post")
> 
> Disliked
> 
> Today i started final tests with setting of signals 4.5 4.8 5.1 . I attached mgic 5555 gbp magic 5656 jpy magic 5454 eur and 5858 usd. its best setting so last and final tests. {image}
> 
> Ignored

How to attach sdifferent magic for differerent currency. you have strarted 3 EA? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#479](/thread/post/10980311#post10980311 "Post Permalink")

  * Apr 19, 2018 9:56pm  Apr 19, 2018 9:56pm 

  * [ spojka](spojka)

  * | Joined Oct 2016  | Status: Trader | [42 Posts](/search?do=process&provider=Member&searchuser=506593)

Why is big unbalance between Global stop loss and Global take profit? Did you try 50/50? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#480](/thread/post/10980364#post10980364 "Post Permalink")

  * Apr 19, 2018 10:04pm  Apr 19, 2018 10:04pm 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

attach each ea with each different magic number in each different chart  
set the string to wich currency y9u want to trade.  
stop loss is 100 because the market have to run first to reach the profit.  
in that period where there are the news the price goes against.  
if yiu want to try other money management try... it can be useful.  

> [Quoting spojka](/thread/post/10980311#post10980311 "View Quoted Post")
> 
> Disliked
> 
> Why is big unbalance between Global stop loss and Global take profit? Did you try 50/50?
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Playing with the currencies: Gabin System
  *   * [ **Reply to Thread** ](/thread/739272-playing-with-the-currencies-gabin-system/reply#reply)

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

[Doubling up method or playing casino](/thread/4169-doubling-up-method-or-playing-casino "Hi everyone, 
  
I was thinking about one strategy which I called doubling up method but I want to share it and you to review and make...") 24 replies

[Playing the Double-Up Game?](/thread/42119-playing-the-double-up-game "It's sure a crazy full of risk system. I was just wondering if anyone ever heard of someone doing this and winning? 
  
With this system...") 40 replies

[Playing with datetime...](/thread/36065-playing-with-datetime "Hi, 
  
Setting the date, manually, in Alert 2 to todays date, why does Alert 1 return a different value than Alert 2? Even using...") 2 replies

[Playing the Breakout Trade](/thread/6189-playing-the-breakout-trade "by Abe Cofnas 
 
When markets move, particularly in Forex, they move fast. We all have witnessed breakouts and have had the occasion to...") 4 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/739272-playing-with-the-currencies-gabin-system/reply#reply)
  * Subscribe
  * [161](javascript:void\(0\);)

Attachments: Playing with the currencies: Gabin System

Tags: Playing with the currencies: Gabin System

#  [](/thread/739272-playing-with-the-currencies-gabin-system)Playing with the currencies: Gabin System 

  * 

  * [#481](/thread/post/10985079#post10985079 "Post Permalink")

  * Apr 21, 2018 2:26am  Apr 21, 2018 2:26am 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

Tonight profit with yen and still drawdown sith dollar. We will see if next week there will be the profit... 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: 2004jpy.png
Size: 32 KB](/attachment/image/2769519/thumbnail?d=1524245167)](/attachment/image/2769519?d=1524245167)   
[![Click to Enlarge

Name: 2004usd.png
Size: 32 KB](/attachment/image/2769521/thumbnail?d=1524245190)](/attachment/image/2769521?d=1524245190)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#482](/thread/post/10985445#post10985445 "Post Permalink")

  * Apr 21, 2018 5:26am  Apr 21, 2018 5:26am 

  * [ spojka](spojka)

  * | Joined Oct 2016  | Status: Trader | [42 Posts](/search?do=process&provider=Member&searchuser=506593)

> [Quoting Ezios](/thread/post/10985079#post10985079 "View Quoted Post")
> 
> Disliked
> 
> Tonight profit with yen and still drawdown sith dollar. We will see if next week there will be the profit... {image} {image}
> 
> Ignored

I have the same results as you. Do you thing about reversal strategy? Simply buy instead sell in the sane moment. I know it could be bad but it worth to be tried. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#483](/thread/post/10985627#post10985627 "Post Permalink")

  * Apr 21, 2018 7:26am  Apr 21, 2018 7:26am 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

> [Quoting spojka](/thread/post/10985445#post10985445 "View Quoted Post")
> 
> Disliked
> 
> {quote} I have the same results as you. Do you thing about reversal strategy? Simply buy instead sell in the sane moment. I know it could be bad but it worth to be tried.
> 
> Ignored

reversal strategh i tried but dont work. more and more stop loss then take profits.  
so... the unique way is to wait for the price to go in your favour. It doesnt exist a  
allways profitable strategy......  
the reversal of trend is the key. You saw TrendBasket and you saw dont work. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#484](/thread/post/10991807#post10991807 "Post Permalink")

  * Apr 24, 2018 3:39am  Apr 24, 2018 3:39am 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

Week start with loss... dollar big dd and big sl  
gbp little profit... go on with test... 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: 2304gbp.png
Size: 32 KB](/attachment/image/2772436/thumbnail?d=1524508721)](/attachment/image/2772436?d=1524508721)   
[![Click to Enlarge

Name: 2304usd.png
Size: 32 KB](/attachment/image/2772439/thumbnail?d=1524508745)](/attachment/image/2772439?d=1524508745)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#485](/thread/post/10995789#post10995789 "Post Permalink")

  * Apr 25, 2018 3:10am  Apr 25, 2018 3:10am 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

Today jen got profit and gbp still working...  
we will see tomorrow... 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: 2408gbp.png
Size: 32 KB](/attachment/image/2774148/thumbnail?d=1524593361)](/attachment/image/2774148?d=1524593361)   
[![Click to Enlarge

Name: 2408jpy.png
Size: 32 KB](/attachment/image/2774151/thumbnail?d=1524593395)](/attachment/image/2774151?d=1524593395)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#486](/thread/post/10999185#post10999185 "Post Permalink")

  * Apr 26, 2018 12:48am  Apr 26, 2018 12:48am 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

Today gbp got sl in 2 pairs. we will see if tomorrow it will recover.  
Yesterday was about +6 euro but the target is 10 so... no profit.  
waiting.... 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: 2504gbp.png
Size: 32 KB](/attachment/image/2775702/thumbnail?d=1524671282)](/attachment/image/2775702?d=1524671282)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#487](/thread/post/11003658#post11003658 "Post Permalink")

  * Apr 27, 2018 2:39am  Apr 27, 2018 2:39am 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

Today good profit for gbp and eur activated for the first time with this setup. We will see the results. 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: 2604gbp.png
Size: 32 KB](/attachment/image/2777666/thumbnail?d=1524764329)](/attachment/image/2777666?d=1524764329)   
[![Click to Enlarge

Name: 2604eur.png
Size: 33 KB](/attachment/image/2777668/thumbnail?d=1524764352)](/attachment/image/2777668?d=1524764352)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#488](/thread/post/11007240#post11007240 "Post Permalink")

  * Apr 28, 2018 3:00am  Apr 28, 2018 3:00am 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

Today gbp hit stop loss in several pairs and is still suffering...  
eur hit tp in a pair and is still running...  
for now with this setup the currency allways in profit was jen.  
we will see next week... 

Attached Image(s) (click to enlarge)

[![Click to Enlarge

Name: 2704eur.png
Size: 33 KB](/attachment/image/2779404/thumbnail?d=1524851988)](/attachment/image/2779404?d=1524851988)   
[![Click to Enlarge

Name: 2704gbp.png
Size: 32 KB](/attachment/image/2779407/thumbnail?d=1524852005)](/attachment/image/2779407?d=1524852005)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#489](/thread/post/11012660#post11012660 "Post Permalink")

  * May 1, 2018 2:22am  May 1, 2018 2:22am 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

This week start new setting and remove all the others. 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: 6161.png
Size: 32 KB](/attachment/image/2781888/thumbnail?d=1525108905)](/attachment/image/2781888?d=1525108905)   

Attached File(s)

![File Type: txt](https://assets.faireconomy.media/images/attach/txt.gif) [6161.txt](/attachment/file/2781890?d=1525108924) < 1 KB | 222 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#490](/thread/post/11012709#post11012709 "Post Permalink")

  * May 1, 2018 2:35am  May 1, 2018 2:35am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar620434_4.gif) syndicat](syndicat)

  * | Additional Username  | Joined Oct 2017 | [432 Posts](/search?do=process&provider=Member&searchuser=620434)

[Ezios ](https://www.forexfactory.com/ezios) with this logic, the EA will never earn. think about why nobody's testing.... if you want to create a profitable EA, you need to listen to the advice! 

"Money makes Money"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#491](/thread/post/11012725#post11012725 "Post Permalink")

  * May 1, 2018 2:40am  May 1, 2018 2:40am 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

> [Quoting syndicat](/thread/post/11012709#post11012709 "View Quoted Post")
> 
> Disliked
> 
> [Ezios ](https://www.forexfactory.com/ezios) with this logic, the EA will never earn. think about why nobody's testing.... if you want to create a profitable EA, you need to listen to the advice!
> 
> Ignored

i think this setting is good... i want to try for 1 month... then if is not good  
we will see if i change the ea ... dont know... we will see this month. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#492](/thread/post/11012756#post11012756 "Post Permalink")

  * May 1, 2018 2:44am  May 1, 2018 2:44am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar620434_4.gif) syndicat](syndicat)

  * | Additional Username  | Joined Oct 2017 | [432 Posts](/search?do=process&provider=Member&searchuser=620434)

I'm amazed at your perseverance.![](https://resources.faireconomy.media/images/emojis/64/270c-fe0f.png?v=15.1)

"Money makes Money"

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#493](/thread/post/11014124#post11014124 "Post Permalink")

  * May 1, 2018 4:29pm  May 1, 2018 4:29pm 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

The good news for today is that this setup is going well....  
testing for 1 month..... 

Attached Image (click to enlarge)

[![Click to Enlarge

Name: 010518.png
Size: 32 KB](/attachment/image/2782515/thumbnail?d=1525159743)](/attachment/image/2782515?d=1525159743)   

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#494](/thread/post/11103843#post11103843 "Post Permalink")

  * May 27, 2018 11:35pm  May 27, 2018 11:35pm 

  * [ spojka](spojka)

  * | Joined Oct 2016  | Status: Trader | [42 Posts](/search?do=process&provider=Member&searchuser=506593)

> [Quoting Ezios](/thread/post/11014124#post11014124 "View Quoted Post")
> 
> Disliked
> 
> The good news for today is that this setup is going well.... testing for 1 month..... {image}
> 
> Ignored

hello,   
can I ask you? Do you have any new results? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#495](/thread/post/11196883#post11196883 "Post Permalink")

  * Jun 25, 2018 2:58am  Jun 25, 2018 2:58am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar403461_16.gif) shahed58](shahed58)

  * Joined Mar 2015 | Status: i love you | [343 Posts](/search?do=process&provider=Member&searchuser=403461)

hi madscalp  
How was the use of the DeltaUp & DeltaDown with strength currency and Did not you get any results?  
  
Has someone else tested in the long run? 

be healthy and wealthy... Ceeport

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#496](/thread/post/11196907#post11196907 "Post Permalink")

  * Jun 25, 2018 3:10am  Jun 25, 2018 3:10am 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

> [Quoting spojka](/thread/post/11103843#post11103843 "View Quoted Post")
> 
> Disliked
> 
> {quote} hello, can I ask you? Do you have any new results?
> 
> Ignored

i tried this ea in various settings but i did not get good results in the long term so i  
abandoned the project. if someone have new ideas to revive it i will try to look for it. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#497](/thread/post/13127173#post13127173 "Post Permalink")

  * Aug 24, 2020 12:13am  Aug 24, 2020 12:13am 

  * [ Samalin](samalin)

  * Joined Apr 2017 | Status: Trader | [1,068 Posts](/search?do=process&provider=Member&searchuser=573327)

i am a newbie just interested i have been following this thread, please i will like to make a suggestion can we try different use i mean logic of currency strength?  
like using logic with currency pairs giraia 28 pairs?  
Closed cucle F1.6? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#498](/thread/post/13134435#post13134435 "Post Permalink")

  * Aug 27, 2020 6:32pm  Aug 27, 2020 6:32pm 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

> [Quoting Samalin](/thread/post/13127173#post13127173 "View Quoted Post")
> 
> Disliked
> 
> i am a newbie just interested i have been following this thread, please i will like to make a suggestion can we try different use i mean logic of currency strength? like using logic with currency pairs giraia 28 pairs? Closed cucle F1.6?
> 
> Ignored

ok my friend... i dont know exactly what setting you are referring to.....  
anyway im trying the cm_mod1 indicator with delta 1/8 set to 6 for continuation of the trend.  
I explain: when signal delta 1/8 is >=6 and first currency is goiong up and last goiong down (arrow)  
i buy the stronger and sell the weaker. tp 10 sl 25. i am trying this in discretionary way and  
it seems to have good signals. I can think to automatize this. my demo is icmarket account.  
any suggestion is welcome. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#499](/thread/post/13135844#post13135844 "Post Permalink")

  * Aug 28, 2020 4:19am  Aug 28, 2020 4:19am 

  * [ Samalin](samalin)

  * Joined Apr 2017 | Status: Trader | [1,068 Posts](/search?do=process&provider=Member&searchuser=573327)

> [Quoting Ezios](/thread/post/13134435#post13134435 "View Quoted Post")
> 
> Disliked
> 
> {quote} ok my friend... i dont know exactly what setting you are referring to..... anyway im trying the cm_mod1 indicator with delta 1/8 set to 6 for continuation of the trend. I explain: when signal delta 1/8 is >=6 and first currency is goiong up and last goiong down (arrow) i buy the stronger and sell the weaker. tp 10 sl 25. i am trying this in discretionary way and it seems to have good signals. I can think to automatize this. my demo is icmarket account. any suggestion is welcome.
> 
> Ignored

  
ook, just a new thought i like to share  
if the rate of losses is more than profit why not try to reverse the system and see how it goes , just to always be on the profit side 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#500](/thread/post/13135918#post13135918 "Post Permalink")

  * Last Post: Aug 28, 2020 5:51am  Aug 28, 2020 5:51am 

  * [ Ezios](ezios)

  * Joined Jul 2016 | Status: Trader | [586 Posts](/search?do=process&provider=Member&searchuser=476659)

its a fast scalping system. in theory you can go 1:1 for 10 tp and 10 sl but  
i want to give the market the ability to move alittle against... try yourself the best for you  
its the same... the more near you put tp the more probability you have to reach the profit.  
and vice versa. the important is that good signal is move than 50% you understand??????  
bye bye. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * Playing with the currencies: Gabin System
  *   * [ **Reply to Thread** ](/thread/739272-playing-with-the-currencies-gabin-system/reply#reply)

[](https://www.forexfactory.com "Homepage")

  * [Forums](forums)
  * [Trades](trades)
  * [Calendar](calendar)
  * [News](news)
  * [Market](market)
  * [Brokers](brokers)

****

[](https://www.faireconomy.com/)
