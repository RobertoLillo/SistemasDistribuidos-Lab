# frozen_string_literal: true

require 'cassandra'

# Makes a connection to REDIS.
class CassandraConnector
  @cassandra = nil
  def self.get
    @cassandra = Cassandra.new('astro_keyspace', '127.0.0.1:9042')
    @cassandra
  end
end
