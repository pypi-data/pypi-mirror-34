var switchElem = element(by.css('[ng-switch]'));
var select = element(by.model('selection'));

it('should start in settings', function() {
  expect(switchElem.getText()).toMatch(/Settings Div/);
});
it('should change to home', function() {
  select.all(by.css('option')).get(1).click();
  expect(switchElem.getText()).toMatch(/Home Span/);
});
it('should change to settings via "options"', function() {
  select.all(by.css('option')).get(2).click();
  expect(switchElem.getText()).toMatch(/Settings Div/);
});
it('should select default', function() {
  select.all(by.css('option')).get(3).click();
  expect(switchElem.getText()).toMatch(/default/);
});