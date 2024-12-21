import requests
import streamlit as st 


BASE_API_URL = "https://api.langflow.astra.datastax.com"
LANGFLOW_ID = "b06b7bac-aa20-45b3-a387-481bae5fc0ff"
FLOW_ID = "24c62346-3cbf-4855-b9fa-e79856b4911a"
APPLICATION_TOKEN = "AstraCS:DhDOUxZDIElmIFjQYwoLkiIP:c5e1c5691fdfc60f89d49183ef3283092f6429fd457f104cf52a05bb9cf67ca5"
ENDPOINT = "Tech_With_Tim_Endpoint" # The endpoint name of the flow



def run_flow(message: str) -> dict:

    api_url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/{ENDPOINT}"

    payload = {
        "input_value": message,
        "output_type": "chat",
        "input_type": "chat",
    }
  
    headers = {"Authorization": "Bearer " + APPLICATION_TOKEN, "Content-Type": "application/json"}
    response = requests.post(api_url, json=payload, headers=headers)
    return response.json()

def main():
    st.title("Customer Support Interface") 
    message = st.text_area("Message",  placeholder="Ask something...")

    if st.button("Run Flow"): 
        if not message.strip(): 
            st.error("Please enter a message") 
            return 
        
        try: 
            with st.spinner("Running flow..."):
                response = run_flow(message) 

            response = response['outputs'][0]["outputs"][0]["results"]["message"]["text"]
            st.markdown(response)
        except Exception as e: 
            st.error(str(e))
            
if __name__ == "__main__":
    main()
