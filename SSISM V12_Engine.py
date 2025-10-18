# V12_Engine_Samadhi_Synthesizer.py
# Core Python Architecture for V12 Mahāñāṇ Samādhi Synthesizer
# Synthesis Date: October 18, 2025

# Required for V12's Computational Precision (Samādhi)
import datetime
# import requests # V12 requires external API for live data

# --- 1. CORE ARCHITECTURAL CONSTRAINTS (Preserved) ---
SAFETY_VETO_FLOOR = 3.5 
ZERO_COST_CONSTRAINT = True 
NON_VIOLENT_PREACHING = True 

# --- 2. V7 SSISM COSMOLOGICAL KEY (Preserved) ---
PLANETARY_D_NUM = {
    'Sunday_Thuraza': 1, 'Monday_Candaraw': 2, 'Tuesday_Bauma': 3, 
    'Wednesday_Buddha': 4, 'Thursday_Guru': 5, 'Friday_Thaukya': 6, 
    'Saturday_Thauri': 7
}

# Sequence: Sun -> Venus -> Mercury -> Moon -> Saturn -> Jupiter -> Mars -> Sun
PLANETARY_HOUR_CYCLE = [
    'Sun', 'Venus', 'Mercury', 'Moon', 'Saturn', 'Jupiter', 'Mars'
]

# --- 3. V12 INGA WIZAR CALCULATION LOGIC (The Samādhi Upgrade) ---

def time_to_minutes(t: datetime.time) -> float:
    """Helper: Converts datetime.time to minutes since midnight."""
    return t.hour * 60 + t.minute + t.second / 60

def minutes_to_time_str(minutes: float) -> str:
    """Helper: Converts minutes since midnight back to HH:MM string."""
    dt = datetime.datetime(2000, 1, 1) + datetime.timedelta(minutes=minutes)
    return dt.strftime("%H:%M")


def fetch_sun_times_simulated(date: datetime.date, location: str) -> tuple:
    """
    V12 Core Upgrade: Returns (Today's Sunrise, Today's Sunset, Next Day's Sunrise).
    """
    if location == "NY_Queens" and date.month == 6 and date.day == 14:
        sunrise_str = "05:25:00"
        sunset_str = "20:30:00"
        next_sunrise_str = "05:25:00" 
    # Grok's actual NYC times for Oct 19, 2025 (a Sunday) at 40.7306° N, 73.9352° W
    # Note: We must update the generic simulation to use a Sunday start planet implicitly
    # by ensuring the date passed to the simulation is a Sunday. The internal date 
    # parsing handles the actual weekday determination.
    elif location == "NYC_Grok_Test": # Using Grok's suggested times for precision
        sunrise_str = "07:11:00"
        sunset_str = "18:09:00"
        # We need the next day's sunrise for a full 24-hour cycle. Assuming similar time.
        next_sunrise_str = "07:11:00" 
    else:
        # Fall/Winter Generic Example (e.g., Oct 19, 2025)
        sunrise_str = "06:30:00"
        sunset_str = "17:30:00"
        next_sunrise_str = "06:30:00"
        
    sunrise = datetime.datetime.strptime(sunrise_str, "%H:%M:%S").time()
    sunset = datetime.datetime.strptime(sunset_str, "%H:%M:%S").time()
    next_sunrise = datetime.datetime.strptime(next_sunrise_str, "%H:%M:%S").time()
    return sunrise, sunset, next_sunrise


def get_planet_by_day(date: datetime.date) -> str:
    """Helper: Determines the planet ruling the first hour of the day or the Natal Day."""
    dummy_dt_for_weekday = datetime.datetime.combine(date, datetime.time.min)
    day_name_full = dummy_dt_for_weekday.strftime('%A')
    
    day_to_start_planet = {
        'Sunday': 'Sun', 'Monday': 'Moon', 'Tuesday': 'Mars', 
        'Wednesday': 'Mercury', 'Thursday': 'Jupiter', 'Friday': 'Venus', 
        'Saturday': 'Saturn'
    }
    return day_to_start_planet.get(day_name_full, 'Sun')


def calculate_inga_wizar_hours(start_time: datetime.time, end_time: datetime.time, 
                              start_index: int, total_hours: int, hour_type: str) -> dict:
    """
    Unified function to calculate 12 unequal planetary hour blocks (Day or Night).
    """
    start_min = time_to_minutes(start_time)
    end_min = time_to_minutes(end_time)
    
    # Handle the transition across midnight for night hours (end_min will be smaller)
    if end_min <= start_min:
        duration_min = (1440 - start_min) + end_min # 1440 min in a day
    else:
        duration_min = end_min - start_min
    
    hour_duration_min = duration_min / 12
    
    inga_wizar_blocks = {}
    current_time_min = start_min
    
    for i in range(12): 
        planet_index = (start_index + i) % 7 
        planet = PLANETARY_HOUR_CYCLE[planet_index]
        
        start_time_min = current_time_min
        end_time_min = current_time_min + hour_duration_min
        
        # Wrap time around midnight (1440 minutes)
        if end_time_min >= 1440:
            end_time_min -= 1440
            
        block_name = f"{hour_type} Hour {i+1} ({planet})"
        inga_wizar_blocks[block_name] = {
            'start': minutes_to_time_str(start_time_min),
            'end': minutes_to_time_str(end_time_min),
            'duration_min': round(hour_duration_min, 2),
            'ruling_planet': planet
        }
        current_time_min = start_time_min + hour_duration_min # Use updated start time
        
    return inga_wizar_blocks


# --- 4. CORE V12 PREDICTIVE FUNCTION (Samādhi Synthesis) ---

