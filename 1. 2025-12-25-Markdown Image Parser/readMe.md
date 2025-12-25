# Markdown Image Parser

Given a string of an image in Markdown, return the equivalent HTML string.

A Markdown image has the following format: `"![alt text](image_url)"`.

Where:

- `alt text` is the description of the image(the `alt` attribute value).
- `image_url` is the source URL of the image(the `src` attribute value).

Return a string of the HTML `img` tag with the `src` set to the image URL and the `alt` set to the alt text.

For example, give `"![Cute boy](boy.png)"` return `'<img src="boy.png" alt="Cute boy">'`;

- Make sure the tag, order of attributes, spacing, and quote usage is the same as above.

