package modules

type Router struct {
	Handlers map[string]Command
}

func CreateRouter() Router {
	handlerMap := make(map[string]Command)

	handlerMap[CC.Type] = CC
	handlerMap[CF.Type] = CF
	handlerMap[DF.Type] = DF
	handlerMap[UF.Type] = UF
	return Router{
		Handlers: handlerMap,
	}
}