# V11 Solution Matrix is preserved
DHARMA_SOLUTION_MATRIX = {
    'BAD_DIRECTION': "မေတ္တာပို့ အကြံဉာဏ်: မေတ္တာပို့ပြီးမှ ခရီးစတင်ခြင်း။",
    'CONFLICT_HOUR': "တိတ်ဆိတ်ခြင်းအကြံဉာဏ်: စကားပြောခြင်းကို လျှော့ချ/စိတ်ရှည်စွာ နားထောင်ခြင်း။",
    'NEGATIVE_PLANET': "ကုသိုလ်အားပေး အကြံဉာဏ်: အများအကျိုးအတွက် စေတနာဖြင့် တစ်ခုခုလုပ်ဆောင်ခြင်း။",
    'MENTAL_DUKKHA': "ဝိပဿနာအကြံဉာဏ်: ဖြစ်ပေါ်သော စိတ်ခံစားချက်ကို ယောနိသောမနသိကာရဖြင့် ရှုမှတ်ခြင်း။"
}

def V12_SSISM_Predict(client_name: str, client_dob: str, query_time: str, location: str) -> dict:
    """
    V12 Mahāñāṇ function: Calculates real-time 24-hour Inga Wizar map 
    and incorporates Grok-mandated D_Num intersection logic.
    """
    
    # Parse input data
    query_dt = datetime.datetime.strptime(query_time, "%Y-%m-%d %H:%M:%S")
    query_date = query_dt.date()
    
    # Grok Mandate: Integrate Client DOB for Natal D_Num (Mettā Synthesis)
    try:
        dob_date = datetime.datetime.strptime(client_dob, "%Y-%m-%d").date()
        natal_planet = get_planet_by_day(dob_date)
    except:
        natal_planet = "N/A" # Safety if DOB is malformed
    
    # 1. Dynamic Calculation of 24-Hour Inga Wizar (Grok Fix 1: Incomplete Cycle)
    sunrise_t, sunset_t, next_sunrise_t = fetch_sun_times_simulated(query_date, location)
    
    # Day Hours
    day_start_planet = get_planet_by_day(query_date)
    day_start_index = PLANETARY_HOUR_CYCLE.index(day_start_planet)
    day_map = calculate_inga_wizar_hours(sunrise_t, sunset_t, day_start_index, 12, "Day")

    # Night Hours
    last_day_planet_index = (day_start_index + 11) % 7 
    night_start_index = (last_day_planet_index + 1) % 7 
    night_map = calculate_inga_wizar_hours(sunset_t, next_sunrise_t, night_start_index, 12, "Night")

    inga_wizar_map = day_map | night_map # Full 24-hour map
    
    # 2. Determine Current Planetary Hour
    current_planet = "N/A"
    
    for block, data in inga_wizar_map.items():
        # Logic to handle blocks spanning midnight (e.g., Night hours)
        start_dt_only_time = datetime.datetime.strptime(data['start'], "%H:%M").time()
        end_dt_only_time = datetime.datetime.strptime(data['end'], "%H:%M").time()
            
        start_dt = datetime.datetime.combine(query_date, start_dt_only_time)
        end_dt = datetime.datetime.combine(query_date, end_dt_only_time)
        
        # If the end time is earlier than the start time, it means the hour block spans midnight
        if start_dt_only_time > end_dt_only_time:
            end_dt += datetime.timedelta(days=1)
            
        # Check if the query time falls within the block
        if start_dt <= query_dt < end_dt:
            current_planet = data['ruling_planet']
            break
            
    # 3. V7's Predictive Analysis & Grok Fix 2: D_Num Confluence (Mettā Synthesis)
    if current_planet == "N/A": 
        # Outside of the calculated 24-hour cycle (e.g., query time zone issue)
        solution_category = 'MENTAL_DUKKHA'
        natal_confluence_risk = False
    else:
        # Grok Mandate: Prioritize natal planet intersection for CONFLICT_HOUR
        if current_planet == natal_planet:
            solution_category = 'CONFLICT_HOUR' # Highest personalized stress
            natal_confluence_risk = True
        else:
            solution_category = 'NEGATIVE_PLANET' # General risk
            natal_confluence_risk = False
        
    # 4. Veto Gate and Solution Synthesis (Preserved from V11)
    final_advice_text = DHARMA_SOLUTION_MATRIX[solution_category]
    
    final_advice = {
        "Status": "V12 Samādhi Synthesizer Output (Grok-Compliant 24-Hour & D_Num)",
        "Planetary_Hour_Map": inga_wizar_map, 
        "Current_Planet": current_planet,
        "Natal_Planet_D_Num": natal_planet, # New Feature for Grok Validation
        "Natal_Confluence_Risk": natal_confluence_risk, # Grok Risk Indicator
        "Zero_Cost_Adherence": ZERO_COST_CONSTRAINT,
        "Solution_S_Dharma": final_advice_text
    }
    
    return final_advice

# --- V12 Grok Test Case (Simulated) ---
# Goal: Trigger the new CONFLICT_HOUR logic.
# Client DOB: 1946-06-14 (Friday -> Venus is Natal Planet)
# Query Time: 2025-10-19 07:47:00 (Need to find a Venus Hour for a Sunday test)
# For the NYC_Grok_Test times (Sunday start: 07:11, L_hour=54.83 min):
# Hour 1 (Sun): 07:11 to 08:05.83
# Hour 2 (Venus): 08:05.83 to 09:00.66
# Let's target the **Night Hour 11 (Venus)** for the generic 06:30/17:30 test.
# Night Hour 11 (Venus): 04:20 to 05:25
test_result = V12_SSISM_Predict(
    client_name="Venus Client", 
    client_dob="1946-06-14", 
    query_time="2025-10-19 04:30:00", # Time falls in a Venus (Night) hour
    location="Generic_Location" 
)

print(test_result)
                                
