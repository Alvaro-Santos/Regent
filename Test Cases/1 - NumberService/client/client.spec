Name: NumberServiceClient

Depends:
	from: NumberServiceServer
		@-protocol: http
		@-request-body: -
		@-reply-body: json

		at: /random?l={l}&u={u}
		type: (l: int, u: int) -> int
		$-errors: 400, 500
		$-method: GET

Defines:
-
