from playwright.sync_api import sync_playwright

def test_post_sap_vario():
    with sync_playwright() as playwright:
        token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0ZW5hbnRfaWQiOiI3NjRCRTdFOS1ENDIxLTQ2OUUtODU0OS0zODEyNjg3QjgyNTYiLCJzdWIiOiJiNzI4MWJjMi0zMTEyLTQ5YTYtOTExMS05YjdiZTIyOTQ2NjQiLCJzaXRlX2lkIjoiNUFGRDIyMjItQjIwOC00RjIyLUEwOEUtQjg4OTNGQTNEMjIyMiIsIm9yaWdpbiI6InN0Zy52aXAuc2VsaXNlLmRldiIsInNlc3Npb25faWQiOiJzZWxpc2VibG9ja3MtOTdkNjZjOTYtZWI4NC00ZTQ4LWIyODgtNjc5MTg4Y2QyYmZmIiwidXNlcl9pZCI6ImI3MjgxYmMyLTMxMTItNDlhNi05MTExLTliN2JlMjI5NDY2NCIsImRpc3BsYXlfbmFtZSI6IlN1cGVyIEFkbWluaXN0cmF0b3IiLCJzaXRlX25hbWUiOiJFY2FwIFRlYW0iLCJ1c2VyX25hbWUiOiJzdXBlcmFkbWluQGJsb2Nrcy5jb20iLCJlbWFpbCI6InN1cGVyYWRtaW5AYmxvY2tzLmNvbSIsInBob25lX251bWJlciI6Iis4ODAxNzE3MzcyMzQ2IiwibGFuZ3VhZ2UiOiJlbiIsInVzZXJfbG9nZ2VkaW4iOiJUcnVlIiwibmFtZSI6ImI3MjgxYmMyLTMxMTItNDlhNi05MTExLTliN2JlMjI5NDY2NCIsInVzZXJfYXV0b19leHBpcmUiOiJGYWxzZSIsInVzZXJfZXhwaXJlX29uIjoiMDEvMDEvMDAwMSAwMDowMDowMCIsImlhdCI6MTc1MTUyNDA1MCwicm9sZSI6InN1cGVyX2FkbWluIiwibmJmIjoxNzUxNTI0MDUwLCJleHAiOjE3NTE1Mjc2NTAsImlzcyI6IkNOPUVudGVycHJpc2UgQ2xvdWQgQXBwbGljYXRpb24gUGxhdGZvcm0iLCJhdWQiOiIqIn0.KddSpJkBzu-jMu9p7J97UZHyb5tRpykMgfzXZke_Ma4BBta0unBsJGx8dVBESQ_aIhnVje1ig-QPC4jZGSqD8-Mi8nplndsQmDg3zVxWzv-meG9PqYh1VoHs2sbbJThig9041jLCMeZkEfw-U_5JLIRe6UMbnNTkG2ZGCVTyCa6o2pLUqRiFev-dAyGO5btSMjuWu5B5CO4nmXG5_5UX24bMnyoyBjgQEWTHe1bY5HyUUN4aYQkbaA9q_04hJxYkUV2N6LX2QVhYNdowsMDG5HliPyTLCZ99ta50X-nZ9cRzlYWkYbRD33NMEiIUsaipMbzmrAENN-_aapHvF41tJg"
        auth_context = playwright.request.new_context(
            extra_http_headers= {
                "Authorization":f"Bearer {token}"
            }
        )

        payload ={
                "SapBomId": "0007e3cc-f8fc-44d5-b9dd-85e16cb93030",
                "CustomerId": "b2b0a636-cbf4-41b7-9014-a6bfd77e0827",
                "CurrencyId": "0da2a985-8601-471c-849e-e1af00f7c3f3",
                "ProcurementStrategies": [
                    {
                        "OrderQuantity": 1,
                        "StrategyId": "6d69421f-aab1-44bb-98d1-e13bb1a09424"
                    }
                ]
            }
        post_url = "https://stg.vip.selise.dev/api/business-variosystems/CreateProjectFromSapBom"
        post_data = auth_context.post(post_url,data=payload) # Here after auth_context we need to use GET/POST/PUT/PATCH/DELETE

        assert post_data.ok, f"Failed with Status: {post_data.status}"
        print("POST Status: ", post_data.status)
        print("Post Data: ", post_data.json())
