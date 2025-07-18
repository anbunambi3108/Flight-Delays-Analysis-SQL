# app.py
import streamlit as st
import pandas as pd
import plotly.express as px

# --- PAGE CONFIGURATION ---
# Set the page configuration. This must be the first Streamlit command.
st.set_page_config(
    layout="wide",
    page_title="US Flight Delay Analysis Dashboard",
    page_icon="✈️"
)

# --- TITLE ---
st.title(" US Flight Delay Analysis Dashboard")
st.markdown("This dashboard analyzes US flight delay trends, causes, and high-risk routes from 2019 to 2023.")

# --- DATA LOADING ---
# Use a function with caching to load data for better performance.
# Using forward slashes in paths for cross-platform compatibility.
@st.cache_data
def load_data():
    try:
        base_path = 'C:/Users/anbun/Desktop/Portfolio projects/Flight-Delays-Analysis-SQL-main/result/'
        result1 = pd.read_csv(f'{base_path}result1.csv')
        result2 = pd.read_csv(f'{base_path}result2.csv')
        result3 = pd.read_csv(f'{base_path}result3.csv')
        result4 = pd.read_csv(f'{base_path}result4.csv')
        result5 = pd.read_csv(f'{base_path}result5.csv')
        result6 = pd.read_csv(f'{base_path}result6.csv')
        result7 = pd.read_csv(f'{base_path}result7.csv')
        result8 = pd.read_csv(f'{base_path}result8.csv')
        result9 = pd.read_csv(f'{base_path}result9.csv')
        result10 = pd.read_csv(f'{base_path}result10.csv')
        return result1, result2, result3, result4, result5, result6, result7, result8, result9, result10
    except FileNotFoundError as e:
        st.error(f"Error loading data file: {e}. Please ensure the CSV files are in the 'Flight-Delays-Analysis-SQL-main/result/' directory.")
        return (pd.DataFrame() for _ in range(10))

# Load all the dataframes
result1, result2, result3, result4, result5, result6, result7, result8, result9, result10 = load_data()


# --- SECTION 1: Delay Trends Over Time ---
with st.expander(" SECTION 1: Delay Trends Over Time", expanded=True):
    st.header("Visualizing Yearly Trends in Flights, Delays, and Cancellations")
    
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("1.1 Total Flights per Year")
        if not result1.empty:
            fig1 = px.bar(result1, x='Year', y='Total_Flights',
                          title='Total Number of Flights per Year',
                          labels={'Total_Flights': 'Total Flights', 'Year': 'Year'},
                          template='plotly_white')
            fig1.update_layout(title_x=0.5)
            st.plotly_chart(fig1, use_container_width=True)
        else:
            st.warning("Data for 'Total Flights per Year' is not available.")

        st.subheader("1.3 Total Cancellations per Year")
        if not result3.empty:
            fig3 = px.bar(result3, x='Year', y='Total_Cancellations',
                          title='Total Flight Cancellations per Year',
                          labels={'Total_Cancellations': 'Number of Cancellations', 'Year': 'Year'},
                          template='plotly_white')
            fig3.update_layout(title_x=0.5)
            st.plotly_chart(fig3, use_container_width=True)
        else:
            st.warning("Data for 'Total Cancellations per Year' is not available.")

    with col2:
        st.subheader("1.2 On-Time vs. Delayed Flights")
        if not result2.empty:
            fig2 = px.bar(result2, x='Year', y=['On_Time_Flights', 'Delayed_Flights'],
                          title='On-Time vs. Delayed Flights per Year',
                          labels={'value': 'Number of Flights', 'variable': 'Flight Status'},
                          barmode='stack', template='plotly_white')
            fig2.update_layout(title_x=0.5, legend_title_text='Flight Status')
            st.plotly_chart(fig2, use_container_width=True)
        else:
            st.warning("Data for 'On-Time vs. Delayed Flights' is not available.")

        st.subheader("1.4 Average Delays by Year")
        if not result4.empty:
            fig4 = px.bar(result4, x='Year',
                          y=['Average_Departure_Delay', 'Average_Arrival_Delay'],
                          title='Average Departure & Arrival Delay by Year',
                          labels={'value': 'Average Delay (minutes)', 'variable': 'Delay Type'},
                          barmode='group', template='plotly_white')
            fig4.update_layout(title_x=0.5, legend_title_text='Delay Type')
            st.plotly_chart(fig4, use_container_width=True)
        else:
            st.warning("Data for 'Average Delays by Year' is not available.")
    
    st.markdown("---")
    st.subheader("Section 1 Insights")
    st.markdown("""
    * **Total Flights & On-Time Performance:** 2019 had the most flights (~758K), but 2023 showed the worst delay rates (nearly 40%) despite lower volume — hinting at deeper operational inefficiencies rather than passenger demand.
        * *Why? This may point to staffing shortages, airline scheduling compression, or inefficient fleet management post-COVID.*
    * **Cancellations:** 2020's cancellation spike (~6%) aligns with the pandemic onset. Rates stabilized in 2023, but delays continued rising — suggesting the problem shifted from cancellations to delay management.
    * **Connecting the Dots:** As cancellation rates dropped but delays increased, airlines may have opted to avoid cancellations by padding schedules, inadvertently increasing delays and turnarounds.
    """)


