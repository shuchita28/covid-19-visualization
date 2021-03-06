# Draw a line plot of cumulative cases vs. date, grouped and colored by is_china
# Define aesthetics within the line geom
plt_cum_confirmed_cases_china_vs_world <- ggplot((confirmed_cases_china_vs_world),
        aes(x=date,
            y=cum_cases,
            color = is_china)) +
  geom_line() +
  labs(title="China vs World", x="Date(Month)", y="Cumulative confirmed cases") 
  
# See the plot
plt_cum_confirmed_cases_china_vs_world

#is_china object not found
who_events <- tribble(
  ~ date, ~ event,
  "2020-01-30", "Global health\nemergency declared",
  "2020-03-11", "Pandemic\ndeclared",
  "2020-02-13", "China reporting\nchange"
) %>%
  mutate(date = as.Date(date))
  
who_events

# Using who_events, add vertical dashed lines with an xintercept at date
# and text at date, labeled by event, and at 100000 on the y-axis
plt_cum_confirmed_cases_china_vs_world +
  geom_vline(
              data=who_events,
              linetype="dashed",
              aes(xintercept=date)
            ) +
  geom_text( 
             aes(date,
                 label=event
                ),
             data=who_events,
             y=1e5
          )
