# frozen_string_literal: true

# Controller that connects to:
# - Redis to get the last night information.
# - Cassandra to get the historical nights infomarmation.
class NightController < ApplicationController
  before_action :cassandra_connect

  def historical_nb
    nearly_black = @cassandra[:nearly_black].to_json

    render json: nearly_black, status: :ok
  end

  def historical_s
    statistics = @cassandra[:statistics]
  end

  def cassandra_connect
    @cassandra = Util::CassandraConnector.get
  end
end
