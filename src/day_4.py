"""
--- Day 4: Passport Processing ---
You arrive at the airport only to realize that you grabbed your North Pole Credentials instead of your passport. 
While these documents are extremely similar, North Pole Credentials aren't issued by a country and therefore 
aren't actually valid documentation for travel in most of the world.

It seems like you're not the only one having problems, though; a very long line has formed for the automatic 
passport scanners, and the delay could upset your travel itinerary.

Due to some questionable network security, you realize you might be able to solve both of these problems at the 
same time.

The automatic passport scanners are slow because they're having trouble detecting which passports have all 
required fields. The expected fields are as follows:

byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID)

Passport data is validated in batch files (your puzzle input). Each passport is represented as a sequence of key:value pairs separated by spaces or newlines. Passports are separated by blank lines.

Here is an example batch file containing four passports:

ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in

The first passport is valid - all eight fields are present. 
The second passport is invalid - it is missing hgt (the Height field).
The third passport is interesting; the only missing field is cid, so it looks like data from North Pole 
Credentials, not a passport at all! Surely, nobody would mind if you made the system temporarily ignore missing 
cid fields. Treat this "passport" as valid.

The fourth passport is missing two fields, cid and byr. Missing cid is fine, but missing any other field is not, 
so this passport is invalid.

According to the above rules, your improved system would report 2 valid passports.

Count the number of valid passports - those that have all required fields. Treat cid as optional. In your batch 
file, how many passports are valid?

To begin, get your puzzle input.

--- Part Two ---

The line is moving more quickly now, but you overhear airport security talking about how passports with invalid 
data are getting through. Better add some data validation, quick!

You can continue to ignore the cid field, but each other field has strict rules about what values are valid for 
automatic validation:

byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
If cm, the number must be at least 150 and at most 193.
If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
cid (Country ID) - ignored, missing or not.

Your job is to count the passports where all required fields are both present and valid according to the above 
rules. Here are some example values:

byr valid:   2002
byr invalid: 2003

hgt valid:   60in
hgt valid:   190cm
hgt invalid: 190in
hgt invalid: 190

hcl valid:   #123abc
hcl invalid: #123abz
hcl invalid: 123abc

ecl valid:   brn
ecl invalid: wat

pid valid:   000000001
pid invalid: 0123456789

"""

def get_passport_validation_info(data, tags = {}):

    try:
        if not get_tags(data, tags):
            return False, f"{tags} has errors"
        
        required_tags = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

        for tag in required_tags:
            if not tag in tags.keys() or tags[tag] == "":
                return False, f"{tag} is missing"

        return True, ""

    except:
        return False, ""

def get_tags(data, tags = {}):
    try:
        for tag in data.split():
            dt = tag.split(":")
            name = dt[0].strip()
            value = dt[1].strip()
            tags[name] = value
        return True
    except:
        return False

def get_passport_validation_info2(data):

    def get_hgt_type():
        hgt_type = None
        hgt_value = None
        if not hgt_type: 
            try:
                hgt_cm_index = tags["hgt"].index("cm")
                hgt_value = int(tags["hgt"][:hgt_cm_index])
                hgt_type = tags["hgt"][hgt_cm_index:]
                return hgt_type, hgt_value
            except ValueError:
                hgt_type = None
        if not hgt_type: 
            try:
                hgt_in_index = tags["hgt"].index("in")
                hgt_value = int(tags["hgt"][:hgt_in_index])
                hgt_type = tags["hgt"][hgt_in_index:]
                return hgt_type, hgt_value
            except ValueError:
                hgt_type = None
        return hgt_type, hgt_value

    tags = {}

    try:
        is_valid, error = get_passport_validation_info(data, tags)
        if not is_valid:
            return False, error
        byr = int(tags["byr"])
        iyr = int(tags["iyr"])
        eyr = int(tags["eyr"])
        hcl = tags["hcl"]
        ecl = tags["ecl"]
        pid = tags["pid"]
        hgt_type, hgt_value = get_hgt_type()

        if not (byr >= 1920 and byr <= 2002):
            return False, f"byr is {byr} not in 1920 and 2002"
        if not (iyr >= 2010 and iyr <= 2020):
            return False, f"iyr is {iyr} not in 2010 and 2020"
        if not (eyr >= 2020 and eyr <= 2030):
            return False, f"eyr is {eyr} not in 2020 and 2030"
        if not (hgt_type == "cm" or hgt_type == "in"):
            return False, f"hgt type is {hgt_type} not 'cm' or 'in'"
        if hgt_type == "cm" and not (hgt_value >= 150 and hgt_value <= 193):
            return False, f"hgt type is {hgt_type} not in 150 and 193"
        if hgt_type == "in" and not ( hgt_value >= 59 and hgt_value <= 76):
            return False, f"hgt type is {hgt_type} not in 59 and 76"
        if not (hcl[:1] == "#" and len(hcl[1:]) == 6 and int(hcl[1:], 16)):
            return False, f"hcl is {hcl} not hex"
        if not (ecl in "blu brn gry grn hzl oth".split()):
            return False, f"ecl type is {ecl} blu brn gry grn hzl oth"
        if not (len([ch for ch in pid if ch in "0 1 2 3 4 5 6 7 8 9".split()]) == 9):
            return False, f"pid is {pid}, not in [000000000] and [999999999]"
        return True, ""
    except Exception as ex:
        return False, ex.__str__()
