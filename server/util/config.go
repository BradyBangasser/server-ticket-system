package util

import (
	"encoding/json"
	"os"
)

func GetConfig() (*interface{}, error) {
	configBytes, err := os.ReadFile("./config.json")

	if err != nil {
		return nil, err
	}

	var config interface{}

	json.Unmarshal(configBytes, &config)

	return &config, nil
}