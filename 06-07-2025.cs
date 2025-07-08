/*
This problem was asked by Amazon.

You are given a list of data entries that represent entries and exits of groups of people into a building. An entry looks like this:

{"timestamp": 1526579928, count: 3, "type": "enter"}
This means 3 people entered the building. An exit looks like this:

{"timestamp": 1526580382, count: 2, "type": "exit"}
This means that 2 people exited the building. timestamp is in Unix time.

Find the busiest period in the building, that is, the time with the most people in the building.
Return it as a pair of (start, end) timestamps. 
You can assume the building always starts off and ends up empty, i.e. with 0 people inside.

*/ 



using System;
using System.Collections.Generic;

public class Event
{
    public int timestamp { get; set; }
    public int count { get; set; }
    public string type { get; set; }  // type for enter or exit 
}

public class BusiestPeriodFind
{
    public static Tuple<int, int> FindBusiestPeriod(List<Event> events)
    {
        events.Sort((a, b) => a.timestamp.CompareTo(b.timestamp));  // sort oldest to newest entrys 

        int maxPeople = 0;      // highest number people 
        int currentPeople = 0;  
        int busiestStartTime = 0;   // time of highest people start 
        int busiestEndTime = 0;     // time of highest people end  

        for (int i = 0; i < events.Count; i++)
        {
            var currentEvent = events[i];

            if (currentEvent.type == "enter")       // if enter add to count 
            {
                currentPeople += currentEvent.count;
            }   
            
            else if (currentEvent.type == "exit")   // if exit take away 
            {
                currentPeople -= currentEvent.count;
            }
            
            else  // basic error handling Exception
            {
                throw new Exception($"Unknown event type error: {currentEvent.type}");
            }
            
            bool isLastEvent = (i == events.Count - 1);   // check if last event and if it is set to current 
            int nextTimestamp = isLastEvent ? currentEvent.timestamp : events[i + 1].timestamp;

            if (currentPeople > maxPeople) // check if higher than past max 
            {
                maxPeople = currentPeople;
                busiestStartTime = currentEvent.timestamp;
                busiestEndTime = nextTimestamp;
            }
        }

        return Tuple.Create(busiestStartTime, busiestEndTime); // return start and end times of busiest 
    }

    // Testing 
    public static void Main()
    {
        var data = new List<Event> 
        {
            new Event { timestamp = 1526579928, count = 3, type = "enter" },
            new Event { timestamp = 1526580382, count = 2, type = "exit" },
            new Event { timestamp = 1526580385, count = 4, type = "enter" },
            new Event { timestamp = 1526580400, count = 3, type = "exit" },
            new Event { timestamp = 1526580415, count = 7, type = "enter" },
            new Event { timestamp = 1526580437, count = 2, type = "exit" },
            new Event { timestamp = 1526580550, count = 4, type = "enter" },
            new Event { timestamp = 1526580660, count = 3, type = "exit" }
        };

        var busiest = FindBusiestPeriod(data);
        Console.WriteLine($"Busiest period: Start = {busiest.Item1}, End = {busiest.Item2} "); // output 
    }
}
