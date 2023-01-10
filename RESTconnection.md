## Values for setting up connection in Azure Data factory ingest.

### Source
 - Source Type: REST
 - Connection:
    - BaseURL: https://api.spotify.com/v1
    - Authentication Type: OAuth2
    - Token Endpoint: https://accounts.spotify.com/api/token
    - scope: user-read-recently-played
 - Relative URL: https://api.spotify.com/v1/me/player/recently-played
 - Request method: GET
 
 Welp, I'm getting a 500 error.