# --- SECTION 2: Delay Causes ---
with st.expander(" SECTION 2: Analyzing the Causes of Delays", expanded=True):
    st.header("Breakdown of Delay Causes by Airport and Airline")

    if not result5.empty:
        # Data processing for this section
        df_causes = result5.copy()
        delay_types = ['Carrier_Delays', 'Weather_Delays', 'NAS_Delays', 'Security_Delays', 'Late_Aircraft_Delays']
        
        # Group by Destination
        dest_group = df_causes.groupby('DEST')[delay_types].sum().nlargest(10, columns=delay_types)
        dest_long = dest_group.reset_index().melt(id_vars='DEST', var_name='Delay Cause', value_name='Total Delay Minutes')

        # Group by Origin
        origin_group = df_causes.groupby('ORIGIN')[delay_types].sum().nlargest(10, columns=delay_types)
        origin_long = origin_group.reset_index().melt(id_vars='ORIGIN', var_name='Delay Cause', value_name='Total Delay Minutes')

        # Group by Airline
        airline_group = df_causes.groupby('AIRLINE')[delay_types].sum().nlargest(10, columns=delay_types)
        airline_long = airline_group.reset_index().melt(id_vars='AIRLINE', var_name='Delay Cause', value_name='Total Delay Minutes')

        st.subheader("2.1 Delay Causes for Top 10 Destination Airports")
        fig_dest = px.bar(dest_long, x='DEST', y='Total Delay Minutes', color='Delay Cause',
                          title='Total Delay Minutes by Cause for Top 10 Destination Airports',
                          labels={'DEST': 'Destination Airport'},
                          barmode='group', template='plotly_white')
        fig_dest.update_layout(title_x=0.5)
        st.plotly_chart(fig_dest, use_container_width=True)

        st.subheader("2.2 Delay Causes for Top 10 Origin Airports")
        fig_origin = px.bar(origin_long, x='ORIGIN', y='Total Delay Minutes', color='Delay Cause',
                            title='Total Delay Minutes by Cause for Top 10 Origin Airports',
                            labels={'ORIGIN': 'Origin Airport'},
                            barmode='group', template='plotly_white')
        fig_origin.update_layout(title_x=0.5)
        st.plotly_chart(fig_origin, use_container_width=True)

        st.subheader("2.3 Delay Causes for Top 10 Airlines")
        fig_airline = px.bar(airline_long, x='AIRLINE', y='Total Delay Minutes', color='Delay Cause',
                             title='Total Delay Minutes by Cause for Top 10 Airlines',
                             labels={'AIRLINE': 'Airline'},
                             barmode='group', template='plotly_white')
        fig_airline.update_layout(title_x=0.5)
        st.plotly_chart(fig_airline, use_container_width=True)
    else:
        st.warning("Data for 'Delay Causes' is not available.")

    st.markdown("---")
    st.subheader("Section 2 Insights")
    st.markdown("""
    * **Dominant Causes:** Late Aircraft and Carrier Delays were consistently the top causes — both internal and controllable. External causes (Weather, NAS, Security) were relatively low.
    * **Example (OGG–HNL):** Of 3,577 flights, 522 delays were from late aircraft and 517 from the carrier, while only 41 were from weather.
    * **Why This Matters:** These delays can be fixed. Airlines should optimize scheduling, crew rotations, and turnaround times.
    """)


