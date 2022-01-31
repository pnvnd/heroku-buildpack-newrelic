# Heroku Buildpack: New Relic
This buildpack is used to send deployment markers to New Relic.

## Requirements

This buildpack requires the `requests` library. Please add it to the `requirements.txt` file of your project.

You should also add the following two variables to Heroku `env` variables:

- `NEW_RELIC_APP_ID`: Go to the app in New Relic APM and get the AppId from the URL or click the "tag" icon to copy the AppId
- `NEW_RELIC_API_KEY`: This is the USER API key.  Create one if one does't exist.
- `DEPLOYER`: A name or email address to identify who did the deployment.  If blank, account number is used instead.

Finally, use Heroku CLI to enable `HEROKU_RELEASE_VERSION` environment variable by entering:  
`heroku labs:enable runtime-dyno-metadata -a <app name>`
