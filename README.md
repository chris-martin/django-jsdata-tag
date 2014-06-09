# Django `jsdata` tag

## Example

Let the Django template context contain the value `status = { 'user': 'Alice' }`.

This line in the template:

```
{{ status | jsobject:'initialStatus' }}
```

produces this HTML:

```html
<script id="initialStatus-json" type="application/json">
{
    &quot;a&quot;: &quot;Alice&quot;
}
</script>

<script type="text/javascript">
    var script = document.getElementById('initialStatus-json');
    var div = document.createElement('div');
    div.innerHTML = script.innerHTML;
    var text = div.textContent || div.innerText;
    window['initialStatus'] = JSON.parse(text);
</script>
```

Which is functionally equivalent to:

```js
window.initialStatus = { 'user': 'Alice' };
```