# --- SECTION 3: Airport & Airline Bottlenecks ---
with st.expander("SECTION 3: Identifying Airport & Airline Bottlenecks", expanded=True):
    st.header("Pinpointing the Most Delay-Prone Airports and Airlines")
    
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("3.1 Top 10 Airports by Delay %")
        if not result6.empty:
            fig_airport_delay = px.bar(
                result6,
                x='ORIGIN',
                y='Departure_Delay_Percentage',
                title='Top 10 Airports by Departure Delay %',
                labels={'Departure_Delay_Percentage': 'Departure Delay (%)', 'ORIGIN': 'Airport Code'},
                template='plotly_white'
            )
            fig_airport_delay.update_layout(title_x=0.5)
            st.plotly_chart(fig_airport_delay, use_container_width=True)
        else:
            st.warning("Data for 'Top 10 Airports by Delay %' is not available.")

        st.subheader("3.2 Top 10 Airlines by Cancellation %")
        if not result8.empty:
            fig_cancel_pct = px.bar(
                result8,
                y='AIRLINE',
                x='Cancellation_Percentage',
                orientation='h',
                title='Top 10 Airlines by Cancellation %',
                labels={'Cancellation_Percentage': 'Cancellation Percentage (%)', 'AIRLINE': 'Airline'},
                template='plotly_white'
            )
            fig_cancel_pct.update_layout(yaxis={'categoryorder':'total ascending'}, title_x=0.5)
            st.plotly_chart(fig_cancel_pct, use_container_width=True)
        else:
            st.warning("Data for 'Top 10 Airlines by Cancellation %' is not available.")

    with col2:
        st.subheader("3.3 Top 10 Airlines by Average Delay")
        if not result7.empty:
            fig_airline_delay = px.bar(
                result7,
                y='AIRLINE',
                x='Average_Departure_Delay',
                orientation='h',
                title='Top 10 Airlines by Avg. Departure Delay',
                labels={'Average_Departure_Delay': 'Avg. Departure Delay (minutes)', 'AIRLINE': 'Airline'},
                template='plotly_white'
            )
            fig_airline_delay.update_layout(yaxis={'categoryorder':'total ascending'}, title_x=0.5)
            st.plotly_chart(fig_airline_delay, use_container_width=True)
        else:
            st.warning("Data for 'Top 10 Airlines by Average Delay' is not available.")

    st.markdown("---")
    st.subheader("Section 3 Insights")
    st.markdown("""
    * **Worst Airports:** Cold Bay (AK) leads with 71% delayed departures, but major hubs like MDW (Chicago) and HOU (Houston) are highly impacted too.
    * **Worst Airlines:** JetBlue, Frontier, and Allegiant are among the worst in both average delay and cancellation percentage. Delta and Hawaiian are the best-performing.
    * **Cross-link Insight:** The high-delay SEA-HOU route (from Section 4) is operated by airlines like Southwest, which is in the worst-performing group for cancellations. This connects specific route problems to broader airline performance issues.
    * **Why Low-Cost Airlines Struggle:** Their business model, which relies on tight scheduling and point-to-point routes, leaves less room for recovery from initial delays, causing a domino effect.
    """)


