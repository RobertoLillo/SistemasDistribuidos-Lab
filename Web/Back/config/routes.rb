# frozen_string_literal: true

Rails.application.routes.draw do
  resources :night do
    member do
      get :historical_nb
      get :historical_s
    end
  end
end
