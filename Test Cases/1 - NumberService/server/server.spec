Name: NumberServiceServer

Depends:
-

Defines:
	@-protocol: http
	@-request-body: -
	@-reply-body: json

	at: /random?l={l}&u={u}
	type: (l: int, u: int) -> int
	$-errors: 400, 500
	$-method: GET
