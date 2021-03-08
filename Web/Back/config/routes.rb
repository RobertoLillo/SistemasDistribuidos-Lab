# frozen_string_literal: true

Rails.application.routes.draw do
  resources :night do
    member do
      get :last
      get :historical
    end
  end
end
