<https://azure.github.io/apim-lab/apim-lab/7-security/security-7-3-managed-identities.html>
https://medium.com/bb-tutorials-and-thoughts/configuring-auth-2-0-in-apim-for-python-apis-running-on-azure-functions-63d074744bcf
efc_backend_app
NX.8Q~jnAl_9sYQAWRphVPsv9QtBIwS~PuRAGdr~
37d5eb41-d3a7-4995-bb4b-29d4f9f2db2e

oauth_backend_app
M2g8Q~Pb6qs~M4Vmpz-bRTd85Mm5VQgRRFE5_b9p
c44d1417-c7a1-4668-a82c-f6f8901b282d


grant_type: client_credentials
client_id: 37d5eb41-d3a7-4995-bb4b-29d4f9f2db2e
client_secret: NX.8Q~jnAl_9sYQAWRphVPsv9QtBIwS~PuRAGdr~
resource: <https://graph.microsoft.com>

 <validate-jwt header-name="Authorization" failed-validation-httpcode="401" failed-validation-error-message="Unauthorized. Access token is missing or invalid.">
            <openid-config url="https://login.microsoftonline.com/7d5a8898-6564-4329-9289-c87046c026ef/v2.0/.well-known/openid-configuration" />
            <audiences>
                <audience>{audience-value - (ex:api://guid)}</audience>
            </audiences>
            <issuers>
                <issuer>{issuer-value - (ex: https://sts.windows.net/{tenant id}/)}</issuer>
            </issuers>
            <required-claims>
                <claim name="aud">
                    <value>37d5eb41-d3a7-4995-bb4b-29d4f9f2db2e</value>
                </claim>
            </required-claims>
        </validate-jwt>
