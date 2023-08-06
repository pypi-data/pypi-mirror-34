Django stars widget
===================

Description
-----------

This is a simple widget rendering so-called rating stars as input for an
integer field. It is based solely on CSS 3, as laid out by `Martin Ivanov
<http://experiments.wemakesites.net/css3-rating-stars-with-selection.html>`_.

Usage
-----

Just add the Stars widget to any IntegerField in a Django form.

.. code:: python

  from django import forms
  from django_starfield import Stars

  class StarsExampleForm(forms.Form):
      rating = forms.IntegerField(widget=Stars)

The following aspects are configurable, both in the Django settings and when
creating the widget (by passing an argument to Stars):

+------------------------+-----------------------+---------+---------------------+-----------+
| Aspect                 | Format                | Default | Setting name        | Argument  |
+========================+=======================+=========+=====================+===========+
| Number of stars        | integer               | 5       | STARFIELD_STARS     | stars     |
+------------------------+-----------------------+---------+---------------------+-----------+
| Character used as star | hexadecimal codepoint | 2605    | STARFIELD_CODEPOINT | codepoint |
+------------------------+-----------------------+---------+---------------------+-----------+
| Colour of stars        | HTML colour           | #f5b301 | STARFIELD_COLOUR    | colour    |
+------------------------+-----------------------+---------+---------------------+-----------+

Please note that some browsers render some Unicode characters, especially
emojis, as images, so changing the font colour will not work.

Differences
-----------

This is different from other star rating applications in that it provides
only a widget returning its selction to any IntegerField. It is not a
complete rating application, just a presentational widget for integer input.
It is also different in that it depends only on CSS3, without any
JavaScript.
