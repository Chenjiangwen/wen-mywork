package featureflags

type Featureflag struct {
	ID   string `json:"id" bson:"id"`
	Name string `json:"name" bson:"name"`
	IsOn bool   `json:"isOn" bson:"isOn"`
}

type Featureflags struct {
	ID           string        `json:"id" bson:"id"`
	Username     string        `json:"email" bson:"email"`
	Featureflags []Featureflag `json:"featureflags" bson:"featureflags"`
}

type featureflagRequestV1 struct {
	Id string `json:"id"`
}

type featureflagResponseV1 struct {
	Id     string `json:"id" bson:"_id"`
	Status bool   `json:"status"`
}

//eg: [{_id: "ffname:projectname:env", ffname:"aa", isOn:true}]
