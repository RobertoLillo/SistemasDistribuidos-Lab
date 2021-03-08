# frozen_string_literal: true

require 'redis'

# Makes a connection to REDIS.
class RedisConnector
  @redis = nil
  def self.get
    @redis = Redis.new(url: ENV['REDIS_URL']) if @redis.nil?
    @redis
  end
end
