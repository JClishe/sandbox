# Displays summarized disk usage of the top-level directories within the current folder. Adjust the 'd 1' argument to specify how many directories deep to summarize.
du -h -c -d 1

# -t threshold returns only files greater than the specified size. Ex "-t 100G"