# --- SECTION 4: High-Risk Routes and Timings ---
with st.expander("SECTION 4: Identifying High-Risk Routes and Timings", expanded=True):
    st.header("Finding Consistently Delayed Routes and Problematic Departure Times")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("4.1 Top 10 Routes by Departure Delay %")
        if not result9.empty:
            fig_routes_dep = px.bar(
                result9,
                x='Route',
                y='Departure_Delay_Percentage',
                title='Top 10 Routes by Departure Delay %',
                labels={'Departure_Delay_Percentage': 'Departure Delay (%)', 'Route': 'Flight Route'},
                template='plotly_white'
            )
            fig_routes_dep.update_layout(title_x=0.5)
            st.plotly_chart(fig_routes_dep, use_container_width=True)
        else:
            st.warning("Data for 'Top 10 Routes by Departure Delay %' is not available.")

    with col2:
        st.subheader("4.2 Top 10 Routes by Arrival Delay %")
        if not result9.empty:
            fig_routes_arr = px.bar(
                result9,
                x='Route',
                y='Arrival_Delay_Percentage',
                title='Top 10 Routes by Arrival Delay %',
                labels={'Arrival_Delay_Percentage': 'Arrival Delay (%)', 'Route': 'Flight Route'},
                template='plotly_white'
            )
            fig_routes_arr.update_layout(title_x=0.5)
            st.plotly_chart(fig_routes_arr, use_container_width=True)
        else:
            st.warning("Data for 'Top 10 Routes by Arrival Delay %' is not available.")

    st.subheader("4.3 Impact of Departure Time on Delays")
    if not result10.empty:
        fig_time_delay = px.line(
            result10,
            x='CRS_DEP_TIME',
            y=['Departure_Delay_Percentage', 'Arrival_Delay_Percentage'],
            title='Impact of Scheduled Departure Time on Delay Percentages',
            labels={
                'CRS_DEP_TIME': 'Scheduled Departure Time (Hour of Day)',
                'value': 'Delay Percentage (%)',
                'variable': 'Delay Type'
            },
            template='plotly_white'
        )
        fig_time_delay.update_layout(title_x=0.5, legend_title_text='Delay Type')
        st.plotly_chart(fig_time_delay, use_container_width=True)
    else:
        st.warning("Data for 'Impact of Departure Time on Delays' is not available.")
    
    st.markdown("---")
    st.subheader("Section 4 Insights")
    st.markdown("""
    * **Worst Routes:** Routes like SEA–HOU and SJU–CVG had 100% delayed departures. Some routes catch up on arrival, suggesting intentional schedule padding to absorb delays.
    * **Time-of-Day Patterns:** High delay percentages are seen in 3–5 AM and 11 PM–12 AM windows. This may indicate issues with crew changes, overnight airport constraints, or early morning mechanical readiness.
    * **Cross-link:** The airports identified as bottlenecks in Section 3 (like MDW and HOU) are part of the high-risk routes in this section, confirming they are sources of structural, system-wide inefficiencies.
    """)

# --- RECOMMENDATIONS ---
with st.expander("Recommendations", expanded=True):
    st.header("Actionable Recommendations Based on Analysis")
    st.subheader("For Airlines")
    st.markdown("""
    * **Operational Efficiency:** Focus on improving turnaround efficiency and crew planning to reduce the top two causes of delays: 'Late Aircraft' and 'Carrier' issues.
    * **Contingency Planning:** Low-cost carriers in particular should re-evaluate buffer times and contingency routing to build more resilience into their tight schedules.
    """)
    st.subheader("For Passengers")
    st.markdown("""
    * **Strategic Booking:** Avoid flights departing late at night or very early in the morning, especially on known high-risk routes like SEA–HOU.
    * **Airline Choice:** For better on-time performance and lower cancellation risk, consider legacy carriers like Delta or Hawaiian, which consistently outperform their low-cost counterparts in this dataset.
    """)

# --- FOOTER ---
st.markdown("---")
st.caption("Created by Anbu Ezhilmathi Nambi | Powered by Streamlit & Plotly")

