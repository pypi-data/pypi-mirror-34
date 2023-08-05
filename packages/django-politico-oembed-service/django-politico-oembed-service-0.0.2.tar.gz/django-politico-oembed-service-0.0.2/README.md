![POLITICO](https://rawgithub.com/The-Politico/src/master/images/logo/badge.png)

# django-politico-oembed-service

### Quickstart

1. Install the app.

  ```
  $ pip install django-politico-oembed-service
  ```

2. Add the app to your Django project and configure settings.

  ```python
  INSTALLED_APPS = [
      # ...
      'rest_framework',
      'oembeder',
  ]

  #########################
  # oembeder settings

  OEMBEDSERVICE_API_AUTHENTICATION_CLASS = ''
  OEMBEDSERVICE_API_PERMISSION_CLASS = ''
  ```


### Services

##### Twitter

`twitter/`

```javascript
fetch('https://your-api.com/twitter/', {
  method: 'POST',
  headers: {
    Authorization: `Token ${YOUR_TOKEN}`, // or whatever auth strategy you use
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    url: 'https://twitter.com/someuser/sometweeturl/'
  })
})
.then(response => response.json())
.then(data => {
  console.log(data);
});
```

You may also pass values for the following params:

- `maxwidth`
- `hide_media`
- `hide_thread`
- `omit_script`
- `link_color`

See Twitter's [API docs](https://developer.twitter.com/en/docs/tweets/post-and-engage/api-reference/get-statuses-oembed.html) for valid values.


##### YouTube

`youtube/`

```javascript
fetch('https://your-api.com/youtube/', {
  method: 'POST',
  headers: {
    Authorization: `Token ${YOUR_TOKEN}`, // or whatever auth strategy you use
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    url: 'https://www.youtube.com/watch?v=V7uEb_XrK1U'
  })
})
.then(response => response.json())
.then(data => {
  console.log(data);
});
```
