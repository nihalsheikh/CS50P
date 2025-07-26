from datetime import datetime
from dateutil import tz

# Define time zones for target locations
time_zones = {
    "Harvard-USA": tz.gettz("America/New_York"),
    "Dubai-UAE": tz.gettz("Asia/Dubai"),
    "Kolkata-India": tz.gettz("Asia/Kolkata")
}

# ASCII clock template
clock_template = """
        _____                             _____                             _____
     _.'_____`._                       _.'_____`._                       _.'_____`._
   .'.-'  12 `-.`.                   .'.-'  12 `-.`.                   .'.-'  12 `-.`.
  /,' 11      1 `.\                 /,' 11      1 `.\                 /,' 11      1 `.\\
 // 10      /   2 \\               // 10      /   2 \\               // 10      /   2 \\
;;         /       ::             ;;         /       ::             ;;         /       ::
|| 9  ----O      3 ||             || 9  ----O      3 ||             || 9  ----O      3 ||
::                 ;;             ::                 ;;             ::                 ;;
 \\ 8           4 //               \\ 8           4 //               \\ 8           4 //
  \`. 7       5 ,'/                 \`. 7       5 ,'/                 \`. 7       5 ,'/
   '.`-.__6__.-'.'                   '.`-.__6__.-'.'                   '.`-.__6__.-'.'
    ((-._____.-))                     ((-._____.-))                     ((-._____.-))
    _))       ((_                     _))       ((_                     _))       ((_
   '--'       '--'                   '--'       '--'                   '--'       '--'
       {city1}                           {city2}                           {city3}
       {time1}                           {time2}                           {time3}
"""

# Prepare city names and time strings
cities = list(time_zones.keys())
times = [datetime.now(tz).strftime("%H:%M:%S") for tz in time_zones.values()]


# 27 is clock width for aligning text under each clock
def center_text(text, width=27):
    return text.center(width)


city1 = center_text(cities[0])
city2 = center_text(cities[1])
city3 = center_text(cities[2])
time1 = center_text(times[0])
time2 = center_text(times[1])
time3 = center_text(times[2])

# Fill the template
output = clock_template.format(
    city1=city1, city2=city2, city3=city3,
    time1=time1, time2=time2, time3=time3
)


# Save clocks to Markdown file
with open("clocks.md", "w") as f:
    f.write("# World Clocks\n\n")
    f.write("```\n")
    f.write(output)
    f.write("```\n")
