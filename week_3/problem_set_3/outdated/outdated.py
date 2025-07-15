# Week 3: Problem 4
# Convert outdated date format to YYYY-MM-DD
def main():
    # List of months
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    # infinitely asking for correct input from user
    while True:
        try:
            # Taking date input from user
            date = input("Date: ")
            date = date.strip()

            # When Date format is in the Form: MM/DD/YYYY
            if "/" in date:
                mth, dt, yr = date.split(sep="/")
                yr = int(yr.strip())
                mth = int(mth.strip())
                dt = int(dt.strip())

                # when months are valid
                if 1 <= mth <= 12 and 1 <= dt <= 31:
                    print(f"{yr}-{mth:02d}-{dt:02d}")
                    break
                else:
                    continue

            # When Date format is in form: MONTH DATE, YEAR
            elif "," in date:
                # Split the format in to 2: (Month and Date) and Year
                m_d, yr = date.split(sep=",")

                # Split the format in to 2: Month and Date
                mth, dt = m_d.split(sep=" ")
                yr = int(yr.strip())
                dt = int(dt.strip())

                #  Change month into the format we want: in number
                if mth in months:
                    mth = months.index(mth) + 1

                    if 1 <= dt <= 31:
                        # print the new Format: YYYY-MM-DD
                        print(f"{yr}-{mth:02d}-{dt:02d}")
                        break
                    else:
                        continue
                else:
                    continue
            else:
                continue

        except (ValueError, IndexError):
            pass

main()
