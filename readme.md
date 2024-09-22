cloudmigrate.yaml is the only file that can be implemented on Google Cloud.

Currently Dockerfile is not working because of google cloud authentication.

- many setup are based on: https://cloud.google.com/python/django/run

Staging URL: https://imgogo-service-main-796017178582.us-central1.run.app

Production URL: https://imgogo-service-main-796017178582.us-central1.run.app

---

To setup cloudmigrate.yaml in Google Cloud go to:

Google Cloud Console >> Cloud Build >> Trigger >> Create Trigger

Substitution variables:

- _INSTANCE_NAME

- _REGION

- _SECRET_SETTINGS_NAME

- _SERVICE_NAME

Please noted that "_SECRET_SETTINGS_NAME" is the secrets that was set based on: "https://cloud.google.com/python/django/run"
