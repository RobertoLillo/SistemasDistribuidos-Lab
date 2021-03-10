# frozen_string_literal: true

# Makes a connection to REDIS.
class CassandraConnector
  @cassandra = nil
  def self.get
    @cassandra = Cequel.connect(
                  :host => '127.0.0.1:9042',
                  :keyspace => 'astro_keyspace'
                )
    @cassandra
  end
end
