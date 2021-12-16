# Heroku Buildpack: New Relic
This buildpack is used to send deployment markers to New Relic.

## Requirements

This buildpack requires the `requests` library. Please add it to the `requirements.txt` file of your project.

You should also add the following two variables to Heroku `env` variables:

- `NEW_RELIC_APP_ID`: You can find this in the url of the app on newrelic's website.
- `NEW_RELIC_API_KEY`: This is account wide, you can find it in newrelic's account settings.
- `DEPLOYER`: A name or email address to identify who did the deployment.  If blank, account number is used instead.

Finally, use Heroku CLI to enable `HEROKU_RELEASE_VERSION` environment variable by entering:  
`heroku labs:enable runtime-dyno-metadata -a <app name>`
