

  * 

[The Pouria Method](/thread/17011-the-pouria-method "OKay here is one of the 4 best systems that I've made and used, with this system I pickup atleast 50 pips a day, I'm sharing this because...") 562 replies

[Lessons Learned during System Development](/thread/2986-lessons-learned-during-system-development "Hi, 
  
I've been reading through the forum and somehow I'm in the process of developing my own system.. But not really doing actual...") 29 replies

[(pouria method II on the test)](/thread/23104-pouria-method-ii-on-the-test "Hello  
pouria method II is now DONE thanks to the group of experts and mathematicians that helped and made this method. 
now we are...") 218 replies

[System Development Secrets](/thread/7342-system-development-secrets "&lt;meta http-equiv=&quot;CONTENT-TYPE&quot; content=&quot;text/html; charset=utf-8&quot;&gt;&lt;title&gt;&lt;/title&gt;&lt;meta name=&quot;GENERATOR&quot; content=&quot;OpenOffice.org 2.0 ...") 5 replies

[Metatrader 4 Development Course](/thread/5906-metatrader-4-development-course "Here is the Mql_4_Metatrader_4_Development_Course in pdf \(link fixed\) : 
 
http://www.freefilehosting.org/pupload/view/8711") 3 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/17242-the-pouria-ea-development-thread/reply#reply)
  * Subscribe
  * [45](javascript:void\(0\);)

Attachments: The Pouria EA Development Thread

Tags: The Pouria EA Development Thread

#  [](/thread/17242-the-pouria-ea-development-thread)The Pouria EA Development Thread 

  * 

  * [#1](/thread/17242-the-pouria-ea-development-thread "Post Permalink")

  * First Post: Feb 9, 2007 6:58pm  Feb 9, 2007 6:58pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar25698_4.gif) mikhaildgreat](mikhaildgreat)

  * | Joined Nov 2006  | Status: EA Programmer | [298 Posts](/search?do=process&provider=Member&searchuser=25698)

Hello All,  
  
Before Going any further, And you have no Idea what Pouria is about, please fallow this link: <http://www.forexfactory.com/showthread.php?t=17011>  
  
Below is the Pouria EA Beta. It has not yet tested on live market and has not yet been optimized. The purpose of this thread is to find any bugs in the program as well as find the best settings for the EA.  
  
OK, so first let me explain how the EA works because I programmed it according to my interpretation of The Pouria Method which you may disagree with.   
  
The EA take the signals generated from both the MACD and the MA with equal weight. For example MACD crosses below zero then moves back up, and MA is also signals up it will take a buy position, same with with MA when MA cross Up and MACD points to the same direction it will take a Buy trade. So as long as both indicators agree when either one crosses the signal line it will take the trade. (I attached Chart Image below to better illustrate this)  
  
So here are the external variables:  
  
**\---------- Pouria EA Beta**  
  
**MagicNumber** = Set Magic Number to whatever lucky number you desire  
  
**StopLoss** = Set Initial Stoploss Level  
  
**TakeProfit** = Set TP Level  
  
**BreakEvenAfterPips** = Move The SL to breakeven after this number in pips is reached, Set to Zero to disable  
  
**ConfirmedOnEntry** = if set to true EA will open trade after close of the candle; if false EA will open trade as soon as there is a signal  
  
**\---------- Order Setting**  
  
**NumberOfTries** = Number of tries EA will attempt to open a trade, just leave as default  
  
**Slippage** = Set Slippage value depending on your broker  
  
**\---------- Money Management**  
  
**Lots** = Amount in lots you want to trade. EA will use this value if MM is false  
**MM** = Use Money Management or not  
**AccountIsMicro** = Use Micro-Account or not  
**Risk** = Percent of free margin to risk per trade, MM must be set to true  
  
**\---------- Alert Setting**  
  
**EnableAlert** = set to true if you want to be alerted every time EA makes a trade  
  
So that's It, Pls Play around with the EA and look for the Optimal settings for each pair then post it here. That is your Job because I'm quite lazy when it comes to optimization. When we have found the best settings we can then integrate those values to the code so that everyone(including noobs) can profit from this EA.  
  
Thats it! Enjoy!  
  
Mikhail 

Attached Image

![](/attachment/image/21873?d=1171014575)

Attached File(s)

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [Pouria EA Beta.mq4](/attachment/file/21871?d=1171014552) 13 KB | 2,473 downloads 

  * [#2](/thread/post/212609#post212609 "Post Permalink")

  * Feb 9, 2007 7:17pm  Feb 9, 2007 7:17pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar10886_4.gif) radyfox](radyfox)

  * | Joined May 2006  | Status: Trader | [41 Posts](/search?do=process&provider=Member&searchuser=10886)

Perfect work! ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)  
But why can't I see the indicators in my chart? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#3](/thread/post/212610#post212610 "Post Permalink")

  * Edited 7:27pm  Feb 9, 2007 7:17pm | Edited 7:27pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar29751_4.gif) lexazver](lexazver)

  * | Joined Dec 2006  | Status: o_O | [1,511 Posts](/search?do=process&provider=Member&searchuser=29751)

SO if i will just put this file into indicators folder then load it in the terminal it should work ( buy and sell) automatically? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#4](/thread/post/212612#post212612 "Post Permalink")

  * Feb 9, 2007 7:19pm  Feb 9, 2007 7:19pm 

  * [ forig](forig)

  * | Joined May 2006  | Status: Trader | [33 Posts](/search?do=process&provider=Member&searchuser=9267)

> [Quoting lexazver](/thread/post/212610#post212610 "View Quoted Post")
> 
> Disliked
> 
> SO if i will just put this file into indicators folder then load it in the terminal it should work ( and and sell) automatically?
> 
> Ignored

в директорию экспертов и перезагрузить МТ4, только он сливает безбожно, чего и следовало ожидать 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#5](/thread/post/212630#post212630 "Post Permalink")

  * Feb 9, 2007 7:27pm  Feb 9, 2007 7:27pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar29751_4.gif) lexazver](lexazver)

  * | Joined Dec 2006  | Status: o_O | [1,511 Posts](/search?do=process&provider=Member&searchuser=29751)

ну я так и сделал , только не понятно он загружается или нет...график таким же остается как и первоначально ничего не меняется. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#6](/thread/post/212633#post212633 "Post Permalink")

  * Feb 9, 2007 7:29pm  Feb 9, 2007 7:29pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar25698_4.gif) mikhaildgreat](mikhaildgreat)

  * | Joined Nov 2006  | Status: EA Programmer | [298 Posts](/search?do=process&provider=Member&searchuser=25698)

> [Quoting radyfox](/thread/post/212609#post212609 "View Quoted Post")
> 
> Disliked
> 
> Perfect work! ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1)  
>  But why can't I see the indicators in my chart?
> 
> Ignored

radyfox load the indicators separately, EA will trade even without the indicators loaded in your chart, but for now place the indicators to see if EA is doing the right thing.  
  
  

> Quoting lexazver
> 
> Disliked
> 
> SO if i will just put this file into indicators folder then load it in the terminal it should work ( and and sell) automatically?
> 
> Ignored

lexazver you have to put it in the experts folder, then attach the expert to your chart, then make sure the you see a happy face beside the experts name.  
  

> [Quoting forig](/thread/post/212609#post212609 "View Quoted Post")
> 
> Disliked
> 
> в директорию экспертов и перезагрузить МТ4, только он сливает безбожно, чего и следовало ожидать
> 
> Ignored

Sorry my friend I have no idea what you are talking about.  
  
-Mikhail 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#7](/thread/post/212634#post212634 "Post Permalink")

  * Feb 9, 2007 7:29pm  Feb 9, 2007 7:29pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar6011_5.gif) mp777](mp777)

  * | Joined Feb 2006  | Status: Trader | [147 Posts](/search?do=process&provider=Member&searchuser=6011)

> [Quoting lexazver](/thread/post/212630#post212630 "View Quoted Post")
> 
> Disliked
> 
> ну я так и сделал , только не понятно он загружается или нет...график таким же остается как и первоначально ничего не меняется.
> 
> Ignored

I agree........I think  
  
M 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#8](/thread/post/212645#post212645 "Post Permalink")

  * Feb 9, 2007 7:35pm  Feb 9, 2007 7:35pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar29751_4.gif) lexazver](lexazver)

  * | Joined Dec 2006  | Status: o_O | [1,511 Posts](/search?do=process&provider=Member&searchuser=29751)

Yeah i did put it in the expert folder, but how do you go about running it? sorry for stupid questions like that i just never run an expert in Terminal. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#9](/thread/post/212652#post212652 "Post Permalink")

  * Feb 9, 2007 7:44pm  Feb 9, 2007 7:44pm 

  * [ forig](forig)

  * | Joined May 2006  | Status: Trader | [33 Posts](/search?do=process&provider=Member&searchuser=9267)

> [Quoting mikhaildgreat](/thread/post/212633#post212633 "View Quoted Post")
> 
> Disliked
> 
> radyfox load the indicators separately, EA will trade even without the indicators loaded in your chart, but for now place the indicators to see if EA is doing the right thing.  
>    
>    
>    
>    
>  lexazver you have to put it in the experts folder, then attach the expert to your chart, then make sure the you see a happy face beside the experts name.  
>    
>    
>    
>  Sorry, I`ve used another language  
>    
>  -Mikhail
> 
> Ignored

Sorry, I`ve used another language 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#10](/thread/post/212653#post212653 "Post Permalink")

  * Feb 9, 2007 7:45pm  Feb 9, 2007 7:45pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar25698_4.gif) mikhaildgreat](mikhaildgreat)

  * | Joined Nov 2006  | Status: EA Programmer | [298 Posts](/search?do=process&provider=Member&searchuser=25698)

> [Quoting lexazver](/thread/post/212645#post212645 "View Quoted Post")
> 
> Disliked
> 
> Yeah i did put it in the expert folder, but how do you go about running it? sorry for stupid questions like that i just never run an expert in Terminal.
> 
> Ignored

Please fallow the link below and watch the nice little tutorial video:  
  
<http://www.pipinion.com/factory/experts.htm>  
  
-Mikhail 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#11](/thread/post/212654#post212654 "Post Permalink")

  * Feb 9, 2007 7:45pm  Feb 9, 2007 7:45pm 

  * [ forig](forig)

  * | Joined May 2006  | Status: Trader | [33 Posts](/search?do=process&provider=Member&searchuser=9267)

> [Quoting lexazver](/thread/post/212645#post212645 "View Quoted Post")
> 
> Disliked
> 
> Yeah i did put it in the expert folder, but how do you go about running it? sorry for stupid questions like that i just never run an expert in Terminal.
> 
> Ignored

In expert folder click twice on expert, that all.  
But backtests showing awfull results so far ... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#12](/thread/post/212657#post212657 "Post Permalink")

  * Feb 9, 2007 7:48pm  Feb 9, 2007 7:48pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar29751_4.gif) lexazver](lexazver)

  * | Joined Dec 2006  | Status: o_O | [1,511 Posts](/search?do=process&provider=Member&searchuser=29751)

> [Quoting mikhaildgreat](/thread/post/212653#post212653 "View Quoted Post")
> 
> Disliked
> 
> Please fallow the link below and watch the nice little tutorial video:  
>    
>  <http://www.pipinion.com/factory/experts.htm>  
>    
>  -Mikhail
> 
> Ignored

  
i think ive figured it out 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#13](/thread/post/212658#post212658 "Post Permalink")

  * Feb 9, 2007 7:53pm  Feb 9, 2007 7:53pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar29751_4.gif) lexazver](lexazver)

  * | Joined Dec 2006  | Status: o_O | [1,511 Posts](/search?do=process&provider=Member&searchuser=29751)

Thank you for indicator, but when i did the test I started with 10k and ended up with something like 200$ i guess im probably doing something wrong .....but what ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) i checked the setting tried different stops and targets but still end up in the red for a year. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#14](/thread/post/212663#post212663 "Post Permalink")

  * Feb 9, 2007 8:00pm  Feb 9, 2007 8:00pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar25698_4.gif) mikhaildgreat](mikhaildgreat)

  * | Joined Nov 2006  | Status: EA Programmer | [298 Posts](/search?do=process&provider=Member&searchuser=25698)

> [Quoting lexazver](/thread/post/212658#post212658 "View Quoted Post")
> 
> Disliked
> 
> Thank you for indicator, but when i did the test I started with 10k and ended up with something like 200$ i guess im probably doing something wrong .....but what ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) i checked the setting tried different stops and targets but still end up in the red for a year.
> 
> Ignored

yup like I said this expert has not been optimized yet, It just blindly fallows the Pouria Method. And when backtesting make sure you have at least 90% modeling quality.  
  
Regards,  
Mikhail 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#15](/thread/post/212670#post212670 "Post Permalink")

  * Feb 9, 2007 8:11pm  Feb 9, 2007 8:11pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar25698_4.gif) mikhaildgreat](mikhaildgreat)

  * | Joined Nov 2006  | Status: EA Programmer | [298 Posts](/search?do=process&provider=Member&searchuser=25698)

> [Quoting forig](/thread/post/212654#post212654 "View Quoted Post")
> 
> Disliked
> 
> In expert folder click twice on expert, that all.  
>  But backtests showing awfull results so far ...
> 
> Ignored

LOL I agree.   
  
Its wierd though when you test it starting 2007 it does pretty well. but everything before that just doesnt work... so when backtesting pls enable visiual mode then load the indicators in the testing charts to see if the Expert is doing things that is against the original pouria method. If its faithful to the method then the problem is just optimization, if its still not profitable after optimization then the problem is either strategy tester (which could likely be because we have small TP and SL levels) or the strategy itself needs rethinking...  
  
-Mikhail 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#16](/thread/post/212677#post212677 "Post Permalink")

  * Feb 9, 2007 8:24pm  Feb 9, 2007 8:24pm 

  * [ BearPaw](bearpaw)

  * | Joined Jul 2006  | Status: A Trader for Life | [218 Posts](/search?do=process&provider=Member&searchuser=13999)

Mikhail,  
  
Sorry if this is a stupid question...but forexpert had us do different periods for different pairs...i.e. audjpy is on a 30 min chart and nzdusd is on an hour chart.  
  
Does the indicator need to worry about that if it does not need those indicators set up on the chart to work?  
  
Am I explaining my question well enough?  
  
Also, I turned off money management (False), and said true to mini lots, and changed my lot size to .10. Are those settings correct for testing it? I am just testing it live (forward testing), not back testing.  
  
Thanks,  
  
BP 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#17](/thread/post/212684#post212684 "Post Permalink")

  * Feb 9, 2007 8:32pm  Feb 9, 2007 8:32pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar25698_4.gif) mikhaildgreat](mikhaildgreat)

  * | Joined Nov 2006  | Status: EA Programmer | [298 Posts](/search?do=process&provider=Member&searchuser=25698)

> [Quoting BearPaw](/thread/post/212677#post212677 "View Quoted Post")
> 
> Disliked
> 
> Mikhail,  
>    
>  Sorry if this is a stupid question...but forexpert had us do different periods for different pairs...i.e. audjpy is on a 30 min chart and nzdusd is on an hour chart.  
>    
>  Does the indicator need to worry about that if it does not need those indicators set up on the chart to work?  
>    
>  Am I explaining my question well enough?  
>    
>  Also, I turned off money management (False), and said true to mini lots, and changed my lot size to .10. Are those settings correct for testing it? I am just testing it live (forward testing), not back testing.  
>    
>  Thanks,  
>    
>  BP
> 
> Ignored

Attach the expert depending on the timeframe you want to employ the strategy to. If you put it on 30M chart it will generate signals according to 30M chart if in H1 it will trade signals from H1. Also I think your other settings are correct but Please don't trade this EA in your live account until you have tested it in demo and are already comfortable with how it works. This EA has not yet been tested, I just finished this today so there may still be bugs that I haven't found.  
  
I am also testing it in demo right now, so far no trades yet.  
Thanks,  
Mikhail 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#18](/thread/post/212691#post212691 "Post Permalink")

  * Feb 9, 2007 8:43pm  Feb 9, 2007 8:43pm 

  * [ BearPaw](bearpaw)

  * | Joined Jul 2006  | Status: A Trader for Life | [218 Posts](/search?do=process&provider=Member&searchuser=13999)

> [Quoting mikhaildgreat](/thread/post/212684#post212684 "View Quoted Post")
> 
> Disliked
> 
> Attach the expert depending on the timeframe you want to employ the strategy to. If you put it on 30M chart it will generate signals according to 30M chart if in H1 it will trade signals from H1. Also I think your other settings are correct but Please don't trade this EA in your live account until you have tested it in demo and are already comfortable with how it works. This EA has not yet been tested, I just finished this today so there may still be bugs that I haven't found.  
>    
>  I am also testing it in demo right now, so far no trades yet.  
>  Thanks,  
>  Mikhail
> 
> Ignored

No problem...thanks for clarifying. I have no trades yet but it looks like aud/jpy should be close...we shall see.  
  
Thanks,  
  
BP 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#19](/thread/post/212693#post212693 "Post Permalink")

  * Feb 9, 2007 8:52pm  Feb 9, 2007 8:52pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar20609_4.gif) Ronyn76](ronyn76)

  * | Joined Oct 2006  | Status: Lord Of The Pips? | [227 Posts](/search?do=process&provider=Member&searchuser=20609)

I'm a bit confused...What is the purpose of this setting in the EA? Am i missing something? 

Liberate me ex inferis

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#20](/thread/post/212698#post212698 "Post Permalink")

  * Feb 9, 2007 9:01pm  Feb 9, 2007 9:01pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar25698_4.gif) mikhaildgreat](mikhaildgreat)

  * | Joined Nov 2006  | Status: EA Programmer | [298 Posts](/search?do=process&provider=Member&searchuser=25698)

> [Quoting Ronyn76](/thread/post/212693#post212693 "View Quoted Post")
> 
> Disliked
> 
> I'm a bit confused...What is the purpose of this setting in the EA? Am i missing something?
> 
> Ignored

LOL. magicnumber is just there so that EA can differentiate the trades it made from the other active trades done by you or other EAs.  
  
Just put whatever random number you like for magic number.  
  
-Mikhail 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * The Pouria EA Development Thread
  *   * [ **Reply to Thread** ](/thread/17242-the-pouria-ea-development-thread/reply#reply)

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

[The Pouria Method](/thread/17011-the-pouria-method "OKay here is one of the 4 best systems that I've made and used, with this system I pickup atleast 50 pips a day, I'm sharing this because...") 562 replies

[Lessons Learned during System Development](/thread/2986-lessons-learned-during-system-development "Hi, 
  
I've been reading through the forum and somehow I'm in the process of developing my own system.. But not really doing actual...") 29 replies

[(pouria method II on the test)](/thread/23104-pouria-method-ii-on-the-test "Hello  
pouria method II is now DONE thanks to the group of experts and mathematicians that helped and made this method. 
now we are...") 218 replies

[System Development Secrets](/thread/7342-system-development-secrets "&lt;meta http-equiv=&quot;CONTENT-TYPE&quot; content=&quot;text/html; charset=utf-8&quot;&gt;&lt;title&gt;&lt;/title&gt;&lt;meta name=&quot;GENERATOR&quot; content=&quot;OpenOffice.org 2.0 ...") 5 replies

[Metatrader 4 Development Course](/thread/5906-metatrader-4-development-course "Here is the Mql_4_Metatrader_4_Development_Course in pdf \(link fixed\) : 
 
http://www.freefilehosting.org/pupload/view/8711") 3 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/17242-the-pouria-ea-development-thread/reply#reply)
  * Subscribe
  * [45](javascript:void\(0\);)

Attachments: The Pouria EA Development Thread

Tags: The Pouria EA Development Thread

#  [](/thread/17242-the-pouria-ea-development-thread)The Pouria EA Development Thread 

  * 

  * [#21](/thread/post/212705#post212705 "Post Permalink")

  * Feb 9, 2007 9:10pm  Feb 9, 2007 9:10pm 

  * [ BearPaw](bearpaw)

  * | Joined Jul 2006  | Status: A Trader for Life | [218 Posts](/search?do=process&provider=Member&searchuser=13999)

Ok, so I am in the canusd and audjpy trade right now.  
  
looks like the ea got me in at the bottom of the bar. would be nice if it could get us in right when it crosses the two red lines.  
  
On the audjpy, I would not have entered yet...but it entered. In my view of things, the yellow had not crossed the two reds.  
  
Thoughts?  
  
BP 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#22](/thread/post/212715#post212715 "Post Permalink")

  * Feb 9, 2007 9:19pm  Feb 9, 2007 9:19pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar25698_4.gif) mikhaildgreat](mikhaildgreat)

  * | Joined Nov 2006  | Status: EA Programmer | [298 Posts](/search?do=process&provider=Member&searchuser=25698)

Yup Mine Opened USDCAD and AUDJPY just now both sell. trades looks right according to my indicators. EA opens the trade even if the cross is just small, as long as the value of the yellow line is less than the 2 MAs it will sell, I did this so EA will get in as early as possible. We could later improve this by putting MinimumCrossDistance, but for now lets jsut see how it works out...  
  
-Mikhail 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#23](/thread/post/212726#post212726 "Post Permalink")

  * Feb 9, 2007 9:33pm  Feb 9, 2007 9:33pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar25698_4.gif) mikhaildgreat](mikhaildgreat)

  * | Joined Nov 2006  | Status: EA Programmer | [298 Posts](/search?do=process&provider=Member&searchuser=25698)

Cool! USDCAD just hit TP! ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1) AUDJPY is still open... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#24](/thread/post/212742#post212742 "Post Permalink")

  * Feb 9, 2007 9:49pm  Feb 9, 2007 9:49pm 

  * [ BearPaw](bearpaw)

  * | Joined Jul 2006  | Status: A Trader for Life | [218 Posts](/search?do=process&provider=Member&searchuser=13999)

> [Quoting mikhaildgreat](/thread/post/212726#post212726 "View Quoted Post")
> 
> Disliked
> 
> Cool! USDCAD just hit TP! ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1) AUDJPY is still open...
> 
> Ignored

Yep...me too....audjpy still open....  
  
Good job on the first trade Mikhail.  
  
BP 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#25](/thread/post/212750#post212750 "Post Permalink")

  * Feb 9, 2007 9:56pm  Feb 9, 2007 9:56pm 

  * [ parabolic](parabolic)

  * | Joined Jul 2006  | Status: Trader | [16 Posts](/search?do=process&provider=Member&searchuser=14363)

I did a 2 year backtest with Alpari data for EURUSD with my EA and the EA of Mikhail.  
  
No MM, 0.1 Lot and the rest standard settings.  
  
Both results are **NOT** promising. 

Attached Images

![](/attachment/image/21889?d=1171025615) ![](/attachment/image/21891?d=1171025655)

Attached File(s)

![File Type: zip](https://assets.faireconomy.media/images/attach/zip.gif) [HF_Pouria_EURUSD.zip](/attachment/file/21890?d=1171025635) 20 KB | 372 downloads 

![File Type: zip](https://assets.faireconomy.media/images/attach/zip.gif) [Pouria_EA_EURUSD.zip](/attachment/file/21892?d=1171025687) 36 KB | 360 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#26](/thread/post/212759#post212759 "Post Permalink")

  * Feb 9, 2007 10:02pm  Feb 9, 2007 10:02pm 

  * [ BearPaw](bearpaw)

  * | Joined Jul 2006  | Status: A Trader for Life | [218 Posts](/search?do=process&provider=Member&searchuser=13999)

> [Quoting parabolic](/thread/post/212750#post212750 "View Quoted Post")
> 
> Disliked
> 
> I did a 2 year backtest with Alpari data for EURUSD with my EA and the EA of Mikhail.  
>    
>  No MM, 0.1 Lot and the rest standard settings.  
>    
>  Both results are **NOT** promising.
> 
> Ignored

Interesting...dont have time to look at this....going out. But interested in more comments on parabolic's posting.  
  
BP 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#27](/thread/post/212760#post212760 "Post Permalink")

  * Feb 9, 2007 10:03pm  Feb 9, 2007 10:03pm 

  * [ BearPaw](bearpaw)

  * | Joined Jul 2006  | Status: A Trader for Life | [218 Posts](/search?do=process&provider=Member&searchuser=13999)

Ok...so both trades that the EA triggered this morning closed profitably.  
  
Let's see what else today brings.  
  
BP 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#28](/thread/post/212766#post212766 "Post Permalink")

  * Feb 9, 2007 10:08pm  Feb 9, 2007 10:08pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar25698_4.gif) mikhaildgreat](mikhaildgreat)

  * | Joined Nov 2006  | Status: EA Programmer | [298 Posts](/search?do=process&provider=Member&searchuser=25698)

> [Quoting parabolic](/thread/post/212750#post212750 "View Quoted Post")
> 
> Disliked
> 
> I did a 2 year backtest with Alpari data for EURUSD with my EA and the EA of Mikhail.  
>    
>  No MM, 0.1 Lot and the rest standard settings.  
>    
>  Both results are **NOT** promising.
> 
> Ignored

LOL! At least the equity curve of our EAs are similar ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)  
  
You think there is hope for this strategy?  
  
-Mikhail 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#29](/thread/post/212770#post212770 "Post Permalink")

  * Feb 9, 2007 10:12pm  Feb 9, 2007 10:12pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar3729_9.gif) highway](highway)

  * Joined Sep 2005 | Status: Trader | [1,352 Posts](/search?do=process&provider=Member&searchuser=3729)

> [Quoting forig](/thread/post/212612#post212612 "View Quoted Post")
> 
> Disliked
> 
> в директорию экспертов и перезагрузить МТ4, только он сливает безбожно, чего и следовало ожидать
> 
> Ignored

Put in path directory of experts and reload МТ4, hopefully it should go. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#30](/thread/post/212777#post212777 "Post Permalink")

  * Feb 9, 2007 10:20pm  Feb 9, 2007 10:20pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar3729_9.gif) highway](highway)

  * Joined Sep 2005 | Status: Trader | [1,352 Posts](/search?do=process&provider=Member&searchuser=3729)

> [Quoting lexazver](/thread/post/212630#post212630 "View Quoted Post")
> 
> Disliked
> 
> ну я так и сделал , только не понятно он загружается или нет...график таким же остается как и первоначально ничего не меняется.
> 
> Ignored

Well, I have made it, only not clear if it is loaded or not... The schedule remais the same as the original - nothing changed.  
  
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx  
  
Didn't think we have our friends from Russia or former USSR here ! !  
Nice to meet you guys here. Have read a lot of interesting stuff from your local forum. Great informations ! !   
And Thanks  
Spasibo 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#31](/thread/post/212789#post212789 "Post Permalink")

  * Feb 9, 2007 10:32pm  Feb 9, 2007 10:32pm 

  * [ parabolic](parabolic)

  * | Joined Jul 2006  | Status: Trader | [16 Posts](/search?do=process&provider=Member&searchuser=14363)

> [Quoting mikhaildgreat](/thread/post/212766#post212766 "View Quoted Post")
> 
> Disliked
> 
> LOL! At least the equity curve of our EAs are similar ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)  
>    
>  You think there is hope for this strategy?  
>    
>  -Mikhail
> 
> Ignored

I did another 2 year backtest on EURCHF.  
As recommended 1H timeframe, Target and SL 15 Pips.  
  
Not much hope for this strategy after looking at the equity curve... 

Attached Image

![](/attachment/image/21896?d=1171027847)

Attached File(s)

![File Type: zip](https://assets.faireconomy.media/images/attach/zip.gif) [Pouria_EA_EURCHF.zip](/attachment/file/21897?d=1171027866) 22 KB | 317 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#32](/thread/post/212796#post212796 "Post Permalink")

  * Feb 9, 2007 10:36pm  Feb 9, 2007 10:36pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar25698_4.gif) mikhaildgreat](mikhaildgreat)

  * | Joined Nov 2006  | Status: EA Programmer | [298 Posts](/search?do=process&provider=Member&searchuser=25698)

> [Quoting parabolic](/thread/post/212789#post212789 "View Quoted Post")
> 
> Disliked
> 
> I did another 2 year backtest on EURCHF.  
>  As recommended 1H timeframe, Target and SL 15 Pips.  
>    
>  Not much hope for this strategy after looking at the equity curve...
> 
> Ignored

LOL, what a beautiful downward equity curve! you think it will work if we reversed the signal?  
  
-Mikhail 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#33](/thread/post/212800#post212800 "Post Permalink")

  * Feb 9, 2007 10:40pm  Feb 9, 2007 10:40pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar29751_4.gif) lexazver](lexazver)

  * | Joined Dec 2006  | Status: o_O | [1,511 Posts](/search?do=process&provider=Member&searchuser=29751)

Mikhail, one thing ive noticed is that your EA opens orders before candle closes i mean as soon as cross happens it opens a trade but the candle can close in the way that setup wouldnt happen , which brongs me to another point , i checked the chart that STRATEGY TESTER gave me and sometimes positions open when EMA5 crosses only one of the red lines and not the other which give negative trades but if you wait untill it crosses fully and then enter at the open of a new candle it gives good entry. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#34](/thread/post/212802#post212802 "Post Permalink")

  * Feb 9, 2007 10:41pm  Feb 9, 2007 10:41pm 

  * [ forig](forig)

  * | Joined May 2006  | Status: Trader | [33 Posts](/search?do=process&provider=Member&searchuser=9267)

> [Quoting highway3000](/thread/post/212777#post212777 "View Quoted Post")
> 
> Disliked
> 
> Well, I have made it, only not clear if it is loaded or not... The schedule remais the same as the original - nothing changed.  
>    
>  xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx  
>    
>  Didn't think we have our friends from Russia or former USSR here ! !  
>  Nice to meet you guys here. Have read a lot of interesting stuff from your local forum. Great informations ! !   
>  And Thanks  
>  Spasibo
> 
> Ignored

From Russia with .... profit ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#35](/thread/post/212804#post212804 "Post Permalink")

  * Feb 9, 2007 10:42pm  Feb 9, 2007 10:42pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar29751_4.gif) lexazver](lexazver)

  * | Joined Dec 2006  | Status: o_O | [1,511 Posts](/search?do=process&provider=Member&searchuser=29751)

I have a suggestion , what if the size of position is doubled everytime loss is taken until the first profit i mean i looked at eurousd there are max 3 consecutive losses so when you start for example trade leverage 1:5, if you loose double you money so you use 1:11 ( 11 since you have lost some money before) and so on, or you can start with leverage 1:1, then 1:2 then 1:4 gives you 3 extra steps ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#36](/thread/post/212808#post212808 "Post Permalink")

  * Feb 9, 2007 10:47pm  Feb 9, 2007 10:47pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar19951_4.gif) nicolas_nrjk](nicolas_nrjk)

  * | Joined Sep 2006  | Status: Trader | [37 Posts](/search?do=process&provider=Member&searchuser=19951)

the EA is working greatly but it was a little problem.  
you have to add a fuction that checkes for open positions befor entering a new one. the EA bought me twice a short position in USD CAD.  
  
thanks you for the EA. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#37](/thread/post/212810#post212810 "Post Permalink")

  * Feb 9, 2007 10:51pm  Feb 9, 2007 10:51pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar25698_4.gif) mikhaildgreat](mikhaildgreat)

  * | Joined Nov 2006  | Status: EA Programmer | [298 Posts](/search?do=process&provider=Member&searchuser=25698)

The truth is there are 2 things in question here... Srategy Tester and Pouria's method. I myself honestly don't have much confidence in either of them but only time can tell. Because with manual backtesting(using my beutiful eyes) The strategy seems profitable, Im baffled why startegy tester shows consistent losses which we cannot see during manual backtesting.  
  
One of my theories is that since backtester merely averages the minute chart and this strategy has very tight stops and target so the results are not accurate at all. Or it could simply be that Paurias method itself is truely flawed.  
  
Anyways I will continue my forward test for at least a month then compare actual results from that of backtester, And if my theory is correct and Strategy Tester is no good, then goodriddence to the Strategy tester, no more wasting my time with optimizing this and that.  
  
But right now Im off to the casino to score me some pips, I mean chips!  
  
Good Luck Everyone,  
Mikhail 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#38](/thread/post/212814#post212814 "Post Permalink")

  * Feb 9, 2007 10:52pm  Feb 9, 2007 10:52pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar25698_4.gif) mikhaildgreat](mikhaildgreat)

  * | Joined Nov 2006  | Status: EA Programmer | [298 Posts](/search?do=process&provider=Member&searchuser=25698)

> [Quoting nicolas_nrjk](/thread/post/212808#post212808 "View Quoted Post")
> 
> Disliked
> 
> the EA is working greatly but it was a little problem.  
>  you have to add a fuction that checkes for open positions befor entering a new one. the EA bought me twice a short position in USD CAD.  
>    
>  thanks you for the EA.
> 
> Ignored

really! now thats a problem, will look into it.  
  
-Mikhail 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#39](/thread/post/212815#post212815 "Post Permalink")

  * Feb 9, 2007 10:52pm  Feb 9, 2007 10:52pm 

  * [ megamo](megamo)

  * | Joined Sep 2006  | Status: BengalTrader | [175 Posts](/search?do=process&provider=Member&searchuser=19380)

The point is to find out how good the strategy is and if it holds out to be successful over the long term. If we try martingaling it then I'm sure alot of different strategies would seem successful, but I don't believe thats the best way to go. I still think this strategy, given some discretion, looking at trend and support and resistance levels, has a good chance of profitability. All MA crossover systems require the subjectivity part of a trader in my opinion since you have to look at the bigger picture if you're going trend, or counter trend, or considering the [spreads](/brokers/spreads "View Live Spreads on the Broker Guide"), the time frame used, as well as the ADR of different pairs. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#40](/thread/post/212872#post212872 "Post Permalink")

  * Feb 9, 2007 11:27pm  Feb 9, 2007 11:27pm 

  * [ JamDown](jamdown)

  * | Joined Dec 2006  | Status: Trader | [39 Posts](/search?do=process&provider=Member&searchuser=27324)

> [Quoting parabolic](/thread/post/212789#post212789 "View Quoted Post")
> 
> Disliked
> 
> I did another 2 year backtest on EURCHF.  
>  As recommended 1H timeframe, Target and SL 15 Pips.  
>    
>  Not much hope for this strategy after looking at the equity curve...
> 
> Ignored

I think the stop loss is the problem. When I went back to the original P post it looked as if the system was not intended to be used with a stoploss. I have notice that when trading one of the biggest reason for loosing is having a stop that was too narrow. We should retest with a wider stop...say 25 to 30 with a 40 pip TP. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * The Pouria EA Development Thread
  *   * [ **Reply to Thread** ](/thread/17242-the-pouria-ea-development-thread/reply#reply)

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

[The Pouria Method](/thread/17011-the-pouria-method "OKay here is one of the 4 best systems that I've made and used, with this system I pickup atleast 50 pips a day, I'm sharing this because...") 562 replies

[Lessons Learned during System Development](/thread/2986-lessons-learned-during-system-development "Hi, 
  
I've been reading through the forum and somehow I'm in the process of developing my own system.. But not really doing actual...") 29 replies

[(pouria method II on the test)](/thread/23104-pouria-method-ii-on-the-test "Hello  
pouria method II is now DONE thanks to the group of experts and mathematicians that helped and made this method. 
now we are...") 218 replies

[System Development Secrets](/thread/7342-system-development-secrets "&lt;meta http-equiv=&quot;CONTENT-TYPE&quot; content=&quot;text/html; charset=utf-8&quot;&gt;&lt;title&gt;&lt;/title&gt;&lt;meta name=&quot;GENERATOR&quot; content=&quot;OpenOffice.org 2.0 ...") 5 replies

[Metatrader 4 Development Course](/thread/5906-metatrader-4-development-course "Here is the Mql_4_Metatrader_4_Development_Course in pdf \(link fixed\) : 
 
http://www.freefilehosting.org/pupload/view/8711") 3 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/17242-the-pouria-ea-development-thread/reply#reply)
  * Subscribe
  * [45](javascript:void\(0\);)

Attachments: The Pouria EA Development Thread

Tags: The Pouria EA Development Thread

#  [](/thread/17242-the-pouria-ea-development-thread)The Pouria EA Development Thread 

  * 

  * [#41](/thread/post/212896#post212896 "Post Permalink")

  * Edited Feb 10, 2007 12:35am  Feb 9, 2007 11:41pm | Edited Feb 10, 2007 12:35am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30695_4.gif) toti1972](toti1972)

  * | Joined Jan 2007  | Status: Trader | [107 Posts](/search?do=process&provider=Member&searchuser=30695)

> [Quoting JamDown](/thread/post/212872#post212872 "View Quoted Post")
> 
> Disliked
> 
> I think the stop loss is the problem. When I went back to the original P post it looked as if the system was not intended to be used with a stoploss. I have notice that when trading one of the biggest reason for loosing is having a stop that was too narrow. We should retest with a wider stop...say 25 to 30 with a 40 pip TP.
> 
> Ignored

I posted the same on the other thread...(post 181)  
  
I wonder what would happen if we do not take loss until we got a reverse signal. For instance: yesterday night we got SL on CAN but we never got a reverse signal, so if we didn't set SL, now we would be making profit....On the other hand, if we get a reverse signal, then we take the loss and enter the market the other way...  
Just a thought  
  
Hope it'd be useful 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#42](/thread/post/212995#post212995 "Post Permalink")

  * Feb 10, 2007 1:17am  Feb 10, 2007 1:17am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar5179_4.gif) cgldsmth](cgldsmth)

  * Joined Dec 2005 | Status: It's only money | [1,413 Posts](/search?do=process&provider=Member&searchuser=5179)

mmm, the EA opened a buy on EURJPY at 1500GMT with no sign of a signal on the chart (M30) 

TRADE FOR SWAP

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#43](/thread/post/212998#post212998 "Post Permalink")

  * Feb 10, 2007 1:19am  Feb 10, 2007 1:19am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar33539_4.gif) mwilkinw](mwilkinw)

  * | Joined Feb 2007  | Status: Trader | [27 Posts](/search?do=process&provider=Member&searchuser=33539)

Hey thanks everyone for your input and advice! I think this system certainly has potential... but like others have said, because of the MA's these crosses usually are followed by large trends. So, for testing purposes...I saw how horrible the system was testing according to the stop loss and profit taking parameters being so small... if you change your SL-50 pips and TP-100 pips, total lots-2 the results are staggering for a one month test! Try it, $3696.70 Net Profit on GBP/USD 30 day test!  
  
I do suggest multiple lots, taking profit and letting the remaining lots ride with a moved up SL to solidify gains... I've tested this for some time and have reaped the rewards.. I.E. I've been in the eur/jpy since the 6th, usd/jpy since the 7th, and eur/chf since the 7th... there is definitely potential if you scale out of your trades and implement a good money management system... I personally use a 'half kelly" type system.. I increase as I get profitable!  
  
Happy Trading  
  
p.s. I think a proper stop for this system is better if put on the opposite side of the 75 and 85 MA's rather than a preset number... but i think these numbers will help with testnig purposes! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#44](/thread/post/213019#post213019 "Post Permalink")

  * Feb 10, 2007 1:35am  Feb 10, 2007 1:35am 

  * [ JamDown](jamdown)

  * | Joined Dec 2006  | Status: Trader | [39 Posts](/search?do=process&provider=Member&searchuser=27324)

> [Quoting toti1972](/thread/post/212896#post212896 "View Quoted Post")
> 
> Disliked
> 
> I posted the same on the other thread...(post 181)  
>    
>  I wonder what would happen if we do not take loss until we got a reverse signal. For instance: yesterday night we got SL on CAN but we never got a reverse signal, so if we didn't set SL, now we would be making profit....On the other hand, if we get a reverse signal, then we take the loss and enter the market the other way...  
>  Just a thought  
>    
>  Hope it'd be useful
> 
> Ignored

I just went back and saw that. Great minds pull from the same source of all knowledge...El Kaluwm.  
BigDog 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#45](/thread/post/213122#post213122 "Post Permalink")

  * Feb 10, 2007 3:14am  Feb 10, 2007 3:14am 

  * [ NKE](nke)

  * | Joined Sep 2006  | Status: Trader | [62 Posts](/search?do=process&provider=Member&searchuser=18940)

> [Quoting mwilkinw](/thread/post/212998#post212998 "View Quoted Post")
> 
> Disliked
> 
> Hey thanks everyone for your input and advice! I think this system certainly has potential... but like others have said, because of the MA's these crosses usually are followed by large trends. So, for testing purposes...I saw how horrible the system was testing according to the stop loss and profit taking parameters being so small... if you change your SL-50 pips and TP-100 pips, total lots-2 the results are staggering for a one month test! Try it, $3696.70 Net Profit on GBP/USD 30 day test!  
>    
>  I do suggest multiple lots, taking profit and letting the remaining lots ride with a moved up SL to solidify gains... I've tested this for some time and have reaped the rewards.. I.E. I've been in the eur/jpy since the 6th, usd/jpy since the 7th, and eur/chf since the 7th... there is definitely potential if you scale out of your trades and implement a good money management system... I personally use a 'half kelly" type system.. I increase as I get profitable!  
>    
>  Happy Trading  
>    
>  p.s. I think a proper stop for this system is better if put on the opposite side of the 75 and 85 MA's rather than a preset number... but i think these numbers will help with testnig purposes!
> 
> Ignored

  
Excuse my ignorance, what is a "half kelly" system? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#46](/thread/post/213131#post213131 "Post Permalink")

  * Feb 10, 2007 3:27am  Feb 10, 2007 3:27am 

  * [ FXLogic](fxlogic)

  * | Joined Apr 2005  | Status: Trader | [51 Posts](/search?do=process&provider=Member&searchuser=2243)

Have you tested for other months, too? I'm just wondering how this would do in choppier markets, like we had for the first half of 2005 or during the summer of most any year. If it's profitable in those periods without any serious drawdowns, it may have a lot potential.  
  
  

> [Quoting mwilkinw](/thread/post/212998#post212998 "View Quoted Post")
> 
> Disliked
> 
> Hey thanks everyone for your input and advice! I think this system certainly has potential... but like others have said, because of the MA's these crosses usually are followed by large trends. So, for testing purposes...I saw how horrible the system was testing according to the stop loss and profit taking parameters being so small... if you change your SL-50 pips and TP-100 pips, total lots-2 the results are staggering for a one month test! Try it, $3696.70 Net Profit on GBP/USD 30 day test!  
>    
>  I do suggest multiple lots, taking profit and letting the remaining lots ride with a moved up SL to solidify gains... I've tested this for some time and have reaped the rewards.. I.E. I've been in the eur/jpy since the 6th, usd/jpy since the 7th, and eur/chf since the 7th... there is definitely potential if you scale out of your trades and implement a good money management system... I personally use a 'half kelly" type system.. I increase as I get profitable!  
>    
>  Happy Trading  
>    
>  p.s. I think a proper stop for this system is better if put on the opposite side of the 75 and 85 MA's rather than a preset number... but i think these numbers will help with testnig purposes!
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#47](/thread/post/213137#post213137 "Post Permalink")

  * Feb 10, 2007 3:35am  Feb 10, 2007 3:35am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar33539_4.gif) mwilkinw](mwilkinw)

  * | Joined Feb 2007  | Status: Trader | [27 Posts](/search?do=process&provider=Member&searchuser=33539)

> [Quoting NKE](/thread/post/213122#post213122 "View Quoted Post")
> 
> Disliked
> 
> Excuse my ignorance, what is a "half kelly" system?
> 
> Ignored

Hey NKE! The 'half kelly" is a money management system. Essentially the kelly system is a bet sizing system. It was made popular by the MIT prof. Edward Thorp, the man who inveted hi-lo card counting for blackjack and broke Vegas. After cleaning up, he published his card counting strategy (resulting in the prosecution of card counters from that day on). He used the Kelly System for placing his bets.  
  
He started a hedge fund and used the "helf kelly" system for placing trades... basically using the kelly but the initial position is half of a normal kelly bet. His success brought this system popularity in securities trading and variations of it have been used by traders and fund managers ever since!  
  
I use a half kelly system on my initial trade position and add to my position as the account increases... still using the kelly system to either get out of my trades or figure out initial position size.  
  
Here's the link for the Kelly:  
[www.bjmath.com/bjmath/thorp/paper.htm](http://www.bjmath.com/bjmath/thorp/paper.htm)  
  
and you can always google Kelly System  
  
Happy Trading! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#48](/thread/post/213170#post213170 "Post Permalink")

  * Feb 10, 2007 4:04am  Feb 10, 2007 4:04am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar25698_4.gif) mikhaildgreat](mikhaildgreat)

  * | Joined Nov 2006  | Status: EA Programmer | [298 Posts](/search?do=process&provider=Member&searchuser=25698)

> [Quoting lexazver](/thread/post/212800#post212800 "View Quoted Post")
> 
> Disliked
> 
> Mikhail, one thing ive noticed is that your EA opens orders before candle closes i mean as soon as cross happens it opens a trade but the candle can close in the way that setup wouldnt happen , which brongs me to another point , i checked the chart that STRATEGY TESTER gave me and sometimes positions open when EMA5 crosses only one of the red lines and not the other which give negative trades but if you wait untill it crosses fully and then enter at the open of a new candle it gives good entry.
> 
> Ignored

Hello Sorry for the late reply just got back home... Anyways if you want to wait for candle to close before opening position simply set **ConfirmedOnEntry = true** This could be found in external variables.  
  
Hope that helps,  
Mikhail 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#49](/thread/post/213177#post213177 "Post Permalink")

  * Feb 10, 2007 4:12am  Feb 10, 2007 4:12am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar33539_4.gif) mwilkinw](mwilkinw)

  * | Joined Feb 2007  | Status: Trader | [27 Posts](/search?do=process&provider=Member&searchuser=33539)

> [Quoting FXLogic](/thread/post/213131#post213131 "View Quoted Post")
> 
> Disliked
> 
> Have you tested for other months, too? I'm just wondering how this would do in choppier markets, like we had for the first half of 2005 or during the summer of most any year. If it's profitable in those periods without any serious drawdowns, it may have a lot potential.
> 
> Ignored

  
Hey FXLogic.. I think there were some people on this thread that did extensive research on those time frames. I can only test over a year with 1Hr charts for some reason.. I tested it with the 1hr on the GBP YTD at 51.7% profitablity... This can definitely be stretched out with Money Mangement and Stop Losses set on the opposite side of the MA's rather than a set number.  
  
I also traded the GBP and EUR Crosses (I usually only trade those) and have had the same results... much better on the GBP/Yen and EUR/Yen crosses. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#50](/thread/post/213182#post213182 "Post Permalink")

  * Feb 10, 2007 4:17am  Feb 10, 2007 4:17am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar25698_4.gif) mikhaildgreat](mikhaildgreat)

  * | Joined Nov 2006  | Status: EA Programmer | [298 Posts](/search?do=process&provider=Member&searchuser=25698)

> [Quoting cgldsmth](/thread/post/212995#post212995 "View Quoted Post")
> 
> Disliked
> 
> mmm, the EA opened a buy on EURJPY at 1500GMT with no sign of a signal on the chart (M30)
> 
> Ignored

Hello This is a valid trade according to the rules in the EA. If you refer to the first post EA will take trade if a cross occurs in either the MACD or the MA and both signals agree. You would see that the MACD diped and crossed again back up to the zero line, at the same time MA was pointing in the same direction, so trade was taken.   
  
The trade was profitable anywyas right so no worries ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)  
  
Currently 3 closed trades from 3 different pairs all hit TP( my TP settings are exactly the same as that of the orginal method exept my stoploss is set at 20pips)  
Regards,  
Mikhail 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#51](/thread/post/213187#post213187 "Post Permalink")

  * Feb 10, 2007 4:32am  Feb 10, 2007 4:32am 

  * [ gtketum](gtketum)

  * | Joined Oct 2006  | Status: Trader | [68 Posts](/search?do=process&provider=Member&searchuser=21048)

so maybe forward testing with the EA is the way to go or is it too early to say. but 3 out of 3 so far does not look like a strategy that will produce such nice downward equity curves. well we will see, and Mikhail thanks for all the effort you are putting into this ea.  
  

> [Quoting mikhaildgreat](/thread/post/213182#post213182 "View Quoted Post")
> 
> Disliked
> 
> Hello This is a valid trade according to the rules in the EA. If you refer to the first post EA will take trade if a cross occurs in either the MACD or the MA and both signals agree. You would see that the MACD diped and crossed again back up to the zero line, at the same time MA was pointing in the same direction, so trade was taken.   
>    
>  The trade was profitable anywyas right so no worries ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)  
>    
>  Currently 3 closed trades from 3 different pairs all hit TP( my TP settings are exactly the same as that of the orginal method exept my stoploss is set at 20pips)  
>  Regards,  
>  Mikhail
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#52](/thread/post/213188#post213188 "Post Permalink")

  * Feb 10, 2007 4:35am  Feb 10, 2007 4:35am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar25698_4.gif) mikhaildgreat](mikhaildgreat)

  * | Joined Nov 2006  | Status: EA Programmer | [298 Posts](/search?do=process&provider=Member&searchuser=25698)

> [Quoting mwilkinw](/thread/post/213177#post213177 "View Quoted Post")
> 
> Disliked
> 
> Hey FXLogic.. I think there were some people on this thread that did extensive research on those time frames. I can only test over a year with 1Hr charts for some reason.. I tested it with the 1hr on the GBP YTD at 51.7% profitablity... This can definitely be stretched out with Money Mangement and Stop Losses set on the opposite side of the MA's rather than a set number.  
>    
>  I also traded the GBP and EUR Crosses (I usually only trade those) and have had the same results... much better on the GBP/Yen and EUR/Yen crosses.
> 
> Ignored

Hmm... thats a good idea but wouldnt we be sacrificing Risk Reward Ratio By doing this? putting SL above MAs would mean bigger stops and our gains per trade would still be really small...  
  
I think So many pips are wasted with these small TPs, I believe in letting the winners run, and cutting the losers short, IF we find a good exit strategy then we can do this, But on the other hand by doing this we are already making a whole new strategy...  
  
-Mikhail 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#53](/thread/post/213197#post213197 "Post Permalink")

  * Feb 10, 2007 4:45am  Feb 10, 2007 4:45am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar25698_4.gif) mikhaildgreat](mikhaildgreat)

  * | Joined Nov 2006  | Status: EA Programmer | [298 Posts](/search?do=process&provider=Member&searchuser=25698)

LOL! ![](https://resources.faireconomy.media/images/emojis/64/1f923.png?v=15.1) Thank you to whoever put that one star rating to this thread! LOL 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#54](/thread/post/213204#post213204 "Post Permalink")

  * Feb 10, 2007 4:51am  Feb 10, 2007 4:51am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar7129_7.gif) smjones](smjones)

  * Joined Mar 2006 | Status: THANK YOU MERLIN,TWEE and FF Team | [4,603 Posts](/search?do=process&provider=Member&searchuser=7129)

> [Quoting mikhaildgreat](/thread/post/213197#post213197 "View Quoted Post")
> 
> Disliked
> 
> LOL! ![](https://resources.faireconomy.media/images/emojis/64/1f923.png?v=15.1) Thank you to whoever put that one star rating to this thread! LOL
> 
> Ignored

Well that is taken care of... LOL I don't have enough to move it al the way up, but maybe others will pitch in 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#55](/thread/post/213210#post213210 "Post Permalink")

  * Feb 10, 2007 4:55am  Feb 10, 2007 4:55am 

  * [ Forex1man](forex1man)

  * | Joined Oct 2006  | Status: Trader | [58 Posts](/search?do=process&provider=Member&searchuser=21229)

Did the EA call this GBP/JPY Long ? And if so what price? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#56](/thread/post/213214#post213214 "Post Permalink")

  * Feb 10, 2007 4:59am  Feb 10, 2007 4:59am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar33539_4.gif) mwilkinw](mwilkinw)

  * | Joined Feb 2007  | Status: Trader | [27 Posts](/search?do=process&provider=Member&searchuser=33539)

> [Quoting mikhaildgreat](/thread/post/213188#post213188 "View Quoted Post")
> 
> Disliked
> 
> Hmm... thats a good idea but wouldnt we be sacrificing Risk Reward Ratio By doing this? putting SL above MAs would mean bigger stops and our gains per trade would still be really small...  
>    
>  I think So many pips are wasted with these small TPs, I believe in letting the winners run, and cutting the losers short, IF we find a good exit strategy then we can do this, But on the other hand by doing this we are already making a whole new strategy...  
>    
>  -Mikhail
> 
> Ignored

  
No not at all.. I said on the opposite side of the MA's (opposite side of what your position is) either using them as support or resistance.. this allows you to stay in the trade longer! This keeps the validity of the system but allows you to manipulate your exits for the most profit...  
  
I only suggest doing this after the trade is profitable. I enter the trade after the cross and have a SL of 30.. therefore I'm below the MA's initally. Once I'm profitable, either scale out and preserve profit and move SL to the MA's using them either as support or resistance depending on your trade... or scale in and do the same with the SL.   
  
Either way your maximizing your gains... because if you keep your stop the same as your entry position it will be on the opposite side of the MA's( which side, obviously depends on what trade you're in Long or Short) ... Therefore if you're stopped out it triggers an opposite order...where now your losses are larger than if you scaled in or out and moved your SL to the MA's.  
  
Either way it comes down to Money Management to get the most out of every trade... but that is the best way to squeeze as much profit from the trade as possible. And like you said, you have to let your winners run... Holding your SL at your inital entry and not scaling in or out can be detrimental! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#57](/thread/post/213223#post213223 "Post Permalink")

  * Feb 10, 2007 5:10am  Feb 10, 2007 5:10am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar25698_4.gif) mikhaildgreat](mikhaildgreat)

  * | Joined Nov 2006  | Status: EA Programmer | [298 Posts](/search?do=process&provider=Member&searchuser=25698)

> [Quoting mwilkinw](/thread/post/213214#post213214 "View Quoted Post")
> 
> Disliked
> 
> No not at all.. I said on the opposite side of the MA's (opposite side of what your position is) either using them as support or resistance.. this allows you to stay in the trade longer! This keeps the validity of the system but allows you to manipulate your exits for the most profit...  
>    
>  I only suggest doing this after the trade is profitable. I enter the trade after the cross and have a SL of 30.. therefore I'm below the MA's initally. Once I'm profitable, either scale out and preserve profit and move SL to the MA's using them either as support or resistance depending on your trade... or scale in and do the same with the SL.   
>    
>  Either way your maximizing your gains... because if you keep your stop the same as your entry position it will be on the opposite side of the MA's( which side, obviously depends on what trade you're in Long or Short) ... Therefore if you're stopped out it triggers an opposite order...where now your losses are larger than if you scaled in or out and moved your SL to the MA's.  
>    
>  Either way it comes down to Money Management to get the most out of every trade... but that is the best way to squeeze as much profit from the trade as possible. And like you said, you have to let your winners run... Holding your SL at your inital entry and not scaling in or out can be detrimental!
> 
> Ignored

We could explore further on this idea. but looking at the charts 85 and 75 MA looks to far if we are going to use it as some sort of trailing stop. We would be sacrificing so much significant profit here. Im thinking of adding another MA for trailing stop purposes only, like period 50(as used by another method that I cannot recall right now)  
  
Anyways we can explore more in this idea but I believe this should be a different method and EA, dont want to bastardize forexexpert310's method.  
  
Regards,  
Mikhail 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#58](/thread/post/213225#post213225 "Post Permalink")

  * Feb 10, 2007 5:12am  Feb 10, 2007 5:12am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar25698_4.gif) mikhaildgreat](mikhaildgreat)

  * | Joined Nov 2006  | Status: EA Programmer | [298 Posts](/search?do=process&provider=Member&searchuser=25698)

> [Quoting Forex1man](/thread/post/213210#post213210 "View Quoted Post")
> 
> Disliked
> 
> Did the EA call this GBP/JPY Long ? And if so what price?
> 
> Ignored

Sorry Im not testing GBPJPY because The original method did not mention trading this pair.  
  
-Mikhail 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#59](/thread/post/213229#post213229 "Post Permalink")

  * Feb 10, 2007 5:17am  Feb 10, 2007 5:17am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar33539_4.gif) mwilkinw](mwilkinw)

  * | Joined Feb 2007  | Status: Trader | [27 Posts](/search?do=process&provider=Member&searchuser=33539)

> [Quoting mikhaildgreat](/thread/post/213223#post213223 "View Quoted Post")
> 
> Disliked
> 
> We could explore further on this idea. but looking at the charts 85 and 75 MA looks to far if we are going to use it as some sort of trailing stop. We would be sacrificing so much significant profit here. Im thinking of adding another MA for trailing stop purposes only, like period 50(as used by another method that I cannot recall right now)  
>    
>  Anyways we can explore more in this idea but I believe this should be a different method and EA, dont want to bastardize forexexpert310's method.  
>    
>  Regards,  
>  Mikhail
> 
> Ignored

  
  
hahahha!! You're funny! Good work on the EA by the way! Of course we wouldn't want to "bastardize" anything! Unfortunately I must not be explaining myself correctly... I don't mean using the MA's for a trailing stop... but I'm looking forward to your Trailing stop MA (which I think is a good idea)! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#60](/thread/post/213247#post213247 "Post Permalink")

  * Feb 10, 2007 5:48am  Feb 10, 2007 5:48am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar25698_4.gif) mikhaildgreat](mikhaildgreat)

  * | Joined Nov 2006  | Status: EA Programmer | [298 Posts](/search?do=process&provider=Member&searchuser=25698)

> [Quoting mwilkinw](/thread/post/213229#post213229 "View Quoted Post")
> 
> Disliked
> 
> hahahha!! You're funny! Good work on the EA by the way! Of course we wouldn't want to "bastardize" anything! Unfortunately I must not be explaining myself correctly... I don't mean using the MA's for a trailing stop... but I'm looking forward to your Trailing stop MA (which I think is a good idea)!
> 
> Ignored

LOL, sorry for not understanding whatever you are trying to tell me. I'll read up on Kelly's MM method maybe after I read it I will understand the strategy you are proposing.  
  
But right now im signing out, im going out of town tomorrow, so best of luck at the market to all you traders.  
  
Regards,  
Mikhial 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * The Pouria EA Development Thread
  *   * [ **Reply to Thread** ](/thread/17242-the-pouria-ea-development-thread/reply#reply)

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

[The Pouria Method](/thread/17011-the-pouria-method "OKay here is one of the 4 best systems that I've made and used, with this system I pickup atleast 50 pips a day, I'm sharing this because...") 562 replies

[Lessons Learned during System Development](/thread/2986-lessons-learned-during-system-development "Hi, 
  
I've been reading through the forum and somehow I'm in the process of developing my own system.. But not really doing actual...") 29 replies

[(pouria method II on the test)](/thread/23104-pouria-method-ii-on-the-test "Hello  
pouria method II is now DONE thanks to the group of experts and mathematicians that helped and made this method. 
now we are...") 218 replies

[System Development Secrets](/thread/7342-system-development-secrets "&lt;meta http-equiv=&quot;CONTENT-TYPE&quot; content=&quot;text/html; charset=utf-8&quot;&gt;&lt;title&gt;&lt;/title&gt;&lt;meta name=&quot;GENERATOR&quot; content=&quot;OpenOffice.org 2.0 ...") 5 replies

[Metatrader 4 Development Course](/thread/5906-metatrader-4-development-course "Here is the Mql_4_Metatrader_4_Development_Course in pdf \(link fixed\) : 
 
http://www.freefilehosting.org/pupload/view/8711") 3 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/17242-the-pouria-ea-development-thread/reply#reply)
  * Subscribe
  * [45](javascript:void\(0\);)

Attachments: The Pouria EA Development Thread

Tags: The Pouria EA Development Thread

#  [](/thread/17242-the-pouria-ea-development-thread)The Pouria EA Development Thread 

  * 

  * [#61](/thread/post/213657#post213657 "Post Permalink")

  * Feb 11, 2007 12:18am  Feb 11, 2007 12:18am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar10333_10.gif) amenlo9](amenlo9)

  * | Joined May 2006  | Status: Trader | [600 Posts](/search?do=process&provider=Member&searchuser=10333)

can't believe this method have become so popular in just few days.![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#62](/thread/post/213664#post213664 "Post Permalink")

  * Feb 11, 2007 12:40am  Feb 11, 2007 12:40am 

  * [ JamDown](jamdown)

  * | Joined Dec 2006  | Status: Trader | [39 Posts](/search?do=process&provider=Member&searchuser=27324)

> [Quoting amenlo9](/thread/post/213657#post213657 "View Quoted Post")
> 
> Disliked
> 
> can't believe this method have become so popular in just few days.![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)
> 
> Ignored

I back tested the EA on the 15 minute chart GBP/USD for the month of January 07 with 10k, no stop loss, 1 lot. Profit $5715.00. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#63](/thread/post/213666#post213666 "Post Permalink")

  * Feb 11, 2007 12:44am  Feb 11, 2007 12:44am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar10333_10.gif) amenlo9](amenlo9)

  * | Joined May 2006  | Status: Trader | [600 Posts](/search?do=process&provider=Member&searchuser=10333)

> [Quoting JamDown](/thread/post/213664#post213664 "View Quoted Post")
> 
> Disliked
> 
> I back tested the EA on the 15 minute chart GBP/USD for the month of January 07 with 10k, no stop loss, 1 lot. Profit $5715.00.
> 
> Ignored

cool result.but would you trade live without SL?![](https://resources.faireconomy.media/images/emojis/64/1f61c.png?v=15.1): 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#64](/thread/post/213748#post213748 "Post Permalink")

  * Feb 11, 2007 3:28am  Feb 11, 2007 3:28am 

  * [ JamDown](jamdown)

  * | Joined Dec 2006  | Status: Trader | [39 Posts](/search?do=process&provider=Member&searchuser=27324)

> [Quoting amenlo9](/thread/post/213666#post213666 "View Quoted Post")
> 
> Disliked
> 
> cool result.but would you trade live without SL?![](https://resources.faireconomy.media/images/emojis/64/1f61c.png?v=15.1):
> 
> Ignored

I always have a mental stop loss and one that I put in before i go to the bathroom.   
I ran another test and 4 lots, 10k Jan1 - feb 9, No SL, TP 50, GBP/USD.  
Results Below.  
I think there might be a bug in the EA as it opened a buy order on 2/8/07 @ 1:00 for no reason. Thats why the last order is down 5000. If thats fixed it would be a sell and would have close with 50pips.   
This thing is amazing if you have 10 to throw at it without feelings. 

Attached File(s)

![File Type: doc](https://assets.faireconomy.media/images/attach/doc.gif) [PMEA.doc](/attachment/file/22011?d=1171132625) 78 KB | 528 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#65](/thread/post/213765#post213765 "Post Permalink")

  * Feb 11, 2007 4:02am  Feb 11, 2007 4:02am 

  * [ BearPaw](bearpaw)

  * | Joined Jul 2006  | Status: A Trader for Life | [218 Posts](/search?do=process&provider=Member&searchuser=13999)

> [Quoting JamDown](/thread/post/213748#post213748 "View Quoted Post")
> 
> Disliked
> 
> I always have a mental stop loss and one that I put in before i go to the bathroom.   
>  I ran another test and 4 lots, 10k Jan1 - feb 9, No SL, TP 50, GBP/USD.  
>  Results Below.  
>  I think there might be a bug in the EA as it opened a buy order on 2/8/07 @ 1:00 for no reason. Thats why the last order is down 5000. If thats fixed it would be a sell and would have close with 50pips.   
>  This thing is amazing if you have 10 to throw at it without feelings.
> 
> Ignored

That's interesting JamDown. So, maximum drawdown was 5k, and it was never hit? It never hit margin requirements? Was that the farthest it went down? What about November when the GBP skyrocketed up? What about back testing it a couple more months to see what happens there?   
  
Thanks for your results though!!  
  
BP 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#66](/thread/post/213769#post213769 "Post Permalink")

  * Feb 11, 2007 4:08am  Feb 11, 2007 4:08am 

  * [ JamDown](jamdown)

  * | Joined Dec 2006  | Status: Trader | [39 Posts](/search?do=process&provider=Member&searchuser=27324)

> [Quoting BearPaw](/thread/post/213765#post213765 "View Quoted Post")
> 
> Disliked
> 
> That's interesting JamDown. So, maximum drawdown was 5k, and it was never hit? It never hit margin requirements? Was that the farthest it went down? What about November when the GBP skyrocketed up? What about back testing it a couple more months to see what happens there?   
>    
>  Thanks for your results though!!  
>    
>  BP
> 
> Ignored

Here are the results from the USDJPY. SL is the killer for this EA. You just have to keep an eye on your trade. 

Attached File(s)

![File Type: doc](https://assets.faireconomy.media/images/attach/doc.gif) [USDJPY PM EA results.doc](/attachment/file/22018?d=1171134421) 8 KB | 531 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#67](/thread/post/213780#post213780 "Post Permalink")

  * Feb 11, 2007 4:29am  Feb 11, 2007 4:29am 

  * [ BearPaw](bearpaw)

  * | Joined Jul 2006  | Status: A Trader for Life | [218 Posts](/search?do=process&provider=Member&searchuser=13999)

> [Quoting JamDown](/thread/post/213769#post213769 "View Quoted Post")
> 
> Disliked
> 
> Here are the results from the USDJPY. SL is the killer for this EA. You just have to keep an eye on your trade.
> 
> Ignored

But...once again JamDown...during the course of the trade...what is the maximum drawdown? Does it go down 20%, 50%? That would make a difference.  
  
Thanks for your research.  
  
BP 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#68](/thread/post/213790#post213790 "Post Permalink")

  * Feb 11, 2007 5:03am  Feb 11, 2007 5:03am 

  * [ JamDown](jamdown)

  * | Joined Dec 2006  | Status: Trader | [39 Posts](/search?do=process&provider=Member&searchuser=27324)

> [Quoting BearPaw](/thread/post/213780#post213780 "View Quoted Post")
> 
> Disliked
> 
> But...once again JamDown...during the course of the trade...what is the maximum drawdown? Does it go down 20%, 50%? That would make a difference.  
>    
>  Thanks for your research.  
>    
>  BP
> 
> Ignored

The drawdown is in the report 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#69](/thread/post/213827#post213827 "Post Permalink")

  * Feb 11, 2007 6:24am  Feb 11, 2007 6:24am 

  * [ BearPaw](bearpaw)

  * | Joined Jul 2006  | Status: A Trader for Life | [218 Posts](/search?do=process&provider=Member&searchuser=13999)

> [Quoting JamDown](/thread/post/213790#post213790 "View Quoted Post")
> 
> Disliked
> 
> The drawdown is in the report
> 
> Ignored

Maybe I am just not understanding your report then, but it shows absolute, maximal, and relative drawdown as zero. But what I am wondering is during an open trade...even though it is not closed out, how far into the negative does it go before it swings back up?  
  
Thanks JamDown.  
  
BP 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#70](/thread/post/213835#post213835 "Post Permalink")

  * Feb 11, 2007 6:43am  Feb 11, 2007 6:43am 

  * [ JamDown](jamdown)

  * | Joined Dec 2006  | Status: Trader | [39 Posts](/search?do=process&provider=Member&searchuser=27324)

> [Quoting BearPaw](/thread/post/213827#post213827 "View Quoted Post")
> 
> Disliked
> 
> Maybe I am just not understanding your report then, but it shows absolute, maximal, and relative drawdown as zero. But what I am wondering is during an open trade...even though it is not closed out, how far into the negative does it go before it swings back up?  
>    
>  Thanks JamDown.  
>    
>  BP
> 
> Ignored

I will look at that and post the results 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#71](/thread/post/213990#post213990 "Post Permalink")

  * Feb 11, 2007 2:42pm  Feb 11, 2007 2:42pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar25698_4.gif) mikhaildgreat](mikhaildgreat)

  * | Joined Nov 2006  | Status: EA Programmer | [298 Posts](/search?do=process&provider=Member&searchuser=25698)

Hey guys just got back from my short trip. I see you finally found good backtests results. But No stop loss is very dangerouse dont you think? I will experement on other stoploss, like mwilkinw suggested where SL will be placed just above or below 85, 75 MA. Will post updated EA later today.  
  
And I also dont really trust strategy tester, manual backtesting is still more reliable. becasue stategy tester just estimates what happens within a minute, try using visual mode and during long bars look how many times the long bars goes up and down to its low and high sometimes several times before closing which we really dont in the actual market. Just something to think about...  
  
-Mikhail 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#72](/thread/post/214011#post214011 "Post Permalink")

  * Feb 11, 2007 3:45pm  Feb 11, 2007 3:45pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar25698_4.gif) mikhaildgreat](mikhaildgreat)

  * | Joined Nov 2006  | Status: EA Programmer | [298 Posts](/search?do=process&provider=Member&searchuser=25698)

> [Quoting mwilkinw](/thread/post/213137#post213137 "View Quoted Post")
> 
> Disliked
> 
> Hey NKE! The 'half kelly" is a money management system. Essentially the kelly system is a bet sizing system. It was made popular by the MIT prof. Edward Thorp, the man who inveted hi-lo card counting for blackjack and broke Vegas. After cleaning up, he published his card counting strategy (resulting in the prosecution of card counters from that day on). He used the Kelly System for placing his bets.  
>    
>  He started a hedge fund and used the "helf kelly" system for placing trades... basically using the kelly but the initial position is half of a normal kelly bet. His success brought this system popularity in securities trading and variations of it have been used by traders and fund managers ever since!  
>    
>  I use a half kelly system on my initial trade position and add to my position as the account increases... still using the kelly system to either get out of my trades or figure out initial position size.  
>    
>  Here's the link for the Kelly:  
>  [www.bjmath.com/bjmath/thorp/paper.htm](http://www.bjmath.com/bjmath/thorp/paper.htm)  
>    
>  and you can always google Kelly System  
>    
>  Happy Trading!
> 
> Ignored

Hello Again,I just finished reading the paper about the Kelly system sounds very interesting and very relevant to our goals as traders. But to be honest i didnt understand a single thing with all those formulas. I have to admit I'm not very good in calculus with all those F'(x) and stuff made my head numb. were you able to understand the paper and are you able to apply it? I really would like to learn but not with calculus language. I'm very good with mathematical logic, thats why im a programmer, But when it comes to those kind of formulas i suddenly get dyslexia.  
  
mwilkinw can you kindly explain as simple as possible the practical approach of using the formulas when it comes to forex trading? I think this is very important, it deals with position sizing to maximize investment growth but I just cant undertand it. ![](https://resources.faireconomy.media/images/emojis/64/1f61e.png?v=15.1)  
  
-Mikhail 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#73](/thread/post/214035#post214035 "Post Permalink")

  * Feb 11, 2007 5:28pm  Feb 11, 2007 5:28pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar22836_4.gif) ilanr](ilanr)

  * | Joined Oct 2006  | Status: Trader | [260 Posts](/search?do=process&provider=Member&searchuser=22836)

> [Quoting mikhaildgreat](/thread/post/214011#post214011 "View Quoted Post")
> 
> Disliked
> 
> mwilkinw can you kindly explain as simple as possible the practical approach of using the formulas when it comes to forex trading? I think this is very important, it deals with position sizing to maximize investment growth but I just cant undertand it. ![](https://resources.faireconomy.media/images/emojis/64/1f61e.png?v=15.1)  
>    
>  -Mikhail
> 
> Ignored

Indeed, this is of utmost importance. Kelly's formula provides you with the optimal percent of your capital you can risk on a single trade. To use the formula, you have to know the history of a trading system performance: what is the size of a win W (or average win size if it varies), what is the size of a loss L (or its average) and the proportion P of wins out of total number of bets. The assumption is that you place one bet (trade) at a time. Kelly's percent is calculated then using this simple formula:  
  
Kelly% = P - [(1-P)/(W/L]   
  
For example, take Pouria's trades for Jan-Feb 2006 (I'm just starting optimizing this method...). If you'd use a 46 p. SL and a 33 p. TP target (spread not taken into account), you'd have 5 losses and 33 wins (P = .87). So, Kelly% is   
  
Kelly% = .87 - [(1-.87)/(33/46)] = .69.  
  
This means, that you can risk 69% of your capital on a single trade. If you have a 1000 p. capital, and you can risk 690 p., you can you can open 690/46 = 15 positions (again, spread and margin considerations nottaken into account).  
  
Since Kelly% is based on historical performance, and history never repeats itself (at least, the better parts of history, the worst ones tend to repeat over and over again), and since using exact Kelly% leads to huge drawdowns, and since most people don't have the nerve for such a risk, it's customary to use half the Kelly's percent, i.e., in our example, open 7 positions. I don't even have the nerve for that, and usually don't risk more than 15% simulteneously...  
  
mwilkinw, please correct me if I got something wrong. I teach statistics, but always have all my calculus messed up... ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

sans peur et sans reproche

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#74](/thread/post/214039#post214039 "Post Permalink")

  * Feb 11, 2007 5:56pm  Feb 11, 2007 5:56pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar33539_4.gif) mwilkinw](mwilkinw)

  * | Joined Feb 2007  | Status: Trader | [27 Posts](/search?do=process&provider=Member&searchuser=33539)

> [Quoting ilanr](/thread/post/214035#post214035 "View Quoted Post")
> 
> Disliked
> 
> Indeed, this is of utmost importance. Kelly's formula provides you with the optimal percent of your capital you can risk on a single trade. To use the formula, you have to know the history of a trading system performance: what is the size of a win W (or average win size if it varies), what is the size of a loss L (or its average) and the proportion P of wins out of total number of bets. The assumption is that you place one bet (trade) at a time. Kelly's percent is calculated then using this simple formula:  
>    
>  Kelly% = P - [(1-P)/(W/L]   
>    
>  For example, take Pouria's trades for Jan-Feb 2006 (I'm just starting optimizing this method...). If you'd use a 46 p. SL and a 33 p. TP target (spread not taken into account), you'd have 5 losses and 33 wins (P = .87). So, Kelly% is   
>    
>  Kelly% = .87 - [(1-.87)/(33/46)] = .69.  
>    
>  This means, that you can risk 69% of your capital on a single trade. If you have a 1000 p. capital, and you can risk 690 p., you can you can open 690/46 = 15 positions (again, spread and margin considerations nottaken into account).  
>    
>  Since Kelly% is based on historical performance, and history never repeats itself (at least, the better parts of history, the worst ones tend to repeat over and over again), and since using exact Kelly% leads to huge drawdowns, and since most people don't have the nerve for such a risk, it's customary to use half the Kelly's percent, i.e., in our example, open 7 positions. I don't even have the nerve for that, and usually don't risk more than 15% simulteneously...  
>    
>  mwilkinw, please correct me if I got something wrong. I teach statistics, but always have all my calculus messed up... ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)
> 
> Ignored

  
Hey Ilanr! Thanks for doing some of the clarifying for me! The Kelly formula is a great formula for traders  
  
That formula is correct. The kelly formula allows you to figure out your position size based on past performace. (that is why I like backtesting so much)... Having your total profit percentage, your average win, and your average loss will allow you to formulate how large your trade or (bet size) will be as a percentage of your equity.  
  
This is a great way to increase your profits, because as your equity grows your bet sizes grow. This allows you to add to your winning trades and minimize your losses with a set SL.  
  
Figuring out where to take your profit and where your SL is... and backtesting to receive your Profit%, Average Win, Average Loss Data... based on your historical performance, gives you a much better system of increasing your profits and managing your downside without burning out your account.  
  
However, as was stated for securities trading I suggest a 'half kelly" system. I use 80% of the kelly... 80% of the kelly figure is practical and will optimize your rate of return. Determine how many trades you are likely to have on at one time and then divide your 80%-Kelly value by that number of trades.  
  
Increasing your position by the Kelly-Value determined by your increased equity will exponentially grow the size of your winners and keep your losers at a steady loss as determined by your SL.  
  
If you use a strict money management system and know your profitibility, average wins and average losses.. theoretically you will be profitable.  
  
This system was made famous by Dr. Edward Thorp and is used to beat the dealer in blackjack... this is how he broke Vegas and eventually made billions with his hedge fund from the 60's to the 80's.  
  
Optimum Risk Percent = W% - [(1-W%)/(W/L)]  
(W%) is your winning percentage, (W) is the average size of your winning trades, (L) is the average size of your losing trades  
  
This is a critical system for traders who want optimal rates of return. For practical application, use the 80%-Kelly Value for your trading.  
  
Plug in your data and solve left to right.  
  
Happy Trading!  
  
P.S. Ilanr.. you're a statistician... I'm a mathematician! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#75](/thread/post/214057#post214057 "Post Permalink")

  * Feb 11, 2007 6:54pm  Feb 11, 2007 6:54pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar5179_4.gif) cgldsmth](cgldsmth)

  * Joined Dec 2005 | Status: It's only money | [1,413 Posts](/search?do=process&provider=Member&searchuser=5179)

great! so we just need the values of for the formula for each currency pair going back over a decent timeframe, say 1 year. 

TRADE FOR SWAP

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#76](/thread/post/214058#post214058 "Post Permalink")

  * Feb 11, 2007 6:57pm  Feb 11, 2007 6:57pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar22836_4.gif) ilanr](ilanr)

  * | Joined Oct 2006  | Status: Trader | [260 Posts](/search?do=process&provider=Member&searchuser=22836)

> [Quoting mwilkinw](/thread/post/214039#post214039 "View Quoted Post")
> 
> Disliked
> 
> snip... The kelly formula allows you to figure out your position size based on past performace. (that is why I like backtesting so much)... snip... Ilanr.. you're a statistician... I'm a mathematician!
> 
> Ignored

Actually, I'm not a statistician, I only teach statistics. I'm a psychologist specializing, among other things, in evaluation and assessment. That is why I only rely on past performance as a predictor of future performance, and that is why I spend my days backtesting, although, unlike you, I don't "like" backtesting. Actually, I hate it ![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1). 

sans peur et sans reproche

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#77](/thread/post/214100#post214100 "Post Permalink")

  * Feb 11, 2007 9:12pm  Feb 11, 2007 9:12pm 

  * [ JamDown](jamdown)

  * | Joined Dec 2006  | Status: Trader | [39 Posts](/search?do=process&provider=Member&searchuser=27324)

> [Quoting mikhaildgreat](/thread/post/212670#post212670 "View Quoted Post")
> 
> Disliked
> 
> LOL I agree.   
>    
>  Its wierd though when you test it starting 2007 it does pretty well. but everything before that just doesnt work... so when backtesting pls enable visiual mode then load the indicators in the testing charts to see if the Expert is doing things that is against the original pouria method. If its faithful to the method then the problem is just optimization, if its still not profitable after optimization then the problem is either strategy tester (which could likely be because we have small TP and SL levels) or the strategy itself needs rethinking...  
>    
>  -Mikhail
> 
> Ignored

I tested the EURUSD and i could not find a combination that worked. But by looking at the visual for last month it seemed as if the buy and sell were reversed it would have been extremely profitable.  
Another thing.   
If there was a way to incorporate the Takeprofit EA thats floating around in FF into the POEA we could take advantage of the big moves by having it close a portion of our order and moving our stops to where we want them.   
BigDog 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#78](/thread/post/214102#post214102 "Post Permalink")

  * Feb 11, 2007 9:18pm  Feb 11, 2007 9:18pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar25698_4.gif) mikhaildgreat](mikhaildgreat)

  * | Joined Nov 2006  | Status: EA Programmer | [298 Posts](/search?do=process&provider=Member&searchuser=25698)

****mwilkinw******,****ilanr** thank you thank you thank you GREAT GREAT GREAT Stuff! Now this could be applied to all the programs I am doing and using! the EA must be able to collect all the statistical data during forward testing, It must save it in the CSV file then use that to compute the optimal Lot size per trade. WOW! this is like the best money management system i ever came across! The more trades the EA makes the better it will be able to assign the optimal position size!  
  
Thank you to both of you I will start working on this immediately!  
  
Thank you once again,  
Mikhail 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#79](/thread/post/214126#post214126 "Post Permalink")

  * Feb 11, 2007 10:58pm  Feb 11, 2007 10:58pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar29751_4.gif) lexazver](lexazver)

  * | Joined Dec 2006  | Status: o_O | [1,511 Posts](/search?do=process&provider=Member&searchuser=29751)

Ok ive manualy backtested EURUSD for september,october and november,with stop of 14 including the spread and here are the results ( they of course may not be accurate 100%)  
W-winners or profitable trades  
L-looosers or losses ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
**SEP  
**when tp=15 you get  
15W-10L = **+85**  
  
when tp=20  
13W-12L = **+92**  
  
**OCT  
**when tp=15  
10W-12L= **-18**  
  
when tp=20  
9W-13L = **-2  
  
NOV  
  
**when tp =15  
10W-9L= **+24**  
  
when tp=20  
9W-10L = **+40  
  
Max consecutive wins when tp(15)=4, when tp(20)=3  
Max consecutive losses when tp(15)=4, when tp(20)=5  
**So far January showed best results ( posted earlier) for EURUSD , i havent tested any other pairs.  

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#80](/thread/post/214134#post214134 "Post Permalink")

  * Feb 11, 2007 11:09pm  Feb 11, 2007 11:09pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar10333_10.gif) amenlo9](amenlo9)

  * | Joined May 2006  | Status: Trader | [600 Posts](/search?do=process&provider=Member&searchuser=10333)

> [Quoting lexazver](/thread/post/214126#post214126 "View Quoted Post")
> 
> Disliked
> 
> Ok ive manualy backtested EURUSD for september,october and november,with stop of 14 including the spread and here are the results ( they of course may not be accurate 100%)  
>  W-winners or profitable trades  
>  L-looosers or losses ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
>  **SEP  
>  **when tp=15 you get  
>  15W-10L = **+85**  
>    
>  when tp=20  
>  13W-12L = **+92**  
>    
>  **OCT  
>  **when tp=15  
>  10W-12L= **-18**  
>    
>  when tp=20  
>  9W-13L = **-2  
>    
>  NOV  
>    
>  **when tp =15  
>  10W-9L= **+24**  
>    
>  when tp=20  
>  9W-10L = **+40  
>    
>  Max consecutive wins when tp(15)=4, when tp(20)=3  
>  Max consecutive losses when tp(15)=4, when tp(20)=5  
>  **So far January showed best results ( posted earlier) for EURUSD , i havent tested any other pairs.  
> 
> 
> Ignored

i wonder if set the TP=10,will get better result? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * The Pouria EA Development Thread
  *   * [ **Reply to Thread** ](/thread/17242-the-pouria-ea-development-thread/reply#reply)

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

[The Pouria Method](/thread/17011-the-pouria-method "OKay here is one of the 4 best systems that I've made and used, with this system I pickup atleast 50 pips a day, I'm sharing this because...") 562 replies

[Lessons Learned during System Development](/thread/2986-lessons-learned-during-system-development "Hi, 
  
I've been reading through the forum and somehow I'm in the process of developing my own system.. But not really doing actual...") 29 replies

[(pouria method II on the test)](/thread/23104-pouria-method-ii-on-the-test "Hello  
pouria method II is now DONE thanks to the group of experts and mathematicians that helped and made this method. 
now we are...") 218 replies

[System Development Secrets](/thread/7342-system-development-secrets "&lt;meta http-equiv=&quot;CONTENT-TYPE&quot; content=&quot;text/html; charset=utf-8&quot;&gt;&lt;title&gt;&lt;/title&gt;&lt;meta name=&quot;GENERATOR&quot; content=&quot;OpenOffice.org 2.0 ...") 5 replies

[Metatrader 4 Development Course](/thread/5906-metatrader-4-development-course "Here is the Mql_4_Metatrader_4_Development_Course in pdf \(link fixed\) : 
 
http://www.freefilehosting.org/pupload/view/8711") 3 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/17242-the-pouria-ea-development-thread/reply#reply)
  * Subscribe
  * [45](javascript:void\(0\);)

Attachments: The Pouria EA Development Thread

Tags: The Pouria EA Development Thread

#  [](/thread/17242-the-pouria-ea-development-thread)The Pouria EA Development Thread 

  * 

  * [#81](/thread/post/214147#post214147 "Post Permalink")

  * Feb 11, 2007 11:41pm  Feb 11, 2007 11:41pm 

  * [ JamDown](jamdown)

  * | Joined Dec 2006  | Status: Trader | [39 Posts](/search?do=process&provider=Member&searchuser=27324)

> [Quoting mikhaildgreat](/thread/post/214102#post214102 "View Quoted Post")
> 
> Disliked
> 
> ****mwilkinw******,****ilanr** thank you thank you thank you GREAT GREAT GREAT Stuff! Now this could be applied to all the programs I am doing and using! the EA must be able to collect all the statistical data during forward testing, It must save it in the CSV file then use that to compute the optimal Lot size per trade. WOW! this is like the best money management system i ever came across! The more trades the EA makes the better it will be able to assign the optimal position size!  
>    
>  Thank you to both of you I will start working on this immediately!  
>    
>    
>  Thank you once again,  
>  Mikhail
> 
> Ignored

MikhailDGreat,  
I know this might sound ridiculous and too much to ask but could you do a reverse of the buy/sell order for the EA for me. I have an idea that I think might be beneficial in certain types of market conditions for certain pairs. I need it to buy when we should typically be selling and VV. Thanks  
BigDog. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#82](/thread/post/214157#post214157 "Post Permalink")

  * Feb 12, 2007 12:12am  Feb 12, 2007 12:12am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar25698_4.gif) mikhaildgreat](mikhaildgreat)

  * | Joined Nov 2006  | Status: EA Programmer | [298 Posts](/search?do=process&provider=Member&searchuser=25698)

LOL!  
  
No Problem, Here you go! tell us if you find it be profitable.  
  
Regards,  
Mikhail  
  

> [Quoting JamDown](/thread/post/214147#post214147 "View Quoted Post")
> 
> Disliked
> 
> MikhailDGreat,  
>  I know this might sound ridiculous and too much to ask but could you do a reverse of the buy/sell order for the EA for me. I have an idea that I think might be beneficial in certain types of market conditions for certain pairs. I need it to buy when we should typically be selling and VV. Thanks  
>  BigDog.
> 
> Ignored

Attached File(s)

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [Pouria EA Beta - Reversed.mq4](/attachment/file/22089?d=1171206716) 13 KB | 438 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#83](/thread/post/214160#post214160 "Post Permalink")

  * Feb 12, 2007 12:22am  Feb 12, 2007 12:22am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar25698_4.gif) mikhaildgreat](mikhaildgreat)

  * | Joined Nov 2006  | Status: EA Programmer | [298 Posts](/search?do=process&provider=Member&searchuser=25698)

Hello Attached is the new version of the EA with a few minor but important bug fix. **If you are forward testing the original version pls stop using the older version and use this instead.  
**  
Thanks,  
-Mikhail 

Attached File(s)

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [Pouria EA Beta 2.mq4](/attachment/file/22090?d=1171207334) 13 KB | 658 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#84](/thread/post/214161#post214161 "Post Permalink")

  * Feb 12, 2007 12:23am  Feb 12, 2007 12:23am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar10333_10.gif) amenlo9](amenlo9)

  * | Joined May 2006  | Status: Trader | [600 Posts](/search?do=process&provider=Member&searchuser=10333)

> [Quoting mikhaildgreat](/thread/post/214157#post214157 "View Quoted Post")
> 
> Disliked
> 
> LOL!  
>    
>  No Problem, Here you go! tell us if you find it be profitable.  
>    
>  Regards,  
>  Mikhail
> 
> Ignored

Mikhail,you are the man!!!!!!!!!![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)  
  
can't wait the new week start!! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#85](/thread/post/214162#post214162 "Post Permalink")

  * Feb 12, 2007 12:27am  Feb 12, 2007 12:27am 

  * [ BearPaw](bearpaw)

  * | Joined Jul 2006  | Status: A Trader for Life | [218 Posts](/search?do=process&provider=Member&searchuser=13999)

> [Quoting mikhaildgreat](/thread/post/214160#post214160 "View Quoted Post")
> 
> Disliked
> 
> Hello Attached is the new version of the EA with a few minor but important bug fix. **If you are forward testing the original version pls stop using the older version and use this instead.**  
>    
>  Thanks,  
>  -Mikhail
> 
> Ignored

Thanks Mikhail,  
  
Is it possible for you to document what changes have been made?  
  
Thanks again.  
  
BP 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#86](/thread/post/214166#post214166 "Post Permalink")

  * Feb 12, 2007 12:36am  Feb 12, 2007 12:36am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar25698_4.gif) mikhaildgreat](mikhaildgreat)

  * | Joined Nov 2006  | Status: EA Programmer | [298 Posts](/search?do=process&provider=Member&searchuser=25698)

> [Quoting BearPaw](/thread/post/214162#post214162 "View Quoted Post")
> 
> Disliked
> 
> Thanks Mikhail,  
>    
>  Is it possible for you to document what changes have been made?  
>    
>  Thanks again.  
>    
>  BP
> 
> Ignored

Not much really, just that the first version might generate false signals with MACD signals due to my mistake in the encoding.  
  
-Mikhail 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#87](/thread/post/214167#post214167 "Post Permalink")

  * Feb 12, 2007 12:42am  Feb 12, 2007 12:42am 

  * [ BearPaw](bearpaw)

  * | Joined Jul 2006  | Status: A Trader for Life | [218 Posts](/search?do=process&provider=Member&searchuser=13999)

> [Quoting mikhaildgreat](/thread/post/214166#post214166 "View Quoted Post")
> 
> Disliked
> 
> Not much really, just that the first version might generate false signals with MACD signals due to my mistake in the encoding.  
>    
>  -Mikhail
> 
> Ignored

Thanks....wonderful....we shall see how it goes!!  
  
So, do you think the backtesting is not reliable? And we shall just see with the forward testing?  
  
Thanks again.  
  
BP 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#88](/thread/post/214169#post214169 "Post Permalink")

  * Feb 12, 2007 12:50am  Feb 12, 2007 12:50am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar25698_4.gif) mikhaildgreat](mikhaildgreat)

  * | Joined Nov 2006  | Status: EA Programmer | [298 Posts](/search?do=process&provider=Member&searchuser=25698)

> [Quoting BearPaw](/thread/post/214167#post214167 "View Quoted Post")
> 
> Disliked
> 
> Thanks....wonderful....we shall see how it goes!!  
>    
>  So, do you think the backtesting is not reliable? And we shall just see with the forward testing?  
>    
>  Thanks again.  
>    
>  BP
> 
> Ignored

I prefer manual backtesting, I dont trust metatraders Strategy tester. especially with small targets. If this EA had at least 50pip or 30pip SL and TP then strategy tester could generate more or less accurate results. But with such a tight SL and TP the results will be truely flawed. Just like cyberia trader which does insanely well during backtest with strategy tester but during actual trading it trades very very differently with poor results.  
  
I believe its best to know the strategy then backtest using your eyes instead...  
  
-Mikhail 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#89](/thread/post/214171#post214171 "Post Permalink")

  * Feb 12, 2007 12:57am  Feb 12, 2007 12:57am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar5179_4.gif) cgldsmth](cgldsmth)

  * Joined Dec 2005 | Status: It's only money | [1,413 Posts](/search?do=process&provider=Member&searchuser=5179)

Mikhail - awesome stuff.  
  
the next thing is to get the managetakeprofitEA code into it so we can take partil profits and makethe mostof some of the big trends this method gets. 

TRADE FOR SWAP

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#90](/thread/post/214178#post214178 "Post Permalink")

  * Feb 12, 2007 1:17am  Feb 12, 2007 1:17am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar25698_4.gif) mikhaildgreat](mikhaildgreat)

  * | Joined Nov 2006  | Status: EA Programmer | [298 Posts](/search?do=process&provider=Member&searchuser=25698)

> [Quoting cgldsmth](/thread/post/214171#post214171 "View Quoted Post")
> 
> Disliked
> 
> Mikhail - awesome stuff.  
>    
>  the next thing is to get the managetakeprofitEA code into it so we can take partil profits and makethe mostof some of the big trends this method gets.
> 
> Ignored

Yup I know but the question here is when to take profit? We need to find a better exit strategy to find the optimal time to exit.  
  
If you or anyone has a good idea how to exit that would maximize the big trend please post it. because we cannot simply exit using when we get reverse entry signal because we will be exiting too late sacrificing profits as well...  
  
-Mikhail 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#91](/thread/post/214191#post214191 "Post Permalink")

  * Feb 12, 2007 1:55am  Feb 12, 2007 1:55am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar5179_4.gif) cgldsmth](cgldsmth)

  * Joined Dec 2005 | Status: It's only money | [1,413 Posts](/search?do=process&provider=Member&searchuser=5179)

One way would be to backtest and find the average pips each signal gives on each pair. Although that's very laborious. How about a good old trail-lock? 

TRADE FOR SWAP

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#92](/thread/post/214200#post214200 "Post Permalink")

  * Feb 12, 2007 2:19am  Feb 12, 2007 2:19am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar25698_4.gif) mikhaildgreat](mikhaildgreat)

  * | Joined Nov 2006  | Status: EA Programmer | [298 Posts](/search?do=process&provider=Member&searchuser=25698)

> [Quoting cgldsmth](/thread/post/214191#post214191 "View Quoted Post")
> 
> Disliked
> 
> One way would be to backtest and find the average pips each signal gives on each pair. Although that's very laborious. How about a good old trail-lock?
> 
> Ignored

we can give it a try... will post EA with trail stop tomorrow.  
  
-mikhail 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#93](/thread/post/214211#post214211 "Post Permalink")

  * Feb 12, 2007 2:41am  Feb 12, 2007 2:41am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar7129_7.gif) smjones](smjones)

  * Joined Mar 2006 | Status: THANK YOU MERLIN,TWEE and FF Team | [4,603 Posts](/search?do=process&provider=Member&searchuser=7129)

Well I can think of two exit strats that would work well with this approach.   
  
1\. use fibs off of the tunnel just like Vegas style  
  
2\. use ATR to determine exits in the same style as Turtle trading. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#94](/thread/post/214214#post214214 "Post Permalink")

  * Feb 12, 2007 2:48am  Feb 12, 2007 2:48am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar5179_4.gif) cgldsmth](cgldsmth)

  * Joined Dec 2005 | Status: It's only money | [1,413 Posts](/search?do=process&provider=Member&searchuser=5179)

so divide the trade into 3, then exit at 55, 89, and 144 pips? 

TRADE FOR SWAP

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#95](/thread/post/214218#post214218 "Post Permalink")

  * Feb 12, 2007 2:50am  Feb 12, 2007 2:50am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar7129_7.gif) smjones](smjones)

  * Joined Mar 2006 | Status: THANK YOU MERLIN,TWEE and FF Team | [4,603 Posts](/search?do=process&provider=Member&searchuser=7129)

Correction, fibs off the fast moving ma not the tunnel, because price is usually no where near the tunnel  
  
I was more thinking about looking at each currency and seeing what fib level price tends to congregate and using that level, but I see no reason why you could not have multiple exits... The only problem with this, is it does not maximize the potential profit, but it does make for a larger number of profitable trades. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#96](/thread/post/214280#post214280 "Post Permalink")

  * Edited 5:01am  Feb 12, 2007 4:39am | Edited 5:01am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar7129_7.gif) smjones](smjones)

  * Joined Mar 2006 | Status: THANK YOU MERLIN,TWEE and FF Team | [4,603 Posts](/search?do=process&provider=Member&searchuser=7129)

> [Quoting mikhaildgreat](/thread/post/214011#post214011 "View Quoted Post")
> 
> Disliked
> 
> Hello Again,I just finished reading the paper about the Kelly system sounds very interesting and very relevant to our goals as traders. But to be honest i didnt understand a single thing with all those formulas. I have to admit I'm not very good in calculus with all those F'(x) and stuff made my head numb. were you able to understand the paper and are you able to apply it? I really would like to learn but not with calculus language. I'm very good with mathematical logic, thats why im a programmer, But when it comes to those kind of formulas i suddenly get dyslexia.  
>    
>  mwilkinw can you kindly explain as simple as possible the practical approach of using the formulas when it comes to forex trading? I think this is very important, it deals with position sizing to maximize investment growth but I just cant undertand it. ![](https://resources.faireconomy.media/images/emojis/64/1f61e.png?v=15.1)  
>    
>  -Mikhail
> 
> Ignored

Hi, after reading Fortunes Formula and Ed Thorp's mathematics of gambling, this is how I have interpreted Kelly Criteria. I put it in a small spread sheet.  
  
Don't know if it will help you with this, but I think you can see what the formula is getting at...  
The problem is that this style of MM is as aggressive as is possible, so there is a lot of risk of loss. Just not a great risk of ruin, because you can always get closer to zero. Mathematically it is true, but when your account is $10 the point is esoteric at best.  
  
Here is a thread that talks about it at length and this post in particular   
[http://www.forexfactory.com/showpost...2&postcount=16](http://www.forexfactory.com/showpost.php?p=172192&postcount=16)

Attached File(s)

![File Type: zip](https://assets.faireconomy.media/images/attach/zip.gif) [Kelly Risk Percentage.zip](/attachment/file/22105?d=1171222738) 2 KB | 468 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#97](/thread/post/214305#post214305 "Post Permalink")

  * Feb 12, 2007 5:09am  Feb 12, 2007 5:09am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar33539_4.gif) mwilkinw](mwilkinw)

  * | Joined Feb 2007  | Status: Trader | [27 Posts](/search?do=process&provider=Member&searchuser=33539)

> [Quoting mikhaildgreat](/thread/post/214102#post214102 "View Quoted Post")
> 
> Disliked
> 
> ****mwilkinw******,****ilanr** thank you thank you thank you GREAT GREAT GREAT Stuff! Now this could be applied to all the programs I am doing and using! the EA must be able to collect all the statistical data during forward testing, It must save it in the CSV file then use that to compute the optimal Lot size per trade. WOW! this is like the best money management system i ever came across! The more trades the EA makes the better it will be able to assign the optimal position size!  
>    
>  Thank you to both of you I will start working on this immediately!  
>    
>  Thank you once again,  
>  Mikhail
> 
> Ignored

  
Hey, No Problem, Your Welcome! THANK YOU for your EA's you're the man! Like you I usually do all of my backtesting manually.. there are always trades that your eye would take that the automatic back test misses.  
  
I calcualte my percentages manually and then implement them in "half kelly".  
  
If you really give it some study, you'll see that if your profit% is 20-25% you'll still be very profitible, if you keep your betting size at your kelly% and add to your positions based on your increased equity using the kelly formula. That's how gamblers win.. because their win percentage is around 5%.. with a good trading strategy you can desecrate those numbers!  
  
Steven A. Cohen from SAC Capital Partners uses the half-kelly and he's at 25 profit%. Needless to say he's aggressive and very strict with his system!  
  
Happy Trading! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#98](/thread/post/214311#post214311 "Post Permalink")

  * Feb 12, 2007 5:17am  Feb 12, 2007 5:17am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar33539_4.gif) mwilkinw](mwilkinw)

  * | Joined Feb 2007  | Status: Trader | [27 Posts](/search?do=process&provider=Member&searchuser=33539)

> [Quoting smjones](/thread/post/214280#post214280 "View Quoted Post")
> 
> Disliked
> 
> Hi, after reading Fortunes Formula and Ed Thorp's mathematics of gambling, this is how I have interpreted Kelly Criteria. I put it in a small spread sheet.  
>    
>  Don't know if it will help you with this, but I think you can see what the formula is getting at...  
>  The problem is that this style of MM is as aggressive as is possible, so there is a lot of risk of loss. Just not a great risk of ruin, because you can always get closer to zero. Mathematically it is true, but when your account is $10 the point is esoteric at best.  
>    
>  Here is a thread that talks about it at length and this post in particular   
>  [http://www.forexfactory.com/showpost...2&postcount=16](http://www.forexfactory.com/showpost.php?p=172192&postcount=16)
> 
> Ignored

  
smjones! I like the spreadsheet... an easy way to calculate. Although this is the normal kelly percentage... you can change your leverage to receive a half-kelly result!  
  
I use 80%-Kelly Value... can that be input into excel?  
  
Thanks for the tool!  
  
Happy Trading! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#99](/thread/post/214358#post214358 "Post Permalink")

  * Feb 12, 2007 6:27am  Feb 12, 2007 6:27am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar25698_4.gif) mikhaildgreat](mikhaildgreat)

  * | Joined Nov 2006  | Status: EA Programmer | [298 Posts](/search?do=process&provider=Member&searchuser=25698)

> [Quoting mwilkinw](/thread/post/214311#post214311 "View Quoted Post")
> 
> Disliked
> 
> smjones! I like the spreadsheet... an easy way to calculate. Although this is the normal kelly percentage... you can change your leverage to receive a half-kelly result!  
>    
>  I use 80%-Kelly Value... can that be input into excel?  
>    
>  Thanks for the tool!  
>    
>  Happy Trading!
> 
> Ignored

Hello mwilkinw,  
  
I'm trying to integrate kelly in the code of one of my programs but I have a cercern though. when you compute the kelly% and you plug in the values for the (win / loss) do you plug in the values for the trade you are about to make? TP and SL? or does the Win / loss in computing kelly% refer to the average win and loss per trade produced by your system during previous trades? I ask because most of the systems don't have fixed TP and SL value.  
  
Thanks Again,  
Mikhail  
  
PS. Sorry if my question is really noobish I'm still trying to absorb the concept, thanks for your patience. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#100](/thread/post/214362#post214362 "Post Permalink")

  * Feb 12, 2007 6:40am  Feb 12, 2007 6:40am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar7129_7.gif) smjones](smjones)

  * Joined Mar 2006 | Status: THANK YOU MERLIN,TWEE and FF Team | [4,603 Posts](/search?do=process&provider=Member&searchuser=7129)

> [Quoting mikhaildgreat](/thread/post/214358#post214358 "View Quoted Post")
> 
> Disliked
> 
> Hello mwilkinw,  
>    
>  I'm trying to integrate kelly in the code of one of my programs but I have a cercern though. when you compute the kelly% and you plug in the values for the (win / loss) do you plug in the values for the trade you are about to make? TP and SL? or does the Win / loss in computing kelly% refer to the average win and loss per trade produced by your system during previous trades? I ask because most of the systems don't have fixed TP and SL value.  
>    
>  Thanks Again,  
>  Mikhail  
>    
>  PS. Sorry if my question is really noobish I'm still trying to absorb the concept, thanks for your patience.
> 
> Ignored

That is actually and interesting question. For myself, I interpret it to mean the average win ratio the average pip win and the average pip loss, but when the formula was conceived, it was originally used to get the maximum bet for inside information about horse races. So, in it's original form it was applied to a specific horse race and a specific bet..   
  
The reason I chose to apply it to an average, is because there are so many trades in FOREX and the idea is to get an average win ratio and average wins and losses. Thereby no individual trade have a devastating effect on the account balance... Just a personal preferance. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * The Pouria EA Development Thread
  *   * [ **Reply to Thread** ](/thread/17242-the-pouria-ea-development-thread/reply#reply)

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

[The Pouria Method](/thread/17011-the-pouria-method "OKay here is one of the 4 best systems that I've made and used, with this system I pickup atleast 50 pips a day, I'm sharing this because...") 562 replies

[Lessons Learned during System Development](/thread/2986-lessons-learned-during-system-development "Hi, 
  
I've been reading through the forum and somehow I'm in the process of developing my own system.. But not really doing actual...") 29 replies

[(pouria method II on the test)](/thread/23104-pouria-method-ii-on-the-test "Hello  
pouria method II is now DONE thanks to the group of experts and mathematicians that helped and made this method. 
now we are...") 218 replies

[System Development Secrets](/thread/7342-system-development-secrets "&lt;meta http-equiv=&quot;CONTENT-TYPE&quot; content=&quot;text/html; charset=utf-8&quot;&gt;&lt;title&gt;&lt;/title&gt;&lt;meta name=&quot;GENERATOR&quot; content=&quot;OpenOffice.org 2.0 ...") 5 replies

[Metatrader 4 Development Course](/thread/5906-metatrader-4-development-course "Here is the Mql_4_Metatrader_4_Development_Course in pdf \(link fixed\) : 
 
http://www.freefilehosting.org/pupload/view/8711") 3 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/17242-the-pouria-ea-development-thread/reply#reply)
  * Subscribe
  * [45](javascript:void\(0\);)

Attachments: The Pouria EA Development Thread

Tags: The Pouria EA Development Thread

#  [](/thread/17242-the-pouria-ea-development-thread)The Pouria EA Development Thread 

  * 

  * [#101](/thread/post/214374#post214374 "Post Permalink")

  * Feb 12, 2007 7:04am  Feb 12, 2007 7:04am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar22836_4.gif) ilanr](ilanr)

  * | Joined Oct 2006  | Status: Trader | [260 Posts](/search?do=process&provider=Member&searchuser=22836)

Somehow, this thread now seems to be the main outlet for the Pouria method, so I post here...  
  
I've spent the day manually backtesting the data for GBPUSD and then optimizing SLs and TPs usin a computer program. I tested Jan through Oct 2006. Initially intended to go further, but the results were pretty stable, so I stopped after 10 months.   
  
I've used signals provided by Lux' indicator. Somehow, it missed a few good trades (don't know, why), but I sticked to it for the sick of objectivity. Nevertheless, the backtesting that served as input to the optimization program has a subjective element in it (I don't know, how the price behaved in real time), so take the results with MUCH caution.  
  
Anyway, these are the results. As it frequently happens with GBPUSD (anyone knows, why?), most trades on Tuesdays were losers. So I just eliminated all Tuesday trades. There are some Asian hours that seem to be not profitable (like midnight to 0200 GMT), but there is not enough data to decide, so I left them in.   
  
The system produced 136 trades in 10 months. I found that the optimal SL would be 32 p., and TP - 56 p. (not accounting for spread). Assuming a 4 p. spread, 58% of trades would be winners, and 42% losers. Altogether, 2000 pips would be earned net during these months. I think, it's quite fair. More pips can be made using a 46 p. SL, however, this would not be optimal in terms of MM (see the Kelly discussion earlier in this thread).  
  
Clearly, used with fixed SL and TP, the method doesn't allow for making the most from long trends. There were about 20 nice 200 p.+ trends that were not "taken care of" by the method. I'm not sure it must take care of everything... Personally, I got in love with SHI channels used in Perky's fxovereasy method (it may be known to some people here as Barishpolets channels), so I'll try in future to combine them. But this would be another method - and we still know too little about Pouria in its pure form... 

sans peur et sans reproche

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#102](/thread/post/214446#post214446 "Post Permalink")

  * Feb 12, 2007 8:35am  Feb 12, 2007 8:35am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar33539_4.gif) mwilkinw](mwilkinw)

  * | Joined Feb 2007  | Status: Trader | [27 Posts](/search?do=process&provider=Member&searchuser=33539)

> [Quoting mikhaildgreat](/thread/post/214358#post214358 "View Quoted Post")
> 
> Disliked
> 
> Hello mwilkinw,  
>    
>  I'm trying to integrate kelly in the code of one of my programs but I have a cercern though. when you compute the kelly% and you plug in the values for the (win / loss) do you plug in the values for the trade you are about to make? TP and SL? or does the Win / loss in computing kelly% refer to the average win and loss per trade produced by your system during previous trades? I ask because most of the systems don't have fixed TP and SL value.  
>    
>  Thanks Again,  
>  Mikhail  
>    
>  PS. Sorry if my question is really noobish I'm still trying to absorb the concept, thanks for your patience.
> 
> Ignored

  
Hey Mikhail! No problem I love that fact that you're in development of implementing the kelly... I can't wait to see the results.  
  
W/L refers to previous trades... the only time the kelly is computed with current equity during trading is when you are preparing to get into another trade or adding to an existing trade, based on the increase of your equity from that profitable trade.  
  
Happy Trading! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#103](/thread/post/214449#post214449 "Post Permalink")

  * Feb 12, 2007 8:45am  Feb 12, 2007 8:45am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar33539_4.gif) mwilkinw](mwilkinw)

  * | Joined Feb 2007  | Status: Trader | [27 Posts](/search?do=process&provider=Member&searchuser=33539)

> [Quoting ilanr](/thread/post/214374#post214374 "View Quoted Post")
> 
> Disliked
> 
> Somehow, this thread now seems to be the main outlet for the Pouria method, so I post here...  
>    
>  I've spent the day manually backtesting the data for GBPUSD and then optimizing SLs and TPs usin a computer program. I tested Jan through Oct 2006. Initially intended to go further, but the results were pretty stable, so I stopped after 10 months.   
>    
>  I've used signals provided by Lux' indicator. Somehow, it missed a few good trades (don't know, why), but I sticked to it for the sick of objectivity. Nevertheless, the backtesting that served as input to the optimization program has a subjective element in it (I don't know, how the price behaved in real time), so take the results with MUCH caution.  
>    
>  Anyway, these are the results. As it frequently happens with GBPUSD (anyone knows, why?), most trades on Tuesdays were losers. So I just eliminated all Tuesday trades. There are some Asian hours that seem to be not profitable (like midnight to 0200 GMT), but there is not enough data to decide, so I left them in.   
>    
>  The system produced 136 trades in 10 months. I found that the optimal SL would be 32 p., and TP - 56 p. (not accounting for spread). Assuming a 4 p. spread, 58% of trades would be winners, and 42% losers. Altogether, 2000 pips would be earned net during these months. I think, it's quite fair. More pips can be made using a 46 p. SL, however, this would not be optimal in terms of MM (see the Kelly discussion earlier in this thread).  
>    
>  Clearly, used with fixed SL and TP, the method doesn't allow for making the most from long trends. There were about 20 nice 200 p.+ trends that were not "taken care of" by the method. I'm not sure it must take care of everything... Personally, I got in love with SHI channels used in Perky's fxovereasy method (it may be known to some people here as Barishpolets channels), so I'll try in future to combine them. But this would be another method - and we still know too little about Pouria in its pure form...
> 
> Ignored

  
Hey Ilanr! It does seem to miss trades with those parameters... I manually backtest and trade live with the following parameters... give it a look.  
  
  
SL50 TP 100... However... when I enter a trade, I either get out by my TP getting hit or when the 5EMA crosses the MA's. When the 5 EMA crosses the MA's... that triggers another trade in the opposite direction... then I take that trade accordingly.  
  
There is more to my trading this system than that.. but first manually backtest it. You'll see you're losses are substantially smaller and you don't leave anything on the table.. so to speak... as the %'s compound I'm sure you'll appreciate it.   
  
Happy Trading!  
  
(SL is just as a precaution.. it rarely gets hit because by that time, i'm out of the losing trade and in the new trade.. based on the MA cross... you'll see the MACD coincides with this... although I use the FX Sniper Ergodic CCI.) 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#104](/thread/post/214489#post214489 "Post Permalink")

  * Feb 12, 2007 9:40am  Feb 12, 2007 9:40am 

  * [ BearPaw](bearpaw)

  * | Joined Jul 2006  | Status: A Trader for Life | [218 Posts](/search?do=process&provider=Member&searchuser=13999)

Ok...so this evening...it closed out the short audjpy from Friday for a loss. -20  
  
Opened a buy audjpy...it then hit its sl for -20.  
  
Right now have 3 trades open...usdchf, gbpusd, eurousd.  
  
Thanks guys,  
  
BP 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#105](/thread/post/214503#post214503 "Post Permalink")

  * Feb 12, 2007 9:51am  Feb 12, 2007 9:51am 

  * [ traderjane](traderjane)

  * | Joined May 2006  | Status: Trader | [35 Posts](/search?do=process&provider=Member&searchuser=9265)

> [Quoting mikhaildgreat](/thread/post/214160#post214160 "View Quoted Post")
> 
> Disliked
> 
> Hello Attached is the new version of the EA with a few minor but important bug fix. **If you are forward testing the original version pls stop using the older version and use this instead.**  
>    
>  Thanks,  
>  -Mikhail
> 
> Ignored

Hi Mikhail,  
Can you make indicators with buy and sell signals to place on the charts? thanks for your great inputs on this system 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#106](/thread/post/214599#post214599 "Post Permalink")

  * Feb 12, 2007 11:39am  Feb 12, 2007 11:39am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar25698_4.gif) mikhaildgreat](mikhaildgreat)

  * | Joined Nov 2006  | Status: EA Programmer | [298 Posts](/search?do=process&provider=Member&searchuser=25698)

> [Quoting BearPaw](/thread/post/214489#post214489 "View Quoted Post")
> 
> Disliked
> 
> Ok...so this evening...it closed out the short audjpy from Friday for a loss. -20  
>    
>  Opened a buy audjpy...it then hit its sl for -20.  
>    
>  Right now have 3 trades open...usdchf, gbpusd, eurousd.  
>    
>  Thanks guys,  
>    
>  BP
> 
> Ignored

Thanks for the update, I myself am having technical difficulty with my tester PC... So no trades on my end. hope I get it fixed by tomorrow... Pls keep us updated on the progress thanks!  
  

> [Quoting mwilkinw](/thread/post/214489#post214489 "View Quoted Post")
> 
> Disliked
> 
> W/L refers to previous trades... the only time the kelly is computed with current equity during trading is when you are preparing to get into another trade or adding to an existing trade, based on the increase of your equity from that profitable trade.
> 
> Ignored

Thank you for your quick reply, I will post later a pouria EA with a Kelly based MM option, I think pouria having fixed stops would make it easier to implement kelly MM.  
  

> [Quoting traderjane](/thread/post/214489#post214489 "View Quoted Post")
> 
> Disliked
> 
> Hi Mikhail,  
>  Can you make indicators with buy and sell signals to place on the charts? thanks for your great inputs on this system
> 
> Ignored

traderjane I'm sorry I cant help you there. I specialize mostly in making EAs not indicators, but I believe you can find many custom pouria indicators in pouria methods the main thread  
  
-Mikhail 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#107](/thread/post/214611#post214611 "Post Permalink")

  * Feb 12, 2007 11:56am  Feb 12, 2007 11:56am 

  * [ BearPaw](bearpaw)

  * | Joined Jul 2006  | Status: A Trader for Life | [218 Posts](/search?do=process&provider=Member&searchuser=13999)

> [Quoting BearPaw](/thread/post/214489#post214489 "View Quoted Post")
> 
> Disliked
> 
> Ok...so this evening...it closed out the short audjpy from Friday for a loss. -20  
>    
>  Opened a buy audjpy...it then hit its sl for -20.  
>    
>  Right now have 3 trades open...usdchf, gbpusd, eurousd.  
>    
>  Thanks guys,  
>    
>  BP
> 
> Ignored

Rehashing the night thus far.....  
  
audjpy Short (from friday) Stopped out -20  
audjpy Buy Stopped out -20  
usdchf Sell Stopped out -20  
  
Open right now  
  
gbpusd Buy still open  
eurusd Buy still open  
audjpy Sell still open  
  
  
Its amazing that audjpy is getting so much action....  
  
Anyway thats the story as of right now...gbp and aud are close to SL but we shall see....  
  
BP 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#108](/thread/post/214741#post214741 "Post Permalink")

  * Feb 12, 2007 3:05pm  Feb 12, 2007 3:05pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar22836_4.gif) ilanr](ilanr)

  * | Joined Oct 2006  | Status: Trader | [260 Posts](/search?do=process&provider=Member&searchuser=22836)

> [Quoting mwilkinw](/thread/post/214449#post214449 "View Quoted Post")
> 
> Disliked
> 
> Hey Ilanr! It does seem to miss trades with those parameters... I manually backtest and trade live with the following parameters... give it a look.  
>    
>    
>  SL50 TP 100... However... when I enter a trade, I either get out by my TP getting hit or when the 5EMA crosses the MA's. When the 5 EMA crosses the MA's... that triggers another trade in the opposite direction... then I take that trade accordingly.  
>    
>  There is more to my trading this system than that.. but first manually backtest it. You'll see you're losses are substantially smaller and you don't leave anything on the table.. so to speak... as the %'s compound I'm sure you'll appreciate it.   
>    
>  Happy Trading!  
>    
>  (SL is just as a precaution.. it rarely gets hit because by that time, i'm out of the losing trade and in the new trade.. based on the MA cross... you'll see the MACD coincides with this... although I use the FX Sniper Ergodic CCI.)
> 
> Ignored

mwilkinw, do you still find that 50 and 55 MA's work better? 

sans peur et sans reproche

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#109](/thread/post/214865#post214865 "Post Permalink")

  * Feb 12, 2007 6:21pm  Feb 12, 2007 6:21pm 

  * [ BearPaw](bearpaw)

  * | Joined Jul 2006  | Status: A Trader for Life | [218 Posts](/search?do=process&provider=Member&searchuser=13999)

> [Quoting mikhaildgreat](/thread/post/214599#post214599 "View Quoted Post")
> 
> Disliked
> 
> Thanks for the update, I myself am having technical difficulty with my tester PC... So no trades on my end. hope I get it fixed by tomorrow... Pls keep us updated on the progress thanks!  
>    
>  -Mikhail
> 
> Ignored

Mikhail,  
  
This is interesting. The ea entered a NZDUSD trade. But it seemed to enter it really late. Attached is a picture of that.   
  
Please let me know why or what you think happened.  
  
BP 

Attached Image

![](/attachment/image/22167?d=1171272050)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#110](/thread/post/214896#post214896 "Post Permalink")

  * Feb 12, 2007 6:48pm  Feb 12, 2007 6:48pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar29751_4.gif) lexazver](lexazver)

  * | Joined Dec 2006  | Status: o_O | [1,511 Posts](/search?do=process&provider=Member&searchuser=29751)

THe EA just bought EURUSDa nd it ment to sell it, but i did sell it on live aacount at 94, stop at 10 target 76-79 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#111](/thread/post/214899#post214899 "Post Permalink")

  * Feb 12, 2007 6:51pm  Feb 12, 2007 6:51pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar29751_4.gif) lexazver](lexazver)

  * | Joined Dec 2006  | Status: o_O | [1,511 Posts](/search?do=process&provider=Member&searchuser=29751)

haha that was quick and painless profit though io closed at +14, anyways thats 3 trades on live account that turned out to be profitable in the row. EURUSD only./ 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#112](/thread/post/214977#post214977 "Post Permalink")

  * Feb 12, 2007 8:05pm  Feb 12, 2007 8:05pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar22836_4.gif) ilanr](ilanr)

  * | Joined Oct 2006  | Status: Trader | [260 Posts](/search?do=process&provider=Member&searchuser=22836)

> [Quoting ilanr](/thread/post/214741#post214741 "View Quoted Post")
> 
> Disliked
> 
> mwilkinw, do you still find that 50 and 55 MA's work better?
> 
> Ignored

mwilkinw, sorry to have bothered. tested my self and saw the answer myself (positive). enjoy your trades. 

sans peur et sans reproche

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#113](/thread/post/214988#post214988 "Post Permalink")

  * Feb 12, 2007 8:25pm  Feb 12, 2007 8:25pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar23218_2.gif) Jagg](jagg)

  * Joined Oct 2006 | Status: Trader | [533 Posts](/search?do=process&provider=Member&searchuser=23218)

> [Quoting lexazver](/thread/post/214896#post214896 "View Quoted Post")
> 
> Disliked
> 
> THe EA just bought EURUSDa nd it ment to sell it, but i did sell it on live aacount at 94, stop at 10 target 76-79
> 
> Ignored

Yes, had the same... EA would like to buy instead of sell eur/usd (but was first beta, will test the beta2 if this happens again) 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#114](/thread/post/215058#post215058 "Post Permalink")

  * Feb 12, 2007 10:08pm  Feb 12, 2007 10:08pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30695_4.gif) toti1972](toti1972)

  * | Joined Jan 2007  | Status: Trader | [107 Posts](/search?do=process&provider=Member&searchuser=30695)

here my results on Pouria Beta 2 last night (EUR/USD, USD/CHF):  
  
EUR/USD: buy 1.3019 sl: 1.2989: -30  
USD/CHF: sell 1.2474 sl: 1.2494: -20  
USD/CHF: buy 1.2492 TP: 1.2522: +30 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#115](/thread/post/215083#post215083 "Post Permalink")

  * Edited 11:57pm  Feb 12, 2007 10:37pm | Edited 11:57pm 

  * [ JamDown](jamdown)

  * | Joined Dec 2006  | Status: Trader | [39 Posts](/search?do=process&provider=Member&searchuser=27324)

> [Quoting BearPaw](/thread/post/214611#post214611 "View Quoted Post")
> 
> Disliked
> 
> Rehashing the night thus far.....  
>    
>  audjpy Short (from friday) Stopped out -20  
>  audjpy Buy Stopped out -20  
>  usdchf Sell Stopped out -20  
>    
>  Open right now  
>    
>  gbpusd Buy still open  
>  eurusd Buy still open  
>  audjpy Sell still open  
>    
>    
>  Its amazing that audjpy is getting so much action....  
>    
>  Anyway thats the story as of right now...gbp and aud are close to SL but we shall see....  
>    
>  BP
> 
> Ignored

As far as I can see...doing the reverse is the thing to do if you are gunning for 15-20 pips. In almost every case where there was no major news release the pair retraced at the break and then continued on to major moves after the minor retracement. If you are going to be profitable you have to use a wide stoploss or loose it all together.  
my2Cents 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#116](/thread/post/215097#post215097 "Post Permalink")

  * Feb 12, 2007 10:51pm  Feb 12, 2007 10:51pm 

  * [ BearPaw](bearpaw)

  * | Joined Jul 2006  | Status: A Trader for Life | [218 Posts](/search?do=process&provider=Member&searchuser=13999)

> [Quoting toti1972](/thread/post/215058#post215058 "View Quoted Post")
> 
> Disliked
> 
> here my results on Pouria Beta 2 last night (EUR/USD, USD/CHF):  
>    
>  EUR/USD: buy 1.3019 sl: 1.2989: -30  
>  USD/CHF: sell 1.2474 sl: 1.2494: -20  
>  USD/CHF: buy 1.2492 TP: 1.2522: +30
> 
> Ignored

Toti...don't know if my results are different than yours. But here they are. These are since 6pmEST sunday night, till 8amEST Monday morning. The first trade was opened on friday...then closed for a profit on sunday. Interesting to note that the first two of yours are losses...but for me they were wins. My stop losses are 20 pips.  
  
aud/jpy-----sell-----94.38-----profitable----- +15  
aud/jpy-----sell-----94.42-----Loss---------- -20  
aud/jpy-----buy-----94.89-----Loss---------- -20  
usd/chf-----sell-----1.2464----Loss---------- -20  
gbp/usd-----buy----1.9530----profitable------ +20  
aud/jpy-----sell-----94.36-----loss----------- -20   
usd/chf-----sell-----1.2473----profitable------ +10  
eur/usd-----buy-----1.3020---profitable------- +15  
gbp/usd-----sell-----1.9495---profitable------- +20  
usd/chf-----buy-----1.2496----profitable------ +10  
eur/usd-----sell-----1.2993----profitable------ +15  
eur/jpy-----sell------157.99----profitable------ +15  
  
Net Pip total for 14 hours = 40 pips  
  
Currently open...nzdusd trade which is close to BE.  
  
Thanks BP. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#117](/thread/post/215276#post215276 "Post Permalink")

  * Feb 13, 2007 1:52am  Feb 13, 2007 1:52am 

  * [ neshat](neshat)

  * | Joined Sep 2006  | Status: Trader | [70 Posts](/search?do=process&provider=Member&searchuser=20436)

I found a problem in Beta 2 version . As you see in bellow It opend a false BUY position in USD/CAD : 

Attached Image

![](/attachment/image/22205?d=1171299063)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#118](/thread/post/215278#post215278 "Post Permalink")

  * Feb 13, 2007 1:55am  Feb 13, 2007 1:55am 

  * [ BearPaw](bearpaw)

  * | Joined Jul 2006  | Status: A Trader for Life | [218 Posts](/search?do=process&provider=Member&searchuser=13999)

Neshat,  
  
I have not experienced a false buy in the usdcad at all since friday evening EST. Can you elaborate?  
  
BP 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#119](/thread/post/215295#post215295 "Post Permalink")

  * Feb 13, 2007 2:17am  Feb 13, 2007 2:17am 

  * [ neshat](neshat)

  * | Joined Sep 2006  | Status: Trader | [70 Posts](/search?do=process&provider=Member&searchuser=20436)

> [Quoting BearPaw](/thread/post/215278#post215278 "View Quoted Post")
> 
> Disliked
> 
> Neshat,  
>    
>  I have not experienced a false buy in the usdcad at all since friday evening EST. Can you elaborate?  
>    
>  BP
> 
> Ignored

I think it is clear in picture . 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#120](/thread/post/215470#post215470 "Post Permalink")

  * Feb 13, 2007 5:27am  Feb 13, 2007 5:27am 

  * [ cncsm](cncsm)

  * | Joined Feb 2007  | Status: Trader | [7 Posts](/search?do=process&provider=Member&searchuser=33691)

I just joined ff yesterday and really can't say enough about all the good info and sharing that is going on here. It is great. Thank you to those who share their system, and those who program ea's. My pouria 2 just bought eurchf and there was no crossover of the ma's. Did anyone else have this happen? Also if someone will tell me how I will post the screen. I will be glad to do so. I only need to ask once.![](https://resources.faireconomy.media/images/emojis/64/1f61e.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * The Pouria EA Development Thread
  *   * [ **Reply to Thread** ](/thread/17242-the-pouria-ea-development-thread/reply#reply)

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

[The Pouria Method](/thread/17011-the-pouria-method "OKay here is one of the 4 best systems that I've made and used, with this system I pickup atleast 50 pips a day, I'm sharing this because...") 562 replies

[Lessons Learned during System Development](/thread/2986-lessons-learned-during-system-development "Hi, 
  
I've been reading through the forum and somehow I'm in the process of developing my own system.. But not really doing actual...") 29 replies

[(pouria method II on the test)](/thread/23104-pouria-method-ii-on-the-test "Hello  
pouria method II is now DONE thanks to the group of experts and mathematicians that helped and made this method. 
now we are...") 218 replies

[System Development Secrets](/thread/7342-system-development-secrets "&lt;meta http-equiv=&quot;CONTENT-TYPE&quot; content=&quot;text/html; charset=utf-8&quot;&gt;&lt;title&gt;&lt;/title&gt;&lt;meta name=&quot;GENERATOR&quot; content=&quot;OpenOffice.org 2.0 ...") 5 replies

[Metatrader 4 Development Course](/thread/5906-metatrader-4-development-course "Here is the Mql_4_Metatrader_4_Development_Course in pdf \(link fixed\) : 
 
http://www.freefilehosting.org/pupload/view/8711") 3 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/17242-the-pouria-ea-development-thread/reply#reply)
  * Subscribe
  * [45](javascript:void\(0\);)

Attachments: The Pouria EA Development Thread

Tags: The Pouria EA Development Thread

#  [](/thread/17242-the-pouria-ea-development-thread)The Pouria EA Development Thread 

  * 

  * [#121](/thread/post/215515#post215515 "Post Permalink")

  * Feb 13, 2007 6:59am  Feb 13, 2007 6:59am 

  * [ BearPaw](bearpaw)

  * | Joined Jul 2006  | Status: A Trader for Life | [218 Posts](/search?do=process&provider=Member&searchuser=13999)

> [Quoting cncsm](/thread/post/215470#post215470 "View Quoted Post")
> 
> Disliked
> 
> I just joined ff yesterday and really can't say enough about all the good info and sharing that is going on here. It is great. Thank you to those who share their system, and those who program ea's. My pouria 2 just bought eurchf and there was no crossover of the ma's. Did anyone else have this happen? Also if someone will tell me how I will post the screen. I will be glad to do so. I only need to ask once.![](https://resources.faireconomy.media/images/emojis/64/1f61e.png?v=15.1)
> 
> Ignored

cncsm,  
  
The same happened to me. MikhaildGreat will need to tell us if something is up with the EA or if we just aren't seeing something.  
  
To attach a pic of your screen, just hit print screen, go to your paint program, do Control V (for paste) then save that as a jpeg...when You are typing here, just click the paperclip above, and then you can post your pic.  
  
Hopefully that answers your question. Hopefully MikhaildGreat is still around!!   
![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
  
cya,  
  
BP 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#122](/thread/post/215517#post215517 "Post Permalink")

  * Feb 13, 2007 7:03am  Feb 13, 2007 7:03am 

  * [ BearPaw](bearpaw)

  * | Joined Jul 2006  | Status: A Trader for Life | [218 Posts](/search?do=process&provider=Member&searchuser=13999)

Mikhaildgreat,  
  
USDJPY just opened up a buy, even though the 5ma did not cross with the 75/85....please let me know what you think is happening there.  
  
BP 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#123](/thread/post/215693#post215693 "Post Permalink")

  * Feb 13, 2007 11:46am  Feb 13, 2007 11:46am 

  * [ mickeymickey](mickeymickey)

  * | Joined Aug 2006  | Status: Trader | [80 Posts](/search?do=process&provider=Member&searchuser=16777)

I don't know if someone asked this but can you implement in the EA to take partial profits at one point and let the rest of the trade run? I think that is the most profitable way to trade this system. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#124](/thread/post/215715#post215715 "Post Permalink")

  * Feb 13, 2007 12:36pm  Feb 13, 2007 12:36pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30695_4.gif) toti1972](toti1972)

  * | Joined Jan 2007  | Status: Trader | [107 Posts](/search?do=process&provider=Member&searchuser=30695)

Pouria beta 2 triggered an order to buy on CAD/USD and never got a complete cross...the trade is about to be stopped out... I know others are experimenting this situation in other pairs...I think we need to check this issue.  
Thanks 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#125](/thread/post/215742#post215742 "Post Permalink")

  * Feb 13, 2007 1:14pm  Feb 13, 2007 1:14pm 

  * [ cncsm](cncsm)

  * | Joined Feb 2007  | Status: Trader | [7 Posts](/search?do=process&provider=Member&searchuser=33691)

I just got filled on the usdcad without a cross the EA is filling all kinds of orders and I have it set up according to Pouria specs for all the pairs mentioned. I would post the screen shot but when I attempt to paste into paint it tells me I don't have enough memory? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#126](/thread/post/215944#post215944 "Post Permalink")

  * Feb 13, 2007 5:28pm  Feb 13, 2007 5:28pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar25698_4.gif) mikhaildgreat](mikhaildgreat)

  * | Joined Nov 2006  | Status: EA Programmer | [298 Posts](/search?do=process&provider=Member&searchuser=25698)

Hello All,  
  
Sorry I had problems with my internet connection since yesterday but I am back now... Will read the replies and see what issues are brought by the EA.  
  
Regards,  
Mikhail 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#127](/thread/post/215949#post215949 "Post Permalink")

  * Feb 13, 2007 5:33pm  Feb 13, 2007 5:33pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar25698_4.gif) mikhaildgreat](mikhaildgreat)

  * | Joined Nov 2006  | Status: EA Programmer | [298 Posts](/search?do=process&provider=Member&searchuser=25698)

> [Quoting BearPaw](/thread/post/214865#post214865 "View Quoted Post")
> 
> Disliked
> 
> Mikhail,  
>    
>  This is interesting. The ea entered a NZDUSD trade. But it seemed to enter it really late. Attached is a picture of that.   
>    
>  Please let me know why or what you think happened.  
>    
>  BP
> 
> Ignored

EA waited for the MACD to be above zero before entering the trade. This is in line with the rules...  
  
Regards,  
Mikhail 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#128](/thread/post/215960#post215960 "Post Permalink")

  * Feb 13, 2007 5:42pm  Feb 13, 2007 5:42pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar25698_4.gif) mikhaildgreat](mikhaildgreat)

  * | Joined Nov 2006  | Status: EA Programmer | [298 Posts](/search?do=process&provider=Member&searchuser=25698)

I see EA fills orders that it is not supposed to, I was afraid this could happen because of my encoding which might generate these false signals... Anyways will post a fixed version later.  
  
But for everyone testing this EA pls refer to the first post to understand how EA really trades. EA will trade if 1) MA cross over and MACD is in the same direction _OR_ 2) MACD crosses zero line and MA points to the same direction.  
  
But the USDCAD was definitely a false trade, probably caused by how the variables are stored in the code... Anyways I will fix this.  
  
Thank you for testing and for your patience,  
Mikhail 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#129](/thread/post/215984#post215984 "Post Permalink")

  * Feb 13, 2007 6:13pm  Feb 13, 2007 6:13pm 

  * [ BearPaw](bearpaw)

  * | Joined Jul 2006  | Status: A Trader for Life | [218 Posts](/search?do=process&provider=Member&searchuser=13999)

> [Quoting mikhaildgreat](/thread/post/215960#post215960 "View Quoted Post")
> 
> Disliked
> 
> I see EA fills orders that it is not supposed to, I was afraid this could happen because of my encoding which might generate these false signals... Anyways will post a fixed version later.  
>    
>  But for everyone testing this EA pls refer to the first post to understand how EA really trades. EA will trade if 1) MA cross over and MACD is in the same direction _OR_ 2) MACD crosses zero line and MA points to the same direction.  
>    
>  But the USDCAD was definitely a false trade, probably caused by how the variables are stored in the code... Anyways I will fix this.  
>    
>  Thank you for testing and for your patience,  
>  Mikhail
> 
> Ignored

Thanks for your hard work Mikhail!!  
  
BP 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#130](/thread/post/216115#post216115 "Post Permalink")

  * Feb 13, 2007 8:34pm  Feb 13, 2007 8:34pm 

  * [ rogerha](rogerha)

  * | Joined Aug 2006  | Status: Trader | [273 Posts](/search?do=process&provider=Member&searchuser=15670)

Firstly, great work on this EA, I have been testing it now for a couple of days. I noticed one thing today however, maybe its a problem, maybe I have done something wrong.  
  
However since the EA trades the live cross of both the MA cross and the MACD cross, we had a valid entry today on the M30 GBPUSD at 10:30. Because of the settings I was trying (quite a tight SL of 15 pips), I was stopped out on the same bar.  
  
Suprisingly though the EA entered on the next bar also.  
  
So all I can conclude is that both the crosses took place on the 10:30 bar, but because the bar closed above the low of the bar, then one or two of the crosses didn't happen at bar close, and then a new cross happened on the next bar. (I hope that makes sense).  
  
The second trade was a success, but I wondered if we should judge entry conditions at bar close, otherwise this might happen quite regularly. We all know that as bars build the situation can change.  
  
Also, as a suggestion, has anybody looked at using the 75/85 LWMA as your stop loss ?   
  
Good work though !  

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#131](/thread/post/216128#post216128 "Post Permalink")

  * Feb 13, 2007 8:43pm  Feb 13, 2007 8:43pm 

  * [ Coder](coder)

  * | Joined May 2006  | Status: Think Fast, Live Free! | [119 Posts](/search?do=process&provider=Member&searchuser=9708)

Hello,  
  
You will find that the cross will make a crossover then uncross again on the same bar. The only way to detect if a crossover has occurred is to wait for the bar after the cross.   
The problem then is that the move is already over. Catch 22.   
In short, you can not reliably use MA crossovers with an EA for an entry position.  
  
Coder ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#132](/thread/post/216138#post216138 "Post Permalink")

  * Feb 13, 2007 8:53pm  Feb 13, 2007 8:53pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar25698_4.gif) mikhaildgreat](mikhaildgreat)

  * | Joined Nov 2006  | Status: EA Programmer | [298 Posts](/search?do=process&provider=Member&searchuser=25698)

> [Quoting rogerha](/thread/post/216115#post216115 "View Quoted Post")
> 
> Disliked
> 
> Firstly, great work on this EA, I have been testing it now for a couple of days. I noticed one thing today however, maybe its a problem, maybe I have done something wrong.  
>    
>  However since the EA trades the live cross of both the MA cross and the MACD cross, we had a valid entry today on the M30 GBPUSD at 10:30. Because of the settings I was trying (quite a tight SL of 15 pips), I was stopped out on the same bar.  
>    
>  Suprisingly though the EA entered on the next bar also.  
>    
>  So all I can conclude is that both the crosses took place on the 10:30 bar, but because the bar closed above the low of the bar, then one or two of the crosses didn't happen at bar close, and then a new cross happened on the next bar. (I hope that makes sense).  
>    
>  The second trade was a success, but I wondered if we should judge entry conditions at bar close, otherwise this might happen quite regularly. We all know that as bars build the situation can change.  
>    
>  Also, as a suggestion, has anybody looked at using the 75/85 LWMA as your stop loss ?   
>    
>  Good work though !  
> 
> 
> Ignored

If you want to wait for bar to close simply set **ConfirmedOnEntry** = true  
  
this could be found in the external variables  
  
-Mikhail 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#133](/thread/post/216168#post216168 "Post Permalink")

  * Feb 13, 2007 9:35pm  Feb 13, 2007 9:35pm 

  * [ rogerha](rogerha)

  * | Joined Aug 2006  | Status: Trader | [273 Posts](/search?do=process&provider=Member&searchuser=15670)

> [Quoting mikhaildgreat](/thread/post/216138#post216138 "View Quoted Post")
> 
> Disliked
> 
> If you want to wait for bar to close simply set **ConfirmedOnEntry** = true  
>    
>  this could be found in the external variables  
>    
>  -Mikhail
> 
> Ignored

Thanks Mikhail, I figured I was doing something wrong ! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#134](/thread/post/216199#post216199 "Post Permalink")

  * Feb 13, 2007 10:16pm  Feb 13, 2007 10:16pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar25698_4.gif) mikhaildgreat](mikhaildgreat)

  * | Joined Nov 2006  | Status: EA Programmer | [298 Posts](/search?do=process&provider=Member&searchuser=25698)

Hello Once Again!   
  
to All testers pls update the EA you are using. This version should eliminate false entry signals in the EA. When We have tested this version to be working without bugs we can add the improvements to the strategy such as MA based Stoploss and MA based Trailing Stop.  
  
Thank you again for testing,  
Mikhail 

Attached File(s)

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [Pouria EA Beta 3.mq4](/attachment/file/22274?d=1171372556) 12 KB | 642 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#135](/thread/post/216202#post216202 "Post Permalink")

  * Feb 13, 2007 10:18pm  Feb 13, 2007 10:18pm 

  * [ BearPaw](bearpaw)

  * | Joined Jul 2006  | Status: A Trader for Life | [218 Posts](/search?do=process&provider=Member&searchuser=13999)

Will do...thanks Mikhail!!  
  
BP 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#136](/thread/post/216206#post216206 "Post Permalink")

  * Feb 13, 2007 10:26pm  Feb 13, 2007 10:26pm 

  * [ bandito](bandito)

  * | Joined Jan 2007  | Status: Trader | [19 Posts](/search?do=process&provider=Member&searchuser=31069)

_Hai... sir... the great  
  
i have testing your EA Beta2 on NF [broker](http://www.forexfactory.com/brokers.php)... 12/2 - 13/2 (14:32GMT2)  
  
Just Profit 124.04..  
  
Great System  
  
TimeFrame15  
  
SL=20 TP=15_  
_PROFIT - GBPJPY,EURJPY,USDJPY,EURGBP,USDCHF,EURUSD..._  
_But now we have Beta3... i will try it  
  
GU = seem to be loss  
  
Thanks_

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#137](/thread/post/216261#post216261 "Post Permalink")

  * Feb 13, 2007 11:05pm  Feb 13, 2007 11:05pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar14103_16.gif) ut2DaMax](ut2damax)

  * | Joined Jul 2006  | Status: Trader | [592 Posts](/search?do=process&provider=Member&searchuser=14103)

> [Quoting mikhaildgreat](/thread/post/216199#post216199 "View Quoted Post")
> 
> Disliked
> 
> Hello Once Again!   
>    
>  to All testers pls update the EA you are using. This version should eliminate false entry signals in the EA. When We have tested this version to be working without bugs we can add the improvements to the strategy such as MA based Stoploss and MA based Trailing Stop.  
>    
>  Thank you again for testing,  
>  Mikhail
> 
> Ignored

Mikhail, thanks for the latest updated EA ... now we can test this one .... sure would be great if this now made this one correct in the transactions and also Profitable. I am eagerly watching all those that are testing these. This could end up being one of those EA's I can turn lose. Thanks all! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#138](/thread/post/216262#post216262 "Post Permalink")

  * Feb 13, 2007 11:05pm  Feb 13, 2007 11:05pm 

  * [ BearPaw](bearpaw)

  * | Joined Jul 2006  | Status: A Trader for Life | [218 Posts](/search?do=process&provider=Member&searchuser=13999)

Ok,  
  
So here are my results for today....or specifically from Monday 8am to Today 9am, EST. This was with Pouria Beta 2, so there might be a couple bad signals, but then again, I do not know if those were profitable or not...will look into that.  
  
17 entries and exits triggered.   
  
Unprofitable - 7 trades (sl is 20)  
Profitable - 10 trades (tp varies according to rules of Pouria)  
  
Net result is -7 pips.  
  
So, Day 1 = 40 pips profit.  
Day 2 = -7 pips profit.  
  
Still looking good!!  
  
Thanks,  
  
BP 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#139](/thread/post/216274#post216274 "Post Permalink")

  * Feb 13, 2007 11:17pm  Feb 13, 2007 11:17pm 

  * [ bandito](bandito)

  * | Joined Jan 2007  | Status: Trader | [19 Posts](/search?do=process&provider=Member&searchuser=31069)

Hehe...  
  
Demo account... Beta3... profit increse to 190.40  
  
Thanks... the great  
  
Can i using it to real account with US2000...???? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#140](/thread/post/216285#post216285 "Post Permalink")

  * Feb 13, 2007 11:25pm  Feb 13, 2007 11:25pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar18197_4.gif) OwenT](owent)

  * | Joined Sep 2006  | Status: Trader | [186 Posts](/search?do=process&provider=Member&searchuser=18197)

Bandito,  
are you using confirmonentry = false or true? Move to BE?...  
Did you backtested?   
I'm asking that because I'm trying now on GBP/JPY and I have only losses! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * The Pouria EA Development Thread
  *   * [ **Reply to Thread** ](/thread/17242-the-pouria-ea-development-thread/reply#reply)

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

[The Pouria Method](/thread/17011-the-pouria-method "OKay here is one of the 4 best systems that I've made and used, with this system I pickup atleast 50 pips a day, I'm sharing this because...") 562 replies

[Lessons Learned during System Development](/thread/2986-lessons-learned-during-system-development "Hi, 
  
I've been reading through the forum and somehow I'm in the process of developing my own system.. But not really doing actual...") 29 replies

[(pouria method II on the test)](/thread/23104-pouria-method-ii-on-the-test "Hello  
pouria method II is now DONE thanks to the group of experts and mathematicians that helped and made this method. 
now we are...") 218 replies

[System Development Secrets](/thread/7342-system-development-secrets "&lt;meta http-equiv=&quot;CONTENT-TYPE&quot; content=&quot;text/html; charset=utf-8&quot;&gt;&lt;title&gt;&lt;/title&gt;&lt;meta name=&quot;GENERATOR&quot; content=&quot;OpenOffice.org 2.0 ...") 5 replies

[Metatrader 4 Development Course](/thread/5906-metatrader-4-development-course "Here is the Mql_4_Metatrader_4_Development_Course in pdf \(link fixed\) : 
 
http://www.freefilehosting.org/pupload/view/8711") 3 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/17242-the-pouria-ea-development-thread/reply#reply)
  * Subscribe
  * [45](javascript:void\(0\);)

Attachments: The Pouria EA Development Thread

Tags: The Pouria EA Development Thread

#  [](/thread/17242-the-pouria-ea-development-thread)The Pouria EA Development Thread 

  * 

  * [#141](/thread/post/216290#post216290 "Post Permalink")

  * Feb 13, 2007 11:27pm  Feb 13, 2007 11:27pm 

  * [ bandito](bandito)

  * | Joined Jan 2007  | Status: Trader | [19 Posts](/search?do=process&provider=Member&searchuser=31069)

May be u don belived the result... i get  
  
here... the result... look 

Attached Image

![](/attachment/image/22282?d=1171376852)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#142](/thread/post/216291#post216291 "Post Permalink")

  * Feb 13, 2007 11:29pm  Feb 13, 2007 11:29pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar18197_4.gif) OwenT](owent)

  * | Joined Sep 2006  | Status: Trader | [186 Posts](/search?do=process&provider=Member&searchuser=18197)

Of course I believe you, I'm just asking how do you set the other parameters? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#143](/thread/post/216300#post216300 "Post Permalink")

  * Feb 13, 2007 11:35pm  Feb 13, 2007 11:35pm 

  * [ BearPaw](bearpaw)

  * | Joined Jul 2006  | Status: A Trader for Life | [218 Posts](/search?do=process&provider=Member&searchuser=13999)

lol...yeah...what do you have your confirmed signal at bandito...  
  
BP 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#144](/thread/post/216306#post216306 "Post Permalink")

  * Feb 13, 2007 11:36pm  Feb 13, 2007 11:36pm 

  * [ bandito](bandito)

  * | Joined Jan 2007  | Status: Trader | [19 Posts](/search?do=process&provider=Member&searchuser=31069)

OwetT  
  
Hi... i am not changing anything.... i just... turn the TP=15 and SL=20... with lot 0.1... Time Frame15 wint NF broker..  
  
Sorry 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#145](/thread/post/216313#post216313 "Post Permalink")

  * Feb 13, 2007 11:42pm  Feb 13, 2007 11:42pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar25698_4.gif) mikhaildgreat](mikhaildgreat)

  * | Joined Nov 2006  | Status: EA Programmer | [298 Posts](/search?do=process&provider=Member&searchuser=25698)

> [Quoting bandito](/thread/post/216306#post216306 "View Quoted Post")
> 
> Disliked
> 
> OwetT  
>    
>  Hi... i am not changing anything.... i just... turn the TP=15 and SL=20... with lot 0.1... Time Frame15 wint NF broker..  
>    
>  Sorry
> 
> Ignored

Great results bandito... your the only one testing this on M15 but marvelous results. Anyone willing to manually backtest this strategy on M15 timeframe?  
  
Bandito keep up the great work! ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)  
  
Regards,  
Mikhail 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#146](/thread/post/216320#post216320 "Post Permalink")

  * Feb 13, 2007 11:48pm  Feb 13, 2007 11:48pm 

  * [ JamDown](jamdown)

  * | Joined Dec 2006  | Status: Trader | [39 Posts](/search?do=process&provider=Member&searchuser=27324)

> [Quoting mikhaildgreat](/thread/post/216199#post216199 "View Quoted Post")
> 
> Disliked
> 
> Hello Once Again!   
>    
>  to All testers pls update the EA you are using. This version should eliminate false entry signals in the EA. When We have tested this version to be working without bugs we can add the improvements to the strategy such as MA based Stoploss and MA based Trailing Stop.  
>    
>  Thank you again for testing,  
>  Mikhail
> 
> Ignored

My eyes must be deceiving me so someone else should see this.  
No SL  
4 lots  
GBPUSD  
60 TP 

Attached File(s)

![File Type: doc](https://assets.faireconomy.media/images/attach/doc.gif) [Beta3 test.doc](/attachment/file/22285?d=1171378066) 8 KB | 516 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#147](/thread/post/216324#post216324 "Post Permalink")

  * Feb 13, 2007 11:50pm  Feb 13, 2007 11:50pm 

  * [ BearPaw](bearpaw)

  * | Joined Jul 2006  | Status: A Trader for Life | [218 Posts](/search?do=process&provider=Member&searchuser=13999)

nice....if you look at the CHF JPY....it looks so close...and the highs and lows cross the 75/85 but the 5ma does not cross it, and it reversed. The ea did not call that trade...  
  
I think I am impressed. ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
  
BP 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#148](/thread/post/216333#post216333 "Post Permalink")

  * Feb 13, 2007 11:54pm  Feb 13, 2007 11:54pm 

  * [ BearPaw](bearpaw)

  * | Joined Jul 2006  | Status: A Trader for Life | [218 Posts](/search?do=process&provider=Member&searchuser=13999)

> [Quoting JamDown](/thread/post/216320#post216320 "View Quoted Post")
> 
> Disliked
> 
> My eyes must be deceiving me so someone else should see this.  
>  No SL  
>  4 lots  
>  GBPUSD  
>  60 TP
> 
> Ignored

That looks awesome Jamdown, but I do not believe that you never go into a negative balance....that the drawdown is zero seems really unattainable. I have instant drawdown with the current positions the way they are structured.  
  
So, to me, before I even consider looking at something with no stop loss, I would want to know what the maximum drawdown has been.  
  
Others want to say that I am an idiot or confirm what I am saying?  
  
Thanks,  
  
BP 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#149](/thread/post/216341#post216341 "Post Permalink")

  * Feb 13, 2007 11:58pm  Feb 13, 2007 11:58pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar25698_4.gif) mikhaildgreat](mikhaildgreat)

  * | Joined Nov 2006  | Status: EA Programmer | [298 Posts](/search?do=process&provider=Member&searchuser=25698)

Strategy Tester only shows drawdown of the balance, and since he didn't put SL there was no drawdown. Startegy tester doesn't show drawdowns on equity. This is very dangerous basically your using margin call as your SL.  
  
Jamdown how about trying to put high SL like 200 or something just to see if it will be hit or not.  
  
-Mikhail  

> [Quoting BearPaw](/thread/post/216333#post216333 "View Quoted Post")
> 
> Disliked
> 
> That looks awesome Jamdown, but I do not believe that you never go into a negative balance....that the drawdown is zero seems really unattainable. I have instant drawdown with the current positions the way they are structured.  
>    
>  So, to me, before I even consider looking at something with no stop loss, I would want to know what the maximum drawdown has been.  
>    
>  Others want to say that I am an idiot or confirm what I am saying?  
>    
>  Thanks,  
>    
>  BP
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#150](/thread/post/216345#post216345 "Post Permalink")

  * Feb 14, 2007 12:02am  Feb 14, 2007 12:02am 

  * [ BearPaw](bearpaw)

  * | Joined Jul 2006  | Status: A Trader for Life | [218 Posts](/search?do=process&provider=Member&searchuser=13999)

makes sense...thanks for explaining that to me Mikhail.  
  
BP 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#151](/thread/post/216368#post216368 "Post Permalink")

  * Feb 14, 2007 12:23am  Feb 14, 2007 12:23am 

  * [ bandito](bandito)

  * | Joined Jan 2007  | Status: Trader | [19 Posts](/search?do=process&provider=Member&searchuser=31069)

The Great...  
  
I want to know... how to change the setting. so it not open trade with 0.2lot.. i just want to trade with 0.1lot only... because i using US2000.. i will try this... on real account....  
  
Thanks for this system...  
  
Bandito 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#152](/thread/post/216376#post216376 "Post Permalink")

  * Feb 14, 2007 12:29am  Feb 14, 2007 12:29am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar25698_4.gif) mikhaildgreat](mikhaildgreat)

  * | Joined Nov 2006  | Status: EA Programmer | [298 Posts](/search?do=process&provider=Member&searchuser=25698)

> [Quoting bandito](/thread/post/216368#post216368 "View Quoted Post")
> 
> Disliked
> 
> The Great...  
>    
>  I want to know... how to change the setting. so it not open trade with 0.2lot.. i just want to trade with 0.1lot only... because i using US2000.. i will try this... on real account....  
>    
>  Thanks for this system...  
>    
>  Bandito
> 
> Ignored

turn MM=false; then change lot = 0.1  
  
But I believe this EA and Strategy requires further testing before live trading. But its your money and your choice.  
  
-Mikhail 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#153](/thread/post/216377#post216377 "Post Permalink")

  * Feb 14, 2007 12:30am  Feb 14, 2007 12:30am 

  * [ BearPaw](bearpaw)

  * | Joined Jul 2006  | Status: A Trader for Life | [218 Posts](/search?do=process&provider=Member&searchuser=13999)

> [Quoting bandito](/thread/post/216368#post216368 "View Quoted Post")
> 
> Disliked
> 
> The Great...  
>    
>  I want to know... how to change the setting. so it not open trade with 0.2lot.. i just want to trade with 0.1lot only... because i using US2000.. i will try this... on real account....  
>    
>  Thanks for this system...  
>    
>  Bandito
> 
> Ignored

Bandito,  
  
You need to go into properties of the expert advisor or ea on the pair that you are trading, and you need to do it for each pair...., make MM (moneymanagement) False, make Microlots True, and change lot size to .10.  
  
I believe that will do what you desire.  
  
BP 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#154](/thread/post/216378#post216378 "Post Permalink")

  * Feb 14, 2007 12:30am  Feb 14, 2007 12:30am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar22836_4.gif) ilanr](ilanr)

  * | Joined Oct 2006  | Status: Trader | [260 Posts](/search?do=process&provider=Member&searchuser=22836)

> [Quoting mikhaildgreat](/thread/post/216313#post216313 "View Quoted Post")
> 
> Disliked
> 
> Great results bandito... your the only one testing this on M15 but marvelous results. Anyone willing to manually backtest this strategy on M15 timeframe?  
>    
>  Bandito keep up the great work! ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)  
>    
>  Regards,  
>  Mikhail
> 
> Ignored

Bandito's results made me curious. I did a quick manual backtest for Oct 2006 eurusd (it was a tough month...). The optimal TP at M30 timeframe would be 60 p. after crossing the MA's, while for M15 the optimal TP would be 20 p. Re. SL, I now firmly believe that the other side of MA's is best.   
  
M15 produced twice as many trades as M30, but in terms of gain, it was about the same amount. So, being a lazy person, I stay with the original TF, but I guess some people would like M15 more...  
  
Thanks, Bandito, for generating this nice idea! 

sans peur et sans reproche

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#155](/thread/post/216384#post216384 "Post Permalink")

  * Feb 14, 2007 12:36am  Feb 14, 2007 12:36am 

  * [ bandito](bandito)

  * | Joined Jan 2007  | Status: Trader | [19 Posts](/search?do=process&provider=Member&searchuser=31069)

The Great... Thanks for the advice...  
  
i really tension trade manually... its also the same method... waiting for corssing... or etc...   
except when we trade the news...  
  
it will the great one... i belived...  
  
i will post the result... with other timeframe... using original poria setting 30m & 1hour.  
  
Bandito 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#156](/thread/post/216385#post216385 "Post Permalink")

  * Feb 14, 2007 12:37am  Feb 14, 2007 12:37am 

  * [ BearPaw](bearpaw)

  * | Joined Jul 2006  | Status: A Trader for Life | [218 Posts](/search?do=process&provider=Member&searchuser=13999)

Guys,  
  
Right now I use IBFX for my MT4 indicators. Do you guys have reccomendations of other brokers that use MT4?  
  
Is there an ECN that uses MT4?  
  
Thanks,  
  
BP 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#157](/thread/post/216394#post216394 "Post Permalink")

  * Feb 14, 2007 12:49am  Feb 14, 2007 12:49am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar22836_4.gif) ilanr](ilanr)

  * | Joined Oct 2006  | Status: Trader | [260 Posts](/search?do=process&provider=Member&searchuser=22836)

> [Quoting BearPaw](/thread/post/216385#post216385 "View Quoted Post")
> 
> Disliked
> 
> Guys,  
>    
>  Right now I use IBFX for my MT4 indicators. Do you guys have reccomendations of other brokers that use MT4?  
>    
>  Is there an ECN that uses MT4?  
>    
>  Thanks,  
>    
>  BP
> 
> Ignored

In another thread, it has been claimed than an ECN can't use MT4. Regarding market-maker broker, I think that the most important thing for a beginning trader is to use micro-accounts (pip = $.10), which allows for optimal money management. I'm aware of four MT4 broker with micro accounts: Interbank FX (I read awful comments aboput them here and on other forums, but check yourself), NorthFinance (good reviews, 1:500 leverage, an off-shore company - it scares some people), MWHeadway (not many reviews, but seem fair, 3 p. spread on gbpusd, 1:200 leverage), and FXDD (1:200, 4 p. on gbpusd) which I use, they are not bad - if you don't trade the first minute of the news. 

sans peur et sans reproche

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#158](/thread/post/216408#post216408 "Post Permalink")

  * Feb 14, 2007 1:05am  Feb 14, 2007 1:05am 

  * [ JamDown](jamdown)

  * | Joined Dec 2006  | Status: Trader | [39 Posts](/search?do=process&provider=Member&searchuser=27324)

> [Quoting BearPaw](/thread/post/216385#post216385 "View Quoted Post")
> 
> Disliked
> 
> Guys,  
>    
>  Right now I use IBFX for my MT4 indicators. Do you guys have reccomendations of other brokers that use MT4?  
>    
>  Is there an ECN that uses MT4?  
>    
>  Thanks,  
>    
>  BP
> 
> Ignored

My IB can get you on an ECN that uses MT4 if your Dep. is over 20k.  
I retested with a 100 pip stop loss and a 75pip tp. Here are the results...better than before. For the mont of Jan-Feb 13 it never went more than 20 pips in the reverse of the cross so Drawdown was minimal. I dont know how to show that on the report but you can see on the visual. My opinion is that these crosses are very significant to the overall trend so you would have to give it a little more than a 20-50 pip room to do its thing but at the same time go for the big TP. But then again, January was a choppy month for the Cable so that might have been the best scenerio for this setup.  
BigDog 

Attached File(s)

![File Type: doc](https://assets.faireconomy.media/images/attach/doc.gif) [Beta3 test100sl75tp.doc](/attachment/file/22291?d=1171382390) 8 KB | 504 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#159](/thread/post/216450#post216450 "Post Permalink")

  * Feb 14, 2007 1:41am  Feb 14, 2007 1:41am 

  * [ BearPaw](bearpaw)

  * | Joined Jul 2006  | Status: A Trader for Life | [218 Posts](/search?do=process&provider=Member&searchuser=13999)

> [Quoting JamDown](/thread/post/216408#post216408 "View Quoted Post")
> 
> Disliked
> 
> My IB can get you on an ECN that uses MT4 if your Dep. is over 20k.  
>  I retested with a 100 pip stop loss and a 75pip tp. Here are the results...better than before. For the mont of Jan-Feb 13 it never went more than 20 pips in the reverse of the cross so Drawdown was minimal. I dont know how to show that on the report but you can see on the visual. My opinion is that these crosses are very significant to the overall trend so you would have to give it a little more than a 20-50 pip room to do its thing but at the same time go for the big TP. But then again, January was a choppy month for the Cable so that might have been the best scenerio for this setup.  
>  BigDog
> 
> Ignored

Thanks JamDown...now that is interesting and more conclusive to me...would be interesting to see other months...  
  
By the way...who is your IB?  
  
Thanks,  
  
BP 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#160](/thread/post/216503#post216503 "Post Permalink")

  * Feb 14, 2007 2:36am  Feb 14, 2007 2:36am 

  * [ forig](forig)

  * | Joined May 2006  | Status: Trader | [33 Posts](/search?do=process&provider=Member&searchuser=9267)

> [Quoting JamDown](/thread/post/216408#post216408 "View Quoted Post")
> 
> Disliked
> 
> My IB can get you on an ECN that uses MT4 if your Dep. is over 20k.  
>  I retested with a 100 pip stop loss and a 75pip tp. Here are the results...better than before. For the mont of Jan-Feb 13 it never went more than 20 pips in the reverse of the cross so Drawdown was minimal. I dont know how to show that on the report but you can see on the visual. My opinion is that these crosses are very significant to the overall trend so you would have to give it a little more than a 20-50 pip room to do its thing but at the same time go for the big TP. But then again, January was a choppy month for the Cable so that might have been the best scenerio for this setup.  
>  BigDog
> 
> Ignored

It`s absolutely useless to make test with Modelling quality less then 80%, don`t believe in that resalts. You shood try to use all 1min qoutes for selected period - it`s a must. Have a look at my test resalts, I`ve used 1 lot, with 4 - it`s account crash.  
Good luck. 

Attached File(s)

![File Type: zip](https://assets.faireconomy.media/images/attach/zip.gif) [Beta3test.zip](/attachment/file/22310?d=1171387992) 11 KB | 333 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * The Pouria EA Development Thread
  *   * [ **Reply to Thread** ](/thread/17242-the-pouria-ea-development-thread/reply#reply)

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

[The Pouria Method](/thread/17011-the-pouria-method "OKay here is one of the 4 best systems that I've made and used, with this system I pickup atleast 50 pips a day, I'm sharing this because...") 562 replies

[Lessons Learned during System Development](/thread/2986-lessons-learned-during-system-development "Hi, 
  
I've been reading through the forum and somehow I'm in the process of developing my own system.. But not really doing actual...") 29 replies

[(pouria method II on the test)](/thread/23104-pouria-method-ii-on-the-test "Hello  
pouria method II is now DONE thanks to the group of experts and mathematicians that helped and made this method. 
now we are...") 218 replies

[System Development Secrets](/thread/7342-system-development-secrets "&lt;meta http-equiv=&quot;CONTENT-TYPE&quot; content=&quot;text/html; charset=utf-8&quot;&gt;&lt;title&gt;&lt;/title&gt;&lt;meta name=&quot;GENERATOR&quot; content=&quot;OpenOffice.org 2.0 ...") 5 replies

[Metatrader 4 Development Course](/thread/5906-metatrader-4-development-course "Here is the Mql_4_Metatrader_4_Development_Course in pdf \(link fixed\) : 
 
http://www.freefilehosting.org/pupload/view/8711") 3 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/17242-the-pouria-ea-development-thread/reply#reply)
  * Subscribe
  * [45](javascript:void\(0\);)

Attachments: The Pouria EA Development Thread

Tags: The Pouria EA Development Thread

#  [](/thread/17242-the-pouria-ea-development-thread)The Pouria EA Development Thread 

  * 

  * [#161](/thread/post/216507#post216507 "Post Permalink")

  * Feb 14, 2007 2:42am  Feb 14, 2007 2:42am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar22836_4.gif) ilanr](ilanr)

  * | Joined Oct 2006  | Status: Trader | [260 Posts](/search?do=process&provider=Member&searchuser=22836)

When you backtest, note that different weekdays behave differently. Try to play with TP to adjust it for the weekday. For example, it seems that for eurusd, the best TP on Mondays is 80 pips from the MA lines; on Tue: 20; Wed: 60; Thu & Fri: 90. This pattern is similar to what I've seen in other methods, so I think it's valid. 

sans peur et sans reproche

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#162](/thread/post/216629#post216629 "Post Permalink")

  * Feb 14, 2007 5:41am  Feb 14, 2007 5:41am 

  * [ bandito](bandito)

  * | Joined Jan 2007  | Status: Trader | [19 Posts](/search?do=process&provider=Member&searchuser=31069)

The Great...  
  
Take are look at the zip file... i think eurjpy today was false signal.. its late after the crossing  
  
Bandito 

Attached File(s)

![File Type: zip](https://assets.faireconomy.media/images/attach/zip.gif) [2007-02-13_223419.zip](/attachment/file/22329?d=1171399269) 60 KB | 261 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#163](/thread/post/216676#post216676 "Post Permalink")

  * Feb 14, 2007 6:27am  Feb 14, 2007 6:27am 

  * [ BearPaw](bearpaw)

  * | Joined Jul 2006  | Status: A Trader for Life | [218 Posts](/search?do=process&provider=Member&searchuser=13999)

> [Quoting forig](/thread/post/216503#post216503 "View Quoted Post")
> 
> Disliked
> 
> It`s absolutely useless to make test with Modelling quality less then 80%, don`t believe in that resalts. You shood try to use all 1min qoutes for selected period - it`s a must. Have a look at my test resalts, I`ve used 1 lot, with 4 - it`s account crash.  
>  Good luck.
> 
> Ignored

Forig...I was confused with what you were saying at first, but then when I looked at the zipped file, I noticed that you were just saying with a 100 pip SL and 75 pip TP, and with the 1 minute ticks...it is not worth it in your opinion?  
  
Thanks,  
  
BP 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#164](/thread/post/216679#post216679 "Post Permalink")

  * Feb 14, 2007 6:29am  Feb 14, 2007 6:29am 

  * [ BearPaw](bearpaw)

  * | Joined Jul 2006  | Status: A Trader for Life | [218 Posts](/search?do=process&provider=Member&searchuser=13999)

> [Quoting bandito](/thread/post/216629#post216629 "View Quoted Post")
> 
> Disliked
> 
> The Great...  
>    
>  Take are look at the zip file... i think eurjpy today was false signal.. its late after the crossing  
>    
>  Bandito
> 
> Ignored

Euro/JPY crossed the 75/85 and then bought when the MACD was positive...that is why it looks like a late buy.  
  
My beta bought eur/jpy and made a profit on it.  
  
BP 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#165](/thread/post/216690#post216690 "Post Permalink")

  * Feb 14, 2007 6:40am  Feb 14, 2007 6:40am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar19504_4.gif) 1Sundevil](1sundevil)

  * | Joined Sep 2006  | Status: Trader | [228 Posts](/search?do=process&provider=Member&searchuser=19504)

> [Quoting ilanr](/thread/post/216507#post216507 "View Quoted Post")
> 
> Disliked
> 
> When you backtest, note that different weekdays behave differently. Try to play with TP to adjust it for the weekday. For example, it seems that for eurusd, the best TP on Mondays is 80 pips from the MA lines; on Tue: 20; Wed: 60; Thu & Fri: 90. This pattern is similar to what I've seen in other methods, so I think it's valid.
> 
> Ignored

I just started demo testing this as well and I have adjusted the EUR/USD TP to 30 pips and the GBP/USD to 85 pips. The only reason being that the EUR doesn't move the same distance as the GBP and I'd rather 1) be profitable and 2) not have to hold a trade for too long as the EA will get another signal as we go.  
  
So far I am in two EA activated demo trades:  
  
EUR/USD B @ 3026 +9 so far  
GBP/USD B @ 9453 +19 so far 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#166](/thread/post/216799#post216799 "Post Permalink")

  * Feb 14, 2007 8:26am  Feb 14, 2007 8:26am 

  * [ BearPaw](bearpaw)

  * | Joined Jul 2006  | Status: A Trader for Life | [218 Posts](/search?do=process&provider=Member&searchuser=13999)

Mikhail,  
  
On the original Pouria thread, there is talk about the macd not needing to be greater than or less than zero....instead just moving upward or downward to confirm the cross.....  
  
Seems that maybe forexpert said something of the sort in his original post....  
  
Thoughts? Check it out for more specifics....  
  
Maybe that would get us in some of these trades quicker than having us wait? Or maybe it is better to be patient and prudent.  
  
Don't know.  
  
BP 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#167](/thread/post/216998#post216998 "Post Permalink")

  * Feb 14, 2007 2:01pm  Feb 14, 2007 2:01pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar25698_4.gif) mikhaildgreat](mikhaildgreat)

  * | Joined Nov 2006  | Status: EA Programmer | [298 Posts](/search?do=process&provider=Member&searchuser=25698)

I tested the EA with an M15 timeframe I got 11 trade only 2 of them profitable ![](https://resources.faireconomy.media/images/emojis/64/1f923.png?v=15.1)   
  
Anyways at least now we know that all the entry bugs has been eliminated all trades were according to the rules and were valid. So now we can focus on improving the strategy. I will release v1 later with the following improvements. MACD filter = true/false. you can turn off MACD filter as you see fit and Matingale = true/false. where you can employ martingale or not... And Also MA stoploss option.  
  
So see you again later with these improvements.  
  
-Mikhail 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#168](/thread/post/217003#post217003 "Post Permalink")

  * Feb 14, 2007 2:04pm  Feb 14, 2007 2:04pm 

  * [ bandito](bandito)

  * | Joined Jan 2007  | Status: Trader | [19 Posts](/search?do=process&provider=Member&searchuser=31069)

The Great  
  
Cannot using TF15... to many losses for today  
  
Bandito 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#169](/thread/post/217018#post217018 "Post Permalink")

  * Feb 14, 2007 2:14pm  Feb 14, 2007 2:14pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar18503_10.gif) Se[V]eN](member.php?u=18503)

  * | Joined Sep 2006  | Status: Im A Lucky Hyena | [449 Posts](/search?do=process&provider=Member&searchuser=18503)

> [Quoting mikhaildgreat](/thread/post/216998#post216998 "View Quoted Post")
> 
> Disliked
> 
> I tested the EA with an M15 timeframe I got 11 trade only 2 of them profitable ![](https://resources.faireconomy.media/images/emojis/64/1f923.png?v=15.1)
> 
> Ignored

> [Quoting mikhaildgreat](/thread/post/216998#post216998 "View Quoted Post")
> 
> Disliked
> 
>   
>  Anyways at least now we know that all the entry bugs has been eliminated all trades were according to the rules and were valid. So now we can focus on improving the strategy. I will release v1 later with the following improvements. MACD filter = true/false. you can turn off MACD filter as you see fit and Matingale = true/false. where you can employ martingale or not... And Also MA stoploss option.  
>    
>  So see you again later with these improvements.  
>    
>  -Mikhail
> 
> Ignored

  
  
hello all.....  
  
  
i know that im not contributing anything in this thread...but its nothing wrong to support all of the great effort here by watching....anyway mikhail...i got question here...i personally think that martingale principle is working for this method...so what is your personal opinion about martingale?? 

"Analysis Is Hard But Trade Is Easy"![](https://resources.faireconomy.media/images/emojis/64/1f644.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#170](/thread/post/217026#post217026 "Post Permalink")

  * Feb 14, 2007 2:35pm  Feb 14, 2007 2:35pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar25698_4.gif) mikhaildgreat](mikhaildgreat)

  * | Joined Nov 2006  | Status: EA Programmer | [298 Posts](/search?do=process&provider=Member&searchuser=25698)

> [Quoting Se[V]eN](/thread/post/217018#post217018 "View Quoted Post")
> 
> Disliked
> 
> [left]  
>    
>    
>    
>  hello all.....  
>    
>    
>  i know that im not contributing anything in this thread...but its nothing wrong to support all of the great effort here by watching....anyway mikhail...i got question here...i personally think that martingale principle is working for this method...so what is your personal opinion about martingale??
> 
> Ignored

I think it could work. Martingale will work as long as your account can support it and there are minimal consecutive losses. Max we have seen with this strategy is 3 consecutive losses so I think It may just work.  
  
We just have to try it and see how it fairs.  
  
Regards,  
Mikhail 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#171](/thread/post/217109#post217109 "Post Permalink")

  * Feb 14, 2007 4:48pm  Feb 14, 2007 4:48pm 

  * [ neshat](neshat)

  * | Joined Sep 2006  | Status: Trader | [70 Posts](/search?do=process&provider=Member&searchuser=20436)

Hi  
See in picture a false sell signal in USD/JPY by beta3 EA: 

Attached Image

![](/attachment/image/22392?d=1171439199)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#172](/thread/post/217112#post217112 "Post Permalink")

  * Feb 14, 2007 4:53pm  Feb 14, 2007 4:53pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar5179_4.gif) cgldsmth](cgldsmth)

  * Joined Dec 2005 | Status: It's only money | [1,413 Posts](/search?do=process&provider=Member&searchuser=5179)

Mikhail - you're doing great work.  
I think what will really give this EA potential will be a partial take profit routine, whereby the first lot is closed fro about 15 pips and the second lot running free with a stop at break even. Just eyeballing the charts this would harvest some of those very lng trend we can AUDUSD as an example).  
  
looking forward to v1.0 

TRADE FOR SWAP

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#173](/thread/post/217119#post217119 "Post Permalink")

  * Feb 14, 2007 4:56pm  Feb 14, 2007 4:56pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar5179_4.gif) cgldsmth](cgldsmth)

  * Joined Dec 2005 | Status: It's only money | [1,413 Posts](/search?do=process&provider=Member&searchuser=5179)

attached is the manageTP EA. Perhaps yu can take somecode from here to implement the above TP strategy? 

Attached File(s)

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [ManageTPv2-3.mq4](/attachment/file/22394?d=1171439757) 6 KB | 314 downloads 

TRADE FOR SWAP

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#174](/thread/post/217123#post217123 "Post Permalink")

  * Feb 14, 2007 5:03pm  Feb 14, 2007 5:03pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar22836_4.gif) ilanr](ilanr)

  * | Joined Oct 2006  | Status: Trader | [260 Posts](/search?do=process&provider=Member&searchuser=22836)

> [Quoting mikhaildgreat](/thread/post/216998#post216998 "View Quoted Post")
> 
> Disliked
> 
> I will release v1 later with the following improvements. MACD filter = true/false. you can turn off MACD filter as you see fit and Matingale = true/false. where you can employ martingale or not... And Also MA stoploss option.
> 
> Ignored

Sounds like a dream...  
  
Would it be possible to make TP a variable whose value can be defined by the user? Would make experimenting easier...  
  
Have a great day! 

sans peur et sans reproche

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#175](/thread/post/217159#post217159 "Post Permalink")

  * Feb 14, 2007 5:43pm  Feb 14, 2007 5:43pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar25698_4.gif) mikhaildgreat](mikhaildgreat)

  * | Joined Nov 2006  | Status: EA Programmer | [298 Posts](/search?do=process&provider=Member&searchuser=25698)

> [Quoting cgldsmth](/thread/post/217112#post217112 "View Quoted Post")
> 
> Disliked
> 
> Mikhail - you're doing great work.  
>  I think what will really give this EA potential will be a partial take profit routine, whereby the first lot is closed fro about 15 pips and the second lot running free with a stop at break even. Just eyeballing the charts this would harvest some of those very lng trend we can AUDUSD as an example).  
>    
>  looking forward to v1.0
> 
> Ignored

I Agree. But one step at a time my friend..  
  
-Mikhail 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#176](/thread/post/217160#post217160 "Post Permalink")

  * Feb 14, 2007 5:45pm  Feb 14, 2007 5:45pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar25698_4.gif) mikhaildgreat](mikhaildgreat)

  * | Joined Nov 2006  | Status: EA Programmer | [298 Posts](/search?do=process&provider=Member&searchuser=25698)

> [Quoting neshat](/thread/post/217109#post217109 "View Quoted Post")
> 
> Disliked
> 
> Hi  
>  See in picture a false sell signal in USD/JPY by beta3 EA:
> 
> Ignored

This is a valid entry because 5MA line went above the 75MA before going back down...  
  
-Mikhail 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#177](/thread/post/217162#post217162 "Post Permalink")

  * Feb 14, 2007 5:46pm  Feb 14, 2007 5:46pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar25698_4.gif) mikhaildgreat](mikhaildgreat)

  * | Joined Nov 2006  | Status: EA Programmer | [298 Posts](/search?do=process&provider=Member&searchuser=25698)

> [Quoting ilanr](/thread/post/217123#post217123 "View Quoted Post")
> 
> Disliked
> 
> Sounds like a dream...  
>    
>  Would it be possible to make TP a variable whose value can be defined by the user? Would make experimenting easier...  
>    
>  Have a great day!
> 
> Ignored

Yup you will still be able to define TP and SL, Martingale will only be an added option. I should have it ready really soon.  
  
-Mikhail 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#178](/thread/post/217233#post217233 "Post Permalink")

  * Feb 14, 2007 6:56pm  Feb 14, 2007 6:56pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar25698_4.gif) mikhaildgreat](mikhaildgreat)

  * | Joined Nov 2006  | Status: EA Programmer | [298 Posts](/search?do=process&provider=Member&searchuser=25698)

Hello These are new options you can find in V1 of this EA, feel free to play around with the settings to find the most profitable results.  
  
So here they are:  
  
**MACDfiler** = use MACD filter or not. if set to false I suggest you turn on confirmedonentry = ture; because using MA alone will get you more wipsaws  
**  

  
**UseMartingale** = if set to true every time you suffer a loss lot size will be doubled until you get a profitable trade(Standard MM will be set to false if Martingale is set to true)  
**AccountIsMicroM** = set to true of you are using micro account (0.01 lots)  
  
**StartingLots** = Amount of lots you want to start with.  
**MaxLots** = Maximum lots allowed during martingale.(this number in lots will not be exceeded even if you suffer many consecutive losses)   
  
  
If you have questions, clarifications, suggestions pls dont hesitate to post.  
  
Regards,  
Mikhail  
  
PS. I havent put the MA stoploss yet, I will have it ready by the next version. TY. 

Attached File(s)

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [Pouria EA V1.mq4](/attachment/file/22404?d=1171446740) 15 KB | 439 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#179](/thread/post/217399#post217399 "Post Permalink")

  * Feb 14, 2007 9:20pm  Feb 14, 2007 9:20pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar18503_10.gif) Se[V]eN](member.php?u=18503)

  * | Joined Sep 2006  | Status: Im A Lucky Hyena | [449 Posts](/search?do=process&provider=Member&searchuser=18503)

> [Quoting mikhaildgreat](/thread/post/217233#post217233 "View Quoted Post")
> 
> Disliked
> 
> Hello These are new options you can find in V1 of this EA, feel free to play around with the settings to find the most profitable results.
> 
> Ignored

> [Quoting mikhaildgreat](/thread/post/217233#post217233 "View Quoted Post")
> 
> Disliked
> 
>   
>  So here they are:  
>    
>  **MACDfiler** = use MACD filter or not. if set to false I suggest you turn on confirmedonentry = ture; because using MA alone will get you more wipsaws  
>  **  

>    
>  **UseMartingale** = if set to true every time you suffer a loss lot size will be doubled until you get a profitable trade(Standard MM will be set to false if Martingale is set to true)  
>  **AccountIsMicroM** = set to true of you are using micro account (0.01 lots)  
>    
>  **StartingLots** = Amount of lots you want to start with.  
>  **MaxLots** = Maximum lots allowed during martingale.(this number in lots will not be exceeded even if you suffer many consecutive losses)   
>    
>    
>  If you have questions, clarifications, suggestions pls dont hesitate to post.  
>    
>  Regards,  
>  Mikhail  
>    
>  PS. I havent put the MA stoploss yet, I will have it ready by the next version. TY.
> 
> Ignored

  
  
cool man...thanks for sharing....  
EA with martingale???...i think this is a most advance EA version...  
i salute u... 

"Analysis Is Hard But Trade Is Easy"![](https://resources.faireconomy.media/images/emojis/64/1f644.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#180](/thread/post/217436#post217436 "Post Permalink")

  * Feb 14, 2007 9:55pm  Feb 14, 2007 9:55pm 

  * [ BearPaw](bearpaw)

  * | Joined Jul 2006  | Status: A Trader for Life | [218 Posts](/search?do=process&provider=Member&searchuser=13999)

So, Day 3, with Beta 3....looks like no false signals...using macd to confirm...  
  
9 trades total.  
5 profitable   
4 losses  
  
Net gain/loss of +5 pips  
  
SL is at 20 for each pair and TP are as defined in original Pouria method.  
  
So, cumalative results....  
  
Day 1 = +40pips  
Day 2 = -7pips  
Day 3 = +5pips  
  
Slowing down a little...but we shall see!!  
  
BP 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * The Pouria EA Development Thread
  *   * [ **Reply to Thread** ](/thread/17242-the-pouria-ea-development-thread/reply#reply)

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

[The Pouria Method](/thread/17011-the-pouria-method "OKay here is one of the 4 best systems that I've made and used, with this system I pickup atleast 50 pips a day, I'm sharing this because...") 562 replies

[Lessons Learned during System Development](/thread/2986-lessons-learned-during-system-development "Hi, 
  
I've been reading through the forum and somehow I'm in the process of developing my own system.. But not really doing actual...") 29 replies

[(pouria method II on the test)](/thread/23104-pouria-method-ii-on-the-test "Hello  
pouria method II is now DONE thanks to the group of experts and mathematicians that helped and made this method. 
now we are...") 218 replies

[System Development Secrets](/thread/7342-system-development-secrets "&lt;meta http-equiv=&quot;CONTENT-TYPE&quot; content=&quot;text/html; charset=utf-8&quot;&gt;&lt;title&gt;&lt;/title&gt;&lt;meta name=&quot;GENERATOR&quot; content=&quot;OpenOffice.org 2.0 ...") 5 replies

[Metatrader 4 Development Course](/thread/5906-metatrader-4-development-course "Here is the Mql_4_Metatrader_4_Development_Course in pdf \(link fixed\) : 
 
http://www.freefilehosting.org/pupload/view/8711") 3 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/17242-the-pouria-ea-development-thread/reply#reply)
  * Subscribe
  * [45](javascript:void\(0\);)

Attachments: The Pouria EA Development Thread

Tags: The Pouria EA Development Thread

#  [](/thread/17242-the-pouria-ea-development-thread)The Pouria EA Development Thread 

  * 

  * [#181](/thread/post/217469#post217469 "Post Permalink")

  * Feb 14, 2007 10:26pm  Feb 14, 2007 10:26pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar22836_4.gif) ilanr](ilanr)

  * | Joined Oct 2006  | Status: Trader | [260 Posts](/search?do=process&provider=Member&searchuser=22836)

> [Quoting mikhaildgreat](/thread/post/217233#post217233 "View Quoted Post")
> 
> Disliked
> 
> PS. I havent put the MA stoploss yet, I will have it ready by the next version. TY.
> 
> Ignored

  
Bravo. A dedicated PC, a fresh demo account and myself are eagerly waiting for the next version. By now, I'm sure that the MA SL is the right way to go.  
  
Your work is greatly appreciated, Mikhail!  
  
Ilan 

sans peur et sans reproche

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#182](/thread/post/217493#post217493 "Post Permalink")

  * Feb 14, 2007 10:53pm  Feb 14, 2007 10:53pm 

  * [ BearPaw](bearpaw)

  * | Joined Jul 2006  | Status: A Trader for Life | [218 Posts](/search?do=process&provider=Member&searchuser=13999)

Can anyone describe this martingale to me please?  
  
Thanks,  
  
BP 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#183](/thread/post/217680#post217680 "Post Permalink")

  * Feb 15, 2007 1:01am  Feb 15, 2007 1:01am 

  * [ ghamal](ghamal)

  * | Joined Dec 2006  | Status: Trader | [23 Posts](/search?do=process&provider=Member&searchuser=27492)

> [Quoting BearPaw](/thread/post/217493#post217493 "View Quoted Post")
> 
> Disliked
> 
> Can anyone describe this martingale to me please?  
>    
>  Thanks,  
>    
>  BP
> 
> Ignored

<http://en.wikipedia.org/wiki/Martingale_(betting_system>)  
  
It basically doubles your lots after every loss. Might be interesting with this method as it is supposed to have few loses in a row, but it's still risky and will wipe out your account if the EA goes haywire. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#184](/thread/post/217740#post217740 "Post Permalink")

  * Feb 15, 2007 1:41am  Feb 15, 2007 1:41am 

  * [ BearPaw](bearpaw)

  * | Joined Jul 2006  | Status: A Trader for Life | [218 Posts](/search?do=process&provider=Member&searchuser=13999)

Here is a copy of a post and my reply in the other thread...I would like to have input if my results are unique or if others have mirrored my results.  
  
.....BP....  
  

> [Quoting 1Sundevil](/thread/post/217556#post217556 "View Quoted Post")
> 
> Disliked
> 
> I started late yesterday afternoon, around the end of the NYC session. So far the EA has dropped me in 5 demo trades and all 5 have been successful.  
>    
>  GBP +20  
>  EUR +11  
>  GBP +20  
>  EUR +20  
>  _JPY +15_  
>    
>  **total +86**  
>    
>  My demo account was at $5,100 when I stared and is now at $5,492.76 an increase of 7.7% in one day. I am just going to keep the computer on and the EA active all week. The JPY trade was opened and closed as I slept last night.   
>    
>  So far so good for this strategy. I'm using a 50 pip SL and a 15 or 20 pip TP as is recommended on the first page. I have loaded the EA for only four currencies: GBP/USD, EUR/USD, USD/CHF and USD/JPY.
> 
> Ignored

I am using the EA...beta 3...with all the currencies that Forexpert recommended except CADJPY cause my broker does not have it.  
  
yesterday I was entered into GBP trade once and usdjpy trade twice.  
  
Here is what was entered yesterday and the results. My TP is as Forexpert recommended. My SL is at 20. Maybe the stop loss needs to be changed? Have not looked at that.  
  
NZDUSD +25  
EURCHF -20  
EURCHF +15  
GBPUSD -20  
CHFJPY -20  
AUDJPY +15  
USDJPY -20  
CHFJPY +15  
USDJPY +15  
  
Currently there are no open positions. A very slow day so far.  
  
BP 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#185](/thread/post/217770#post217770 "Post Permalink")

  * Feb 15, 2007 2:03am  Feb 15, 2007 2:03am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar19504_4.gif) 1Sundevil](1sundevil)

  * | Joined Sep 2006  | Status: Trader | [228 Posts](/search?do=process&provider=Member&searchuser=19504)

> [Quoting BearPaw](/thread/post/217740#post217740 "View Quoted Post")
> 
> Disliked
> 
> Currently there are no open positions. A very slow day so far.  
>    
>  BP
> 
> Ignored

Same here, no positions opened. Now correct me if I'm wrong here, but since the MA (5) has to cross the 85 and 75 for a trade to be entered, what do we do when the trend is moving away from the red lines?   
  
To be honest, if the system can generate even +50 pips a week or more consistently then it's a HUGE winner. +86 yesterday may have been a fluke as I was still tuning the data on the EA. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#186](/thread/post/217787#post217787 "Post Permalink")

  * Feb 15, 2007 2:15am  Feb 15, 2007 2:15am 

  * [ BearPaw](bearpaw)

  * | Joined Jul 2006  | Status: A Trader for Life | [218 Posts](/search?do=process&provider=Member&searchuser=13999)

> [Quoting 1Sundevil](/thread/post/217770#post217770 "View Quoted Post")
> 
> Disliked
> 
> Same here, no positions opened.Now correct me if I'm wrong here, but since the MA (5) has to cross the 85 and 75 for a trade to be entered, what do we do when the trend is moving away from the red lines?   
>    
>  To be honest, if the system can generate even +50 pips a week or more consistently then it's a HUGE winner. +86 yesterday may have been a fluke as I was still tuning the data on the EA.
> 
> Ignored

I dont have the answer to your first question Sundevil. I agree on the positive pips action. I wonder if your stop loss is what is making it different for you?  
  
We shall see.  
  
BP 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#187](/thread/post/217799#post217799 "Post Permalink")

  * Feb 15, 2007 2:25am  Feb 15, 2007 2:25am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar19504_4.gif) 1Sundevil](1sundevil)

  * | Joined Sep 2006  | Status: Trader | [228 Posts](/search?do=process&provider=Member&searchuser=19504)

> [Quoting BearPaw](/thread/post/217787#post217787 "View Quoted Post")
> 
> Disliked
> 
> I dont have the answer to your first question Sundevil. I agree on the positive pips action. I wonder if your stop loss is what is making it different for you?  
>    
>  We shall see.  
>    
>  BP
> 
> Ignored

I can tell you that if my SL was at 20 pips I would have been stopped out of both GBP trades. Also, both were at +20 before dropping down to -20 and then back up again (see 11:30pm EST). Initially I had my TP at a much higher level and then, after seeing it drop, rethought my strategy and felt that the system originator was correct in going after +15 and +20 TP's with higher lots. Again, 7.7% increase in one day with 5 trades in unbelievably good. Let's hope that it does close to this we ll over the long haul. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#188](/thread/post/217805#post217805 "Post Permalink")

  * Feb 15, 2007 2:34am  Feb 15, 2007 2:34am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar10157_7.gif) amaruenterprise](amaruenterprise)

  * | Joined May 2006  | Status: Trader | [282 Posts](/search?do=process&provider=Member&searchuser=10157)

> [Quoting BearPaw](/thread/post/217493#post217493 "View Quoted Post")
> 
> Disliked
> 
> Can anyone describe this martingale to me please?  
>    
>  Thanks,  
>    
>  BP
> 
> Ignored

Hi Bearpaw to the best of my knowledge the martingale will keep doubling your lot amount if you lose until you get a winner. Could be very profitable but also could devistate your account if several losses in row occur....Valerie....![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) P.S. Anyone if I'm wrong please correct me.....![](https://resources.faireconomy.media/images/emojis/64/1f61c.png?v=15.1): 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#189](/thread/post/217818#post217818 "Post Permalink")

  * Feb 15, 2007 2:43am  Feb 15, 2007 2:43am 

  * [ BearPaw](bearpaw)

  * | Joined Jul 2006  | Status: A Trader for Life | [218 Posts](/search?do=process&provider=Member&searchuser=13999)

> [Quoting amaruenterprise](/thread/post/217805#post217805 "View Quoted Post")
> 
> Disliked
> 
> Hi Bearpaw to the best of my knowledge the martingale will keep doubling your lot amount if you lose until you get a winner. Could be very profitable but also could devistate your account if several losses in row occur....Valerie....![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) P.S. Anyone if I'm wrong please correct me.....![](https://resources.faireconomy.media/images/emojis/64/1f61c.png?v=15.1):
> 
> Ignored

Thanks Amaru (Valerie)....guess I dont want to jump into that!! ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
  
BP 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#190](/thread/post/217835#post217835 "Post Permalink")

  * Feb 15, 2007 2:56am  Feb 15, 2007 2:56am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar7129_7.gif) smjones](smjones)

  * Joined Mar 2006 | Status: THANK YOU MERLIN,TWEE and FF Team | [4,603 Posts](/search?do=process&provider=Member&searchuser=7129)

> [Quoting amaruenterprise](/thread/post/217805#post217805 "View Quoted Post")
> 
> Disliked
> 
> Hi Bearpaw to the best of my knowledge the martingale will keep doubling your lot amount if you lose until you get a winner. Could be very profitable but also could devistate your account if several losses in row occur....Valerie....![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1) P.S. Anyone if I'm wrong please correct me.....![](https://resources.faireconomy.media/images/emojis/64/1f61c.png?v=15.1):
> 
> Ignored

Valerie, you are absolutely correct. Martingale was a fromula developed for gambling a few hundred years ago, It is mathematically sound, but if one gets on a losing streak, their account can be depleated in short order... One way to help avoid that is to use smaller positioning and or to only go a certain number of levels deep. and then start over and accept the loss.  
  
Another way is to disperse the loss in a sequence of trades.  
  
The problem is these are all negative progression methods.   
Another is **D'Alembert method,** which while risky is not as risky, but still negative progression**.** Just google it and you will see how it works.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#191](/thread/post/218047#post218047 "Post Permalink")

  * Feb 15, 2007 6:55am  Feb 15, 2007 6:55am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar25698_4.gif) mikhaildgreat](mikhaildgreat)

  * | Joined Nov 2006  | Status: EA Programmer | [298 Posts](/search?do=process&provider=Member&searchuser=25698)

Hello Again,  
  
I hope by now you have found some profitable settings. This EA has a few additional features that may further enhance the win rate of the EA.  
  
Here are the new features:  
**  
MinCrossDistance =** this is the minimum required distance in pips between 5MA and the 75&85 MAs before the Cross is considered valid. This option gets you in the trade a little later but also prevents whipsaws due to entering too soon. Sometime EA will even miss a trade if the cross between the MAs are too small. Set to zero if you want to disable this option.  
  
**  
MA_StopLoss = "---------- MA StopLoss Settings";**  
  
**useMAStopLoss** = set to true if you want to use 85 and 75 MA as stoploss. Stoploss will be placed on either at 85 or 75 MA depending on which is further from the entry price.  
  
**MINStopLoss** = if MA stoploss is less than this value MINStopLoss will be the value used as stoploss  
**MAXStopLoss** = if MA stoploss is greater than this value MAXStopLoss will be the value used as stoploss  
  
I found that **MinCrossDistance** greatly enhances the win rate of the EA.  
  
I hope I explained that clearly if you have any questions and suggestions, don't hesitate to post. Also if you discover some profitable settings please share it in the thread as well.  
  
  
Enjoy,  
Mikhail 

Attached File(s)

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [Pouria EA V-1.1.mq4](/attachment/file/22483?d=1171490140) 20 KB | 462 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#192](/thread/post/218135#post218135 "Post Permalink")

  * Feb 15, 2007 8:42am  Feb 15, 2007 8:42am 

  * [ BearPaw](bearpaw)

  * | Joined Jul 2006  | Status: A Trader for Life | [218 Posts](/search?do=process&provider=Member&searchuser=13999)

Mikhail,  
  
What time zone are you in? And when are you usually looking at the thread/forex issues?  
  
Thanks,  
  
BP 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#193](/thread/post/218239#post218239 "Post Permalink")

  * Feb 15, 2007 10:43am  Feb 15, 2007 10:43am 

  * [ meltri](meltri)

  * | Joined Oct 2006  | Status: Trader | [59 Posts](/search?do=process&provider=Member&searchuser=22738)

Can we include some logic to check the news and not to trade?  
Can this be an addition to the EA? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#194](/thread/post/218366#post218366 "Post Permalink")

  * Feb 15, 2007 2:18pm  Feb 15, 2007 2:18pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar25698_4.gif) mikhaildgreat](mikhaildgreat)

  * | Joined Nov 2006  | Status: EA Programmer | [298 Posts](/search?do=process&provider=Member&searchuser=25698)

> [Quoting BearPaw](/thread/post/218135#post218135 "View Quoted Post")
> 
> Disliked
> 
> Mikhail,  
>    
>  What time zone are you in? And when are you usually looking at the thread/forex issues?  
>    
>  Thanks,  
>    
>  BP
> 
> Ignored

I live in GMT +8 timezone. but my body clock is a whole different story ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1) I check the thread/issues whenever I'm home then add the necessary modifications when I have time.  
  

> Quoting meltri
> 
> Disliked
> 
> Can we include some logic to check the news and not to trade?  
>  Can this be an addition to the EA?
> 
> Ignored

Yup this can be an addition to the EA but I believe this should be added much later, We can add thi when we already have proven that EA can generate profits, and we find the best settings for each pair.  
  
-Mikhail 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#195](/thread/post/218431#post218431 "Post Permalink")

  * Feb 15, 2007 4:31pm  Feb 15, 2007 4:31pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar22836_4.gif) ilanr](ilanr)

  * | Joined Oct 2006  | Status: Trader | [260 Posts](/search?do=process&provider=Member&searchuser=22836)

> [Quoting mikhaildgreat](/thread/post/218366#post218366 "View Quoted Post")
> 
> Disliked
> 
> I live in GMT +8 timezone.
> 
> Ignored

I live in GMT+2 zone, so it was so nice to get up in the morning and find all these goodies in the sock! MinCrossDistance is a great thing. I find it especially useful in the end of the US and during the Asian sessions (GMT 18:00-06:00), when the prices sometimes cross for less than 6 points and then go back.   
Thank you, Mikhail-d-Santa-Claus! 

sans peur et sans reproche

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#196](/thread/post/218536#post218536 "Post Permalink")

  * Feb 15, 2007 6:40pm  Feb 15, 2007 6:40pm 

  * [ BearPaw](bearpaw)

  * | Joined Jul 2006  | Status: A Trader for Life | [218 Posts](/search?do=process&provider=Member&searchuser=13999)

eurgbp entered into a trade just now...but it doesnt look like it should have.  
  
Entered a buy.  
  
Anyone else see that?   
  
BP 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#197](/thread/post/218545#post218545 "Post Permalink")

  * Feb 15, 2007 6:44pm  Feb 15, 2007 6:44pm 

  * [ rogerha](rogerha)

  * | Joined Aug 2006  | Status: Trader | [273 Posts](/search?do=process&provider=Member&searchuser=15670)

> [Quoting mikhaildgreat](/thread/post/218047#post218047 "View Quoted Post")
> 
> Disliked
> 
> Hello Again,  
>    
>  I hope by now you have found some profitable settings. This EA has a few additional features that may further enhance the win rate of the EA.  
>    
>  Here are the new features:  
>  **  
> MinCrossDistance =** this is the minimum required distance in pips between 5MA and the 75&85 MAs before the Cross is considered valid. This option gets you in the trade a little later but also prevents whipsaws due to entering too soon. Sometime EA will even miss a trade if the cross between the MAs are too small. Set to zero if you want to disable this option.  
>    
>  **  
> MA_StopLoss = "---------- MA StopLoss Settings";**  
>    
>  **useMAStopLoss** = set to true if you want to use 85 and 75 MA as stoploss. Stoploss will be placed on either at 85 or 75 MA depending on which is further from the entry price.  
>    
>  **MINStopLoss** = if MA stoploss is less than this value MINStopLoss will be the value used as stoploss  
>  **MAXStopLoss** = if MA stoploss is greater than this value MAXStopLoss will be the value used as stoploss  
>    
>  I found that **MinCrossDistance** greatly enhances the win rate of the EA.  
>    
>  I hope I explained that clearly if you have any questions and suggestions, don't hesitate to post. Also if you discover some profitable settings please share it in the thread as well.  
>    
>    
>  Enjoy,  
>  Mikhail
> 
> Ignored

Mikhail,  
  
Thanks for your continued hard work, an in particular thanks for adding the MA as a stop loss, I think it may be of value.  
  
I'll continue to test.  
  
Rogerha 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#198](/thread/post/218585#post218585 "Post Permalink")

  * Feb 15, 2007 7:19pm  Feb 15, 2007 7:19pm 

  * [ raven](raven)

  * | Joined Jul 2006  | Status: Trader | [21 Posts](/search?do=process&provider=Member&searchuser=14079)

eurgbp entered into a trade just now...but it doesnt look like it should have.  
  
I had that, i thought it was triggered by the news spike so i manually closed when it was at 0 pips, rather get nothing than lose on a possible retrace.  
  
currently have 2 trades open USD/JPY and USD/CHF both currently losing, but had a GBP/USD winner earlier for 20 pips  
  
running v1.1 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#199](/thread/post/218636#post218636 "Post Permalink")

  * Feb 15, 2007 8:44pm  Feb 15, 2007 8:44pm 

  * [ rogerha](rogerha)

  * | Joined Aug 2006  | Status: Trader | [273 Posts](/search?do=process&provider=Member&searchuser=15670)

Mikhail,  
  
I didn't enter a recent trade on Cable with the new version. I can only assume looking at my settings that I have made a mistake with the MinCrossDistance parameter which I have set to 1.0 ?  
  
What exactly is that ? Its the only difference to my previous settings with the older EA.  
  
Thanks  
  
Rogerha 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#200](/thread/post/218642#post218642 "Post Permalink")

  * Feb 15, 2007 8:52pm  Feb 15, 2007 8:52pm 

  * [ Mobsie](mobsie)

  * | Joined Jan 2007  | Status: Trader | [84 Posts](/search?do=process&provider=Member&searchuser=30399)

Hello,  
  
the new EA open an GBPUSD trade, and is now -15. Well see.  
I post later.  
  
Cheers  
Mobsie 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * The Pouria EA Development Thread
  *   * [ **Reply to Thread** ](/thread/17242-the-pouria-ea-development-thread/reply#reply)

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

[The Pouria Method](/thread/17011-the-pouria-method "OKay here is one of the 4 best systems that I've made and used, with this system I pickup atleast 50 pips a day, I'm sharing this because...") 562 replies

[Lessons Learned during System Development](/thread/2986-lessons-learned-during-system-development "Hi, 
  
I've been reading through the forum and somehow I'm in the process of developing my own system.. But not really doing actual...") 29 replies

[(pouria method II on the test)](/thread/23104-pouria-method-ii-on-the-test "Hello  
pouria method II is now DONE thanks to the group of experts and mathematicians that helped and made this method. 
now we are...") 218 replies

[System Development Secrets](/thread/7342-system-development-secrets "&lt;meta http-equiv=&quot;CONTENT-TYPE&quot; content=&quot;text/html; charset=utf-8&quot;&gt;&lt;title&gt;&lt;/title&gt;&lt;meta name=&quot;GENERATOR&quot; content=&quot;OpenOffice.org 2.0 ...") 5 replies

[Metatrader 4 Development Course](/thread/5906-metatrader-4-development-course "Here is the Mql_4_Metatrader_4_Development_Course in pdf \(link fixed\) : 
 
http://www.freefilehosting.org/pupload/view/8711") 3 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/17242-the-pouria-ea-development-thread/reply#reply)
  * Subscribe
  * [45](javascript:void\(0\);)

Attachments: The Pouria EA Development Thread

Tags: The Pouria EA Development Thread

#  [](/thread/17242-the-pouria-ea-development-thread)The Pouria EA Development Thread 

  * 

  * [#201](/thread/post/218668#post218668 "Post Permalink")

  * Feb 15, 2007 9:22pm  Feb 15, 2007 9:22pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar25698_4.gif) mikhaildgreat](mikhaildgreat)

  * | Joined Nov 2006  | Status: EA Programmer | [298 Posts](/search?do=process&provider=Member&searchuser=25698)

> [Quoting BearPaw](/thread/post/218536#post218536 "View Quoted Post")
> 
> Disliked
> 
> eurgbp entered into a trade just now...but it doesnt look like it should have.  
>    
>  Entered a buy.  
>    
>  Anyone else see that?   
>    
>  BP
> 
> Ignored

thats a valid trade bearpaw. take a look at the MACD, it came up and crossed zero line... I repeat the EA puts equal weight to the signals generated by both the MACD and the MAs, as long as one of them makes a signal and both indicators agree EA will enter a trade.  
  
I don't know if its a profitable trade or not but it a valid one according to the rules.  
  
-Mikhail 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#202](/thread/post/218674#post218674 "Post Permalink")

  * Feb 15, 2007 9:27pm  Feb 15, 2007 9:27pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar25698_4.gif) mikhaildgreat](mikhaildgreat)

  * | Joined Nov 2006  | Status: EA Programmer | [298 Posts](/search?do=process&provider=Member&searchuser=25698)

> [Quoting raven](/thread/post/218585#post218585 "View Quoted Post")
> 
> Disliked
> 
> eurgbp entered into a trade just now...but it doesnt look like it should have.  
>    
>  I had that, i thought it was triggered by the news spike so i manually closed when it was at 0 pips, rather get nothing than lose on a possible retrace.  
>    
>  currently have 2 trades open USD/JPY and USD/CHF both currently losing, but had a GBP/USD winner earlier for 20 pips  
>    
>  running v1.1
> 
> Ignored

I dont have those trades? I only have GBP/USD and EUR/GBP open right now. what timeframe are you using? and what broker?  
  
-Mikhail 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#203](/thread/post/218678#post218678 "Post Permalink")

  * Feb 15, 2007 9:30pm  Feb 15, 2007 9:30pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar25698_4.gif) mikhaildgreat](mikhaildgreat)

  * | Joined Nov 2006  | Status: EA Programmer | [298 Posts](/search?do=process&provider=Member&searchuser=25698)

> [Quoting rogerha](/thread/post/218636#post218636 "View Quoted Post")
> 
> Disliked
> 
> Mikhail,  
>    
>  I didn't enter a recent trade on Cable with the new version. I can only assume looking at my settings that I have made a mistake with the MinCrossDistance parameter which I have set to 1.0 ?  
>    
>  What exactly is that ? Its the only difference to my previous settings with the older EA.  
>    
>  Thanks  
>    
>  Rogerha
> 
> Ignored

The MinCrossDistance is the minimum required distance between the MAs before it is considered a valid cross... mine is set at 5. Im not sure why yours didn't open a trade.. can you please look at the experts tab and see if there are any error reports? and what TF are you using? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#204](/thread/post/218700#post218700 "Post Permalink")

  * Feb 15, 2007 9:51pm  Feb 15, 2007 9:51pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30695_4.gif) toti1972](toti1972)

  * | Joined Jan 2007  | Status: Trader | [107 Posts](/search?do=process&provider=Member&searchuser=30695)

Hi all,  
  
For some reason Pouria V 1-1 didn't trigger the order in GBP/USD that I think it should....  
My settings are MACD filter =true and confirmedonEntry = true. MinCrossDistance=5.  
  
Also last night it entered on EUR/JPY well below the cross at 158.21 and Pouria triggered at 157.90   
Maybe I set something wrong...Anybody else with this scenario?  
  
Thanks. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#205](/thread/post/218725#post218725 "Post Permalink")

  * Feb 15, 2007 10:24pm  Feb 15, 2007 10:24pm 

  * [ rogerha](rogerha)

  * | Joined Aug 2006  | Status: Trader | [273 Posts](/search?do=process&provider=Member&searchuser=15670)

> [Quoting mikhaildgreat](/thread/post/218678#post218678 "View Quoted Post")
> 
> Disliked
> 
> The MinCrossDistance is the minimum required distance between the MAs before it is considered a valid cross... mine is set at 5. Im not sure why yours didn't open a trade.. can you please look at the experts tab and see if there are any error reports? and what TF are you using?
> 
> Ignored

Hi Mikhail,  
  
Since that post, it did open a trade (eventually). Presumably you are specifying no. of pips as the distance, so the MA's would need to be 1 pip apart in my case, and 5 in yours ?  
  
I have checked the experts tab, no errors. Timeframe is M30  
  
I have attached a screenshot for you, I hope that helps, I have placed the cursor over the trade entry candle.  
  
All of my settings are default apart from Alerts, which I have set to false, MinCrossDifference = 1.0, and confirmedonentry=true. 

Attached Image

![](/attachment/image/22558?d=1171545695)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#206](/thread/post/218727#post218727 "Post Permalink")

  * Feb 15, 2007 10:28pm  Feb 15, 2007 10:28pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar25698_4.gif) mikhaildgreat](mikhaildgreat)

  * | Joined Nov 2006  | Status: EA Programmer | [298 Posts](/search?do=process&provider=Member&searchuser=25698)

> [Quoting rogerha](/thread/post/218725#post218725 "View Quoted Post")
> 
> Disliked
> 
> Hi Mikhail,  
>    
>  Since that post, it did open a trade (eventually). Presumably you are specifying no. of pips as the distance, so the MA's would need to be 1 pip apart in my case, and 5 in yours ?  
>    
>  I have checked the experts tab, no errors. Timeframe is M30  
>    
>  I have attached a screenshot for you, I hope that helps, I have placed the cursor over the trade entry candle.  
>    
>  All of my settings are default apart from Alerts, which I have set to false, MinCrossDifference = 1.0, and confirmedonentry=true.
> 
> Ignored

thanks for your reply, mine opened 30mins later than yours. yup you are correct, number of pips distance between MAs.  
  
Thanks again for your reply,  
Mikhail 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#207](/thread/post/218737#post218737 "Post Permalink")

  * Feb 15, 2007 11:24pm  Feb 15, 2007 11:24pm 

  * [ Mobsie](mobsie)

  * | Joined Jan 2007  | Status: Trader | [84 Posts](/search?do=process&provider=Member&searchuser=30399)

Hello,  
  
my trade hit SL.   
  
To open the trade was right, but then prince move very fast against.  
First Lose.  
  
Mobsie 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#208](/thread/post/218754#post218754 "Post Permalink")

  * Feb 15, 2007 11:37pm  Feb 15, 2007 11:37pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar19504_4.gif) 1Sundevil](1sundevil)

  * | Joined Sep 2006  | Status: Trader | [228 Posts](/search?do=process&provider=Member&searchuser=19504)

The only trade that the EA entered in for me was the GBP/USD S @ 9574.  
  
Now, I screwed up last night as I was adjusting the parameters. I upped them to take 2 lots per trade and forgot to adjust the TP level. I had the TP level set at +50 when I wanted to have it permanently at +15.   
  
The trade was entered by the EA and would have hit my TP on two different M30 candles. By the time I woke up I still could have manually closed it for +12 pips, yet I decided to keep it open to see if it would hit +15 again. Well, that was just before 9 am EST and that thing shot negative FAST! Right now it is open for a large loss but hasn't hit my SL of -50 (although it got within 4 pips of it at one point. Right now it's at -22.   
  
Since this is a demo I'm going to let it ride out. *I'm also going to characterize this as a successful trade since the "system" according to the rules was successful, and it was my mistake that made it unsuccessful.  
  
So, I can confidently say that the EA has initiated 7 trades. All successful* for +121 pips and my account (would have) has grown 15.2% now going into day 3. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#209](/thread/post/218761#post218761 "Post Permalink")

  * Feb 15, 2007 11:40pm  Feb 15, 2007 11:40pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30695_4.gif) toti1972](toti1972)

  * | Joined Jan 2007  | Status: Trader | [107 Posts](/search?do=process&provider=Member&searchuser=30695)

hi, this might be a silly question but, in others EA, I always see a tab to set the TF. but in this one I cannot find it...is the TF pre-programmed as per original rules? how can I do to change the TF to try different settings?  
sorry if it is too basic question, but i really couldn't solve...  
thanks 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#210](/thread/post/218765#post218765 "Post Permalink")

  * Feb 15, 2007 11:41pm  Feb 15, 2007 11:41pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar25698_4.gif) mikhaildgreat](mikhaildgreat)

  * | Joined Nov 2006  | Status: EA Programmer | [298 Posts](/search?do=process&provider=Member&searchuser=25698)

> [Quoting 1Sundevil](/thread/post/218754#post218754 "View Quoted Post")
> 
> Disliked
> 
> The only trade that the EA entered in for me was the GBP/USD S @ 9574.  
>    
>  Now, I screwed up last night as I was adjusting the parameters. I upped them to take 2 lots per trade and forgot to adjust the TP level. I had the TP level set at +50 when I wanted to have it permanently at +15.   
>    
>  The trade was entered by the EA and would have hit my TP on two different M30 candles. By the time I woke up I still could have manually closed it for +12 pips, yet I decided to keep it open to see if it would hit +15 again. Well, that was just before 9 am EST and that thing shot negative FAST! Right now it is open for a large loss but hasn't hit my SL of -50 (although it got within 4 pips of it at one point. Right now it's at -22.   
>    
>  Since this is a demo I'm going to let it ride out. *I'm also going to characterize this as a successful trade since the "system" according to the rules was successful, and it was my mistake that made it unsuccessful.  
>    
>  So, I can confidently say that the EA has initiated 7 trades. All successful* for +121 pips and my account (would have) has grown 15.2% now going into day 3.
> 
> Ignored

hi,  
  
are you still using beta3?  
  
-Mikhail 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#211](/thread/post/218769#post218769 "Post Permalink")

  * Feb 15, 2007 11:44pm  Feb 15, 2007 11:44pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar19504_4.gif) 1Sundevil](1sundevil)

  * | Joined Sep 2006  | Status: Trader | [228 Posts](/search?do=process&provider=Member&searchuser=19504)

> [Quoting mikhaildgreat](/thread/post/218765#post218765 "View Quoted Post")
> 
> Disliked
> 
> hi,  
>    
>  are you still using beta3?  
>    
>  -Mikhail
> 
> Ignored

I just saw your post in the other thread (just woke up 45 min ago). I haven't switched over yet but I will. I'm thinking of opening a seperate demo account for the new beta, as beta3 has been doing well so far. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#212](/thread/post/218770#post218770 "Post Permalink")

  * Feb 15, 2007 11:45pm  Feb 15, 2007 11:45pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar25698_4.gif) mikhaildgreat](mikhaildgreat)

  * | Joined Nov 2006  | Status: EA Programmer | [298 Posts](/search?do=process&provider=Member&searchuser=25698)

> [Quoting toti1972](/thread/post/218761#post218761 "View Quoted Post")
> 
> Disliked
> 
> hi, this might be a silly question but, in others EA, I always see a tab to set the TF. but in this one I cannot find it...is the TF pre-programmed as per original rules? how can I do to change the TF to try different settings?  
>  sorry if it is too basic question, but i really couldn't solve...  
>  thanks
> 
> Ignored

just attach the EA to the timeframe you wish to test. the EA timeframe depends on the timeframe of the chart.  
  
-mikhail 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#213](/thread/post/218776#post218776 "Post Permalink")

  * Feb 15, 2007 11:47pm  Feb 15, 2007 11:47pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar25698_4.gif) mikhaildgreat](mikhaildgreat)

  * | Joined Nov 2006  | Status: EA Programmer | [298 Posts](/search?do=process&provider=Member&searchuser=25698)

> [Quoting 1Sundevil](/thread/post/218769#post218769 "View Quoted Post")
> 
> Disliked
> 
> I just saw your post in the other thread (just woke up 45 min ago). I haven't switched over yet but I will. I'm thinking of opening a seperate demo account for the new beta, as beta3 has been doing well so far.
> 
> Ignored

yup thats a good idea. Its good that you continue testing beta 3, for comparison purposes... its good that its profitable, I just hope it continues to be, can't argue with success right.  
  
thanks again,  
  
-Mikhail 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#214](/thread/post/218780#post218780 "Post Permalink")

  * Feb 15, 2007 11:51pm  Feb 15, 2007 11:51pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar19504_4.gif) 1Sundevil](1sundevil)

  * | Joined Sep 2006  | Status: Trader | [228 Posts](/search?do=process&provider=Member&searchuser=19504)

> [Quoting mikhaildgreat](/thread/post/218776#post218776 "View Quoted Post")
> 
> Disliked
> 
> yup thats a good idea. Its good that you continue testing beta 3, for comparison purposes... its good that its profitable, I just hope it continues to be, can't argue with success right.  
>    
>  thanks again,  
>    
>  -Mikhail
> 
> Ignored

I'm hoping it continues to be profitable as well. The trade I'm in is back down to -15 (was at -7 a min ago). We'll see if my mistake desn't count against me. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#215](/thread/post/218785#post218785 "Post Permalink")

  * Feb 15, 2007 11:57pm  Feb 15, 2007 11:57pm 

  * [ BearPaw](bearpaw)

  * | Joined Jul 2006  | Status: A Trader for Life | [218 Posts](/search?do=process&provider=Member&searchuser=13999)

These are results with Beta 3. From 8am Wednesday EST to 930am Thursday EST....  
  
Eurjpy----- sell ----157.92----- +15  
audjpy----- sell---- 94.08------ +15  
chfjpy----- sell----- 96.95 ------+15  
eurchf------sell----1.6243------- (-22) (tried to account for spread)  
gbpusd-----sell----1.9560-------(-20)  
gbpusd-----sell----1.9577-------(-20)  
eurgbp-----buy----.6707-------- +10   
  
Net profit/loss = -7  
Total for this week so far 31 pip profit.  
  
I am trading all pairs that forexpert recommended except the CADJPY.  
  
So, generally I have used 20 pip SL and Original TPs that Forexpert prescribed.  
  
I do not have the same results as Sundevil...and I need to figure out if it is the SL issue or not.  
  
Please let me know if any others find anything else to help in profitable trades.  
  
BP 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#216](/thread/post/218794#post218794 "Post Permalink")

  * Feb 16, 2007 12:05am  Feb 16, 2007 12:05am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar19504_4.gif) 1Sundevil](1sundevil)

  * | Joined Sep 2006  | Status: Trader | [228 Posts](/search?do=process&provider=Member&searchuser=19504)

> [Quoting BearPaw](/thread/post/218785#post218785 "View Quoted Post")
> 
> Disliked
> 
> These are results with Beta 3. From 8am Wednesday EST to 930am Thursday EST....  
>    
>  Eurjpy----- sell ----157.92----- +15  
>  audjpy----- sell---- 94.08------ +15  
>  chfjpy----- sell----- 96.95 ------+15  
>  eurchf------sell----1.6243------- (-22) (tried to account for spread)  
>  gbpusd-----sell----1.9560-------(-20)  
>  gbpusd-----sell----1.9577-------(-20)  
>  eurgbp-----buy----.6707-------- +4 (closed early cause of news)  
>    
>  Net profit/loss = -13  
>  Total for this week so far 25 pip profit.  
>    
>  I am trading all pairs that forexpert recommended except the CADJPY.  
>    
>  So, generally I have used 20 pip SL and Original TPs that Forexpert prescribed.  
>    
>  I do not have the same results as Sundevil...and I need to figure out if it is the SL issue or not.  
>    
>  Please let me know if any others find anything else to help in profitable trades.  
>    
>  BP
> 
> Ignored

I'm currently not using four of your currency pairs: audjpy, chfjpy, eurgbp and eurchf.  
  
I'm not sure if it's a SL issue per se, as I was never in danger of hitting one until this last trade, which has now gone positive again BTW (we'll see if it hits my +15 TP).  
  
I didn't watch for news reports either, which I should have.   
  
Also, the only GBP/USD trades that the EA has entered for me were "BUY's" @ 9453 and 9477. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#217](/thread/post/218796#post218796 "Post Permalink")

  * Feb 16, 2007 12:09am  Feb 16, 2007 12:09am 

  * [ BearPaw](bearpaw)

  * | Joined Jul 2006  | Status: A Trader for Life | [218 Posts](/search?do=process&provider=Member&searchuser=13999)

I wonder how your ea is different from mine? We are both using Beta 3. I have only changed the settings for the following items..  
  
TP - as designated by originator  
Lot size...  
MM-false  
microlots-true  
  
That is all I have done to tweak it....what time frame do or did you have your gbpusd in? That might make a difference.  
  
I was having trouble with audjpy and then forexpert told me to change the time frame to 1 hour and it has produced 2 positive trades since then.  
  
BP 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#218](/thread/post/218799#post218799 "Post Permalink")

  * Feb 16, 2007 12:17am  Feb 16, 2007 12:17am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar19504_4.gif) 1Sundevil](1sundevil)

  * | Joined Sep 2006  | Status: Trader | [228 Posts](/search?do=process&provider=Member&searchuser=19504)

> [Quoting BearPaw](/thread/post/218796#post218796 "View Quoted Post")
> 
> Disliked
> 
> I wonder how your ea is different from mine? We are both using Beta 3. I have only changed the settings for the following items..  
>    
>  TP - as designated by originator  
>  Lot size...  
>  MM-false  
>  microlots-true  
>    
>  That is all I have done to tweak it....what time frame do or did you have your gbpusd in? That might make a difference.  
>    
>  I was having trouble with audjpy and then forexpert told me to change the time frame to 1 hour and it has produced 2 positive trades since then.  
>    
>  BP
> 
> Ignored

My settings are the same as yours.  
  
I just closed that "bad" trade for +5 pips.  
  
updated totals are 7 trades, all positive, for **+111** pips. My account has grown from $5,100 to $5,676, an increase of **_11.3%_**.  
  
I was close t o hitting my -50 SL (4 pips away), but luckily it came back. Had I not messed up the parameters it would have hit my +15 TP within 20 min after opening. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#219](/thread/post/218801#post218801 "Post Permalink")

  * Feb 16, 2007 12:19am  Feb 16, 2007 12:19am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar19504_4.gif) 1Sundevil](1sundevil)

  * | Joined Sep 2006  | Status: Trader | [228 Posts](/search?do=process&provider=Member&searchuser=19504)

LOL! Had I waited 3 more min. it would have hit my +15 TP anyway. Just goes to show that I should allow the EA to do what it does. When I mess with it I only screw things up! DAMN! ![](https://resources.faireconomy.media/images/emojis/64/1f647-200d-2642-fe0f.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#220](/thread/post/218813#post218813 "Post Permalink")

  * Feb 16, 2007 12:23am  Feb 16, 2007 12:23am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30695_4.gif) toti1972](toti1972)

  * | Joined Jan 2007  | Status: Trader | [107 Posts](/search?do=process&provider=Member&searchuser=30695)

> [Quoting mikhaildgreat](/thread/post/218770#post218770 "View Quoted Post")
> 
> Disliked
> 
> just attach the EA to the timeframe you wish to test. the EA timeframe depends on the timeframe of the chart.  
>    
>  -mikhail
> 
> Ignored

The problem is that the EA icon shows in all timeframes, not just the one I attached to. does the EA work with the TF I am watching at any specific time?   
so I understand if I want to try a different TF all I need to do is to switch the chart and the EA start working on the new one since it appears already attached. Am I correct?  
  
Thanks 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * The Pouria EA Development Thread
  *   * [ **Reply to Thread** ](/thread/17242-the-pouria-ea-development-thread/reply#reply)

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

[The Pouria Method](/thread/17011-the-pouria-method "OKay here is one of the 4 best systems that I've made and used, with this system I pickup atleast 50 pips a day, I'm sharing this because...") 562 replies

[Lessons Learned during System Development](/thread/2986-lessons-learned-during-system-development "Hi, 
  
I've been reading through the forum and somehow I'm in the process of developing my own system.. But not really doing actual...") 29 replies

[(pouria method II on the test)](/thread/23104-pouria-method-ii-on-the-test "Hello  
pouria method II is now DONE thanks to the group of experts and mathematicians that helped and made this method. 
now we are...") 218 replies

[System Development Secrets](/thread/7342-system-development-secrets "&lt;meta http-equiv=&quot;CONTENT-TYPE&quot; content=&quot;text/html; charset=utf-8&quot;&gt;&lt;title&gt;&lt;/title&gt;&lt;meta name=&quot;GENERATOR&quot; content=&quot;OpenOffice.org 2.0 ...") 5 replies

[Metatrader 4 Development Course](/thread/5906-metatrader-4-development-course "Here is the Mql_4_Metatrader_4_Development_Course in pdf \(link fixed\) : 
 
http://www.freefilehosting.org/pupload/view/8711") 3 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/17242-the-pouria-ea-development-thread/reply#reply)
  * Subscribe
  * [45](javascript:void\(0\);)

Attachments: The Pouria EA Development Thread

Tags: The Pouria EA Development Thread

#  [](/thread/17242-the-pouria-ea-development-thread)The Pouria EA Development Thread 

  * 

  * [#221](/thread/post/218840#post218840 "Post Permalink")

  * Feb 16, 2007 12:41am  Feb 16, 2007 12:41am 

  * [ BearPaw](bearpaw)

  * | Joined Jul 2006  | Status: A Trader for Life | [218 Posts](/search?do=process&provider=Member&searchuser=13999)

> [Quoting toti1972](/thread/post/218813#post218813 "View Quoted Post")
> 
> Disliked
> 
> The problem is that the EA icon shows in all timeframes, not just the one I attached to. does the EA work with the TF I am watching at any specific time?   
>  so I understand if I want to try a different TF all I need to do is to switch the chart and the EA start working on the new one since it appears already attached. Am I correct?  
>    
>  Thanks
> 
> Ignored

If you have the ea in a current time frame...lets say 1 hour, and then change that time frame to 30 min..or whatever...the ea will stay attached and work in it.  
  
You would have to open up a completely different chart if you wanted it to work without the ea.  
  
BP 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#222](/thread/post/218850#post218850 "Post Permalink")

  * Feb 16, 2007 12:48am  Feb 16, 2007 12:48am 

  * [ BearPaw](bearpaw)

  * | Joined Jul 2006  | Status: A Trader for Life | [218 Posts](/search?do=process&provider=Member&searchuser=13999)

> [Quoting 1Sundevil](/thread/post/218799#post218799 "View Quoted Post")
> 
> Disliked
> 
> My settings are the same as yours.  
>    
>  I just closed that "bad" trade for +5 pips.  
>    
>  updated totals are 7 trades, all positive, for **+111** pips. My account has grown from $5,100 to $5,676, an increase of **_11.3%_**.  
>    
>  I was close t o hitting my -50 SL (4 pips away), but luckily it came back. Had I not messed up the parameters it would have hit my +15 TP within 20 min after opening.
> 
> Ignored

Sundevil,  
  
I do not understand how our settings are the same. Over the last 24 hours, the only trade that Beta 3 put me in that had the GBPUSD were 2 shorts. They both got stopped out. Your trade sounds like it is a long with the GBPUSD. I have not had that trade for 24 hours...so that is why I am puzzled.   
  
Please let me know if it was not a long....and if anyone else has the same results as me or sundevil, please post.  
  
Thanks,  
  
BP 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#223](/thread/post/218911#post218911 "Post Permalink")

  * Feb 16, 2007 1:24am  Feb 16, 2007 1:24am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar19504_4.gif) 1Sundevil](1sundevil)

  * | Joined Sep 2006  | Status: Trader | [228 Posts](/search?do=process&provider=Member&searchuser=19504)

> [Quoting BearPaw](/thread/post/218850#post218850 "View Quoted Post")
> 
> Disliked
> 
> Sundevil,  
>    
>  I do not understand how our settings are the same. Over the last 24 hours, the only trade that Beta 3 put me in that had the GBPUSD were 2 shorts. They both got stopped out. Your trade sounds like it is a long with the GBPUSD. I have not had that trade for 24 hours...so that is why I am puzzled.   
>    
>  Please let me know if it was not a long....and if anyone else has the same results as me or sundevil, please post.  
>    
>  Thanks,  
>    
>  BP
> 
> Ignored

My last GBP/USD (+5) was a sell @ 9574, TP @ 9559 and SL @ 9624. I manually closed it @ 9569 for +5. It came close to my SL before heading back down again in my direction. Had I been more patient it would have hit my TP yet again.  
  
One thing I was thinking. I believe that the EA is set up to only take a % of available margin. If you are in multiple trades you may miss out on some because of margin. Does that sound right? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#224](/thread/post/218925#post218925 "Post Permalink")

  * Feb 16, 2007 1:31am  Feb 16, 2007 1:31am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar25698_4.gif) mikhaildgreat](mikhaildgreat)

  * | Joined Nov 2006  | Status: EA Programmer | [298 Posts](/search?do=process&provider=Member&searchuser=25698)

> [Quoting 1Sundevil](/thread/post/218911#post218911 "View Quoted Post")
> 
> Disliked
> 
> My last GBP/USD (+5) was a sell @ 9574, TP @ 9559 and SL @ 9624. I manually closed it @ 9569 for +5. It came close to my SL before heading back down again in my direction. Had I been more patient it would have hit my TP yet again.  
>    
>  One thing I was thinking. I believe that the EA is set up to only take a % of available margin. If you are in multiple trades you may miss out on some because of margin. Does that sound right?
> 
> Ignored

yup thats right. if you want to be more aggressive you can change the code. just replace the _**AccountFreeMargin()**_ in the MM function of the code to _**AccountBalance()**_ or _**AccountEquity()  
  
**_-Mikhail 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#225](/thread/post/218950#post218950 "Post Permalink")

  * Feb 16, 2007 1:41am  Feb 16, 2007 1:41am 

  * [ BearPaw](bearpaw)

  * | Joined Jul 2006  | Status: A Trader for Life | [218 Posts](/search?do=process&provider=Member&searchuser=13999)

> [Quoting 1Sundevil](/thread/post/218911#post218911 "View Quoted Post")
> 
> Disliked
> 
> My last GBP/USD (+5) was a sell @ 9574, TP @ 9559 and SL @ 9624. I manually closed it @ 9569 for +5. It came close to my SL before heading back down again in my direction. Had I been more patient it would have hit my TP yet again.  
>    
>  One thing I was thinking. I believe that the EA is set up to only take a % of available margin. If you are in multiple trades you may miss out on some because of margin. Does that sound right?
> 
> Ignored

Ok...so it was a sell....that helps me....I had two sells...one at 9560 and one at 9577....so that was probably it. Mine were stopped out...yours were not.  
  
Good..thank makes sense to me...I was hitting my head on the wall trying to figure it out!! ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
  
So, I wonder if the higher stop loss is a good thing to do?  
  
BP 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#226](/thread/post/218967#post218967 "Post Permalink")

  * Feb 16, 2007 1:56am  Feb 16, 2007 1:56am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar18503_10.gif) Se[V]eN](member.php?u=18503)

  * | Joined Sep 2006  | Status: Im A Lucky Hyena | [449 Posts](/search?do=process&provider=Member&searchuser=18503)

hello all...  
  
  
i doesnt mean to be rude but i got a couples of opinion here..  
what i most like bout this thread is the philosophy of the originator...  
to take small pips at one time...  
thats need a lot of patience...  
my strategy is get 10 pips every trade without waiting for long...  
this method seems to fail to catch a movement in instant(i mean before sentiment are faden off the market)....  
so im about to combine MR forexexpert philosophy with sidus method(which im not testing yet)...  
i hope my post doesnt hurt anyone and i wanna thanks to MR forexexpert for his great piece of pholosophy...  
see u all then...  

"Analysis Is Hard But Trade Is Easy"![](https://resources.faireconomy.media/images/emojis/64/1f644.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#227](/thread/post/218980#post218980 "Post Permalink")

  * Feb 16, 2007 2:04am  Feb 16, 2007 2:04am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar19504_4.gif) 1Sundevil](1sundevil)

  * | Joined Sep 2006  | Status: Trader | [228 Posts](/search?do=process&provider=Member&searchuser=19504)

> [Quoting BearPaw](/thread/post/218950#post218950 "View Quoted Post")
> 
> Disliked
> 
> So, I wonder if the higher stop loss is a good thing to do?  
>  BP
> 
> Ignored

Well, if I had my TP set at +15, like I had intended when I upped the lots to 2.0, it would have never gone negative before hitting the TP.  
  
Since I still had the TP set at +50, it almost hit my SL at -50.  
  
The way I look at it now is that with the EA taking 2 lots it's like getting a 4 for 1 for every pip. Thus +15 in reality is like +60, if you're using 2.0 lots. Of course this changes the whole idea of the 5% rule for MM. But I'm ok with that so long as this system can continue to hit +15 or +20 consistently. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#228](/thread/post/219226#post219226 "Post Permalink")

  * Feb 16, 2007 6:22am  Feb 16, 2007 6:22am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar32091_6.gif) Spudfyre](spudfyre)

  * Joined Jan 2007 | Status: MTF Stochastics and Volume/Price | [1,133 Posts](/search?do=process&provider=Member&searchuser=32091)

I've back tested these to be the "best" settings for EURUSD. Criteria for "best" is limiting the number of bad trades so that all trades can be at the same size lot.  
  
  
M30 Timeframe  
T/P = 15 pips (+3 pip spread) = 18 pips  
Spread = 3 Pips  
Stop = 21 pips (+3 pip spread) = 24 pips  
Minimum 5 MA Cross = 11 pips  
  
If someone else could run these numbers and confirm results or share better settings? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#229](/thread/post/219233#post219233 "Post Permalink")

  * Feb 16, 2007 6:25am  Feb 16, 2007 6:25am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar25698_4.gif) mikhaildgreat](mikhaildgreat)

  * | Joined Nov 2006  | Status: EA Programmer | [298 Posts](/search?do=process&provider=Member&searchuser=25698)

hi,  
  
what version are you using? are these the optimized settings from strategy tester?  
  
-Mikhail  

> [Quoting Spudfyre](/thread/post/219226#post219226 "View Quoted Post")
> 
> Disliked
> 
> I've back tested these to be the "best" settings for EURUSD. Criteria for "best" is limiting the number of bad trades so that all trades can be at the same size lot.  
>    
>    
>  M30 Timeframe  
>  T/P = 15 pips (+3 pip spread) = 18 pips  
>  Spread = 3 Pips  
>  Stop = 21 pips (+3 pip spread) = 24 pips  
>  Minimum 5 MA Cross = 11 pips  
>    
>  If someone else could run these numbers and confirm results or share better settings?
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#230](/thread/post/219302#post219302 "Post Permalink")

  * Feb 16, 2007 7:42am  Feb 16, 2007 7:42am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar25698_4.gif) mikhaildgreat](mikhaildgreat)

  * | Joined Nov 2006  | Status: EA Programmer | [298 Posts](/search?do=process&provider=Member&searchuser=25698)

> [Quoting Se[V]eN](/thread/post/218967#post218967 "View Quoted Post")
> 
> Disliked
> 
> hello all...  
>    
>    
>  i doesnt mean to be rude but i got a couples of opinion here..  
>  what i most like bout this thread is the philosophy of the originator...  
>  to take small pips at one time...  
>  thats need a lot of patience...  
>  my strategy is get 10 pips every trade without waiting for long...  
>  this method seems to fail to catch a movement in instant(i mean before sentiment are faden off the market)....  
>  so im about to combine MR forexexpert philosophy with sidus method(which im not testing yet)...  
>  i hope my post doesnt hurt anyone and i wanna thanks to MR forexexpert for his great piece of pholosophy...  
>  see u all then...  
> 
> 
> Ignored

Hi,  
  
Thanks for your post. your post actually got me thinking because you are right, The EA right now is not to efficient is scalping. we usually see a pullback before price goes to the favorable direction of our trade. that is why some have found better luck with putting higher stoploss, but this also means higher risk... So with that in mind the best entry should not be on the cross but instead on the pullback of the already established trend.   
  
Im thinking of using RSI or stochastic as a trigger to get us in the pullback, this way we can enter those long trends everytime it retrace, unlike right now where we are just waiting for the cross when the market is clearly trending...  
  
I will have to eyeball the chart to find the best indicator... if you guys have can suggest a good indicator that would get us in the trade during pullbacks of trends pls don't hesitate to post.  
  
Regards,  
Mikhail 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#231](/thread/post/219347#post219347 "Post Permalink")

  * Feb 16, 2007 8:39am  Feb 16, 2007 8:39am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar28980_4.gif) anthonyrae](anthonyrae)

  * | Joined Dec 2006  | Status: Trader | [68 Posts](/search?do=process&provider=Member&searchuser=28980)

> [Quoting mikhaildgreat](/thread/post/219302#post219302 "View Quoted Post")
> 
> Disliked
> 
> Hi,  
>    
>  Thanks for your post. your post actually got me thinking because you are right, The EA right now is not to efficient is scalping. we usually see a pullback before price goes to the favorable direction of our trade. that is why some have found better luck with putting higher stoploss, but this also means higher risk... So with that in mind the best entry should not be on the cross but instead on the pullback of the already established trend.   
>    
>  Im thinking of using RSI or stochastic as a trigger to get us in the pullback, this way we can enter those long trends everytime it retrace, unlike right now where we are just waiting for the cross when the market is clearly trending...  
>    
>  I will have to eyeball the chart to find the best indicator... if you guys have can suggest a good indicator that would get us in the trade during pullbacks of trends pls don't hesitate to post.  
>    
>  Regards,  
>  Mikhail
> 
> Ignored

Mikhail, I think that is a great idea, because sometimes if you miss out on the longer term trend which may well go for 100 + pips, (just look at recent USD/JPY move).. so if you can enter a trade on the pullback to catch this trend, that would be fantastic, but I don't have any ideas at the moment on how to do this... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#232](/thread/post/219417#post219417 "Post Permalink")

  * Edited 10:51am  Feb 16, 2007 10:35am | Edited 10:51am 

  * [ Forex1man](forex1man)

  * | Joined Oct 2006  | Status: Trader | [58 Posts](/search?do=process&provider=Member&searchuser=21229)

Pullbacks are my main method of trading. I use stochiastics for the timing. There is a thread here called bringin sexy back - stochastics by boxingis life. He basically uses four differnent periods of stoch all in one indicator with the shorest period being the signal ones and the rest showing trade direction. It got me in the this GBP/USD short trade on the 4th 15 min bar after the major pullback bar so I am short after the pullback 1.9560 for the long haul. Looking for pullbacks entrances I drop down a timeframe.I still took 15 pips heat on trade before getting up over 50 pips while ago. At this point you still need MM for the trade. But never need to risk over 20 pips for the pullback. I have been trading like this for sometime way before this thread and even the other thread. Only thing the stochiastic thread gave me the best thing so far I found for pullbackks. I am sure that it could be coded also, although I am not a programmer. I get paid to trade is my moto. This method has been working extremely well for me combined with this thread. If this muddy's up the water here, please forget all this my only intention was to give my 2 cents. I also have some other great software I pay money for that I like and use for pullbacks. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#233](/thread/post/219440#post219440 "Post Permalink")

  * Edited 11:35am  Feb 16, 2007 11:34am | Edited 11:35am 

  * [ 1trader2](1trader2)

  * | Joined Mar 2006  | Status: Trader | [110 Posts](/search?do=process&provider=Member&searchuser=7147)

Mikhail, et al.  
  
I have been looking at the visual mode of Strategy tester backtesting the EA with the EURUSD pair and have observed some things which seem obvious to me. If I am wrong about this, please let me know. The observations/suggestions are as follows:

  1. Once a trade is entered… if MACD continues to increase positive or negative by a certain amount or percentage, scale in a 2nd or 3rd trade in the same size lot or by increased amounts, such as Martingale doubling. This could also be done to scale out of the trade as the MACD reverses from your entries. This might ensure that we capture more profit on the trending crosses.
  2. There would have to be a drop dead point of reversal to get out of the trade(s) when the MACD reverses by a (x) amount.
  3. Another alternative, but probably not as good as MACD would be to measure the MA separation distance (MinCrossDistance) between the 75 or 85 MA’s and the 5 MA and when it reaches (x) pips enter positions as above.
  4. From my observation based on the visual mode of the Strategy Backtester, a more obvious way to exit is to stay in the trade until the value of the MACD begins to reverse or has a reversal over (x) number of periods, rather than with a fixed TP. If it is over a (x) number of periods this allows for some minor retracement. Or what you could do is take the first TP whatever it may be set to and then (re)enter increased positions based on the parameters of #1 or #3 above and then exit as suggested.

Mikhail. could you program some options like this into the EA and I would be more than happy to test it. This looks like a great system and with continued tweaking will reap the pips, I believe.  
  
1Trader2 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#234](/thread/post/219521#post219521 "Post Permalink")

  * Feb 16, 2007 1:31pm  Feb 16, 2007 1:31pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar25698_4.gif) mikhaildgreat](mikhaildgreat)

  * | Joined Nov 2006  | Status: EA Programmer | [298 Posts](/search?do=process&provider=Member&searchuser=25698)

> [Quoting Forex1man](/thread/post/219417#post219417 "View Quoted Post")
> 
> Disliked
> 
> Pullbacks are my main method of trading. I use stochiastics for the timing. There is a thread here called bringin sexy back - stochastics by boxingis life. He basically uses four differnent periods of stoch all in one indicator with the shorest period being the signal ones and the rest showing trade direction. It got me in the this GBP/USD short trade on the 4th 15 min bar after the major pullback bar so I am short after the pullback 1.9560 for the long haul. Looking for pullbacks entrances I drop down a timeframe.I still took 15 pips heat on trade before getting up over 50 pips while ago. At this point you still need MM for the trade. But never need to risk over 20 pips for the pullback. I have been trading like this for sometime way before this thread and even the other thread. Only thing the stochiastic thread gave me the best thing so far I found for pullbackks. I am sure that it could be coded also, although I am not a programmer. I get paid to trade is my moto. This method has been working extremely well for me combined with this thread. If this muddy's up the water here, please forget all this my only intention was to give my 2 cents. I also have some other great software I pay money for that I like and use for pullbacks.
> 
> Ignored

yes Ive looked in that thread and its very good, bringing sexy back is one of those strategies that is very difficult to automate because it involves alot on traders discretion but the strategy is very good. That thread is also what got me thinking about trading the retracement.   
  
Yes, I believe signals from MAs at a lower timeframe or stochastics might just do the trick. But if you think of something that my work don't hesitate to post.  
  
thanks for the great post,  
Mikhail 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#235](/thread/post/219527#post219527 "Post Permalink")

  * Feb 16, 2007 1:40pm  Feb 16, 2007 1:40pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar25698_4.gif) mikhaildgreat](mikhaildgreat)

  * | Joined Nov 2006  | Status: EA Programmer | [298 Posts](/search?do=process&provider=Member&searchuser=25698)

> [Quoting 1trader2](/thread/post/219440#post219440 "View Quoted Post")
> 
> Disliked
> 
> Mikhail, et al.
> 
>   1. There would have to be a drop dead point of reversal to get out of the trade(s) when the MACD reverses by a (x) amount.
> 

> 
> 1Trader2
> 
> Ignored

Hi good suggestions, but what do you mean when you say "MACD reverses"? does it have to cross the zero line for it to be considered a reversal? or are we simply looking at MACD slope?   
  
the way I understand it is that you are simply looking at the value of the MACD and when it starts to drop(during a buy bosition for example) you consider it a reversal? is that correct? this requires some sort of trailing stop based on the MACD value alone...   
  
Thank you for your suggestion can you please elaborate more on this?  
  
regards,  
Mikhail 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#236](/thread/post/219638#post219638 "Post Permalink")

  * Feb 16, 2007 5:32pm  Feb 16, 2007 5:32pm 

  * [ Forex1man](forex1man)

  * | Joined Oct 2006  | Status: Trader | [58 Posts](/search?do=process&provider=Member&searchuser=21229)

See my post #232 7 hrs ago and now up 80 pips on this trade. It has had 4 pullbacks since it started, you are spending all your time trying to optimize the holygrail of a trading plan that will never happen. This methods is a great concept for finding long term trades of 40 -100 pips. You will never make money trading forex by taking 10 and 20 pip profits. Trade1-2 pairs learn them,how they work with this concept and find you a money management that works for your style and use a pullback concept and you will be on the road to being an expert forex trader. Good luck..... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#237](/thread/post/219653#post219653 "Post Permalink")

  * Feb 16, 2007 6:00pm  Feb 16, 2007 6:00pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar25698_4.gif) mikhaildgreat](mikhaildgreat)

  * | Joined Nov 2006  | Status: EA Programmer | [298 Posts](/search?do=process&provider=Member&searchuser=25698)

> [Quoting Forex1man](/thread/post/219638#post219638 "View Quoted Post")
> 
> Disliked
> 
> See my post #232 7 hrs ago and now up 80 pips on this trade. It has had 4 pullbacks since it started, you are spending all your time trying to optimize the holygrail of a trading plan that will never happen. This methods is a great concept for finding long term trades of 40 -100 pips. You will never make money trading forex by taking 10 and 20 pip profits. Trade1-2 pairs learn them,how they work with this concept and find you a money management that works for your style and use a pullback concept and you will be on the road to being an expert forex trader. Good luck.....
> 
> Ignored

LOL. good for you my friend i completely agree. Im planing to make a new EA sexy pauria, pouria MAs and MACD to identify the trend then use stochastic 5,3,3 as my trigger. I got a question though, what timeframe are you using for "sexy back" and do you exit only when the stochs cross again?  
  
thanks,  
Mikhail 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#238](/thread/post/219815#post219815 "Post Permalink")

  * Feb 16, 2007 10:01pm  Feb 16, 2007 10:01pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30695_4.gif) toti1972](toti1972)

  * | Joined Jan 2007  | Status: Trader | [107 Posts](/search?do=process&provider=Member&searchuser=30695)

good morning to all,  
  
This was not a valid entry...If it had been an buy, we could say it was too early and still unconfirmed...but the worst thing is that it was actually a "SELL" , not even close...  
Anybody else got this one?  
thanks 

Attached Image

![](/attachment/image/22644?d=1171630469)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#239](/thread/post/219875#post219875 "Post Permalink")

  * Feb 16, 2007 11:01pm  Feb 16, 2007 11:01pm 

  * [ rogerha](rogerha)

  * | Joined Aug 2006  | Status: Trader | [273 Posts](/search?do=process&provider=Member&searchuser=15670)

> [Quoting toti1972](/thread/post/219815#post219815 "View Quoted Post")
> 
> Disliked
> 
> good morning to all,  
>    
>  This was not a valid entry...If it had been an buy, we could say it was too early and still unconfirmed...but the worst thing is that it was actually a "SELL" , not even close...  
>  Anybody else got this one?  
>  thanks
> 
> Ignored

Actually looking a little closely (speculating without the actual data), did the 5MA briefly go above the lower of the two longer term MA's and then back below it again ? Then if it did, that would be valid. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#240](/thread/post/219878#post219878 "Post Permalink")

  * Feb 16, 2007 11:02pm  Feb 16, 2007 11:02pm 

  * [ 1trader2](1trader2)

  * | Joined Mar 2006  | Status: Trader | [110 Posts](/search?do=process&provider=Member&searchuser=7147)

> [Quoting mikhaildgreat](/thread/post/219527#post219527 "View Quoted Post")
> 
> Disliked
> 
> Hi good suggestions, but what do you mean when you say "MACD reverses"? does it have to cross the zero line for it to be considered a reversal? or are we simply looking at MACD slope?   
>    
>  the way I understand it is that you are simply looking at the value of the MACD and when it starts to drop(during a buy bosition for example) you consider it a reversal? is that correct? this requires some sort of trailing stop based on the MACD value alone...   
>    
>  Thank you for your suggestion can you please elaborate more on this?  
>    
>  regards,  
>  Mikhail
> 
> Ignored

Mikhail,  
  
Sorry about the confusion. By reversal, I am talking about the change in MACD slope. If the bar has a change in slope from its present trend, lets say increasing and the next bar is decreasing, this would signal an exit. You could let it change over more than one MACD bar. For example, let's say the trend is up over the last 7 histogram bars, and then it decreases the next bar, and then increases or stays the same over the next two bars...stay in the trade. Let's say that it has continuously increased over, six bars, and then decreases over two bars, exit the trade. You could also look at how far it decreased or increased from the previous, either as points or as a percentage of the previous bar(s), to determine how rapidly it is changing and then base an exit strategy on that. I hope that this makes this clearer. It is helpful to run Strategy Tester in visual mode to see how the MACD Histogram bars change in relation to price and MA movement to get a sense of how they relate to each other and the trend. Hope this helps.  
  
1Trader2 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * The Pouria EA Development Thread
  *   * [ **Reply to Thread** ](/thread/17242-the-pouria-ea-development-thread/reply#reply)

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

[The Pouria Method](/thread/17011-the-pouria-method "OKay here is one of the 4 best systems that I've made and used, with this system I pickup atleast 50 pips a day, I'm sharing this because...") 562 replies

[Lessons Learned during System Development](/thread/2986-lessons-learned-during-system-development "Hi, 
  
I've been reading through the forum and somehow I'm in the process of developing my own system.. But not really doing actual...") 29 replies

[(pouria method II on the test)](/thread/23104-pouria-method-ii-on-the-test "Hello  
pouria method II is now DONE thanks to the group of experts and mathematicians that helped and made this method. 
now we are...") 218 replies

[System Development Secrets](/thread/7342-system-development-secrets "&lt;meta http-equiv=&quot;CONTENT-TYPE&quot; content=&quot;text/html; charset=utf-8&quot;&gt;&lt;title&gt;&lt;/title&gt;&lt;meta name=&quot;GENERATOR&quot; content=&quot;OpenOffice.org 2.0 ...") 5 replies

[Metatrader 4 Development Course](/thread/5906-metatrader-4-development-course "Here is the Mql_4_Metatrader_4_Development_Course in pdf \(link fixed\) : 
 
http://www.freefilehosting.org/pupload/view/8711") 3 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/17242-the-pouria-ea-development-thread/reply#reply)
  * Subscribe
  * [45](javascript:void\(0\);)

Attachments: The Pouria EA Development Thread

Tags: The Pouria EA Development Thread

#  [](/thread/17242-the-pouria-ea-development-thread)The Pouria EA Development Thread 

  * 

  * [#241](/thread/post/219908#post219908 "Post Permalink")

  * Feb 16, 2007 11:22pm  Feb 16, 2007 11:22pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar19504_4.gif) 1Sundevil](1sundevil)

  * | Joined Sep 2006  | Status: Trader | [228 Posts](/search?do=process&provider=Member&searchuser=19504)

> [Quoting toti1972](/thread/post/219815#post219815 "View Quoted Post")
> 
> Disliked
> 
> good morning to all,  
>    
>  This was not a valid entry...If it had been an buy, we could say it was too early and still unconfirmed...but the worst thing is that it was actually a "SELL" , not even close...  
>  Anybody else got this one?  
>  thanks
> 
> Ignored

What price did the EA drop you in a sell on? It looks like it was 2350. What's funny is that, the way I have my parameters set up, you would have almost reached your TP level when it hit 2335.   
  
But you're right, it was a strange entry point. Which beta version are you using? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#242](/thread/post/219980#post219980 "Post Permalink")

  * Feb 17, 2007 12:08am  Feb 17, 2007 12:08am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30695_4.gif) toti1972](toti1972)

  * | Joined Jan 2007  | Status: Trader | [107 Posts](/search?do=process&provider=Member&searchuser=30695)

Hi Sundevil,  
  
The order was: Sell 1.2349 and was not able to catch pullback to 1.2335 because hit SL @ 1.2369, almost immediatly. In addition, two candles after the order, we got a valid entry to "buy" which for me would represents the S/L and a reversal entry for this order.   
What becomes weird is that is was an undoubtedly approach to a "buy" signal, 5 MA was heading north to cross, and MACD is in the same path ready to confirm the trade. I see not even a chance to interpret this scenario in a different way.   
I cannot understand what could have made the program to trigger this order. btw I am using Pouria V-1.1  
  
thanks 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#243](/thread/post/219984#post219984 "Post Permalink")

  * Feb 17, 2007 12:10am  Feb 17, 2007 12:10am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar19504_4.gif) 1Sundevil](1sundevil)

  * | Joined Sep 2006  | Status: Trader | [228 Posts](/search?do=process&provider=Member&searchuser=19504)

> [Quoting toti1972](/thread/post/219980#post219980 "View Quoted Post")
> 
> Disliked
> 
> Hi Sundevil,  
>    
>  The order was: Sell 1.2349 and was not able to catch pullback to 1.2335 because hit SL @ 1.2369, almost immediatly. In addition, two candles after the order, we got a valid entry to "buy" which for me would represents the S/L and a reversal entry for this order.   
>  What becomes weird is that is was an undoubtedly approach to a "buy" signal, 5 MA was heading north to cross, and MACD is in the same path ready to confirm the trade. I see not even a chance to interpret this scenario in a different way.   
>  I cannot understand what could have made the program to trigger this order. btw I am using Pouria V-1.1  
>    
>  thanks
> 
> Ignored

Ahh, a couple of things. I have my SL set at -50 and have yet to have a bad trade. Obviously this is risky. Also, I'm using version beta3 and I know that there is now a version beta4. You may want to upgrade as the trade may have been triggered by a "bug" that he has now fixed. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#244](/thread/post/219987#post219987 "Post Permalink")

  * Feb 17, 2007 12:13am  Feb 17, 2007 12:13am 

  * [ BearPaw](bearpaw)

  * | Joined Jul 2006  | Status: A Trader for Life | [218 Posts](/search?do=process&provider=Member&searchuser=13999)

Hey guys,  
  
From the balance, Day 5 was a loser...I think this week I barely came above BE.  
  
But I need to look at it and post it later. Please look at this thread over the weekend and make comments.  
  
I am thinking that a higher SL is needed...but not sure.  
  
I will not be able to post what I see until tomorrow morning..but will do so...I am traveling all day today.  
  
Thanks,  
  
BP 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#245](/thread/post/220021#post220021 "Post Permalink")

  * Feb 17, 2007 12:32am  Feb 17, 2007 12:32am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30695_4.gif) toti1972](toti1972)

  * | Joined Jan 2007  | Status: Trader | [107 Posts](/search?do=process&provider=Member&searchuser=30695)

> [Quoting 1Sundevil](/thread/post/219984#post219984 "View Quoted Post")
> 
> Disliked
> 
> Ahh, a couple of things. I have my SL set at -50 and have yet to have a bad trade. Obviously this is risky. Also, I'm using version beta3 and I know that there is now a version beta4. You may want to upgrade as the trade may have been triggered by a "bug" that he has now fixed.
> 
> Ignored

Upss, I must have skipped beta 3 and 4 release, that is weirder than the trade, cause I am the whole day checking for updates ![](https://resources.faireconomy.media/images/emojis/64/1f621.png?v=15.1) . Perhaps it was just posted during my sleepping time ![](https://resources.faireconomy.media/images/emojis/64/1f914.png?v=15.1) Can you please address me if you don't mind, to post where i could find them if you remember....  
regarding your SL got a question here. Do you hold your trade opened even though you got a confirmed signal to place an order in opposite direccion?  
  
Many thanks for your advice 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#246](/thread/post/220063#post220063 "Post Permalink")

  * Feb 17, 2007 1:06am  Feb 17, 2007 1:06am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar19504_4.gif) 1Sundevil](1sundevil)

  * | Joined Sep 2006  | Status: Trader | [228 Posts](/search?do=process&provider=Member&searchuser=19504)

My mistake, it looks like you are using the latest version. I missed the "V" and only saw the "1-1". Thought you were using the original version. I haven't switched over to the new version yet and am still using beta3. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#247](/thread/post/220071#post220071 "Post Permalink")

  * Feb 17, 2007 1:12am  Feb 17, 2007 1:12am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30695_4.gif) toti1972](toti1972)

  * | Joined Jan 2007  | Status: Trader | [107 Posts](/search?do=process&provider=Member&searchuser=30695)

> [Quoting 1Sundevil](/thread/post/220063#post220063 "View Quoted Post")
> 
> Disliked
> 
> My mistake, it looks like you are using the latest version. I missed the "V" and only saw the "1-1". Thought you were using the original version. I haven't switched over to the new version yet and am still using beta3.
> 
> Ignored

i just was about to tell you that, I was looking through the trade I found out that you decided to keep using beta 3 because of your results, but latest version is v 1-1 , no problem, thanks anyway for taking the time to answer my posts...  
Now we need to find out why that issue ( my first post) happened...  
  
regards 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#248](/thread/post/220078#post220078 "Post Permalink")

  * Feb 17, 2007 1:20am  Feb 17, 2007 1:20am 

  * [ Mobsie](mobsie)

  * | Joined Jan 2007  | Status: Trader | [84 Posts](/search?do=process&provider=Member&searchuser=30399)

Hello,  
  
yes i got the same wrong trade.  
  
Mobsie 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#249](/thread/post/220095#post220095 "Post Permalink")

  * Edited 2:01am  Feb 17, 2007 1:35am | Edited 2:01am 

  * [ Forex1man](forex1man)

  * | Joined Oct 2006  | Status: Trader | [58 Posts](/search?do=process&provider=Member&searchuser=21229)

> [Quoting mikhaildgreat](/thread/post/219653#post219653 "View Quoted Post")
> 
> Disliked
> 
> LOL. good for you my friend i completely agree. Im planing to make a new EA sexy pauria, pouria MAs and MACD to identify the trend then use stochastic 5,3,3 as my trigger. I got a question though, what timeframe are you using for "sexy back" and do you exit only when the stochs cross again?  
>    
>  thanks,  
>  Mikhail
> 
> Ignored

  
**I will give you what I do, but please don't trade on my method. It works for me and my style. I use the above "sexy back" indicator setup. I watch in 30 min chart. I use 15 min for pullback trades. I try to wait to sell or buy a pullback after 30 min gets above 80 or below 20 on the 5,3,3 .Then use 15 min for the entry and only make the trade when all the other stoch. are angling up or down and try to trade the 15 min 5,3,3 crossing usually the 20,10,20 in the right direction you are wanting to trade. Sometimes a pullback doesn't take the 30 min back to a 80 or 20. I then see if15 min did. Sometimes the pullbacks are quick but after you watch this part they are easy to spot. I only use the stoch. for _ENTRY_ and use a MM to take profits, I trade serveral lots, or break down the lots into mini's so that you have several exits. My MM method is to have 10 exits to take profits from 25-100 pips. Anything over 100 pip run and I am flat. Remember I am waiting for the pullback before entering 1 st trade, then waiting for it to be either in the 80 or 20 range on the 30 min chart, then using 15 to get in the trade, then I use a 25 pip s/l and ride the wave till it dies or gets me 100 pips, it can take several hours I was in this last one for the last 11 hours see 1 st post time #232. Hope this helps some.**  
  
**Also to help me learn the "sexy method" better he combines all 4 stoch. settings on 1 indicator. That is fine,and then I break all 4 into their own indicator under the main so you get the feel of what you are doing. Then brake them into two time frames 30 and 15. It might seem like a lot of indicators but that helped me get the feel of how good they are. In my opinion mastertering that and taking the trades after a pullback here will net you huge total pips. The last 2 GBP/USD trades both went close to 100 pips each. I am currently only trading GBP so cannot say anything about the rest of the pairs for sure. I am happy with it so don't care about any others at the moment.**

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#250](/thread/post/220296#post220296 "Post Permalink")

  * Feb 17, 2007 5:27am  Feb 17, 2007 5:27am 

  * [ Mobsie](mobsie)

  * | Joined Jan 2007  | Status: Trader | [84 Posts](/search?do=process&provider=Member&searchuser=30399)

Hello,  
  
yes i got the same wrong trade.  
  
Mobsie 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#251](/thread/post/220307#post220307 "Post Permalink")

  * Edited 5:57am  Feb 17, 2007 5:41am | Edited 5:57am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar25698_4.gif) mikhaildgreat](mikhaildgreat)

  * | Joined Nov 2006  | Status: EA Programmer | [298 Posts](/search?do=process&provider=Member&searchuser=25698)

Hello guys,  
  
thats strange indeed toti, as for me I got buy trade for usdchf which hit TP and now im in a sell trade, using M30 timeframe. FXDD broker, what broker are you using? maybe price dipped on your platform because I see a long bear candle on your chart before becoming bullish...  
  
-Mikhail 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#252](/thread/post/220311#post220311 "Post Permalink")

  * Feb 17, 2007 5:55am  Feb 17, 2007 5:55am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar25698_4.gif) mikhaildgreat](mikhaildgreat)

  * | Joined Nov 2006  | Status: EA Programmer | [298 Posts](/search?do=process&provider=Member&searchuser=25698)

> [Quoting Forex1man](/thread/post/220095#post220095 "View Quoted Post")
> 
> Disliked
> 
> **I will give you what I do, but please don't trade on my method. It works for me and my style. I use the above "sexy back" indicator setup. I watch in 30 min chart. I use 15 min for pullback trades. I try to wait to sell or buy a pullback after 30 min gets above 80 or below 20 on the 5,3,3 .Then use 15 min for the entry and only make the trade when all the other stoch. are angling up or down and try to trade the 15 min 5,3,3 crossing usually the 20,10,20 in the right direction you are wanting to trade. Sometimes a pullback doesn't take the 30 min back to a 80 or 20. I then see if15 min did. Sometimes the pullbacks are quick but after you watch this part they are easy to spot. I only use the stoch. for _ENTRY_ and use a MM to take profits, I trade serveral lots, or break down the lots into mini's so that you have several exits. My MM method is to have 10 exits to take profits from 25-100 pips. Anything over 100 pip run and I am flat. Remember I am waiting for the pullback before entering 1 st trade, then waiting for it to be either in the 80 or 20 range on the 30 min chart, then using 15 to get in the trade, then I use a 25 pip s/l and ride the wave till it dies or gets me 100 pips, it can take several hours I was in this last one for the last 11 hours see 1 st post time #232. Hope this helps some.**  
>    
>  **Also to help me learn the "sexy method" better he combines all 4 stoch. settings on 1 indicator. That is fine,and then I break all 4 into their own indicator under the main so you get the feel of what you are doing. Then brake them into two time frames 30 and 15. It might seem like a lot of indicators but that helped me get the feel of how good they are. In my opinion mastertering that and taking the trades after a pullback here will net you huge total pips. The last 2 GBP/USD trades both went close to 100 pips each. I am currently only trading GBP so cannot say anything about the rest of the pairs for sure. I am happy with it so don't care about any others at the moment.**
> 
> Ignored

Hey thanks for your reply. I'm looking to use 30M timeframe for the pouria indicators. But I havnt decide which timeframe to employ the stochs. And maybe Ill focus on either EURUSD or GBPUSD, but EURUSD seems more favorable because of the low spread. So you just use 25 trailing stop and don't actually use the stochs for exit signal, will take a look at that as well.  
  
hmm... maybe 3 entries one with ATR tp, other will be stoch exit, then 3rd with 25 trailing stop. LOL this is all still theory right now will have to do allot of eyeballing the chart and testing... I think this strategy is good enough for the automated championships, combined with a powerful MM like kelly this could make a monster EA.   
  
LOL but its still all theory right now, will see how it fairs in the actual market, hopefully I finish building the first version over the weekend.  
  
Thanks again for your reply,  
Mikhail 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#253](/thread/post/220316#post220316 "Post Permalink")

  * Feb 17, 2007 6:02am  Feb 17, 2007 6:02am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30695_4.gif) toti1972](toti1972)

  * | Joined Jan 2007  | Status: Trader | [107 Posts](/search?do=process&provider=Member&searchuser=30695)

> [Quoting rogerha](/thread/post/219875#post219875 "View Quoted Post")
> 
> Disliked
> 
> Actually looking a little closely (speculating without the actual data), did the 5MA briefly go above the lower of the two longer term MA's and then back below it again ? Then if it did, that would be valid.
> 
> Ignored

rogerha was right in one point, I can see 5MA at exactly the same price than 75MA, and the candle before was bearish, so this makes it a valid entry only for one thing...It never gets the MACD cross confirmation which it is set to "true"   
The point here is. what does the program define as MACD Filter, is it just that the MACD need to be on the right side of the trade? or the program needs to see a cross of 0 line to confirm entry?   
If the answer is the 1st then it was a valid entry...  
If the answer is the 2nd then it wasn't...  
Even though this is a very particular situation, In my opinion the 2nd scenario would be the one to code. But I am not the programmer and I really have no idea if it is possible to do.  
Mikhail you got the answer...  
Thank you. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#254](/thread/post/220321#post220321 "Post Permalink")

  * Feb 17, 2007 6:10am  Feb 17, 2007 6:10am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar19504_4.gif) 1Sundevil](1sundevil)

  * | Joined Sep 2006  | Status: Trader | [228 Posts](/search?do=process&provider=Member&searchuser=19504)

Right now the EA has me in three trades:  
  
BUY: EUR/JPY @ 156.71 right now it's **+12** with TP @ 156.86  
SELL: USD/CHF @ 2341 right now it's **-6** TP @ 2326  
BUY: EUR/USD @ 3138 right now it's **Even/-1** TP @ 3153 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#255](/thread/post/220324#post220324 "Post Permalink")

  * Feb 17, 2007 6:15am  Feb 17, 2007 6:15am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar25698_4.gif) mikhaildgreat](mikhaildgreat)

  * | Joined Nov 2006  | Status: EA Programmer | [298 Posts](/search?do=process&provider=Member&searchuser=25698)

Hello I thought of a simple solution to solve the problem with false entries as what was experienced by toti. Hopefully this will solve the issue. Attached below is version 1.2 with simple fix to avoid entries like this in the future.  
  
Regards,  
Mikhail 

Attached File(s)

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [Pouria EA V-1.2.mq4](/attachment/file/22683?d=1171660537) 20 KB | 421 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#256](/thread/post/220326#post220326 "Post Permalink")

  * Feb 17, 2007 6:20am  Feb 17, 2007 6:20am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar25698_4.gif) mikhaildgreat](mikhaildgreat)

  * | Joined Nov 2006  | Status: EA Programmer | [298 Posts](/search?do=process&provider=Member&searchuser=25698)

yes because EA simply looks at the previous candle to see where the 5MA came from and since previous candle was slightly above 75 MA then went down so it made a sell entry. which we would really have not take if we were trading manually. What I did in this new version is that it looks 2 candles back to see where 5 MA came from, this trade would no longer be taken with the new version. Hopefully this will solve the issue...  
  
-Mikhail  
  

> [Quoting toti1972](/thread/post/220316#post220316 "View Quoted Post")
> 
> Disliked
> 
> rogerha was right in one point, I can see 5MA at exactly the same price than 75MA, and the candle before was bearish, so this makes it a valid entry only for one thing...It never gets the MACD cross confirmation which it is set to "true"   
>  The point here is. what does the program define as MACD Filter, is it just that the MACD need to be on the right side of the trade? or the program needs to see a cross of 0 line to confirm entry?   
>  If the answer is the 1st then it was a valid entry...  
>  If the answer is the 2nd then it wasn't...  
>  Even though this is a very particular situation, In my opinion the 2nd scenario would be the one to code. But I am not the programmer and I really have no idea if it is possible to do.  
>  Mikhail you got the answer...  
>  Thank you.
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#257](/thread/post/220330#post220330 "Post Permalink")

  * Feb 17, 2007 6:30am  Feb 17, 2007 6:30am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar19504_4.gif) 1Sundevil](1sundevil)

  * | Joined Sep 2006  | Status: Trader | [228 Posts](/search?do=process&provider=Member&searchuser=19504)

> [Quoting 1Sundevil](/thread/post/220321#post220321 "View Quoted Post")
> 
> Disliked
> 
> Right now the EA has me in three trades:  
>    
>  BUY: EUR/JPY @ 156.71 right now it's **+12** with TP @ 156.86  
>  SELL: USD/CHF @ 2341 right now it's **-6** TP @ 2326  
>  BUY: EUR/USD @ 3138 right now it's **Even/-1** TP @ 3153
> 
> Ignored

Closed out the EUR/JPY trade for +10. I didn't want to hold a winning trade through the weekend. Right now EUR/USD is +3, so I may close it as well before the bell. CHF is -4, so I'll hold it and take my chances.  
  
So, 8 for 8, 121 pips and up 19.5% this week. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#258](/thread/post/220341#post220341 "Post Permalink")

  * Feb 17, 2007 6:53am  Feb 17, 2007 6:53am 

  * [ Mobsie](mobsie)

  * | Joined Jan 2007  | Status: Trader | [84 Posts](/search?do=process&provider=Member&searchuser=30399)

Hello,  
  
yes i got the same wrong trade.  
  
Mobsie 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#259](/thread/post/220443#post220443 "Post Permalink")

  * Feb 17, 2007 12:56pm  Feb 17, 2007 12:56pm 

  * [ tnh_z](tnh_z)

  * | Joined Apr 2006  | Status: Trader | [16 Posts](/search?do=process&provider=Member&searchuser=8205)

> [Quoting 1Sundevil](/thread/post/220330#post220330 "View Quoted Post")
> 
> Disliked
> 
> ...  
>  So, 8 for 8, 121 pips and up 19.5% this week.
> 
> Ignored

What setting you use for TP & SL ?  
my result was not good. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#260](/thread/post/220446#post220446 "Post Permalink")

  * Feb 17, 2007 1:05pm  Feb 17, 2007 1:05pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar19504_4.gif) 1Sundevil](1sundevil)

  * | Joined Sep 2006  | Status: Trader | [228 Posts](/search?do=process&provider=Member&searchuser=19504)

> [Quoting tnh_z](/thread/post/220443#post220443 "View Quoted Post")
> 
> Disliked
> 
> What setting you use for TP & SL ?  
>  my result was not good.
> 
> Ignored

Generally my TP is what the creator recommended, +15 to +20. My SL is set at -50. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * The Pouria EA Development Thread
  *   * [ **Reply to Thread** ](/thread/17242-the-pouria-ea-development-thread/reply#reply)

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

[The Pouria Method](/thread/17011-the-pouria-method "OKay here is one of the 4 best systems that I've made and used, with this system I pickup atleast 50 pips a day, I'm sharing this because...") 562 replies

[Lessons Learned during System Development](/thread/2986-lessons-learned-during-system-development "Hi, 
  
I've been reading through the forum and somehow I'm in the process of developing my own system.. But not really doing actual...") 29 replies

[(pouria method II on the test)](/thread/23104-pouria-method-ii-on-the-test "Hello  
pouria method II is now DONE thanks to the group of experts and mathematicians that helped and made this method. 
now we are...") 218 replies

[System Development Secrets](/thread/7342-system-development-secrets "&lt;meta http-equiv=&quot;CONTENT-TYPE&quot; content=&quot;text/html; charset=utf-8&quot;&gt;&lt;title&gt;&lt;/title&gt;&lt;meta name=&quot;GENERATOR&quot; content=&quot;OpenOffice.org 2.0 ...") 5 replies

[Metatrader 4 Development Course](/thread/5906-metatrader-4-development-course "Here is the Mql_4_Metatrader_4_Development_Course in pdf \(link fixed\) : 
 
http://www.freefilehosting.org/pupload/view/8711") 3 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/17242-the-pouria-ea-development-thread/reply#reply)
  * Subscribe
  * [45](javascript:void\(0\);)

Attachments: The Pouria EA Development Thread

Tags: The Pouria EA Development Thread

#  [](/thread/17242-the-pouria-ea-development-thread)The Pouria EA Development Thread 

  * 

  * [#261](/thread/post/220454#post220454 "Post Permalink")

  * Feb 17, 2007 1:44pm  Feb 17, 2007 1:44pm 

  * [ tnh_z](tnh_z)

  * | Joined Apr 2006  | Status: Trader | [16 Posts](/search?do=process&provider=Member&searchuser=8205)

> [Quoting 1Sundevil](/thread/post/220446#post220446 "View Quoted Post")
> 
> Disliked
> 
> Generally my TP is what the creator recommended, +15 to +20. My SL is set at -50.
> 
> Ignored

Thank you 1Sundevil,here is my result.TP was based on original method and SL=20. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#262](/thread/post/220459#post220459 "Post Permalink")

  * Feb 17, 2007 2:05pm  Feb 17, 2007 2:05pm 

  * [ tnh_z](tnh_z)

  * | Joined Apr 2006  | Status: Trader | [16 Posts](/search?do=process&provider=Member&searchuser=8205)

Sorry ,forgot it. 

Attached File(s)

![File Type: doc](https://assets.faireconomy.media/images/attach/doc.gif) [Pouria Beta 3.doc](/attachment/file/22706?d=1171688714) 97 KB | 385 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#263](/thread/post/220461#post220461 "Post Permalink")

  * Feb 17, 2007 2:13pm  Feb 17, 2007 2:13pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar19504_4.gif) 1Sundevil](1sundevil)

  * | Joined Sep 2006  | Status: Trader | [228 Posts](/search?do=process&provider=Member&searchuser=19504)

> [Quoting tnh_z](/thread/post/220459#post220459 "View Quoted Post")
> 
> Disliked
> 
> Sorry ,forgot it.
> 
> Ignored

Very strange that although we started at the same time, the EA has dropped you in a lot more trades than me. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#264](/thread/post/220563#post220563 "Post Permalink")

  * Feb 17, 2007 9:50pm  Feb 17, 2007 9:50pm 

  * [ Mobsie](mobsie)

  * | Joined Jan 2007  | Status: Trader | [84 Posts](/search?do=process&provider=Member&searchuser=30399)

Hello,  
  
yes i got the same wrong trade.  
  
Mobsie 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#265](/thread/post/221015#post221015 "Post Permalink")

  * Feb 19, 2007 2:32am  Feb 19, 2007 2:32am 

  * [ raven](raven)

  * | Joined Jul 2006  | Status: Trader | [21 Posts](/search?do=process&provider=Member&searchuser=14079)

Statement for v1.1 below, Traded from about 10 am (GMT) Thursday morning. 33 trades 14 winners 19 losers, although this would have been more as i noticed it kept on trying to buy eur/usd at exactly the right time to sell so i closed a couple and manually put in a sell. The chart timeframes are as stated in the original Pouria thread post 1.  
  
Whilst i was running the ea i also had Luxinterior's pouria indicator v1.2.1 (post 240 on the original thread) running, i have to say it is very impressive, the win loss ratio seems very good and almost all the time it wins if you let it run it wins 60-100 pips a go over a few days, i think if the settings from that indicator could be turned into an ea with just a trailing stop added it could be a really good ea. I would love to run it with a 20 pip sl then as soon as it gets to 10 pip profit move the sl to the breakeven point let it go with a 20 pip trailing stop and leave it. I could not find many times where it did not make 10 pips so you are virtually sure of a free trade. Pity i cant build an ea, any offers...:-)  
  
Heres a little something for you to play with, i built an excel fx fund projections spreadsheet, it works out possible future income based on average pip gains either on a daily or weekly basis based on %fund risk, sl settings and fund size, its a little bit of fun but does show the danger of large sl's, there is also a seperate % fund risk calculator and seperate pip value calculators, all the values can be based on either $ amounts or your own currencies. Feel free to let me know of any comments for revisions or improvments. 

Attached File(s)

![File Type: doc](https://assets.faireconomy.media/images/attach/doc.gif) [North Finance pouria 1.doc](/attachment/file/22804?d=1171819364) 113 KB | 265 downloads 

![File Type: xml](https://assets.faireconomy.media/images/attach/xml.gif) [FX projections v4 excel 2003 international version 3.xml](/attachment/file/22807?d=1171819834) 821 KB | 302 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#266](/thread/post/221080#post221080 "Post Permalink")

  * Feb 19, 2007 5:18am  Feb 19, 2007 5:18am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar22836_4.gif) ilanr](ilanr)

  * | Joined Oct 2006  | Status: Trader | [260 Posts](/search?do=process&provider=Member&searchuser=22836)

Mikhail,  
I suddenly realized that I did not understand your explanations regarding MINStopLoss and MAXStopLoss parameters. Could you please explain in diffrent terms for a dummy like myself, what is their function? I use MA_StopLoss. Thank you...  
Ilan  
  
PS In future versions of the EA you might want to consider using TP defined not from the point of opening a position, but rather from the cross point - because this is the only anchor that can be used in manual backtesting/optimization. For example, the optimal TP for EURUSD seems to be 90 pips from the cross - while the position can opened at different distances from it. 

sans peur et sans reproche

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#267](/thread/post/221084#post221084 "Post Permalink")

  * Feb 19, 2007 5:23am  Feb 19, 2007 5:23am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar25698_4.gif) mikhaildgreat](mikhaildgreat)

  * | Joined Nov 2006  | Status: EA Programmer | [298 Posts](/search?do=process&provider=Member&searchuser=25698)

Hello Again,  
  
V 1.3 Has some new bug fix and features you guys can play around with. further bug fix to prevent false entries. and added trailing stop option. with trailing stop type as fallows. 1 = After profit TS, 2 = instant TS even before profit, 3 = TS 50% of profits.  
  
Again this feature has not yet been tested I just added this today, so play around with it as you see fit and report any bugs when you encounter them.  
  
Thanks,  
  
Mikhail 

Attached File(s)

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [Pouria EA V-1.3.mq4](/attachment/file/22826?d=1171830165) 26 KB | 469 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#268](/thread/post/221178#post221178 "Post Permalink")

  * Feb 19, 2007 8:20am  Feb 19, 2007 8:20am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar19504_4.gif) 1Sundevil](1sundevil)

  * | Joined Sep 2006  | Status: Trader | [228 Posts](/search?do=process&provider=Member&searchuser=19504)

> [Quoting 1Sundevil](/thread/post/220330#post220330 "View Quoted Post")
> 
> Disliked
> 
> Closed out the EUR/JPY trade for +10. I didn't want to hold a winning trade through the weekend. Right now EUR/USD is +3, so I may close it as well before the bell. CHF is -4, so I'll hold it and take my chances.  
>    
>  So, 8 for 8, 121 pips and up 19.5% this week.
> 
> Ignored

WOW! Well, the market opened and closed both of my trades out for +15 each.  
  
So, 10 for 10, +151 pips and my account is now up 42%. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#269](/thread/post/221189#post221189 "Post Permalink")

  * Feb 19, 2007 8:34am  Feb 19, 2007 8:34am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar10157_7.gif) amaruenterprise](amaruenterprise)

  * | Joined May 2006  | Status: Trader | [282 Posts](/search?do=process&provider=Member&searchuser=10157)

Hi 1Sundevil,  
If it's no trouble what settings are you using and what pouria ea version are you using ? Thanks in advanced....Valerie....![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#270](/thread/post/221194#post221194 "Post Permalink")

  * Feb 19, 2007 8:43am  Feb 19, 2007 8:43am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar19504_4.gif) 1Sundevil](1sundevil)

  * | Joined Sep 2006  | Status: Trader | [228 Posts](/search?do=process&provider=Member&searchuser=19504)

> [Quoting amaruenterprise](/thread/post/221189#post221189 "View Quoted Post")
> 
> Disliked
> 
> Hi 1Sundevil,  
>  If it's no trouble what settings are you using and what pouria ea version are you using ? Thanks in advanced....Valerie....![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)
> 
> Ignored

beta3, TP +15 or +20 (as per instructions) and SL at -50. I think I've closed 4 of the trades manually, as I was still either toying with the settings and on Friday I closed my EUR/JPY trade at +10 because I didn't want to hold it through the weekend. Had I it would have hit the +15 TP today, like the other two did.  
  
I'm also having to manually write down each trade as my MT4 platform isn't showing all of the trades, but it is showing the correct "balance" ($). I don't know why it's doing this, but as long as the balance is correct it's ok. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#271](/thread/post/221764#post221764 "Post Permalink")

  * Edited 11:55pm  Feb 19, 2007 11:32pm | Edited 11:55pm 

  * [ BearPaw](bearpaw)

  * | Joined Jul 2006  | Status: A Trader for Life | [218 Posts](/search?do=process&provider=Member&searchuser=13999)

So guys, sorry I was gone...emergency over the weekend.  
  
Last weeks trades netted me 23 pips. Not as good as I had hoped. This is with Beta 3. GBPUSD has been a big loser for me. Or at least netting me out zero.  
  
I am going to keep beta 3 this week, and change SL to -50. Any thoughts?  
  
Thanks,  
  
BP 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#272](/thread/post/221776#post221776 "Post Permalink")

  * Feb 19, 2007 11:56pm  Feb 19, 2007 11:56pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar19504_4.gif) 1Sundevil](1sundevil)

  * | Joined Sep 2006  | Status: Trader | [228 Posts](/search?do=process&provider=Member&searchuser=19504)

The EA has put me in several trades overnight. One, the GBP/USD opened and closed as I slept for +15. So that makes it 11 for 11, +166 pips and my account is now up 47.7%.  
  
Now, that USD/JPY trade has come back around to where it is -1 pip right now.  
  
The other trades are:  
USD/CAD buy @ 1645 (right now -8)  
USD/CHF sell @ 2328 (right now -17)  
EUR/USD sell @ 3122 (right now -13)  
  
So we'll see how these 4 trades do. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#273](/thread/post/221777#post221777 "Post Permalink")

  * Feb 19, 2007 11:56pm  Feb 19, 2007 11:56pm 

  * [ BearPaw](bearpaw)

  * | Joined Jul 2006  | Status: A Trader for Life | [218 Posts](/search?do=process&provider=Member&searchuser=13999)

Mikhail,  
  
Can you describe any fundamental differences in the Beta 3 EA and the V 1, V 1.1, V 1.2, V 1.3 versions?  
  
Thanks,  
  
BP 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#274](/thread/post/221778#post221778 "Post Permalink")

  * Feb 19, 2007 11:58pm  Feb 19, 2007 11:58pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar14103_16.gif) ut2DaMax](ut2damax)

  * | Joined Jul 2006  | Status: Trader | [592 Posts](/search?do=process&provider=Member&searchuser=14103)

I let .... Pouria EA V1.3 ... run on GBP/USD .... settings as is .... net 300.00 over night. Pretty good ..... if it did this most of the time. Forward testing is the only way to be sure on Pouria. It takes time .... but all the backtesting in the world won't compare with actual trading. Mikhail, thanks! You must have done something right on the latest version ... LOL ..... You will eventually perfect it I believe! I like it .... now i hope it keeps raking in the pips! IMO 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#275](/thread/post/221780#post221780 "Post Permalink")

  * Feb 20, 2007 12:04am  Feb 20, 2007 12:04am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar14103_16.gif) ut2DaMax](ut2damax)

  * | Joined Jul 2006  | Status: Trader | [592 Posts](/search?do=process&provider=Member&searchuser=14103)

> [Quoting 1Sundevil](/thread/post/221776#post221776 "View Quoted Post")
> 
> Disliked
> 
> The EA has put me in several trades overnight. One, the GBP/USD opened and closed as I slept for +15. So that makes it 11 for 11, +166 pips and my account is now up 47.7%.  
>    
>  Now, that USD/JPY trade has come back around to where it is -1 pip right now.  
>    
>  The other trades are:  
>  USD/CAD buy @ 1645 (right now -8)  
>  USD/CHF sell @ 2328 (right now -17)  
>  EUR/USD sell @ 3122 (right now -13)  
>    
>  So we'll see how these 4 trades do.
> 
> Ignored

  
  
  
What If I want to use Pouria on 6 pairs for example. Does the magic number have to be different on all pairs,   
  
or only on the same pairs if I have several EA's running on the same pair, & different charts?   
  
Thanks for your help. I wasn't sure. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#276](/thread/post/221784#post221784 "Post Permalink")

  * Feb 20, 2007 12:12am  Feb 20, 2007 12:12am 

  * [ BearPaw](bearpaw)

  * | Joined Jul 2006  | Status: A Trader for Life | [218 Posts](/search?do=process&provider=Member&searchuser=13999)

> [Quoting ut2DaMax](/thread/post/221780#post221780 "View Quoted Post")
> 
> Disliked
> 
> What If I want to use Pouria on 6 pairs for example. Does the magic number have to be different on all pairs,   
>    
>  or only on the same pairs if I have several EA's running on the same pair, & different charts?   
>    
>  Thanks for your help. I wasn't sure.
> 
> Ignored

ut2DaMax,  
  
I have 12 pairs trading with the ea at the same time. I do not change the magic number at all....just the TP settings.  
  
Hopefully this helps,  
  
BP 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#277](/thread/post/222014#post222014 "Post Permalink")

  * Feb 20, 2007 4:05am  Feb 20, 2007 4:05am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar25698_4.gif) mikhaildgreat](mikhaildgreat)

  * | Joined Nov 2006  | Status: EA Programmer | [298 Posts](/search?do=process&provider=Member&searchuser=25698)

> [Quoting ilanr](/thread/post/221080#post221080 "View Quoted Post")
> 
> Disliked
> 
> Mikhail,  
>  I suddenly realized that I did not understand your explanations regarding MINStopLoss and MAXStopLoss parameters. Could you please explain in diffrent terms for a dummy like myself, what is their function? I use MA_StopLoss. Thank you...  
>  Ilan  
>    
>  PS In future versions of the EA you might want to consider using TP defined not from the point of opening a position, but rather from the cross point - because this is the only anchor that can be used in manual backtesting/optimization. For example, the optimal TP for EURUSD seems to be 90 pips from the cross - while the position can opened at different distances from it.
> 
> Ignored

hello.  
  
the MINStopLoss is the minimum stoploss in pips that the EA will you in case the distance from the entry price and the MAs is too near. example if the distance between the entry price and the MAs is just 5 pips. istead us having 5 pips as your stoploss EA will use the MINStoploss in MINStoploss is greater than pips. this is to avoid stoploss being too small. Same with maxstoploss which prevents EA from putting stops that are too large.  
  
-Mikhail 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#278](/thread/post/222015#post222015 "Post Permalink")

  * Feb 20, 2007 4:07am  Feb 20, 2007 4:07am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar25698_4.gif) mikhaildgreat](mikhaildgreat)

  * | Joined Nov 2006  | Status: EA Programmer | [298 Posts](/search?do=process&provider=Member&searchuser=25698)

> [Quoting BearPaw](/thread/post/221777#post221777 "View Quoted Post")
> 
> Disliked
> 
> Mikhail,  
>    
>  Can you describe any fundamental differences in the Beta 3 EA and the V 1, V 1.1, V 1.2, V 1.3 versions?  
>    
>  Thanks,  
>    
>  BP
> 
> Ignored

not much difference only added feature and bug fix.  
  
-Mikhail 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#279](/thread/post/222016#post222016 "Post Permalink")

  * Feb 20, 2007 4:11am  Feb 20, 2007 4:11am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar25698_4.gif) mikhaildgreat](mikhaildgreat)

  * | Joined Nov 2006  | Status: EA Programmer | [298 Posts](/search?do=process&provider=Member&searchuser=25698)

> [Quoting ut2DaMax](/thread/post/221780#post221780 "View Quoted Post")
> 
> Disliked
> 
> What If I want to use Pouria on 6 pairs for example. Does the magic number have to be different on all pairs,   
>    
>  or only on the same pairs if I have several EA's running on the same pair, & different charts?   
>    
>  Thanks for your help. I wasn't sure.
> 
> Ignored

no need to change magic number for each pair.  
  
-Mikhail 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#280](/thread/post/222018#post222018 "Post Permalink")

  * Feb 20, 2007 4:13am  Feb 20, 2007 4:13am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar25698_4.gif) mikhaildgreat](mikhaildgreat)

  * | Joined Nov 2006  | Status: EA Programmer | [298 Posts](/search?do=process&provider=Member&searchuser=25698)

> [Quoting ut2DaMax](/thread/post/221778#post221778 "View Quoted Post")
> 
> Disliked
> 
> I let .... Pouria EA V1.3 ... run on GBP/USD .... settings as is .... net 300.00 over night. Pretty good ..... if it did this most of the time. Forward testing is the only way to be sure on Pouria. It takes time .... but all the backtesting in the world won't compare with actual trading. Mikhail, thanks! You must have done something right on the latest version ... LOL ..... You will eventually perfect it I believe! I like it .... now i hope it keeps raking in the pips! IMO
> 
> Ignored

good to hear that. I know there are still many improvements that must be made. specially false entries that happen when MAs are just hovering very near the 75&85 MAs. I have thought of a couple of solutions... but v1.3 is still not completely free from these bugs...   
  
I hope when we get to version 2 we have fixed all these irritating bugs...  
  
-Mikhail 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * The Pouria EA Development Thread
  *   * [ **Reply to Thread** ](/thread/17242-the-pouria-ea-development-thread/reply#reply)

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

[The Pouria Method](/thread/17011-the-pouria-method "OKay here is one of the 4 best systems that I've made and used, with this system I pickup atleast 50 pips a day, I'm sharing this because...") 562 replies

[Lessons Learned during System Development](/thread/2986-lessons-learned-during-system-development "Hi, 
  
I've been reading through the forum and somehow I'm in the process of developing my own system.. But not really doing actual...") 29 replies

[(pouria method II on the test)](/thread/23104-pouria-method-ii-on-the-test "Hello  
pouria method II is now DONE thanks to the group of experts and mathematicians that helped and made this method. 
now we are...") 218 replies

[System Development Secrets](/thread/7342-system-development-secrets "&lt;meta http-equiv=&quot;CONTENT-TYPE&quot; content=&quot;text/html; charset=utf-8&quot;&gt;&lt;title&gt;&lt;/title&gt;&lt;meta name=&quot;GENERATOR&quot; content=&quot;OpenOffice.org 2.0 ...") 5 replies

[Metatrader 4 Development Course](/thread/5906-metatrader-4-development-course "Here is the Mql_4_Metatrader_4_Development_Course in pdf \(link fixed\) : 
 
http://www.freefilehosting.org/pupload/view/8711") 3 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/17242-the-pouria-ea-development-thread/reply#reply)
  * Subscribe
  * [45](javascript:void\(0\);)

Attachments: The Pouria EA Development Thread

Tags: The Pouria EA Development Thread

#  [](/thread/17242-the-pouria-ea-development-thread)The Pouria EA Development Thread 

  * 

  * [#281](/thread/post/222082#post222082 "Post Permalink")

  * Feb 20, 2007 6:01am  Feb 20, 2007 6:01am 

  * [ BearPaw](bearpaw)

  * | Joined Jul 2006  | Status: A Trader for Life | [218 Posts](/search?do=process&provider=Member&searchuser=13999)

So Mikhail, if the later versions are the same as Beta 3, should I use V1.3 which has the fixes?  
  
Thanks,  
  
BP 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#282](/thread/post/222085#post222085 "Post Permalink")

  * Feb 20, 2007 6:06am  Feb 20, 2007 6:06am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar25698_4.gif) mikhaildgreat](mikhaildgreat)

  * | Joined Nov 2006  | Status: EA Programmer | [298 Posts](/search?do=process&provider=Member&searchuser=25698)

> [Quoting BearPaw](/thread/post/222082#post222082 "View Quoted Post")
> 
> Disliked
> 
> So Mikhail, if the later versions are the same as Beta 3, should I use V1.3 which has the fixes?  
>    
>  Thanks,  
>    
>  BP
> 
> Ignored

yup, it just has more settings you can play with...  
  
-Mikhail 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#283](/thread/post/222129#post222129 "Post Permalink")

  * Feb 20, 2007 7:22am  Feb 20, 2007 7:22am 

  * [ BearPaw](bearpaw)

  * | Joined Jul 2006  | Status: A Trader for Life | [218 Posts](/search?do=process&provider=Member&searchuser=13999)

> [Quoting mikhaildgreat](/thread/post/222085#post222085 "View Quoted Post")
> 
> Disliked
> 
> yup, it just has more settings you can play with...  
>    
>  -Mikhail
> 
> Ignored

Mikhail,  
  
Ok, so here are the settings that I am using that are somewhat variable....  
  
mincross....I am keeping this at the 3.0 that you have...is that a good setting?  
  
Use MAstoploss - I do not want to use that, have set it at false  
  
Trailing Stop = 1 - kept that there...do not want trailing stop at this time...so is that correct?  
  
Martingale = false - do not want to use it at this time  
  
MM = false - do not want to use Money Management at this time.  
  
So, is that correct?  
  
Thanks,  
  
BP 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#284](/thread/post/222133#post222133 "Post Permalink")

  * Feb 20, 2007 7:26am  Feb 20, 2007 7:26am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar25698_4.gif) mikhaildgreat](mikhaildgreat)

  * | Joined Nov 2006  | Status: EA Programmer | [298 Posts](/search?do=process&provider=Member&searchuser=25698)

> [Quoting BearPaw](/thread/post/222129#post222129 "View Quoted Post")
> 
> Disliked
> 
> Mikhail,  
>    
>  Ok, so here are the settings that I am using that are somewhat variable....  
>    
>  mincross....I am keeping this at the 3.0 that you have...is that a good setting?  
>    
>  Use MAstoploss - I do not want to use that, have set it at false  
>    
>  Trailing Stop = 1 - kept that there...do not want trailing stop at this time...so is that correct?  
>    
>  Martingale = false - do not want to use it at this time  
>    
>  MM = false - do not want to use Money Management at this time.  
>    
>  So, is that correct?  
>    
>  Thanks,  
>    
>  BP
> 
> Ignored

yup looks good 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#285](/thread/post/222136#post222136 "Post Permalink")

  * Feb 20, 2007 7:33am  Feb 20, 2007 7:33am 

  * [ BearPaw](bearpaw)

  * | Joined Jul 2006  | Status: A Trader for Life | [218 Posts](/search?do=process&provider=Member&searchuser=13999)

> [Quoting mikhaildgreat](/thread/post/222133#post222133 "View Quoted Post")
> 
> Disliked
> 
> yup looks good
> 
> Ignored

lol...sorry Mikhail...  
  
MACdfiler...set to true....what is this? Should I just keep it at true?  
  
Thanks,  
  
BP 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#286](/thread/post/222139#post222139 "Post Permalink")

  * Feb 20, 2007 7:40am  Feb 20, 2007 7:40am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar25698_4.gif) mikhaildgreat](mikhaildgreat)

  * | Joined Nov 2006  | Status: EA Programmer | [298 Posts](/search?do=process&provider=Member&searchuser=25698)

> [Quoting BearPaw](/thread/post/222136#post222136 "View Quoted Post")
> 
> Disliked
> 
> lol...sorry Mikhail...  
>    
>  MACdfiler...set to true....what is this? Should I just keep it at true?  
>    
>  Thanks,  
>    
>  BP
> 
> Ignored

yup. if false EA will only trade using MAs. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#287](/thread/post/222183#post222183 "Post Permalink")

  * Feb 20, 2007 8:47am  Feb 20, 2007 8:47am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar19504_4.gif) 1Sundevil](1sundevil)

  * | Joined Sep 2006  | Status: Trader | [228 Posts](/search?do=process&provider=Member&searchuser=19504)

Manually closed out the USDJPY trade for +12. So, 12 for 12, +178 pips.  
  
The EA still has me in 4 trades right now. I'm very worried about the EURUSD trade (as it is still a big loser right now) and now the newest is a GBPUSD trade, but I have them going in opposite directions. So, as always, we'll see what happens. I'd rather take the -50 on the GBPUSD as it is half the lots of the EURUSD trade. I need some "DOLLAR POWER" tomorrow to make it happen.  
  
Right now:  
USDCAD is EVEN  
USDCHF is -8  
EURUSD is -30  
GBPUSD is -15 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#288](/thread/post/222247#post222247 "Post Permalink")

  * Feb 20, 2007 10:49am  Feb 20, 2007 10:49am 

  * [ BearPaw](bearpaw)

  * | Joined Jul 2006  | Status: A Trader for Life | [218 Posts](/search?do=process&provider=Member&searchuser=13999)

> [Quoting 1Sundevil](/thread/post/222183#post222183 "View Quoted Post")
> 
> Disliked
> 
> Manually closed out the USDJPY trade for +12. So, 12 for 12, +178 pips.  
>    
>  The EA still has me in 4 trades right now. I'm very worried about the EURUSD trade (as it is still a big loser right now) and now the newest is a GBPUSD trade, but I have them going in opposite directions. So, as always, we'll see what happens. I'd rather take the -50 on the GBPUSD as it is half the lots of the EURUSD trade. I need some "DOLLAR POWER" tomorrow to make it happen.  
>    
>  Right now:  
>  USDCAD is EVEN  
>  USDCHF is -8  
>  EURUSD is -30  
>  GBPUSD is -15
> 
> Ignored

Hey Sundevil...I hear ya. The eurusd turned around and came in to make some money. I would have been stopped out had it not been for the new SL of 50...we shall see.  
  
Anyway...I must have been closed out of the CAD cause of the different stop loss amount...so I am out of that trade for a loss of 20.  
  
I am still in:  
  
USDCHF -19  
GBPUSD -22  
  
I was entered into these 2 trades today as well....  
  
AUDUSD -13  
EURCHF -6  
  
So, in the negatives...but maybe they will turn around. I am now using V1.3.  
  
Thanks guys,  
  
BP 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#289](/thread/post/222258#post222258 "Post Permalink")

  * Feb 20, 2007 11:13am  Feb 20, 2007 11:13am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar19504_4.gif) 1Sundevil](1sundevil)

  * | Joined Sep 2006  | Status: Trader | [228 Posts](/search?do=process&provider=Member&searchuser=19504)

> [Quoting 1Sundevil](/thread/post/222183#post222183 "View Quoted Post")
> 
> Disliked
> 
> Manually closed out the USDJPY trade for +12. So, 12 for 12, +178 pips.  
>    
>  The EA still has me in 4 trades right now. I'm very worried about the EURUSD trade (as it is still a big loser right now) and now the newest is a GBPUSD trade, but I have them going in opposite directions. So, as always, we'll see what happens. I'd rather take the -50 on the GBPUSD as it is half the lots of the EURUSD trade. I need some "DOLLAR POWER" tomorrow to make it happen.  
>    
>  Right now:  
>  USDCAD is EVEN  
>  USDCHF is -8  
>  EURUSD is -30  
>  GBPUSD is -15
> 
> Ignored

Well, my fear were realized and got STOMPED out on the EUR trade for -50...and it was a big one in terms of lot size.  
  
On the positive side, the GBPUSD trade closed for +15. The other two are still open and both are currently positive.  
  
So, 13 out of 14 and +143 pips with two still open. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#290](/thread/post/222264#post222264 "Post Permalink")

  * Feb 20, 2007 11:22am  Feb 20, 2007 11:22am 

  * [ ghamal](ghamal)

  * | Joined Dec 2006  | Status: Trader | [23 Posts](/search?do=process&provider=Member&searchuser=27492)

Hi Mikhail, thanks for all your work on the EAs. I started forward testing 1.3. These are the results so far with 6 pairs, eurusd, gbpusd, usdjpy, usdcad, cadusd, usdchf:  
  
So far not great but it's still way too early to tell,  
  
<http://img443.imageshack.us/img443/8425/43499997yk3.jpg>

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#291](/thread/post/222266#post222266 "Post Permalink")

  * Feb 20, 2007 11:23am  Feb 20, 2007 11:23am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar19504_4.gif) 1Sundevil](1sundevil)

  * | Joined Sep 2006  | Status: Trader | [228 Posts](/search?do=process&provider=Member&searchuser=19504)

The infamous EURUSD (-50) trade: Hard to see, but it starts at the "LOW" end on the right half of the screen. You can just make out the little red arrow inbetween the big drop and the subsequent long rise back up. 

Attached Image

![](/attachment/image/22958?d=1171938170)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#292](/thread/post/222273#post222273 "Post Permalink")

  * Feb 20, 2007 11:46am  Feb 20, 2007 11:46am 

  * [ asiaboss](asiaboss)

  * | Joined Jul 2006  | Status: Trader | [7 Posts](/search?do=process&provider=Member&searchuser=13622)

Could anyone please give me a little help as I am new to EA? I'm using Pouria EA V-1.3 on MT4 but I can't get the system to trade on my demo account of 5k. I checked the "Allow Live Trading" box in the Live Trading area already. But, I'm not getting the system to trade on my demo account. Can anyone please give me some hint? Thanks. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#293](/thread/post/222355#post222355 "Post Permalink")

  * Feb 20, 2007 2:14pm  Feb 20, 2007 2:14pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar10333_10.gif) amenlo9](amenlo9)

  * | Joined May 2006  | Status: Trader | [600 Posts](/search?do=process&provider=Member&searchuser=10333)

> [Quoting asiaboss](/thread/post/222273#post222273 "View Quoted Post")
> 
> Disliked
> 
> Could anyone please give me a little help as I am new to EA? I'm using Pouria EA V-1.3 on MT4 but I can't get the system to trade on my demo account of 5k. I checked the "Allow Live Trading" box in the Live Trading area already. But, I'm not getting the system to trade on my demo account. Can anyone please give me some hint? Thanks.
> 
> Ignored

did you enable Expert Advisor already?if not,please enable it at the toolbar beside MetaEditor 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#294](/thread/post/222359#post222359 "Post Permalink")

  * Feb 20, 2007 2:17pm  Feb 20, 2007 2:17pm 

  * [ asiaboss](asiaboss)

  * | Joined Jul 2006  | Status: Trader | [7 Posts](/search?do=process&provider=Member&searchuser=13622)

Yes, I've already enabled it and see a green icon on the chart. But still it's not working. I don't know what else I am missing as I look everywhere but couldn't find the reason. I've also reinstall everything on a second computer and got the same result. ![](https://resources.faireconomy.media/images/emojis/64/1f641.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#295](/thread/post/222362#post222362 "Post Permalink")

  * Feb 20, 2007 2:23pm  Feb 20, 2007 2:23pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar10333_10.gif) amenlo9](amenlo9)

  * | Joined May 2006  | Status: Trader | [600 Posts](/search?do=process&provider=Member&searchuser=10333)

> [Quoting asiaboss](/thread/post/222359#post222359 "View Quoted Post")
> 
> Disliked
> 
> Yes, I've already enabled it and see a green icon on the chart. But still it's not working. I don't know what else I am missing as I look everywhere but couldn't find the reason. I've also reinstall everything on a second computer and got the same result. ![](https://resources.faireconomy.media/images/emojis/64/1f641.png?v=15.1)
> 
> Ignored

that pretty strange.did you the smile icon at the top of your right hand side?maybe your EA is working but just haven't trigger any position yet because no entry signal.  
  
second thing u can do is uninstall your metatrader, delete the folder inside Program Files as well and re-install it. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#296](/thread/post/222631#post222631 "Post Permalink")

  * Feb 20, 2007 8:31pm  Feb 20, 2007 8:31pm 

  * [ BearPaw](bearpaw)

  * | Joined Jul 2006  | Status: A Trader for Life | [218 Posts](/search?do=process&provider=Member&searchuser=13999)

Well, had some success overnight....![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)   
  
Here it is....  
  
eurusd------------buy----------1.3149-----------+15  
eurchf------------buy----------1.6232-----------+15  
usdchf------------buy----------1.2346-----------+10  
gbpusd-----------buy-----------1.9534-----------(-50)  
usdchf-----------buy-----------1.2361-----------+10  
  
Net result = zero pips!!  
  
GBPUSD has not been a good pair for me...but lets see how it goes this week with the new SL.  
  
Still open...  
  
AUDUSD -------open for a buy  
EURCHF--------open for a buy - close to TP  
GBPUSD-------open for a sell  
EURUSD-------open for a sell  
  
  
Thanks,  
BP 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#297](/thread/post/222820#post222820 "Post Permalink")

  * Feb 20, 2007 11:50pm  Feb 20, 2007 11:50pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar19504_4.gif) 1Sundevil](1sundevil)

  * | Joined Sep 2006  | Status: Trader | [228 Posts](/search?do=process&provider=Member&searchuser=19504)

> [Quoting 1Sundevil](/thread/post/222183#post222183 "View Quoted Post")
> 
> Disliked
> 
> Manually closed out the USDJPY trade for +12. So, 12 for 12, +178 pips.  
>    
>  The EA still has me in 4 trades right now. I'm very worried about the EURUSD trade (as it is still a big loser right now) and now the newest is a GBPUSD trade, but I have them going in opposite directions. So, as always, we'll see what happens. I'd rather take the -50 on the GBPUSD as it is half the lots of the EURUSD trade. I need some "DOLLAR POWER" tomorrow to make it happen.  
>    
>  Right now:  
>  USDCAD is EVEN  
>  USDCHF is -8  
>  EURUSD is -30  
>  GBPUSD is -15
> 
> Ignored

Well, one thing I have definitely learned is that I simply don't trust MetaTrader as a platform.   
  
1: Got up this morning and found that my balance is much less than last night, even though the "account history" is showing no new trades closed. Hmmmm.  
  
2: BOTH of my USDCAD and USDCHF trades have completely disappeared...even though they both should have hit my TP for +15 each. Hmmmm.  
  
3: The EA entered me into a GBPUSD sell @ 9492. Now, it should have hit my TP at 9477 as the charts show that it got as low as 9476. Well, it didn't close the trade at 9477 and instead just closed it for -50. Hmmmm.  
  
**So, who has a better set of charts out there to use? Ones which I can add this EA to?**

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#298](/thread/post/222827#post222827 "Post Permalink")

  * Feb 20, 2007 11:55pm  Feb 20, 2007 11:55pm 

  * [ BearPaw](bearpaw)

  * | Joined Jul 2006  | Status: A Trader for Life | [218 Posts](/search?do=process&provider=Member&searchuser=13999)

> [Quoting 1Sundevil](/thread/post/222820#post222820 "View Quoted Post")
> 
> Disliked
> 
> Well, one thing I have definitely learned is that I simply don't trust MetaTrader as a platform.   
>    
>  1: Got up this morning and found that my balance is much less than last night, even though the "account history" is showing no new trades closed. Hmmmm.  
>    
>  2: BOTH of my USDCAD and USDCHF trades have completely disappeared...even though they both should have hit my TP for +15 each. Hmmmm.  
>    
>  3: The EA entered me into a GBPUSD sell @ 9492. Now, it should have hit my TP at 9477 as the charts show that it got as low as 9476. Well, it didn't close the trade at 9477 and instead just closed it for -50. Hmmmm.  
>    
>  **So, who has a better set of charts out there to use? Ones which I can add this EA to?**
> 
> Ignored

Sundevil,  
  
I like the IBFX platform for MT4. It has not been bad for me. You can demo it...is that who you are using now?  
  
BP 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#299](/thread/post/222832#post222832 "Post Permalink")

  * Feb 20, 2007 11:59pm  Feb 20, 2007 11:59pm 

  * [ BearPaw](bearpaw)

  * | Joined Jul 2006  | Status: A Trader for Life | [218 Posts](/search?do=process&provider=Member&searchuser=13999)

> [Quoting BearPaw](/thread/post/222631#post222631 "View Quoted Post")
> 
> Disliked
> 
> Well, had some success overnight....![](https://resources.faireconomy.media/images/emojis/64/1f609.png?v=15.1)   
>    
>  Here it is....  
>    
>  eurusd------------buy----------1.3149-----------+15  
>  eurchf------------buy----------1.6232-----------+15  
>  usdchf------------buy----------1.2346-----------+10  
>  gbpusd-----------buy-----------1.9534-----------(-50)  
>  usdchf-----------buy-----------1.2361-----------+10  
>    
>  Net result = zero pips!!  
>    
>  GBPUSD has not been a good pair for me...but lets see how it goes this week with the new SL.  
>    
>  Still open...  
>    
>  AUDUSD -------open for a buy  
>  EURCHF--------open for a buy - close to TP  
>  GBPUSD-------open for a sell  
>  EURUSD-------open for a sell  
>    
>    
>  Thanks,  
>  BP
> 
> Ignored

Ok...adding to the above calculations....  
  
EURCHF closed out for a 15 pip profit.  
GBPUSD closed out for another 50 pip loss....  
  
Total net for the day.... (-35)pips.  
  
Forexpert......GBP seems to be killing me....advice here????!!!  
  
Now open....  
  
AUDUSD from above...still open for a buy  
EURUSD from above ....still open for a sell  
GBPUSD ....new...open for a buy....close to TP....  
  
BP 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#300](/thread/post/222841#post222841 "Post Permalink")

  * Feb 21, 2007 12:05am  Feb 21, 2007 12:05am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar19504_4.gif) 1Sundevil](1sundevil)

  * | Joined Sep 2006  | Status: Trader | [228 Posts](/search?do=process&provider=Member&searchuser=19504)

> [Quoting BearPaw](/thread/post/222827#post222827 "View Quoted Post")
> 
> Disliked
> 
> Sundevil,  
>    
>  I like the IBFX platform for MT4. It has not been bad for me. You can demo it...is that who you are using now?  
>    
>  BP
> 
> Ignored

It says that my server is MIG-Demo. How do I switch to IBFX? I just downloaded the MT4 platform from the metatrader site.   
  
Very frustrating as I'm showing good results with the EA but now the platform is starting to screw with things it shouldn't.  
  
I'm also considering moving all of my TP's to +10. It seems that even in the one BIG loser, that it would have hit +10 early and never would have gone negative. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * The Pouria EA Development Thread
  *   * [ **Reply to Thread** ](/thread/17242-the-pouria-ea-development-thread/reply#reply)

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

[The Pouria Method](/thread/17011-the-pouria-method "OKay here is one of the 4 best systems that I've made and used, with this system I pickup atleast 50 pips a day, I'm sharing this because...") 562 replies

[Lessons Learned during System Development](/thread/2986-lessons-learned-during-system-development "Hi, 
  
I've been reading through the forum and somehow I'm in the process of developing my own system.. But not really doing actual...") 29 replies

[(pouria method II on the test)](/thread/23104-pouria-method-ii-on-the-test "Hello  
pouria method II is now DONE thanks to the group of experts and mathematicians that helped and made this method. 
now we are...") 218 replies

[System Development Secrets](/thread/7342-system-development-secrets "&lt;meta http-equiv=&quot;CONTENT-TYPE&quot; content=&quot;text/html; charset=utf-8&quot;&gt;&lt;title&gt;&lt;/title&gt;&lt;meta name=&quot;GENERATOR&quot; content=&quot;OpenOffice.org 2.0 ...") 5 replies

[Metatrader 4 Development Course](/thread/5906-metatrader-4-development-course "Here is the Mql_4_Metatrader_4_Development_Course in pdf \(link fixed\) : 
 
http://www.freefilehosting.org/pupload/view/8711") 3 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/17242-the-pouria-ea-development-thread/reply#reply)
  * Subscribe
  * [45](javascript:void\(0\);)

Attachments: The Pouria EA Development Thread

Tags: The Pouria EA Development Thread

#  [](/thread/17242-the-pouria-ea-development-thread)The Pouria EA Development Thread 

  * 

  * [#301](/thread/post/222858#post222858 "Post Permalink")

  * Feb 21, 2007 12:22am  Feb 21, 2007 12:22am 

  * [ BearPaw](bearpaw)

  * | Joined Jul 2006  | Status: A Trader for Life | [218 Posts](/search?do=process&provider=Member&searchuser=13999)

> [Quoting 1Sundevil](/thread/post/222841#post222841 "View Quoted Post")
> 
> Disliked
> 
> It says that my server is MIG-Demo. How do I switch to IBFX? I just downloaded the MT4 platform from the metatrader site.   
>    
>  Very frustrating as I'm showing good results with the EA but now the platform is starting to screw with things it shouldn't.  
>    
>  I'm also considering moving all of my TP's to +10. It seems that even in the one BIG loser, that it would have hit +10 early and never would have gone negative.
> 
> Ignored

Sundevil,  
  
Go to interbankfx.com   
Download the demo account for MT4.  
  
That should do it.  
  
BP 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#302](/thread/post/222861#post222861 "Post Permalink")

  * Edited 12:49am  Feb 21, 2007 12:24am | Edited 12:49am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar19504_4.gif) 1Sundevil](1sundevil)

  * | Joined Sep 2006  | Status: Trader | [228 Posts](/search?do=process&provider=Member&searchuser=19504)

> [Quoting BearPaw](/thread/post/222858#post222858 "View Quoted Post")
> 
> Disliked
> 
> Sundevil,  
>    
>  Go to interbankfx.com   
>  Download the demo account for MT4.  
>    
>  That should do it.  
>    
>  BP
> 
> Ignored

Thanks, I'm on my way there.  
  
Ok, set it up so we're back in business. I made a small change this time. I set my TP at +10 and my SL is still at +50. We'll see what this does. Obviously one loss would be trouble, but from what I've seen, even in the one loss I've taken, it would have hit a +10 TP before heading away. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#303](/thread/post/222905#post222905 "Post Permalink")

  * Feb 21, 2007 12:56am  Feb 21, 2007 12:56am 

  * [ raven](raven)

  * | Joined Jul 2006  | Status: Trader | [21 Posts](/search?do=process&provider=Member&searchuser=14079)

ive just changed all my settings to a tp of 10, but ive kept the sl at 20, i couldnt run a sl of 50 on a live account to high a risk ratio for a 10 pip gain. Lets see how we get on. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#304](/thread/post/222968#post222968 "Post Permalink")

  * Feb 21, 2007 1:40am  Feb 21, 2007 1:40am 

  * [ BearPaw](bearpaw)

  * | Joined Jul 2006  | Status: A Trader for Life | [218 Posts](/search?do=process&provider=Member&searchuser=13999)

Mikhail,  
  
This GBP sell trade entered early and did not seem to wait for the cross...if it would have entered at 1.9496 or close to where the 5ma crosses the 75/85, it could have come away with profit probably.....So, is there a way???  
  
Or is the ea just set up this way and that is how the program works?  
  
Thanks for any who comment.  
  
BP 

Attached Image

![](/attachment/image/23016?d=1171989512)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#305](/thread/post/223135#post223135 "Post Permalink")

  * Feb 21, 2007 3:58am  Feb 21, 2007 3:58am 

  * [ winsteadglenn](winsteadglenn)

  * | Joined Nov 2006  | Status: Trader | [330 Posts](/search?do=process&provider=Member&searchuser=25826)

My gut tells me that SunDevil is right: TP 10 across the board.  
Also that Raven is right: tight stops, even if it means some minor losses. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#306](/thread/post/223185#post223185 "Post Permalink")

  * Feb 21, 2007 5:03am  Feb 21, 2007 5:03am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar22836_4.gif) ilanr](ilanr)

  * | Joined Oct 2006  | Status: Trader | [260 Posts](/search?do=process&provider=Member&searchuser=22836)

The EA v. 1.3 is attached to a 1HR AUDUSD chart. MinCrossDistance is set at 3 points. The 5 MA came from above and spent about 4 hours between the slower MA lines (never going below). Then it moved up 1 point above the upper MA - and the EA opened a long position. The price didn't cross up from below and it crossed only by 1 p. Could there still be a bug? 

sans peur et sans reproche

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#307](/thread/post/223203#post223203 "Post Permalink")

  * Feb 21, 2007 5:21am  Feb 21, 2007 5:21am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar25698_4.gif) mikhaildgreat](mikhaildgreat)

  * | Joined Nov 2006  | Status: EA Programmer | [298 Posts](/search?do=process&provider=Member&searchuser=25698)

Hello everyone Ive also been forward testing version 1.3 and it has opened a couple of wrong trades. to let everyone know the most stable version is still beta 3.  
  
I hate these bugs! LOL. I will clean the code again and release next version. I will work on beta 3. strip all the other features and only work on just eliminating false entries...  
  
-Mikhail  

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#308](/thread/post/223223#post223223 "Post Permalink")

  * Feb 21, 2007 5:58am  Feb 21, 2007 5:58am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar25698_4.gif) mikhaildgreat](mikhaildgreat)

  * | Joined Nov 2006  | Status: EA Programmer | [298 Posts](/search?do=process&provider=Member&searchuser=25698)

I found the problem on V1.3... I put a (+) sign when it was supposed to be a (-). I took a long look at the code to make sure there were no longer any such stupid mistakes... All the features are in still intact but im almost certain there will no longer be false entires. In backtest its working as It should. Now we can finally focus on the strategy...  
  
Thank you for your patience, hopefully this is the final version.  
  
-Mikhail 

Attached File(s)

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [Pouria EA V-1.4.mq4](/attachment/file/23053?d=1172005093) 26 KB | 745 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#309](/thread/post/223288#post223288 "Post Permalink")

  * Feb 21, 2007 7:32am  Feb 21, 2007 7:32am 

  * [ BearPaw](bearpaw)

  * | Joined Jul 2006  | Status: A Trader for Life | [218 Posts](/search?do=process&provider=Member&searchuser=13999)

> [Quoting mikhaildgreat](/thread/post/223223#post223223 "View Quoted Post")
> 
> Disliked
> 
> I found the problem on V1.3... I put a (+) sign when it was supposed to be a (-). I took a long look at the code to make sure there were no longer any such stupid mistakes... All the features are in still intact but im almost certain there will no longer be false entires. In backtest its working as It should. Now we can finally focus on the strategy...  
>    
>  Thank you for your patience, hopefully this is the final version.  
>    
>  -Mikhail
> 
> Ignored

Mikhail....you are great...  
  
Thanks for your efforts!!!  
  
BP 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#310](/thread/post/223429#post223429 "Post Permalink")

  * Feb 21, 2007 10:55am  Feb 21, 2007 10:55am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30695_4.gif) toti1972](toti1972)

  * | Joined Jan 2007  | Status: Trader | [107 Posts](/search?do=process&provider=Member&searchuser=30695)

Hi everyone,  
  
I got this order a few min ago on the brand new Pouria 1.4 version, which was not a valid entry (upper right corner)  
5ma never crosses.  
Anybody else got it?  
the order was Buy EUR/JPY 158.12 and now is 15 pips down.  
Mikhail, what could have happened????  
  
Thanks. 

Attached Image

![](/attachment/image/23074?d=1172021799)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#311](/thread/post/223454#post223454 "Post Permalink")

  * Feb 21, 2007 11:48am  Feb 21, 2007 11:48am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar19504_4.gif) 1Sundevil](1sundevil)

  * | Joined Sep 2006  | Status: Trader | [228 Posts](/search?do=process&provider=Member&searchuser=19504)

> [Quoting toti1972](/thread/post/223429#post223429 "View Quoted Post")
> 
> Disliked
> 
> Hi everyone,  
>    
>  I got this order a few min ago on the brand new Pouria 1.4 version, which was not a valid entry (upper right corner)  
>  5ma never crosses.  
>  Anybody else got it?  
>  the order was Buy EUR/JPY 158.12 and now is 15 pips down.  
>  Mikhail, what could have happened????  
>    
>  Thanks.
> 
> Ignored

I got the same order, which is now EVEN. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#312](/thread/post/223456#post223456 "Post Permalink")

  * Feb 21, 2007 11:50am  Feb 21, 2007 11:50am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar19504_4.gif) 1Sundevil](1sundevil)

  * | Joined Sep 2006  | Status: Trader | [228 Posts](/search?do=process&provider=Member&searchuser=19504)

> [Quoting 1Sundevil](/thread/post/223454#post223454 "View Quoted Post")
> 
> Disliked
> 
> I got the same order, which is now EVEN.
> 
> Ignored

Correction, it just hit my TP for +15! Nice.  
  
So, 15 of 16 for +173 pips. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#313](/thread/post/223482#post223482 "Post Permalink")

  * Feb 21, 2007 12:23pm  Feb 21, 2007 12:23pm 

  * [ BearPaw](bearpaw)

  * | Joined Jul 2006  | Status: A Trader for Life | [218 Posts](/search?do=process&provider=Member&searchuser=13999)

Mine seemed to hit TP pretty quickly...  
  
Did not look to see if any of the crosses did or did not happen.  
  
Still in my AUDUSD and EURUSD trades though...  
  
Both close to BE.  
  
Goodnite,  
  
BP 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#314](/thread/post/223501#post223501 "Post Permalink")

  * Feb 21, 2007 12:46pm  Feb 21, 2007 12:46pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30695_4.gif) toti1972](toti1972)

  * | Joined Jan 2007  | Status: Trader | [107 Posts](/search?do=process&provider=Member&searchuser=30695)

> [Quoting 1Sundevil](/thread/post/223456#post223456 "View Quoted Post")
> 
> Disliked
> 
> Correction, it just hit my TP for +15! Nice.  
>    
>  So, 15 of 16 for +173 pips.
> 
> Ignored

Yeah hopefully it was a winner, but I think it shouldn't have happened...  
  
still struggling with AUD/USD : -22 so far...  
EUR/GBP: -10  
EUR/CHF; -6  
  
will see you guys tomorrow morning...with overnight results  
  
Take a rest...have a good night...![](https://resources.faireconomy.media/images/emojis/64/1f44b.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#315](/thread/post/223718#post223718 "Post Permalink")

  * Feb 21, 2007 4:50pm  Feb 21, 2007 4:50pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar25698_4.gif) mikhaildgreat](mikhaildgreat)

  * | Joined Nov 2006  | Status: EA Programmer | [298 Posts](/search?do=process&provider=Member&searchuser=25698)

> [Quoting toti1972](/thread/post/223429#post223429 "View Quoted Post")
> 
> Disliked
> 
> Hi everyone,  
>    
>  I got this order a few min ago on the brand new Pouria 1.4 version, which was not a valid entry (upper right corner)  
>  5ma never crosses.  
>  Anybody else got it?  
>  the order was Buy EUR/JPY 158.12 and now is 15 pips down.  
>  Mikhail, what could have happened????  
>    
>  Thanks.
> 
> Ignored

Its a valid entry. MACD dipped below zero then went back up... read post #1 to get better understanding  
  
-Mikhail  
  
-Mikhail 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#316](/thread/post/224029#post224029 "Post Permalink")

  * Feb 21, 2007 9:59pm  Feb 21, 2007 9:59pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30695_4.gif) toti1972](toti1972)

  * | Joined Jan 2007  | Status: Trader | [107 Posts](/search?do=process&provider=Member&searchuser=30695)

> [Quoting mikhaildgreat](/thread/post/223718#post223718 "View Quoted Post")
> 
> Disliked
> 
> Its a valid entry. MACD dipped below zero then went back up... read post #1 to get better understanding  
>    
>  -Mikhail  
>    
>  -Mikhail
> 
> Ignored

Good morning,  
  
Mikhail, thanks for your answer,   
  
According to post # 1 of THIS thread, it was a valid entry because it establishes one situation OR the other to get in the trade, that is a yellow line cross OR a MACD cross. having said that,  
I believe that the trade should be based on a yellow line cross as 1st scenario and basic condition and the MACD cross as a confirmation to finally trigger the order.   
Post # 1 of POURIA Method Thread by FOREXPERT says:  
  
"SHORT: when the yellow line crosses the 2 red lines downward and get the confirmation from the MACD it has to be downward too  
LONG: when the yellow line crosses the 2 red lines upward and get the confirmation from the MACD it has to be upward too"  
  
I could have misunderstood, but I don't know if the system based in one situation OR the other can get the same result. Maybe we should ask Forexpert. What do you think?  
  
Back in a few minutes with overnight results...  
  
Thanks 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#317](/thread/post/224100#post224100 "Post Permalink")

  * Feb 21, 2007 11:01pm  Feb 21, 2007 11:01pm 

  * [ BearPaw](bearpaw)

  * | Joined Jul 2006  | Status: A Trader for Life | [218 Posts](/search?do=process&provider=Member&searchuser=13999)

Forexpert...or anyone for that matter...  
  
GBPUSD seems to be a big loser for me....Here are my results with that pair since February 12th....  
  
Feb 12th -- 2 trades ---+20, +20  
Feb 13th--4 trades-----+20, -20, +20, +20  
Feb 15th---2 trades----(-20), -20  
Feb 20th---3 trades----(change stop loss to 50)-50, -50, +20  
Feb 21st---2 trades----+20, -50  
  
Net for GBP.....13 trades....6 profitable, 7 unprofitable  
Net return = -110 pips  
  
Any ideas from anyone would help me out.....  
  
BP 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#318](/thread/post/224129#post224129 "Post Permalink")

  * Feb 21, 2007 11:25pm  Feb 21, 2007 11:25pm 

  * [ timntools](timntools)

  * | Joined Dec 2006  | Status: Trader | [17 Posts](/search?do=process&provider=Member&searchuser=27197)

I received a bad signal on the usd/chf last night...  
  
but its there on all versions...anyone else get this? 

Attached Image

![](/attachment/image/23114?d=1172067877)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#319](/thread/post/224156#post224156 "Post Permalink")

  * Feb 21, 2007 11:39pm  Feb 21, 2007 11:39pm 

  * [ ghamal](ghamal)

  * | Joined Dec 2006  | Status: Trader | [23 Posts](/search?do=process&provider=Member&searchuser=27492)

Hi Mikaihl, i tried upgrading to1.4 but I get an X instead of a smiley face on the expert. Not sure if its working proper or not. Here is the log:  
  
2007.02.21 09:36:27 Pouria EA V-1.4 GBPUSD,H1: initialized  
2007.02.21 09:36:27 Pouria EA V-1.4 USDJPY,H1: initialized  
2007.02.21 09:36:27 Pouria EA V-1.4 AUDUSD,H1: initialized  
2007.02.21 09:36:27 Pouria EA V-1.4 USDCAD,H1: initialized  
2007.02.21 09:36:27 Pouria EA V-1.4 EURUSD,H1: initialized  

2007.02.21 09:36:19 Pouria EA V-1.4 USDCAD,H1: loaded successfully  

2007.02.21 09:36:19 Pouria EA V-1.4 AUDUSD,H1: loaded successfully  

2007.02.21 09:36:19 Pouria EA V-1.4 USDJPY,H1: loaded successfully  

2007.02.21 09:36:19 Pouria EA V-1.4 GBPUSD,H1: loaded successfully  

2007.02.21 09:36:19 Pouria EA V-1.4 USDCHF,H1: loaded successfully  

2007.02.21 09:36:19 Pouria EA V-1.4 EURUSD,H1: loaded successfully 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#320](/thread/post/224168#post224168 "Post Permalink")

  * Feb 21, 2007 11:47pm  Feb 21, 2007 11:47pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30695_4.gif) toti1972](toti1972)

  * | Joined Jan 2007  | Status: Trader | [107 Posts](/search?do=process&provider=Member&searchuser=30695)

Here my results last night...  
  
USD/CHF + 10 (post # 310)  
EUR/JPY + 15  
USD/CHF - 20 (wrong entry, a different one, not the one posted on # 310 which was already discussed)  
EUR/JPY + 15 (2nd entry for this pair, not clear cross though)  
  
AUD/USD - 40   
EUR/GBP - 20  
EUR/CHF + 20  
  
Opened a few min ago...  
  
USD/CAN: quick TP + 20  
  
still open EUR/USD : - 8   
  
Regards 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * The Pouria EA Development Thread
  *   * [ **Reply to Thread** ](/thread/17242-the-pouria-ea-development-thread/reply#reply)

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

[The Pouria Method](/thread/17011-the-pouria-method "OKay here is one of the 4 best systems that I've made and used, with this system I pickup atleast 50 pips a day, I'm sharing this because...") 562 replies

[Lessons Learned during System Development](/thread/2986-lessons-learned-during-system-development "Hi, 
  
I've been reading through the forum and somehow I'm in the process of developing my own system.. But not really doing actual...") 29 replies

[(pouria method II on the test)](/thread/23104-pouria-method-ii-on-the-test "Hello  
pouria method II is now DONE thanks to the group of experts and mathematicians that helped and made this method. 
now we are...") 218 replies

[System Development Secrets](/thread/7342-system-development-secrets "&lt;meta http-equiv=&quot;CONTENT-TYPE&quot; content=&quot;text/html; charset=utf-8&quot;&gt;&lt;title&gt;&lt;/title&gt;&lt;meta name=&quot;GENERATOR&quot; content=&quot;OpenOffice.org 2.0 ...") 5 replies

[Metatrader 4 Development Course](/thread/5906-metatrader-4-development-course "Here is the Mql_4_Metatrader_4_Development_Course in pdf \(link fixed\) : 
 
http://www.freefilehosting.org/pupload/view/8711") 3 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/17242-the-pouria-ea-development-thread/reply#reply)
  * Subscribe
  * [45](javascript:void\(0\);)

Attachments: The Pouria EA Development Thread

Tags: The Pouria EA Development Thread

#  [](/thread/17242-the-pouria-ea-development-thread)The Pouria EA Development Thread 

  * 

  * [#321](/thread/post/224173#post224173 "Post Permalink")

  * Feb 21, 2007 11:50pm  Feb 21, 2007 11:50pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar19504_4.gif) 1Sundevil](1sundevil)

  * | Joined Sep 2006  | Status: Trader | [228 Posts](/search?do=process&provider=Member&searchuser=19504)

Well, the original demo account is still showing very promising results with beta3. A few trades were opened and closed last night.  
  
I am now 21 for 23 for +213 pips.  
  
What is sttange is that I have two different demo's running the same beta3 and they are getting different entry signals. In the new demo I'm 2 for 5 for -120 pips. So I'm not sure what to do now. I'll keep both open and active and we'll see what happens. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#322](/thread/post/224178#post224178 "Post Permalink")

  * Feb 21, 2007 11:57pm  Feb 21, 2007 11:57pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar25698_4.gif) mikhaildgreat](mikhaildgreat)

  * | Joined Nov 2006  | Status: EA Programmer | [298 Posts](/search?do=process&provider=Member&searchuser=25698)

> [Quoting toti1972](/thread/post/224029#post224029 "View Quoted Post")
> 
> Disliked
> 
> Good morning,  
>    
>  Mikhail, thanks for your answer,   
>    
>  According to post # 1 of THIS thread, it was a valid entry because it establishes one situation OR the other to get in the trade, that is a yellow line cross OR a MACD cross. having said that,  
>  I believe that the trade should be based on a yellow line cross as 1st scenario and basic condition and the MACD cross as a confirmation to finally trigger the order.   
>  Post # 1 of POURIA Method Thread by FOREXPERT says:  
>    
>  "SHORT: when the yellow line crosses the 2 red lines downward and get the confirmation from the MACD it has to be downward too  
>  LONG: when the yellow line crosses the 2 red lines upward and get the confirmation from the MACD it has to be upward too"  
>    
>  I could have misunderstood, but I don't know if the system based in one situation OR the other can get the same result. Maybe we should ask Forexpert. What do you think?  
>    
>  Back in a few minutes with overnight results...  
>    
>  Thanks
> 
> Ignored

Hi Toti,  
  
Here you go, This EA Attached do not put equal weight on the MACD and the MAs. So here is how it will work. It will only trade when MA cross and there is an immediate confirmation from MACD. if there is none the trade will be skipped by the EA. this will significantly reduce the number of trades... which could be good or bad...   
  
Enjoy.  
Mikhail 

Attached File(s)

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [Pouria EA Cross Dependent.mq4](/attachment/file/23120?d=1172069848) 23 KB | 519 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#323](/thread/post/224182#post224182 "Post Permalink")

  * Feb 22, 2007 12:00am  Feb 22, 2007 12:00am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar25698_4.gif) mikhaildgreat](mikhaildgreat)

  * | Joined Nov 2006  | Status: EA Programmer | [298 Posts](/search?do=process&provider=Member&searchuser=25698)

> [Quoting 1Sundevil](/thread/post/224173#post224173 "View Quoted Post")
> 
> Disliked
> 
> Well, the original demo account is still showing very promising results with beta3. A few trades were opened and closed last night.  
>    
>  I am now 21 for 23 for +213 pips.  
>    
>  What is sttange is that I have two different demo's running the same beta3 and they are getting different entry signals. In the new demo I'm 2 for 5 for -120 pips. So I'm not sure what to do now. I'll keep both open and active and we'll see what happens.
> 
> Ignored

This could be the case because different brokers use different data feeds. try to attached the MAs on the chart you will find different cross times from different brokers...  
  
-Mikhail 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#324](/thread/post/224190#post224190 "Post Permalink")

  * Feb 22, 2007 12:11am  Feb 22, 2007 12:11am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30695_4.gif) toti1972](toti1972)

  * | Joined Jan 2007  | Status: Trader | [107 Posts](/search?do=process&provider=Member&searchuser=30695)

Mikhail, as always, lot of thanks for your efforts...  
  
I believe the essence of the methods is this, at least that is what I understand from Post # 1, even though it may reduce the trades, looks that could be safer. In any case it is every trader's style, what finally determine which one to use.   
Aside of that, I would like to hear different points of view regarding the interpretation of original rules.  
  
Regards 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#325](/thread/post/224211#post224211 "Post Permalink")

  * Feb 22, 2007 12:33am  Feb 22, 2007 12:33am 

  * [ BearPaw](bearpaw)

  * | Joined Jul 2006  | Status: A Trader for Life | [218 Posts](/search?do=process&provider=Member&searchuser=13999)

> [Quoting toti1972](/thread/post/224168#post224168 "View Quoted Post")
> 
> Disliked
> 
> Here my results last night...  
>    
>  USD/CHF + 10 (post # 310)  
>  EUR/JPY + 15  
>  USD/CHF - 20 (wrong entry, a different one, not the one posted on # 310 which was already discussed)  
>  EUR/JPY + 15 (2nd entry for this pair, not clear cross though)  
>    
>  AUD/USD - 40   
>  EUR/GBP - 20  
>  EUR/CHF + 20  
>    
>  Opened a few min ago...  
>    
>  USD/CAN: quick TP + 20  
>    
>  still open EUR/USD : - 8   
>    
>  Regards
> 
> Ignored

Toti,  
  
My results....seem to be kinda like yours???  
  
EurJPY +15  
EURJPY -50  
EURJPY +14  
GBPUSD +20  
AUDUSD +10  
USDCHF +10  
EURUSD +15  
GBPUSD -50  
USDCAN +20  
  
Still open EURUSD right around BE.  
  
BP 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#326](/thread/post/224304#post224304 "Post Permalink")

  * Feb 22, 2007 1:46am  Feb 22, 2007 1:46am 

  * [ BearPaw](bearpaw)

  * | Joined Jul 2006  | Status: A Trader for Life | [218 Posts](/search?do=process&provider=Member&searchuser=13999)

> [Quoting mikhaildgreat](/thread/post/224182#post224182 "View Quoted Post")
> 
> Disliked
> 
> This could be the case because different brokers use different data feeds. try to attached the MAs on the chart you will find different cross times from different brokers...  
>    
>  -Mikhail
> 
> Ignored

Mikhail,  
  
One other setting question...do we only need to worry about "AccountisMicro" if we are using MoneyManagement?  
  
Otherwise, what is that for...so we can use sublots? Like 1.4 standard lots?  
  
Thanks,  
  
BP 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#327](/thread/post/224306#post224306 "Post Permalink")

  * Feb 22, 2007 1:47am  Feb 22, 2007 1:47am 

  * [ BearPaw](bearpaw)

  * | Joined Jul 2006  | Status: A Trader for Life | [218 Posts](/search?do=process&provider=Member&searchuser=13999)

> [Quoting ghamal](/thread/post/224156#post224156 "View Quoted Post")
> 
> Disliked
> 
> Hi Mikaihl, i tried upgrading to1.4 but I get an X instead of a smiley face on the expert. Not sure if its working proper or not. Here is the log:  
>    
>  2007.02.21 09:36:27 Pouria EA V-1.4 GBPUSD,H1: initialized  
>  2007.02.21 09:36:27 Pouria EA V-1.4 USDJPY,H1: initialized  
>  2007.02.21 09:36:27 Pouria EA V-1.4 AUDUSD,H1: initialized  
>  2007.02.21 09:36:27 Pouria EA V-1.4 USDCAD,H1: initialized  
>  2007.02.21 09:36:27 Pouria EA V-1.4 EURUSD,H1: initialized  

>  2007.02.21 09:36:19 Pouria EA V-1.4 USDCAD,H1: loaded successfully  

>  2007.02.21 09:36:19 Pouria EA V-1.4 AUDUSD,H1: loaded successfully  

>  2007.02.21 09:36:19 Pouria EA V-1.4 USDJPY,H1: loaded successfully  

>  2007.02.21 09:36:19 Pouria EA V-1.4 GBPUSD,H1: loaded successfully  

>  2007.02.21 09:36:19 Pouria EA V-1.4 USDCHF,H1: loaded successfully  

>  2007.02.21 09:36:19 Pouria EA V-1.4 EURUSD,H1: loaded successfully
> 
> Ignored

Ghamal,   
  
You have to enable expert advisors in the main toolbar as well. In each pair you need to check live trading, then on the main tool bar, enable expert advisors. Once you do that the X's will turn to smiley faces.  
  
BP 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#328](/thread/post/224314#post224314 "Post Permalink")

  * Feb 22, 2007 2:02am  Feb 22, 2007 2:02am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar25698_4.gif) mikhaildgreat](mikhaildgreat)

  * | Joined Nov 2006  | Status: EA Programmer | [298 Posts](/search?do=process&provider=Member&searchuser=25698)

> [Quoting BearPaw](/thread/post/224304#post224304 "View Quoted Post")
> 
> Disliked
> 
> Mikhail,  
>    
>  One other setting question...do we only need to worry about "AccountisMicro" if we are using MoneyManagement?  
>    
>  Otherwise, what is that for...so we can use sublots? Like 1.4 standard lots?  
>    
>  Thanks,  
>    
>  BP
> 
> Ignored

Some Brokers do not allow 0.01 lots, if account is micro is set to false minimum lot will be 0.1 if true 0.01 will be the minimum lot. because if your broker does not allow the lot size you want to open order will be rejected...  
  
-Mikhail 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#329](/thread/post/224321#post224321 "Post Permalink")

  * Feb 22, 2007 2:10am  Feb 22, 2007 2:10am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar19504_4.gif) 1Sundevil](1sundevil)

  * | Joined Sep 2006  | Status: Trader | [228 Posts](/search?do=process&provider=Member&searchuser=19504)

One pattern I'm definitely seeing, when it comes to bad trades, is that they are entered right after a large spike, which then slowly moves in the opposite direction.   
  
Obviously this is a case of "news", but is there a way to fix this for those that truly want the EA to trade without them having to watch the computer all day and night? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#330](/thread/post/224334#post224334 "Post Permalink")

  * Feb 22, 2007 2:24am  Feb 22, 2007 2:24am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar22836_4.gif) ilanr](ilanr)

  * | Joined Oct 2006  | Status: Trader | [260 Posts](/search?do=process&provider=Member&searchuser=22836)

Two strange positions (GBPUSD and EURUSD) were opened today by version 1.4. I wasn't near the monitor when it happened, but what I can see now is that at 08:42 Eastern time, when the price at both charts was 17 p. BELOW the slow MA's and the fast MA was also BELOW the slow MA's - two LONG positions were opened. Any ideas, what might have caused this? 

sans peur et sans reproche

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#331](/thread/post/224358#post224358 "Post Permalink")

  * Feb 22, 2007 2:46am  Feb 22, 2007 2:46am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar25698_4.gif) mikhaildgreat](mikhaildgreat)

  * | Joined Nov 2006  | Status: EA Programmer | [298 Posts](/search?do=process&provider=Member&searchuser=25698)

> [Quoting 1Sundevil](/thread/post/224321#post224321 "View Quoted Post")
> 
> Disliked
> 
> One pattern I'm definitely seeing, when it comes to bad trades, is that they are entered right after a large spike, which then slowly moves in the opposite direction.   
>    
>  Obviously this is a case of "news", but is there a way to fix this for those that truly want the EA to trade without them having to watch the computer all day and night?
> 
> Ignored

set confirmonentry = true, to avoid this nasty spikes. But the problem with this is that you will also be entering the trade a little later...  
  
hope that helps,  
Mikhail 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#332](/thread/post/224376#post224376 "Post Permalink")

  * Feb 22, 2007 3:09am  Feb 22, 2007 3:09am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar19504_4.gif) 1Sundevil](1sundevil)

  * | Joined Sep 2006  | Status: Trader | [228 Posts](/search?do=process&provider=Member&searchuser=19504)

> [Quoting mikhaildgreat](/thread/post/224358#post224358 "View Quoted Post")
> 
> Disliked
> 
> set confirmonentry = true, to avoid this nasty spikes. But the problem with this is that you will also be entering the trade a little later...  
>    
>  hope that helps,  
>  Mikhail
> 
> Ignored

I just checked..it already is set to "true". Here are two entries that I'm talking about. 

Attached Image

![](/attachment/image/23139?d=1172081371)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#333](/thread/post/224391#post224391 "Post Permalink")

  * Feb 22, 2007 3:25am  Feb 22, 2007 3:25am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar25698_4.gif) mikhaildgreat](mikhaildgreat)

  * | Joined Nov 2006  | Status: EA Programmer | [298 Posts](/search?do=process&provider=Member&searchuser=25698)

if thats the case nothing can be done at the moment. the market is whipsawing all over the place, specially GBPUSD. not good for many MA based strategy...  
  
by the way, during your whole forward test did you have confirmonetry = true;? I ask because you have the best forward test results compared to everyone else...  
  
Regards,  
  
Mikhail 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#334](/thread/post/224393#post224393 "Post Permalink")

  * Feb 22, 2007 3:26am  Feb 22, 2007 3:26am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar19504_4.gif) 1Sundevil](1sundevil)

  * | Joined Sep 2006  | Status: Trader | [228 Posts](/search?do=process&provider=Member&searchuser=19504)

> [Quoting mikhaildgreat](/thread/post/224391#post224391 "View Quoted Post")
> 
> Disliked
> 
> if thats the case nothing can be done at the moment. the market is whipsawing all over the place, specially GBPUSD. not good fo rnay MA based strategy...  
>    
>  by the way, during your whole forward test did you have confirmonetry = true;? I ask because you have the best forward test results compared to everyone else...  
>    
>  Regards,  
>    
>  Mikhail
> 
> Ignored

Yes, it was always set to true. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#335](/thread/post/224394#post224394 "Post Permalink")

  * Feb 22, 2007 3:26am  Feb 22, 2007 3:26am 

  * [ ghamal](ghamal)

  * | Joined Dec 2006  | Status: Trader | [23 Posts](/search?do=process&provider=Member&searchuser=27492)

> [Quoting BearPaw](/thread/post/224306#post224306 "View Quoted Post")
> 
> Disliked
> 
> Ghamal,   
>    
>  You have to enable expert advisors in the main toolbar as well. In each pair you need to check live trading, then on the main tool bar, enable expert advisors. Once you do that the X's will turn to smiley faces.  
>    
>  BP
> 
> Ignored

Thanks BearPaw, I wil do so. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#336](/thread/post/224607#post224607 "Post Permalink")

  * Feb 22, 2007 8:20am  Feb 22, 2007 8:20am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar14103_16.gif) ut2DaMax](ut2damax)

  * | Joined Jul 2006  | Status: Trader | [592 Posts](/search?do=process&provider=Member&searchuser=14103)

**MACD ... 3,9,1 works a lot better** MACD ... 3,9,1 works a lot better for this Method. Try it ..... tell me what you think. IMO 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#337](/thread/post/224609#post224609 "Post Permalink")

  * Feb 22, 2007 8:34am  Feb 22, 2007 8:34am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar19504_4.gif) 1Sundevil](1sundevil)

  * | Joined Sep 2006  | Status: Trader | [228 Posts](/search?do=process&provider=Member&searchuser=19504)

> [Quoting ut2DaMax](/thread/post/224607#post224607 "View Quoted Post")
> 
> Disliked
> 
> **MACD ... 3,9,1 works a lot better** MACD ... 3,9,1 works a lot better for this Method. Try it ..... tell me what you think. IMO
> 
> Ignored

What kind of results are you getting? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#338](/thread/post/224615#post224615 "Post Permalink")

  * Feb 22, 2007 8:59am  Feb 22, 2007 8:59am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar14103_16.gif) ut2DaMax](ut2damax)

  * | Joined Jul 2006  | Status: Trader | [592 Posts](/search?do=process&provider=Member&searchuser=14103)

add MV .... 30/35 - 50/55   
  
Gives you a lot more times you can trade. IMO 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#339](/thread/post/224618#post224618 "Post Permalink")

  * Feb 22, 2007 9:03am  Feb 22, 2007 9:03am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar14103_16.gif) ut2DaMax](ut2damax)

  * | Joined Jul 2006  | Status: Trader | [592 Posts](/search?do=process&provider=Member&searchuser=14103)

> [Quoting 1Sundevil](/thread/post/224609#post224609 "View Quoted Post")
> 
> Disliked
> 
> What kind of results are you getting?
> 
> Ignored

  
I am getting better results trading this manually.   
  
  
Just something for you all to try and see if you like it. I am hoping the newer versions incorporates this as well. But you can adjust the moving averages to what works best for you. I do not think this is a dead end. I think the Method can evolve to a working system. Just my 2 cents ..... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#340](/thread/post/225101#post225101 "Post Permalink")

  * Feb 22, 2007 9:29pm  Feb 22, 2007 9:29pm 

  * [ BearPaw](bearpaw)

  * | Joined Jul 2006  | Status: A Trader for Life | [218 Posts](/search?do=process&provider=Member&searchuser=13999)

Well, another day has passed and Forexpert has not been able to give any advice concerning the gbpusd trade.  
  
Another day means another GBPUSD trade that is -50 in the hole.  
  
So, 2 options...1) change the timeframe on the chart for the GBPUSD. 2) stop trading the GBPUSD pair.  
  
I am open to suggestions from anyone on this matter.  
  
Thoughts?  
  
BP 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * The Pouria EA Development Thread
  *   * [ **Reply to Thread** ](/thread/17242-the-pouria-ea-development-thread/reply#reply)

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

[The Pouria Method](/thread/17011-the-pouria-method "OKay here is one of the 4 best systems that I've made and used, with this system I pickup atleast 50 pips a day, I'm sharing this because...") 562 replies

[Lessons Learned during System Development](/thread/2986-lessons-learned-during-system-development "Hi, 
  
I've been reading through the forum and somehow I'm in the process of developing my own system.. But not really doing actual...") 29 replies

[(pouria method II on the test)](/thread/23104-pouria-method-ii-on-the-test "Hello  
pouria method II is now DONE thanks to the group of experts and mathematicians that helped and made this method. 
now we are...") 218 replies

[System Development Secrets](/thread/7342-system-development-secrets "&lt;meta http-equiv=&quot;CONTENT-TYPE&quot; content=&quot;text/html; charset=utf-8&quot;&gt;&lt;title&gt;&lt;/title&gt;&lt;meta name=&quot;GENERATOR&quot; content=&quot;OpenOffice.org 2.0 ...") 5 replies

[Metatrader 4 Development Course](/thread/5906-metatrader-4-development-course "Here is the Mql_4_Metatrader_4_Development_Course in pdf \(link fixed\) : 
 
http://www.freefilehosting.org/pupload/view/8711") 3 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/17242-the-pouria-ea-development-thread/reply#reply)
  * Subscribe
  * [45](javascript:void\(0\);)

Attachments: The Pouria EA Development Thread

Tags: The Pouria EA Development Thread

#  [](/thread/17242-the-pouria-ea-development-thread)The Pouria EA Development Thread 

  * 

  * [#341](/thread/post/225193#post225193 "Post Permalink")

  * Feb 22, 2007 11:03pm  Feb 22, 2007 11:03pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30695_4.gif) toti1972](toti1972)

  * | Joined Jan 2007  | Status: Trader | [107 Posts](/search?do=process&provider=Member&searchuser=30695)

I am still open USD/CAD 1.1614 from yesterday noon  
My TP is 1.1594  
  
It is unbelievable that yesterday and today, the market reached 1.1595 and 1.1596 several times and then back up  
  
Now is 1.1611...pretty cool uhh??  
  
What is the name of this damn game?????  
  
just a funny comment... ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#342](/thread/post/225252#post225252 "Post Permalink")

  * Feb 22, 2007 11:51pm  Feb 22, 2007 11:51pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar19504_4.gif) 1Sundevil](1sundevil)

  * | Joined Sep 2006  | Status: Trader | [228 Posts](/search?do=process&provider=Member&searchuser=19504)

> [Quoting BearPaw](/thread/post/225101#post225101 "View Quoted Post")
> 
> Disliked
> 
> Well, another day has passed and Forexpert has not been able to give any advice concerning the gbpusd trade.  
>    
>  Another day means another GBPUSD trade that is -50 in the hole.  
>    
>  So, 2 options...1) change the timeframe on the chart for the GBPUSD. 2) stop trading the GBPUSD pair.  
>    
>  I am open to suggestions from anyone on this matter.  
>    
>  Thoughts?  
>    
>  BP
> 
> Ignored

I've noticed that I'm getting excellent results with the MIG demo, and terrible results with Interbank.  
  
USDCAD trade closed for +15.  
  
So 22 for 24 (MIG), +228 pips.   
  
What is strange though is that some positive trades disappear yet my account balance is correct (MIG). Right now it states that my "account balance" is $54,216.76 (an increase of 8.4%). Yet the "profit/loss" is only at $2,806.76. Where did the other $1,410 go? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#343](/thread/post/225258#post225258 "Post Permalink")

  * Feb 22, 2007 11:54pm  Feb 22, 2007 11:54pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar19504_4.gif) 1Sundevil](1sundevil)

  * | Joined Sep 2006  | Status: Trader | [228 Posts](/search?do=process&provider=Member&searchuser=19504)

> [Quoting toti1972](/thread/post/225193#post225193 "View Quoted Post")
> 
> Disliked
> 
> I am still open USD/CAD 1.1614 from yesterday noon  
>  My TP is 1.1594  
>    
>  It is unbelievable that yesterday and today, the market reached 1.1595 and 1.1596 several times and then back up  
>    
>  Now is 1.1611...pretty cool uhh??  
>    
>  What is the name of this damn game?????  
>    
>  just a funny comment... ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)
> 
> Ignored

My USDCAD was opened at 1636 and TP was taken at 1621. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#344](/thread/post/225272#post225272 "Post Permalink")

  * Feb 23, 2007 12:03am  Feb 23, 2007 12:03am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar19504_4.gif) 1Sundevil](1sundevil)

  * | Joined Sep 2006  | Status: Trader | [228 Posts](/search?do=process&provider=Member&searchuser=19504)

> [Quoting 1Sundevil](/thread/post/225252#post225252 "View Quoted Post")
> 
> Disliked
> 
> I've noticed that I'm getting excellent results with the MIG demo, and terrible results with Interbank.  
>    
>  USDCAD trade closed for +15.  
>    
>  So 22 for 24 (MIG), +228 pips.
> 
> Ignored

EURJPY just closed for +15.  
  
Now, 23 for 25 for +243 pips (MIG)  
  
On the Interbank Demo I am **_3 for 7 for -130 pips_**. Not good at all. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#345](/thread/post/225295#post225295 "Post Permalink")

  * Feb 23, 2007 12:16am  Feb 23, 2007 12:16am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30695_4.gif) toti1972](toti1972)

  * | Joined Jan 2007  | Status: Trader | [107 Posts](/search?do=process&provider=Member&searchuser=30695)

> [Quoting 1Sundevil](/thread/post/225258#post225258 "View Quoted Post")
> 
> Disliked
> 
> My USDCAD was opened at 1636 and TP was taken at 1621.
> 
> Ignored

I got your trade too, and was closed 1621 but later it opens the current which gets me a little anxious...jeje, now is +4. didn't you get the 2nd CAD trade?  
BTW I am MIG demo too...  
  
Regards 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#346](/thread/post/225311#post225311 "Post Permalink")

  * Feb 23, 2007 12:36am  Feb 23, 2007 12:36am 

  * [ BearPaw](bearpaw)

  * | Joined Jul 2006  | Status: A Trader for Life | [218 Posts](/search?do=process&provider=Member&searchuser=13999)

> [Quoting 1Sundevil](/thread/post/225272#post225272 "View Quoted Post")
> 
> Disliked
> 
> EURJPY just closed for +15.  
>    
>  Now, 23 for 25 for +243 pips (MIG)  
>    
>  On the Interbank Demo I am **_3 for 7 for -130 pips_**. Not good at all.
> 
> Ignored

On the MIG demo, it opened up a:  
  
GBP Buy which was stopped out...same as my interbankfx account  
EurUSd buy which was also stopped out.....which my ibfx account did not open  
  
Did anyone else get this euro trade?  
  
BP 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#347](/thread/post/225318#post225318 "Post Permalink")

  * Feb 23, 2007 12:44am  Feb 23, 2007 12:44am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30695_4.gif) toti1972](toti1972)

  * | Joined Jan 2007  | Status: Trader | [107 Posts](/search?do=process&provider=Member&searchuser=30695)

> [Quoting BearPaw](/thread/post/225311#post225311 "View Quoted Post")
> 
> Disliked
> 
> On the MIG demo, it opened up a:  
>    
>  GBP Buy which was stopped out...same as my interbankfx account  
>  EurUSd buy which was also stopped out.....which my ibfx account did not open  
>    
>  Did anyone else get this euro trade?  
>    
>  BP
> 
> Ignored

Nop, none of them...  
I am MIG   
  
recent trades:  
  
EUR/JPY closed TP: + 15  
Still open USD/CAD  
  
Coming:  
  
GBP/USD (waiting MACD cross confirmation...) 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#348](/thread/post/225401#post225401 "Post Permalink")

  * Feb 23, 2007 1:43am  Feb 23, 2007 1:43am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar19504_4.gif) 1Sundevil](1sundevil)

  * | Joined Sep 2006  | Status: Trader | [228 Posts](/search?do=process&provider=Member&searchuser=19504)

> [Quoting BearPaw](/thread/post/225311#post225311 "View Quoted Post")
> 
> Disliked
> 
> On the MIG demo, it opened up a:  
>    
>  GBP Buy which was stopped out...same as my interbankfx account  
>  EurUSd buy which was also stopped out.....which my ibfx account did not open  
>    
>  Did anyone else get this euro trade?  
>    
>  BP
> 
> Ignored

Something strange just happened. Both MIG and Interbank opened up a GBPUSD buy trade.  
  
MIG opened at 9582 (currently negative), but this time Interbank opened at 9558 and closed at 9568 for +10. Strange that two accounts using the same beat3 would get different signals. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#349](/thread/post/225479#post225479 "Post Permalink")

  * Feb 23, 2007 2:29am  Feb 23, 2007 2:29am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar19504_4.gif) 1Sundevil](1sundevil)

  * | Joined Sep 2006  | Status: Trader | [228 Posts](/search?do=process&provider=Member&searchuser=19504)

> [Quoting 1Sundevil](/thread/post/225401#post225401 "View Quoted Post")
> 
> Disliked
> 
> Something strange just happened. Both MIG and Interbank opened up a GBPUSD buy trade.  
>    
>  MIG opened at 9582 (currently negative), but this time Interbank opened at 9558 and closed at 9568 for +10. Strange that two accounts using the same beat3 would get different signals.
> 
> Ignored

MIG GBP trade closed for +15. Now, 24 of 26 for +258 pips. No other trades open right now.  
  
Interbank has me in two trades, both slightly negative, EURUSD and USDCHF. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#350](/thread/post/225702#post225702 "Post Permalink")

  * Feb 23, 2007 5:48am  Feb 23, 2007 5:48am 

  * [ winsteadglenn](winsteadglenn)

  * | Joined Nov 2006  | Status: Trader | [330 Posts](/search?do=process&provider=Member&searchuser=25826)

MACD 3,9,1.  
MA 50/55.  
running MACD dependent format.  
  
Glenn 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#351](/thread/post/226089#post226089 "Post Permalink")

  * Feb 23, 2007 4:36pm  Feb 23, 2007 4:36pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar28980_4.gif) anthonyrae](anthonyrae)

  * | Joined Dec 2006  | Status: Trader | [68 Posts](/search?do=process&provider=Member&searchuser=28980)

Hello,

  

I was back testing Pouria EA v1.4(thanks Mikhaild!!!) and it seems that it missed a trade on the 13th of Feb. See the picture where the MA's cross. Is it because the MACD has crossed at exactly the same time ? (or does this not make a difference?)  
  
This happened when the settings for MACDFiler = true and ConfirmedOnEntry = false.  
  
But when I changed MACDFiler to false, the EA makes a trade on this cross.  
  
The EA makes less trade with MACDfiler to false, but these trades are more profitable. But it seems to have missed this trade, which would have been very profitable !  
  
Is this a bug or not ? - anyone else notice things like this ?

  
Anthony 

Attached Image

![](/attachment/image/23344?d=1172215901)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#352](/thread/post/226476#post226476 "Post Permalink")

  * Feb 23, 2007 10:28pm  Feb 23, 2007 10:28pm 

  * [ BearPaw](bearpaw)

  * | Joined Jul 2006  | Status: A Trader for Life | [218 Posts](/search?do=process&provider=Member&searchuser=13999)

Wow guys,  
  
I am a little perplexed. I am getting different results on different accounts....  
  
I am using an IBFX live account, IBFX demo account, and MIG demo account. I think I am getting different triggers on every account!  
  
Let me outline below what has happened on each account...  
  
IBFX live account....  
  
Buy EURJPY 158.92 +15  
Buy GBPUSD 1.9558 +20  
Sell USDCAD 1.1624 +20  
  
Still Open  
  
Sell AUDUSD .7880  
Buy EURUSD 1.3133  
Buy EURJPY 159.58  
  
IBX-DEMO account  
  
Same as above except it also has another position still open  
  
Buy USDCHF 1.2411  
  
MIG-DEMO account  
  
Buy EURJPY 158.93 +15  
Buy GBPUSD 1.9559 +20  
(Missed the USDCAD for some reason)  
  
Still Open....  
  
Sell AUDUSD .7879  
Buy EURUSD 1.3133  
(Missed EURJPY entry that IBFX has)  
BUY USDCHF 1.2403 (Look at difference of this entry from IBFX Demo)  
Buy NZDUSD .7064 (This entry is not in either IBFX platform)  
  
Very interesting to me. Dont know if a live account and demo account at IBFX receive different feeds. Then MIG receives different feeds probably. But why the different entries if my settings on the EA are the same?  
  
Thoughts?  
  
BP 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#353](/thread/post/226494#post226494 "Post Permalink")

  * Feb 23, 2007 10:44pm  Feb 23, 2007 10:44pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar7129_7.gif) smjones](smjones)

  * Joined Mar 2006 | Status: THANK YOU MERLIN,TWEE and FF Team | [4,603 Posts](/search?do=process&provider=Member&searchuser=7129)

Yes, the live and demo feeds are different. For one thing, the demo never has a problem filling at a certain price, because the broker is not at risk, so it is just assumed that no matter where you place your order there will be liquidity to fill it. This is not always the case with a live trade. That can make a huge difference. Demos are good for getting a feel, but not for testing, as they are unrealistic, in regards to liquidity and orderflow. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#354](/thread/post/226570#post226570 "Post Permalink")

  * Feb 23, 2007 11:54pm  Feb 23, 2007 11:54pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30695_4.gif) toti1972](toti1972)

  * | Joined Jan 2007  | Status: Trader | [107 Posts](/search?do=process&provider=Member&searchuser=30695)

finally USD/CAD close for a profit (almost 2 days opened): +20  
  
a few minutes ago:  
  
buy EUR/USD : + 15  
sell USD/JPY : + 15  
sell USD/CHF : + 10  
  
today so far...: + 60  
  
to be considered:  
  
Didn't get a single loss since I moved my SL to 40 (10-0)= 150 PIPS (since wed noon)  
  
Regards. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#355](/thread/post/226609#post226609 "Post Permalink")

  * Feb 24, 2007 12:25am  Feb 24, 2007 12:25am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar19504_4.gif) 1Sundevil](1sundevil)

  * | Joined Sep 2006  | Status: Trader | [228 Posts](/search?do=process&provider=Member&searchuser=19504)

> [Quoting toti1972](/thread/post/226570#post226570 "View Quoted Post")
> 
> Disliked
> 
> finally USD/CAD close for a profit (almost 2 days opened): +20  
>    
>  a few minutes ago:  
>    
>  buy EUR/USD : + 15  
>  sell USD/JPY : + 15  
>  sell USD/CHF : + 10  
>    
>  today so far...: + 60  
>    
>  to be considered:  
>    
>  Didn't get a single loss since I moved my SL to 40 (10-0)= 150 PIPS (since wed noon)  
>    
>  Regards.
> 
> Ignored

I also had a good night. When I went to sleep MIG had two trades open, EURUSD and USDCHF, and both were negative about 15 pips a piece. When I woke I found that both closed for +15 and the EA had opened two more, USDJPY and USDCHF, which also each c losed for +15.  
  
Now, 28 of 30 for 318 pips. The MIG account is up 15.5%. No other trades open right now. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#356](/thread/post/226655#post226655 "Post Permalink")

  * Edited 7:05am  Feb 24, 2007 1:01am | Edited 7:05am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30695_4.gif) toti1972](toti1972)

  * | Joined Jan 2007  | Status: Trader | [107 Posts](/search?do=process&provider=Member&searchuser=30695)

sell EUR/CHF open @ 10:00 EST  
closed @ 10:20 EST profit: +15  
  
Today: + 75  
  
That's all for this week 11-0   
  
still open: long EUR/JPY currently -6   
  
I find no reason to close that trade, so i decided to carry to next week.  
  
You all guys have a happy weekend... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#357](/thread/post/226948#post226948 "Post Permalink")

  * Feb 24, 2007 7:29am  Feb 24, 2007 7:29am 

  * [ Askjo](askjo)

  * | Joined Oct 2005  | Status: Trader | [57 Posts](/search?do=process&provider=Member&searchuser=4185)

I follwed the instruction on the pouria method. I also followed other instruction on the same method. I used demo trading for testing this method. My results showed the difference between 2 instructions.   
  
I traded 2 same pairs on **30 minutes** chart: EUR/USD, but the difference is stop loss: 20 pips vs 50 pips.  
  
2/21/07 time: 6.56 am. Stop loss is **20 pips**  
  
Sell  
  
1.3127   
  
Closed time: 8:16 am  
  
1.3147  
  
**Loss** : 20 pips  
  
2/**21** /07 time: 6.58 am. Stop loss is **50 pips**.  
  
Sell  
  
1.3130  
  
Closed 2/**22** /07 time 2:38 am.  
  
1.3106  
  
**Profit** ; 24 pips.  
  
I took profits: 4 pts.  
  
Any thoughts?

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#358](/thread/post/228280#post228280 "Post Permalink")

  * Feb 26, 2007 10:56pm  Feb 26, 2007 10:56pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30695_4.gif) toti1972](toti1972)

  * | Joined Jan 2007  | Status: Trader | [107 Posts](/search?do=process&provider=Member&searchuser=30695)

last night I got 1-1, that makes and overall result of 11-1 since wed last week  
  
EUR/JPY: buy 159.44 SL: 159.04 : -40  
EUR/JPY: sell 158.96 TP: 158.81 :+15  
  
still open: buy EUR/GBP: -10   
  
this week: -25  
  
So far : 165 - 25 = 140 PIPS   
  
Regards 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#359](/thread/post/228416#post228416 "Post Permalink")

  * Feb 27, 2007 1:11am  Feb 27, 2007 1:11am 

  * [ Easy4xTrading](easy4xtrading)

  * | Joined Jan 2007  | Status: Trader | [17 Posts](/search?do=process&provider=Member&searchuser=31330)

Last night I had only one sell eur/jpy @ 159.22 TP @ 158.92  
  
EZ 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#360](/thread/post/228485#post228485 "Post Permalink")

  * Feb 27, 2007 2:06am  Feb 27, 2007 2:06am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar19504_4.gif) 1Sundevil](1sundevil)

  * | Joined Sep 2006  | Status: Trader | [228 Posts](/search?do=process&provider=Member&searchuser=19504)

> [Quoting BearPaw](/thread/post/226476#post226476 "View Quoted Post")
> 
> Disliked
> 
> Wow guys,  
>    
>  I am a little perplexed. I am getting different results on different accounts....
> 
> Ignored

I am also experiencing that. I have both Interbank and MIG demo accounts open. Yesterday I had a GBPUSD buy triggered on each.   
  
MIG bought at 9633  
INT bought at 9646, 13 pips higher, which is not good. My MIG demo is doing much, much better than the INT demo is.  
  
INT just dropped me into a USDCHF buy trade (11 pips negative right now), which MIG hasn't triggered. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * The Pouria EA Development Thread
  *   * [ **Reply to Thread** ](/thread/17242-the-pouria-ea-development-thread/reply#reply)

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

[The Pouria Method](/thread/17011-the-pouria-method "OKay here is one of the 4 best systems that I've made and used, with this system I pickup atleast 50 pips a day, I'm sharing this because...") 562 replies

[Lessons Learned during System Development](/thread/2986-lessons-learned-during-system-development "Hi, 
  
I've been reading through the forum and somehow I'm in the process of developing my own system.. But not really doing actual...") 29 replies

[(pouria method II on the test)](/thread/23104-pouria-method-ii-on-the-test "Hello  
pouria method II is now DONE thanks to the group of experts and mathematicians that helped and made this method. 
now we are...") 218 replies

[System Development Secrets](/thread/7342-system-development-secrets "&lt;meta http-equiv=&quot;CONTENT-TYPE&quot; content=&quot;text/html; charset=utf-8&quot;&gt;&lt;title&gt;&lt;/title&gt;&lt;meta name=&quot;GENERATOR&quot; content=&quot;OpenOffice.org 2.0 ...") 5 replies

[Metatrader 4 Development Course](/thread/5906-metatrader-4-development-course "Here is the Mql_4_Metatrader_4_Development_Course in pdf \(link fixed\) : 
 
http://www.freefilehosting.org/pupload/view/8711") 3 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/17242-the-pouria-ea-development-thread/reply#reply)
  * Subscribe
  * [45](javascript:void\(0\);)

Attachments: The Pouria EA Development Thread

Tags: The Pouria EA Development Thread

#  [](/thread/17242-the-pouria-ea-development-thread)The Pouria EA Development Thread 

  * 

  * [#361](/thread/post/228490#post228490 "Post Permalink")

  * Feb 27, 2007 2:10am  Feb 27, 2007 2:10am 

  * [ Easy4xTrading](easy4xtrading)

  * | Joined Jan 2007  | Status: Trader | [17 Posts](/search?do=process&provider=Member&searchuser=31330)

Interbank has not put me in anything at the present!!  
  
EZ 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#362](/thread/post/228501#post228501 "Post Permalink")

  * Feb 27, 2007 2:24am  Feb 27, 2007 2:24am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar25698_4.gif) mikhaildgreat](mikhaildgreat)

  * | Joined Nov 2006  | Status: EA Programmer | [298 Posts](/search?do=process&provider=Member&searchuser=25698)

> [Quoting BearPaw](/thread/post/226476#post226476 "View Quoted Post")
> 
> Disliked
> 
> Wow guys,  
>    
>  I am a little perplexed. I am getting different results on different accounts....  
>    
>  I am using an IBFX live account, IBFX demo account, and MIG demo account. I think I am getting different triggers on every account!  
>    
>  BP
> 
> Ignored

  
If you think thats strange try doing this simple experiment, attach RSI indicator on the chart of different brokers, same currency, same TF same everything. Notice that no RSI in those brokers will have the same value. Now try doing that on the same broker but one on live account and the other in demo account, And you will still see different RSI values. ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)  
  
Hard to believe? Believe it! LOL!  
  
-Mikhail 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#363](/thread/post/228521#post228521 "Post Permalink")

  * Feb 27, 2007 2:57am  Feb 27, 2007 2:57am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar25698_4.gif) mikhaildgreat](mikhaildgreat)

  * | Joined Nov 2006  | Status: EA Programmer | [298 Posts](/search?do=process&provider=Member&searchuser=25698)

Hello Again,  
  
I was contemplating about the pouria method and I was thinking what is the significance of the 75,85 MA and why in the world is it applied to the Price_Low... Anyways it still remains a mystery to me, but I figured why not substitute 75,85 MAs with MAs with same period one applied to High the other to low. that way some sort channel is formed, there would somehow be some rational behind the system. By doing this we are trading channel breakout...  
  
I havnt tested this this is all theory right now but attached below is the graph of what I am talking about and the EA for experiment purposes.  
  
-Mikhail 

Attached Image

![](/attachment/image/23629?d=1172512583)

Attached File(s)

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [Pouria EA Beta H-L.mq4](/attachment/file/23630?d=1172512604) 12 KB | 525 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#364](/thread/post/228533#post228533 "Post Permalink")

  * Feb 27, 2007 3:17am  Feb 27, 2007 3:17am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar19504_4.gif) 1Sundevil](1sundevil)

  * | Joined Sep 2006  | Status: Trader | [228 Posts](/search?do=process&provider=Member&searchuser=19504)

> [Quoting mikhaildgreat](/thread/post/228521#post228521 "View Quoted Post")
> 
> Disliked
> 
> Hello Again,  
>    
>  I was contemplating about the pouria method and I was thinking what is the significance of the 75,85 MA and why in the world is it applied to the Price_Low... Anyways it still remains a mystery to me, but I figured why not substitute 75,85 MAs with MAs with same period one applied to High the other to low. that way some sort channel is formed, there would somehow be some rational behind the system. By doing this we are trading channel breakout...  
>    
>  I havnt tested this this is all theory right now but attached below is the graph of what I am talking about and the EA for experiment purposes.  
>    
>  -Mikhail
> 
> Ignored

It certainly makes sense. Let me know how the demo trading goes. Given the disparities between demo and live, and MIG and Interbank, I'm thinking that my next test will be to live trade the EA through MIG with a mini account and see what happens. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#365](/thread/post/228545#post228545 "Post Permalink")

  * Feb 27, 2007 3:41am  Feb 27, 2007 3:41am 

  * [ raven](raven)

  * | Joined Jul 2006  | Status: Trader | [21 Posts](/search?do=process&provider=Member&searchuser=14079)

I have started forward testing the beta HL ea, settings as they come apart from the sl which i have changed to 30, usual pairs and usual TFs, will let you know how it goes. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#366](/thread/post/228554#post228554 "Post Permalink")

  * Feb 27, 2007 3:48am  Feb 27, 2007 3:48am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar25698_4.gif) mikhaildgreat](mikhaildgreat)

  * | Joined Nov 2006  | Status: EA Programmer | [298 Posts](/search?do=process&provider=Member&searchuser=25698)

> [Quoting raven](/thread/post/228545#post228545 "View Quoted Post")
> 
> Disliked
> 
> I have started forward testing the beta HL ea, settings as they come apart from the sl which i have changed to 30, usual pairs and usual TFs, will let you know how it goes.
> 
> Ignored

thanks 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#367](/thread/post/228807#post228807 "Post Permalink")

  * Feb 27, 2007 10:19am  Feb 27, 2007 10:19am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar19504_4.gif) 1Sundevil](1sundevil)

  * | Joined Sep 2006  | Status: Trader | [228 Posts](/search?do=process&provider=Member&searchuser=19504)

Well, closed a few more trades (positive) today on MIG.   
  
GBPUSD and EURUSD, both buys, for +15 each. So, for MIG, I'm 30 for 34 and +313 pips.  
  
Interbank is NOT the way to go for this method. There I'm 7 for 13 and a BIG negative for pips and account %. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#368](/thread/post/229097#post229097 "Post Permalink")

  * Feb 27, 2007 6:39pm  Feb 27, 2007 6:39pm 

  * [ raven](raven)

  * | Joined Jul 2006  | Status: Trader | [21 Posts](/search?do=process&provider=Member&searchuser=14079)

First 12 hours using beta HL;  
TP 15, SL 30  
16 trades  
7 win  
5 Lose  
4 manually closed during spike this morning.  
currently -$57  
  
looking back at the losers none would have been saved by a bigger sl in fact all would have been better off with lower sl so i have changed the sl to 15, lets see how that plays out. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#369](/thread/post/229515#post229515 "Post Permalink")

  * Feb 28, 2007 1:06am  Feb 28, 2007 1:06am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar19504_4.gif) 1Sundevil](1sundevil)

  * | Joined Sep 2006  | Status: Trader | [228 Posts](/search?do=process&provider=Member&searchuser=19504)

Opened and closed 8 trades over night.  
  
USDCHF -50  
USDCAD +15  
EURUSD +15  
EURJPY -50  
EURJPY +15  
GBPUSD +15  
EURUSD +15  
GBPUSD +15  
  
So, now I'm 38 for 44, +268 pips on MIG. Interbank is getting HORRIBLE results. There I'm 9 for 18 and minus a HUGE amount on the demo account. I certainly _**will not**_ be using Interbank for this strategy with a live account.  
  
One thing I have noticed is my win/loss pip numbers on the EURJPY is bad. Out of my 6 total losses (at -50 each) three (3) of them are EURJPY. Overall I've had 11 EURJPY trades and I'm 8 for 11, and -35 pips on that currency. I may end up removing that currency. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#370](/thread/post/229540#post229540 "Post Permalink")

  * Feb 28, 2007 1:32am  Feb 28, 2007 1:32am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar25698_4.gif) mikhaildgreat](mikhaildgreat)

  * | Joined Nov 2006  | Status: EA Programmer | [298 Posts](/search?do=process&provider=Member&searchuser=25698)

Pouria HL forward test results, fxdd demo  
  
GBPUSD -50  
USDCAD +15  
EURGBP +15  
EURUSD +30 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#371](/thread/post/229695#post229695 "Post Permalink")

  * Feb 28, 2007 4:12am  Feb 28, 2007 4:12am 

  * [ BearPaw](bearpaw)

  * | Joined Jul 2006  | Status: A Trader for Life | [218 Posts](/search?do=process&provider=Member&searchuser=13999)

This is so perplexing...but interbank is not doing well with the GBP/USD pair.  
  
I am not trading that pair any more as of right now.  
  
Last nights results were this...  
  
EURJPY -50  
EURJPY +15  
CHFJPY -50  
AUDJPY +15  
GBPUSD -50  
GBPUSD -50  
EURUSD +15  
USDCAD +20  
  
So a net today of -205 pips....terrible.....As I said I have taken out GBPUSD.  
  
Thoughts?  
  
BP 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#372](/thread/post/229712#post229712 "Post Permalink")

  * Edited 4:38am  Feb 28, 2007 4:27am | Edited 4:38am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30695_4.gif) toti1972](toti1972)

  * | Joined Jan 2007  | Status: Trader | [107 Posts](/search?do=process&provider=Member&searchuser=30695)

OK, I'll post it here since I consider this thread is more active than the original:  
  
so far this week I got:  
  
EUR/JPY: -40 (already posted)  
EUR/JPY: -40  
EUR/JPY: +15  
EUR/JPY: +15  
EUR/GBP: +10  
USD/CAD: +20  
AUD/USD: +10  
  
But here the point for today:  
I opened manually a parallel order to those in red and one on USD/CHF (which although I got the cross, for some reason EA didn't get it)  
And I decided not to set a TP and just wait to see what happend...  
  
Actually I am:  
EUR/JPY: + 160   
USD/CHF: +100  
EUR/GBP: +26  
  
I am just trailing stop 40 on the first 2 and move my stop to BE on the 3rd...  
  
What I am trying to say is IMHO this sys is solid for entry points, but I think we are leaving the trade too early, and with 40 pips SL, if we got 2 losses, we need 5 or 6 winners to BE (I got two losses on EUR/JPY since yesterday) we need to develop a method to get a reliable exit signal to be able to "ride" the EMA 5 longer and be sure to catch most of the trend. this way we can afford better those negatives...  
Anybody got a good method or know some indicator that could help?   
  
Just a thought...  
  
Hope this helps...  
  
Regards 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#373](/thread/post/229809#post229809 "Post Permalink")

  * Feb 28, 2007 6:00am  Feb 28, 2007 6:00am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar19504_4.gif) 1Sundevil](1sundevil)

  * | Joined Sep 2006  | Status: Trader | [228 Posts](/search?do=process&provider=Member&searchuser=19504)

> [Quoting BearPaw](/thread/post/229695#post229695 "View Quoted Post")
> 
> Disliked
> 
> This is so perplexing...but interbank is not doing well with the GBP/USD pair.  
>    
>  I am not trading that pair any more as of right now.  
>    
>  Last nights results were this...  
>    
>  EURJPY -50  
>  EURJPY +15  
>  CHFJPY -50  
>  AUDJPY +15  
>  GBPUSD -50  
>  GBPUSD -50  
>  EURUSD +15  
>  USDCAD +20  
>    
>  So a net today of -205 pips....terrible.....As I said I have taken out GBPUSD.  
>    
>  Thoughts?  
>    
>  BP
> 
> Ignored

This definitely has something to do with Interbank. My results with them are terrible and they put me in many "bad" trades that MIG doesn't, and Interbank misses many "good" trades that MIG triggers. I don't know why this is, from a technical point of view, but I know that I don't like Interbank with this EA. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#374](/thread/post/230091#post230091 "Post Permalink")

  * Feb 28, 2007 11:26am  Feb 28, 2007 11:26am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar25698_4.gif) mikhaildgreat](mikhaildgreat)

  * | Joined Nov 2006  | Status: EA Programmer | [298 Posts](/search?do=process&provider=Member&searchuser=25698)

> [Quoting toti1972](/thread/post/229712#post229712 "View Quoted Post")
> 
> Disliked
> 
> OK, I'll post it here since I consider this thread is more active than the original:  
>    
>  so far this week I got:  
>    
>  EUR/JPY: -40 (already posted)  
>  EUR/JPY: -40  
>  EUR/JPY: +15  
>  EUR/JPY: +15  
>  EUR/GBP: +10  
>  USD/CAD: +20  
>  AUD/USD: +10  
>    
>  But here the point for today:  
>  I opened manually a parallel order to those in red and one on USD/CHF (which although I got the cross, for some reason EA didn't get it)  
>  And I decided not to set a TP and just wait to see what happend...  
>    
>  Actually I am:  
>  EUR/JPY: + 160   
>  USD/CHF: +100  
>  EUR/GBP: +26  
>    
>  I am just trailing stop 40 on the first 2 and move my stop to BE on the 3rd...  
>    
>  What I am trying to say is IMHO this sys is solid for entry points, but I think we are leaving the trade too early, and with 40 pips SL, if we got 2 losses, we need 5 or 6 winners to BE (I got two losses on EUR/JPY since yesterday) we need to develop a method to get a reliable exit signal to be able to "ride" the EMA 5 longer and be sure to catch most of the trend. this way we can afford better those negatives...  
>  Anybody got a good method or know some indicator that could help?   
>    
>  Just a thought...  
>    
>  Hope this helps...  
>    
>  Regards
> 
> Ignored

Yup an exit strategy is missing in this method. Any suggestions? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#375](/thread/post/230252#post230252 "Post Permalink")

  * Feb 28, 2007 3:51pm  Feb 28, 2007 3:51pm 

  * [ raven](raven)

  * | Joined Jul 2006  | Status: Trader | [21 Posts](/search?do=process&provider=Member&searchuser=14079)

beta HL TP15, SL15.  
Results for last 24 hours  
7 Trades   
2 win  
5 lose  
  
had 4 losers on cable would have been 1 had sl been 20 as it would have stayed around for a while.   
  
Having said that the buy entries that did happen would have been good sell entries and would all have been winners, even thought about what if the ea could reverse its trades based on if the previous trade lost, but it was only a thought.   
  
Beacause i am finding the entries to not be that accurate i am beginning to wonder if it might be more profitable just have a Gambling ea, ie it randomly picks which direction to trade in, then using a small sl, once into say a 10 pip profit it moves the sl to the breakeven point and then lets the chart run with say a 30 trailing stop. ![](https://resources.faireconomy.media/images/emojis/64/1f60a.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#376](/thread/post/231063#post231063 "Post Permalink")

  * Mar 1, 2007 7:42am  Mar 1, 2007 7:42am 

  * [ Askjo](askjo)

  * | Joined Oct 2005  | Status: Trader | [57 Posts](/search?do=process&provider=Member&searchuser=4185)

I traded 2 same pairs on **30 minutes** chart: EUR/USD, but the difference is stop loss: 20 pips vs 50 pips.  
  
2/26/07 time: 6.28 am. Stop loss is **20 pips**  
  
Sell  
  
1.3164  
  
Closed time: 2:47 pm  
  
1.3147  
  
**Loss** : -19 pips  
  
2/**26** /07 time: 6.31 am. Stop loss is **50 pips**.  
  
Sell  
  
1.3164  
  
Closed 2/**27** /07 time 3:18 am.  
  
1.3214  
  
**Loss** ; -50 pips.  
  
_Total_ _Loss_ : -69 pts.  
  
Last time I profited 4 pts, but now I lost -65 pts. (Demo only)  
  
Any thoughts?

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#377](/thread/post/231819#post231819 "Post Permalink")

  * Mar 2, 2007 12:13am  Mar 2, 2007 12:13am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar19504_4.gif) 1Sundevil](1sundevil)

  * | Joined Sep 2006  | Status: Trader | [228 Posts](/search?do=process&provider=Member&searchuser=19504)

Things have definitely changed a bit. I started out 28 of 30 for +320 pips. Since then I'm 16 for 23 for -110 pips.  
  
I've had a total of 9 losses overall.  
  
EURUSD three times (33%), overall 9 of 12 for -15 pips   
EURJPY three times (33%), overall 10 of 13 for 0 pips (break even)  
USDCHF twice (22%), overall 5 of 7 for +25 pips  
GBPUSD once (11%), overall 14 of 15 for +160 pips.  
  
What I'm seeing is that, specifically with the EURJPY and the EURUSD, the program is getting in at the top or bottom of a move going in the opposite direction. A few of these trades never hit a positive number. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#378](/thread/post/231829#post231829 "Post Permalink")

  * Mar 2, 2007 12:20am  Mar 2, 2007 12:20am 

  * [ BearPaw](bearpaw)

  * | Joined Jul 2006  | Status: A Trader for Life | [218 Posts](/search?do=process&provider=Member&searchuser=13999)

I wonder if this is a better strategy for live trading?  
  
Does the indicator posted in the other forum give accurate entry calls?  
  
BP 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#379](/thread/post/232612#post232612 "Post Permalink")

  * Mar 2, 2007 4:30pm  Mar 2, 2007 4:30pm 

  * [ raven](raven)

  * | Joined Jul 2006  | Status: Trader | [21 Posts](/search?do=process&provider=Member&searchuser=14079)

I cannot find a profitable way of trading any of the ea's in this thread, the funny thing is, the indicator in the other thread luxinteriours from memory has a much better entry point, i use it with a 5ema, 13 ema, and 50ema, i find using that indicator along with the crossing points of those emas get good results.  
  
Does anyone know of an ea that uses these crosses for entries and then lets you breakeven after (x) pip gain then, has a trailing stop after (x) number of pips, i think using this strategy would work in getting a good number of the longer trends. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#380](/thread/post/234901#post234901 "Post Permalink")

  * Mar 5, 2007 11:26pm  Mar 5, 2007 11:26pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar19504_4.gif) 1Sundevil](1sundevil)

  * | Joined Sep 2006  | Status: Trader | [228 Posts](/search?do=process&provider=Member&searchuser=19504)

Things are still going well on my end. The EA has put me in several more trades and my account is now up greater than 15%.  
  
I just had shoulder surgery, so I can't really type. I'll put in the EA trades ASAP. I can say that it dropped me into a EURUSD sell trade (3126) last night, after a huge drop down, which I thought about cancelling out of. Well, it came within 1 pip of my -50 SL before turning around and hitting my TP (3111). 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * The Pouria EA Development Thread
  *   * [ **Reply to Thread** ](/thread/17242-the-pouria-ea-development-thread/reply#reply)

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

[The Pouria Method](/thread/17011-the-pouria-method "OKay here is one of the 4 best systems that I've made and used, with this system I pickup atleast 50 pips a day, I'm sharing this because...") 562 replies

[Lessons Learned during System Development](/thread/2986-lessons-learned-during-system-development "Hi, 
  
I've been reading through the forum and somehow I'm in the process of developing my own system.. But not really doing actual...") 29 replies

[(pouria method II on the test)](/thread/23104-pouria-method-ii-on-the-test "Hello  
pouria method II is now DONE thanks to the group of experts and mathematicians that helped and made this method. 
now we are...") 218 replies

[System Development Secrets](/thread/7342-system-development-secrets "&lt;meta http-equiv=&quot;CONTENT-TYPE&quot; content=&quot;text/html; charset=utf-8&quot;&gt;&lt;title&gt;&lt;/title&gt;&lt;meta name=&quot;GENERATOR&quot; content=&quot;OpenOffice.org 2.0 ...") 5 replies

[Metatrader 4 Development Course](/thread/5906-metatrader-4-development-course "Here is the Mql_4_Metatrader_4_Development_Course in pdf \(link fixed\) : 
 
http://www.freefilehosting.org/pupload/view/8711") 3 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/17242-the-pouria-ea-development-thread/reply#reply)
  * Subscribe
  * [45](javascript:void\(0\);)

Attachments: The Pouria EA Development Thread

Tags: The Pouria EA Development Thread

#  [](/thread/17242-the-pouria-ea-development-thread)The Pouria EA Development Thread 

  * 

  * [#381](/thread/post/235210#post235210 "Post Permalink")

  * Mar 6, 2007 4:34am  Mar 6, 2007 4:34am 

  * [ stimuls](stimuls)

  * | Joined Jan 2007  | Status: Trader | [41 Posts](/search?do=process&provider=Member&searchuser=32146)

> [Quoting mikhaildgreat](/thread/post/230091#post230091 "View Quoted Post")
> 
> Disliked
> 
> Yup an exit strategy is missing in this method. Any suggestions?
> 
> Ignored

Here is an idea might make this ea really successful. Forget setting a TP.   
  
When a trade is triggered for a buy, set a trailing stop at the close of the next new bar's low. If the the trade is trending, the trialing stop would be moved up to the next new bar's low, so on and so forth. This would work the same if the trade was short, but the trailing stop would be set at the close of the next new bar's high.   
  
For a trade going long, the initial stop loss could be entered at the low of the bar which caused the trade. The trailing stop would not begin until the new low bar is higher than break even.   
  
If a trade is signaled long and the next closed bar signals a short trade, the position would be reversed going short even if the initial stop loss of the long trade was not hit.   
  
I think this sort of exit strategy would work well with an ea. I feel this approach has a good balance of letting the trade run and locking in pips. Let me know what you guys think. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#382](/thread/post/235313#post235313 "Post Permalink")

  * Mar 6, 2007 6:28am  Mar 6, 2007 6:28am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar19504_4.gif) 1Sundevil](1sundevil)

  * | Joined Sep 2006  | Status: Trader | [228 Posts](/search?do=process&provider=Member&searchuser=19504)

It's a good idea, but I have seen many of my trades that have "just" hit the +15 TP before racing in the opposite direction.  
  
For me the best way would be a combination of conservative EA settings (which it has) and then watching the trade as it goes. If you feel that it will go beyond your EA TP, then either adjust the TP or remove the TP and wait to close it manually.  
  
Right now the EA alone has increased my demo account +15% since 2/16/07. +15% in 17 days?! I'll take that and never look back. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#383](/thread/post/235337#post235337 "Post Permalink")

  * Mar 6, 2007 7:03am  Mar 6, 2007 7:03am 

  * [ stimuls](stimuls)

  * | Joined Jan 2007  | Status: Trader | [41 Posts](/search?do=process&provider=Member&searchuser=32146)

> [Quoting 1Sundevil](/thread/post/235313#post235313 "View Quoted Post")
> 
> Disliked
> 
> It's a good idea, but I have seen many of my trades that have "just" hit the +15 TP before racing in the opposite direction.  
>    
>  For me the best way would be a combination of conservative EA settings (which it has) and then watching the trade as it goes. If you feel that it will go beyond your EA TP, then either adjust the TP or remove the TP and wait to close it manually.  
>    
>  Right now the EA alone has increased my demo account +15% since 2/16/07. +15% in 17 days?! I'll take that and never look back.
> 
> Ignored

What TP and SL settings are you using? Thanks. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#384](/thread/post/235403#post235403 "Post Permalink")

  * Mar 6, 2007 8:02am  Mar 6, 2007 8:02am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar19504_4.gif) 1Sundevil](1sundevil)

  * | Joined Sep 2006  | Status: Trader | [228 Posts](/search?do=process&provider=Member&searchuser=19504)

> [Quoting stimuls](/thread/post/235337#post235337 "View Quoted Post")
> 
> Disliked
> 
> What TP and SL settings are you using? Thanks.
> 
> Ignored

TP +15  
SL -50  
  
Right now the EA is hitting at +83% winners. $50,000 demo account is up $7,647.37. It's certainly not perfect and I want to see how things will change with a small live account soon. But you are right about leaving pips on the table on some trades. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#385](/thread/post/235416#post235416 "Post Permalink")

  * Mar 6, 2007 8:16am  Mar 6, 2007 8:16am 

  * [ stimuls](stimuls)

  * | Joined Jan 2007  | Status: Trader | [41 Posts](/search?do=process&provider=Member&searchuser=32146)

> [Quoting 1Sundevil](/thread/post/235403#post235403 "View Quoted Post")
> 
> Disliked
> 
> TP +15  
>  SL -50  
>    
>  Right now the EA is hitting at +83% winners. $50,000 demo account is up $7,647.37. It's certainly not perfect and I want to see how things will change with a small live account soon. But you are right about leaving pips on the table on some trades.
> 
> Ignored

Risk/Reward ratio is not good but I guess that does not matter if the win rate is high. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#386](/thread/post/235601#post235601 "Post Permalink")

  * Mar 6, 2007 12:46pm  Mar 6, 2007 12:46pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1668_4.gif) traderone](traderone)

  * | Joined Feb 2005  | Status: Trader | [392 Posts](/search?do=process&provider=Member&searchuser=1668)

1sundevil.....  
  
What version are you using? what are your best pairs? Thanks for any info. 

Don Life is expensive, but includes a free trip around the sun.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#387](/thread/post/235710#post235710 "Post Permalink")

  * Mar 6, 2007 2:56pm  Mar 6, 2007 2:56pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar19504_4.gif) 1Sundevil](1sundevil)

  * | Joined Sep 2006  | Status: Trader | [228 Posts](/search?do=process&provider=Member&searchuser=19504)

> [Quoting traderone](/thread/post/235601#post235601 "View Quoted Post")
> 
> Disliked
> 
> 1sundevil.....  
>    
>  What version are you using? what are your best pairs? Thanks for any info.
> 
> Ignored

beta3 with a MIG demo. My results on Interbank were horrible. I'll do some research to see which are best, but I believe that GBPUSD was doing really well.  
  
The only problem with MIG is that some completed trades seem to disappear from my Account History, although the account balance is correct. Trying to find out why and if it's just a "demo" issue. As far as I can tell I'm currently 54 for 65 (83% winners) and +258 pips. The account is now up 14.8%. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#388](/thread/post/235769#post235769 "Post Permalink")

  * Mar 6, 2007 4:48pm  Mar 6, 2007 4:48pm 

  * [ stimuls](stimuls)

  * | Joined Jan 2007  | Status: Trader | [41 Posts](/search?do=process&provider=Member&searchuser=32146)

> [Quoting 1Sundevil](/thread/post/235710#post235710 "View Quoted Post")
> 
> Disliked
> 
> beta3 with a MIG demo. My results on Interbank were horrible. I'll do some research to see which are best, but I believe that GBPUSD was doing really well.  
>    
>  The only problem with MIG is that some completed trades seem to disappear from my Account History, although the account balance is correct. Trying to find out why and if it's just a "demo" issue. As far as I can tell I'm currently 54 for 65 (83% winners) and +258 pips. The account is now up 14.8%.
> 
> Ignored

Why do you thing there is such a discrepancy between the two brokers? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#389](/thread/post/236100#post236100 "Post Permalink")

  * Mar 7, 2007 12:13am  Mar 7, 2007 12:13am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar6378_4.gif) brainjt](brainjt)

  * | Joined Feb 2006  | Status: brainjt | [376 Posts](/search?do=process&provider=Member&searchuser=6378)

> [Quoting 1Sundevil](/thread/post/235403#post235403 "View Quoted Post")
> 
> Disliked
> 
> TP +15  
>  SL -50  
>    
>  Right now the EA is hitting at +83% winners. $50,000 demo account is up $7,647.37. It's certainly not perfect and I want to see how things will change with a small live account soon. But you are right about leaving pips on the table on some trades.
> 
> Ignored

Can you please send this EA with your setup ?   
Thx 

BJ

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#390](/thread/post/236102#post236102 "Post Permalink")

  * Mar 7, 2007 12:16am  Mar 7, 2007 12:16am 

  * [ brentmack](brentmack)

  * | Joined Apr 2006  | Status: Commissioner of Autotrading | [462 Posts](/search?do=process&provider=Member&searchuser=8726)

> [Quoting 1Sundevil](/thread/post/235710#post235710 "View Quoted Post")
> 
> Disliked
> 
> The account is now up 14.8%.
> 
> Ignored

Hi 1SunDevil:  
  
What kind of risk level or money management techniques are you using? Anything special or default settings?   
  
P.S. Thanks for blazing the trail with tesing this EA. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#391](/thread/post/236108#post236108 "Post Permalink")

  * Mar 7, 2007 12:32am  Mar 7, 2007 12:32am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar19504_4.gif) 1Sundevil](1sundevil)

  * | Joined Sep 2006  | Status: Trader | [228 Posts](/search?do=process&provider=Member&searchuser=19504)

> [Quoting brentmack](/thread/post/236102#post236102 "View Quoted Post")
> 
> Disliked
> 
> Hi 1SunDevil:  
>    
>  What kind of risk level or money management techniques are you using? Anything special or default settings?   
>    
>  P.S. Thanks for blazing the trail with tesing this EA.
> 
> Ignored

1: I don't know why there is a discrepency between the two brokers, just that the trades, triggers and results were very different. We, here on this thread, also suspect that "live" trading this EA will differ from demo trading, which I hope to test soon.  
  
2: The beta3 EA should still be listed in either this thread or the other Pouria thread. It would be in the early pages.  
  
3: I'm just using the default setting established in the EA. I did mess up early and lost out on some money by having the gbpusd set lower, which has been rectified since.  
  
I'm going to try and paste the account history here ASAP so you can see what it has done. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#392](/thread/post/236131#post236131 "Post Permalink")

  * Edited 1:12am  Mar 7, 2007 12:54am | Edited 1:12am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar19504_4.gif) 1Sundevil](1sundevil)

  * | Joined Sep 2006  | Status: Trader | [228 Posts](/search?do=process&provider=Member&searchuser=19504)

Hope this attachment comes through.  
  
From what I'm seeing, my pairs break down like this: (TP = +15 ; SL = -50)  
  
EURUSD 11 for 14 = 78.6% (+15 pips overall)  
GBPUSD 14 for 16 = 87.5% (+110 pips)  
USDJPY 5 for 6 = 83.3% (+25 pips)  
USDCAD 3 for 3 = 100% (+45 pips)  
USDCHF 9 for 12 = 75% (-15 pips)  
EURJPY 9 for 11 = 81.8% (+35 pips) 

Attached File(s)

![File Type: doc](https://assets.faireconomy.media/images/attach/doc.gif) [MIG Investments SA.doc](/attachment/file/24485?d=1173196427) 377 KB | 394 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#393](/thread/post/236164#post236164 "Post Permalink")

  * Mar 7, 2007 1:32am  Mar 7, 2007 1:32am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1668_4.gif) traderone](traderone)

  * | Joined Feb 2005  | Status: Trader | [392 Posts](/search?do=process&provider=Member&searchuser=1668)

Thanks 1SunDevil.  
  
I have lost hundreds of pips on IBFX running version 1.1  
  
Maybe I will try Vel oci ty4 x. their demo and live servers are supposed to be the same. 

Don Life is expensive, but includes a free trip around the sun.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#394](/thread/post/236181#post236181 "Post Permalink")

  * Mar 7, 2007 1:49am  Mar 7, 2007 1:49am 

  * [ txsundevil](txsundevil)

  * | Joined Jul 2006  | Status: txsundevil | [38 Posts](/search?do=process&provider=Member&searchuser=14820)

Hello TraderOne:  
  
I have a Live Account at Velocity4x, their Demo and Live servers are not the SAME, however the results are almost always exactly the Same, (running an EA etc) however the Demo Servers have downtime but this is not frequent, amybe once a week for 1-5 minutes or so. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#395](/thread/post/236188#post236188 "Post Permalink")

  * Mar 7, 2007 1:56am  Mar 7, 2007 1:56am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar19504_4.gif) 1Sundevil](1sundevil)

  * | Joined Sep 2006  | Status: Trader | [228 Posts](/search?do=process&provider=Member&searchuser=19504)

Good to see another Sundevil here! Here's a pic of ASU women for the non-sundevils out there!  
  
[http://i141.photobucket.com/albums/r...asuhotties.jpg](http://i141.photobucket.com/albums/r51/sundevil520/asuhotties.jpg)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#396](/thread/post/237314#post237314 "Post Permalink")

  * Mar 8, 2007 12:28am  Mar 8, 2007 12:28am 

  * [ brentmack](brentmack)

  * | Joined Apr 2006  | Status: Commissioner of Autotrading | [462 Posts](/search?do=process&provider=Member&searchuser=8726)

> [Quoting 1Sundevil](/thread/post/236188#post236188 "View Quoted Post")
> 
> Disliked
> 
> Good to see another Sundevil here! Here's a pic of ASU women for the non-sundevils out there!  
>    
>  [http://i141.photobucket.com/albums/r...asuhotties.jpg](http://i141.photobucket.com/albums/r51/sundevil520/asuhotties.jpg)
> 
> Ignored

It looks like these ladies brought this thread to a screaming halt. Everybody needs to quit gawking at the babes and get back to the Pouria Method. ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#397](/thread/post/237341#post237341 "Post Permalink")

  * Mar 8, 2007 12:55am  Mar 8, 2007 12:55am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar25698_4.gif) mikhaildgreat](mikhaildgreat)

  * | Joined Nov 2006  | Status: EA Programmer | [298 Posts](/search?do=process&provider=Member&searchuser=25698)

> [Quoting 1Sundevil](/thread/post/236188#post236188 "View Quoted Post")
> 
> Disliked
> 
> Good to see another Sundevil here! Here's a pic of ASU women for the non-sundevils out there!  
>    
>  [http://i141.photobucket.com/albums/r...asuhotties.jpg](http://i141.photobucket.com/albums/r51/sundevil520/asuhotties.jpg)
> 
> Ignored

![](https://resources.faireconomy.media/images/emojis/64/1f911.png?v=15.1) I've been out of this thread for quite awhile working on other projects but those 2 girls just dragged me back in! YUM! ![](https://resources.faireconomy.media/images/emojis/64/1f923.png?v=15.1)  
  
-Mikhail 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#398](/thread/post/237357#post237357 "Post Permalink")

  * Mar 8, 2007 1:06am  Mar 8, 2007 1:06am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30695_4.gif) toti1972](toti1972)

  * | Joined Jan 2007  | Status: Trader | [107 Posts](/search?do=process&provider=Member&searchuser=30695)

> [Quoting 1Sundevil](/thread/post/236188#post236188 "View Quoted Post")
> 
> Disliked
> 
> Good to see another Sundevil here! Here's a pic of ASU women for the non-sundevils out there!  
> 
> 
> Ignored

  
IS THERE ANY NON-SUNDEVIL OUT THERE??? I DON'T THINK SO...NO FROM NOW ON...  
  
HEY BRENTMACK,  
  
When you say " get back to the Pouria Method...what do you mean???  
  
WHAT POURIA METHOD??? WHAT FOREX MARKET???  
  
GO SUNDEVILS!!!!!!!  
  
  
![](https://resources.faireconomy.media/images/emojis/64/1f923.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#399](/thread/post/237572#post237572 "Post Permalink")

  * Mar 8, 2007 4:32am  Mar 8, 2007 4:32am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar19504_4.gif) 1Sundevil](1sundevil)

  * | Joined Sep 2006  | Status: Trader | [228 Posts](/search?do=process&provider=Member&searchuser=19504)

Went 2 for 4 last night. EURUSD screwed me again and is now the biggest loser of the 6 currencies. CAD suffered its first loss, but I thought about closing it out when it was +13....just before it tanked.  
  
GBP and CHF both hit their TP of +15 each. I am also in CAD, JPY and EURJPY trades right now.  
  
Oh, BTW (got to love those ASU girls!): 

Attached Image

![](/attachment/image/24637?d=1173295883)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#400](/thread/post/237595#post237595 "Post Permalink")

  * Mar 8, 2007 4:48am  Mar 8, 2007 4:48am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30695_4.gif) toti1972](toti1972)

  * | Joined Jan 2007  | Status: Trader | [107 Posts](/search?do=process&provider=Member&searchuser=30695)

> [Quoting 1Sundevil](/thread/post/237572#post237572 "View Quoted Post")
> 
> Disliked
> 
> Went 2 for 4 last night. EURUSD screwed me again and is now the biggest loser of the 6 currencies. CAD suffered its first loss, but I thought about closing it out when it was +13....just before it tanked.  
>    
>  GBP and CHF both hit their TP of +15 each. I am also in CAD, JPY and EURJPY trades right now.  
>    
>  Oh, BTW (got to love those ASU girls!):
> 
> Ignored

  
Hey sundevil...  
  
Wouldn't be a great idea to open a special thread for all of us who are "ASU Sundevil's fans"   
I bet it'll get more views than the best system here in FF in a couple of days...what do you think uh?  
Now I know I need money out of forex for 2 reasons: 1. move to ARZ and 2nd to fill out a divorce application...![](https://resources.faireconomy.media/images/emojis/64/1f923.png?v=15.1)   
  
GO SUNDEVILS!!!! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * The Pouria EA Development Thread
  *   * [ **Reply to Thread** ](/thread/17242-the-pouria-ea-development-thread/reply#reply)

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

[The Pouria Method](/thread/17011-the-pouria-method "OKay here is one of the 4 best systems that I've made and used, with this system I pickup atleast 50 pips a day, I'm sharing this because...") 562 replies

[Lessons Learned during System Development](/thread/2986-lessons-learned-during-system-development "Hi, 
  
I've been reading through the forum and somehow I'm in the process of developing my own system.. But not really doing actual...") 29 replies

[(pouria method II on the test)](/thread/23104-pouria-method-ii-on-the-test "Hello  
pouria method II is now DONE thanks to the group of experts and mathematicians that helped and made this method. 
now we are...") 218 replies

[System Development Secrets](/thread/7342-system-development-secrets "&lt;meta http-equiv=&quot;CONTENT-TYPE&quot; content=&quot;text/html; charset=utf-8&quot;&gt;&lt;title&gt;&lt;/title&gt;&lt;meta name=&quot;GENERATOR&quot; content=&quot;OpenOffice.org 2.0 ...") 5 replies

[Metatrader 4 Development Course](/thread/5906-metatrader-4-development-course "Here is the Mql_4_Metatrader_4_Development_Course in pdf \(link fixed\) : 
 
http://www.freefilehosting.org/pupload/view/8711") 3 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/17242-the-pouria-ea-development-thread/reply#reply)
  * Subscribe
  * [45](javascript:void\(0\);)

Attachments: The Pouria EA Development Thread

Tags: The Pouria EA Development Thread

#  [](/thread/17242-the-pouria-ea-development-thread)The Pouria EA Development Thread 

  * 

  * [#401](/thread/post/237656#post237656 "Post Permalink")

  * Mar 8, 2007 5:46am  Mar 8, 2007 5:46am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar19504_4.gif) 1Sundevil](1sundevil)

  * | Joined Sep 2006  | Status: Trader | [228 Posts](/search?do=process&provider=Member&searchuser=19504)

> [Quoting toti1972](/thread/post/237595#post237595 "View Quoted Post")
> 
> Disliked
> 
> Hey sundevil...  
>    
>  Wouldn't be a great idea to open a special thread for all of us who are "ASU Sundevil's fans"   
>  I bet it'll get more views than the best system here in FF in a couple of days...what do you think uh?  
>  Now I know I need money out of forex for 2 reasons: 1. move to ARZ and 2nd to fill out a divorce application...![](https://resources.faireconomy.media/images/emojis/64/1f923.png?v=15.1)   
>    
>  GO SUNDEVILS!!!!
> 
> Ignored

LOL! Have you been to devilsdigest.com? Check it out for ASU athletics forums. On there I'm DenverDevil.  
  
As for Pouria, it just closed out my EURJPY trade for +15.   
JPY is even right now and CAD is slightly negative. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#402](/thread/post/237962#post237962 "Post Permalink")

  * Mar 8, 2007 11:40am  Mar 8, 2007 11:40am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar19504_4.gif) 1Sundevil](1sundevil)

  * | Joined Sep 2006  | Status: Trader | [228 Posts](/search?do=process&provider=Member&searchuser=19504)

EA dropped me in a EURJPY trade that went bust (-50), so I did a little checking.  
  
So far the EA has placed me in 69 trades. 55 have been positive which equates to a 79.7% winning percentage and a total of +125 pips overall.  
  
Now, that means that I have had 14 losses. SEVEN of those losses (50%) come from either the EURUSD or the EURJPY. If I was to take out the EUR pairs my numbers change for the better. I'd be 34 for 41 (82.9% winners) and +160 pips overall.  
  
My guess is that EUR pairs will not fair well with this EA strategy. Why? I have no idea. EURUSD has lost 4 times (11 for 15, -35 pips) and the EURJPY has lost 3 times (10 for 13, 0 pips).  
  
When this demo account is up I will be removing the EUR pairs and looking at adding two different ones for the next go around. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#403](/thread/post/238106#post238106 "Post Permalink")

  * Mar 8, 2007 3:50pm  Mar 8, 2007 3:50pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar19504_4.gif) 1Sundevil](1sundevil)

  * | Joined Sep 2006  | Status: Trader | [228 Posts](/search?do=process&provider=Member&searchuser=19504)

A little more analysis. Since the pip amounts change as the account balance does, I thought I'd look at how much MONEY each pair has generated with this EA.  
  
GBPUSD = + $5700  
USDJPY = + $1802.03  
USDCHF = + $39.28  
  
the negative pairs  
  
EURJPY = - $10.80  
USDCAD = - $432.72  
EURUSD = **\- $1680**  
  
Basically the GBP reigns supreme and the EUR sucks with this EA. I'm thinking about switching out the EURUSD for the GBPJPY, to see what that pair does. I also need to look at two new pairs to replace the EJ and CAD. Any ideas? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#404](/thread/post/240438#post240438 "Post Permalink")

  * Mar 11, 2007 1:48pm  Mar 11, 2007 1:48pm 

  * [ timntools](timntools)

  * | Joined Dec 2006  | Status: Trader | [17 Posts](/search?do=process&provider=Member&searchuser=27197)

> Quote
> 
> Disliked
> 
> Basically the GBP reigns supreme and the EUR sucks with this EA. I'm thinking about switching out the EURUSD for the GBPJPY, to see what that pair does. I also need to look at two new pairs to replace the EJ and CAD. Any ideas?

  
gbp/jpy and chf 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#405](/thread/post/241668#post241668 "Post Permalink")

  * Mar 13, 2007 12:30am  Mar 13, 2007 12:30am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar19504_4.gif) 1Sundevil](1sundevil)

  * | Joined Sep 2006  | Status: Trader | [228 Posts](/search?do=process&provider=Member&searchuser=19504)

Big night for the EA last night. Put me in six trades and all hit my +15 TP.  
  
EURJPY Buy  
USDCHF sell  
EURJPY sell  
USDJPY sell  
GBPJPY sell  
GBPUSD sell  
  
my demo account is now up over 21% 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#406](/thread/post/241675#post241675 "Post Permalink")

  * Mar 13, 2007 12:35am  Mar 13, 2007 12:35am 

  * [ JamDown](jamdown)

  * | Joined Dec 2006  | Status: Trader | [39 Posts](/search?do=process&provider=Member&searchuser=27324)

[quote=mikhaildgreat;237341]![](https://resources.faireconomy.media/images/emojis/64/1f911.png?v=15.1) I've been out of this thread for quite awhile working on other projects but those 2 girls just dragged me back in! YUM! ![](https://resources.faireconomy.media/images/emojis/64/1f923.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#407](/thread/post/242075#post242075 "Post Permalink")

  * Mar 13, 2007 9:32am  Mar 13, 2007 9:32am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar19504_4.gif) 1Sundevil](1sundevil)

  * | Joined Sep 2006  | Status: Trader | [228 Posts](/search?do=process&provider=Member&searchuser=19504)

EA hit another (EURJPY) for +15.  
  
So, since 2/16, the EA is 71 for 85 (83.5%) and the account is up 22.6%.  
  
I'm contemplating adjusting the TP up five to +20 and the SL down ten to -40. I need to go back and look to see how that would have effected past trades, but this appears to be a few tweaks away from a very good system. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#408](/thread/post/242155#post242155 "Post Permalink")

  * Mar 13, 2007 11:19am  Mar 13, 2007 11:19am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1668_4.gif) traderone](traderone)

  * | Joined Feb 2005  | Status: Trader | [392 Posts](/search?do=process&provider=Member&searchuser=1668)

sundevil... are you still running Beta3?  
  
Those are great results. 

Don Life is expensive, but includes a free trip around the sun.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#409](/thread/post/242197#post242197 "Post Permalink")

  * Mar 13, 2007 12:14pm  Mar 13, 2007 12:14pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar19504_4.gif) 1Sundevil](1sundevil)

  * | Joined Sep 2006  | Status: Trader | [228 Posts](/search?do=process&provider=Member&searchuser=19504)

> [Quoting traderone](/thread/post/242155#post242155 "View Quoted Post")
> 
> Disliked
> 
> sundevil... are you still running Beta3?  
>    
>  Those are great results.
> 
> Ignored

Yes, beta3. I took out the EURUSD and put in GBPJPY. I think that is the only change thus far, but the EURUSD was really sucking bad. This system really needs currencies that "move" in order to really work. The EURUSD was just too weak in its moves to be effective.  
  
Right now the EA has me in USDCAD and GBPUSD trades. We'll see how those work out. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#410](/thread/post/242880#post242880 "Post Permalink")

  * Mar 14, 2007 2:24am  Mar 14, 2007 2:24am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar19504_4.gif) 1Sundevil](1sundevil)

  * | Joined Sep 2006  | Status: Trader | [228 Posts](/search?do=process&provider=Member&searchuser=19504)

I can say that the EURJPY EA trades have really gone off big time the last two days. It opened and closed another one last night for +15. Since the week began, the EA has gone 5 for 5 in the EURJPY for +75 pips.   
  
Right now the EA is 74 for 88 (84.1%) and the demo account is up 27% since 2/16.   
  
The USDCAD trade is still active (I may dump that currency as it is also a slow mover), and the EA dropped me into a GBPUSD trade that is slightly negative as well. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#411](/thread/post/243702#post243702 "Post Permalink")

  * Mar 14, 2007 7:51pm  Mar 14, 2007 7:51pm 

  * [ tnh_z](tnh_z)

  * | Joined Apr 2006  | Status: Trader | [16 Posts](/search?do=process&provider=Member&searchuser=8205)

1Sundevil, a question please.  
  
do you set "ConfimedOnEntry" on false or true?  
  
my result isn't good so far. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#412](/thread/post/243985#post243985 "Post Permalink")

  * Mar 15, 2007 1:12am  Mar 15, 2007 1:12am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar19504_4.gif) 1Sundevil](1sundevil)

  * | Joined Sep 2006  | Status: Trader | [228 Posts](/search?do=process&provider=Member&searchuser=19504)

> [Quoting tnh_z](/thread/post/243702#post243702 "View Quoted Post")
> 
> Disliked
> 
> 1Sundevil, a question please.  
>    
>  do you set "ConfimedOnEntry" on false or true?  
>    
>  my result isn't good so far.
> 
> Ignored

Confirmed entry is set to true. I am using MIG. I had terrible results on Interbank. The only problem with MIG is that trades continue to dissapear in my "account history".   
  
Last night I can see that the EA dropped me into "buys" on the GBPJPY, EURJPY and USDJPY that all closed for +20. It also dropped me into a USDCHF buy that went -40. None of those four are showing up in my "account history", so it's difficult to track.  
  
I also just, as of last night, adjusted my TP to +20 and my SL to -40. I want to see how much of a difference that makes. The 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#413](/thread/post/244243#post244243 "Post Permalink")

  * Mar 15, 2007 6:10am  Mar 15, 2007 6:10am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar19504_4.gif) 1Sundevil](1sundevil)

  * | Joined Sep 2006  | Status: Trader | [228 Posts](/search?do=process&provider=Member&searchuser=19504)

Well, the EA demo just reached 100 closed trades. It started on 2/16/07 and went 83 for 100 (83% winners). The $50,000 demo account is now up 26.2% at $63,097.37.  
  
I can't wait to see how it does over the next 100. Getting ready to try it with real money very soon. A few more tweaks to go. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#414](/thread/post/244260#post244260 "Post Permalink")

  * Mar 15, 2007 6:24am  Mar 15, 2007 6:24am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30695_4.gif) toti1972](toti1972)

  * | Joined Jan 2007  | Status: Trader | [107 Posts](/search?do=process&provider=Member&searchuser=30695)

> [Quoting 1Sundevil](/thread/post/244243#post244243 "View Quoted Post")
> 
> Disliked
> 
> Well, the EA demo just reached 100 closed trades. It started on 2/16/07 and went 83 for 100 (83% winners). The $50,000 demo account is now up 26.2% at $63,097.37.  
>    
>  I can't wait to see how it does over the next 100. Getting ready to try it with real money very soon. A few more tweaks to go.
> 
> Ignored

Hey DenverDevil...(heisman winner ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1) )  
  
what a great news...unfortunately I wasn't able to trade Pouria this week but I am closely following your results...Please keep us updated with your new SL and TP settings which IMO will improve the performance.   
Great job...  
Thank you 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#415](/thread/post/244267#post244267 "Post Permalink")

  * Mar 15, 2007 6:33am  Mar 15, 2007 6:33am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar19504_4.gif) 1Sundevil](1sundevil)

  * | Joined Sep 2006  | Status: Trader | [228 Posts](/search?do=process&provider=Member&searchuser=19504)

> [Quoting toti1972](/thread/post/244260#post244260 "View Quoted Post")
> 
> Disliked
> 
> Hey DenverDevil...(heisman winner ![](https://resources.faireconomy.media/images/emojis/64/1f44d.png?v=15.1) )  
>    
>  what a great news...unfortunately I wasn't able to trade Pouria this week but I am closely following your results...Please keep us updated with your new SL and TP settings which IMO will improve the performance.   
>  Great job...  
>  Thank you
> 
> Ignored

LOL, now you have to let me know who you are on DD!  
  
So far the change in TP has been good with all four of the new trades hitting +20. I also think I figured out why MIG was "losing" some of my trades. For some reason it was looking at "today" as tomorrow and the trades wouldn't show up in my account history. All seems to be fixed now in that regard. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#416](/thread/post/244272#post244272 "Post Permalink")

  * Mar 15, 2007 6:42am  Mar 15, 2007 6:42am 

  * [ tnh_z](tnh_z)

  * | Joined Apr 2006  | Status: Trader | [16 Posts](/search?do=process&provider=Member&searchuser=8205)

> [Quoting 1Sundevil](/thread/post/243985#post243985 "View Quoted Post")
> 
> Disliked
> 
> Confirmed entry is set to true. I am using MIG. I had terrible results on Interbank. The only problem with MIG is that trades continue to dissapear in my "account history".   
>    
>  Last night I can see that the EA dropped me into "buys" on the GBPJPY, EURJPY and USDJPY that all closed for +20. It also dropped me into a USDCHF buy that went -40. None of those four are showing up in my "account history", so it's difficult to track.  
>    
>  I also just, as of last night, adjusted my TP to +20 and my SL to -40. I want to see how much of a difference that makes. The
> 
> Ignored

Thank you 1Sundevil for your explanation.Mine was set to false so far and perhaps bad result has been because of that.  
now I'll make a forward test on it again with new setting.  
Hope you have good result on real like demo.please inform us about EA real performance. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#417](/thread/post/244674#post244674 "Post Permalink")

  * Mar 15, 2007 5:03pm  Mar 15, 2007 5:03pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar19951_4.gif) nicolas_nrjk](nicolas_nrjk)

  * | Joined Sep 2006  | Status: Trader | [37 Posts](/search?do=process&provider=Member&searchuser=19951)

hi guys, what version of Pouria EA are you using and do you still use the target point described in the first page of the pouria method.  
there are a lot of EA's and i am very confused. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#418](/thread/post/245009#post245009 "Post Permalink")

  * Mar 15, 2007 11:58pm  Mar 15, 2007 11:58pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar19504_4.gif) 1Sundevil](1sundevil)

  * | Joined Sep 2006  | Status: Trader | [228 Posts](/search?do=process&provider=Member&searchuser=19504)

> [Quoting nicolas_nrjk](/thread/post/244674#post244674 "View Quoted Post")
> 
> Disliked
> 
> hi guys, what version of Pouria EA are you using and do you still use the target point described in the first page of the pouria method.  
>  there are a lot of EA's and i am very confused.
> 
> Ignored

I'm using beta3. My TP is set to +20 on most, but I thin k it's still +15 on the USDCHF and USDCAD because those currencies don't move that much. My SL is -40 on all.  
  
The EA had another good night while I was sleeping. Dropped me into four trades CAD, 2 x CHF, and GBPUSD. All closed at their TP. Account is now up 35.6% since 2/16.   
  
Right now the EA has me in a JPY (buy) and CAD (sell). Both are negative right now. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#419](/thread/post/245065#post245065 "Post Permalink")

  * Mar 16, 2007 1:16am  Mar 16, 2007 1:16am 

  * [ tnh_z](tnh_z)

  * | Joined Apr 2006  | Status: Trader | [16 Posts](/search?do=process&provider=Member&searchuser=8205)

  
1Sundevil, did you test ( I mean forward test) default setting based on original method?   
If yes, which broker you used it’s platform? and what was it’s result on the whole?  
Thanks in advance.  
  

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#420](/thread/post/245115#post245115 "Post Permalink")

  * Mar 16, 2007 2:01am  Mar 16, 2007 2:01am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar19504_4.gif) 1Sundevil](1sundevil)

  * | Joined Sep 2006  | Status: Trader | [228 Posts](/search?do=process&provider=Member&searchuser=19504)

> [Quoting tnh_z](/thread/post/245065#post245065 "View Quoted Post")
> 
> Disliked
> 
> 1Sundevil, did you test ( I mean forward test) default setting based on original method?   
>  If yes, which broker you used it’s platform? and what was it’s result on the whole?  
>  Thanks in advance.  
> 
> 
> Ignored

For the most part this whole test is using the default setting. I did change the SL to -50 early on as many of us felt that it needed room to "breath" in case it went against us initially. I had a few trades that came within ONE pip of going -50 before turning around to hit my TP. I've now adjusted my SL to -40 and my TP to +20 in order to see if I can better my results.  
  
I'm using a MIG demo account. I also opened an Interbank demo and got absolutely horrible results. Why the difference? I have no idea.  
  
Here's a graph that shows what the EA has done on MIG since I started it on 2/16:  
[http://i141.photobucket.com/albums/r...Statement2.gif](http://i141.photobucket.com/albums/r51/sundevil520/DetailedStatement2.gif)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * The Pouria EA Development Thread
  *   * [ **Reply to Thread** ](/thread/17242-the-pouria-ea-development-thread/reply#reply)

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

[The Pouria Method](/thread/17011-the-pouria-method "OKay here is one of the 4 best systems that I've made and used, with this system I pickup atleast 50 pips a day, I'm sharing this because...") 562 replies

[Lessons Learned during System Development](/thread/2986-lessons-learned-during-system-development "Hi, 
  
I've been reading through the forum and somehow I'm in the process of developing my own system.. But not really doing actual...") 29 replies

[(pouria method II on the test)](/thread/23104-pouria-method-ii-on-the-test "Hello  
pouria method II is now DONE thanks to the group of experts and mathematicians that helped and made this method. 
now we are...") 218 replies

[System Development Secrets](/thread/7342-system-development-secrets "&lt;meta http-equiv=&quot;CONTENT-TYPE&quot; content=&quot;text/html; charset=utf-8&quot;&gt;&lt;title&gt;&lt;/title&gt;&lt;meta name=&quot;GENERATOR&quot; content=&quot;OpenOffice.org 2.0 ...") 5 replies

[Metatrader 4 Development Course](/thread/5906-metatrader-4-development-course "Here is the Mql_4_Metatrader_4_Development_Course in pdf \(link fixed\) : 
 
http://www.freefilehosting.org/pupload/view/8711") 3 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/17242-the-pouria-ea-development-thread/reply#reply)
  * Subscribe
  * [45](javascript:void\(0\);)

Attachments: The Pouria EA Development Thread

Tags: The Pouria EA Development Thread

#  [](/thread/17242-the-pouria-ea-development-thread)The Pouria EA Development Thread 

  * 

  * [#421](/thread/post/245122#post245122 "Post Permalink")

  * Mar 16, 2007 2:07am  Mar 16, 2007 2:07am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar19504_4.gif) 1Sundevil](1sundevil)

  * | Joined Sep 2006  | Status: Trader | [228 Posts](/search?do=process&provider=Member&searchuser=19504)

> [Quoting 1Sundevil](/thread/post/245009#post245009 "View Quoted Post")
> 
> Disliked
> 
> Right now the EA has me in a JPY (buy) and CAD (sell). Both are negative right now.
> 
> Ignored

The JPY hit my +20 TP and the CAD looks to be close to my -40 SL. We'll see if it turns. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#422](/thread/post/245159#post245159 "Post Permalink")

  * Mar 16, 2007 2:51am  Mar 16, 2007 2:51am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar19504_4.gif) 1Sundevil](1sundevil)

  * | Joined Sep 2006  | Status: Trader | [228 Posts](/search?do=process&provider=Member&searchuser=19504)

CAD hit my -40 SL. I'm surprised that the EA didn't trigger a "BUY" around 1.1755. Very strange.  
  
[http://i141.photobucket.com/albums/r...0/badtrade.gif](http://i141.photobucket.com/albums/r51/sundevil520/badtrade.gif)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#423](/thread/post/245204#post245204 "Post Permalink")

  * Mar 16, 2007 3:29am  Mar 16, 2007 3:29am 

  * [ tnh_z](tnh_z)

  * | Joined Apr 2006  | Status: Trader | [16 Posts](/search?do=process&provider=Member&searchuser=8205)

> [Quoting 1Sundevil](/thread/post/245115#post245115 "View Quoted Post")
> 
> Disliked
> 
> For the most part this whole test is using the default setting. I did change the SL to -50 early on as many of us felt that it needed room to "breath" in case it went against us initially. I had a few trades that came within ONE pip of going -50 before turning around to hit my TP. I've now adjusted my SL to -40 and my TP to +20 in order to see if I can better my results.  
>    
>  I'm using a MIG demo account. I also opened an Interbank demo and got absolutely horrible results. Why the difference? I have no idea.  
>    
>  Here's a graph that shows what the EA has done on MIG since I started it on 2/16:  
>  [http://i141.photobucket.com/albums/r...Statement2.gif](http://i141.photobucket.com/albums/r51/sundevil520/DetailedStatement2.gif)
> 
> Ignored

ok , thank you 1Sundevil.I start to tset original setting but this time with "true" on ConfirmedonEntry.  
have a good time. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#424](/thread/post/246507#post246507 "Post Permalink")

  * Mar 17, 2007 6:54am  Mar 17, 2007 6:54am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar19504_4.gif) 1Sundevil](1sundevil)

  * | Joined Sep 2006  | Status: Trader | [228 Posts](/search?do=process&provider=Member&searchuser=19504)

EA is still plugging away, and I feel that the +20 TP and the -40 SL has worked out thus far. Here's the account as of the close today:  
  
[http://i141.photobucket.com/albums/r...evil520/DS.gif](http://i141.photobucket.com/albums/r51/sundevil520/DS.gif)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#425](/thread/post/247626#post247626 "Post Permalink")

  * Mar 19, 2007 12:56pm  Mar 19, 2007 12:56pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar19504_4.gif) 1Sundevil](1sundevil)

  * | Joined Sep 2006  | Status: Trader | [228 Posts](/search?do=process&provider=Member&searchuser=19504)

Well, my 30 day MIG demo account is done. Here is what it did.  
  
The EA made 119 trades with an 80.7% winning percentage.   
  
My $50,000 demo account grew to $66,698.97, an increase of 33.4% (in 30 days)  
  
I am submitting the paperwork for an MIG live account this week. In the meantime I have opened another Demo account ($1,000,000...just for the hell of it) to continue my "tweaking". I hope to go "live" by the beginning of April. I'll keep updating as things move. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#426](/thread/post/247632#post247632 "Post Permalink")

  * Mar 19, 2007 1:10pm  Mar 19, 2007 1:10pm 

  * [ brentmack](brentmack)

  * | Joined Apr 2006  | Status: Commissioner of Autotrading | [462 Posts](/search?do=process&provider=Member&searchuser=8726)

> [Quoting 1Sundevil](/thread/post/247626#post247626 "View Quoted Post")
> 
> Disliked
> 
> Well, my 30 day MIG demo account is done. Here is what it did.
> 
> Ignored

1Sundevil -  
  
Thanks for a month's worth of dedicated testing. May you make a pile of pips when you go live with this. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#427](/thread/post/247933#post247933 "Post Permalink")

  * Mar 19, 2007 9:58pm  Mar 19, 2007 9:58pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar30695_4.gif) toti1972](toti1972)

  * | Joined Jan 2007  | Status: Trader | [107 Posts](/search?do=process&provider=Member&searchuser=30695)

> [Quoting 1Sundevil](/thread/post/247626#post247626 "View Quoted Post")
> 
> Disliked
> 
> Well, my 30 day MIG demo account is done. Here is what it did.  
>    
>  The EA made 119 trades with an 80.7% winning percentage.   
>    
>  My $50,000 demo account grew to $66,698.97, an increase of 33.4% (in 30 days)  
>    
>  I am submitting the paperwork for an MIG live account this week. In the meantime I have opened another Demo account ($1,000,000...just for the hell of it) to continue my "tweaking". I hope to go "live" by the beginning of April. I'll keep updating as things move.
> 
> Ignored

Hi mate,  
  
Thank you for your work, I see now you rule this thread, so please, keep us up to date on your results,   
Couple of questions here:  
I'd like to concentrate my trading in no more than 2 pairs...According to your research, which pairs show the better results?  
You said your acc grew 33%...What about your contract size? every trade the same? did you increase the contract size as long as your acc increases?  
did you set MM to true or false?  
what SL and TP gives better results?  
  
I see there are several people following this system...  
It'd be helpful for everyone to post their results here ...  
  
Sundevil, I wish you the very best trading this method live...  
  
Thanks... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#428](/thread/post/247990#post247990 "Post Permalink")

  * Mar 19, 2007 11:24pm  Mar 19, 2007 11:24pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar19504_4.gif) 1Sundevil](1sundevil)

  * | Joined Sep 2006  | Status: Trader | [228 Posts](/search?do=process&provider=Member&searchuser=19504)

> [Quoting toti1972](/thread/post/247933#post247933 "View Quoted Post")
> 
> Disliked
> 
> Hi mate,  
>    
>  Thank you for your work, I see now you rule this thread, so please, keep us up to date on your results,   
>  Couple of questions here:  
>  I'd like to concentrate my trading in no more than 2 pairs...According to your research, which pairs show the better results?  
>  You said your acc grew 33%...What about your contract size? every trade the same? did you increase the contract size as long as your acc increases?  
>  did you set MM to true or false?  
>  what SL and TP gives better results?  
>    
>  I see there are several people following this system...  
>  It'd be helpful for everyone to post their results here ...  
>    
>  Sundevil, I wish you the very best trading this method live...  
>    
>  Thanks...
> 
> Ignored

I know that the GBPUSD is getting the best results, but I'd have to look to see which is in second place. My guess would be either the GBPJPY or the EURJPY.   
  
The two that make me the most nervous are the USDCAD and USDCHF. This method really needs a currency pair that moves, as it is not designed to anticipate the "start" of a move, rather it gets in late. Thus a pair that is prone to larger swings will have a much better chance of hitting TP before it turns.  
  
MM is set to "true", so the EA increases and decreases lot size as to the account size at the time of the trade automatically. Right now I'm testing a +20 TP and a -40 SL. I still have to go back and look to see if the -10 pip differece in SL is warranted, but it seems to be for now.   
  
I've just opened a new Demo on MIG, so I will conitinue to test the EA over the next 30 days. The new Demo is $1,000,000 and it hit it's first trade last night (GBPUSD) for $19,800. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#429](/thread/post/248028#post248028 "Post Permalink")

  * Mar 20, 2007 12:25am  Mar 20, 2007 12:25am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar25698_4.gif) mikhaildgreat](mikhaildgreat)

  * | Joined Nov 2006  | Status: EA Programmer | [298 Posts](/search?do=process&provider=Member&searchuser=25698)

> [Quoting 1Sundevil](/thread/post/247990#post247990 "View Quoted Post")
> 
> Disliked
> 
> I know that the GBPUSD is getting the best results, but I'd have to look to see which is in second place. My guess would be either the GBPJPY or the EURJPY.   
>    
>  The two that make me the most nervous are the USDCAD and USDCHF. This method really needs a currency pair that moves, as it is not designed to anticipate the "start" of a move, rather it gets in late. Thus a pair that is prone to larger swings will have a much better chance of hitting TP before it turns.  
>    
>  MM is set to "true", so the EA increases and decreases lot size as to the account size at the time of the trade automatically. Right now I'm testing a +20 TP and a -40 SL. I still have to go back and look to see if the -10 pip differece in SL is warranted, but it seems to be for now.   
>    
>  I've just opened a new Demo on MIG, so I will conitinue to test the EA over the next 30 days. The new Demo is $1,000,000 and it hit it's first trade last night (GBPUSD) for $19,800.
> 
> Ignored

Hey Sundevil, Thank you for your dedication in forward testing this EA, may I suggest something since you just created a new Demo Account why don't you try risking more in MM, instead of the default 10% why don't pull it up a notch and bring it up to 25% or hell even make it 50%. the calculations for MM is based on Free Margin anyways so you'll never have to fear the margin call... Just a suggestion to make your forward testing a little more exciting, its real nice to see them big numbers (and them devil girls)![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)  
  
Good luck to you sundevil,   
Mikhail 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#430](/thread/post/248946#post248946 "Post Permalink")

  * Mar 20, 2007 10:21pm  Mar 20, 2007 10:21pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar28980_4.gif) anthonyrae](anthonyrae)

  * | Joined Dec 2006  | Status: Trader | [68 Posts](/search?do=process&provider=Member&searchuser=28980)

hi sundevil,  
  
congrats on the great results. I'm having trouble trying to get a successul/profitable backtest result using beta 3 on GBP/USD 30min. Doing everything as per the original system, but having no luck.  
  
any thoughts ? Thanks 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#431](/thread/post/249327#post249327 "Post Permalink")

  * Mar 21, 2007 4:34am  Mar 21, 2007 4:34am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar19504_4.gif) 1Sundevil](1sundevil)

  * | Joined Sep 2006  | Status: Trader | [228 Posts](/search?do=process&provider=Member&searchuser=19504)

why not just forward test with a demo account. It doesn't cost anything. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#432](/thread/post/249371#post249371 "Post Permalink")

  * Mar 21, 2007 5:25am  Mar 21, 2007 5:25am 

  * [ traderis](traderis)

  * | Joined Mar 2007  | Status: Trader | [37 Posts](/search?do=process&provider=Member&searchuser=35446)

> [Quoting 1Sundevil](/thread/post/249327#post249327 "View Quoted Post")
> 
> Disliked
> 
> why not just forward test with a demo account. It doesn't cost anything.
> 
> Ignored

Can you attack EA version you are using? Thanks! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#433](/thread/post/249416#post249416 "Post Permalink")

  * Mar 21, 2007 6:29am  Mar 21, 2007 6:29am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar19504_4.gif) 1Sundevil](1sundevil)

  * | Joined Sep 2006  | Status: Trader | [228 Posts](/search?do=process&provider=Member&searchuser=19504)

> [Quoting traderis](/thread/post/249371#post249371 "View Quoted Post")
> 
> Disliked
> 
> Can you attack EA version you are using? Thanks!
> 
> Ignored

It's still in this or the other thread. In one of the first pages. Beta3 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#434](/thread/post/251614#post251614 "Post Permalink")

  * Mar 23, 2007 5:19am  Mar 23, 2007 5:19am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar5604_4.gif) fingotrader](fingotrader)

  * | Joined Jan 2006  | Status: Go for it... | [101 Posts](/search?do=process&provider=Member&searchuser=5604)

Hi Mikhal,  
  
thanks for all your effort on this EA.  
  
I am about to test the EA and have a few questions:  
  
How do I totally disable the TS, set TrailStopType to "0" or?  
  
If I will use the TS to trail AFTER my originally tp is hit, how do I set it?  
  
Thank you very much,  
  
FT 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#435](/thread/post/251671#post251671 "Post Permalink")

  * Mar 23, 2007 6:16am  Mar 23, 2007 6:16am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar25698_4.gif) mikhaildgreat](mikhaildgreat)

  * | Joined Nov 2006  | Status: EA Programmer | [298 Posts](/search?do=process&provider=Member&searchuser=25698)

> [Quoting fingotrader](/thread/post/251614#post251614 "View Quoted Post")
> 
> Disliked
> 
> Hi Mikhal,  
>    
>  thanks for all your effort on this EA.  
>    
>  I am about to test the EA and have a few questions:  
>    
>  How do I totally disable the TS, set TrailStopType to "0" or?  
>    
>  If I will use the TS to trail AFTER my originally tp is hit, how do I set it?  
>    
>  Thank you very much,  
>    
>  FT
> 
> Ignored

if you want to disable TS set trailing stop = 0;  
  
If you want ts to activate only after a certain profit is met set TStype = 1, TStype = 2 will immediatly activate the as soon a market moves 1 pip in your favor.  
  
Good luck,  
Mikhail 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#436](/thread/post/251758#post251758 "Post Permalink")

  * Edited 8:08am  Mar 23, 2007 7:51am | Edited 8:08am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar5604_4.gif) fingotrader](fingotrader)

  * | Joined Jan 2006  | Status: Go for it... | [101 Posts](/search?do=process&provider=Member&searchuser=5604)

Hi Mikhail,  
  
thanks for your quick reply.  
  
So if I wanna try ie TP 100 and a trail stop at 25, **after** the 100 TP is reached/locked in, I then set the setting to TStype 1 and then 25 pip trailingstop?  
  
Does the "breakevenafterpips" have any affect on the above? I have set this to 50.  
  
About the SL:  
  
If i have a fixed SL at say 50, but there is a valid oppsiste signal, at say -43, will the EA stop out  
and reverse the trade, even the -50 SL has not been hit or will it wait until -50 and then reverse?  
  
  
Thanks for your help,  
  
FT  
  
  
  
  

> [Quoting mikhaildgreat](/thread/post/251671#post251671 "View Quoted Post")
> 
> Disliked
> 
> if you want to disable TS set trailing stop = 0;  
>    
>  If you want ts to activate only after a certain profit is met set TStype = 1, TStype = 2 will immediatly activate the as soon a market moves 1 pip in your favor.  
>    
>  Good luck,  
>  Mikhail
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#437](/thread/post/252086#post252086 "Post Permalink")

  * Mar 23, 2007 3:16pm  Mar 23, 2007 3:16pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar25698_4.gif) mikhaildgreat](mikhaildgreat)

  * | Joined Nov 2006  | Status: EA Programmer | [298 Posts](/search?do=process&provider=Member&searchuser=25698)

No the EA will not stop and Reverse. Breakeven and TrailStop will work indepedently of each other use any value you prefer. just experement and backtest the EA to see how it works.  
  
Good Luck,  
Mikhail  

> [Quoting fingotrader](/thread/post/251758#post251758 "View Quoted Post")
> 
> Disliked
> 
> Hi Mikhail,  
>    
>  thanks for your quick reply.  
>    
>  So if I wanna try ie TP 100 and a trail stop at 25, **after** the 100 TP is reached/locked in, I then set the setting to TStype 1 and then 25 pip trailingstop?  
>    
>  Does the "breakevenafterpips" have any affect on the above? I have set this to 50.  
>    
>  About the SL:  
>    
>  If i have a fixed SL at say 50, but there is a valid oppsiste signal, at say -43, will the EA stop out  
>  and reverse the trade, even the -50 SL has not been hit or will it wait until -50 and then reverse?  
>    
>    
>  Thanks for your help,  
>    
>  FT
> 
> Ignored

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#438](/thread/post/252487#post252487 "Post Permalink")

  * Mar 23, 2007 11:57pm  Mar 23, 2007 11:57pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar19504_4.gif) 1Sundevil](1sundevil)

  * | Joined Sep 2006  | Status: Trader | [228 Posts](/search?do=process&provider=Member&searchuser=19504)

My new demo test is not working anywhere near as well as the first one. So far it is only 6 for 14 and the account is down 16%. I'm using some different currency pairs and I'm going to see if I made any other changes. The GBPUSD, which was such a big winner for this EA the first go around, is now ZERO for 3. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#439](/thread/post/252850#post252850 "Post Permalink")

  * Mar 24, 2007 9:39am  Mar 24, 2007 9:39am 

  * [ brentmack](brentmack)

  * | Joined Apr 2006  | Status: Commissioner of Autotrading | [462 Posts](/search?do=process&provider=Member&searchuser=8726)

> [Quoting 1Sundevil](/thread/post/252487#post252487 "View Quoted Post")
> 
> Disliked
> 
> So far it is only 6 for 14 and the account is down 16%.
> 
> Ignored

That's bad news. It's going to make next week pretty interesting.  
  
I ran Beta3 for a day or two and it was a net loser, but I still had hopes for it.  
  
Give it hell next week! ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#440](/thread/post/254237#post254237 "Post Permalink")

  * Mar 27, 2007 12:59am  Mar 27, 2007 12:59am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar19504_4.gif) 1Sundevil](1sundevil)

  * | Joined Sep 2006  | Status: Trader | [228 Posts](/search?do=process&provider=Member&searchuser=19504)

> [Quoting brentmack](/thread/post/252850#post252850 "View Quoted Post")
> 
> Disliked
> 
> That's bad news. It's going to make next week pretty interesting.  
>    
>  I ran Beta3 for a day or two and it was a net loser, but I still had hopes for it.  
>    
>  Give it hell next week! ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)
> 
> Ignored

It's very strange. I'm running six pairs, and here's how they break down on positive trades versus overall:  
EURAUD 3 of 4 (75%)  
USDJPY 3 of 4  
GBPCHF 2 of 3 (66%)  
EURJPY 2 of 3  
GBPJPY 1 of 2 (50%)  
  
**_GBPUSD 0 FOR 5!_**  
  
Right now the account ($1M) is down $163,195. The GBPUSD pair alone is accounts for $162,595 of that amount (99.6%).  
  
I'm trying to figure out what's different. I know I messed up the MACD setting early on, but that's been fixed now, and last night I went 4 for 5. But the GBP is making some strange calls. It's trading when it's "questionable" to do so and it's not hitting it's trade trigger when it seems obvious that it should. I'm going to keep this going and see if it gets back to where it was before. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * The Pouria EA Development Thread
  *   * [ **Reply to Thread** ](/thread/17242-the-pouria-ea-development-thread/reply#reply)

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

[The Pouria Method](/thread/17011-the-pouria-method "OKay here is one of the 4 best systems that I've made and used, with this system I pickup atleast 50 pips a day, I'm sharing this because...") 562 replies

[Lessons Learned during System Development](/thread/2986-lessons-learned-during-system-development "Hi, 
  
I've been reading through the forum and somehow I'm in the process of developing my own system.. But not really doing actual...") 29 replies

[(pouria method II on the test)](/thread/23104-pouria-method-ii-on-the-test "Hello  
pouria method II is now DONE thanks to the group of experts and mathematicians that helped and made this method. 
now we are...") 218 replies

[System Development Secrets](/thread/7342-system-development-secrets "&lt;meta http-equiv=&quot;CONTENT-TYPE&quot; content=&quot;text/html; charset=utf-8&quot;&gt;&lt;title&gt;&lt;/title&gt;&lt;meta name=&quot;GENERATOR&quot; content=&quot;OpenOffice.org 2.0 ...") 5 replies

[Metatrader 4 Development Course](/thread/5906-metatrader-4-development-course "Here is the Mql_4_Metatrader_4_Development_Course in pdf \(link fixed\) : 
 
http://www.freefilehosting.org/pupload/view/8711") 3 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/17242-the-pouria-ea-development-thread/reply#reply)
  * Subscribe
  * [45](javascript:void\(0\);)

Attachments: The Pouria EA Development Thread

Tags: The Pouria EA Development Thread

#  [](/thread/17242-the-pouria-ea-development-thread)The Pouria EA Development Thread 

  * 

  * [#441](/thread/post/254249#post254249 "Post Permalink")

  * Mar 27, 2007 1:07am  Mar 27, 2007 1:07am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar19504_4.gif) 1Sundevil](1sundevil)

  * | Joined Sep 2006  | Status: Trader | [228 Posts](/search?do=process&provider=Member&searchuser=19504)

One thing on the MACD indicators. I have them set to the 15, 26, 1, and then have them applied to the LOW.   
  
What I messed up on with the new demo was using the "custom" MACD without the "applied to" setting this time around. I'm hoping that is the reason for the bad start. Like I said, I fixed them and went 4 for 5 last night....the lone LOSER was of course the GBPUSD. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#442](/thread/post/254623#post254623 "Post Permalink")

  * Mar 27, 2007 10:34am  Mar 27, 2007 10:34am 

  * [ shaker22a](shaker22a)

  * | Joined Sep 2006  | Status: Trader | [10 Posts](/search?do=process&provider=Member&searchuser=18778)

hi all,  
  
yesterday 26/3 there was a good cross on the eur/usd but the ea didn't buy any ideas why?  
thnx in advance 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#443](/thread/post/255147#post255147 "Post Permalink")

  * Mar 27, 2007 11:57pm  Mar 27, 2007 11:57pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar19504_4.gif) 1Sundevil](1sundevil)

  * | Joined Sep 2006  | Status: Trader | [228 Posts](/search?do=process&provider=Member&searchuser=19504)

I don't know what's wrong, but things aren't getting better. The account is now down 25%. GBPUSD continues to be a big loser.  
  
I'm wondering if something was messed up when I lost all of my charts and data when I started the second demo. Having to reupload everything may have thrown it out of whack. I just have no idea why it's suddenly doing so bad when before it was doing so well. Went 2 for 5 yesterday. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#444](/thread/post/256375#post256375 "Post Permalink")

  * Mar 29, 2007 12:43am  Mar 29, 2007 12:43am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar19504_4.gif) 1Sundevil](1sundevil)

  * | Joined Sep 2006  | Status: Trader | [228 Posts](/search?do=process&provider=Member&searchuser=19504)

It's now 1 for 8!! The demo account ($1M) is down $244,285. The GbpUSD pair alone count for $209,333 of that!  
  
I'm trying to figure out how a pair can be such a big winner for this EA on a demo all of last month, and then such a HUGE loser in the last week on a new demo. Any ideas? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#445](/thread/post/256388#post256388 "Post Permalink")

  * Mar 29, 2007 1:06am  Mar 29, 2007 1:06am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar19504_4.gif) 1Sundevil](1sundevil)

  * | Joined Sep 2006  | Status: Trader | [228 Posts](/search?do=process&provider=Member&searchuser=19504)

I just looked, and in the last demo the GBPUSD pair went 23 and 5, an 82% positive ratio.  
  
This demo has gone 1 and 7, a 12.5% positive ratio. can't figure it out. It's about to go 1 and 8!! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#446](/thread/post/256863#post256863 "Post Permalink")

  * Mar 29, 2007 9:09am  Mar 29, 2007 9:09am 

  * [ BearPaw](bearpaw)

  * | Joined Jul 2006  | Status: A Trader for Life | [218 Posts](/search?do=process&provider=Member&searchuser=13999)

That's why I stopped trading the GBP with beta 3. It had too many losers. I was confused when you kept on having winners. Then we thought it might be the feed...I was using ibfx and you were using migfx...  
  
Who knows....but thanks for all the testing.  
  
BP 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#447](/thread/post/257888#post257888 "Post Permalink")

  * Mar 30, 2007 5:08am  Mar 30, 2007 5:08am 

  * [ brentmack](brentmack)

  * | Joined Apr 2006  | Status: Commissioner of Autotrading | [462 Posts](/search?do=process&provider=Member&searchuser=8726)

> [Quoting 1Sundevil](/thread/post/256388#post256388 "View Quoted Post")
> 
> Disliked
> 
> I just looked, and in the last demo the GBPUSD pair went 23 and 5, an 82% positive ratio. This demo has gone 1 and 7, a 12.5% positive ratio. can't figure it out. It's about to go 1 and 8!!
> 
> Ignored

Sundevil -   
  
And you were all set for Easy Street. This sucks... ![](https://resources.faireconomy.media/images/emojis/64/1f633.png?v=15.1)  
  
I haven't looked at the charts, so this is why I ask - is there any kind of difference in the price action, i.e., ranging vs. trending?  
  
Is the stop/loss at the same level? I believe you've used both 40 and 50 for S/L - and you may have changed in mid-stream. Only you would know for sure.   
  
Perhaps you were getting lucky with the change to 40 S/L? How much are your recent trades missing the mark by?  
  
If nothing turns up there - I'd do the obvious thing. Stop trading the pair and see if the EA can continue to profit from the remaining pairs.  
  
This could be a problem that migrates from pair to pair, essentially rendering the EA useless.  
  
However, if the performance for all of the other pairs is roughly consistent from month to month - you've probably got a subtle flaw or change somewhere within the code that you're overlooking.  
  
P.S. Here's another bright idea... I believe that there are updated versions of this EA available. Look into running both of them. I know this will make your record keeping a lot tougher - but you've got to get to the bottom of this. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#448](/thread/post/258141#post258141 "Post Permalink")

  * Mar 30, 2007 11:51am  Mar 30, 2007 11:51am 

  * [ tnh_z](tnh_z)

  * | Joined Apr 2006  | Status: Trader | [16 Posts](/search?do=process&provider=Member&searchuser=8205)

> [Quoting BearPaw](/thread/post/256863#post256863 "View Quoted Post")
> 
> Disliked
> 
> ....It had too many losers. I was confused when you kept on having winners. ...  
>    
>  BP
> 
> Ignored

exactly like me.I used Alpari demo and got bad results on all pairs except eurchf, nzdusd and eurjpy.But realy can I trust and run EA on real account on these three pairs? I think there is no guarantee for being real like demo!! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#449](/thread/post/258821#post258821 "Post Permalink")

  * Mar 31, 2007 3:28am  Mar 31, 2007 3:28am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar19504_4.gif) 1Sundevil](1sundevil)

  * | Joined Sep 2006  | Status: Trader | [228 Posts](/search?do=process&provider=Member&searchuser=19504)

I dumped that last demo and reopened another one and reset all of my charts etc.. So far the EA has dropped me into 14 trades and I'm 9 for 14. More importantly the GBPUSD is now 3 for 3. The GBPCHF is 0 for 3. This was one of my "new" currencies that I wanted to test. If it doesn't look good through next week I'll drop it.   
  
Another thing I've been thinking. I've been trying to use 6 different currencies. Why? I have no idea. I may just find the best four and see how that effects my account.  
  
I don't know what happened with the last demo, but things "appear" to be back on track with the new one. We'll see. My "live" MIG account has been apporved, but I want to test this a little more to find the best combinatio of pairs and settings first. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#450](/thread/post/258831#post258831 "Post Permalink")

  * Mar 31, 2007 3:43am  Mar 31, 2007 3:43am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar1668_4.gif) traderone](traderone)

  * | Joined Feb 2005  | Status: Trader | [392 Posts](/search?do=process&provider=Member&searchuser=1668)

Is there some reason you thought your demo was invalid? I would caution against ignoring a "bad test". That is really why we test these things. I know that we all really want the EA to be successful, but we shouldn't ignore a bad run. They happen too often on LIVE accounts. 

Don Life is expensive, but includes a free trip around the sun.

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#451](/thread/post/258870#post258870 "Post Permalink")

  * Edited 4:49am  Mar 31, 2007 4:35am | Edited 4:49am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar19504_4.gif) 1Sundevil](1sundevil)

  * | Joined Sep 2006  | Status: Trader | [228 Posts](/search?do=process&provider=Member&searchuser=19504)

> [Quoting traderone](/thread/post/258831#post258831 "View Quoted Post")
> 
> Disliked
> 
> Is there some reason you thought your demo was invalid? I would caution against ignoring a "bad test". That is really why we test these things. I know that we all really want the EA to be successful, but we shouldn't ignore a bad run. They happen too often on LIVE accounts.
> 
> Ignored

When I opened up a second demo, after one day the account froze and all of my charts disappeared. So I opened up another demo and had to re-do everything, and that is the one that did terrible. The telling sign for me was the GBPUSD pair. It went 25 for 28 in the first 30 day test and 1 for 9 in the second 3 day test. That's not a coincidence.  
  
I'm not ignoring it, but it was so far to the other end of the spectrum that it just screamed "something's wrong". That's why I closed it and opened up a new demo to further test this EA. If this one doesn't do well then we'll have to tinker some more. So far the GBPUSD has gone 3 for 3. 1 day down, 29 to go. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#452](/thread/post/260438#post260438 "Post Permalink")

  * Apr 2, 2007 10:55pm  Apr 2, 2007 10:55pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar19504_4.gif) 1Sundevil](1sundevil)

  * | Joined Sep 2006  | Status: Trader | [228 Posts](/search?do=process&provider=Member&searchuser=19504)

Well, the new demo isn't as bad as the last one, but certainly ot as good as the first. Now, I am using different pairs and different SL's and TP's, so we'll see, but this also has me thinking.  
  
I sent Mikhaildgreat a private message and asked him about the possibility of creating an "Anti-Pouria EA". Basically everything would be the same except where the EA is programmed to "buy" right now it would "sell" and vice versa. I can see many times where the EA has dropped me into "sell" trades at the bottom of a move, or "buy" trades at the top. It hits my SL with ease and was never a threat to hit my TP.  
  
Given that it appears easy to find pairs that DON'T work and hit the -40 SL way before they would ever hit a +15 or +20 TP, it stands to reason that if we reversed the two (+40 TP and -20 SL) we would have a big winner with little drawdown. Sometimes finding an EA that consistantly doesn't work can be just as good as finding one that does.  
What do you guys think about this idea? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#453](/thread/post/260531#post260531 "Post Permalink")

  * Apr 3, 2007 12:57am  Apr 3, 2007 12:57am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar25698_4.gif) mikhaildgreat](mikhaildgreat)

  * | Joined Nov 2006  | Status: EA Programmer | [298 Posts](/search?do=process&provider=Member&searchuser=25698)

Heres your Anti-Pouria sundevil... Enjoy!  
  
Mikhail 

Attached File(s)

![File Type: mq4](https://assets.faireconomy.media/images/attach/mq4.gif) [Anti- Pouria EA Beta 3.mq4](/attachment/file/27643?d=1175529412) 12 KB | 769 downloads 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#454](/thread/post/260724#post260724 "Post Permalink")

  * Apr 3, 2007 4:51am  Apr 3, 2007 4:51am 

  * [ BearPaw](bearpaw)

  * | Joined Jul 2006  | Status: A Trader for Life | [218 Posts](/search?do=process&provider=Member&searchuser=13999)

> [Quoting 1Sundevil](/thread/post/260438#post260438 "View Quoted Post")
> 
> Disliked
> 
> Well, the new demo isn't as bad as the last one, but certainly ot as good as the first. Now, I am using different pairs and different SL's and TP's, so we'll see, but this also has me thinking.  
>    
>  I sent Mikhaildgreat a private message and asked him about the possibility of creating an "Anti-Pouria EA". Basically everything would be the same except where the EA is programmed to "buy" right now it would "sell" and vice versa. I can see many times where the EA has dropped me into "sell" trades at the bottom of a move, or "buy" trades at the top. It hits my SL with ease and was never a threat to hit my TP.  
>    
>  Given that it appears easy to find pairs that DON'T work and hit the -40 SL way before they would ever hit a +15 or +20 TP, it stands to reason that if we reversed the two (+40 TP and -20 SL) we would have a big winner with little drawdown. Sometimes finding an EA that consistantly doesn't work can be just as good as finding one that does.  
>  What do you guys think about this idea?
> 
> Ignored

Good idea Sundevil....lets see how she does.  
  
BP 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#455](/thread/post/260877#post260877 "Post Permalink")

  * Apr 3, 2007 8:30am  Apr 3, 2007 8:30am 

  * [ brentmack](brentmack)

  * | Joined Apr 2006  | Status: Commissioner of Autotrading | [462 Posts](/search?do=process&provider=Member&searchuser=8726)

> [Quoting 1Sundevil](/thread/post/260438#post260438 "View Quoted Post")
> 
> Disliked
> 
> Basically everything would be the same except where the EA is programmed to "buy" right now it would "sell" and vice versa.   
>  What do you guys think about this idea?
> 
> Ignored

I have no great expectations - other than be greatly amused. ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)   
  
If successful, this will be one of the great feats in FF history - running an EA backwards and producing profit.  
  
This is going to be great. Let the testing begin, SunDevil! 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#456](/thread/post/261071#post261071 "Post Permalink")

  * Apr 3, 2007 1:47pm  Apr 3, 2007 1:47pm 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar19504_4.gif) 1Sundevil](1sundevil)

  * | Joined Sep 2006  | Status: Trader | [228 Posts](/search?do=process&provider=Member&searchuser=19504)

> [Quoting brentmack](/thread/post/260877#post260877 "View Quoted Post")
> 
> Disliked
> 
> I have no great expectations - other than be greatly amused. ![](https://resources.faireconomy.media/images/emojis/64/1f601.png?v=15.1)   
>    
>  If successful, this will be one of the great feats in FF history - running an EA backwards and producing profit.  
>    
>  This is going to be great. Let the testing begin, SunDevil!
> 
> Ignored

This should be interesting to say the least! I opened an Interbank FX demo account, as I couldn't figure out how to open another MIG account to run simultaniously with the regular Pouria EA that I'm still testing. No worries as I earlier had terrible results with Interbank, so this should be fun.  
  
Everything is up and running. I'll see what it did overnight when I wake up. I'm using +40 for TP and -20 for SL and have set the "confirm" to true, so everything is like the regular demo testing. I'm using the GBPUSD, EURUSD, USDCHF, USDJPY, GBPJPY and GBPCHF. I think the GBPUSD and the USDCHF are the wildcards. If they don't work well I'll exchange one for the EURAUD as it's been doing bad on the other test.  
  
If this works I will laugh my a$$ off! If it doesn't here, I'll retest on MIG. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#457](/thread/post/261569#post261569 "Post Permalink")

  * Apr 4, 2007 12:28am  Apr 4, 2007 12:28am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar19504_4.gif) 1Sundevil](1sundevil)

  * | Joined Sep 2006  | Status: Trader | [228 Posts](/search?do=process&provider=Member&searchuser=19504)

well, the Anti-Pouria took two trades last night that are both positive right now. here's a chart of the EURUSD, it's a thing of beauty, just scroll to the right:  
  
[http://i141.photobucket.com/albums/r...l520/chart.gif](http://i141.photobucket.com/albums/r51/sundevil520/chart.gif)

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#458](/thread/post/262956#post262956 "Post Permalink")

  * Apr 5, 2007 2:27am  Apr 5, 2007 2:27am 

  * [ BearPaw](bearpaw)

  * | Joined Jul 2006  | Status: A Trader for Life | [218 Posts](/search?do=process&provider=Member&searchuser=13999)

Had some computer problems...but was going to set up anti and pouria together....  
  
Hopefully will get to it by tomorrow.  
  
BP 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#459](/thread/post/263093#post263093 "Post Permalink")

  * Apr 5, 2007 4:44am  Apr 5, 2007 4:44am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar19504_4.gif) 1Sundevil](1sundevil)

  * | Joined Sep 2006  | Status: Trader | [228 Posts](/search?do=process&provider=Member&searchuser=19504)

> [Quoting BearPaw](/thread/post/262956#post262956 "View Quoted Post")
> 
> Disliked
> 
> Had some computer problems...but was going to set up anti and pouria together....  
>    
>  Hopefully will get to it by tomorrow.  
>    
>  BP
> 
> Ignored

I have the anti-pouria running on both MIG and Interbank demo's to compare. This should be very interesting as I'm still adjusting the TP and SL to find the optimal setting. 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#460](/thread/post/1607976#post1607976 "Post Permalink")

  * Sep 24, 2007 12:03pm  Sep 24, 2007 12:03pm 

  * [ santacruzrepres](santacruzrepres)

  * | Joined Dec 2006  | Status: Trader | [1 Post](/search?do=process&provider=Member&searchuser=28745)

I to have an idea, to make that this 01 EA alone buys or venda time alone, to each crossing on the 02 red lines, I to think that it goes to give certain, that they find? MIKHAILDGREAT  
it could make this? 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * The Pouria EA Development Thread
  *   * [ **Reply to Thread** ](/thread/17242-the-pouria-ea-development-thread/reply#reply)

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

[The Pouria Method](/thread/17011-the-pouria-method "OKay here is one of the 4 best systems that I've made and used, with this system I pickup atleast 50 pips a day, I'm sharing this because...") 562 replies

[Lessons Learned during System Development](/thread/2986-lessons-learned-during-system-development "Hi, 
  
I've been reading through the forum and somehow I'm in the process of developing my own system.. But not really doing actual...") 29 replies

[(pouria method II on the test)](/thread/23104-pouria-method-ii-on-the-test "Hello  
pouria method II is now DONE thanks to the group of experts and mathematicians that helped and made this method. 
now we are...") 218 replies

[System Development Secrets](/thread/7342-system-development-secrets "&lt;meta http-equiv=&quot;CONTENT-TYPE&quot; content=&quot;text/html; charset=utf-8&quot;&gt;&lt;title&gt;&lt;/title&gt;&lt;meta name=&quot;GENERATOR&quot; content=&quot;OpenOffice.org 2.0 ...") 5 replies

[Metatrader 4 Development Course](/thread/5906-metatrader-4-development-course "Here is the Mql_4_Metatrader_4_Development_Course in pdf \(link fixed\) : 
 
http://www.freefilehosting.org/pupload/view/8711") 3 replies

![](https://resources.faireconomy.media/images/logos/logo-print-ff.png)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  *   * [ **Reply to Thread** ](/thread/17242-the-pouria-ea-development-thread/reply#reply)
  * Subscribe
  * [45](javascript:void\(0\);)

Attachments: The Pouria EA Development Thread

Tags: The Pouria EA Development Thread

#  [](/thread/17242-the-pouria-ea-development-thread)The Pouria EA Development Thread 

  * 

  * [#461](/thread/post/1758817#post1758817 "Post Permalink")

  * Dec 14, 2007 9:18am  Dec 14, 2007 9:18am 

  * [![](https://assets.faireconomy.media/nfs/customavatars/thumbs/medium/avatar53444_2.gif) dagoods](dagoods)

  * Joined Nov 2007 | Status: Trader | [3,059 Posts](/search?do=process&provider=Member&searchuser=53444)

the original system was a scalp sysytem looking for small pip gain at 98% win loss ration this thread has seemd to evolve it to a differnt system altogether if you diregard the essence of the original system which is to scalp in a very tight sl an tp ratio ... how does it perform with the original parameters with a broker with low [spreads](/brokers/spreads "View Live Spreads on the Broker Guide") like efx like the creator uses? lets get back to the original system that had 98% win ratio instead of trying to be greedy and increase sl and tp which is NOT the sysytem 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [#462](/thread/post/2791684#post2791684 "Post Permalink")

  * Last Post: Jun 10, 2009 10:52am  Jun 10, 2009 10:52am 

  * [ buffalopip](buffalopip)

  * | Joined Apr 2008  | Status: Trader | [95 Posts](/search?do=process&provider=Member&searchuser=67264)

After reading this thread and the original thread , it appears the original settings appear to be the best settings for a constant profit .... after all we're all here to make profits no matter how they are made . As time goes on that profit turns into powerful small steps to make more profit .... 

[0 ](javascript:void\(0\);) [0 ](javascript:void\(0\);)

  * [Trading Systems](/forum/71-trading-systems)
  * /
  * The Pouria EA Development Thread
  *   * [ **Reply to Thread** ](/thread/17242-the-pouria-ea-development-thread/reply#reply)

[](https://www.forexfactory.com "Homepage")

  * [Forums](forums)
  * [Trades](trades)
  * [Calendar](calendar)
  * [News](news)
  * [Market](market)
  * [Brokers](brokers)

****

[](https://www.faireconomy.com/)
