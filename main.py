import streamlit as st

# Define function to filter logs
def filter_logs(logs, level=None, keyword=None):
    filtered_logs = []
    for log in logs:
        if level is not None and log.level != level:
            continue
        if keyword is not None and keyword not in log.message:
            continue
        filtered_logs.append(log)
    return filtered_logs

# Define your Log class with attributes like level, timestamp, message etc.
class Log:
    def __init__(self, level, timestamp, message):
        self.level = level
        self.timestamp = timestamp
        self.message = message

# Define your upload function
def upload_logs():
    uploaded_file = st.file_uploader("Upload Log File", type=["txt"])
    if uploaded_file is not None:
        file_contents = uploaded_file.read()
        logs = []
        for line in file_contents.decode("utf-8").split("\n"):
            if line:
                timestamp = line[:len('2023-02-20 11:30:39')]
                message=line[len('2023-02-20 11:30:39'):]
                level=message[4:9]
                message=message[9:]
                logs.append(Log(level,timestamp, message))
        return logs

# Define your main function for the Streamlit app
def main():
    st.title("Log Analyzer")

    # Upload logs
    logs = upload_logs()
    # Filter logs
    level = st.selectbox("Filter by Level", ["", "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"])
    keyword = st.text_input("Filter by Keyword")
    if logs is not None:
        filtered_logs = filter_logs(logs, level, keyword)
        st.write(f"Number of logs: {len(filtered_logs)}")
        for log in filtered_logs:
            st.write(f"{log.level}\t{log.timestamp}\t{log.message}")

if __name__ == "__main__":
    main()
