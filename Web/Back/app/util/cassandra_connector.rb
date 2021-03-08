# frozen_string_literal: true

require 'cassandra'

# Makes a connection to REDIS.
class CassandraConnector
  @cassandra = nil
  def self.get
    @cassandra = Cassandra.cluster(
                  username: ENV['DB_USER'],
                  password: ENV['DB_PASSWORD'],
                  hosts: ENV['CASSANDRA_URL']
                )
    @cassandra
  end
end
