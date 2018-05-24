angou\_poloniex 2 (May 24, 2018)
===
- `angou_poloniex.rest` now exposes a module-scoped `LOGGER` variable, instead of
  per-class `angou_poloniex.rest.RestSession.logger`s.
- If a response has a “success” HTTP status code but its body cannot be parsed
  as JSON, `angou_poloniex.rest.InvalidJSON` is raised.
- `angou_poloniex.rest.RestSession` constructor now takes an optional `timeout`
  argument.
- `angou_poloniex.rest.RestSession.request` was renamed to `call_auth`.
- New method `angou_poloniex.rest.RestSession.request.call_public`.

angou\_poloniex 1 (May 19, 2018)
===
The first release of angou\_poloniex!
